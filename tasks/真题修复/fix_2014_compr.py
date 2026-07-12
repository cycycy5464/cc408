"""修复 2014 综合题 41-47"""
import re, os

BASE = 'D:/projet/cc408/cc408'

# ==================== 2014-ds-041 ====================
def fix_041():
    path = os.path.join(BASE, 'content', 'question', '2014-ds-041.md')
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    
    # 1. 格式化 left/weight/right 为表格
    raw = raw.replace(
        '结点结构为：\n\nleft\n\nweight\n\nright',
        '结点结构为：\n\n| left | weight | right |\n|------|--------|-------|'
    )
    
    # 2. 去重 [tag_link]
    # 第1个 [tag_link] 在 stem 后，第2个紧跟着，取第1个
    lines = raw.split('\n')
    tag_count = 0
    new_lines = []
    skip_tag = False
    for l in lines:
        if '[tag_link]' in l:
            tag_count += 1
            if tag_count == 1:
                new_lines.append(l)
                new_lines.append('')
            continue
        if tag_count >= 2 and l.strip() == '':
            continue
        new_lines.append(l)
    
    raw = '\n'.join(new_lines)
    
    # 3. 从 answer 部分剥离 JS 和 Q42 污染
    js_marker = 'if(typeof window.quizDB==="undefined")'
    if js_marker in raw:
        raw = raw[:raw.index(js_marker)]
    
    # 末尾可能还有 Q42 残片
    q42_marker = '42 某网络中的路由器'
    if q42_marker in raw:
        raw = raw[:raw.index(q42_marker)]
    
    # 4. 整理 answer 中散落的编号
    # 把单独的 ① ② ③ ④ ⑤ ⑥ 等放回对应行
    raw = re.sub(r'\n①\n', ' ', raw)
    raw = re.sub(r'\n②\n', ' ', raw)
    raw = re.sub(r'\n③\n', ' ', raw)
    raw = re.sub(r'\n④\n', ' ', raw)
    raw = re.sub(r'\n⑤\n', ' ', raw)
    raw = re.sub(r'\n⑥\n', ' ', raw)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(raw)
    print("  041 OK")

# ==================== 2014-ds-042 ====================
def fix_042():
    path = os.path.join(BASE, 'content', 'question', '2014-ds-042.md')
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    
    lines = raw.split('\n')
    
    # 找到关键位置
    # 1. stem 区直到 题42表R1所维护的LSI
    # 2. 表格数据区 (line 27-151)
    # 3. SVG 图片
    # 4. 跨题 Q43 内容删除
    # 5. Answer 区保留
    
    # 找到 "R1的LSI" 表格开始和 ">" SVG 行
    table_start = None
    svg_idx = None
    for i, l in enumerate(lines):
        if '题42表R1所维护的LSI' in l:
            table_start = i
        if '2014_Q42_4.svg' in l:
            svg_idx = i
    
    if table_start is None or svg_idx is None:
        print("  042 ⚠️ cannot locate table boundaries")
        return
    
    print(f"  042 table_start={table_start}, svg_idx={svg_idx}")
    
    # 保留 stem 到 table_start
    stem_lines = lines[:table_start]
    
    # 构建 MD 表格
    md_table = '''题42表R1所维护的LSI

| | R1的LSI | R2的LSI | R3的LSI | R4的LSI | 备注 |
|---|---------|---------|---------|---------|------|
| Router ID | 10.1.1.1 | 10.1.1.2 | 10.1.1.5 | 10.1.1.6 | 标识路由器的IP地址 |
| Link1 | | | | | |
| ID | 10.1.1.2 | 10.1.1.1 | 10.1.1.6 | 10.1.1.5 | 所连路由器的Router ID |
| IP | 10.1.1.1 | 10.1.1.2 | 10.1.1.5 | 10.1.1.6 | Link1的本地IP地址 |
| Metric | 3 | 3 | 6 | 6 | Link1的费用 |
| Link2 | | | | | |
| ID | 10.1.1.5 | 10.1.1.6 | 10.1.1.1 | 10.1.1.2 | 所连路由器的Router ID |
| IP | 10.1.1.9 | 10.1.1.13 | 10.1.1.10 | 10.1.1.14 | Link2的本地IP地址 |
| Metric | 2 | 4 | 2 | 4 | Link2的费用 |
| Link3 | | | | | |
| Prefix | 192.1.1.0/24 | 192.1.6.0/24 | 192.1.5.0/24 | 192.1.7.0/24 | 直连网络Net1的网络前缀 |
| Metric | 1 | 1 | 1 | 1 | 到达直连网络Net1的费用 |

'''
    
    # SVG 和后面的内容
    svg_line = lines[svg_idx]
    
    # 找到 [tag_link] 区域
    answer_start = None
    for i in range(svg_idx + 1, len(lines)):
        if '[tag_link]' in lines[i]:
            answer_start = i
            break
    
    if answer_start is None:
        print("  042 ⚠️ no [tag_link] found")
        return
    
    # 提取 answer 内容（从 answer_start 开始，跳过 Q43 污染）
    answer_lines_raw = lines[answer_start:]
    
    # 清理 answer: 去重 [tag_link], 删除 Q43 污染
    clean_answer = []
    has_tag = False
    for l in answer_lines_raw:
        if '[tag_link]' in l:
            if not has_tag:
                clean_answer.append(l)
                has_tag = True
            continue
        # 跳过 Q43 的内容 ("43 .." 开头的或 "计算机网络 43" 的)
        if l.strip().startswith('43') and ('请根据题42' in l or '.' in l[:5]):
            continue
        if '计算机网络 43' in l:
            continue
        if '目的网络' in l and '下一跳' in l:
            continue
        if l.strip() in ['目的网络', '下一跳', '接口']:
            continue
        clean_answer.append(l)
    
    # 重组内容
    new_content = '\n'.join(stem_lines) + '\n\n' + md_table + svg_line + '\n\n' + '\n'.join(clean_answer)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("  042 OK")

