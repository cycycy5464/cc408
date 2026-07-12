/**
 * 408真题答案解析爬虫
 * 爬取 csgraduates.com 上历年408真题的答案、解析、题干和选项
 *
 * 用法: node crawler.js [年份范围]
 *       例如: node crawler.js            # 爬取所有年份
 *             node crawler.js 2024       # 只爬2024年
 *             node crawler.js 2020 2025  # 爬2020-2025年
 *
 * 输出: crawled_data/{year}.json
 *       每个题包含: stem, options(选择题), answer, analysis(选择题解析), solution(综合题解析)
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

const ALL_YEARS = [];
for (let y = 2009; y <= 2026; y++) ALL_YEARS.push(y);

const BASE_URL = 'https://www.csgraduates.com';
const QUIZ_PATH = '/study_methods/408quiz';
const OUTPUT_DIR = path.join(__dirname, 'crawled_data');

/** 带重试的HTTPS GET请求 */
function fetch(url, retries = 3) {
  return new Promise((resolve, reject) => {
    const attempt = (n) => {
      https.get(url, res => {
        let data = '';
        res.on('data', c => data += c);
        res.on('end', () => {
          if (res.statusCode >= 400 && n > 0) {
            console.log(`  重试(${3-n}/3): ${url}`);
            return attempt(n - 1);
          }
          resolve(data);
        });
      }).on('error', e => {
        if (n > 0) setTimeout(() => attempt(n - 1), 2000);
        else reject(e);
      });
    };
    attempt(retries);
  });
}

/** 提取meta description中的选择题答案速对 */
function extractAnswerKey(html, year) {
  const metaMatch = html.match(/答案速对([^<]*)/);
  if (!metaMatch) {
    console.log(`  [警告] ${year}年: 未找到答案速对`);
    return {};
  }
  const text = metaMatch[1];
  const pairs = [...text.matchAll(/(\d+)\s*([A-D])/g)];
  const answers = {};
  pairs.forEach(([_, num, ans]) => { answers[num] = ans; });
  console.log(`  [答案] 已提取 ${Object.keys(answers).length} 道选择题答案`);
  return answers;
}

/**
 * 提取每个题的题干(stem)和选项(options)
 * 选择题(Q1-40): 题干在 <h5 id=N> 之后的 <p>，选项在 <choice-container> 内
 * 综合题(Q41-47): 题干在 <h5 id=N> 之后的多个 <p>，直到 answer-container 或 solution-detail
 */
function extractQuestions(html) {
  const questions = {};

  // 找所有题目标题 h5 id=N
  const h5Regex = /<h5\s+id=(\d+)>/g;
  let h5Match;

  // 先把所有题号的位置找出来
  const positions = [];
  while ((h5Match = h5Regex.exec(html)) !== null) {
    positions.push({
      num: parseInt(h5Match[1]),
      start: h5Match.index,
      h5End: h5Match.index + h5Match[0].length
    });
  }

  for (let i = 0; i < positions.length; i++) {
    const pos = positions[i];
    const num = pos.num;
    const nextStart = i + 1 < positions.length ? positions[i + 1].start : html.length;
    const sectionHtml = html.substring(pos.h5End, nextStart);

    if (num >= 1 && num <= 40) {
      // === 选择题 ===
      // 题干: 第一个 <p> 标签
      const stemMatch = sectionHtml.match(/<p>([\s\S]*?)<\/p>/);
      const stem = stemMatch ? cleanHtml(stemMatch[1]) : '';

      // 选项: choice-container 内的 choice-label + choice-text
      const options = {};
      const optRegex = /<span class=choice-label>([A-D])\.<\/span>\s*<span class=choice-text>([\s\S]*?)<\/span>/g;
      let optMatch;
      while ((optMatch = optRegex.exec(sectionHtml)) !== null) {
        options[optMatch[1]] = cleanHtml(optMatch[2]);
      }

      questions[num] = { stem, options };

    } else if (num >= 41 && num <= 47) {
      // === 综合题 ===
      // 题干: h5 之后的所有 <p>，直到 answer-container、solution-detail 或下一个 h5
      const stemEndMarkers = [
        '<div class="answer-container',
        '<div class="solution-detail',
        '<div class=answer-container',
        '<div class=solution-detail',
        '<div class="choice-container'  // For inline choice questions
      ];
      let stemEnd = sectionHtml.length;
      for (const marker of stemEndMarkers) {
        const p = sectionHtml.indexOf(marker);
        if (p !== -1 && p < stemEnd) stemEnd = p;
      }

      const stemSection = sectionHtml.substring(0, stemEnd);
      const stemRegex = /<p>([\s\S]*?)<\/p>/g;
      let sMatch;
      const stemParts = [];
      while ((sMatch = stemRegex.exec(stemSection)) !== null) {
        const text = cleanHtml(sMatch[1]);
        if (text) stemParts.push(text);
      }
      questions[num] = { stem: stemParts.join('\n\n'), options: {} };
    }
  }

  return questions;
}

