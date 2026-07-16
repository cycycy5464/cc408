#!/usr/bin/env python3
"""
课后题提取脚本 v6
从各科目章节 docx 文件中提取课后题，生成单题 md 文档
支持: 操作系统、计算机网络、计算机组成原理、数据结构
修复: 跳过目录区、按节号匹配答案、处理交叉顺序、支持降序答案格式
用法: python scripts/extract-chapter-exercises.py [subject]
"""

import zipfile
import xml.etree.ElementTree as ET
import re
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(r"D:\BaiduSyncdisk\考研相关\ppt\os27")
OUTPUT_BASE = Path(r"E:\programcc408\cc408\content\question\chapterExercises")

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

# 科目配置
SUBJECTS = {
    "os": {
        "name": "操作系统",
        "source_dir": BASE_DIR / "os" / "os章节",
        "output_dir": OUTPUT_BASE / "os",
        "chapters": [
            ("第1章_计算机系统概述.docx", "chapter1-computer-system", "计算机系统概述", {
                "1.1": "操作系统概念", "1.2": "操作系统结构",
                "1.3": "程序运行环境", "1.6": "性能指标",
            }),
            ("第2章_进程与线程.docx", "chapter2-process-thread", "进程与线程", {
                "2.1": "进程与线程", "2.2": "处理机调度",
                "2.3": "同步与互斥", "2.4": "死锁",
            }),
            ("第3章_内存管理.docx", "chapter3-memory", "内存管理", {
                "3.1": "内存管理概念", "3.2": "虚拟内存管理",
            }),
            ("第4章_文件管理.docx", "chapter4-file", "文件管理", {
                "4.1": "文件", "4.2": "目录", "4.3": "文件系统",
            }),
            ("第5章_输入输出管理.docx", "chapter5-io", "输入输出管理", {
                "5.1": "I/O设备", "5.2": "设备管理", "5.3": "磁盘",
            }),
        ],
    },
    "cn": {
        "name": "计算机网络",
        "source_dir": BASE_DIR / "计网" / "计算机网络",
        "output_dir": OUTPUT_BASE / "cn",
        "chapters": [
            ("第_1_章.docx", "chapter1-physical", "物理层", {
                "1.1": "通信基础", "1.2": "传输介质",
                "1.3": "物理层设备",
            }),
            ("第_2_章.docx", "chapter2-data-link", "数据链路层", {
                "2.1": "数据链路层功能", "2.2": "差错控制",
                "2.3": "流量控制与可靠传输", "2.4": "介质访问控制",
                "2.5": "局域网", "2.6": "广域网", "2.7": "数据链路层设备",
            }),
            ("第_3_章.docx", "chapter3-network", "网络层", {
                "3.1": "网络层功能", "3.2": "路由算法",
                "3.3": "IPv4", "3.4": "IPv6",
                "3.5": "路由协议", "3.6": "IP组播",
                "3.7": "移动IP", "3.8": "网络层设备",
            }),
            ("第_4_章.docx", "chapter4-transport", "传输层", {
                "4.1": "传输层概述", "4.2": "UDP",
                "4.3": "TCP", "4.4": "TCP拥塞控制",
            }),
            ("第_5_章.docx", "chapter5-application", "应用层", {
                "5.1": "网络应用模型", "5.2": "DNS",
                "5.3": "HTTP", "5.4": "电子邮件",
                "5.5": "FTP", "5.6": "即时通信",
            }),
            ("第_6_章.docx", "chapter6-security", "网络安全", {
                "6.1": "网络安全概述", "6.2": "加密与认证",
                "6.3": "密钥分配", "6.4": "数字签名",
                "6.5": "报文完整性", "6.6": "网络安全协议",
            }),
        ],
    },
    "co": {
        "name": "计算机组成原理",
        "source_dir": BASE_DIR / "计组" / "计算机组成原理",
        "output_dir": OUTPUT_BASE / "co",
        "chapters": [
            ("第_1_章_计_算_机_系_统_概_述.docx", "chapter1-overview", "计算机系统概述", {
                "1.1": "计算机发展历程", "1.2": "计算机系统层次结构",
                "1.3": "计算机性能指标",
            }),
            ("第_2_章.docx", "chapter2-number", "数据的表示和运算", {
                "2.1": "数制与编码", "2.2": "定点数的表示和运算",
                "2.3": "浮点数的表示和运算", "2.4": "算术逻辑单元",
            }),
            ("第_3_章_存_储_系_统.docx", "chapter3-memory", "存储系统", {
                "3.1": "存储器概述", "3.2": "主存储器",
                "3.3": "外部存储器", "3.4": "高速缓冲存储器",
                "3.5": "虚拟存储器",
            }),
            ("第_4_章.docx", "chapter4-instruction", "指令系统", {
                "4.1": "指令格式", "4.2": "指令的寻址方式",
                "4.3": "CISC和RISC",
            }),
            ("第_5_章.docx", "chapter5-cpu", "中央处理器", {
                "5.1": "CPU功能和基本结构", "5.2": "指令执行过程",
                "5.3": "数据通路的功能和基本结构", "5.4": "控制器的功能和工作方式",
                "5.5": "微程序控制器", "5.6": "硬布线控制器",
                "5.7": "指令流水线",
            }),
            ("第_6_章.docx", "chapter6-bus", "总线", {
                "6.1": "总线概述", "6.2": "总线仲裁",
                "6.3": "总线操作和定时", "6.4": "总线标准",
            }),
            ("第_7_章_输_入_输_出_系_统.docx", "chapter7-io", "输入输出系统", {
                "7.1": "I/O系统基本概念", "7.2": "I/O接口",
                "7.3": "I/O方式",
            }),
        ],
    },
    "ds": {
        "name": "数据结构",
        "source_dir": BASE_DIR / "数构" / "数据结构",
        "output_dir": OUTPUT_BASE / "ds",
        "chapters": [
            ("第_1_章_绪_论.docx", "chapter1-intro", "绪论", {
                "1.1": "什么是数据结构", "1.2": "算法和算法分析",
            }),
            ("第_2_章.docx", "chapter2-linear-list", "线性表", {
                "2.1": "线性表的定义", "2.2": "线性表的顺序表示",
                "2.3": "线性表的链式表示",
            }),
            ("第_3_章.docx", "chapter3-stack-queue", "栈、队列和数组", {
                "3.1": "栈", "3.2": "队列",
                "3.3": "数组", "3.4": "特殊矩阵",
            }),
            ("第_4_章.docx", "chapter4-string", "串", {
                "4.1": "串的定义", "4.2": "串的模式匹配",
            }),
            ("第_5_章.docx", "chapter5-tree", "树与二叉树", {
                "5.1": "树的基本概念", "5.2": "二叉树",
                "5.3": "二叉排序树", "5.4": "平衡二叉树",
                "5.5": "赫夫曼树", "5.6": "树与森林",
            }),
            ("第_6_章.docx", "chapter6-graph", "图", {
                "6.1": "图的基本概念", "6.2": "图的存储",
                "6.3": "图的遍历", "6.4": "最小生成树",
                "6.5": "最短路径", "6.6": "拓扑排序",
                "6.7": "关键路径",
            }),
            ("第_7_章.docx", "chapter7-search", "查找", {
                "7.1": "查找的基本概念", "7.2": "顺序查找和折半查找",
                "7.3": "B树和B+树", "7.4": "散列表",
            }),
            ("第_8_章.docx", "chapter8-sort", "排序", {
                "8.1": "排序的基本概念", "8.2": "插入排序",
                "8.3": "交换排序", "8.4": "选择排序",
                "8.5": "归并排序", "8.6": "基数排序",
                "8.7": "排序比较",
            }),
        ],
    },
}


