"""检查 2014 年综合题的质量"""
import re, os, glob

BASE = 'D:/projet/cc408/cc408'
CONTENT = os.path.join(BASE, 'content', 'question')

# 检查 41-47
for num in range(41, 48):
    # 找出对应文件
    pattern = f'2014-*-{num:03d}.md'
    files = glob.glob(os.path.join(CONTENT, pattern))
    
    for f in files:
        bn = os.path.basename(f)
        with open(f, encoding='utf-8') as fh:
            raw = fh.read()
        lines = raw.split('\n')
        
        print(f"{'='*60}")
        print(f"  {bn} ({len(lines)} 行)")
        print(f"{'='*60}")
        
        # 是否有 MD 表格
        has_table = any('|' in l and ('---' in l or l.strip().startswith('|')) for l in lines)
        print(f"  MD表格: {'有' if has_table else '无'}")
        
        # 是否有代码块
        code_fences = [i for i, l in enumerate(lines) if l.strip().startswith('```')]
        print(f"  代码块: {len(code_fences)} 个 (行 {[f+1 for f in code_fences]})")
        
        # 显示前 10 行
        print(f"  --- 前 10 行 ---")
        for i in range(min(10, len(lines))):
            print(f"  L{i+1}: {lines[i][:80]}")
        
        # 显示包含 | 的行
        table_lines = [i+1 for i, l in enumerate(lines) if '|' in l and l.strip().startswith('|')]
        if table_lines:
            print(f"  表格行: {table_lines}")
            for i in [t-1 for t in table_lines[:5]]:
                if i < len(lines):
                    print(f"    L{i+1}: {lines[i][:100]}")
        
        # 检查是否有 [tag_link]
        has_tag = any('[tag_link]' in l for l in lines)
        print(f"  [tag_link]: {'有' if has_tag else '无'}")
        
        # 显示包含 "正确答案" 的行
        answer_lines = [i+1 for i, l in enumerate(lines) if '正确答案' in l]
        print(f"  答案行: {answer_lines}")
        
        print()
