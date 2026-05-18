#!/usr/bin/env python3
"""
论文 PDF → 博客 Markdown 模板生成器

用法:
    python tools/paper2post.py paper/论文名.pdf

需要先安装依赖:
    pip install pdfplumber
"""

import sys, os, re
from datetime import date

def extract_text(pdf_path):
    try:
        import pdfplumber
    except ImportError:
        print("错误: 请先安装 pdfplumber: pip install pdfplumber")
        sys.exit(1)

    with pdfplumber.open(pdf_path) as pdf:
        pages = []
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                pages.append(text)
            if i > 15:  # 最多读 16 页
                break
    return "\n\n".join(pages)


def guess_title(text):
    """猜测论文标题：第一段非空文本或 Abstract 前的内容"""
    lines = text.strip().split("\n")
    # 收集前几行直到遇到明显不是标题的内容
    title_lines = []
    for line in lines[:30]:
        s = line.strip()
        if not s or len(s) < 5:
            if title_lines:
                break
            continue
        if re.match(r'(Abstract|Introduction|Related|1\.|I\.)', s, re.I):
            break
        title_lines.append(s)
    return " ".join(title_lines[:3]) if title_lines else "PAPER_TITLE"


def guess_abstract(text):
    """提取摘要"""
    m = re.search(
        r'(?:Abstract|ABSTRACT)[\s—-]*(.*?)(?:\n\s*\n|\n(?:1\.|I\.|Introduction|Related))',
        text, re.DOTALL
    )
    return m.group(1).strip().replace("\n", " ") if m else ""


def find_sections(text):
    """找到所有疑似章节标题"""
    pattern = r'^(\d+\.?\s+[A-Z][A-Za-z\s-]{3,60})$'
    return re.findall(pattern, text, re.MULTILINE)


def slugify(title):
    """标题 → 安全文件名"""
    s = re.sub(r'[^\w\s-]', '', title.lower())
    s = re.sub(r'[-\s]+', '-', s)
    return s.strip('-')[:80]


def generate_post(pdf_path, title, abstract, sections):
    basename = os.path.splitext(os.path.basename(pdf_path))[0]
    slug = slugify(title)
    today = date.today()

    sections_md = ""
    for sec in sections:
        sec_clean = sec.strip()
        level = "##" if not sec.startswith(("2.", "3.", "4.", "5.", "6.")) else "###"
        sections_md += f"\n{level} {sec_clean}\n\n> TODO: 补充内容\n\n"

    return f'''---
title: "{title}"
author: timzxx
date: {today}
categories: [3D重建]
tags: [卫星影像, 3DGS]
description: >
  {abstract[:200] if abstract else title}
---

## 基本信息

- **论文**: {title}
- **arXiv**: [TODO](https://arxiv.org/abs/xxxx)
- **GitHub**: [TODO](https://github.com/xxx/xxx)
- **Project Page**: [TODO]()
- **作者及单位**: TODO

## 背景与动机

> TODO: 已有方法的问题是什么？本文的动机？

## 方法

### 整体流程

> TODO: 概述 pipeline

{sections_md}
### 损失函数

> TODO: 训练用的损失函数

## 实验

### 数据集与设置

> TODO

### 对比实验

| 方法 | PSNR ↑ | SSIM ↑ | LPIPS ↓ |
|------|--------|--------|---------|
| 方法A | xx.xx | x.xxx | x.xxx |
| **{title[:40]}** | **xx.xx** | **x.xxx** | **x.xxx** |

### 消融实验

> TODO

### 定性结果

> TODO

## 总结

- **贡献1**: TODO
- **贡献2**: TODO
- **局限**: TODO

## 思考与启发

> TODO: 方法和自己的研究方向有什么关联？
'''


def main():
    if len(sys.argv) < 2:
        print("用法: python tools/paper2post.py paper/论文名.pdf")
        sys.exit(1)

    pdf_path = sys.argv[1]
    if not os.path.exists(pdf_path):
        print(f"文件不存在: {pdf_path}")
        sys.exit(1)

    print(f"正在提取: {pdf_path}")
    text = extract_text(pdf_path)
    print(f"  提取了 {len(text)} 个字符")

    title = guess_title(text)
    abstract = guess_abstract(text)
    sections = find_sections(text)

    print(f"  标题: {title}")
    print(f"  摘要: {abstract[:100]}..." if len(abstract) > 100 else f"  摘要: {abstract}")
    print(f"  找到 {len(sections)} 个章节: {[s[:30] for s in sections]}")

    output = generate_post(pdf_path, title, abstract, sections)

    # 确保 _posts 目录存在
    os.makedirs("_posts", exist_ok=True)

    slug = slugify(title)
    today = date.today()
    out_path = f"_posts/{today}-{slug}.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"\n已生成: {out_path}")
    print(f"请打开编辑，替换所有 TODO 占位符。")


if __name__ == "__main__":
    main()
