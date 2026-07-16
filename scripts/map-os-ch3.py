#!/usr/bin/env python3
"""Map the actual answer ranges for OS Ch3"""
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

# Markers:
# [0] line 521: exercise 3.1
# [1] line 1741: answer 3.2
# [2] line 2219: exercise 3.2
# [3] line 3585: answer 3.1

# Actual structure:
# 521-748: exercise 3.1
# 749-1425: comprehensive answers for 3.2 (22→1, descending)
# 1428-1739: choice answers for 3.1 (61→01, descending)
# 1741: answer header 3.2 (一、单项选择题 label)
# 1742-2218: ???
# 2219: exercise header 3.2
# 2220-3248: exercise 3.2
# 3249-3395: comprehensive answers for 3.1 (11→1, descending)
# 3398-3584: choice answers for 3.1 (72→01, descending)
# 3585: answer header 3.1

# So the correct mapping should be:
# Answer 3.2 comprehensive: 749-1425 (22 comprehensive questions)
# Answer 3.2 choice: NONE in this file (3.2 only has comprehensive answers)
# Answer 3.1 comprehensive: 3249-3395 (11 comprehensive questions)
# Answer 3.1 choice: 3398-3584 (67 choice questions, 72→01 descending)

# Wait - let me check: 3.2 has both choice and comprehensive?
# Let me check the exercise content to see what question types are in each section

# Exercise 3.1 content (lines 522-1740)
exercise_31 = paragraphs[522:1741]
# Exercise 3.2 content (lines 2220-3584)
exercise_32 = paragraphs[2220:3585]

# Count question types in exercise 3.1
choice_31 = 0
comp_31 = 0
current_type = None
for line in exercise_31:
    if re.search(r"单项选择题", line):
        current_type = "choice"
    elif re.search(r"综合应用题", line):
        current_type = "comp"
    elif re.match(r"^(\d{1,2})[.．]\s*(.*)", line):
        if current_type == "choice":
            choice_31 += 1
        elif current_type == "comp":
            comp_31 += 1

print(f"Exercise 3.1: {choice_31} choice, {comp_31} comprehensive")
print(f"  Total lines: {len(exercise_31)}")

# Count question types in exercise 3.2
choice_32 = 0
comp_32 = 0
current_type = None
for line in exercise_32:
    if re.search(r"单项选择题", line):
        current_type = "choice"
    elif re.search(r"综合应用题", line):
        current_type = "comp"
    elif re.match(r"^(\d{1,2})[.．]\s*(.*)", line):
        if current_type == "choice":
            choice_32 += 1
        elif current_type == "comp":
            comp_32 += 1

print(f"Exercise 3.2: {choice_32} choice, {comp_32} comprehensive")
print(f"  Total lines: {len(exercise_32)}")

# Check answer 3.2 range more carefully
# Look for choice answer patterns in 1428-1739
print("\n=== Choice answers in range 1428-1739 (for 3.1) ===")
choice_nums = []
for i in range(1428, 1740):
    line = paragraphs[i]
    m = re.match(r"^(\d{1,2})[.．]\s*([A-D])\s*$", line)
    if m:
        choice_nums.append(int(m.group(1)))
print(f"Numbers: {choice_nums[:10]}...{choice_nums[-10:]}")
print(f"Count: {len(choice_nums)}")

# Check comprehensive answers in range 749-1425 (for 3.2)
print("\n=== Comprehensive answers in range 749-1425 (for 3.2) ===")
comp_nums = []
for i in range(749, 1426):
    line = paragraphs[i]
    m = re.match(r"^(\d{1,2})[.．]\s*【(解答|解)】", line)
    if m:
        comp_nums.append(int(m.group(1)))
print(f"Numbers: {comp_nums}")
print(f"Count: {len(comp_nums)}")

# Check comprehensive answers in range 3249-3395 (for 3.1)
print("\n=== Comprehensive answers in range 3249-3395 (for 3.1) ===")
comp_nums_31 = []
for i in range(3249, 3396):
    line = paragraphs[i]
    m = re.match(r"^(\d{1,2})[.．]\s*【(解答|解)】", line)
    if m:
        comp_nums_31.append(int(m.group(1)))
print(f"Numbers: {comp_nums_31}")
print(f"Count: {len(comp_nums_31)}")

# Check choice answers in range 3398-3584 (for 3.1)
print("\n=== Choice answers in range 3398-3584 (for 3.1) ===")
choice_nums_31 = []
for i in range(3398, 3585):
    line = paragraphs[i]
    m = re.match(r"^(\d{1,2})[.．]\s*([A-D])\s*$", line)
    if m:
        choice_nums_31.append(int(m.group(1)))
print(f"Numbers: {choice_nums_31[:10]}...{choice_nums_31[-10:]}")
print(f"Count: {len(choice_nums_31)}")
