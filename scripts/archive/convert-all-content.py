#!/usr/bin/env python3
"""Universal content converter for all 408 subjects"""
import os, re, shutil, sys, argparse

parser = argparse.ArgumentParser(description='Convert 408 content to Hugo format')
parser.add_argument('subject', choices=['computer-org', 'os', 'network'], help='Subject to convert')
parser.add_argument('--src', required=True, help='Source directory path')
parser.add_argument('--images', help='Global images directory path')
args = parser.parse_args()

SUBJECT = args.subject

# Subject configs
CONFIGS = {
    'computer-org': {
        'dir': '组成原理',
        'tag': 'computer-org',
        'static_dir': 'computer-org',
        'label': '计算机组成原理',
        'chapters': {
            '概述.md': ('ch00-overview/introduction.md', 0, '概论'),
            '概述-计算机系统层次结构.md': ('ch00-overview/system-hierarchy.md', 1, '计算机系统层次结构'),
            '概述-计算机性能指标.md': ('ch00-overview/performance.md', 2, '计算机性能指标'),
            '数据表示和计算.md': ('ch01-data-representation/data-index.md', 3, '数据表示与计算'),
            '数据表示-整数的表示.md': ('ch01-data-representation/integers.md', 4, '整数的表示'),
            '数据表示-浮点数表示.md': ('ch01-data-representation/float.md', 5, '浮点数表示'),
            '数据表示-类型转换.md': ('ch01-data-representation/type-conversion.md', 6, '类型转换'),
            '数据表示-运算电路.md': ('ch01-data-representation/circuits.md', 7, '运算电路'),
            '存储系统.md': ('ch02-memory/memory-index.md', 8, '存储系统'),
            '存储系统-存储系统概述.md': ('ch02-memory/overview.md', 9, '存储系统概述'),
            '存储系统-内存.md': ('ch02-memory/ram.md', 10, '内存'),
            '存储系统-Cache.md': ('ch02-memory/cache.md', 11, 'Cache'),
            '存储系统-外存.md': ('ch02-memory/external.md', 12, '外存'),
            '存储系统-虚拟存储器.md': ('ch02-memory/virtual.md', 13, '虚拟存储器'),
            '指令系统.md': ('ch03-instruction/instruction-index.md', 14, '指令系统'),
            '指令系统-指令集种类.md': ('ch03-instruction/types.md', 15, '指令集种类'),
            '指令系统-格式和寻址方式.md': ('ch03-instruction/format-addressing.md', 16, '指令格式与寻址方式'),
            '指令系统-数据对齐方式.md': ('ch03-instruction/data-alignment.md', 17, '数据对齐'),
            '指令系统-指令操作码.md': ('ch03-instruction/opcode.md', 18, '指令操作码'),
            '指令系统-高级语言和机器码.md': ('ch03-instruction/hll-machine.md', 19, '高级语言与机器码'),
            '中央处理器.md': ('ch04-cpu/cpu-index.md', 20, '中央处理器'),
            'CPU-功能和结构.md': ('ch04-cpu/function-structure.md', 21, 'CPU功能与结构'),
            'CPU-控制器.md': ('ch04-cpu/controller.md', 22, '控制器'),
            'CPU-异常与中断.md': ('ch04-cpu/exceptions.md', 23, '异常与中断'),
            'CPU-指令流水线.md': ('ch04-cpu/pipeline.md', 24, '指令流水线'),
            'CPU-多处理器.md': ('ch04-cpu/multiprocessor.md', 25, '多处理器'),
            '总线.md': ('ch05-bus/bus.md', 26, '总线'),
            '总线和输入输出系统.md': ('ch05-bus/bus-io.md', 27, '总线和I/O系统'),
            'I_O 系统.md': ('ch06-io/io-system.md', 28, 'I/O系统'),
        }
    },
    'os': {
        'dir': '操作系统',
        'tag': 'os',
        'static_dir': 'os',
        'label': '操作系统',
        'chapters': {
            '计算机系统概述.md': ('ch00-overview/computer-overview.md', 0, '计算机系统概述'),
            '操作系统概念.md': ('ch00-overview/os-concept.md', 1, '操作系统概念'),
            '操作系统结构.md': ('ch00-overview/os-structure.md', 2, '操作系统结构'),
            '程序运行环境.md': ('ch00-overview/program-env.md', 3, '程序运行环境'),
            '进程管理.md': ('ch01-process/process-index.md', 4, '进程管理'),
            '进程管理-进程和线程.md': ('ch01-process/process-thread.md', 5, '进程与线程'),
            '进程管理-处理机调度.md': ('ch01-process/scheduling.md', 6, '处理机调度'),
            '进程管理-同步和互斥.md': ('ch01-process/sync-mutex.md', 7, '同步与互斥'),
            '进程管理-经典同步问题.md': ('ch01-process/classic-sync.md', 8, '经典同步问题'),
            '进程管理-死锁.md': ('ch01-process/deadlock.md', 9, '死锁'),
            '内存管理.md': ('ch02-memory/memory-index.md', 10, '内存管理'),
            '内存管理-内存管理概念.md': ('ch02-memory/concepts.md', 11, '内存管理概念'),
            '内存管理-虚拟内存管理.md': ('ch02-memory/virtual.md', 12, '虚拟内存管理'),
            '文件管理.md': ('ch03-file/file-index.md', 13, '文件管理'),
            '文件管理-文件.md': ('ch03-file/file-basics.md', 14, '文件'),
            '文件管理-目录.md': ('ch03-file/directory.md', 15, '目录'),
            '文件管理-文件系统.md': ('ch03-file/filesystem.md', 16, '文件系统'),
            'I_O 管理.md': ('ch04-io/io-index.md', 17, 'I/O管理'),
            'I_O 管理-I_O 设备.md': ('ch04-io/devices.md', 18, 'I/O设备'),
            'I_O 管理-设备管理.md': ('ch04-io/device-mgmt.md', 19, '设备管理'),
            'I_O 管理-磁盘.md': ('ch04-io/disk.md', 20, '磁盘'),
        }
    },
    'network': {
        'dir': '计算机网络',
        'tag': 'network',
        'static_dir': 'network',
        'label': '计算机网络',
        'chapters': {
            '计算机网络体系结构.md': ('ch00-overview/arch-index.md', 0, '计算机网络体系结构'),
            '体系结构-分层结构.md': ('ch00-overview/layered.md', 1, '分层结构'),
            '体系结构-各层协议总结.md': ('ch00-overview/protocol-summary.md', 2, '各层协议总结'),
            '体系结构-网络设备总结.md': ('ch00-overview/device-summary.md', 3, '网络设备总结'),
            '物理层.md': ('ch01-physical/phy-index.md', 4, '物理层'),
            '物理层-通信概念.md': ('ch01-physical/communication.md', 5, '通信概念'),
            '物理层-编码和调制.md': ('ch01-physical/encoding.md', 6, '编码与调制'),
            '物理层-交换方式.md': ('ch01-physical/switching.md', 7, '交换方式'),
            '物理层-物理层设备.md': ('ch01-physical/devices.md', 8, '物理层设备'),
            '数据链路层.md': ('ch02-datalink/dl-index.md', 9, '数据链路层'),
            '数据链路层-组帧.md': ('ch02-datalink/framing.md', 10, '组帧'),
            '数据链路层-差错控制.md': ('ch02-datalink/error-control.md', 11, '差错控制'),
            '数据链路层-流量控制.md': ('ch02-datalink/flow-control.md', 12, '流量控制'),
            '数据链路层-介质访问控制.md': ('ch02-datalink/mac.md', 13, '介质访问控制'),
            '数据链路层-局域网和广域网.md': ('ch02-datalink/lan-wan.md', 14, '局域网与广域网'),
            '数据链路层-数据链路层设备.md': ('ch02-datalink/devices.md', 15, '数据链路层设备'),
            '网络层.md': ('ch03-network/nw-index.md', 16, '网络层'),
            '网络层-IP.md': ('ch03-network/ip.md', 17, 'IP协议'),
            '网络层-ARP.md': ('ch03-network/arp.md', 18, 'ARP协议'),
            '网络层-ICMP.md': ('ch03-network/icmp.md', 19, 'ICMP协议'),
            '网络层-DHCP.md': ('ch03-network/dhcp.md', 20, 'DHCP协议'),
            '网络层-路由算法.md': ('ch03-network/routing.md', 21, '路由算法'),
            '网络层-SDN.md': ('ch03-network/sdn.md', 22, 'SDN'),
            '网络层-网络层设备.md': ('ch03-network/devices.md', 23, '网络层设备'),
            '传输层.md': ('ch04-transport/tp-index.md', 24, '传输层'),
            '传输层-TCP.md': ('ch04-transport/tcp.md', 25, 'TCP'),
            '传输层-UDP.md': ('ch04-transport/udp.md', 26, 'UDP'),
            '应用层.md': ('ch05-application/app-index.md', 27, '应用层'),
            '应用层-网络应用模型.md': ('ch05-application/app-model.md', 28, '网络应用模型'),
            '应用层-DNS.md': ('ch05-application/dns.md', 29, 'DNS'),
            '应用层-FTP.md': ('ch05-application/ftp.md', 30, 'FTP'),
            '应用层-电子邮件.md': ('ch05-application/email.md', 31, '电子邮件'),
            '应用层-万维网.md': ('ch05-application/www.md', 32, '万维网'),
        }
    }
}