/** 提取选择题解析 — 保留 KaTeX 原始格式 */
function extractChoiceExplanations(html) {
  const explanations = {};
  const regex = /id=explanation-(choice-[^-]+-(\d+))[^>]*>/g;
  let m;
  const positions = [];
  while ((m = regex.exec(html)) !== null) {
    positions.push({
      id: m[1], num: parseInt(m[2]),
      start: m.index, endOpenTag: m.index + m[0].length
    });
  }

  for (let i = 0; i < positions.length; i++) {
    const pos = positions[i];
    const contentStart = pos.endOpenTag;
    const afterContent = html.substring(contentStart);

    const endMarkers = ['</div></div><script', '</div></div><h5', '</div></div><div id='];
    let endPos = -1;
    for (const marker of endMarkers) {
      const p = afterContent.indexOf(marker);
      if (p !== -1) { if (endPos === -1 || p < endPos) endPos = p; }
    }
    if (endPos === -1) continue;

    const rawContent = afterContent.substring(0, endPos);
    const ansMatch = rawContent.match(/<span class=correct-answer-text>([A-D]+)<\/span>/);
    const answer = ansMatch ? ansMatch[1] : null;

    const analysis = rawContent
      .replace(/<strong>正确答案[^<]*<\/strong><br>/g, '')
      .replace(/<span class=correct-answer-text>[A-D]+<\/span>/g, '')
      .replace(/<br\s*\/?>/gi, '\n')
      .replace(/<strong>/g, '**').replace(/<\/strong>/g, '**')
      .replace(/<em>/g, '*').replace(/<\/em>/g, '*')
      .replace(/<code>/g, '`').replace(/<\/code>/g, '`')
      .replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&')
      .replace(/&lt;/g, '<').replace(/&gt;/g, '>')
      .replace(/​/g, '')
      .replace(/\n{3,}/g, '\n\n')
      .trim();

    explanations[pos.num] = { answer, analysis };
  }
  return explanations;
}

/** 提取综合题解析 — 保留 SVG/KaTeX 原始格式 */
function extractSolutionAnswers(html) {
  const solutions = {};
  const regex = /<div class="?solution-detail[^"]*"?[^>]*?id=solution-answer-[^-]+-(\d+)[^>]*>/g;
  let m;
  const positions = [];
  while ((m = regex.exec(html)) !== null) {
    positions.push({ num: parseInt(m[1]), start: m.index, contentStart: m.index + m[0].length });
  }

  for (let i = 0; i < positions.length; i++) {
    const pos = positions[i];
    const afterContent = html.substring(pos.contentStart);

    let endPos = -1;
    const p = afterContent.indexOf('</div></div>');
    if (p !== -1) endPos = p;
    if (endPos === -1) continue;

    const rawContent = afterContent.substring(0, endPos);
    let text = rawContent
      .replace(/<br\s*\/?>/gi, '\n')
      .replace(/<\/p>/gi, '\n')
      .replace(/<\/div>/gi, '\n')
      .replace(/<script[\s\S]*?<\/script>/gi, '')
      .replace(/<style[\s\S]*?<\/style>/gi, '')
      .replace(/<strong>/g, '**').replace(/<\/strong>/g, '**')
      .replace(/<em>/g, '*').replace(/<\/em>/g, '*')
      .replace(/<code>/g, '`').replace(/<\/code>/g, '`')
      .replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&')
      .replace(/&lt;/g, '<').replace(/&gt;/g, '>')
      .replace(/​/g, '')
      .replace(/\n{3,}/g, '\n\n')
      .trim();

    solutions[pos.num] = text;
  }
  return solutions;
}

