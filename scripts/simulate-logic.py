#!/usr/bin/env python3
"""Check what answers are being assigned to each section"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import zipfile
import xml.etree.ElementTree as ET
import re
from collections import defaultdict

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

# Find markers
markers = []
for i, line in enumerate(paragraphs):
    if "本节习题精选" in line or "本节试题精选" in line:
        m = re.match(r"\*?(\d+\.\d+)", line)
        markers.append((i, "exercise", m.group(1) if m else ""))
    elif "答案与解析" in line:
        m = re.match(r"\*?(\d+\.\d+)", line)
        markers.append((i, "answer", m.group(1) if m else ""))

print("=== Markers ===")
for idx, (start, sec_type, sec_num) in enumerate(markers):
    print(f"  [{idx}] line {start}: {sec_type} {sec_num}")

# Simulate the script's special path logic
print("\n=== Simulating special path logic ===")
for idx, (start, sec_type, sec_num) in enumerate(markers):
    if sec_type != "answer" or not sec_num:
        continue

    # Find prev_end and next_start
    prev_end = 0
    for prev_idx in range(idx - 1, -1, -1):
        if markers[prev_idx][1] != "answer":
            prev_end = markers[prev_idx][0] + 1
            break
    next_start = len(paragraphs)
    for next_idx in range(idx + 1, len(markers)):
        if markers[next_idx][1] != "answer":
            next_start = markers[next_idx][0]
            break

    print(f"\nAnswer {sec_num} (line {start}):")
    print(f"  prev_end: {prev_end}, next_start: {next_start}")

    # Search for answers in range prev_end to start
    all_choice = []
    all_comp = []
    in_comp = False
    for i in range(prev_end, start):
        line = paragraphs[i]
        if re.match(r"^(\d{1,2})[.．]\s*([A-D])\s*$", line):
            all_choice.append((i, line))
            in_comp = False
        elif re.match(r"^(\d{1,2})[.．]\s*【(解答|解)】", line):
            in_comp = True
            all_comp.append((i, line))
        elif in_comp:
            all_comp.append((i, line))
        else:
            in_comp = False

    # Search for answers in range start+1 to next_start
    for i in range(start + 1, next_start):
        line = paragraphs[i]
        if re.match(r"^(\d{1,2})[.．]\s*([A-D])\s*$", line):
            all_choice.append((i, line))
            in_comp = False
        elif re.match(r"^(\d{1,2})[.．]\s*【(解答|解)】", line):
            in_comp = True
            all_comp.append((i, line))
        elif in_comp:
            all_comp.append((i, line))
        else:
            in_comp = False

    print(f"  Choice answers: {len(all_choice)}")
    print(f"  Comprehensive answers: {len(all_comp)}")

    # Show first few
    if all_choice:
        print(f"  First choice: {all_choice[0][1][:50]}")
    if all_comp:
        print(f"  First comp: {all_comp[0][1][:50]}")
