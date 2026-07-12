#!/usr/bin/env python
"""Add blank line before [tag_link] so Goldmark renders it as a separate <p>.

The key issue: when [tag_link] is in the same <p> as other content (options or links),
it won't be hidden by the JS step 1 (which only hides pure [tag_link] <p>).
This script ensures [tag_link] is ALWAYS in its own paragraph by adding a blank line
before it, for ALL file types (not just files with options).

Handles both LF (\n) and CRLF (\r\n) line endings.
"""
import glob, os

def needs_fix(fpath):
    """Check if file has [tag_link] that is NOT in its own paragraph."""
    with open(fpath, encoding='utf-8') as f:
        text = f.read()
    
    body = text.split('---', 2)[-1]
    idx = body.find('[tag_link]')
    if idx < 0:
        return False
    
    # A blank line = at least 2 '\n' chars in the last 4 chars before [tag_link]
    last_few = body[max(0, idx-4):idx]
    has_blank = last_few.count('\n') >= 2
    
    return not has_blank

def fix_file(fpath):
    """Add blank line before [tag_link] if not already separated."""
    with open(fpath, encoding='utf-8') as f:
        text = f.read()
    
    body_idx = text.find('---', 2) + 3
    if body_idx < 3:
        body_idx = 0
    body = text[body_idx:]
    
    idx = body.find('[tag_link]')
    if idx < 0:
        return False
    
    last_few = body[max(0, idx-4):idx]
    if last_few.count('\n') >= 2:
        return False  # Already has blank line
    
    # Detect line ending convention
    insert = '\r\n' if '\r\n' in body else '\n'
    
    new_body = body[:idx] + insert + body[idx:]
    new_text = text[:body_idx] + new_body
    
    with open(fpath, 'w', encoding='utf-8', newline='') as f:
        f.write(new_text)
    return True

# === MAIN ===
count = 0
fixed = []

for f in sorted(glob.glob('content/question/*.md')):
    fname = os.path.basename(f)
    if fix_file(f):
        count += 1
        fixed.append(fname)

print(f"Fixed {count} files: added blank line before [tag_link].")

# Verification
print("\nVerification...")
remaining = 0
for f in sorted(glob.glob('content/question/*.md')):
    with open(f, encoding='utf-8') as fh:
        body = fh.read().split('---', 2)[-1]
    idx = body.find('[tag_link]')
    if idx < 0:
        continue
    if body[max(0, idx-4):idx].count('\n') < 2:
        remaining += 1
        print(f"  STILL BROKEN: {os.path.basename(f)}")

print(f"Files still needing fix: {remaining}")
if remaining == 0:
    print("ALL files are now correctly formatted!")
