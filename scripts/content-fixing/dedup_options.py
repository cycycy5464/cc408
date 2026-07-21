"""
通用去重脚本：删除选择题中重复的选项组
用途：fix_year.py 覆盖选项时可能追加了新选项而未删除旧的，导致 >4 个选项行
检测：A.xxx、A\.xxx、A.<katex> 各种格式
策略：优先保留 KaTeX 版本（爬虫恢复的）；若无 KaTeX 保留前 4 个
用法：python dedup_options.py <年份> [年份...]
示例：python dedup_options.py 2014 2015 2016
"""
import re, os, sys, glob

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTENT_DIR = os.path.join(BASE, 'content', 'question')

YEARS = sys.argv[1:] if len(sys.argv) > 1 else []

if not YEARS:
    print("用法: python dedup_options.py <年份> [年份...]")
    sys.exit(1)

for Y in YEARS:
    files = sorted(glob.glob(os.path.join(CONTENT_DIR, f'{Y}-*.md')))
    fixed = 0
    for f in files:
        basename = os.path.basename(f)
        num = int(basename.split('-')[2].replace('.md',''))
        if num > 40:
            continue
        
        with open(f, encoding='utf-8') as fh:
            content = fh.read()
        lines = content.split('\n')
        
        # 匹配所有以 A. B. C. D. 开头的行（含 A\.
        opt_indices = []
        for i, l in enumerate(lines):
            s = l.strip()
            if re.match(r'^[A-D]\.', s):     # A.xxx 或 A\.
                opt_indices.append(i)
        
        if len(opt_indices) <= 4:
            continue
        
        # 找 KaTeX 版本
        katex_indices = [i for i in opt_indices if 'katex' in lines[i]]
        
        if len(katex_indices) >= 4:
            # 保留 KaTeX 版本这 4 行
            keep_start = katex_indices[0]
            keep_end = katex_indices[3]
        else:
            # 没有 KaTeX 保留前 4 行
            keep_start = opt_indices[0]
            keep_end = opt_indices[3]
        
        # 构建新内容
        new_lines = lines[:keep_start] + lines[keep_start:keep_end + 1]
        
        # 跳过后续所有选项行
        after = keep_end + 1
        while after < len(lines):
            s = lines[after].strip()
            if re.match(r'^[A-D][\.\\]', s):
                after += 1
            else:
                break
        new_lines.extend(lines[after:])
        
        new_content = '\n'.join(new_lines)
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(new_content)
            fixed += 1
            print(f"  修复: {basename}")
    
    if fixed:
        print(f"  {Y}: 修复 {fixed} 个文件")
    else:
        print(f"  {Y}: 无重复")

print("\n✅ 去重完成")
