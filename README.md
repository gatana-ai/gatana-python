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

## Packages

This is a monorepo containing multiple PyPI packages:

| Package | Description | PyPI |
|---------|-------------|------|
| [`gatana-langchain`](packages/gatana-langchain/) | LangChain Sandbox integration toolkit | [![PyPI](https://img.shields.io/pypi/v/gatana-langchain)](https://pypi.org/project/gatana-langchain/) |
| [`gatana-client`](packages/gatana-client/) | SDK client for Gatana | [![PyPI](https://img.shields.io/pypi/v/gatana-client)](https://pypi.org/project/gatana-client/) |

## Installation

```bash
pip install gatana-langchain
# or, if you only want the SDK:
pip install gatana-client
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add gatana-langchain
# or, if you only want the SDK:
uv add gatana-client
```

## Quick Start

```python
from gatana_client import GatanaClient
from gatana_langchain import GatanaSandbox

# Env variables: GATANA_API_KEY and GATANA_ORG_ID
# Or, ~/.gatana.config

client = GatanaClient()
```

For configuration, you can prepare a file at `~/.gatana.config`, see [Config File](#config-file) for details. You can override configuration using environment variables or by passing options directly in the SDK.

## Configuration

`gatana-client` resolves authentication in the following order:

1. **Passed options** — `token` + (`org_id` or `base_url`)
2. **Environment variables** — `GATANA_API_KEY` + (`GATANA_ORG_ID` or `GATANA_BASE_URL`)
3. **Config file** `~/.gatana.config` — API key or access token per organization

### Environment Variables

| Variable | Description |
|----------|-------------|
| `GATANA_API_KEY` | API key for authentication |
| `GATANA_ORG_ID` | Organization ID (derives `https://<org-id>.gatana.ai/api/v1`) |
| `GATANA_BASE_URL` | Override the base URL directly |

### Config File

The config file at `~/.gatana.config` supports multiple organizations:

```json
{
  "orgs": {
    "my-org": {
      "baseUrl": "https://my-org.gatana.ai",
      "apiKey": "sk-...",
      "tokens": {
        "access_token": "...",
        "refresh_token": "...",
        "expires_at": 1234567890
      }
    }
  },
  "defaultOrgId": "my-org"
}
```

Authentication methods per organization:

- **API key** — set directly in the config file or via the Gatana CLI (`gatana config set-api-key`)
- **OIDC tokens** — set via the Gatana CLI (`gatana config login`), tokens are read as-is

> **Note:** The config file format is shared with the [Gatana CLI tools](https://github.com/gatana-ai/gatana-js). You can use the CLI to manage your `~/.gatana.config` and the Python SDK will pick it up automatically.

## SDK

### Custom Authentication

Provide a `ConfigLoader` or explicit options:

```python
from gatana_client import GatanaClient, ConfigLoader, OptionsConfigStrategy

# Using explicit options
client = GatanaClient(token="sk-...", org_id="my-org")

# Using a custom config loader
client = GatanaClient(
    config_loader=ConfigLoader([
        OptionsConfigStrategy(api_key="sk-...", org_id="my-org")
    ])
)
```

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to set up the development environment, run tests, and submit changes.

## License

[MIT](LICENSE) — Copyright (c) 2026 Gatana
