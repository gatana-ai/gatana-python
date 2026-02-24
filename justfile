# Default recipe: show available commands
default:
    @just --list

# Install all dependencies (including dev)
install:
    uv sync --all-groups --all-packages

# Run linter checks
lint:
    uv run ruff check packages/gatana-langchain/ tests/
    uv run ruff format --check packages/gatana-langchain/ tests/

# Format code and fix lint issues
format:
    uv run ruff format packages/gatana-langchain/ tests/
    uv run ruff check --fix packages/gatana-langchain/ tests/

# Run type checker
typecheck:
    uv run mypy packages/gatana-langchain/

# Run tests
test:
    uv run pytest tests/

# Run tests with coverage report
test-cov:
    uv run pytest tests/ --cov --cov-report=term-missing

# Build both packages (sdist + wheel)
build:
    uv build --package gatana-client
    uv build --package gatana-langchain

# Publish both packages to PyPI
publish:
    uv publish dist/gatana_client*
    uv publish dist/gatana_langchain*

# Release: bump version, run checks, build, tag, and optionally publish
release bump publish="":
    #!/usr/bin/env bash
    set -euo pipefail
    echo "🔍 Running checks before release..."
    just lint
    just typecheck
    just test
    echo "✅ All checks passed. Bumping {{ bump }} version..."
    bumpsemver --no-commit --no-tag {{ bump }}
    NEW_VERSION=$(grep 'current_version = ' .bumpsemver.cfg | cut -d= -f2 | tr -d '[:space:]')
    echo "🏷️  Version bumped to $NEW_VERSION"
    just clean
    just build
    git commit -am "release: ${NEW_VERSION}"
    git tag "v${NEW_VERSION}" -m "release: v${NEW_VERSION}"
    echo "✅ Released v${NEW_VERSION}"
    if [[ "{{ publish }}" == "publish" ]]; then
      echo "📦 Publishing to PyPI..."
      just publish
    fi

# Regenerate the Python SDK from the OpenAPI spec
generate-sdk openapi_url="https://acme.s.gatana.ai/api/v1/openapi.json":
    #!/usr/bin/env bash
    set -euo pipefail
    curl -sf -o openapi.json "{{ openapi_url }}"
    openapi-python-client generate --path openapi.json --overwrite --output-path packages/gatana-client
    # Inject [project] table required by uv workspace (generator only emits [tool.poetry])
    PYPROJECT=packages/gatana-client/pyproject.toml
    if ! grep -q '^\[project\]' "$PYPROJECT"; then
      HEADER='[project]\nname = "gatana-client"\nversion = "0.1.0"\ndescription = "A client library for accessing Gatana"\nrequires-python = ">=3.10"\ndependencies = [\n    "httpx>=0.23.0,<0.29.0",\n    "attrs>=22.2.0",\n    "python-dateutil>=2.8.0",\n]\n'
      printf '%b\n' "$HEADER" | cat - "$PYPROJECT" > "$PYPROJECT.tmp" && mv "$PYPROJECT.tmp" "$PYPROJECT"
    fi
    echo "SDK regenerated in packages/gatana-client/"

# Remove build artifacts and caches
clean:
    rm -rf dist/ build/ *.egg-info
    rm -rf packages/gatana-client/dist/ packages/gatana-client/build/
    rm -rf packages/gatana-langchain/dist/ packages/gatana-langchain/build/
    rm -rf .mypy_cache .pytest_cache .ruff_cache htmlcov
    rm -f .coverage coverage.xml
    find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
