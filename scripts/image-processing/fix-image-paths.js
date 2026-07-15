/**
 * fix-image-paths.js
 * 
 * 扫描 content/question/ 下所有 .md 文件，修复图片引用指向。
 * 
 * 问题：很多图片引用指向了 Qx 文件（如 2012_Qx_4.svg），但根据题号（number）
 * 应该指向具体题号的文件（如 2012_Q44_12.svg）。
 * 
 * 工作流：
 *   1. 从 frontmatter 中提取年份（years）和题号（number）
 *   2. 对每个图片引用，如果当前路径不是精确匹配（指向 Qx 或不同题号的文件）：
 *      - 按 [年份]_Q[题号]_ 在 static/images/questions/ 下查找
 *      - 找到唯一匹配 → 替换
 *      - 找不到 → 警告保留
 *   3. 已有精确匹配且文件存在的 → 跳过
 */

const fs = require('fs');
const path = require('path');

const QUESTION_DIR = path.resolve(__dirname, '..', 'content', 'question');
const IMAGES_DIR = path.resolve(__dirname, '..', 'static', 'images', 'questions');

// ---- Build file index ----
const fileIndex = {};
if (fs.existsSync(IMAGES_DIR)) {
  const files = fs.readdirSync(IMAGES_DIR);
  files.forEach(f => {
    const m = f.match(/^(\d{4})_Q(\d+)_(\d+)\.(svg|png)$/i);
    if (m) {
      const key = m[1] + '_' + m[2];
      if (!fileIndex[key]) fileIndex[key] = [];
      fileIndex[key].push(f);
    }
  });
}

// ---- Parse YAML frontmatter ----
function parseFrontmatter(rawContent) {
  // Normalize \r\n to \n for Windows line endings
  const content = rawContent.replace(/\r\n/g, '\n');
  const m = content.match(/^---\s*\n([\s\S]*?)\n---/);
  if (!m) return { years: null, number: null };
  
  const lines = m[1].split('\n');
  const result = { years: null, number: null };
  let inList = false;
  let listKey = null;
  
  for (const rawLine of lines) {
    const line = rawLine.trimEnd();
    
    // Empty line ends any list context
    if (line.match(/^\s*$/)) { inList = false; listKey = null; continue; }
    
    // List item (dash prefix)
    if (line.match(/^\s*-\s/)) {
      const val = line.replace(/^\s*-\s*/, '').trim().replace(/['"]/g, '');
      if (inList && listKey) {
        if (!result[listKey]) result[listKey] = [];
        result[listKey].push(val);
      }
      continue;
    }
    
    // Key-value line
    const kv = line.match(/^(\w+)\s*:\s*(.*)$/);
    if (kv) {
      const key = kv[1];
      let val = kv[2].trim();
      inList = false;
      listKey = null;
      
      if (val === '') {
        // Start of list
        inList = true;
        listKey = key;
        if (key === 'years') result.years = [];
        continue;
      }
      
      // Remove quotes
      if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
        val = val.slice(1, -1);
      }
      
      if (key === 'number') {
        result.number = parseInt(val);
      }
    }
  }
  
  return result;
}

// ---- Get year from filename ----
function getYearFromFilename(fname) {
  const m = fname.match(/^(\d{4})-/);
  return m ? m[1] : null;
}

function getFileBasename(refPath) {
  return refPath.split('/').pop();
}

function isExactMatchFile(fname) {
  return fname.match(/^\d{4}_Q\d+_\d+\.(svg|png)$/i) !== null;
}

function isQxFile(fname) {
  return fname.match(/^\d{4}_Qx_\d+\.(svg|png)$/i) !== null;
}

function fileExists(fname) {
  return fs.existsSync(path.join(IMAGES_DIR, fname));
}

// ---- Process ----
console.log('='.repeat(70));
console.log('  Fixing image reference paths in content/question/');
console.log('='.repeat(70));
console.log();

const mdFiles = [];
const entries = fs.readdirSync(QUESTION_DIR, { withFileTypes: true });
for (const entry of entries) {
  if (entry.isFile() && entry.name.endsWith('.md') && !entry.name.endsWith('.bak')) {
    mdFiles.push({ name: entry.name, fullPath: path.join(QUESTION_DIR, entry.name) });
  }
}

let totalReplacements = 0;
let totalFilesModified = 0;
const unmatched = [];

for (const { name: fname, fullPath: filePath } of mdFiles) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const fm = parseFrontmatter(content);
  const yearFromFile = getYearFromFilename(fname);
  
  // Get target year
  let targetYear = null;
  if (fm.years && fm.years.length > 0) {
    targetYear = fm.years[0];
  } else if (yearFromFile) {
    targetYear = yearFromFile;
  }
  const targetNumber = fm.number;
  
  if (!targetYear || !targetNumber) {
    continue; // Can't determine target
  }

  const targetKey = targetYear + '_' + targetNumber;
  const expectedFname = fileIndex[targetKey];

  const imgRe = /!\[.*?\]\(([^)]+)\)/g;
  const fileReplacements = [];
  
  let match;
  while ((match = imgRe.exec(content)) !== null) {
    const refPath = match[1];
    
    // Only handle paths under /cc408/images/questions/ or /images/
    let refFname = null;
    if (refPath.startsWith('/cc408/images/questions/')) {
      refFname = refPath.replace('/cc408/images/questions/', '');
    } else if (refPath.startsWith('/images/questions/')) {
      refFname = refPath.replace('/images/questions/', '');
    } else if (refPath.startsWith('/images/')) {
      // Extract filename from /images/.../fname
      refFname = refPath.split('/').pop();
    }
    
    if (!refFname) continue;
    
    // If it's already an exact match (not Qx) and file exists -> skip
    if (isExactMatchFile(refFname) && fileExists(refFname)) {
      continue;
    }
    
    // Try to find the correct file
    if (expectedFname) {
      if (expectedFname.length === 1) {
        const newPath = '/cc408/images/questions/' + expectedFname[0];
        if (refPath !== newPath) {
          fileReplacements.push({ from: refPath, to: newPath, oldFname: refFname });
        }
      } else {
        unmatched.push({ file: fname, ref: refPath, reason: `Multiple candidates for ${targetKey}: ${expectedFname.join(', ')}` });
      }
    } else {
      // Check if Qx file has seq matching targetNumber
      const qxMatch = refFname.match(/^(\d{4})_Qx_(\d+)\.(svg|png)$/);
      if (qxMatch && qxMatch[2] === String(targetNumber)) {
        // Qx seq matches targetNumber, might be intentional - warn but don't replace
        unmatched.push({ file: fname, ref: refPath, reason: `No exact match for ${targetKey}, Qx seq matches targetNumber though` });
      } else {
        unmatched.push({ file: fname, ref: refPath, reason: `No exact match for ${targetKey}` });
      }
    }
  }
  
  if (fileReplacements.length > 0) {
    let modified = content;
    for (const r of fileReplacements) {
      modified = modified.split(r.from).join(r.to);
    }
    // Backup
    const bakPath = filePath + '.bak';
    if (!fs.existsSync(bakPath)) {
      fs.writeFileSync(bakPath, content, 'utf-8');
    }
    fs.writeFileSync(filePath, modified, 'utf-8');
    
    console.log(`  ✅ ${fname}: ${fileReplacements.length} replacement(s)`);
    for (const r of fileReplacements) {
      console.log(`       ${r.from}  →  ${r.to}`);
    }
    totalReplacements += fileReplacements.length;
    totalFilesModified++;
  }
}

