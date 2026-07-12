"""
通用修复脚本：处理指定年份的所有题目

修复项目:
1. 选择题确保 4 个选项（从爬虫数据覆盖，去重）
2. MD 表格与文本间加空行
3. 子问题前加空行
4. 代码块缺少语言标识符 -> 加 c
5. 删除解析区域的多余标题混入（如 "### 解答题"）
6. D 选项与 [tag_link] 间加空行

用法: python fix_year.py <年份> [年份...]
示例: python fix_year.py 2013
      python fix_year.py 2014 2015 2016
"""
import re, os, glob, json, sys

YEARS = sys.argv[1:] if len(sys.argv) > 1 else ['2013']

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTENT_DIR = os.path.join(BASE, 'content', 'question')
RAW_OPTS_DIR = os.path.join(BASE, 'tasks', '408-crawler', 'crawled_data')

# Load raw options for the first year
raw_opts = {}
raw_opts_path = os.path.join(RAW_OPTS_DIR, f'{YEARS[0]}_raw_opts.json')
if os.path.exists(raw_opts_path):
    with open(raw_opts_path, encoding='utf-8') as f:
        raw_opts = json.load(f)
    print(f"Loaded raw options from {raw_opts_path}")
else:
    print(f"WARNING: No raw options at {raw_opts_path} (选项恢复将跳过)")

files = []
for Y in YEARS:
    files += glob.glob(os.path.join(CONTENT_DIR, f'{Y}-*.md'))
files = sorted(set(files))
print(f"Found {len(files)} files for years {YEARS}")


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
                if s == f'{c}.' or s.startswith(f'{c}.'):
                    is_opt = True
                    break
            if not is_opt:
                cleaned.append(line)
        lines = cleaned

        if raw_opts and key in raw_opts and len(raw_opts[key]) >= 4:
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

    # ----- Fix 2: MD 表格前后加空行 -----
    new_lines = []
    for i, line in enumerate(lines):
        s = line.strip()
        is_data = s.startswith('|') and '---' not in s
        # 前空行：表格行前、前行非空非表
        if is_data:
            if i > 0:
                prev = lines[i-1].strip()
                if prev and not prev.startswith('|') and not prev.startswith('---'):
                    new_lines.append('')
        # 后空行：非空非表行紧跟在表格数据行后
        if i > 0 and not is_data and s:
            prev = lines[i-1].strip()
            if prev.startswith('|') and '---' not in prev:
                new_lines.append('')
        new_lines.append(line)
    lines = new_lines

    # ----- Fix 3: 子问题前加空行 -----
    new_lines = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if re.match(r'^\d+[）\)]', stripped) and i > 0:
            prev = lines[i-1].strip()
            if prev:
                new_lines.append('')
        new_lines.append(line)
    lines = new_lines

    # ----- Fix 4: 代码块加语言标识符 -----
    new_lines = []
    in_fence = False
    for line in lines:
        if line.strip().startswith('```'):
            if not in_fence:
                rest = line.strip()[3:]
                if not rest:
                    line = '```c'
                in_fence = True
            else:
                in_fence = False
        new_lines.append(line)
    lines = new_lines

    # ----- Fix 5: 删除解析区域的多余标题混入 -----
    tag_pos = -1
    for i, line in enumerate(lines):
        if '[tag_link]' in line:
            tag_pos = i
            break

    if tag_pos >= 0 and num_val <= 40:
        clean_after_tag = []
        keep = True
        for line in lines[tag_pos:]:
            stripped = line.strip()
            if re.match(r'^#{1,6}\s+解答', stripped) or re.match(r'^#{1,6}\s+答案\b', stripped):
                keep = False
                continue
            if keep:
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

print(f"\nFixed {fixed} / {len(files)} files")
