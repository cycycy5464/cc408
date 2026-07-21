"""转换剩余的 plain 选项文件为 backslash 格式"""
import re, os, glob

BASE = 'D:/projet/cc408/cc408'
CONTENT = os.path.join(BASE, 'content', 'question')

remaining = ['2014-cn-034.md', '2014-ds-004.md', '2014-ds-007.md']

for bn in remaining:
    fpath = os.path.join(CONTENT, bn)
    with open(fpath, encoding='utf-8') as fh:
        raw = fh.read()
    lines = raw.split('\n')
    
    new_lines = []
    for l in lines:
        s = l.strip()
        if len(s) >= 2 and s[0] in 'ABCD' and s[1] == '.' and not (len(s) >= 3 and s[2] == '.'):
            # A.xxx -> A\.xxx
            indent = l[:len(l) - len(s)]
            letter = s[0]
            content = s[2:].strip()
            new_lines.append(indent + letter + '\\' + '.' + content)
        else:
            new_lines.append(l)
    
    new_raw = '\n'.join(new_lines)
    with open(fpath, 'w', encoding='utf-8') as fh:
        fh.write(new_raw)
    print(f"  转换 {bn}")

# 最终验证
print("\n=== 最终全面验证 ===")
for Y in ['2014']:
    files = sorted(glob.glob(os.path.join(CONTENT, f'{Y}-*.md')))
    good = 0
    bad = 0
    for f in files:
        bn = os.path.basename(f)
        num = int(bn.split('-')[2].replace('.md',''))
        if num > 40: continue
        
        with open(f, encoding='utf-8') as fh:
            lines = fh.read().split('\n')
        
        backslash_opts = []  # A\.xxx
        plain_opts = []      # A.xxx
        
        for i, l in enumerate(lines):
            s = l.strip()
            if len(s) < 2: continue
            if s[0] in 'ABCD' and s[1] == '\\' and len(s) >= 3 and s[2] == '.':
                backslash_opts.append(s[:50])
            elif s[0] in 'ABCD' and s[1] == '.':
                plain_opts.append(s[:50])
        
        total = len(backslash_opts) + len(plain_opts)
        if total != 4:
            print(f"  ❌ {bn}: backslash={len(backslash_opts)} plain={len(plain_opts)} (共{total})")
            bad += 1
        elif len(plain_opts) > 0:
            print(f"  ❌ {bn}: 仍有 {len(plain_opts)} 个 plain 选项: {plain_opts}")
            bad += 1
        elif len(backslash_opts) == 4:
            good += 1
    
    print(f"\n  {Y}: {good} 正确, {bad} 问题")
    if good == 40:
        print("  ✅ 全部通过！")