def extract_paragraphs(docx_path: str) -> list[str]:
    """从docx文件中提取所有段落文本"""
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
    return paragraphs


def is_toc_entry(line: str) -> bool:
    """检测是否为目录条目"""
    return bool(re.search(r"(本节[习试]题精选|答案与解析|本章[小疑])\s*\d+\s*$", line))


def extract_section_num(title: str) -> str:
    """从标题中提取节号 (如 1.1, 2.3) - 支持带星号的标题"""
    m = re.match(r"\*?(\d+\.\d+)", title)
    return m.group(1) if m else ""


def detect_answer_order(answer_lines: list[str]) -> str:
    """检测答案是升序还是降序排列"""
    numbers = []
    for line in answer_lines:
        m = re.match(r"^(\d{1,2})[.．]\s*([A-D])", line)
        if m:
            numbers.append(int(m.group(1)))
            if len(numbers) >= 2:
                break
    if len(numbers) >= 2:
        return "descending" if numbers[0] > numbers[1] else "ascending"
    return "ascending"


def parse_all_sections(paragraphs: list[str]) -> dict:
    """
    解析所有段落，提取习题和答案内容，按节号分组
    返回: { "1.1": {"exercise": [...], "answer": [...]}, ... }
    """
    # 第一遍: 收集所有标记的位置和类型
    markers = []  # [(index, type, section_num)]
    for i, line in enumerate(paragraphs):
        if is_toc_entry(line):
            continue
        if "本节习题精选" in line or "本节试题精选" in line:
            markers.append((i, "exercise", extract_section_num(line)))
        elif "答案与解析" in line:
            markers.append((i, "answer", extract_section_num(line)))
        elif "本章疑难点" in line or "本章小结" in line:
            markers.append((i, "end", ""))

    # 第二遍: 根据标记切分内容
    result = defaultdict(lambda: {"exercise": [], "answer": []})
    
    # 检测是否为特殊结构 (answer content 在 answer header 之前)
    has_answer_before_header = False
    for idx, (start, sec_type, sec_num) in enumerate(markers):
        if sec_type == "answer" and sec_num:
            # 检查 answer header 之前的内容是否包含答案
            if idx > 0:
                prev_start = markers[idx - 1][0]
                prev_content = paragraphs[prev_start + 1:start]
                # 检查是否包含答案格式 (仅匹配答案行，不匹配题干)
                for line in prev_content:
                    # 匹配答案行: 01. D 或 01.D (仅字母，无额外文本)
                    if re.match(r"^(\d{1,2})[.．]\s*([A-D])\s*$", line):
                        has_answer_before_header = True
                        break
            break
    
    if has_answer_before_header:
        # 特殊处理 (OS Ch3): 文件结构交错，answer content在header之前
        # exercise正常处理，answer需要特殊处理

        # exercise: 标准路径
        for idx, (start, sec_type, sec_num) in enumerate(markers):
            if sec_type != "exercise" or not sec_num:
                continue
            end = len(paragraphs)
            for next_idx in range(idx + 1, len(markers)):
                if markers[next_idx][1] != "exercise":
                    end = markers[next_idx][0]
                    break
            result[sec_num]["exercise"] = paragraphs[start + 1:end]

        # answer: 每个header向前搜索choice answers，向后搜索comprehensive answers
        for idx, (start, sec_type, sec_num) in enumerate(markers):
            if sec_type != "answer" or not sec_num:
                continue

            # 找到前一个标记和后一个标记的范围
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

            # 在prev_end到start之间搜索所有choice answers和comprehensive answers
            all_choice = []
            all_comp = []
            in_comp = False
            for i in range(prev_end, start):
                line = paragraphs[i]
                # choice answer
                if re.match(r"^(\d{1,2})[.．]\s*([A-D])\s*$", line):
                    all_choice.append(line)
                    in_comp = False
                # comprehensive answer
                elif re.match(r"^(\d{1,2})[.．]\s*【(解答|解)】", line):
                    in_comp = True
                    all_comp.append(line)
                elif in_comp:
                    all_comp.append(line)
                else:
                    in_comp = False

            # 在start+1到next_start之间搜索comprehensive answers
            in_comp = False
            for i in range(start + 1, next_start):
                line = paragraphs[i]
                if re.match(r"^(\d{1,2})[.．]\s*【(解答|解)】", line):
                    in_comp = True
                    all_comp.append(line)
                elif in_comp:
                    all_comp.append(line)
                else:
                    in_comp = False

            # 处理选择答案顺序
            order = detect_answer_order(all_choice)
            if order == "descending":
                all_choice = all_choice[::-1]

            result[sec_num]["answer"] = all_comp + all_choice
    else:
        # 标准处理: 答案内容在 answer header 和下一个标记之间
        for idx, (start, sec_type, sec_num) in enumerate(markers):
            if sec_type == "end":
                continue
            # 找到下一个标记的位置
            if idx + 1 < len(markers):
                end = markers[idx + 1][0]
            else:
                end = len(paragraphs)
            # 提取内容 (跳过标记行本身)
            content = paragraphs[start + 1:end]
            if sec_num:
                # 检查答案是否为降序排列
                if sec_type == "answer":
                    order = detect_answer_order(content)
                    if order == "descending":
                        content = content[::-1]
                result[sec_num][sec_type] = content

    return dict(result)


