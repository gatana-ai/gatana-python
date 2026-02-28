<div align="center">
  <img alt="Gatana Logo" height="86" src="https://gatana.gatana.ai/favicon-prod.png" width="86">
  <h1 align="center"><b>Gatana Python</b></h1>
  <p align="center">🚀 Python SDK & LangChain Sandbox Backend</p>
</div>
<br/>

<p align="center">
  <a href="https://pypi.org/project/gatana-langchain/" rel="nofollow"><img src="https://img.shields.io/pypi/v/gatana-langchain?label=gatana-langchain" /></a>
  <a href="https://pypi.org/project/gatana-client/" rel="nofollow"><img src="https://img.shields.io/pypi/v/gatana-client?label=gatana-client" /></a>
  <a href="https://opensource.org/licenses/MIT" rel="nofollow"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" /></a>
</p>

<p align="center">
  <a href="https://gatana.ai">Homepage</a>
  <span>&nbsp;•&nbsp;</span>
  <a href="https://docs.gatana.ai/">Documentation</a>
  <span>&nbsp;•&nbsp;</span>
  <a href="https://discord.gg/6TvjvmSP">Discord</a>
  <span>&nbsp;•&nbsp;</span>
  <a href="https://github.com/gatana-ai/gatana-python">JavaScript SDK & CLI tools</a>
</p>


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
