.PHONY: help install clean test lint format build validate
.PHONY: test-node test-python lint-node lint-python format-node format-python build-node build-python

help:
	@printf "CheckMarK RAI Lint - Makefile Commands\n"
	@printf "\n"
	@printf "Main targets:\n"
	@printf "  make validate       - Run all checks (lint, format-check, test, build)\n"
	@printf "  make test           - Run all tests (Node + Python)\n"
	@printf "  make lint           - Run all linters (Node + Python)\n"
	@printf "  make format         - Format all code (Node + Python)\n"
	@printf "  make build          - Build all packages\n"
	@printf "  make install        - Install all dependencies\n"
	@printf "  make clean          - Clean build artifacts\n"
	@printf "\n"
	@printf "Node-specific targets:\n"
	@printf "  make test-node      - Run Node tests\n"
	@printf "  make lint-node      - Run Node linter\n"
	@printf "  make format-node    - Format Node code\n"
	@printf "  make build-node     - Build Node package\n"
	@printf "\n"
	@printf "Python-specific targets:\n"
	@printf "  make test-python    - Run Python tests\n"
	@printf "  make lint-python    - Run Python linter (black check + isort check)\n"
	@printf "  make format-python  - Format Python code (black + isort)\n"
	@printf "  make build-python   - Build Python package\n"

install:
	npm install
	cd packages/python-gitlint && uv sync --locked --group dev

clean:
	rm -rf .venv
	rm -rf node_modules
	rm -rf packages/node-commitlint/dist
	rm -rf packages/node-commitlint/node_modules
	rm -rf packages/python-gitlint/build
	rm -rf packages/python-gitlint/dist
	rm -rf packages/python-gitlint/*.egg-info
	rm -rf packages/python-gitlint/htmlcov
	rm -rf packages/python-gitlint/.venv
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true

test-node:
	cd packages/node-commitlint && npm test

test-python:
	cd packages/python-gitlint && uv run pytest tests/

test: test-node test-python

lint-node:
	cd packages/node-commitlint && npm run lint

lint-python:
	cd packages/python-gitlint && uv run black --check checkmark_rai_lint/ tests/
	cd packages/python-gitlint && uv run isort --check-only checkmark_rai_lint/ tests/

lint: lint-node lint-python

format-node:
	npm run format

format-python:
	cd packages/python-gitlint && uv run black checkmark_rai_lint/ tests/
	cd packages/python-gitlint && uv run isort checkmark_rai_lint/ tests/

format: format-node format-python

build-node:
	cd packages/node-commitlint && npm run build

build-python:
	cd packages/python-gitlint && uv run python -m build

build: build-node build-python

validate: format lint test build
