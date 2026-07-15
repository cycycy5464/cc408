/**
 * 批量修复SVG图片文字
 *
 * 1. 扫描所有 question markdown 文件中的 SVG 引用
 * 2. 对每个 SVG，将 foreignObject 文字转换为标准 <text> 元素
 * 3. 清理 Markdown 中重复的文字标签
 */

const fs = require('fs');
const path = require('path');
const glob = require('glob');

const QUESTION_DIR = 'E:/programcc408/cc408/content/question';
const SVG_DIR = 'E:/programcc408/cc408/static/images/questions';

/** 提取 SVG 中所有 foreignObject 内的文本 + 对应 image 坐标 */
function extractForeignObjectTexts(svgContent) {
  const switches = [...svgContent.matchAll(/<switch>([\s\S]*?)<\/switch>/gi)];
  const result = [];
  for (const sw of switches) {
    // 提取文本（div/span/font 内的非空文字）
    const textMatch = sw[1].match(/(?:<div[^>]*>|<span[^>]*>|<font[^>]*>)([^<]{2,})<\//);
    const text = textMatch ? textMatch[1].trim() : '';
    if (!text) continue;

    // 提取 fallback image 坐标
    const imgMatch = sw[1].match(/<image[^>]*>/);
    if (!imgMatch) continue;
    const attrs = imgMatch[0];
    const xM = attrs.match(/x=["']?([\d.]+)/);
    const yM = attrs.match(/y=["']?([\d.]+)/);
    result.push({
      text,
      x: xM ? parseFloat(xM[1]) : 0,
      y: yM ? parseFloat(yM[1]) : 0
    });
  }
  return result;
}

/** 生成 SVG <text> 元素 */
function makeTextElements(labels) {
  return labels.map(l =>
    `<text x="${l.x}" y="${l.y + 20}" font-size="16" font-family="Helvetica,sans-serif" fill="#000">${l.text}</text>`
  ).join('\n');
}

/** 处理单个SVG文件：转换 foreignObject → text 元素 */
function fixSvgFile(svgPath) {
  let svg = fs.readFileSync(svgPath, 'utf8');

  // 检查是否还含有需要转换的 switch
  if (!svg.includes('<switch>')) return 0; // 已处理过

  const labels = extractForeignObjectTexts(svg);
  if (labels.length === 0) return 0;

  // 替换所有 switch 为 text 元素
  const switches = [...svg.matchAll(/<switch>([\s\S]*?)<\/switch>/gi)];
  for (const sw of switches) {
    const textMatch = sw[1].match(/(?:<div[^>]*>|<span[^>]*>|<font[^>]*>)([^<]{2,})<\//);
    const text = textMatch ? textMatch[1].trim() : '';
    if (!text) continue;

    const imgMatch = sw[1].match(/<image[^>]*>/);
    if (!imgMatch) continue;
    const attrs = imgMatch[0];
    const xM = attrs.match(/x=["']?([\d.]+)/);
    const yM = attrs.match(/y=["']?([\d.]+)/);
    if (!xM || !yM) continue;

    const x = parseFloat(xM[1]);
    const y = parseFloat(yM[1]);
    const textEl = `<text x="${x}" y="${y + 20}" font-size="16" font-family="Helvetica,sans-serif" fill="#000">${text}</text>`;
    svg = svg.replace(sw[0], textEl);
  }

  // 清理空的 g 标签
  svg = svg.replace(/<g><\/g>/g, '');
  svg = svg.replace(/<g\/>/g, '');

  fs.writeFileSync(svgPath, svg, 'utf8');
  return labels.length;
}

/** 提取Markdown中SVG引用后紧跟的文字标签行 */
function extractMdTextLabels(mdContent, svgFileName) {
  const lines = mdContent.split('\n');
  const svgIdx = lines.findIndex(l => l.includes(svgFileName));
  if (svgIdx === -1) return { start: -1, end: -1, labels: [] };

  // 从 SVG 下一行开始，到第一个非标签行（空行、标题、tag_link、题目正文）为止
  let endIdx = -1;
  const labels = [];
  for (let i = svgIdx + 1; i < lines.length; i++) {
    const line = lines[i].trim();
    if (!line || line === '---' || line.startsWith('#####') || line.startsWith('####') ||
        line.startsWith('[') || line.startsWith('R1') || line.startsWith('R2') ||
        line.startsWith('(') || line.startsWith('目的') || line.startsWith('接口') ||
        line.startsWith('子网') || line.startsWith('下一条') || line.startsWith('下一跳')) {
      endIdx = i;
      break;
    }
    if (line.length <= 40) { // 短文字行可能是标签
      labels.push(line);
      endIdx = i + 1;
    } else {
      endIdx = i;
      break;
    }
  }

  return { start: svgIdx + 1, end: endIdx, labels };
}

/** 处理单个Markdown文件：清除SVG后的重复文字 */
function fixMdFile(mdPath) {
  let md = fs.readFileSync(mdPath, 'utf8');

  // 找 SVG 引用
  const svgMatch = md.match(/!\[\]\(\/cc408\/images\/questions\/([\w-]+\.svg)\)/);
  if (!svgMatch) return null;

  const svgFileName = svgMatch[1];
  const svgPath = path.join(SVG_DIR, svgFileName);
  if (!fs.existsSync(svgPath)) {
    console.log(`  [跳过] SVG文件不存在: ${svgFileName}`);
    return null;
  }

  // 处理SVG文件
  const replaced = fixSvgFile(svgPath);

  // 获取SVG中的文字列表
  const svgContent = fs.readFileSync(svgPath, 'utf8');
  const svgTexts = [...svgContent.matchAll(/<text[^>]*>([^<]+)<\/text>/g)].map(m => m[1]);

  // 清理Markdown中重复的文字标签
  const result = extractMdTextLabels(md, svgFileName);
  if (result.start > 0 && result.end > result.start) {
    const labelSection = md.split('\n').slice(result.start, result.end);
    const cleaned = labelSection.filter(line => {
      const trimmed = line.trim();
      // 如果这行文字已经在SVG的text元素中，删除
      if (svgTexts.some(t => t.includes(trimmed) || trimmed.includes(t))) {
        return false;
      }
      return true;
    });

    if (cleaned.length < labelSection.length) {
      // 需要删除一些行
      const lines = md.split('\n');
      const newLines = [...lines.slice(0, result.start)];
      // 只保留未被SVG包含的行
      for (const line of cleaned) {
        newLines.push(line);
      }
      // 接上剩余部分
      for (let i = result.end; i < lines.length; i++) {
        newLines.push(lines[i]);
      }
      md = newLines.join('\n');
      fs.writeFileSync(mdPath, md, 'utf8');
      const removed = labelSection.length - cleaned.length;
      return { svg: svgFileName, textsReplaced: replaced, labelsRemoved: removed };
    }
  }

  if (replaced > 0) {
    return { svg: svgFileName, textsReplaced: replaced, labelsRemoved: 0 };
  }

  return null;
}

//======= 主函数 =======//
async function main() {
  console.log('批量修复SVG图片文字\n');

  // 读取所有 question md 文件
  const files = fs.readdirSync(QUESTION_DIR)
    .filter(f => f.endsWith('.md') && !f.endsWith('.bak'))
    .sort();

  let svgFixed = 0;
  let mdFixed = 0;
  let totalTexts = 0;
  let totalLabels = 0;

  for (const file of files) {
    const mdPath = path.join(QUESTION_DIR, file);
    process.stdout.write(file + '...');
    const result = fixMdFile(mdPath);
    if (result) {
      if (result.textsReplaced > 0) {
        svgFixed++;
        totalTexts += result.textsReplaced;
        process.stdout.write(` SVG:${result.textsReplaced}text`);
      }
      if (result.labelsRemoved > 0) {
        mdFixed++;
        totalLabels += result.labelsRemoved;
        process.stdout.write(` MD:${result.labelsRemoved}标签`);
      }
      console.log(' ✓');
    } else {
      console.log(' -');
    }
  }

  console.log(`\n======= 完成 =======`);
  console.log(`SVG文件修复: ${svgFixed} 个 (${totalTexts} 个文字标签转换)`);
  console.log(`Markdown清理: ${mdFixed} 个 (${totalLabels} 行重复标签删除)`);
  console.log(`未改动: ${files.length - svgFixed} 个（已处理或无SVG）`);
}

main().catch(e => console.error('错误:', e));