cfg = CONFIGS.get(SUBJECT)
if not cfg:
    print(f'Unknown subject: {SUBJECT}')
    sys.exit(1)

SRC_BASE = args.src
DST_BASE = f"content/docs/{cfg['tag']}"
IMG_DST = f"static/images/docs/{cfg['static_dir']}"
TMP = f'_tmp/{cfg["tag"]}_source'

os.makedirs(TMP, exist_ok=True)
os.makedirs(IMG_DST, exist_ok=True)

# Copy source files
for fname in os.listdir(SRC_BASE):
    if fname.endswith('.md'):
        shutil.copy2(os.path.join(SRC_BASE, fname), os.path.join(TMP, fname))

def fix_image_paths(text, src_filename):
    text = re.sub(r'!\[\]\(\.\./images/([^)]+)\)', rf'![](/images/docs/{cfg["static_dir"]}/\1)', text)
    stem = os.path.splitext(src_filename)[0]
    text = re.sub(rf'!\[([^\]]*)\]\({re.escape(stem)}\.assets/([^)]+)\)', rf'![](/images/docs/{cfg["static_dir"]}/\2)', text)
    return text

def process_code_blocks(text):
    """Convert indented code blocks to fenced code blocks without forcing language."""
    lines = text.split('\n')
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Match lines with 4-space indent that look like code (not just list items)
        if line.startswith('    ') and line.strip() and not line.strip().startswith(('-', '*', '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
            code_lines = []
            while i < len(lines) and lines[i].startswith('    '):
                code_lines.append(lines[i][4:])
                i += 1
            # Use plain fenced block without language tag
            result.append('```')
            result.extend(code_lines)
            result.append('```')
            result.append('')
            continue
        result.append(line)
        i += 1
    return '\n'.join(result)

def get_tags(title):
    if any(k in title for k in ['概述', '概念', '层次', '结构']):
        return ['基础概念']
    if any(k in title for k in ['表示', '计算', '电路', '类型转换', '对齐']):
        return ['数据表示']
    if '存储' in title or '内存' in title or '外存' in title or 'Cache' in title or '虚拟' in title:
        return ['存储系统']
    if any(k in title for k in ['指令', '寻址', '操作码']):
        return ['指令系统']
    if any(k in title for k in ['CPU', '中央处理器', '控制', '流水线', '中断', '异常']):
        return ['CPU']
    if any(k in title for k in ['总线', 'I/O', '输入输出']):
        return ['总线', 'I/O']
    if any(k in title for k in ['进程', '线程', '调度', '同步', '互斥', '死锁']):
        return ['进程管理']
    if any(k in title for k in ['文件', '目录', '文件系统']):
        return ['文件管理']
    if any(k in title for k in ['磁盘', '设备']):
        return ['设备管理']
    if any(k in title for k in ['体系结构', '分层', '协议', '网络设备']):
        return ['体系结构']
    if '物理' in title:
        return ['物理层']
    if any(k in title for k in ['数据链路', '组帧', '差错', '流量', '介质', 'LAN', 'WAN']):
        return ['数据链路层']
    if any(k in title for k in ['网络层', 'IP', 'ARP', 'ICMP', 'DHCP', '路由', 'SDN']):
        return ['网络层']
    if any(k in title for k in ['传输层', 'TCP', 'UDP']):
        return ['传输层']
    if any(k in title for k in ['应用层', 'DNS', 'FTP', '邮件', '万维网', '网络应用']):
        return ['应用层']
    return ['基础概念']

def get_difficulty(title, weight):
    if any(k in title for k in ['概述', '概念', '总结']):
        return 1
    if weight <= 10:
        return 1
    if weight <= 20:
        return 2
    return 3

count = 0
for chinese_name, (rel_path, weight, tags_extra) in cfg['chapters'].items():
    src = os.path.join(TMP, chinese_name)
    dst = os.path.join(DST_BASE, rel_path)
    if not os.path.exists(src):
        print(f'  MISSING: {chinese_name}')
        continue
    with open(src, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'^# .+\n?', '', content, count=1)
    content = re.sub(r'^[🔥💡]+\s*(高|低|中)优先级\s*\n', '', content, re.MULTILINE)
    content = process_code_blocks(content)
    content = fix_image_paths(content, chinese_name)

    tags = get_tags(tags_extra)
    diff = get_difficulty(tags_extra, weight)

    fm = f'''---
title: "{tags_extra}"
date: 2026-06-25
weight: {weight}
tags: [{', '.join(tags)}]
difficulty: {diff}
prerequisites: []
subject: {cfg['tag']}
chapter: {weight // 10 + 1}
chapter_title: "{tags_extra}"
---

'''
    full = fm + content.strip() + '\n'
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(full)
    print(f'  OK {chinese_name}')
    count += 1

print(f'\nConverted {count} files for {SUBJECT}')

# Copy images from .assets folders and global images/
asset_folders = [f for f in os.listdir(SRC_BASE) if os.path.isdir(os.path.join(SRC_BASE, f)) and f.endswith('.assets')]
img_count = 0
for folder in asset_folders:
    src_folder = os.path.join(SRC_BASE, folder)
    for img in os.listdir(src_folder):
        src = os.path.join(src_folder, img)
        dst = os.path.join(IMG_DST, img)
        if os.path.isfile(src) and not os.path.exists(dst):
            shutil.copy2(src, dst)
            img_count += 1

global_src = args.images
if global_src and os.path.isdir(global_src):
    for img in os.listdir(global_src):
        src = os.path.join(global_src, img)
        dst = os.path.join(IMG_DST, img)
        if os.path.isfile(src) and not os.path.exists(dst):
            shutil.copy2(src, dst)
            img_count += 1

print(f'Copied {img_count} images')