def parse_questions(exercise_lines: list[str], answer_lines: list[str]) -> list[dict]:
    """解析习题内容，提取题目和答案"""
    questions = []
    current_type = None
    current_q = None

    for line in exercise_lines:
        # 检测题目类型
        if re.search(r"单项选择题", line):
            current_type = "choice"
            continue
        if re.search(r"综合应用题", line):
            current_type = "comprehensive"
            continue

        # 匹配题目编号
        q_match = re.match(r"^(\d{1,2})[.．]\s*(.*)", line)
        if q_match:
            if current_q:
                questions.append(current_q)
            current_q = {
                "number": int(q_match.group(1)),
                "type": current_type or "choice",
                "stem": q_match.group(2),
                "options": [],
                "is_national_exam": bool(re.search(r"【\d{4}统考真题】", line)),
            }
            continue

        # 匹配选项
        opt_match = re.match(r"^([A-D])[.．]\s*(.*)", line)
        if opt_match and current_q:
            current_q["options"].append(f"{opt_match.group(1)}. {opt_match.group(2)}")
            continue

        # 累加题目内容
        if current_q:
            current_q["stem"] += "\n" + line

    if current_q:
        questions.append(current_q)

    # 解析答案
    answers = parse_answers(answer_lines)
    for q in questions:
        q["answer"] = answers.get(q["number"], "")

    return questions


