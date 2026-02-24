# Default recipe: show available commands
default:
    @just --list

# Set up the full development environment
init: install
    .venv/bin/pre-commit install

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

# Build a specific package (sdist + wheel)
build pkg:
    uv build --package {{ pkg }}

# Build all packages
build-all:
    just build gatana-client
    just build gatana-langchain

# Publish a specific package to PyPI (builds first if needed)
publish pkg: (build pkg)
    #!/usr/bin/env bash
    set -euo pipefail
    PKG_UNDER=$(echo "{{ pkg }}" | tr '-' '_')
    UV_PUBLISH_TOKEN=$(uv auth token pypi) uv publish __token__ dist/${PKG_UNDER}*

# Publish all packages to PyPI
publish-all:
    just publish gatana-client
    just publish gatana-langchain

# Release a specific package: bump version, run checks, build, tag, and optionally publish
release pkg bump publish="":
    #!/usr/bin/env bash
    set -euo pipefail
    PKG_DIR="packages/{{ pkg }}"
    echo "🔍 Running checks before release..."
    just lint
    just typecheck
    just test
    echo "✅ All checks passed. Bumping {{ bump }} version for {{ pkg }}..."
    pushd "$PKG_DIR" > /dev/null
    bumpsemver --no-commit --no-tag {{ bump }}
    NEW_VERSION=$(grep 'current_version = ' .bumpsemver.cfg | cut -d= -f2 | tr -d '[:space:]')
    popd > /dev/null
    echo "🏷️  {{ pkg }} version bumped to $NEW_VERSION"
    just clean
    just build {{ pkg }}
    git commit -am "release({{ pkg }}): v${NEW_VERSION}"
    git tag "{{ pkg }}/v${NEW_VERSION}" -m "release: {{ pkg }} v${NEW_VERSION}"
    echo "✅ Released {{ pkg }} v${NEW_VERSION}"
    if [[ "{{ publish }}" == "publish" ]]; then
      echo "📦 Publishing {{ pkg }} to PyPI..."
      just publish {{ pkg }}
    fi

# Release all packages with the same bump level
release-all bump publish="":
    just release gatana-client {{ bump }} {{ publish }}
    just release gatana-langchain {{ bump }} {{ publish }}

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
