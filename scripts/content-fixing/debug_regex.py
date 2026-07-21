import re

with open('content/question/2014-ds-001.md', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
print(f"Total lines: {len(lines)}")

opt_lines = []
for i, l in enumerate(lines):
    s = l.strip()
    # Try various patterns
    m1 = bool(re.match(r'^[A-D]\.', s))
    m2 = bool(re.match(r'^[A-D]\\.', s))
    m3 = bool(re.match(r'^[A-D]\\\.', s))
    
    if m1 or m2 or m3:
        which = "m1" if m1 else ("m2" if m2 else "m3")
        opt_lines.append((i, s, which))
        print(f"  line {i}: [{which}] |{s[:50]}|")

print(f"\nFound {len(opt_lines)} option lines")

# Now check every char of line 26/27 for debugging
if len(lines) > 27:
    for lnum in [26, 27]:
        s = lines[lnum]
        print(f"\nline {lnum} raw: {repr(s)}")
        for j, c in enumerate(s[:5]):
            print(f"  [{j}] {repr(c)} ord={ord(c)}")
