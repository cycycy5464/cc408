"""全面检查 2014 综合题的 JS 注入、跨题污染、表格格式问题"""
import re, os, glob, json

BASE = 'D:/projet/cc408/cc408'
CONTENT = os.path.join(BASE, 'content', 'question')

# 检查 41-47
for num in range(41, 48):
    files = glob.glob(os.path.join(CONTENT, f'2014-*-{num:03d}.md'))
    for f in files:
        bn = os.path.basename(f)
        with open(f, encoding='utf-8') as fh:
            raw = fh.read()
        
        print(f"{'='*60}")
        print(f"  {bn} ({len(raw)} 字节)")
        print(f"{'='*60}")
        
        # 检查是否有 JS 注入
        has_js = 'function ' in raw or 'window.quizDB' in raw or 'addEventListener' in raw
        has_var_js = 'var ' in raw or 'const ' in raw
        print(f"  JS代码注入: {'有' if has_js else '无'}")
        
        # 检查是否有其他题号的内容
        other_questions = []
        for q in range(41, 48):
            if q != num:
                pattern = f'第{q}题'
                if pattern in raw:
                    other_questions.append(q)
        if other_questions:
            print(f"  跨题污染: 含 {other_questions} 题的内容")
        
        # 检查 [tag_link]
        tag_count = raw.count('[tag_link]')
        print(f"  [tag_link]: {tag_count} 个")
        
        # 检查 正确答案
        has_answer = '正确答案' in raw
        print(f"  正确答案: {'有' if has_answer else '无'}")
        
        # 检查表格（含 | 且像表格的行）
        lines = raw.split('\n')
        table_lines = [i+1 for i, l in enumerate(lines) if l.strip().startswith('|') and '---' in l]
        if table_lines:
            print(f"  MD表格分隔行: {table_lines}")
        
        # 检查代码块
        code_blocks = [i+1 for i, l in enumerate(lines) if l.strip().startswith('```')]
        if code_blocks:
            print(f"  代码块: {code_blocks}")
        else:
            print(f"  代码块: 无")
        
        # 检查前 5 行和后 5 行
        print(f"  最后5行:")
        for i in range(max(0, len(lines)-5), len(lines)):
            print(f"    L{i+1}: {lines[i][:80]}")
        
        print()
