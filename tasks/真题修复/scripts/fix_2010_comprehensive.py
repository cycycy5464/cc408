"""Fix 2010 comprehensive questions: [tag_link], dedup, cleanup"""
import re, os

QUESTION_DIR = r"D:\projet\cc408\cc408\content\question"

for filename in sorted(os.listdir(QUESTION_DIR)):
    if not filename.startswith('2010-') or not filename.endswith('.md'):
        continue
    fp = os.path.join(QUESTION_DIR, filename)
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'question_type: "comprehensive"' not in content:
        continue

    # Normalize line endings
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    orig = content

    # 1. Deduplicate [tag_link]
    lines = content.split('\n')
    seen_tag = False
    new_lines = []
    for line in lines:
        if line.strip() == '[tag_link]':
            if not seen_tag:
                seen_tag = True
                new_lines.append(line)
        else:
            new_lines.append(line)
    content = '\n'.join(new_lines)

    # 2. Remove JS code pollution (IndexedDB/quizDB) by truncating at known markers
    # If the file has quizDB code, find where it starts and remove
    js_markers = [
        'if(typeof window.quizDB',
        'window.quizDB',
        'function toggleSolutionDetail',
        'async function collectAnswerQuiz',
    ]
    for marker in js_markers:
        idx = content.find(marker)
        if idx >= 0:
            content = content[:idx]

    # 3. Remove leaked next-question content
    for marker in ['计算机网络 47', '组成原理 43', '数据结构 42']:
        idx = content.find(marker)
        if idx > 0:
            # Check that this is in the body (not front matter)
            before = content[:idx]
            if '---' in before[before.find('---')+3:]:
                content = content[:idx].rstrip()

    # 4. Add [tag_link] if missing - find insertion point
    if '[tag_link]' not in content:
        lines = content.split('\n')
        # Find last knowledge tag link in body
        last_tag_idx = -1
        in_body = False
        seen_first_sep = False
        for i, line in enumerate(lines):
            s = line.strip()
            if s == '---' and not seen_first_sep:
                seen_first_sep = True
                continue
            if s == '---' and seen_first_sep:
                in_body = True
                continue
            if in_body and re.match(r'^\[.+\]\(/.+\)$', s):
                last_tag_idx = i

        if last_tag_idx >= 0:
            # Insert [tag_link] after last tag, with blank line
            before = lines[:last_tag_idx+1]
            after = lines[last_tag_idx+1:]
            if before and before[-1].strip() != '':
                before.append('')
            before.append('[tag_link]')
            if after and after[0].strip() != '':
                after.insert(0, '')
            content = '\n'.join(before + after)
        else:
            # No knowledge tags - insert before "1）"
            find_start = content.find('---', content.find('---') + 3) + 3
            body = content[find_start:]
            m = re.search(r'^\s*[1①]\s*[)）]', body, re.MULTILINE)
            if m:
                insert_pos = find_start + m.start()
                before = content[:insert_pos]
                after = content[insert_pos:]
                if before and before[-1] != '\n':
                    before += '\n'
                if not before.endswith('\n\n'):
                    before += '\n'
                before += '[tag_link]\n\n'
                content = before + after

    # 5. Fix table spacing
    lines = content.split('\n')
    result = []
    in_fence = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('```'):
            in_fence = not in_fence
        if not in_fence:
            stripped = line.strip()
            is_tbl = stripped.startswith('|') and stripped.endswith('|') and '|' in stripped[1:-1]
            if is_tbl:
                if i > 0 and lines[i-1].strip() and not lines[i-1].strip().startswith('|'):
                    result.append('')
                result.append(line)
                if i + 1 < len(lines) and lines[i+1].strip() and not lines[i+1].strip().startswith('|'):
                    result.append('')
                i += 1
                continue
        result.append(line)
        i += 1
    content = '\n'.join(result)

    # 6. Clean up excessive blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    # 7. Remove trailing "查看答案与解析" / "收藏" buttons that leaked in
    content = re.sub(r'\n*查看答案与解析.*$', '', content)
    content = re.sub(r'\n*收藏\s*$', '', content)

    if content != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'✅ {filename}')
    else:
        print(f'   {filename} (unchanged)')
