/**
 * 408真题答案解析爬虫
 * 爬取 csgraduates.com 上历年408真题的答案和解析
 *
 * author: 37648
 * 用法: node crawler.js [年份范围]
 *       例如: node crawler.js            # 爬取所有年份
 *             node crawler.js 2024       # 只爬2024年
 *             node crawler.js 2020 2025  # 爬2020-2025年
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

// 年份列表
const ALL_YEARS = [];
for (let y = 2009; y <= 2026; y++) ALL_YEARS.push(y);

//======= 配置 =======//
const BASE_URL = 'https://www.csgraduates.com';
const QUIZ_PATH = '/study_methods/408quiz';
const OUTPUT_DIR = path.join(__dirname, 'crawled_data');

//======= 工具函数 =======//

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
  // 从meta description中提取 "1 B 2 C 3 D ..." 模式的答案
  const metaMatch = html.match(/答案速对([^<]*)/);
  if (!metaMatch) {
    console.log(`  [警告] ${year}年: 未找到答案速对`);
    return {};
  }

  const text = metaMatch[1];
  const pairs = [...text.matchAll(/(\d+)\s*([A-D])/g)];
  const answers = {};
  pairs.forEach(([_, num, ans]) => {
    answers[num] = ans;
  });

  console.log(`  [答案] 已提取 ${Object.keys(answers).length} 道选择题答案`);
  return answers;
}

/** 提取HTML标签间的内容，处理嵌套 */
function extractBetweenTags(html, openTag, closeTag) {
  let depth = 0;
  let result = '';
  let collecting = false;
  let i = 0;

  while (i < html.length) {
    if (html.substring(i, i + openTag.length) === openTag) {
      depth++;
      if (!collecting) {
        collecting = true;
        result = '';
      }
      i += openTag.length;
    } else if (html.substring(i, i + closeTag.length) === closeTag) {
      depth--;
      i += closeTag.length;
      if (depth === 0 && collecting) {
        return result;
      }
    } else if (collecting) {
      result += html[i];
      i++;
    } else {
      i++;
    }
  }
  return null;
}

