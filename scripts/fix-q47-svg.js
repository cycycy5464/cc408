/**
 * 修复 SVG 自闭合标签
 * HTML 允许 <path ...> 不闭合，但 XML/SVG 要求 <path .../>
 */
const fs = require('fs');

const INPUT = 'E:/programcc408/cc408/static/images/questions/2009_Q47_9.svg';

let svg = fs.readFileSync(INPUT, 'utf8');
console.log(`输入: ${svg.length} 字节`);

const voidElements = ['path', 'ellipse', 'rect', 'circle', 'line', 'polygon', 'polyline', 'use', 'image'];
let count = 0;
for (const el of voidElements) {
  const regex = new RegExp(`<${el}([^>]*?[^/])>`, 'g');
  svg = svg.replace(regex, (match, attrs) => {
    count++;
    return `<${el}${attrs}/>`;
  });
}

fs.writeFileSync(INPUT, svg, 'utf8');
console.log(`修复自闭合: ${count} 处`);
console.log(`输出: ${svg.length} 字节`);

// 验证
const checkVoid = ['path', 'ellipse', 'rect'];
for (const el of checkVoid) {
  const total = (svg.match(new RegExp(`<${el}[^>]*>`, 'g')) || []).length;
  const selfClosed = (svg.match(new RegExp(`<${el}[^>]*/>`, 'g')) || []).length;
  const unclosed = total - selfClosed;
  console.log(`  <${el}>: ${total} total, ${selfClosed} self-closed, ${unclosed} unclosed`);
}
console.log('✅ Done');
