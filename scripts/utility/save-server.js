/**
 * SVG 保存服务
 * 启动后监听 3456 端口，接收编辑器 POST 的 SVG 内容并写入文件
 *
 * 用法: node save-server.js
 * 编辑器 POST: { file: "2009_Q47_9.svg", content: "<svg>...</svg>" }
 */

const http = require('http');
const fs = require('fs');
const path = require('path');

const SVG_DIR = 'E:/programcc408/cc408/static/images/questions';
const PORT = 3456;

const server = http.createServer((req, res) => {
  // CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(200);
    res.end();
    return;
  }

  if (req.method !== 'POST') {
    res.writeHead(405);
    res.end('Method not allowed');
    return;
  }

  let body = '';
  req.on('data', chunk => body += chunk);
  req.on('end', () => {
    try {
      const { file, content } = JSON.parse(body);
      if (!file || !content) {
        res.writeHead(400);
        res.end('Missing file or content');
        return;
      }

      // 安全校验：只允许写 SVG 文件
      if (!file.endsWith('.svg') || file.includes('..')) {
        res.writeHead(400);
        res.end('Invalid filename');
        return;
      }

      const filePath = path.join(SVG_DIR, file);
      fs.writeFileSync(filePath, content, 'utf8');
      console.log('✓ 已保存: ' + file);
      res.writeHead(200);
      res.end('OK');
    } catch(e) {
      console.error('保存失败:', e.message);
      res.writeHead(500);
      res.end(e.message);
    }
  });
});

server.listen(PORT, () => {
  console.log('SVG 保存服务运行中 → http://localhost:' + PORT);
  console.log('按 Ctrl+C 停止');
  console.log('静态文件目录: ' + SVG_DIR);
});
