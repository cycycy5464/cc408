"""
通用修复脚本：对所有年份的 408 真题应用已知修复规则
可处理：
1. 选择题去重（8选项→4选项）+ 从爬虫数据覆盖
2. D 选项与 [tag_link] 间加空行
3. MD 表格格式化（散落数据→表格）+ 表格前加空行
4. 子问题间加空行
5. 代码块加 ```c 语言标识
6. 清除解析中的多余标记（如 ### 解答题、### 分析题等）
7. 选择题确保 4 个选项
"""
import re, os, glob, json, sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTENT_DIR = os.path.join(PROJECT_ROOT, 'content', 'question')

def load_raw_opts(year):
    """加载爬虫提取的选项数据"""
    fpath = os.path.join(PROJECT_ROOT, 'tasks', '408-crawler', 'crawled_data', f'{year}_raw_opts.json')
    if os.path.exists(fpath):
        with open(fpath, encoding='utf-8') as f:
            return json.load(f)
    return {}

def load_crawl_answers(year):
    """加载爬虫的正确答案"""
    fpath = os.path.join(PROJECT_ROOT, 'tasks', '408-crawler', 'crawled_data', f'{year}.json')
    if os.path.exists(fpath):
        with open(fpath, encoding='utf-8') as f:
            data = json.load(f)
        return data.get('answers', {})
    return {}

def fix_scattered_table(text):
    """修复散落的表格数据为 markdown 表格"""
    # Pattern: "文本\n\n文本\n\n文本\n\n..." where it looks like table data
    # Check for common table patterns: Header rows followed by data rows
    lines = text.split('\n')
    fixed = False
    
    # Common table headers in 408 questions
    table_headers = ['指令类型', '指令', '操作', '寻址方式', '字段', '含义', '页', '段', '类型']
    
    for header_word in table_headers:
        if header_word not in text:
            continue
        
        # Look for table structure: header (3 cols) + repeated data rows
        # Simple approach: find sequences of single-word lines that form a table
        idx = text.find(header_word)
        if idx < 0:
            continue
            
        # Check if it's already a proper md table
        before_table = text[max(0, idx-50):idx+len(header_word)+50]
        if '|---' in before_table:
            continue  # already formatted
        
        # Extract candidate table region
        start = max(0, text.rfind('\n\n', 0, idx))
        if start == -1:
            start = 0
        else:
            start = text.rfind('\n', 0, start) + 1  # include the blank line
        
        # Look for end of table (next question text or options)
        end_markers = ['该机的', '则', '是', 'A.', 'B.', 'C.', 'D.', '[tag_link]']
        end = len(text)
        for marker in end_markers:
            m_idx = text.find(marker, idx)
            if m_idx > idx and m_idx < end:
                end = m_idx
        
        region = text[start:end].strip()
        
        # Check if region has the scattered table pattern (single items on separate lines)
        region_lines = region.split('\n')
        non_empty = [l.strip() for l in region_lines if l.strip()]
        
        # If we have 8+ single-line items, it's likely a scattered table
        if len(non_empty) >= 8 and all(' ' not in l for l in non_empty[:6]):
            # Try to build 3-column table
            if len(non_empty) % 3 == 0:
                cols = len(non_empty) // 3
                header = non_empty[:3]
                data_rows = []
                for i in range(cols - 1):
                    row = non_empty[3 + i*3: 3 + (i+1)*3]
                    data_rows.append(row)
                
                md_table = '|' + '|'.join(header) + '|\n'
                md_table += '|' + '|'.join(['---'] * 3) + '|\n'
                for row in data_rows:
                    md_table += '|' + '|'.join(row) + '|\n'
                
                text = text[:start] + md_table + text[end:]
                fixed = True
                break
    
    return text, fixed

