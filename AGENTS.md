# AGENTS.md

This repository is used to solve Luogu problems.

Use C++ when the user does not specify a programming language.

## Getting Problems

- When the user asks to solve a problem (for example, "solve P1024"), run `python luogu_spider.py <pid>` (for example, `python luogu_spider.py P1024`) to generate the corresponding `<pid>.md` file.
- Base the solution on the problem statement and samples in `<pid>.md`, then verify it against those samples.

## Task Tracking

- Do not create or update task lists for routine problem-solving requests.

## General Code Format

- Do not include blank lines or comments in source code.

## C++ Code Format

- Use the following structure for C++ solution files:

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
}
```

- Do not include blank lines or comments in C++ source files.
- Name solution files `<pid>.cpp`.

## Compile Command

```powershell
g++ -std=c++23 -O2 -Wall -fno-asm <file>.cpp -o <file>.exe
```

Example:

```powershell
g++ -std=c++23 -O2 -Wall -fno-asm 1.cpp -o 1.exe
```

## Python Code Format

- For large input or output, or when faster I/O is needed, prefer `import sys` and use `sys.stdin.buffer` and `sys.stdout.write`.
