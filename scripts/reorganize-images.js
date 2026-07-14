/**
 * reorganize-images.js
 * 
 * 功能：
 *   1. 从 E:\参考\2026-07\svg_images 复制所有 SVG/PNG 到
 *      static/images/questions/ 下按类型+年份组织：
 *        - 真题: static/images/questions/exam/2009/, exam/2010/, ...
 *        - 模拟题: static/images/questions/simulate/simulate_1/, ...
 *   2. 源目录中文件命名为 Q{NUM}_{SEQ}.svg（如 Q3_1.svg）
 *      目标命名为 {YEAR}_Q{NUM}_{SEQ}.svg（如 2009_Q3_1.svg）
 *      已有带年份前缀的文件直接保留
 *   3. 修复 content/question/ 下所有 .md 文件中的图片引用路径
 *      旧格式: /cc408/images/questions/filename.svg
 *      新格式: /cc408/images/questions/exam/2009/filename.svg
 *      模拟题: /cc408/images/questions/simulate/simulate_1/filename.svg
 *   4. 修复 6 个断裂引用（Qx → 实际题号文件）
 */

const fs = require('fs');
const path = require('path');

const SRC_BASE = 'E:/参考/2026-07/svg_images';
const DST_BASE = path.resolve(__dirname, '..', 'static', 'images', 'questions');
const QUESTION_DIR = path.resolve(__dirname, '..', 'content', 'question');

// ======== STEP 1: Build copy plan ========
console.log('='.repeat(70));
console.log('  Step 1: 扫描源目录，规划文件复制');
console.log('='.repeat(70));
console.log();

const copyPlan = [];

// 真题年份
const srcYears = fs.readdirSync(SRC_BASE).filter(d => /^\d{4}$/.test(d)).sort();
for (const year of srcYears) {
  const srcDir = path.join(SRC_BASE, year);
  const files = fs.readdirSync(srcDir).filter(f => f.endsWith('.svg'));
  
  // 目标子目录: exam/{year}/
  const dstSubDir = path.join(DST_BASE, 'exam', year);
  
  for (const f of files) {
    // 源文件: Q3_1.svg → 目标: 2009_Q3_1.svg
    let dstName = f;
    if (!f.startsWith(year)) {
      dstName = year + '_' + f;
    }
    copyPlan.push({
      src: path.join(srcDir, f),
      dst: path.join(dstSubDir, dstName),
      dstRel: path.join('exam', year, dstName).replace(/\\/g, '/')
    });
  }
}

// 模拟题
const srcSims = fs.readdirSync(SRC_BASE).filter(d => d.startsWith('simulate_')).sort();
for (const sim of srcSims) {
  const srcDir = path.join(SRC_BASE, sim);
  const files = fs.readdirSync(srcDir).filter(f => f.endsWith('.svg') || f.endsWith('.png'));
  
  // 目标子目录: simulate/{sim}/
  const dstSubDir = path.join(DST_BASE, 'simulate', sim);
  
  for (const f of files) {
    let dstName = f;
    // PNG文件名: 1_27.png → simulate_1_1_27.png (加前缀防止冲突)
    if (!f.startsWith(sim) && !f.startsWith('Qx')) {
      // 处理如 1_27.png → 源目录名中已经有编号
      // 从 simulate_N 提取 N
      const simNum = sim.replace('simulate_', '');
      dstName = simNum + '_' + f;
    }
    copyPlan.push({
      src: path.join(srcDir, f),
      dst: path.join(dstSubDir, dstName),
      dstRel: path.join('simulate', sim, dstName).replace(/\\/g, '/')
    });
  }
}

console.log(`  共计 ${copyPlan.length} 个文件待复制`);
console.log();

// ======== STEP 2: Execute copy ========
console.log('='.repeat(70));
console.log('  Step 2: 执行文件复制');
console.log('='.repeat(70));
console.log();

