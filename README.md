# gatana-python

[![PyPI gatana-langchain](https://img.shields.io/pypi/v/gatana-langchain?label=gatana-langchain)](https://pypi.org/project/gatana-langchain/)
[![PyPI gatana-client](https://img.shields.io/pypi/v/gatana-client?label=gatana-client)](https://pypi.org/project/gatana-client/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A toolkit for building LangChain applications with [Gatana](https://gatana.ai).

## Packages

This is a monorepo containing multiple PyPI packages:

| Package | Description | PyPI |
|---------|-------------|------|
| [`gatana-langchain`](packages/gatana-langchain/) | LangChain integration toolkit | [![PyPI](https://img.shields.io/pypi/v/gatana-langchain)](https://pypi.org/project/gatana-langchain/) |
| [`gatana-client`](packages/gatana-client/) | Auto-generated API client for Gatana | [![PyPI](https://img.shields.io/pypi/v/gatana-client)](https://pypi.org/project/gatana-client/) |

## Installation

```bash
pip install gatana-langchain
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add gatana-langchain
```

This will also install `gatana-client` as a dependency.

## Quick Start

```python
import gatana_langchain

print(gatana_langchain.__version__)
```

## Repository structure

```
packages/
├── gatana-client/      # Auto-generated API SDK (from OpenAPI spec)
│   └── gatana_client/
└── gatana-langchain/   # LangChain integration (hand-written)
    └── gatana_langchain/
tests/                  # Integration tests
```

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to set up the development environment, run tests, and submit changes.

## License

[MIT](LICENSE) — Copyright (c) 2026 Gatana
