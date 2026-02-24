# gatana-client

Python client for the [Gatana](https://gatana.ai) API, generated using https://github.com/openapi-generators/openapi-python-client. Sync + async, built on httpx. Requires Python 3.10+.

```bash
pip install gatana-client
```

## Authentication

Use your user API key or a personal access token as the `token`:

```python
from gatana_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://acme.gatana.ai", token="your-api-key-or-pat")
```

Verify the authenticated identity:

```python
from gatana_client.api.auth import get_auth_me

me = get_auth_me.sync(client=client)  # returns user, tenant, quota metadata
```

## Usage

Endpoints live under `gatana_client.api.<group>.<module>`. Each module exposes `sync()`, `sync_detailed()`, `asyncio()`, and `asyncio_detailed()`. The `_detailed` variants return a `Response[T]` with status, headers, and parsed body; the plain variants return `T | None`.

```python
from gatana_client.api.sandboxes import post_sandboxes, post_sandboxes_sandbox_id_exec, delete_sandboxes_sandbox_id
from gatana_client.models.exec_command_body import ExecCommandBody

sandbox_id = post_sandboxes.sync_detailed(client=client).parsed.sandbox.id
result = post_sandboxes_sandbox_id_exec.sync_detailed(sandbox_id, client=client, body=ExecCommandBody(command="echo hi"))
delete_sandboxes_sandbox_id.sync(sandbox_id, client=client)

# async: await post_sandboxes.asyncio(client=client)
```

File I/O uses `gatana_client.types.File`:

```python
from gatana_client.api.sandboxes import post_sandboxes_sandbox_id_write_file, post_sandboxes_sandbox_id_read_file
from gatana_client.types import File
import io

post_sandboxes_sandbox_id_write_file.sync(sandbox_id, client=client, body=File(payload=io.BytesIO(b"hello")), path="/tmp/f.txt")
content = post_sandboxes_sandbox_id_read_file.sync_detailed(sandbox_id, client=client, path="/tmp/f.txt").content
```

## Client options

| Parameter                    | Default | Description                                |
| ---------------------------- | ------- | ------------------------------------------ |
| `base_url`                   | —       | API base URL                               |
| `token`                      | —       | API key or PAT (`AuthenticatedClient` only)|
| `timeout`                    | `None`  | `httpx.Timeout`                            |
| `verify_ssl`                 | `True`  | SSL verification                           |
| `raise_on_unexpected_status` | `False` | Raise `UnexpectedStatus` on undocumented HTTP codes instead of returning `None` |
| `headers` / `cookies`        | `{}`    | Extra headers/cookies per request          |
| `httpx_args`                 | `{}`    | Kwargs forwarded to `httpx.Client`         |

Clients support context managers and builder methods (`with_headers`, `with_cookies`, `with_timeout`).

## API groups

`sandboxes` · `mcp_servers` · `teams` · `users` · `profiles` · `auth` · `tenants` · `secret_stores` · `tools` · `audit_logs` · `email_verification`
