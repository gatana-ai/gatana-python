# gatana-python

[![PyPI](https://img.shields.io/pypi/v/gatana)](https://pypi.org/project/gatana/)
[![Python](https://img.shields.io/pypi/pyversions/gatana)](https://pypi.org/project/gatana/)
[![CI](https://github.com/gatana-ai/gatana-langchain-sandbox/actions/workflows/ci.yml/badge.svg)](https://github.com/gatana-ai/gatana-langchain-sandbox/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A toolkit for building LangChain applications.

## Features

- Built on top of [LangChain](https://python.langchain.com/)
- Fully typed with [PEP 561](https://peps.python.org/pep-0561/) support
- Python 3.10+

## Installation

```bash
pip install gatana
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add gatana
```

### Optional dependencies

```bash
# OpenAI support
pip install gatana[openai]

# Anthropic support
pip install gatana[anthropic]
```

## Quick Start

```python
import gatana

print(gatana.__version__)
```

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to set up the development environment, run tests, and submit changes.

## License

[MIT](LICENSE) — Copyright (c) 2026 Gatana
