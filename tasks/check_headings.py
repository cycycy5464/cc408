#!/usr/bin/env python3
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('content/exam/408quiz/backup/2010-content.md', 'rb') as f:
    t = f.read().decode('utf-8')

# Find all heading lines
for m in re.finditer(r'^#{2,5}\s.*$', t, re.MULTILINE):
    line = m.group()
    print(repr(line))