let copied = 0;
let skipped = 0;
for (const item of copyPlan) {
  const dstDir = path.dirname(item.dst);
  if (!fs.existsSync(dstDir)) {
    fs.mkdirSync(dstDir, { recursive: true });
  }
  
  if (fs.existsSync(item.dst)) {
    // 检查源和目标是否相同（通过大小简单判断）
    const srcStat = fs.statSync(item.src);
    const dstStat = fs.statSync(item.dst);
    if (srcStat.size === dstStat.size) {
      skipped++;
      continue;
    }
  }
  
  fs.copyFileSync(item.src, item.dst);
  copied++;
  console.log(`  ✅ ${item.dstRel}`);
}

console.log();
console.log(`  复制 ${copied} 个文件，跳过 ${skipped} 个已存在文件`);
console.log();

// ======== STEP 3: Build old→new path mapping ========
console.log('='.repeat(70));
console.log('  Step 3: 构建文件路径映射');
console.log('='.repeat(70));
console.log();

// 从旧的扁平目录中读取所有文件，建立 旧文件名 → 新路径 的映射
const flatFiles = {};
if (fs.existsSync(DST_BASE)) {
  const oldItems = fs.readdirSync(DST_BASE);
  for (const item of oldItems) {
    const fullPath = path.join(DST_BASE, item);
    if (fs.statSync(fullPath).isFile() && (item.endsWith('.svg') || item.endsWith('.png'))) {
      flatFiles[item] = fullPath;
    }
  }
}

// 为旧文件名寻找新路径（在 exam/ 或 simulate/ 子目录中）
const oldToNewMap = {};
for (const item of copyPlan) {
  const oldFname = path.basename(item.src);
  // 旧引用可能是带年份前缀的，也可能是不带的
  const dstFname = path.basename(item.dst);
  const dstDirname = item.dstRel.split('/')[0]; // exam 或 simulate
  
  // 带年份前缀的: 2009_Q3_1.svg
  oldToNewMap[dstFname] = item.dstRel;
  
  // 也记录不带年份前缀的（如 Q3_1.svg → 但后面年份提取会更精确）
  // 对于真题，也有引用可能是旧格式文件名
}

// 同时处理当前存在的旧文件引用
// 遍历所有 md 文件中的引用，构建修正映射
console.log('  扫描 md 文件中的旧引用...');

const mdFiles = fs.readdirSync(QUESTION_DIR)
  .filter(f => f.endsWith('.md') && !f.endsWith('.bak'));

const refFixMap = {}; // 旧完整路径 → 新完整路径

