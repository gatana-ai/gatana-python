.DEFAULT_GOAL := help

.PHONY: help install lint format typecheck test test-cov build publish clean generate-sdk

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install all dependencies (including dev)
	uv sync --all-groups --all-packages

lint:  ## Run linter checks
	uv run ruff check packages/gatana-langchain/ tests/
	uv run ruff format --check packages/gatana-langchain/ tests/

format:  ## Format code and fix lint issues
	uv run ruff format packages/gatana-langchain/ tests/
	uv run ruff check --fix packages/gatana-langchain/ tests/

typecheck:  ## Run type checker
	uv run mypy packages/gatana-langchain/

test:  ## Run tests
	uv run pytest tests/

test-cov:  ## Run tests with coverage report
	uv run pytest tests/ --cov --cov-report=term-missing

build:  ## Build both packages (sdist + wheel)
	uv build --package gatana-client
	uv build --package gatana-langchain

publish:  ## Publish both packages to PyPI
	uv publish dist/gatana_client*
	uv publish dist/gatana_langchain*

OPENAPI_URL ?= https://acme.s.gatana.ai/api/v1/openapi.json

generate-sdk:  ## Regenerate the Python SDK from the OpenAPI spec
	curl -sf -o openapi.json "$(OPENAPI_URL)"
	openapi-python-client generate --path openapi.json --overwrite --output-path packages/gatana-client
	@if ! grep -q '^\[project\]' packages/gatana-client/pyproject.toml; then \
		printf '[project]\nname = "gatana-client"\nversion = "0.1.0"\ndescription = "A client library for accessing Gatana"\nrequires-python = ">=3.10"\ndependencies = [\n    "httpx>=0.23.0,<0.29.0",\n    "attrs>=22.2.0",\n    "python-dateutil>=2.8.0",\n]\n\n' \
		| cat - packages/gatana-client/pyproject.toml > packages/gatana-client/pyproject.toml.tmp \
		&& mv packages/gatana-client/pyproject.toml.tmp packages/gatana-client/pyproject.toml; \
	fi
	@echo "SDK regenerated in packages/gatana-client/"

clean:  ## Remove build artifacts and caches
	rm -rf dist/ build/ *.egg-info
	rm -rf packages/gatana-client/dist/ packages/gatana-client/build/
	rm -rf packages/gatana-langchain/dist/ packages/gatana-langchain/build/
	rm -rf .mypy_cache .pytest_cache .ruff_cache htmlcov
	rm -f .coverage coverage.xml
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
