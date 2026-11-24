#!/usr/bin/env python3
"""Lint a Luogu solution article (markdown) against the format used by this skill.

Usage: python3 lint_article.py <article.md>
Exit code 0 means no findings; 1 means at least one finding was printed.
"""
import re
import sys

SECTIONS = ["题意简述", "思路", "复杂度分析", "参考代码"]
FLUFF = ["蒟蒻", "求赞", "求过", "点赞", "管理员", "管理大大", "审核大大", "第一篇题解", "闲聊", "吐槽"]
CJK = "\u4e00-\u9fff"


def split_blocks(text):
    """Return (prose_lines, code_blocks) with fenced code and ::: fold markers removed."""
    prose, codes, cur, fence = [], [], None, None
    for line in text.split("\n"):
        m = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if fence is None and m:
            fence, cur = m.group(1)[0], [m.group(2).strip()]
            continue
        if fence is not None:
            if re.match(r"^\s*" + re.escape(fence) + r"{3,}\s*$", line):
                codes.append(cur)
                fence, cur = None, None
            else:
                cur.append(line)
            continue
        if re.match(r"^\s*:{3,}", line):
            continue
        prose.append(line)
    return prose, codes


def math_spans(text):
    spans = re.findall(r"\$\$(.+?)\$\$", text, re.S)
    rest = re.sub(r"\$\$.+?\$\$", " ", text, flags=re.S)
    spans += re.findall(r"\$([^$\n]+)\$", rest)
    return spans


def main(path):
    text = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    out = []

    def warn(msg):
        out.append(msg)

    prose, codes = split_blocks(text)
    body = "\n".join(prose)

    heads = [l[3:].strip() for l in prose if l.startswith("## ")]
    if heads != SECTIONS:
        warn(f"二级标题应依次为 {SECTIONS}，实际为 {heads}")
    for l in prose:
        if re.match(r"^(#\s|#{3,6}\s)", l):
            warn(f"正文标题最大为二级标题，且不用更深的标题：{l.strip()!r}")
    if not any(c and c[0].lower() in ("cpp", "c++", "") for c in codes):
        warn("缺少 cpp 代码块")
    for c in codes:
        code = "\n".join(c)
        if re.search(r"#pragma\s+GCC\s+optimize|__attribute__\s*\(\(\s*optimize", code):
            warn("代码含 GCC optimize 指令，洛谷评测会编译错误")
    complexity = re.search(r"## 复杂度分析\n(.*?)(?=\n## |\Z)", body, re.S)
    if complexity and "O(" not in complexity.group(1) and "O\\" not in complexity.group(1):
        warn("复杂度分析中没有出现 $O(\\dots)$")

    for word in FLUFF:
        if word in body:
            warn(f"出现与题目无关的用语：{word}")

    for m in math_spans(body):
        if re.search(r"<=|>=|!=|==|\*|%", m):
            warn(f"公式中使用了代码写法：${m.strip()}$（应使用 \\le \\ge \\ne \\times \\bmod 等）")
        if re.search(r"O\(\s*\d+\s*[A-Za-z\\]", m):
            warn(f"大 O 记号带常数：${m.strip()}$")
        if re.search(r"\b[a-z]\.[a-z]\b", m):
            warn(f"公式中出现结构体式写法：${m.strip()}$")

    flat = re.sub(r"\]\([^)]*\)", "]", body)
    flat = re.sub(r"https?://\S+", "", flat)
    flat = re.sub(r"`[^`\n]*`", lambda m: "`" + "x" * max(len(m.group(0)) - 2, 1) + "`", flat)
    for lineno, line in enumerate(flat.split("\n"), 1):
        scan = line.replace("`xx", "`aa")
        for m in re.finditer(rf"[{CJK}][A-Za-z0-9$`]|[A-Za-z0-9$`][{CJK}]", scan):
            warn(f"中文与英文/数字/公式/行内代码之间缺少半角空格：{scan[max(m.start()-6, 0):m.end()+6]!r}")
        for m in re.finditer(rf"[{CJK}][,;:!?()]|[,;:!?()][{CJK}]|[{CJK}]\.(?!\d)", scan):
            warn(f"中文语境使用了半角标点：{scan[max(m.start()-6, 0):m.end()+6]!r}")
        for m in re.finditer(r"[，。；：！？、）] \$|\$ [，。；：！？、（]", scan):
            warn(f"中文标点与公式之间不应有空格：{scan[max(m.start()-6, 0):m.end()+6]!r}")

    in_display = False
    paragraph = []
    paragraphs = []
    for line in prose + [""]:
        if line.strip().startswith("$$") and line.strip().count("$$") == 1:
            in_display = not in_display
            continue
        if in_display or line.strip().startswith("$$"):
            continue
        if line.strip() == "":
            if paragraph:
                paragraphs.append("\n".join(paragraph))
                paragraph = []
        else:
            paragraph.append(line)
    for p in paragraphs:
        first = p.lstrip()
        if first.startswith(("#", "-", "+", "*", "|", "!")) or re.match(r"\d+\.", first):
            continue
        last = p.rstrip()
        if re.search(r"\]\(https?://[^)]*\)$", last):
            continue
        if last[-1] not in "。！？：" and not last.endswith("$$"):
            warn(f"段落未以全角句末标点结束：…{last[-20:]!r}")

    if out:
        print("\n".join(sorted(set(out), key=out.index)))
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
