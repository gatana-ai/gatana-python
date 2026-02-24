# Contributing to gatana

Thank you for your interest in contributing! This guide will help you get started.

## Prerequisites

- **Python 3.10+**
- **[uv](https://docs.astral.sh/uv/)** – fast Python package manager

## Setup

1. **Fork & clone** the repository:

   ```bash
   git clone git@github.com:<your-username>/gatana-langchain-sandbox.git
   cd gatana-langchain-sandbox
   ```

2. **Install all dependencies** (including dev tools):

   ```bash
   uv sync --all-groups
   ```

3. **Install pre-commit hooks**:

   ```bash
   uv run pre-commit install
   ```

## Development workflow

| Task | Command |
|------|---------|
| Run tests | `make test` |
| Run tests with coverage | `make test-cov` |
| Lint | `make lint` |
| Format code | `make format` |
| Type check | `make typecheck` |
| Build package | `make build` |

Or use `uv run` directly:

```bash
uv run pytest tests/
uv run ruff check src/ tests/
uv run ruff format src/ tests/
uv run mypy src/
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
   make lint typecheck test
   ```

4. Commit using clear, descriptive messages

5. Push and open a pull request against `main`

6. Fill in the PR template — describe **what** changed and **why**

## Reporting issues

- Use the [bug report template](https://github.com/gatana-ai/gatana-langchain-sandbox/issues/new?template=bug_report.md) for bugs
- Use the [feature request template](https://github.com/gatana-ai/gatana-langchain-sandbox/issues/new?template=feature_request.md) for ideas
