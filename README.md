# AI Luogu

Solve [Luogu](https://www.luogu.com.cn/) problems with an AI coding agent.

This repository pairs a small problem scraper with agent instructions, so an AI coding agent can read a Luogu problem statement and write a verified C++ solution.

## How It Works

```text
Problem ID  ->  luogu_spider.py  ->  <pid>.md  ->  AI coding agent  ->  <pid>.cpp
```

`luogu_spider.py` downloads the problem and stores it as Markdown. The agent then reads that file, writes a solution, compiles it, and checks it against the samples.

## Requirements

- Python 3 (`python3`, or `python` on Windows)
- `requests`
- A C++23 compiler (`g++`)
- An AI coding agent such as [OpenCode](https://opencode.ai/)

## Usage

```bash
git clone https://github.com/xxxand/ai_luogu.git
cd ai_luogu
python3 -m pip install requests
```

The commands below use `python3`; both `python3` and `python` work on Windows.

Fetch a problem by ID:

```bash
python3 luogu_spider.py P1024
```

This writes `P1024.md` containing the time and memory limits, description, input/output format, samples, hints, and attachment links. Without an ID the script defaults to `P1024`.

Fetch a training list by number:

```bash
python3 luogu_spider.py 100
```

This writes `100.txt` with the B- and P-prefixed problem IDs from [training list 100](https://www.luogu.com.cn/training/100#problems), one per line in ascending order.

Then ask your agent to solve it, for example:

```text
solve P1024
```

## Output

| File        | Contents                                        |
| ----------- | ----------------------------------------------- |
| `<pid>.md`  | Scraped problem statement                       |
| `<pid>.cpp` | C++ solution                                    |
| `<pid>.exe` | Compiled binary (Windows)                       |
| `<pid>`     | Compiled binary (Linux)                         |
| `<tid>.txt` | B/P problem IDs from training list `<tid>`      |

Generated problems and binaries are ignored by Git (see `.gitignore`).

## Building

Linux:

```bash
g++ -std=c++23 -O2 -Wall -fno-asm P1024.cpp -o P1024
```

Windows:

```powershell
g++ -std=c++23 -O2 -Wall -fno-asm P1024.cpp -o P1024.exe
```

Run the binary with `./P1024` on Linux or `.\P1024.exe` on Windows.

## Agent Instructions

[`AGENTS.md`](AGENTS.md) defines the workflow the agent follows: fetching problems with the scraper, using C++ by default, keeping source files comment-free and compact, and verifying solutions against the samples.

## Disclaimer

AI-generated solutions may contain wrong assumptions, bugs, or inefficient algorithms. Always review and test before submitting.

This project is not affiliated with or endorsed by Luogu. Please respect Luogu's terms of service and rate limits.

## License

[MIT](LICENSE) © 2026 jxxyyy
