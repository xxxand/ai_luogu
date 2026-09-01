# AI Luogu

**Using AI to solve [Luogu](https://www.luogu.com.cn/) problems.**

AI Luogu is a lightweight tool designed to assist with solving programming problems from Luogu. It provides a simple workflow for retrieving problem information and generating solutions with the help of AI.

## Features

* Fetch Luogu problem information automatically.
* Use AI to assist with problem solving.
* Generate C++ solutions based on a predefined template.
* Simple and lightweight Python-based workflow.
* Easy to customize for different AI models or solution-generation strategies.

## Project Structure

```text
.
├── luogu_spider.py   # Fetches problem information from Luogu
├── template.cpp      # C++ solution template
├── AGENTS.md         # Project instructions
└── LICENSE           # MIT License
```

## Requirements

* Python 3.x
* A working internet connection
* An AI model/API capable of generating programming solutions

## Usage

Clone the repository:

```bash
git clone https://github.com/xxxand/ai_luogu.git
cd ai_luogu
```

Run the main script:

```bash
python luogu_spider.py
```

Depending on your configuration, you may need to provide the problem URL, problem ID, or AI service credentials.

## Workflow

The general workflow is:

```text
Luogu Problem
      │
      ▼
 Problem Spider
      │
      ▼
Problem Information
      │
      ▼
      AI Model
      │
      ▼
Generated Solution
      │
      ▼
   C++ Code
```

The project separates problem retrieval from solution generation, making it easier to replace or extend individual components.

## Example

Given a Luogu problem, the tool can retrieve the relevant problem information and use an AI model to help produce a C++ solution.

The generated code can then be reviewed, compiled, tested, and submitted manually.

> **Note:** AI-generated solutions may contain incorrect assumptions, implementation bugs, or inefficient algorithms. Always verify the solution before submission.

## Customization

You can modify `template.cpp` to define your preferred C++ solution template, coding style, or commonly used utilities.

The spider implementation in `luogu_spider.py` can also be extended to support additional problem information or different input methods.

## Disclaimer

This project is intended for learning, experimentation, and programming assistance.

It is **not affiliated with or endorsed by Luogu**.

Please respect Luogu's terms of service and applicable rate limits when accessing its website. Do not use this project to abuse or overload Luogu's services.

## Contributing

Contributions are welcome.

If you have an idea for an improvement:

1. Fork this repository.
2. Create a new branch.
3. Make your changes.
4. Open a Pull Request.

Bug reports and feature requests can also be submitted through GitHub Issues.

## License

This project is licensed under the [MIT License](LICENSE).

Copyright © 2026 jxxyyy.
