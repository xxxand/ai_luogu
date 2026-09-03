# AGENTS.md

This project is for solving Luogu problems.

If no language is specified, use C++.

## Getting Problems

- When the user says to solve a problem (e.g., "solve P1024"), run `python luogu_spider.py <pid>` (e.g., `python luogu_spider.py P1024`) to generate the `<pid>.md` problem file.
- Write the solution based on the problem statement and samples in `<pid>.md`, and verify it against the samples.

## Task Tracking

- Do not create or update task lists for routine problem-solving requests in this repository.

## General Code Format

- Write code without blank lines or comments in all programming languages used in this project.

## C++ Code Format

- Write solution files based on `template.cpp`, following its structure (`#include <bits/stdc++.h>`, `using namespace std;`, `cin.tie(nullptr)->sync_with_stdio(false);`, etc.).
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

- If the input or output volume is large, or faster IO is required, prefer `import sys` and read/write via `sys.stdin.buffer` / `sys.stdout.write`.
