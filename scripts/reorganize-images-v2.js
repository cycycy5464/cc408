/**
 * reorganize-images-v2.js
 * 
 * 基于源目录 E:\参考\2026-07\svg_images 的文件列表，
 * 按 年份+题号 精确匹配 md 文件中的图片引用。
 * 
 * 规则：
 *   1. 真题文件在 exam/{year}/ 下
 *   2. 模拟题文件在 simulate/{simName}/ 下
 *   3. 源文件 Q{NUM}_{SEQ}.svg → 目标 {YEAR}_Q{NUM}_{SEQ}.svg
 *   4. md 引用路径根据 frontmatter 中的 year + number 匹配
 *      如果在对应 exam/{year}/ 中有 Q{NUM}_* 文件，逐个插入
 *      替换旧的引用（包括已存在的精确匹配、Qx、错误序号等）
 */

const fs = require('fs');
const path = require('path');

const SRC_BASE = 'E:/参考/2026-07/svg_images';
const DST_BASE = path.resolve(__dirname, '..', 'static', 'images', 'questions');
const QUESTION_DIR = path.resolve(__dirname, '..', 'content', 'question');

// ======== 1. 计算所有源文件的真实列表（标准） ========
console.log('Step 1: 扫描源目录，构建标准文件索引');
console.log('='.repeat(70));

const srcIndex = {}; // { year_qnum: [ { seq, fname } ] }

// 真题
for (const year of fs.readdirSync(SRC_BASE).filter(d => /^\d{4}$/.test(d)).sort()) {
  for (const f of fs.readdirSync(path.join(SRC_BASE, year)).filter(f => f.endsWith('.svg'))) {
    const m = f.match(/^Q(\d+)_(\d+)\.svg$/);
    if (m) {
      const key = year + '_' + m[1]; // year_qnum
      if (!srcIndex[key]) srcIndex[key] = [];
      srcIndex[key].push({ seq: parseInt(m[2]), fname: year + '_' + f, srcFname: f });
    }
  }
}

// 模拟题
for (const sim of fs.readdirSync(SRC_BASE).filter(d => d.startsWith('simulate_')).sort()) {
  for (const f of fs.readdirSync(path.join(SRC_BASE, sim)).filter(f => f.endsWith('.svg') || f.endsWith('.png'))) {
    const dstDir = path.join(DST_BASE, 'simulate', sim);
    if (!fs.existsSync(dstDir)) fs.mkdirSync(dstDir, { recursive: true });
    const dstPath = path.join(dstDir, f);
    if (!fs.existsSync(dstPath)) {
      fs.copyFileSync(path.join(SRC_BASE, sim, f), dstPath);
    }
  }
}

// 确保 exam/ 目录下的文件已复制
for (const year of fs.readdirSync(SRC_BASE).filter(d => /^\d{4}$/.test(d)).sort()) {
  const srcDir = path.join(SRC_BASE, year);
  const dstDir = path.join(DST_BASE, 'exam', year);
  if (!fs.existsSync(dstDir)) fs.mkdirSync(dstDir, { recursive: true });
  for (const f of fs.readdirSync(srcDir).filter(f => f.endsWith('.svg'))) {
    const dstName = year + '_' + f;
    const srcPath = path.join(srcDir, f);
    const dstPath = path.join(dstDir, dstName);
    if (!fs.existsSync(dstPath)) {
      fs.copyFileSync(srcPath, dstPath);
    }
  }
}

console.log('  标准文件索引建立完毕，共 ' + Object.keys(srcIndex).length + ' 个题号条目');
console.log();

// ======== 2. 解析每个 md 文件 ========
console.log('Step 2: 解析 md 文件，修复引用');
console.log('='.repeat(70));