def parse_answers(answer_lines: list[str]) -> dict:
    """解析答案内容，返回 {题号: 答案} 字典。选择题答案优先于综合题答案。"""
    choice_answers = {}
    comprehensive_answers = {}
    
    for line in answer_lines:
        # 格式: 一、单项选择题 01.D 或 一 单项选择题 01.D (章节标签+答案同行，优先匹配)
        m = re.search(r"单项选择题\s*(\d{1,2})[.．]\s*([A-D])", line)
        if m:
            choice_answers[int(m.group(1))] = m.group(2)
            continue
        
        # 格式: N N. X 或 NN. X 或 NN.X (选择题答案) - 严格匹配，仅字母
        # 支持数字中有空格的情况，如 "0 1. B"
        m = re.match(r"^(\d\s*\d)[.．]\s*([A-D])\s*$", line)
        if m:
            num_str = m.group(1).replace(" ", "")
            choice_answers[int(num_str)] = m.group(2)
            continue
        
        # 格式: NN.【解答】 或 NN. 【解答】 (综合题答案)
        m = re.match(r"^(\d{1,2})[.．]\s*【(解答|解)】", line)
        if m:
            comprehensive_answers[int(m.group(1))] = "【解答】"
            continue
    
    # 合并：选择题答案仅在综合题答案不存在时才写入
    answers = {}
    answers.update(comprehensive_answers)
    for k, v in choice_answers.items():
        if k not in answers:
            answers[k] = v
    return answers


