/**
 * 经验复用 tasks/408-crawler/crawler.js：Node https GET -> 解析隐藏 div
 * 目标：爬取 2009 年第 43 题（综合应用题），输出 markdown 表格
 */
const https = require('https');
const fs = require('fs');

function fetch(url) {
  return new Promise((resolve, reject) => {
    https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' } }, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => resolve(data));
    }).on('error', e => reject(e));
  });
}

function stripTags(html) {
  return html
    .replace(/<svg[\s\S]*?<\/svg>/g, ' [图片] ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/\s+/g, ' ')
    .trim();
}

function escapeCell(s) {
  // markdown 表格里把换行和管道转义
  return s.replace(/\|/g, '\\|').replace(/\r?\n/g, ' ').trim();
}

(async () => {
  const html = await fetch('https://www.csgraduates.com/study_methods/408quiz/2009/');

  // 1) 定位 <h5 id=43> 综合题标题
  const h5idx = html.search(/<h5\s+id=43(\s|>)/i);
  if (h5idx === -1) { console.error('未找到 #43'); process.exit(1); }
  const rest = html.substring(h5idx);
  const nextH5 = rest.indexOf('<h5', 10);
  const chunk = nextH5 === -1 ? rest : rest.substring(0, nextH5);

  // 2) 题干：answer-container 之前的所有 <p> 文本
  const ansIdx = chunk.indexOf('answer-container');
  const qPart = ansIdx === -1 ? chunk : chunk.substring(0, ansIdx);
  const qParas = [...qPart.matchAll(/<p[^>]*>([\s\S]*?)<\/p>/g)].map(m => stripTags(m[1]));
  const stem = qParas[0] || '';
  const subs = qParas.slice(1).filter(p => p.trim());

  // 3) 解析：solution-detail 内 <p> 文本
  const solMatch = chunk.match(/<div class="solution-detail[^>]*>([\s\S]*?)<\/div>/i);
  let solText = '';
  if (solMatch) {
    const inner = solMatch[1] || '';
    const solParas = [...inner.matchAll(/<p[^>]*>([\s\S]*?)<\/p>/g)].map(m => stripTags(m[1]));
    solText = solParas.join(' ');
  }

  // 4) 拆解答疑：(1)(2) 与 解析 1）2）
  const ans1 = subs[0] || '';
  const ans2 = subs[1] || '';
  const solParts = solText.split(/（\d+ 分）|（\d+分）/).map(s => s.trim()).filter(Boolean);
  const solBody = solText;

  // 5) 组装 markdown 表格
  const rows = [
    ['题号', '43'],
    ['科目', '计算机组成原理'],
    ['题型', '综合应用题（8 分）'],
    ['题干', stem],
    ['问题 (1)', ans1],
    ['问题 (2)', ans2],
    ['解析', solBody],
  ];
  let md = '# 2009 年第 43 题（爬取自 csgraduates）\n\n';
  md += '| 项目 | 内容 |\n';
  md += '|------|------|\n';
  for (const [k, v] of rows) {
    md += `| ${k} | ${escapeCell(v)} |\n`;
  }
  md += '\n> 来源: https://www.csgraduates.com/study_methods/408quiz/2009/#43\n';

  fs.writeFileSync('E:/programcc408/cc408/scripts/_tmp_q43.md', md, 'utf8');
  console.error('已写出 markdown 表格 -> scripts/_tmp_q43.md');
})().catch(e => console.error('ERR', e.message));
