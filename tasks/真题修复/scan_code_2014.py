"""扫描 2014 年所有文件，检查代码块缺少语言标识"""
import re, os, glob

base = 'D:/projet/cc408/cc408'
content_dir = os.path.join(base, 'content', 'question')

files = sorted(glob.glob(os.path.join(content_dir, '2014-*.md')))
total = 0
problems = []
for f in files:
    bn = os.path.basename(f)
    with open(f, encoding='utf-8') as fh:
        lines = fh.read().split('\n')
    
    i = 0
    in_code = False
    while i < len(lines):
        l = lines[i]
        stripped = l.strip()
        if stripped.startswith('```'):
            if not in_code:
                # 代码块开始
                in_code = True
                # 检查是否只有 ``` 没有语言标识
                if stripped == '```' or stripped == '````':
                    problems.append((bn, i+1, '代码块起始缺少语言标识'))
            else:
                # 代码块结束
                in_code = False
        i += 1

if problems:
    print(f"⚠️ 发现 {len(problems)} 处缺少语言标识的代码块：")
    for bn, line, desc in problems:
        print(f"  {bn} L{line}: {desc}")
else:
    print("✅ 所有代码块都有语言标识")

# 也列出所有有代码块的文件，看看哪些代码块是正常的
print("\n所有含代码块的文件：")
for f in files:
    bn = os.path.basename(f)
    with open(f, encoding='utf-8') as fh:
        content = fh.read()
    code_blocks = re.findall(r'```(\w*)\n', content)
    if code_blocks:
        print(f"  {bn}: {code_blocks}")
