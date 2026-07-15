/**
 * 修复 SVG 中残留的未引用属性值
 * 主要问题: xlink:href=data:image/png;base64,... 长值未引号包裹
 */
const fs = require('fs');

const INPUT = 'E:/programcc408/cc408/static/images/questions/2009_Q47_9.svg';

let svg = fs.readFileSync(INPUT, 'utf8');
console.log(`输入: ${svg.length} 字节`);

let count = 0;

// 修复 xlink:href=data:... (带冒号、分号、斜杠的值)
// 匹配 = 后跟非引号、非空格的值
svg = svg.replace(/=([a-zA-Z][\w-]*:[\S]+?)(?=\s|\/?>)/g, (match, value) => {
  // 确保值不以引号开头
  if (value.startsWith('"') || value.startsWith("'")) return match;
  count++;
  return '="' + value + '"';
});

// 修复 xlink:href= 后面直接跟 data: 的情况（上面可能漏掉）
svg = svg.replace(/xlink:href=(data:[^"'\s>]+)/g, (match, value) => {
  count++;
  return 'xlink:href="' + value + '"';
});

// 修复空属性值 (如一些设为空的属性)
svg = svg.replace(/=(\s*)(\/?>)/g, '=""$2');
// 这个可能会匹配太多，保守处理

console.log(`修复未引用值: ${count} 处`);
console.log(`输出: ${svg.length} 字节`);

fs.writeFileSync(INPUT, svg, 'utf8');

// 验证
const remaining = [];
let m;
const re = /=\s*(?!["'])([^\s>\/]+)/g;
while ((m = re.exec(svg)) !== null) {
  if (svg[m.index-1] === '"') continue;
  remaining.push(m[1].slice(0, 40));
}
console.log('剩余未引用值:', remaining.length);
if (remaining.length > 0) {
  remaining.forEach(r => console.log('  ', r));
} else {
  console.log('✅ All attribute values quoted');
}