console.log();
console.log('='.repeat(70));
console.log(`  Summary: ${totalFilesModified} files modified, ${totalReplacements} replacements done.`);
console.log();

if (unmatched.length > 0) {
  console.log('--- Cannot auto-fix (no exact match in static/images/questions/) ---');
  const seen = new Set();
  for (const u of unmatched) {
    const key = u.file + '|' + u.ref;
    if (!seen.has(key)) {
      seen.add(key);
      console.log(`  ${u.file}: ${u.ref}`);
      console.log(`    ${u.reason}`);
    }
  }
}

// Final scan
console.log();
console.log('--- Final scan ---');
let imgCount = 0;
let exactCount = 0;
let qxCount = 0;
let brokenCount = 0;

for (const { name: fname, fullPath: filePath } of mdFiles) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const imgRe = /!\[.*?\]\(([^)]+)\)/g;
  let m;
  while ((m = imgRe.exec(content)) !== null) {
    const refPath = m[1];
    if (refPath.includes('/images/')) {
      imgCount++;
      const rfname = refPath.split('/').pop();
      const fullImgPath = path.join(IMAGES_DIR, rfname);
      if (fs.existsSync(fullImgPath)) {
        if (rfname.includes('_Qx_')) {
          qxCount++;
        } else {
          exactCount++;
        }
      } else {
        console.warn(`  ❌ ${fname}: ${refPath} (file not found!)`);
        brokenCount++;
      }
    }
  }
}

console.log(`  Total image refs: ${imgCount}`);
console.log(`  Exact match (non-Qx): ${exactCount}`);
console.log(`  Qx fallback: ${qxCount}`);
console.log(`  Broken (file not found): ${brokenCount}`);
console.log();
console.log('Done.');
