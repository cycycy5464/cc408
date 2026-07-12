"""为 2013 年选项行间加空行，确保 Goldmark 分段渲染"""
import re, os, glob

CONTENT_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'content', 'question')

files = sorted(glob.glob(os.path.join(CONTENT_DIR, '2013-*.md')))

fixed = 0
for fpath in files:
    basename = os.path.basename(fpath)
    parts = basename.replace('.md', '').split('-')
    if len(parts) < 3:
        continue
    num_val = int(parts[2])
    if num_val > 40:
        continue

    with open(fpath, encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    new_lines = []
    i = 0
    modified = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        is_option = any(stripped.startswith(c + '.') for c in 'ABCD')

        if is_option:
            # Check if the next line is also an option
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                is_next_option = any(next_line.startswith(c + '.') for c in 'ABCD')
                if is_next_option:
                    # Add blank line between options
                    new_lines.append(line)
                    new_lines.append('')  # blank line
                    modified = True
                    i += 1
                    continue

        # Check if D option is followed by [tag_link] without blank line
        if is_option and line[0] == 'D':
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if '[tag_link]' in next_line:
                    # Add blank line between D and [tag_link]
                    new_lines.append(line)
                    new_lines.append('')
                    modified = True
                    i += 1
                    continue

        new_lines.append(line)
        i += 1

    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        print(f"FIXED {basename}")
        fixed += 1

print(f"\nFixed {fixed} files with blank line fixes")