function parseFm(content) {
  const c = content.replace(/\r\n/g, '\n');
  const m = c.match(/^---\n([\s\S]*?)\n---/);
  if (!m) return { years: null, number: null };
  const lines = m[1].split('\n');
  const result = { years: [], number: null };
  let inList = false;
  let listKey = null;
  for (const l of lines) {
    const tl = l.trimEnd();
    if (tl.match(/^\s*$/)) { inList = false; listKey = null; continue; }
    if (tl.match(/^\s*-\s/)) {
      const val = tl.replace(/^\s*-\s*/, '').trim().replace(/['"]/g, '');
      if (inList && listKey === 'years') result.years.push(val);
      continue;
    }
    const kv = tl.match(/^(\w+)\s*:\s*(.*)$/);
    if (kv) {
      const key = kv[1];
      const val = kv[2].trim();
      if (val === '') { inList = true; listKey = key; continue; }
      inList = false; listKey = null;
      if (key === 'number') result.number = parseInt(val);
    }
  }
  return result;
}

const mdFiles = fs.readdirSync(QUESTION_DIR)
  .filter(f => f.endsWith('.md') && !f.endsWith('.bak') && !f.endsWith('.bak2'));

let totalFixed = 0;
let filesFixedCount = 0;
let brokenAfter = 0;

for (const fname of mdFiles.sort()) {
  const filePath = path.join(QUESTION_DIR, fname);
  const content = fs.readFileSync(filePath, 'utf8');
  const fm = parseFm(content);
  
  const targetYear = fm.years && fm.years.length > 0 ? fm.years[0] : fname.substring(0, 4);
  const targetNumber = fm.number;
  
  if (!targetNumber) continue; // 无法确定题号，跳过
  
  // 是真题还是模拟题？
  const isSimulate = fname.startsWith('simulate-');
  
  // 该题号在源目录中有哪些文件
  const key = targetYear + '_' + targetNumber;
  const srcFiles = srcIndex[key];
  
  if (!srcFiles || srcFiles.length === 0) {
    // 无对应源文件，检查是否有断裂引用
    const imgRe = /!\[.*?\]\(([^)]+)\)/g;
    let m;
    while ((m = imgRe.exec(content)) !== null) {
      const refPath = m[1];
      if (refPath.includes('/images/')) {
        const rfname = refPath.split('/').pop();
        const fullPath = path.join(DST_BASE, refPath.replace('/cc408/images/questions/', ''));
        if (!fs.existsSync(fullPath)) {
          console.log(`  ❌ ${fname}: ${refPath} (源目录中无 ${key} 文件)`);
          brokenAfter++;
        }
      }
    }
    continue;
  }
  
  // 按 seq 排序
  srcFiles.sort((a, b) => a.seq - b.seq);
  
  // 构建这个 md 文件应有的引用列表
  const expectedRefs = srcFiles.map(sf => 
    isSimulate 
      ? `/cc408/images/questions/simulate/${fname.match(/^(simulate-\d+)/)[1]}/${sf.fname}`
      : `/cc408/images/questions/exam/${targetYear}/${sf.fname}`
  );
  
  // 获取当前文件中的所有图片引用
  const imgRe = /!\[.*?\]\(([^)]+)\)/g;
  const currentRefs = [];
  while ((m = imgRe.exec(content)) !== null) {
    if (m[1].includes('/images/')) {
      currentRefs.push(m[1]);
    }
  }
  
  // 判断当前引用是否需要修复
  let newContent = content;
  let hasChanges = false;
  
  // 如果当前引用数 ≠ 期望引用数，或有不同路径
  const currentSet = new Set(currentRefs);
  const expectedSet = new Set(expectedRefs);
  
  // 检查差异
  const missingFromCurrent = [...expectedSet].filter(r => !currentSet.has(r));
  const extraInCurrent = [...currentSet].filter(r => !expectedSet.has(r) && r.startsWith('/cc408/images/questions/'));
  
  if (missingFromCurrent.length > 0 || extraInCurrent.length > 0) {
    // 需要修复：替换所有旧引用为新的引用列表
    // 先删除所有旧引用
    let tempContent = newContent;
    for (const oldRef of currentRefs) {
      // 只替换 /cc408/ 路径的
      if (oldRef.startsWith('/cc408/')) {
        tempContent = tempContent.split(oldRef).join('__DELETED_IMG__');
      }
    }
    
    // 按顺序插入新引用
    let modified = tempContent;
    let insertedCount = 0;
    
    // 找到第一个 __DELETED_IMG__ 位置，替换回去
    // 对于每个删除的占位符，我们按顺序替换为期望的引用
    for (const expectedRef of expectedRefs) {
      const idx = modified.indexOf('__DELETED_IMG__');
      if (idx !== -1) {
        // 替换为期望引用
        modified = modified.replace('__DELETED_IMG__', expectedRef);
        insertedCount++;
      } else {
        // 没有更多占位符了，追加到文件末尾的合适位置
        // 找到最后一个引用附近插入
      }
    }
    
    // 清理多余的 __DELETED_IMG__
    modified = modified.split('__DELETED_IMG__').join('');
    
    if (modified !== content) {
      // Backup
      const bakPath = filePath + '.v2bak';
      if (!fs.existsSync(bakPath)) {
        fs.writeFileSync(bakPath, content, 'utf8');
      }
      fs.writeFileSync(filePath, modified, 'utf8');
      newContent = modified;
      hasChanges = true;
      
      // 输出修改详情
      console.log(`  ✅ ${fname}:`);
      if (extraInCurrent.length > 0) {
        for (const r of extraInCurrent) console.log(`      删除: ${r}`);
      }
      for (const r of expectedRefs) console.log(`      插入: ${r}`);
      
      totalFixed += expectedRefs.length;
      filesFixedCount++;
    }
  }
}

console.log();
console.log(`  修改了 ${filesFixedCount} 个文件`);

// ======== 3. 最终检查 ========
console.log();
console.log('Step 3: 最终断裂引用检查');
console.log('='.repeat(70));

brokenAfter = 0;
for (const fname of mdFiles) {
  const content = fs.readFileSync(path.join(QUESTION_DIR, fname), 'utf8');
  const imgRe = /!\[.*?\]\(([^)]+)\)/g;
  let m;
  while ((m = imgRe.exec(content)) !== null) {
    const refPath = m[1];
    if (refPath.includes('/images/')) {
      const rfname = refPath.split('/').pop();
      const fullPath = path.join(DST_BASE, refPath.replace('/cc408/images/questions/', ''));
      if (!fs.existsSync(fullPath)) {
        console.log(`  ❌ ${fname}: ${refPath}`);
        brokenAfter++;
      }
    }
  }
}

if (brokenAfter === 0) {
  console.log('  ✅ 无断裂引用！');
} else {
  console.log(`  ${brokenAfter} 个断裂引用`);
}

console.log();
console.log('Done.');
