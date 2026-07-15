/**
 * 2009-cn-047 图片还原脚本
 *
 * 问题：SVG 已通过 <switch>+<foreignObject> 包含所有文字标签，
 *       但 Markdown 中重复列出了这些文字标签（DOCX 转换残留）
 *
 * 处理：
 * 1. 验证 SVG 已包含所有关键标签
 * 2. 删除 Markdown 中 SVG 引用后的重复文字标签区域
 * 3. 保留题目正文和答案区域
 */

const fs = require('fs');

const SVG_PATH = 'E:/programcc408/cc408/static/images/questions/2009_Q47_9.svg';
const MD_PATH = 'E:/programcc408/cc408/content/question/2009-cn-047.md';

// 1. 验证 SVG 已包含所有标签
const svg = fs.readFileSync(SVG_PATH, 'utf8');
const fos = [...svg.matchAll(/<foreignobject[^>]*>([\s\S]*?)<\/foreignobject>/gi)];
const allTexts = [];
for (const fo of fos) {
  const textMatches = [...fo[1].matchAll(/(?:<div[^>]*>|<span[^>]*>|<font[^>]*>)([^<]{2,})<\//g)];
  for (const t of textMatches) {
    const clean = t[1].trim().replace(/\s+/g, ' ');
    if (clean.length > 0) allTexts.push(clean);
  }
}

const keyLabels = ['互联网', '局域网1', '局域网2', 'R1', 'R2', 'L0', 'E1', 'E2', 'E0', '202.118.2.1', '202.118.2.2', '202.118.3.1', '202.118.3.2', '域名服务器'];
const missing = keyLabels.filter(l => !allTexts.some(t => t.includes(l)));

if (missing.length > 0) {
  console.error('❌ SVG 缺少标签:', missing);
  console.error('请先生成包含所有标签的 SVG');
  process.exit(1);
}

console.log('✅ SVG 验证通过，所有标签已包含');

// 2. 读取 Markdown
let md = fs.readFileSync(MD_PATH, 'utf8');
const lines = md.split('\n');

// 找到 SVG 引用行和 [tag_link] 之间的文字标签区域
const svgLineIdx = lines.findIndex(l => l.includes('2009_Q47_9.svg'));
const tagLinkIdx = lines.findIndex(l => l.trim() === '[tag_link]');

if (svgLineIdx === -1 || tagLinkIdx === -1) {
  console.error('❌ 未找到 SVG 引用或 [tag_link]');
  process.exit(1);
}

// 要删除的文字标签行列表（这些在 SVG 中已存在）
const redundantLabels = [
  '互联网', 'E1', '局域网1', 'R2', 'LO', 'L1',
  /\n?\[130\\?\.11\\?\.120\\?\.1\]\(130\\?\.11\\?\.120\\?\.1\)/,
  'E0',
  /\n?\[202\\?\.118\\?\.3\\?\.1\]\(202\\?\.118\\?\.3\\?\.1\) 域名服务器/,
  /\n?\[202\\?\.118\\?\.3\\?\.2\]\(202\\?\.118\\?\.3\\?\.2\)/,
  /\n?\[202\\?\.118\\?\.2\\?\.1\]\(202\\?\.118\\?\.2\\?\.1\) LO/,
  /\n?\[202\\?\.118\\?\.2\\?\.2\]\(202\\?\.118\\?\.2\\?\.2\)/,
  '局域网2', 'R1', 'E1'
];

// 标记要删除的行范围：从 SVG 行之后到第一个非标签的行
let deleteStart = svgLineIdx + 1;  // SVG 下一行开始删
let deleteEnd = tagLinkIdx - 1;    // 删到 tag_link 前

// 确认删除区域内的行都是标签行（不是题目正文）
const labelsAfterSvg = lines.slice(deleteStart, tagLinkIdx);
let firstNonLabel = -1;
for (let i = 0; i < labelsAfterSvg.length; i++) {
  const line = labelsAfterSvg[i].trim();
  const isLabel = redundantLabels.some(label => {
    if (typeof label === 'string') return line === label;
    if (label instanceof RegExp) return label.test(line);
    return false;
  });
  if (!isLabel && line !== '' && !line.startsWith('[')) {
    firstNonLabel = i;
    break;
  }
}

// 只删除标签区域（不是所有行）
if (firstNonLabel > 0) {
  deleteEnd = deleteStart + firstNonLabel - 1;
}

// 构建新内容：跳过要删除的行
const newLines = [
  ...lines.slice(0, deleteStart),
  ...lines.slice(deleteEnd + 1)
];

md = newLines.join('\n');

// 3. 写入
fs.writeFileSync(MD_PATH, md, 'utf8');
console.log(`✅ 已从 Markdown 中删除 ${deleteEnd - deleteStart + 1} 行重复文字标签`);
console.log('   保留 SVG 引用和题目正文');