/** 提取选择题解析 (explanation-choice-XXX-N) */
function extractChoiceExplanations(html) {
  const explanations = {};

  // 匹配 explanation 区域
  const pattern = /id=explanation-([^"']+)-(\d+)["'][^>]*>/g;
  let match;
  const segments = [];

  while ((match = pattern.exec(html)) !== null) {
    const prefix = match[1];  // 如 "choice-" 后带UUID前缀
    // 其实 match[1] 包含了 "choice-" + UUID，但这里我们只关心题号
    // 题号在 match[2] 中
    // 我们需要找到这个div的结束位置
  }

  // 更稳健的方法: 直接搜 id=explanation-choice- 模式
  const regex = /id=explanation-(choice-[^-]+-(\d+))[^>]*>/g;
  let m;
  const positions = [];
  while ((m = regex.exec(html)) !== null) {
    positions.push({
      id: m[1],
      num: parseInt(m[2]),
      start: m.index,
      endOpenTag: m.index + m[0].length
    });
  }

  // 对每个找到的解释区域，提取内容到下一个解释区域或脚本标签前
  for (let i = 0; i < positions.length; i++) {
    const pos = positions[i];
    const contentStart = pos.endOpenTag;

    // 找结束 </div> 然后紧接着 </div> (双重嵌套)
    const afterContent = html.substring(contentStart);

    // 最稳定的方法：找 </div></div><script 或 </div></div><h5
    const endMarkers = ['</div></div><script', '</div></div><h5', '</div></div><div id='];
    let endPos = -1;
    for (const marker of endMarkers) {
      const p = afterContent.indexOf(marker);
      if (p !== -1) {
        if (endPos === -1 || p < endPos) endPos = p;
      }
    }

    if (endPos === -1) continue;

    const rawContent = afterContent.substring(0, endPos);

    // 提取正确答案
    const ansMatch = rawContent.match(/<span class=correct-answer-text>([A-D]+)<\/span>/);
    const answer = ansMatch ? ansMatch[1] : null;

    // 提取解析文本 (去除HTML标签)
    const analysis = rawContent
      .replace(/<strong>正确答案[^<]*<\/strong><br>/g, '')
      .replace(/<span class=correct-answer-text>[A-D]+<\/span>/g, '')
      .replace(/<[^>]+>/g, ' ')
      .replace(/&nbsp;/g, ' ')
      .replace(/&amp;/g, '&')
      .replace(/&lt;/g, '<')
      .replace(/&gt;/g, '>')
      .replace(/\s+/g, ' ')
      .trim();

    explanations[pos.num] = {
      answer: answer,
      analysis: analysis
    };
  }

  return explanations;
}

/** 提取综合题解析 (solution-answer-XXX-N) */
function extractSolutionAnswers(html) {
  const solutions = {};

  // 匹配 solution-detail div
  const regex = /<div class="solution-detail[^>]*id=solution-answer-[^-]+-(\d+)[^>]*style=display:none>/g;
  let m;
  const positions = [];
  while ((m = regex.exec(html)) !== null) {
    positions.push({
      num: parseInt(m[1]),
      start: m.index,
      contentStart: m.index + m[0].length
    });
  }

  for (let i = 0; i < positions.length; i++) {
    const pos = positions[i];
    const afterContent = html.substring(pos.contentStart);

    // 找结束: </div></div>  (solution div闭合 + 外层div闭合)
    let endPos = -1;
    const endMarker = '</div></div>';
    const p = afterContent.indexOf(endMarker);
    if (p !== -1) endPos = p;

    if (endPos === -1) continue;

    const rawContent = afterContent.substring(0, endPos);

    // 提取文本内容，将SVG替换为占位符
    let text = rawContent.replace(/<svg[\s\S]*?<\/svg>/g, ' [图片] ');
    text = text.replace(/<div class=svg-wrapper[^>]*>[\s\S]*?<\/div>/g, ' [图片] ');
    text = text.replace(/<[^>]+>/g, ' ')
               .replace(/&nbsp;/g, ' ')
               .replace(/&amp;/g, '&')
               .replace(/&lt;/g, '<')
               .replace(/&gt;/g, '>')
               .replace(/\s+/g, ' ')
               .trim();

    solutions[pos.num] = text;
  }

  return solutions;
}

/** 清理HTML文本 */
function cleanText(text) {
  return text.replace(/<[^>]+>/g, ' ')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/\s+/g, ' ')
    .trim();
}

/** 爬取单年份页面 */
async function crawlYear(year) {
  const url = `${BASE_URL}${QUIZ_PATH}/${year}/`;
  console.log(`\n====== 正在爬取 ${year} 年 ======`);
  console.log(`  URL: ${url}`);

  try {
    const html = await fetch(url);

    // 1. 提取答案速对 (选择题)
    const answerKey = extractAnswerKey(html, year);

    // 2. 提取选择题解析
    const explanations = extractChoiceExplanations(html);
    const explainCount = Object.keys(explanations).length;
    console.log(`  [解析] 已提取 ${explainCount} 道选择题解析`);

    // 3. 提取综合题答案
    const solutions = extractSolutionAnswers(html);
    const solCount = Object.keys(solutions).length;
    console.log(`  [综合] 已提取 ${solCount} 道综合题解析`);

    // 组装结果
    const result = {
      year: year,
      url: url,
      answers: answerKey,
      explanations: explanations,
      solutions: solutions
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

/** 生成更新后的Markdown（基于现有模板填充答案） */
function generateUpdatedMarkdown(originalContent, data) {
  let content = originalContent;
  const answersMap = data.answers || {};
  const explanations = data.explanations || {};

  // 选择题: 填充正确答案和解析
  for (const [qNum, answer] of Object.entries(answersMap)) {
    const num = parseInt(qNum);

    // 填充正确答案
    const ansRegex = new RegExp(`(正确答案：)([^\\n]*)`, 'g');
    // 需要找到对应题号的正确答案行
    // 方法: 先找到题号标题, 再找之后的正确答案行
  }

  // 选择题解析
  // 解析在各种位置, 用更精确的替换方式
  for (const [qNum, exp] of Object.entries(explanations)) {
    // 替换该题号的解析内容
  }

  return content;
}

//======= 主函数 =======//

async function main() {
  const args = process.argv.slice(2);
  let years;

  if (args.length === 0) {
    years = ALL_YEARS;
  } else if (args.length === 1 && !isNaN(args[0])) {
    years = [parseInt(args[0])];
  } else if (args.length === 2 && !isNaN(args[0]) && !isNaN(args[1])) {
    const start = parseInt(args[0]);
    const end = parseInt(args[1]);
    years = [];
    for (let y = start; y <= end; y++) years.push(y);
  } else {
    console.error('用法: node crawler.js [起始年份] [结束年份]');
    console.error('示例: node crawler.js           # 爬取2009-2026');
    console.error('      node crawler.js 2024       # 只爬2024');
    console.error('      node crawler.js 2010 2020  # 爬2010-2020');
    process.exit(1);
  }

  console.log(`408真题答案解析爬虫`);
  console.log(`目标: ${BASE_URL}${QUIZ_PATH}/`);
  console.log(`年份: ${years[0]} ~ ${years[years.length - 1]} (共${years.length}年)`);
  console.log(`输出目录: ${OUTPUT_DIR}`);

  const allResults = {};

  for (const year of years) {
    const result = await crawlYear(year);
    if (result) {
      allResults[year] = result;
      saveResult(result);
    }
    // 短暂延迟，避免请求过快
    await new Promise(r => setTimeout(r, 500));
  }

  // 保存汇总
  saveSummary(allResults);

  // 打印统计
  console.log('\n======= 爬取完成 =======');
  console.log(`成功: ${Object.keys(allResults).length}/${years.length} 年`);
  console.log(`数据保存在: ${OUTPUT_DIR}`);
}

main().catch(e => console.error('爬虫异常:', e));
