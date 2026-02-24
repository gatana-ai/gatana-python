.DEFAULT_GOAL := help

.PHONY: help install lint format typecheck test test-cov build publish clean

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install all dependencies (including dev)
	uv sync --all-groups

lint:  ## Run linter checks
	uv run ruff check src/ tests/
	uv run ruff format --check src/ tests/

format:  ## Format code and fix lint issues
	uv run ruff format src/ tests/
	uv run ruff check --fix src/ tests/

typecheck:  ## Run type checker
	uv run mypy src/

test:  ## Run tests
	uv run pytest tests/

test-cov:  ## Run tests with coverage report
	uv run pytest tests/ --cov --cov-report=term-missing

build:  ## Build package (sdist + wheel)
	uv build

publish:  ## Publish to PyPI (use after 'make build')
	uv publish

clean:  ## Remove build artifacts and caches
	rm -rf dist/ build/ *.egg-info src/*.egg-info
	rm -rf .mypy_cache .pytest_cache .ruff_cache htmlcov
	rm -f .coverage coverage.xml
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
