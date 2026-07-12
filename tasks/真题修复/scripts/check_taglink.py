#!/usr/bin/env python
"""Check which files have [tag_link] in same paragraph as options."""
import glob, os

all_bad = []
with_opts_before = []  # [tag_link] immediately after options (A-D lines)
with_text_before = []  # [tag_link] immediately after text (not options)

for f in sorted(glob.glob('content/question/*.md')):
    with open(f, encoding='utf-8') as fh:
        text = fh.read()

    body = text.split('---', 2)[-1]
    idx = body.find('[tag_link]')
    if idx < 0:
        continue

    # Check blank line before [tag_link]
    before = body[idx-2:idx] if idx >= 2 else ''
    if before == '\n\n':
        continue  # Good file - blank line before [tag_link]

    # Bad file - classify
    fname = os.path.basename(f)
    all_bad.append(fname)

    # Find the line that precedes [tag_link]
    # The [tag_link] line itself starts from the previous \n
    line_start = body.rfind('\n', 0, idx) + 1
    # Find the line before that
    prev_line_start = body.rfind('\n', 0, line_start - 1)
    if prev_line_start < 0:
        prev_line_start = 0
    prev_line_end = line_start - 1  # The \n before [tag_link]
    prev_line = body[prev_line_start:prev_line_end].strip() if prev_line_end > prev_line_start else ''

    # Check if prev_line starts with option marker (D\. C\. B\. A\.)
    # where backslash is literal backslash
    is_option = False
    for c in 'ABCD':
        marker = c + '\\.'
        if prev_line.startswith(marker):
            is_option = True
            break

    if is_option:
        with_opts_before.append(fname)
    else:
        with_text_before.append(fname)

print(f"Total bad files (no blank line before [tag_link]): {len(all_bad)}")
print(f"  [tag_link] after options: {len(with_opts_before)}")
print(f"  [tag_link] after other text: {len(with_text_before)}")
print()

print("Files where [tag_link] is after options (needs fix):")
for fname in with_opts_before:
    print(f"  {fname}")
print()

if with_text_before:
    print("Files where [tag_link] is NOT after options (check):")
    for fname in with_text_before[:30]:
        print(f"  {fname}")
    if len(with_text_before) > 30:
        print(f"  ... and {len(with_text_before) - 30} more")