/** 清理HTML文本 — 保留 KaTeX 原始格式 */
function cleanHtml(text) {
  // 保留原始 KaTeX 结构（不清理 katex 标签内的内容）
  return text
    .replace(/<code>/g, '`').replace(/<\/code>/g, '`')
    .replace(/<br\s*\/?>/gi, '\n')
    .replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<').replace(/&gt;/g, '>')
    .replace(/​/g, '')  // Zero-width space
    .replace(/\u200b/g, '') // Another zero-width space
    .replace(/\n{3,}/g, '\n\n')  // Collapse excessive newlines
    .trim();
}

/** 爬取单年份页面 */
async function crawlYear(year) {
  const url = `${BASE_URL}${QUIZ_PATH}/${year}/`;
  console.log(`\n====== 正在爬取 ${year} 年 ======`);
  console.log(`  URL: ${url}`);

  try {
    const html = await fetch(url);

    const answerKey = extractAnswerKey(html, year);
    const explanations = extractChoiceExplanations(html);
    const solutions = extractSolutionAnswers(html);
    const questions = extractQuestions(html);

    const explainCount = Object.keys(explanations).length;
    const solCount = Object.keys(solutions).length;
    const qCount = Object.keys(questions).length;
    console.log(`  [解析] 已提取 ${explainCount} 道选择题解析`);
    console.log(`  [综合] 已提取 ${solCount} 道综合题解析`);
    console.log(`  [题干] 已提取 ${qCount} 道题题干`);

    // 统计有选项的题数
    let optCount = 0;
    for (const q of Object.values(questions)) {
      if (q.options && Object.keys(q.options).length > 0) optCount++;
    }
    console.log(`  [选项] 已提取 ${optCount} 道题选项`);

    const result = {
      year,
      url,
      answers: answerKey,
      questions,
      explanations,
      solutions
    };

    return result;
  } catch (e) {
    console.error(`  [错误] 爬取 ${year} 年失败: ${e.message}`);
    return null;
  }
}

/** 保存结果到JSON文件 */
function saveResult(result) {
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }
  const filePath = path.join(OUTPUT_DIR, `${result.year}.json`);
  fs.writeFileSync(filePath, JSON.stringify(result, null, 2), 'utf8');
  console.log(`  [保存] ${filePath}`);
}

/** 保存汇总JSON */
function saveSummary(allResults) {
  const filePath = path.join(OUTPUT_DIR, 'all_years.json');
  fs.writeFileSync(filePath, JSON.stringify(allResults, null, 2), 'utf8');
  console.log(`\n[汇总] 已保存到 ${filePath}`);
}

async function main() {
  const args = process.argv.slice(2);
  let years;

  if (args.length === 0) {
    years = ALL_YEARS;
  } else if (args.length === 1 && !isNaN(args[0])) {
    years = [parseInt(args[0])];
  } else if (args.length === 2 && !isNaN(args[0]) && !isNaN(args[1])) {
    const start = parseInt(args[0]), end = parseInt(args[1]);
    years = [];
    for (let y = start; y <= end; y++) years.push(y);
  } else {
    console.error('用法: node crawler.js [起始年份] [结束年份]');
    process.exit(1);
  }

  console.log(`408真题答案解析爬虫 (题干+选项增强版)`);
  console.log(`目标: ${BASE_URL}${QUIZ_PATH}/`);
  console.log(`年份: ${years[0]} ~ ${years[years.length - 1]} (共${years.length}年)`);

  const allResults = {};
  for (const year of years) {
    const result = await crawlYear(year);
    if (result) {
      allResults[year] = result;
      saveResult(result);
    }
    await new Promise(r => setTimeout(r, 500));
  }

  saveSummary(allResults);
  console.log('\n======= 爬取完成 =======');
  console.log(`成功: ${Object.keys(allResults).length}/${years.length} 年`);
}

main().catch(e => console.error('爬虫异常:', e));
