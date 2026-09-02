import json
import re
import sys

import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Referer": "https://www.luogu.com.cn/",
}


def fetch(url):
    with requests.Session() as s:
        s.headers.update(HEADERS)
        resp = s.get(url, timeout=20)
        resp.raise_for_status()
        return resp.text


def main():
    pid = sys.argv[1] if len(sys.argv) > 1 else "P1024"
    html = fetch(f"https://www.luogu.com.cn/problem/{pid}")
    m = re.search(r'<script id="lentille-context" type="application/json">(.*?)</script>', html, re.S)
    if not m:
        print("Parse failed: problem data not found")
        return
    problem = json.loads(m.group(1))["data"]["problem"]
    pid = problem["pid"]
    content = problem["contenu"]
    name = content.get("name", "")
    desc = content.get("description", "").strip()
    format_in = content.get("formatI", "").strip()
    format_out = content.get("formatO", "").strip()
    hint = (content.get("hint") or "").strip()
    samples = problem.get("samples") or []

    md = [f"# {pid} {name}", "", "## 题目描述", "", desc, "", "## 输入格式", "", format_in, "", "## 输出格式", "", format_out]
    for i, (input_data, output_data) in enumerate(samples, 1):
        md += ["", f"## 样例输入 {i}", "", "```", input_data.rstrip(), "```", "", f"## 样例输出 {i}", "", "```", output_data.rstrip(), "```"]
    if hint:
        md += ["", "## 提示", "", hint, ""]

    with open(f"{pid}.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"Saved {pid}.md")


if __name__ == "__main__":
    main()
