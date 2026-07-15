const fs = require('fs');
const path = require('path');

const qDir = 'content/question';
const backupDir = 'content/exam/408quiz/backup-整卷';
const years = ['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025'];

// 按年份分组
const byYear = {};
for (const f of fs.readdirSync(qDir)) {
  if (!f.endsWith('.md') || f.includes('.bak') || f.includes('.v2bak')) continue;
  const match = f.match(/^(\d{4})-/);
  if (!match) continue;
  const year = match[1];
  if (!byYear[year]) byYear[year] = [];
  byYear[year].push(f);
}

for (const year of years) {
  if (!byYear[year] || byYear[year].length === 0) {
    console.log(year + ': no files, skipped');
    continue;
  }
  
  byYear[year].sort();
  
  let content = '---\n';
  content += 'title: "' + year + '\u5E74408\u771F\u9898\uFF08\u6574\u5377\uFF09"\n';
  content += 'date: 2025-01-01\n';
  content += 'type: 408quiz\n';
  content += '---\n\n';
  content += '# ' + year + '\u5E74408\u771F\u9898\n\n';
  
  for (const f of byYear[year]) {
    const fileContent = fs.readFileSync(path.join(qDir, f), 'utf8');
    content += '---\n\n';
    content += '## ' + f.replace('.md', '') + '\n\n';
    // 去掉 frontmatter
    const body = fileContent.replace(/^---[\s\S]*?---\n*/, '');
    content += body + '\n\n';
  }
  
  const outPath = path.join(backupDir, year + '.md');
  fs.writeFileSync(outPath, content, 'utf8');
  console.log(year + ': ' + byYear[year].length + ' files');
}

console.log('\n\u5168\u90E8\u66F4\u65B0\u5B8C\u6210');
