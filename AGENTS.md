# AGENTS.md

本项目（D:\lg）用于洛谷刷题。

## 获取题目

- 用户说"完成某题"（如"完成 P1024"）时，运行 `python luogu_spider.py <pid>`（如 `python luogu_spider.py P1024`），生成 `<pid>.md` 题目文件。
- 依据 `<pid>.md` 中的题面、样例编写解答，并用样例验证。

## C++ 代码格式

- 解答文件基于 `template.cpp` 编写，沿用其结构（`#include <bits/stdc++.h>`、`using namespace std;`、`cin.tie(nullptr)->sync_with_stdio(false);` 等）。
- 解答文件命名为 `<pid>.cpp`。

## 编译命令

```powershell
g++ -std=c++23 -O2 -Wall -fno-asm <file>.cpp -o <file>.exe --static -lstdc++exp -lm
```

示例：

```powershell
g++ -std=c++23 -O2 -Wall -fno-asm 1.cpp -o 1.exe --static -lstdc++exp -lm
```