# ==================== 2014-co-043 ====================
def fix_043():
    path = os.path.join(BASE, 'content', 'question', '2014-co-043.md')
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    
    lines = raw.split('\n')
    
    # 找到 [tag_link] 区域
    tag_idx = None
    for i, l in enumerate(lines):
        if '[tag_link]' in l:
            tag_idx = i
            break
    
    if tag_idx is None:
        print("  043 ⚠️ no [tag_link]")
        return
    
    stem = lines[:tag_idx]
    answer = lines[tag_idx:]
    
    # 去重 [tag_link]
    clean_answer = []
    has_tag = False
    for l in answer:
        if '[tag_link]' in l:
            if not has_tag:
                clean_answer.append(l)
                has_tag = True
            continue
        clean_answer.append(l)
    
    # 排版 answer 中的编号
    clean_str = '\n'.join(clean_answer)
    clean_str = re.sub(r'\n①\n', '\n① ', clean_str)
    clean_str = re.sub(r'\n②\n', '\n② ', clean_str)
    
    new_content = '\n'.join(stem) + '\n' + clean_str
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("  043 OK")

# ==================== 2014-co-044 ====================
def fix_044():
    path = os.path.join(BASE, 'content', 'question', '2014-co-044.md')
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    
    # 替换机器代码表为 MD 表格
    machine_table = '''| 编号 | 地址 | 机器代码 | 汇编代码 | 注释 |
|------|------|---------|---------|------|
| 1 | 08048100H | 00022080H | loop:sll R4,R2,2 | (R2)《2→R4 |
| 2 | 08048104H | 00083020H | add R4,R4,R3 | (R4)+(R3)→R4 |
| 3 | 08048108H | 8C850000H | load R5,0(R4) | ((R4)+0)→R5 |
| 4 | 0804810CH | 00250820H | add R1,R1,R5 | (R1)+(R5)→R1 |
| 5 | 08048110H | 20420001H | add R2,R2,1 | (R2)+1→R2 |
| 6 | 08048114H | 1446 FFFAH | bne R2,R6,loop | if (R2)≠(R6) goto loop |

'''
    
    # 删除旧表格数据（从 "编号\\n\\n地址" 到 "注释\\n\\n(R2)≠(R6)goto loop"）
    # 改用更精确的方法：定位旧表格数据区域
    table_data_marker = "编号\n\n地址\n\n机器代码\n\n汇编代码\n\n注释"
    if table_data_marker in raw:
        # 找到表格结束 (bne 行后)
        start_idx = raw.index(table_data_marker)
        
        # 找到表格后内容开始的标记："执行上述代码的计算机 M 采用32位"
        after_table_marker = "执行上述代码的计算机 M"
        if after_table_marker in raw:
            end_idx = raw.index(after_table_marker, start_idx)
            raw = raw[:start_idx] + machine_table + raw[end_idx:]
    
    # 添加 [tag_link] 在合适位置
    if '[tag_link]' not in raw:
        # 在题目内容后加
        lines = raw.split('\n')
        # 找到最后一个小题
        last_q = None
        for i, l in enumerate(lines):
            if '\\(4\\)' in l or '(4)' in l:
                last_q = i
        
        if last_q is not None:
            lines.insert(last_q + 1, '')
            lines.insert(last_q + 2, '[tag_link]')
            lines.insert(last_q + 3, '')
            raw = '\n'.join(lines)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(raw)
    print("  044 OK")

