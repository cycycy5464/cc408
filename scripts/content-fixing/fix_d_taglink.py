#!/usr/bin/env python3
"""
Fix: Add blank line between D\. ... and [tag_link] when consecutive.
Goldmark merges consecutive lines without blank line into one <p>.
JS hides the whole <p> if it contains [tag_link], so D option disappears.
"""
import glob, re, os, sys

os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))

years = sys.argv[1:] if len(sys.argv) > 1 else ['2011']
total_fixed = 0

for year in years:
    files = sorted(glob.glob(f'content/question/{year}-*.md'))
    for fpath in files:
        with open(fpath, encoding='utf-8') as f:
            text = f.read()
        
        # Normalize line endings, strip leading spaces on [tag_link]
        text = re.sub(r'\r\n?', '\n', text)
        text = re.sub(r'^[ \t]+\[tag_link\]', '[tag_link]', text, flags=re.MULTILINE)
        
        # Fix: D-line directly followed by [tag_link] (no blank line between)
        # D\. in text = D + backslash + dot. Regex needs D\\. to match backslash+dot.
        new_text = re.sub(
            r'^(D\\.[^\n]*)\n\[tag_link\]',
            r'\1\n\n[tag_link]',
            text,
            flags=re.MULTILINE
        )
        
        if new_text != text:
            fname = os.path.basename(fpath)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_text)
            print(f"✅ {fname}: fixed D→[tag_link] spacing")
            total_fixed += 1

print(f"\nTotal fixed: {total_fixed} files in {years}")
