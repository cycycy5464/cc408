"""Fix 2010 choice questions: remove blank lines between A/B/C/D options"""
import re, os, glob

QUESTION_DIR = r"D:\projet\cc408\cc408\content\question"

for fp in sorted(glob.glob(os.path.join(QUESTION_DIR, '2010-*.md'))):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'question_type: "choice"' not in content:
        continue

    lines = content.split('\n')

    # Find the option block
    in_body = False
    seen_first_sep = False
    opt_start = -1
    opt_end = -1

    for i, line in enumerate(lines):
        s = line.strip()
        if s == '---':
            if not seen_first_sep:
                seen_first_sep = True
            else:
                in_body = True
            continue
        if not in_body:
            continue

        # Match A. B. C. D. options (with or without backslash before dot)
        if re.match(r'^[A-D]\\?\.', s):
            if opt_start < 0:
                opt_start = i
            opt_end = i

        if s == '[tag_link]' and opt_start >= 0:
            break

    if opt_start < 0:
        continue

    # Remove blank lines between options
    modified = False
    new_lines = []
    in_opt_block = False

    for i, line in enumerate(lines):
        s = line.strip()
        if i == opt_start:
            in_opt_block = True
            new_lines.append(line)
        elif in_opt_block and i <= opt_end:
            if s:
                new_lines.append(line)
            else:
                modified = True
        else:
            if in_opt_block and i > opt_end:
                in_opt_block = False
            new_lines.append(line)

    if modified:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        print(f'✅ {os.path.basename(fp)}')