# ==================== 2014-os-045 ====================
def fix_045():
    path = os.path.join(BASE, 'content', 'question', '2014-os-045.md')
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    
    lines = raw.split('\n')
    tag_idx = None
    for i, l in enumerate(lines):
        if '[tag_link]' in l:
            tag_idx = i
            break
    
    if tag_idx is None:
        print("  045 ⚠️ no [tag_link]")
        return
    
    stem = lines[:tag_idx]
    answer = lines[tag_idx:]
    
    clean_answer = []
    has_tag = False
    for l in answer:
        if '[tag_link]' in l:
            if not has_tag:
                clean_answer.append(l)
                has_tag = True
            continue
        clean_answer.append(l)
    
    new_content = '\n'.join(stem) + '\n' + '\n'.join(clean_answer)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("  045 OK")

# ==================== 2014-os-046 ====================
def fix_046():
    path = os.path.join(BASE, 'content', 'question', '2014-os-046.md')
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    
    # 去除尾部 Q47 污染
    marker = '47 系统中有多个生产者进程'
    if marker in raw:
        raw = raw[:raw.index(marker)]
    
    lines = raw.split('\n')
    tag_idx = None
    for i, l in enumerate(lines):
        if '[tag_link]' in l:
            tag_idx = i
            break
    
    if tag_idx is None:
        print("  046 ⚠️ no [tag_link]")
        return
    
    stem = lines[:tag_idx]
    answer = lines[tag_idx:]
    
    clean_answer = []
    has_tag = False
    for l in answer:
        if '[tag_link]' in l:
            if not has_tag:
                clean_answer.append(l)
                has_tag = True
            continue
        clean_answer.append(l)
    
    new_content = '\n'.join(stem) + '\n' + '\n'.join(clean_answer)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("  046 OK")

# ==================== 2014-cn-047 ====================
def fix_047():
    path = os.path.join(BASE, 'content', 'question', '2014-cn-047.md')
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    
    # 修复 frontmatter: 移除字段间的空行
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)', raw, re.DOTALL)
    if fm_match:
        fm_raw = fm_match.group(1)
        body = fm_match.group(2)
        fm_lines = fm_raw.split('\n')
        fixed = []
        for l in fm_lines:
            stripped = l.strip()
            if not stripped:
                continue
            fixed.append(l)
        raw = '---\n' + '\n'.join(fixed) + '\n---\n' + body
    
    lines = raw.split('\n')
    tag_idx = None
    for i, l in enumerate(lines):
        if '[tag_link]' in l:
            tag_idx = i
            break
    
    if tag_idx is None:
        print("  047 ⚠️ no [tag_link]")
        return
    
    stem = lines[:tag_idx]
    answer = lines[tag_idx:]
    
    clean_answer = []
    has_tag = False
    for l in answer:
        if '[tag_link]' in l:
            if not has_tag:
                clean_answer.append(l)
                has_tag = True
            continue
        clean_answer.append(l)
    
    new_content = '\n'.join(stem) + '\n' + '\n'.join(clean_answer)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("  047 OK")

# ==================== 执行 ====================
if __name__ == '__main__':
    print("=== 2014 综合题修复 ===")
    fix_041()
    fix_042()
    fix_043()
    fix_044()
    fix_045()
    fix_046()
    fix_047()
    print("=== 完成 ===")
