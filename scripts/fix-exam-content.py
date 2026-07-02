#!/usr/bin/env python3
"""Fix exam content: remove video links, individual file answer folding"""
import os, re

# Fix individual exam files (choices, application, comprehensive)
INDIVIDUAL = ['content/exam/choice/2024-q5.md', 'content/exam/application/2023-q1.md', 'content/exam/comprehensive/2022-q1.md']
for path in INDIVIDUAL:
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Wrap ## 答案 section
    new1 = re.sub(r'## 答案\s*\n(.+?)(?=\n## |\Z)', r'<details style="margin:1rem 0;cursor:pointer">\n<summary style="color:var(--accent);font-weight:600">[答案]</summary>\n\n\1\n</details>\n\n', text, flags=re.DOTALL)

    # Wrap ## 解析 section
    new2 = re.sub(r'## 解析\s*\n(.+?)(?=\n## |\Z)', r'<details style="margin:1rem 0;cursor:pointer">\n<summary style="color:var(--accent);font-weight:600">[解析]</summary>\n\n\1\n</details>\n\n', new1, flags=re.DOTALL)

    if new2 != text:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new2)
        print(f'  OK {path}: wrapped answer+analysis')
    else:
        print(f'  -- {path}: no changes')

print('Done')
