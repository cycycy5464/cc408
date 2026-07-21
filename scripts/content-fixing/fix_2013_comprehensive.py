"""2013 年综合修复脚本：
1. D 选项与 [tag_link] 间加空行
2. MD 表格与文本间加空行
3. 子问题间加空行
4. 代码块缺少语言标识符 -> 加 c
5. 选择题确保 4 个选项（从爬虫数据覆盖）
"""
import re, os, glob, json

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTENT_DIR = os.path.join(BASE, 'content', 'question')
RAW_OPTS = os.path.join(BASE, 'tasks', '408-crawler', 'crawled_data', '2013_raw_opts.json')

with open(RAW_OPTS, encoding='utf-8') as f:
    raw_opts = json.load(f)

files = sorted(glob.glob(os.path.join(CONTENT_DIR, '2013-*.md')))

def fix_file(fpath):
    basename = os.path.basename(fpath)
    parts = basename.replace('.md', '').split('-')
    num_val = int(parts[2])
    
    with open(fpath, encoding='utf-8') as f:
        content = f.read()
    
    original = content
    lines = content.split('\n')
    
    # ----- Fix 1: 选择题确保 4 个选项（从爬虫覆盖，去重） -----
    if num_val <= 40:
        key = str(num_val)
        # Remove ALL existing A.-D. lines first
        cleaned = []
        for line in lines:
            s = line.strip()
            is_opt = False
            for c in 'ABCD':
                if s == f'{c}.' or s.startswith(f'{c}.') or (len(s) > 1 and s[0] == c and (s[1] == '.' or s[1:3] == '\\.')):
                    is_opt = True
                    break
            if not is_opt:
                cleaned.append(line)
        lines = cleaned
        
        if key in raw_opts and len(raw_opts[key]) >= 4:
            opts = raw_opts[key][:4]
            letters = ['A', 'B', 'C', 'D']
            option_lines = [f"{l}.{opt}" for l, opt in zip(letters, opts)]
            
            # Find [tag_link] to insert before it
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
            else:
                lines = cleaned  # restore if no [tag_link] (shouldn't happen)
        else:
            lines = cleaned  # no raw data, keep as-is after removing old opts
    
    # ----- Fix 2: MD 表格前加空行 -----
    new_lines = []
    for i, line in enumerate(lines):
        if line.strip().startswith('|') and '---' not in line.strip():
            # Check if previous line is non-empty non-table non-blank-line
            if i > 0:
                prev = lines[i-1].strip()
                if prev and not prev.startswith('|') and not prev.startswith('---') and prev != '':
                    new_lines.append('')
        new_lines.append(line)
    lines = new_lines
    
    # ----- Fix 3: 子问题前加空行 -----
    new_lines = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if re.match(r'^\d+[）\)]', stripped) and i > 0:
            prev = lines[i-1].strip()
            if prev and prev != '':
                new_lines.append('')
        new_lines.append(line)
    lines = new_lines
    
    # ----- Fix 4: 代码块加语言标识符 -----
    new_lines = []
    in_fence = False
    for line in lines:
        if line.strip().startswith('```'):
            if not in_fence:
                # Opening fence
                rest = line.strip()[3:]
                if not rest:  # ``` with no language
                    line = '```c'
                in_fence = True
            else:
                in_fence = False
        new_lines.append(line)
    lines = new_lines
    
    # ----- Fix 5: 删除解析区域的多余标题混入（如 "### 解答题"） -----
    # 这些出现在 [tag_link] 下方，属于复制时混入的无关内容
    # 只在 40 题这类选择题中出现
    tag_pos = -1
    for i, line in enumerate(lines):
        if '[tag_link]' in line:
            tag_pos = i
            break
    
    if tag_pos >= 0 and num_val <= 40:
        # Look after the correct answer section for unwanted headers
        clean_after_tag = []
        keep = True
        for line in lines[tag_pos:]:
            stripped = line.strip()
            # Remove standalone markdown headers that don't belong
            if re.match(r'^#{1,6}\s+解答', stripped) or re.match(r'^#{1,6}\s+答案\b', stripped):
                keep = False
                continue
            # Once we've dropped, only pick up lines that are answer-related
            # But we need to keep the lead into correct answer
            if not keep:
                continue  # skip everything after the bad header
            clean_after_tag.append(line)
        
        if len(clean_after_tag) < len(lines) - tag_pos:
            lines = lines[:tag_pos] + clean_after_tag
    
    # ----- Fix 6: D 与 [tag_link] 间加空行 -----
    new_lines = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('D.') and i+1 < len(lines):
            next_line = lines[i+1].strip()
            if '[tag_link]' in next_line:
                new_lines.append(line)
                new_lines.append('')
                continue
        new_lines.append(line)
    lines = new_lines
    
    new_content = '\n'.join(lines)
    if new_content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, basename
    return False, basename

fixed = 0
for fpath in files:
    ok, name = fix_file(fpath)
    if ok:
        print(f"FIXED {name}")
        fixed += 1

print(f"\nFixed {fixed} files")
