"""
fix_option_blanklines.py — Add blank lines between choice option lines (A\. B\. C\. D\.)
so Goldmark renders each as a separate <p> tag.

Background: Hugo's Goldmark markdown renderer merges consecutive lines
without blank lines into a single <p> (with <br> breaks). The JS extractOptions()
splits on </p>, so merged options aren't extracted.

Pattern to fix:
    A\. xxx
    B\. xxx
    C\. xxx
    D\. xxx

Should become:
    A\. xxx

    B\. xxx

    C\. xxx

    D\. xxx

Usage:
    python fix_option_blanklines.py <years...>
    python fix_option_blanklines.py 2011 2012

If no years given, scans all files.
"""

import os, re, sys, glob, json

CONTENT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'content', 'question')

def fix_file(fpath):
    """Ensure options lines have blank lines between them."""
    with open(fpath, encoding='utf-8') as f:
        text = f.read()
    
    original = text
    
    # Find the body (after frontmatter)
    # Split on ---\n
    parts = text.split('\n---\n', 1)
    if len(parts) != 2:
        # Try other split patterns
        if text.startswith('---'):
            end_idx = text.find('\n---\n', 4)
            if end_idx > 0:
                parts = [text[:end_idx], text[end_idx+5:]]
            else:
                return False
    
    if len(parts) != 2:
        return False
    
    frontmatter = parts[0] + '\n---\n'
    body = parts[1]
    orig_body = body
    
    # Option pattern: A\., B\., C\., D\. at line start
    opt_re = re.compile(r'^[A-D]\\\.')
    
    lines = body.split('\n')
    new_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip('\r')
        
        # Check if this line starts an option sequence
        if opt_re.match(stripped) and stripped.startswith('A\\.') or stripped.startswith('A\\ '):
            # Found potential start of options block
            # Collect consecutive option lines
            opts = []
            j = i
            while j < len(lines) and opt_re.match(lines[j].rstrip('\r')):
                opts.append(j)
                j += 1
            
            if len(opts) >= 2:
                # This is an options block (2+ consecutive option lines)
                # Check if there are blank lines between them
                needs_fix = False
                for k in range(len(opts) - 1):
                    gap = opts[k+1] - opts[k]
                    if gap == 1:  # Direct adjacency, no blank line
                        needs_fix = True
                        break
                
                if needs_fix:
                    # Rebuild: A\....\n\nB\....\n\nC\....\n\nD\....
                    for k, line_idx in enumerate(opts):
                        new_lines.append(lines[line_idx])
                        # Add blank line after each option EXCEPT the last
                        if k < len(opts) - 1:
                            new_lines.append('')
                    i = j
                    continue
        
        new_lines.append(line)
        i += 1
    
    body = '\n'.join(new_lines)
    text = frontmatter + body
    
    if text != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(text)
        return True
    
    return False

def main():
    years = sys.argv[1:] if len(sys.argv) > 1 else None
    
    files = sorted(os.listdir(CONTENT_DIR))
    fixed = []
    skipped = []
    
    for fname in files:
        if not fname.endswith('.md') or not fname.startswith('20'):
            continue
        
        if years:
            # Check if file matches any of the given years
            matched = False
            for y in years:
                if fname.startswith(y):
                    matched = True
                    break
            if not matched:
                continue
        
        fpath = os.path.join(CONTENT_DIR, fname)
        if fix_file(fpath):
            fixed.append(fname)
    
    print(f"Fixed: {len(fixed)} files")
    for f in fixed:
        print(f"  {f}")

if __name__ == '__main__':
    main()
