#!/usr/bin/env python3
"""Check answer 3.2 content more carefully"""
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

# Check the range 749-1741 more carefully
# The answer 3.2 should have comprehensive answers for 3.2
print("=== Checking range 749-1741 for 3.2 answers ===")

# Look for answer patterns
answer_patterns = []
for i in range(749, 1741):
    line = paragraphs[i]
    if re.match(r"^(\d{1,2})[.．]\s*【(解答|解)】", line):
        answer_patterns.append((i, line))
    elif re.match(r"^(\d{1,2})[.．]\s*([A-D])\s*$", line):
        answer_patterns.append((i, line))

print(f"Total answer patterns found: {len(answer_patterns)}")

# Show all answer patterns
for idx, line in answer_patterns:
    print(f"  [{idx}] {line[:60]}")

# Check if there are answer patterns for 3.2 (should be 1-22)
print("\n=== Checking for answer patterns 1-22 ===")
for i in range(749, 1741):
    line = paragraphs[i]
    if re.match(r"^(\d{1,2})[.．]\s*【(解答|解)】", line):
        m = re.match(r"^(\d{1,2})[.．]\s*【(解答|解)】", line)
        num = int(m.group(1))
        if 1 <= num <= 22:
            print(f"  [{i}] {line[:60]}")
