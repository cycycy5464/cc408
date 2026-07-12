"""
修复选择题重复选项：删除 crawl 追加的 A.xxx 格式，保留原始的 A\.xxx 格式
同时处理一行多项（如 A\.x B\.y）的展开
"""
import re, os, glob, sys

BASE = 'D:/projet/cc408/cc408'
CONTENT = os.path.join(BASE, 'content', 'question')

YEARS = sys.argv[1:] if len(sys.argv) > 1 else ['2014']

for Y in YEARS:
    files = sorted(glob.glob(os.path.join(CONTENT, f'{Y}-*.md')))
    fixed = 0
    skipped_one_line = 0  # 一行多项展开数
    
    for f in files:
        bn = os.path.basename(f)
        num = int(bn.split('-')[2].replace('.md',''))
        if num > 40: 
            continue
        
        with open(f, encoding='utf-8') as fh:
            raw = fh.read()
        lines = raw.split('\n')
        
        # 第一步：找到所有选项行并分类
        backslash_opts = []  # A\.xxx 格式
        plain_opts = []      # A.xxx 格式
        
        for i, l in enumerate(lines):
            s = l.strip()
            if len(s) < 2:
                continue
            if s[0] in 'ABCD':
                if s[1] == '\\' and len(s) >= 3 and s[2] == '.':
                    backslash_opts.append((i, s))
                elif s[1] == '.':
                    plain_opts.append((i, s))
        
        # 判断是否有重复
        if len(backslash_opts) == 4 and len(plain_opts) > 0:
            # 有冗余：保留 backslash 格式，删除 plain 格式
            plain_indices = set(i for i, _ in plain_opts)
            new_lines = [l for idx, l in enumerate(lines) if idx not in plain_indices]
            new_raw = '\n'.join(new_lines)
            if new_raw != raw:
                with open(f, 'w', encoding='utf-8') as fh:
                    fh.write(new_raw)
                fixed += 1
                print(f"  修复 {bn}: 删除 {len(plain_opts)} 行 plain 选项")
                
        elif len(backslash_opts) == 0 and len(plain_opts) == 4:
            # 只有 plain 格式，没有 backslash - 这是正常情况（可能原本就只有爬虫数据）
            pass
            
        elif len(backslash_opts) > 4 or len(plain_opts) > 4:
            # 还有更多冗余，都清理
            all_opt_indices = set(i for i, _ in backslash_opts) | set(i for i, _ in plain_opts)
            
            # 保留哪个？优先保留 backslash 格式（最多4个）
            keep_indices = set(i for i, _ in backslash_opts[:4])
            
            # 删除所有其他选项行
            new_lines = []
            removed = 0
            for idx, l in enumerate(lines):
                if idx in all_opt_indices and idx not in keep_indices:
                    removed += 1
                    continue
                new_lines.append(l)
            
            new_raw = '\n'.join(new_lines)
            if new_raw != raw:
                with open(f, 'w', encoding='utf-8') as fh:
                    fh.write(new_raw)
                fixed += 1
                print(f"  修复 {bn}: 删除 {removed} 行冗余选项")
        
        # 检查并展开一行多项
        for i, (idx, s) in enumerate(backslash_opts):
            # 如果一行包含 A 和 B 两个选项（如 "A\.8\.4秒 B\.11\.7 秒"）
            if s.startswith('A') and 'B.' in s[5:] and 'B' not in s[:4]:
                # 这一行包含多个选项
                parts = re.split(r'\s+(?=[A-D]\\)', s)
                if len(parts) > 1:
                    print(f"  一行多项 {bn} 行{idx+1}: [{s[:50]}]")
        
        if len(backslash_opts) == 4 and len(plain_opts) == 0 and num <= 5:
            texts = [l.split('.', 1)[1].strip()[:25] for _, l in backslash_opts]
            print(f"  OK {bn}: {texts}")
    
    print(f"\n{Y}: 修复 {fixed} 个文件\n")

# 最终验证
print("=== 最终验证 ===")
errors = 0
for Y in YEARS:
    files = sorted(glob.glob(os.path.join(CONTENT, f'{Y}-*.md')))
    for f in files:
        bn = os.path.basename(f)
        num = int(bn.split('-')[2].replace('.md',''))
        if num > 40: continue
        
        with open(f, encoding='utf-8') as fh:
            raw = fh.read()
        lines = raw.split('\n')
        
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
            print(f"  ❌ {bn}: backslash={len(backslash_opts)} plain={len(plain_opts)}")
            errors += 1

if errors == 0:
    print("  ✅ 全部 4 个选项")
else:
    print(f"  {errors} 个文件有问题")
