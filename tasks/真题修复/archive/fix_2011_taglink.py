#!/usr/bin/env python
"""针对 2011 年文件，在选项行与 [tag_link] 之间加空行。"""
import glob, os

def needs_fix(filepath):
    with open(filepath, encoding='utf-8') as f:
        text = f.read()
    body = text.split('---', 2)[-1]
    
    idx = body.find('[tag_link]')
    if idx < 0:
        return False, None
    
    # 检查是否有空行（至少2个 \n）在 [tag_link] 前
    last_few = body[max(0, idx-4):idx]
    if last_few.count('\n') >= 2:
        return False, None  # 已有空行
    
    # 检查上一行是否是选项行（D\.，C\.，B\.，A\.）
    # 找到 [tag_link] 所在行的行首
    line_start = body.rfind('\n', 0, idx)
    if line_start < 0:
        line_start = 0
    else:
        line_start += 1
    
    # 找到上一行的行首
    prev_start = body.rfind('\n', 0, line_start - 2)
    if prev_start < 0:
        prev_start = 0
    else:
        prev_start += 1
    
    prev_line = body[prev_start:line_start-1].strip() if line_start > 0 else ''
    
    for c in 'ABCD':
        if prev_line.startswith(c + '\\.'):
            return True, text
    
    return False, None

def fix_file(filepath):
    needs, text = needs_fix(filepath)
    if not needs:
        return False
    
    body_idx = text.find('---', 2) + 3
    if body_idx < 3:
        body_idx = 0
    body = text[body_idx:]
    
    idx = body.find('[tag_link]')
    
    # 确定换行符风格
    insert = '\r\n' if '\r\n' in body else '\n'
    
    # body[:idx] 末尾已有原始换行符，再加一组就是空行
    new_body = body[:idx] + insert + body[idx:]
    new_text = text[:body_idx] + new_body
    
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        f.write(new_text)
    return True

# === 只修复 2011 年 ===
files = sorted(glob.glob('content/question/2011-*.md'))
fixed = 0
for f in files:
    if fix_file(f):
        fname = os.path.basename(f)
        print(f"  fixed: {fname}")
        fixed += 1

print(f"\n共修复 {fixed} 个 2011 年文件")

# 验证
print("\n验证：")
still_bad = 0
for f in files:
    with open(f, encoding='utf-8') as fh:
        text = fh.read()
    body = text.split('---', 2)[-1]
    idx = body.find('[tag_link]')
    if idx < 0:
        continue
    if body[max(0, idx-4):idx].count('\n') < 2:
        # 还是无空行
        still_bad += 1
        fname = os.path.basename(f)
        print(f"  STILL BAD: {fname}")

if still_bad == 0:
    print("  所有 2011 文件均已正确格式化！")
else:
    print(f"  还有 {still_bad} 个文件未修复")
