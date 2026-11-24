# 读取洛谷页面

洛谷拦截没有 cookie 的请求：服务器返回 302，重定向回同一地址，同时 `Set-Cookie: C3VK=...`。必须保存 cookie，再带 cookie 请求。

```bash
curl -sSL -c /tmp/opencode/lg.jar -b /tmp/opencode/lg.jar \
  -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36" \
  -o /tmp/opencode/lg.html \
  "https://www.luogu.com.cn/article/<id>"
```

返回 200。页面正文有两处：

- `<noscript>` 内的 `<article>`，纯 HTML。
- `<script id="lentille-context" type="application/json">` 内 JSON 的 `data.article.content`（文章）或 `data.problem`（题目），中文以 Unicode 转义，`json.loads` 即可还原。

无需 JS 渲染。

坑：

- 不带 `-c/-b`：302 死循环。
- 内置 webfetch 工具：报 `Too many redirects`。
- 换页面：替换 URL 末段 ID。
- 帮助中心（`help.luogu.com.cn`）是静态站，直接请求即可，内容在 HTML 正文里。

题解规范页：`https://help.luogu.com.cn/rules/academic/solution-standard`。
