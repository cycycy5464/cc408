"""
Phase 1: 综合审计扫描器
扫描 content/question/ 下所有文件，报告可自动修复和需人工处理的问题
"""
import os, re, glob

QUESTION_DIR = 'content/question'

def scan_files():
    files = sorted(glob.glob(f'{QUESTION_DIR}/*.md'))
    print(f"共发现 {len(files)} 个题目文件\n")
    return files

def audit_file(path):
    """对一个文件执行所有审计检查，返回问题列表"""
    issues = []
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    filename = os.path.basename(path)
    
    # 解析基本信息
    front = {}
    front_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if front_match:
        for line in front_match.group(1).split('\n'):
            m = re.match(r'(\w+):\s*(.*)', line)
            if m: front[m.group(1)] = m.group(2).strip('"')
    
    subject = front.get('subjects', '')
    qtype = front.get('question_type', '')
    year = filename[:4] if re.match(r'\d{4}', filename) else 'simulate'
    
    # 找到 [tag_link] 标记 — 解析区起点
    tags = [m.start() for m in re.finditer(r'\[tag_link\]', content)]
    parse_start = tags[-1] + len('[tag_link]') if tags else len(content)
    parse_text = content[parse_start:] if parse_start < len(content) else ''
    question_text = content[:tags[0]] if tags else content[:len(content)//2]
    
    # === 检查 1: 数学格式错误 2 6 − 2 → $2^6-2$ ===
    math_patterns = re.findall(r'\d \d [−\-] \d', parse_text)
    if math_patterns:
        issues.append(('math_format', f'数学格式错误: {set(math_patterns)}', ''))
    
    # === 检查 2: 断裂 markdown 链接 ===
    broken_links = re.findall(r'\[([^\]]+\.\d+[^\]]*)\]\(([^)]+)\)', content)
    if broken_links:
        # 只报告看起来不是真正链接的（包含IP地址等）
        suspicious = [f'[{a}]({b})' for a, b in broken_links if '.' in a and re.search(r'\d', a)]
        if suspicious:
            issues.append(('broken_link', f'断裂链接: {suspicious[:3]}', ''))
    
    # === 检查 3: 表格末行污染 ===
    # 搜索管道符行末尾紧跟文字（同一行）
    polluted = re.findall(r'\| 0\.0\.0\.0.*\| L0 \|.*\S', content)
    if polluted and 'L0 | (3)' in content or 'L0 | 若' in content:
        issues.append(('table_pollution', '表格末行被文本污染', ''))
    
    # === 检查 4: 解析区超长段落 ===
    # 解析区有 (1)(2)(3) 但在一行中
    for tag_pos in tags:
        end_pos = len(content)
        parse_section = content[tag_pos + len('[tag_link]'):end_pos].strip()
        # 检查 (1)(2)(3) 是否在同一行（没有换行分隔）
        if re.search(r'\(1\).*\(2\).*\(3\)', parse_section[:3000]):
            issues.append(('long_paragraph', '解析区(1)(2)(3)未分段', ''))
            break
    
    # === 检查 5: 内容是纯文本表格（该是md表格但没管道符）===
    # 查找"见下表"之后跟着列对齐的文本
    if '见下表' in parse_text or '见下表' in question_text:
        # 检查附近是否已经有md表格
        near = parse_text[parse_text.find('见下表'):parse_text.find('见下表')+300] if '见下表' in parse_text else ''
        near_q = question_text[question_text.find('见下表'):question_text.find('见下表')+300] if '见下表' in question_text else ''
        combined = near + near_q
        has_md_table = '| ---' in combined or '|\n|-' in combined
        if not has_md_table:
            issues.append(('missing_table', '"见下表"但无md表格', ''))
    
    # === 检查 6: 内容污染（解析含"第N题"等标记）===
    # 检查解析区是否包含下一道题目的标记
    pollution = re.search(r'(\d{4}[\s\S]{0,20}第\d+题)', parse_text[:500])
    if pollution:
        issues.append(('content_pollution', f'可能的内容污染: {pollution.group(1)[:40]}', ''))
    
    # === 检查 7: 算法题需要代码框 ===
    # 数据结构/组成原理综合题，算法描述段没有代码框
    if subject in ['数据结构', '计算机组成原理'] and qtype == 'comprehensive':
        if '```c' not in content and '```c++' not in content and '```' not in content:
            if '算法' in question_text or '设计' in question_text:
                issues.append(('no_code_block', '算法题无代码框', ''))
    
    return issues, filename, year, subject, qtype


def main():
    files = scan_files()
    
    # 问题类别
    categories = {
        'math_format': ('数学格式错误', []),
        'broken_link': ('断裂md链接', []),
        'table_pollution': ('表格末行污染', []),
        'long_paragraph': ('解析(1)(2)(3)未分段', []),
        'missing_table': ('"见下表"但无表格', []),
        'content_pollution': ('解析内容污染', []),
        'no_code_block': ('算法题无代码框', []),
    }
    
    for path in files:
        try:
            issues, filename, year, subject, qtype = audit_file(path)
            for issue_type, desc, _ in issues:
                categories[issue_type][1].append((filename, year, subject, desc[:60]))
        except Exception as e:
            print(f"  ERROR scanning {path}: {e}")
    
    # 输出报告
    print("=" * 70)
    print("综合审计报告")
    print("=" * 70)
    
    total_files = len(files)
    total_issues = sum(len(items) for _, items in categories.values())
    print(f"\n扫描文件: {total_files}")
    print(f"发现问题: {total_issues}\n")
    
    for cat_key, (cat_name, items) in sorted(categories.items()):
        if not items:
            continue
        print(f"\n{'─'*60}")
        print(f"【{cat_name}】— {len(items)} 处")
        print(f"{'─'*60}")
        # 按年份分组显示
        by_year = {}
        for fn, yr, subj, desc in items:
            by_year.setdefault(yr, []).append((fn, subj, desc))
        
        for yr in sorted(by_year.keys(), key=lambda x: (x=='simulate', x)):
            yr_list = by_year[yr]
            count = len(yr_list)
            label = f"模拟题" if yr == 'simulate' else f"{yr}年"
            print(f"  {label} ({count}处):")
            for fn, subj, desc in yr_list[:5]:
                print(f"    ├ {fn} ({subj})")
            if count > 5:
                print(f"    └ ... 还有 {count-5} 个")
    
    print(f"\n{'='*70}")
    print(f"总计: {total_issues} 个问题分布于 {sum(1 for v in categories.values() if v[1])} 个类别")
    print(f"{'='*70}")


if __name__ == '__main__':
    main()
