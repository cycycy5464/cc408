#!/usr/bin/env python3
"""Check answer content for 3.2"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import zipfile
import xml.etree.ElementTree as ET
import re

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
docx_path = r"D:\BaiduSyncdisk\考研相关\ppt\os27\os\os章节\第3章_内存管理.docx"

paragraphs = []
with zipfile.ZipFile(docx_path) as z:
    xml_content = z.read("word/document.xml")
root = ET.fromstring(xml_content)
for p in root.findall(".//w:p", NS):
    texts = []
    for r in p.findall(".//w:r", NS):
        for t in r.findall("w:t", NS):
            if t.text:
                texts.append(t.text)
    line = "".join(texts).strip()
    if line:
        paragraphs.append(line)

# The answer 3.2 header is at line 1741
# The answer 3.1 header is at line 3585
# The exercise 3.2 header is at line 2219

# According to the script's logic:
# For answer 3.2 (line 1741):
#   prev_end = 522 (exercise 3.1 start)
#   next_start = 2219 (exercise 3.2 start)
#   Search range: 522-1741 and 1741-2219

# For answer 3.1 (line 3585):
#   prev_end = 2220 (exercise 3.2 start)
#   next_start = len(paragraphs)
#   Search range: 2220-3585 and 3585-end

# But the actual answer content is:
# Answer 3.2: lines 749-1741 (before answer 3.2 header)
# Answer 3.1: lines 3249-3585 (before answer 3.1 header)

# Let me check what's in range 1742-2219 (after answer 3.2 header)
print("=== Range 1742-2219 (after answer 3.2 header) ===")
choice_32_after = []
comp_32_after = []
in_comp = False
pattern = r"^(\d{1,2})[.．]\s*【(解答|解)】"

for i in range(1742, 2219):
    line = paragraphs[i]
    if re.match(r"^(\d{1,2})[.．]\s*([A-D])\s*$", line):
        choice_32_after.append((i, line))
        in_comp = False
    elif re.match(pattern, line):
        in_comp = True
        comp_32_after.append((i, line))
    elif in_comp:
        comp_32_after.append((i, line))
    else:
        in_comp = False

print(f"Choice answers: {len(choice_32_after)}")
print(f"Comprehensive answers: {len(comp_32_after)}")

# Show first few
if choice_32_after:
    print("\nFirst 5 choice answers:")
    for idx, line in choice_32_after[:5]:
        print(f"  [{idx}] {line}")

if comp_32_after:
    print("\nFirst 5 comp answers:")
    for idx, line in comp_32_after[:5]:
        print(f"  [{idx}] {line}")

# Check what's in range 749-1741 (before answer 3.2 header)
print("\n=== Range 749-1741 (before answer 3.2 header) ===")
choice_32_before = []
comp_32_before = []
in_comp = False

for i in range(749, 1741):
    line = paragraphs[i]
    if re.match(r"^(\d{1,2})[.．]\s*([A-D])\s*$", line):
        choice_32_before.append((i, line))
        in_comp = False
    elif re.match(pattern, line):
        in_comp = True
        comp_32_before.append((i, line))
    elif in_comp:
        comp_32_before.append((i, line))
    else:
        in_comp = False

print(f"Choice answers: {len(choice_32_before)}")
print(f"Comprehensive answers: {len(comp_32_before)}")

# Show first few
if choice_32_before:
    print("\nFirst 5 choice answers:")
    for idx, line in choice_32_before[:5]:
        print(f"  [{idx}] {line}")

if comp_32_before:
    print("\nFirst 5 comp answers:")
    for idx, line in comp_32_before[:5]:
        print(f"  [{idx}] {line}")