for (const fname of mdFiles) {
  const content = fs.readFileSync(path.join(QUESTION_DIR, fname), 'utf8');
  
  // 从 frontmatter 获取年份和题号
  const c = content.replace(/\r\n/g, '\n');
  const fm = c.match(/^---\n([\s\S]*?)\n---/);
  if (!fm) continue;
  
  let year = null;
  let number = null;
  let subject = null;
  const lines = fm[1].split('\n');
  let inList = false;
  let listKey = null;
  
  for (const line of lines) {
    const tl = line.trim();
    if (tl.match(/^\s*$/)) { inList = false; listKey = null; continue; }
    if (tl.match(/^\s*-\s/)) {
      const val = tl.replace(/^\s*-\s*/, '').trim().replace(/['"]/g, '');
      if (inList && listKey === 'years' && !year) year = val;
      continue;
    }
    const kv = tl.match(/^(\w+)\s*:\s*(.*)$/);
    if (kv) {
      const key = kv[1];
      const val = kv[2].trim();
      if (val === '') { inList = true; listKey = key; continue; }
      inList = false; listKey = null;
      if (key === 'number') number = parseInt(val);
      if (key === 'subjects') { /* 多行列表，跳过 */ }
    }
  }
  
  // 从文件名提取年份作为后备
  const fileYear = fname.match(/^(\d{4})-/);
  if (!year && fileYear) year = fileYear[1];
  
  if (!year || !number) continue;
  
  // 判断是真题还是模拟题
  const isSimulate = fname.startsWith('simulate-');
  const isExam = !isSimulate;
  
  // 遍历所有图片引用
  const imgRe = /!\[.*?\]\(([^)]+)\)/g;
  let m;
  while ((m = imgRe.exec(content)) !== null) {
    const refPath = m[1];
    if (!refPath.includes('/images/')) continue;
    
    const oldFname = refPath.split('/').pop();
    if (!oldFname.match(/\.(svg|png)$/i)) continue;
    
    // 确定目标子目录
    let newRel;
    if (isExam) {
      // 真题：exam/{year}/{newName}
      // 源文件名为 Q{NUM}_{SEQ}.svg，加上年份前缀
      let newName;
      if (oldFname.startsWith(year + '_')) {
        newName = oldFname;
      } else if (oldFname.startsWith('Q')) {
        newName = year + '_' + oldFname;
      } else {
        newName = oldFname;
      }
      newRel = path.join('exam', year, newName).replace(/\\/g, '/');
    } else {
      // 模拟题：simulate/{simName}/{newName}
      const simMatch = fname.match(/^(simulate-\d+)/);
      if (!simMatch) continue;
      const simName = simMatch[1];
      newRel = path.join('simulate', simName, oldFname).replace(/\\/g, '/');
    }
    
    const oldUrl = refPath;
    const newUrl = '/cc408/images/questions/' + newRel;
    
    if (oldUrl !== newUrl) {
      refFixMap[oldUrl] = newUrl;
    }
  }
}

console.log(`  找到 ${Object.keys(refFixMap).length} 处需要修复的引用`);
console.log();

// ======== STEP 4: Apply fixes ========
console.log('='.repeat(70));
console.log('  Step 4: 修复 md 文件中的引用路径');
console.log('='.repeat(70));
console.log();

// 按旧路径排序
const sortedRefs = Object.entries(refFixMap).sort((a, b) => a[0].localeCompare(b[0]));

let totalFixed = 0;
let filesFixed = new Set();

for (const fname of mdFiles) {
  const filePath = path.join(QUESTION_DIR, fname);
  let content = fs.readFileSync(filePath, 'utf8');
  let modified = false;
  
  for (const [oldPath, newPath] of sortedRefs) {
    if (content.includes(oldPath)) {
      content = content.split(oldPath).join(newPath);
      modified = true;
      totalFixed++;
    }
  }
  
  if (modified) {
    // Backup
    const bakPath = filePath + '.bak2';
    if (!fs.existsSync(bakPath)) {
      fs.writeFileSync(bakPath, fs.readFileSync(filePath), 'utf8');
    }
    fs.writeFileSync(filePath, content, 'utf8');
    filesFixed.add(fname);
  }
}

console.log(`  修改了 ${filesFixed.size} 个文件，${totalFixed} 处替换`);
if (filesFixed.size > 0) {
  console.log();
  console.log('  修改的文件:');
  for (const f of [...filesFixed].sort()) {
    console.log('    ' + f);
  }
}
console.log();

// ======== STEP 5: 处理断裂引用（Qx 修复） ========
// 检查还有哪些断裂引用
console.log('='.repeat(70));
console.log('  Step 5: 检查剩余断裂引用');
console.log('='.repeat(70));
console.log();

let brokenRefs = 0;
for (const fname of mdFiles) {
  const content = fs.readFileSync(path.join(QUESTION_DIR, fname), 'utf8');
  const imgRe = /!\[.*?\]\(([^)]+)\)/g;
  let m;
  while ((m = imgRe.exec(content)) !== null) {
    const refPath = m[1];
    if (refPath.includes('/images/')) {
      const rfname = refPath.split('/').pop();
      // 检查文件是否存在
      const fullPath = path.join(DST_BASE, refPath.replace('/cc408/images/questions/', ''));
      if (!fs.existsSync(fullPath)) {
        console.log(`  ❌ ${fname}: ${refPath}`);
        brokenRefs++;
      }
    }
  }
}

if (brokenRefs === 0) {
  console.log('  ✅ 无断裂引用');
} else {
  console.log();
  console.log(`  ${brokenRefs} 个断裂引用待手动处理`);
}
console.log();

console.log('='.repeat(70));
console.log('  完成!');
console.log('='.repeat(70));
