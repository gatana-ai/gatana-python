# Contributing to gatana

Thank you for your interest in contributing! This guide will help you get started.

## Prerequisites

- **Python 3.10+**
- **[uv](https://docs.astral.sh/uv/)** – fast Python package manager
- **[just](https://just.systems/)** – command runner (recommended over `make`)

## Repository structure

This is a **uv workspace** monorepo with two packages under `packages/`:

```
packages/
├── gatana-client/      # Auto-generated API SDK (from OpenAPI spec)
│   └── gatana_client/
└── gatana-langchain/   # LangChain integration (hand-written)
    └── gatana_langchain/
tests/                  # Integration / end-to-end tests
```

- **`gatana-client`** is regenerated with `just generate-sdk` — don't edit it by hand.
- **`gatana-langchain`** is where most contributions go.

## Setup

1. **Fork & clone** the repository:

   ```bash
   git clone git@github.com:<your-username>/gatana-langchain-sandbox.git
   cd gatana-langchain-sandbox
   ```

2. **Install all dependencies** (including dev tools):

   ```bash
   just install
   ```

3. **Install pre-commit hooks**:

   ```bash
   uv run pre-commit install
   ```

Run `just` with no arguments to see all available commands.

## Development workflow

| Task | Command |
|------|---------|
| List all commands | `just` |
| Install deps | `just install` |
| Run tests | `just test` |
| Run tests with coverage | `just test-cov` |
| Lint | `just lint` |
| Format code | `just format` |
| Type check | `just typecheck` |
| Build both packages | `just build` |
| Regenerate SDK | `just generate-sdk` |
| Clean artifacts | `just clean` |

Or use `uv run` directly:

```bash
uv run pytest tests/
uv run ruff check packages/gatana-langchain/ tests/
uv run ruff format packages/gatana-langchain/ tests/
uv run mypy packages/gatana-langchain/
```

## Code style

- We use **[Ruff](https://docs.astral.sh/ruff/)** for linting and formatting
- We use **[mypy](https://mypy-lang.org/)** in strict mode for type checking
- All public functions and classes must have **type annotations** and **docstrings**
- Follow [PEP 8](https://peps.python.org/pep-0008/) naming conventions

## Pull request process

1. Create a feature branch from `main`:

   ```bash
   git checkout -b feature/my-feature
   ```

2. Make your changes with tests

3. Ensure all checks pass:

   ```bash
   just lint && just typecheck && just test
   ```

4. Commit using clear, descriptive messages

5. Push and open a pull request against `main`

6. Fill in the PR template — describe **what** changed and **why**

## Reporting issues

- Use the [bug report template](https://github.com/gatana-ai/gatana-langchain-sandbox/issues/new?template=bug_report.md) for bugs
- Use the [feature request template](https://github.com/gatana-ai/gatana-langchain-sandbox/issues/new?template=feature_request.md) for ideas