def generate_md(question: dict, chapter_title: str, section_kp: str, q_index: int, subject_name: str) -> str:
    """生成单个题目的md文件内容"""
    q_type = question["type"]
    stem = question["stem"].strip()
    options = question.get("options", [])
    answer = question.get("answer", "")
    is_national = question.get("is_national_exam", False)
    num = question["number"]

    title = f"{chapter_title} 第{num}题"
    tags = "['课后题', '统考真题']" if is_national else "['课后题']"

    lines = [
        "---",
        f'title: "{title}"',
        "date: 2026-07-16",
        "type: question",
        "years:",
        '  - "课后题"',
        "subjects:",
        f'  - "{subject_name}"',
        "knowledge_points:",
        f'  - "{section_kp}"',
        f'question_type: "{q_type}"',
        "difficulty: 2",
        'source: "课后题"',
        f"number: {q_index}",
        f"tags: {tags}",
        "---",
        "",
        stem,
        "",
    ]

    if options:
        lines.extend(options)
        lines.append("")

    lines.append("[tag_link]")
    lines.append("")

    if q_type == "choice":
        lines.append(f"正确答案：{answer}" if answer else "正确答案：")
    else:
        lines.append(answer)

    return "\n".join(lines)


def process_chapter(docx_file: str, output_dir: str, chapter_title: str, kp_map: dict, 
                   subject_name: str, source_dir: Path, output_base: Path, chapter_idx: int):
    """处理单个章节"""
    docx_path = source_dir / docx_file
    if not docx_path.exists():
        print(f"[SKIP] {docx_path}")
        return 0

    print(f"[INFO] {docx_file}")
    paragraphs = extract_paragraphs(str(docx_path))

    sections = parse_all_sections(paragraphs)
    q_index = 1

    for sec_num, data in sorted(sections.items()):
        exercise_lines = data["exercise"]
        answer_lines = data["answer"]

        if not exercise_lines:
            continue
        if not answer_lines:
            print(f"  [WARN] {sec_num} 无答案")
            continue

        section_kp = kp_map.get(sec_num, chapter_title)
        questions = parse_questions(exercise_lines, answer_lines)

        non_national = [q for q in questions if not q.get("is_national_exam")]
        national = [q for q in questions if q.get("is_national_exam")]

        print(f"  {sec_num}: {len(questions)}题 (课后:{len(non_national)}, 统考:{len(national)})")

        for q in non_national:
            md = generate_md(q, chapter_title, section_kp, q_index, subject_name)
            filename = f"{subject_name.lower().replace(' ', '-')}-chapter{chapter_idx}-{q_index:03d}.md"
            filepath = output_base / output_dir / filename
            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(md)
            q_index += 1

    print(f"  完成: {q_index - 1} 题")
    return q_index - 1


def main():
    import sys
    
    # 确定要处理的科目
    subjects_to_process = list(SUBJECTS.keys())
    if len(sys.argv) > 1:
        subjects_to_process = [sys.argv[1]]
    
    print("=" * 60)
    print("课后题提取脚本 v6")
    print("=" * 60)
    
    total_questions = 0
    
    for subject_key in subjects_to_process:
        if subject_key not in SUBJECTS:
            print(f"未知科目: {subject_key}")
            continue
        
        subject = SUBJECTS[subject_key]
        print(f"\n{'='*60}")
        print(f"处理科目: {subject['name']}")
        print(f"{'='*60}")
        
        for i, (docx_file, output_dir, chapter_title, kp_map) in enumerate(subject["chapters"]):
            count = process_chapter(
                docx_file, output_dir, chapter_title, kp_map,
                subject["name"], subject["source_dir"], subject["output_dir"], i + 1
            )
            total_questions += count
            print()
    
    print(f"\n全部完成，共提取 {total_questions} 题")


if __name__ == "__main__":
    main()
