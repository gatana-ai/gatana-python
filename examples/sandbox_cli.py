#!/usr/bin/env python3
"""Interactive CLI to test GatanaSandbox."""

from __future__ import annotations

import argparse
import logging

from gatana_client import AuthenticatedClient
from gatana_langchain import GatanaSandbox


def main() -> None:
    parser = argparse.ArgumentParser(description="Test Gatana Sandbox")
    parser.add_argument(
        "--base-url", default="https://acme.s.gatana.ai", help="Gatana API base URL"
    )
    parser.add_argument(
        "--token", required=True, help="API token (or personal access token)"
    )
    parser.add_argument(
        "--sandbox-id",
        default=None,
        help="Existing sandbox ID (creates new if omitted)",
    )
    parser.add_argument(
        "--no-verify",
        action="store_true",
        help="Disable SSL certificate verification (for local dev)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Log every HTTP request and response",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(
            level=logging.DEBUG, format="%(levelname)s %(name)s: %(message)s"
        )
        # httpcore is too noisy and doesn't show URLs; suppress it
        logging.getLogger("httpcore").setLevel(logging.DEBUG)
        logging.getLogger("httpx").setLevel(logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    import httpx as _httpx

    def _log_request(request: _httpx.Request) -> None:
        logger = logging.getLogger("sandbox_cli")
        logger.debug("→ %s %s", request.method, request.url)
        if request.content:
            body = request.content[:500].decode(errors="replace")
            logger.debug("  body: %s", body)

    def _log_response(response: _httpx.Response) -> None:
        response.read()
        logger = logging.getLogger("sandbox_cli")
        logger.debug(
            "← %s %s (%d bytes)",
            response.status_code,
            response.url,
            len(response.content),
        )

    client = AuthenticatedClient(
        base_url=args.base_url,
        token=args.token,
        verify_ssl=not args.no_verify,
        httpx_args={
            "event_hooks": {"request": [_log_request], "response": [_log_response]}
        }
        if args.verbose
        else {},
    )

    print("Connecting to Gatana...", flush=True)
    sandbox = GatanaSandbox(client=client, sandbox_id=args.sandbox_id)
    owns = "created new" if sandbox._owns_sandbox else "wrapped existing"
    print(f"Sandbox ready: {sandbox.id} ({owns})\n")

    print("Commands:")
    print("  !exec <cmd>       — execute a shell command")
    print("  !upload <path>    — upload a local file to sandbox at same path")
    print("  !download <path>  — download a file from sandbox and print it")
    print("  !read <path>      — read file via BaseSandbox.read()")
    print("  !write <path>     — write stdin content to file via BaseSandbox.write()")
    print("  !ls <path>        — list directory via BaseSandbox.ls_info()")
    print("  !status           — print sandbox id")
    print("  !quit             — exit (deletes sandbox if we created it)")
    print()

    try:
        while True:
            try:
                line = input("sandbox> ").strip()
            except EOFError:
                break

            if not line:
                continue

            try:
                if line == "!quit":
                    break
                elif line == "!status":
                    print(f"Sandbox ID: {sandbox.id}")
                elif line.startswith("!exec "):
                    cmd = line[6:]
                    result = sandbox.execute(cmd)
                    if result.output:
                        print(
                            result.output,
                            end="" if result.output.endswith("\n") else "\n",
                        )
                    print(f"[exit code: {result.exit_code}]")
                elif line.startswith("!download "):
                    path = line[10:].strip()
                    results = sandbox.download_files([path])
                    r = results[0]
                    if r.error:
                        print(f"Error: {r.error}")
                    elif r.content:
                        try:
                            print(r.content.decode())
                        except UnicodeDecodeError:
                            print(f"<binary, {len(r.content)} bytes>")
                elif line.startswith("!upload "):
                    local_path = line[8:].strip()
                    try:
                        with open(local_path, "rb") as f:
                            content = f.read()
                        results = sandbox.upload_files([(local_path, content)])
                        r = results[0]
                        if r.error:
                            print(f"Upload error: {r.error}")
                        else:
                            print(f"Uploaded {local_path} ({len(content)} bytes)")
                    except FileNotFoundError:
                        print(f"Local file not found: {local_path}")
                elif line.startswith("!read "):
                    path = line[6:].strip()
                    output = sandbox.read(path)
                    print(output)
                elif line.startswith("!write "):
                    path = line[7:].strip()
                    print("Enter content (Ctrl-D to finish):")
                    content_lines = []
                    try:
                        while True:
                            content_lines.append(input())
                    except EOFError:
                        pass
                    content = "\n".join(content_lines)
                    result = sandbox.write(path, content)
                    if result.error:
                        print(f"Write error: {result.error}")
                    else:
                        print(f"Written to {result.path}")
                elif line.startswith("!ls "):
                    path = line[4:].strip()
                    entries = sandbox.ls_info(path)
                    for e in entries:
                        kind = "d" if e.get("is_dir") else "f"
                        print(f"  [{kind}] {e['path']}")
                    if not entries:
                        print("  (empty)")
                else:
                    # Default: treat as shell command
                    result = sandbox.execute(line)
                    if result.output:
                        print(
                            result.output,
                            end="" if result.output.endswith("\n") else "\n",
                        )
                    print(f"[exit code: {result.exit_code}]")
            except Exception as e:
                print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nInterrupted.")
    finally:
        sandbox.close()
        print(
            f"Sandbox {sandbox.id} {'deleted' if sandbox._owns_sandbox else 'left intact'}."
        )


if __name__ == "__main__":
    main()
