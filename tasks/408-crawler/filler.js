/**
 * 填充答案解析到Markdown文件 - v2
 *
 * 从 crawled_data/{year}.json 读取爬取的答案和解析数据，
 * 按行逐题填充到 {year}.md 文件中
 *
 * author: 37648
 * 用法: node filler.js [起始年份] [结束年份]
 */

const fs = require('fs');
const path = require('path');

const DATA_DIR = path.join(__dirname, 'crawled_data');

const ALL_YEARS = [];
for (let y = 2009; y <= 2026; y++) ALL_YEARS.push(y);

function loadData(year) {
  const fp = path.join(DATA_DIR, `${year}.json`);
  return fs.existsSync(fp) ? JSON.parse(fs.readFileSync(fp, 'utf8')) : null;
}

function processYear(year) {
  const mdPath = path.join(__dirname, `${year}.md`);
  if (!fs.existsSync(mdPath)) {
    console.log(`  [跳过] ${year}.md 不存在`);
    return false;
  }

  const data = loadData(year);
  if (!data) {
    console.log(`  [跳过] 无爬取数据`);
    return false;
  }

  const answers = data.answers || {};
  const explanations = data.explanations || {};
  const solutions = data.solutions || {};

  const lines = fs.readFileSync(mdPath, 'utf8').split('\n');
  const output = [];
  let currentQ = -1;
  let choicesInAnsLine = false;
  let analysisReplaced = false;
  let answerReplaced = false;
  let changes = 0;

  // 综合题映射：爬虫中 solution-answer-XXX-1 ~ 7 对应 Q41 ~ 47
  const solKeyMap = {'41':'1','42':'2','43':'3','44':'4','45':'5','46':'6','47':'7'};

  for (let i = 0; i < lines.length; i++) {
    let line = lines[i];

    // 检测当前题号
    const qMatch = line.match(/^#####\s+(\d+)\b/);
    if (qMatch) {
      currentQ = parseInt(qMatch[1]);
      choicesInAnsLine = false;
      analysisReplaced = false;
      answerReplaced = false;
    }

    // 处理选择题的正确答案 (Q1-40)
    if (currentQ >= 1 && currentQ <= 40 && !answerReplaced) {
      const ansMatch = line.match(/^(正确.*?答案：)(\s*)$/);
      if (ansMatch && answers[String(currentQ)] && !ansMatch[2].trim()) {
        // 正确答案行且为空 且有答案数据
        const ans = answers[String(currentQ)];
        line = `${ansMatch[1]}${ans}`;
        changes++;
        answerReplaced = true;
      }
    }

    // 处理选择题的解析内容 (Q1-40)
    if (currentQ >= 1 && currentQ <= 40 && !analysisReplaced) {
      if (line.trim() === '解析内容...') {
        const exp = explanations[String(currentQ)];
        if (exp && exp.analysis) {
          let analysis = exp.analysis
            .replace(/^正确答案：\s*/, '')
            .trim();

          // 分句 格式化
          const sentences = analysis
            .split(/(?<=[。；])/)
            .map(s => s.trim())
            .filter(s => s.length > 0);

          if (sentences.length > 0) {
            line = '> ' + sentences.join('\n> ');
            changes++;
          }
        }
        analysisReplaced = true;
      }
    }

    // 处理综合题的答案内容 (Q41-47)
    if (currentQ >= 41 && currentQ <= 47 && !answerReplaced) {
      if (line.trim() === '答案内容...') {
        const sol = solutions[solKeyMap[String(currentQ)]];
        if (sol) {
          // 去除 [图片] 标记的文本
          let text = sol.replace(/\[图片\]/g, '').trim();
          if (text) {
            line = text;
            changes++;
          }
        }
        answerReplaced = true;
      }
    }

    // 处理综合题的多选题（如果有多个答案区域）
    // 一些综合题可能有多个 [tag_link] 行对应多个答案区域
    // 但这里我们在第一次遇到 "答案内容..." 时填充

    output.push(line);
  }

  if (changes > 0) {
    fs.writeFileSync(mdPath, output.join('\n'), 'utf8');
    console.log(`  [已填充] ${year}.md: ${changes} 处修改`);
  } else {
    console.log(`  [无变更] ${year}.md`);
  }

  return changes > 0;
}

function main() {
  const args = process.argv.slice(2);
  let years;

  if (args.length === 0) {
    years = ALL_YEARS;
  } else if (args.length === 1 && !isNaN(args[0])) {
    years = [parseInt(args[0])];
  } else if (args.length === 2 && !isNaN(args[0]) && !isNaN(args[1])) {
    years = [];
    for (let y = parseInt(args[0]); y <= parseInt(args[1]); y++) years.push(y);
  } else {
    console.error('用法: node filler.js [起始年份] [结束年份]');
    process.exit(1);
  }

  console.log('填充408真题答案解析');
  console.log(`年份: ${years[0]} ~ ${years[years.length-1]} (共${years.length}年)`);

  let success = 0;
  for (const year of years) {
    process.stdout.write(`处理 ${year} 年...`);
    const ok = processYear(year);
    if (ok) success++;
  }

  console.log(`\n完成: ${success}/${years.length} 年已更新`);
}

main();