def process_file(fpath, raw_opts, year=None):
    """对单个文件执行所有修复流程"""
    basename = os.path.basename(fpath)
    orig_content = open(fpath, encoding='utf-8').read()
    content = orig_content
    parts = basename.replace('.md', '').split('-')
    
    if len(parts) < 3:
        return orig_content, False
    
    num_val = int(parts[2])
    lines = content.split('\n')
    modified = False
    
    # ============ Fix for ALL files ============
    
    # (A) 清除解析中的多余标记
    cleanup_markers = ['### 解答题', '### 分析题', '### 综合题', '## 解答', '## 解析']
    for marker in cleanup_markers:
        if marker in content:
            lines = [l for l in lines if marker not in l]
            modified = True
    
    # (B) 代码块加语言标识
    new_lines = []
    in_fence = False
    for line in lines:
        if line.strip().startswith('```'):
            if not in_fence:
                rest = line.strip()[3:]
                if not rest:  # opening fence with no language
                    line = '```c'
                    modified = True
                in_fence = True
            else:
                in_fence = False
        new_lines.append(line)
    lines = new_lines
    
    # (C) 表格前加空行
    new_lines = []
    for i, line in enumerate(lines):
        if line.strip().startswith('|') and '---' not in line.strip():
            if i > 0:
                prev = lines[i-1].strip()
                if prev and not prev.startswith('|') and not prev.startswith('---') and prev != '':
                    new_lines.append('')
                    modified = True
        new_lines.append(line)
    lines = new_lines
    
    # (D) 子问题前加空行（综合题）
    new_lines = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if re.match(r'^\d+[）\)]', stripped) and i > 0:
            prev = lines[i-1].strip()
            if prev and prev != '':
                new_lines.append('')
                modified = True
        new_lines.append(line)
    lines = new_lines
    
    # (E) D 选项与 [tag_link] 间加空行
    new_lines = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('D.') and i+1 < len(lines):
            next_line = lines[i+1].strip()
            if '[tag_link]' in next_line:
                new_lines.append(line)
                new_lines.append('')
                modified = True
                continue
        new_lines.append(line)
    lines = new_lines
    
    # ============ Fix for choice questions (1-40) ============
    if num_val <= 40:
        key = str(num_val)
        
        # (F) 清除所有 A.-D. 选项行（去重）
        cleaned = []
        for line in lines:
            s = line.strip()
            is_opt = False
            for c in 'ABCD':
                if s == f'{c}.':
                    is_opt = True
                    break
                if s.startswith(f'{c}.') and len(s) > 2 and s[1] == '.':
                    is_opt = True
                    break
                # Check escaped version too
                if len(s) > 3 and s[0] == c and s[1:3] == '\\.':
                    is_opt = True
                    break
            if not is_opt:
                cleaned.append(line)
            else:
                modified = True
        lines = cleaned
        
        # (G) 从爬虫数据插入 4 个选项
        if key in raw_opts and len(raw_opts[key]) >= 4:
            opts = raw_opts[key][:4]
            letters = ['A', 'B', 'C', 'D']
            option_lines = [f"{l}.{opt}" for l, opt in zip(letters, opts)]
            
            tag_idx = -1
            for i, line in enumerate(lines):
                if '[tag_link]' in line:
                    tag_idx = i
                    break
            
            if tag_idx >= 0:
                new_lines = lines[:tag_idx]
                while new_lines and new_lines[-1].strip() == '':
                    new_lines.pop()
                new_lines.append('')
                for ol in option_lines:
                    new_lines.append(ol)
                    new_lines.append('')
                new_lines += lines[tag_idx:]
                lines = new_lines
                modified = True
    
    # ============ Apply scattered table fix ============
    # Do this after option fix to avoid interfering with options
    new_content = '\n'.join(lines)
    new_content, table_fixed = fix_scattered_table(new_content)
    if table_fixed:
        modified = True
    
    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return new_content, True
    
    return orig_content, False

def process_year(year):
    """处理指定年份的所有文件"""
    print(f"\n{'='*50}")
    print(f"Processing {year}...")
    
    raw_opts = load_raw_opts(year)
    print(f"  Loaded raw options for {len(raw_opts)} questions")
    
    pattern = os.path.join(CONTENT_DIR, f'{year}-*.md')
    files = sorted(glob.glob(pattern))
    
    fixed_count = 0
    for fpath in files:
        basename = os.path.basename(fpath)
        parts = basename.replace('.md', '').split('-')
        if len(parts) < 3:
            continue
        new_content, modified = process_file(fpath, raw_opts, year)
        if modified:
            print(f"  FIXED {basename}")
            fixed_count += 1
    
    print(f"\n  Total: {len(files)} files, {fixed_count} modified")
    return fixed_count

if __name__ == '__main__':
    if len(sys.argv) > 1:
        years = sys.argv[1:]
    else:
        years = [str(y) for y in range(2009, 2027)]
    
    total = 0
    for year in years:
        if year.isdigit():
            total += process_year(year)
    
    print(f"\n{'='*50}")
    print(f"All done! Total files modified: {total}")
