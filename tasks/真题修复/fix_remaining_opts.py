"""修复 11 个剩余文件：去掉破损的 A\. 选项，保留 A. 选项并转为 A\. 格式"""
import re, os, glob

BASE = 'D:/projet/cc408/cc408'
CONTENT = os.path.join(BASE, 'content', 'question')

# 这些文件有破损的 A\. 选项（一行多项/缺失），但 A. 选项完整
remaining = [
    '2014-cn-033.md', '2014-cn-037.md', '2014-cn-039.md',
    '2014-co-012.md', '2014-co-013.md', '2014-co-014.md', '2014-co-022.md',
    '2014-ds-005.md', '2014-ds-009.md',
    '2014-os-024.md', '2014-os-027.md',
]

for bn in remaining:
    fpath = os.path.join(CONTENT, bn)
    with open(fpath, encoding='utf-8') as fh:
        raw = fh.read()
    lines = raw.split('\n')
    
    # 找到所有破损的 A\. 行
    bad_indices = set()  # 要删除的行
    plain_indices = {}   # A.xxx 格式 -> (idx, content_after_dot)
    
    for i, l in enumerate(lines):
        s = l.strip()
        if not s or len(s) < 2:
            continue
        first = s[0]
        if first not in 'ABCD':
            continue
        
        if s[1] == '\\' and len(s) >= 3 and s[2] == '.':
            bad_indices.add(i)  # 删除
        elif s[1] == '.':
            # 提取内容
            indent = l[:len(l) - len(s)]
            content = s[2:].strip()
            plain_indices[first] = (i, indent, content)
    
    # 构建新内容
    new_lines = []
    for idx, l in enumerate(lines):
        if idx in bad_indices:
            continue
        if idx in {v[0] for v in plain_indices.values()}:
            # 替换为 A\.xxx 格式
            letter = l.strip()[0]
            indent, content = plain_indices[letter][1], plain_indices[letter][2]
            new_lines.append(indent + letter + '\\.' + content)
        else:
            new_lines.append(l)
    
    new_raw = '\n'.join(new_lines)
    with open(fpath, 'w', encoding='utf-8') as fh:
        fh.write(new_raw)
    print(f"  修复 {bn}")

# 最终全面验证
print("\n=== 最终验证 ===")
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
        
        # 统计选项行
        backslash_opts = []
        plain_opts = []
        for i, l in enumerate(lines):
            s = l.strip()
            if len(s) < 2: continue
            if s[0] in 'ABCD' and s[1] == '\\' and len(s) >= 3 and s[2] == '.':
                backslash_opts.append((i, s))
            elif s[0] in 'ABCD' and s[1] == '.':
                plain_opts.append((i, s))
        
        total = len(backslash_opts) + len(plain_opts)
        if total != 4:
            print(f"  ❌ {bn}: backslash={len(backslash_opts)} plain={len(plain_opts)} (共{total})")
            bad += 1
        elif len(plain_opts) > 0:
            print(f"  ❌ {bn}: 仍有 {len(plain_opts)} 个 plain 选项残留")
            bad += 1
        elif len(backslash_opts) == 4:
            good += 1
    
    print(f"\n  {Y}: {good} 正确, {bad} 问题")
    if good == 40:
        print("  ✅ 全部选择题 4 个 backslash 选项")
