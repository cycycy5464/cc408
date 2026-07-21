#!/usr/bin/env python
"""Fix sub-question spacing in comprehensive question files.

Sub-question markers like 1）2）3）4） need blank lines between them for
Goldmark to render as separate paragraphs.

Uses only Chinese parenthesis ） as sub-question marker (analysis section).
Skips sub-question lines when locating the last knowledge link anchor.
"""
import glob, os, re

# Only match Chinese parenthesis ） (analysis section, NOT stem)
SUBQ_RE = re.compile(r'^\s*\d+）')

def fix_file(fpath):
    with open(fpath, encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find frontmatter end
    fm_end = -1
    for i, line in enumerate(lines):
        stripped = line.rstrip('\n\r')
        if i == 0 and stripped == '---':
            continue
        if stripped == '---' and i > 0:
            fm_end = i
            break
    if fm_end < 0:
        return False
    
    body = lines[fm_end+1:]
    
    # Find analysis section start:
    # 1. After [tag_link] (preferred anchor for choice questions)
    # 2. After the last knowledge link [...](...) that is NOT a sub-question line
    tag_idx = -1
    for i, line in enumerate(body):
        if '[tag_link]' in line:
            tag_idx = i
            break
    
    if tag_idx >= 0:
        analysis_start = tag_idx + 1
        while analysis_start < len(body) and not body[analysis_start].rstrip('\n\r'):
            analysis_start += 1
    else:
        # Find last knowledge link EXCLUDING sub-question lines
        last_link = -1
        for i, line in enumerate(body):
            stripped = line.rstrip('\n\r')
            # Skip lines that start with sub-question markers
            if SUBQ_RE.match(stripped):
                continue
            if re.search(r'\[[^\]]+\]\([^)]+\)', stripped):
                last_link = i
        
        if last_link < 0:
            return False
        
        analysis_start = last_link + 1
        # Skip blank lines
        while analysis_start < len(body) and not body[analysis_start].rstrip('\n\r'):
            analysis_start += 1
    
    if analysis_start >= len(body):
        return False
    
    # Process analysis section:
    # Find all sub-question markers. For each one that isn't the first content
    # line in the analysis section, ensure blank line before it.
    in_code = False
    modified = False
    new_body = list(body)
    offset = 0
    
    for abs_i in range(analysis_start, len(body)):
        adjusted_i = abs_i + offset
        if adjusted_i >= len(new_body):
            break
        
        stripped = new_body[adjusted_i].rstrip('\n\r')
        
        if stripped.startswith('```'):
            in_code = not in_code
            continue
        if in_code or not stripped:
            continue
        
        if SUBQ_RE.match(stripped):
            # Is this the very first non-blank line in analysis section?
            is_first = True
            for j in range(analysis_start, abs_i):
                if new_body[j + offset].rstrip('\n\r'):
                    is_first = False
                    break
            
            if not is_first and adjusted_i > 0:
                prev = new_body[adjusted_i - 1].rstrip('\n\r')
                if prev:
                    le = '\n'
                    if '\r\n' in new_body[adjusted_i]:
                        le = '\r\n'
                    new_body.insert(adjusted_i, le)
                    offset += 1
                    modified = True
    
    if not modified:
        return False
    
    with open(fpath, 'w', encoding='utf-8', newline='') as f:
        f.writelines(lines[:fm_end+1] + new_body)
    return True

# === MAIN ===
count = 0
fixed = []
unchanged = 0

for f in sorted(glob.glob('content/question/*.md')):
    fname = os.path.basename(f)
    if fix_file(f):
        count += 1
        fixed.append(fname)

print(f"Fixed {count} files: added blank lines before sub-question markers.")
if count > 0:
    print("\nFixed files:")
    for f in fixed:
        print(f"  {f}")

# Verification
print("\nVerification (strict consecutive check)...")
remaining = []
for f in sorted(glob.glob('content/question/*.md')):
    with open(f, encoding='utf-8') as fh:
        text = fh.read()
    
    body = text.split('---', 2)[-1]
    lines = body.split('\n')
    
    # Find analysis section start
    # After [tag_link] or after last non-subq knowledge link
    tag_idx = -1
    for i, line in enumerate(lines):
        if '[tag_link]' in line:
            tag_idx = i
            break
    
    if tag_idx >= 0:
        anchor = tag_idx + 1
    else:
        last_link = -1
        for i, line in enumerate(lines):
            stripped = line.rstrip('\r')
            if SUBQ_RE.match(stripped):
                continue
            if re.search(r'\[[^\]]+\]\([^)]+\)', stripped):
                last_link = i
        if last_link < 0:
            continue
        anchor = last_link + 1
    
    # Check for consecutive sub-question markers
    in_code = False
    has_issue = False
    for i in range(anchor, len(lines)):
        stripped = lines[i].rstrip('\r')
        if stripped.startswith('```'):
            in_code = not in_code
            continue
        if in_code or not stripped:
            continue
        if SUBQ_RE.match(stripped):
            if i > anchor:
                prev_line = lines[i-1].rstrip('\r')
                if prev_line != '':
                    # Previous line is NOT blank
                    if not SUBQ_RE.match(prev_line):
                        # And NOT also a sub-question marker
                        has_issue = True
                        break
    
    if has_issue:
        remaining.append(os.path.basename(f))

print(f"Files with consecutive (non-blank-separated) sub-questions: {len(remaining)}")
for f in remaining:
    print(f"  {f}")

if len(remaining) == 0:
    print("ALL comprehensive files are now correctly formatted!")
