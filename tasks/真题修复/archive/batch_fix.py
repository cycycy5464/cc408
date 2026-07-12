#!/usr/bin/env python3
"""
批量修复真题markdown文件中的已知问题
=====================================
规则源自 tasks/真题修复/ 下的经验教训和批量问题修复文档

修复内容：
1. 表格间距：表格前后必须有空行
2. 爬虫残留：删除 ### 解答题 / ## 解答题
3. [tag_link]：为大题(comprehensive)在知识标签后插入
4. 代码块语言标记：C代码块使用 ```c
"""

import re
import os
import glob

QUESTION_DIR = r"D:\projet\cc408\cc408\content\question"


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def iter_body_lines(lines):
    """Yield (index, line) for each line after front matter."""
    seen_first = False
    in_body = False
    for i, line in enumerate(lines):
        if line.strip() == '---':
            if not seen_first:
                seen_first = True
            else:
                in_body = True
            continue
        if in_body:
            yield i, line


def is_table_line(line):
    s = line.strip()
    return s.startswith('|') and s.endswith('|') and '|' in s[1:-1]


def is_table_separator(line):
    s = line.strip()
    return s.startswith('|') and all(c in '|-: ' for c in s)


def fix_table_spacing(content):
    """Fix table-text spacing: ensure blank lines around table blocks."""
    lines = content.split('\n')
    result = []
    in_code_fence = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('```'):
            in_code_fence = not in_code_fence
        if not in_code_fence:
            is_tbl = is_table_line(line) or is_table_separator(line)
            if is_tbl:
                # Previous line: insert blank if non-blank, non-table
                if i > 0:
                    prev = lines[i - 1]
                    ps = prev.strip()
                    if ps and not (is_table_line(prev) or is_table_separator(prev)) and not ps.startswith('```'):
                        result.append('')
                result.append(line)
                # Next line: insert blank if non-blank, non-table
                if i + 1 < len(lines):
                    nxt = lines[i + 1]
                    ns = nxt.strip()
                    if ns and not (is_table_line(nxt) or is_table_separator(nxt)) and not ns.startswith('```'):
                        result.append('')
                i += 1
                continue
        result.append(line)
        i += 1
    return '\n'.join(result)


def remove_residue_headers(content):
    """Remove ### 解答题 and ## 解答题 crawler residue lines."""
    return '\n'.join(
        l for l in content.split('\n')
        if l.strip() not in ('### 解答题', '## 解答题')
    )


def fix_code_block_language(content):
    """Change plain ``` fences to ```c for C-like code blocks."""
    lines = content.split('\n')
    result = []
    i = 0
    in_fence = False
    fence_content = []
    fence_start_index = -1
    fence_was_plain = False

    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('```'):
            lang = line.strip()[3:].strip()
            if not in_fence:
                in_fence = True
                fence_content = []
                fence_start_index = len(result)
                fence_was_plain = (not lang)
                result.append(line)
                i += 1
                continue
            else:
                in_fence = False
                if fence_was_plain:
                    combined = '\n'.join(fence_content)
                    c_patterns = [
                        r'\b(int|char|float|double|void|struct|typedef|return|if|else|for|while|do|switch|case|break|continue)\b',
                        r'\{', r'\};', r'#include', r'//', r'/\*',
                        r'\b(printf|scanf|malloc|free|sizeof)\b',
                        r'\b(load|store|inc|dec|add|sub|push|pop)\b',
                    ]
                    if any(re.search(p, combined) for p in c_patterns):
                        result[fence_start_index] = '```c'
                result.append(line)
                fence_content = []
                i += 1
                continue
        elif in_fence:
            fence_content.append(line)
        result.append(line)
        i += 1
    return '\n'.join(result)


def body_has_tag_link(lines):
    """Check if [tag_link] exists in the body (after front matter)."""
    for _, line in iter_body_lines(lines):
        if line.strip() == '[tag_link]':
            return True
    return False


def find_insertion_point(lines):
    """
    For comprehensive questions, find where to insert [tag_link].
    Returns (insert_index, found_tag_links) or (None, False).
    """
    last_tag_idx = -1
    first_analysis_idx = -1

    for i, line in iter_body_lines(lines):
        s = line.strip()
        # Knowledge tag link: [text](/path)
        if re.match(r'^\[.+\]\(/.+\)$', s):
            last_tag_idx = i
        # Analysis start markers
        if re.match(r'^\s*[1①]\s*[)）]', s) or s.startswith('【答案') or s.startswith('【解析'):
            if first_analysis_idx < 0:
                first_analysis_idx = i

    if last_tag_idx >= 0:
        return last_tag_idx + 1, True
    if first_analysis_idx > 0:
        return first_analysis_idx, False
    return None, False


def add_tag_link_to_comprehensive(content):
    """For comprehensive questions, insert [tag_link] after last knowledge tag."""
    lines = content.split('\n')

    # Only process comprehensive questions
    if not any('question_type: "comprehensive"' in l for l in lines):
        return content

    # Skip if [tag_link] already exists
    if body_has_tag_link(lines):
        return content

    insert_at, has_tags = find_insertion_point(lines)
    if insert_at is None:
        return content

    # Build new content
    before = lines[:insert_at]
    after = lines[insert_at:]

    # Ensure blank line before [tag_link]
    if before and before[-1].strip() != '':
        before.append('')

    # [tag_link] + ensure blank line after
    before.append('[tag_link]')
    if after and after[0].strip() != '':
        after.insert(0, '')

    print(f"  -> [tag_link] at line ~{insert_at + 1} {'(after tags)' if has_tags else '(before analysis)'}")
    return '\n'.join(before + after)


def process_file(filepath):
    """Process a single file with all fixes."""
    original = read_file(filepath)
    content = original

    content = remove_residue_headers(content)
    content = fix_code_block_language(content)
    content = fix_table_spacing(content)
    content = add_tag_link_to_comprehensive(content)

    if content != original:
        write_file(filepath, content)
        return True
    return False


def main():
    files = sorted(glob.glob(os.path.join(QUESTION_DIR, '*.md')))
    changed = 0
    for f in files:
        try:
            if process_file(f):
                print(f"✓ {os.path.basename(f)}")
                changed += 1
        except Exception as e:
            import traceback
            print(f"✗ {os.path.basename(f)}: {e}")
            traceback.print_exc()
    print(f"\n总计: {changed} 个文件已修改, {len(files) - changed} 个文件无变化")


if __name__ == '__main__':
    main()
