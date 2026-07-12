"""精确检测 2014 代码块"""
import os, glob

content_dir = 'content/question'

print("=== 代码块检测 ===")
for num in range(41, 48):
    for f in glob.glob(os.path.join(content_dir, f'2014-*-{num:03d}.md')):
        bn = os.path.basename(f)
        with open(f, encoding='utf-8') as fh:
            lines = fh.read().split('\n')
        
        in_block = False
        issues = []
        for i, l in enumerate(lines):
            s = l.strip()
            if s.startswith('```'):
                if not in_block:
                    # 代码块开始
                    lang = s[3:].strip()
                    if not lang and not issues:
                        issues.append(f'L{i+1} 缺语言标识')
                    in_block = True
                else:
                    in_block = False
        
        if issues:
            print(f"  ❌ {bn}: {issues}")
        else:
            print(f"  ✅ {bn}")

print("\n=== 裸露代码检测（不在代码块内的 struct/semaphore） ===")
for num in range(41, 48):
    for f in glob.glob(os.path.join(content_dir, f'2014-*-{num:03d}.md')):
        bn = os.path.basename(f)
        with open(f, encoding='utf-8') as fh:
            raw = fh.read()
        
        in_block = False
        has_issues = False
        for l in raw.split('\n'):
            s = l.strip()
            if s.startswith('```'):
                in_block = not in_block
                continue
            if not in_block:
                for kw in ['semaphore ', 'Consumer()', 'Producer()', 'struct {', 'int main']:
                    if kw in s:
                        print(f"  ❌ {bn}: {s[:60]}")
                        has_issues = True
                        break
        
        if not has_issues:
            print(f"  ✅ {bn}")
