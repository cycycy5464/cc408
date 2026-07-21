"""从 2013_raw_opts.json 恢复 2013 年所有选择题的选项"""
import json, re, os, glob

RAW_FILE = os.path.join(os.path.dirname(__file__), '..', '408-crawler', 'crawled_data', '2013_raw_opts.json')
CONTENT_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'content', 'question')

with open(RAW_FILE, encoding='utf-8') as f:
    raw_opts = json.load(f)

# Subject mapping for 2013:
# ds=1-11, co=12-22, os=23-32, cn=33-40
def get_subject(n):
    if n <= 11: return 'ds'
    if n <= 22: return 'co'
    if n <= 32: return 'os'
    if n <= 40: return 'cn'
    return None

files = sorted(glob.glob(os.path.join(CONTENT_DIR, '2013-*.md')))

fixed = 0
skipped = []
errors = []

for fpath in files:
    basename = os.path.basename(fpath)
    parts = basename.replace('.md', '').split('-')
    if len(parts) < 3:
        continue
    num_str = parts[2]  # e.g. '001'
    num_val = int(num_str)
    if num_val > 40:
        continue

    key = str(num_val)

    if key not in raw_opts or len(raw_opts[key]) < 4:
        errors.append(f"{basename}: insufficient raw data ({raw_opts.get(key, [])})")
        continue

    opts = raw_opts[key][:4]
    letters = ['A', 'B', 'C', 'D']
    option_lines = [f"{letters[i]}.{opt}" for i, opt in enumerate(opts)]

    with open(fpath, encoding='utf-8') as f:
        content = f.read()

    # Check if meaningful option lines already exist
    # Option line = "A" followed by "." (using literal dot, not backslash)
    lines = content.split('\n')
    existing_opts = []
    for line in lines:
        # Match lines like: A\.xxx  or  A.xxx
        stripped = line.strip()
        for c in 'ABCD':
            if stripped.startswith(c + '.') and len(stripped) > 2:
                existing_opts.append(stripped)
                break

    if len(existing_opts) >= 4:
        skipped.append(f"{basename}: already has {len(existing_opts)} options")
        continue

    # Find [tag_link] to insert before it
    tag_idx = -1
    for i, line in enumerate(lines):
        if '[tag_link]' in line:
            tag_idx = i
            break

    if tag_idx == -1:
        errors.append(f"{basename}: no [tag_link] found")
        continue

    # Remove existing empty/fake option lines (A\.\n or A.\n)
    cleaned = []
    for line in lines:
        stripped = line.strip()
        is_option = any(stripped.startswith(c + '.') or stripped.startswith(c + '\\.') for c in 'ABCD')
        if is_option and (len(stripped) <= 2 or stripped[2:].strip() == ''):
            continue  # skip empty option lines
        cleaned.append(line)
    lines = cleaned

    # Recalculate tag_idx
    tag_idx = -1
    for i, line in enumerate(lines):
        if '[tag_link]' in line:
            tag_idx = i
            break
    if tag_idx == -1:
        errors.append(f"{basename}: [tag_link] lost after cleaning")
        continue

    # Insert options before [tag_link]
    new_lines = lines[:tag_idx]
    # Remove trailing blank lines
    while new_lines and new_lines[-1].strip() == '':
        new_lines.pop()
    new_lines.append('')  # blank line before options (Goldmark needs this)
    new_lines += option_lines
    new_lines.append('')  # blank line after options
    new_lines += lines[tag_idx:]

    new_content = '\n'.join(new_lines)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"FIXED {basename}: A.{opts[0]}, B.{opts[1]}, C.{opts[2]}, D.{opts[3]}")
    fixed += 1

print(f"\n=== Summary ===")
print(f"Fixed: {fixed}")
print(f"Skipped (already has options): {len(skipped)}")
print(f"Errors (no data): {len(errors)}")
if skipped:
    for s in skipped:
        print(f"  SKIP: {s}")
if errors:
    for e in errors:
        print(f"  ERR: {e}")
