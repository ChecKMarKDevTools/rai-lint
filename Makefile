.PHONY: help install clean test lint format build validate
.PHONY: test-node test-python lint-node lint-python format-node format-python build-node

help:
	@echo "CheckMarK RAI Lint - Makefile Commands"
	@echo ""
	@echo "Main targets:"
	@echo "  make validate       - Run all checks (lint, format-check, test, build)"
	@echo "  make test           - Run all tests (Node + Python)"
	@echo "  make lint           - Run all linters (Node + Python)"
	@echo "  make format         - Format all code (Node + Python)"
	@echo "  make build          - Build all packages"
	@echo "  make install        - Install all dependencies"
	@echo "  make clean          - Clean build artifacts"
	@echo ""
	@echo "Node-specific targets:"
	@echo "  make test-node      - Run Node tests"
	@echo "  make lint-node      - Run Node linter"
	@echo "  make format-node    - Format Node code"
	@echo "  make build-node     - Build Node package"
	@echo ""
	@echo "Python-specific targets:"
	@echo "  make test-python    - Run Python tests"
	@echo "  make lint-python    - Run Python linter (black check + isort check)"
	@echo "  make format-python  - Format Python code (black + isort)"

install:
	@echo "Installing Node dependencies..."
	npm install
	@echo "Installing Python dependencies..."
	pip install -e "packages/python-gitlint[dev]"

clean:
	@echo "Cleaning build artifacts..."
	rm -rf node_modules
	rm -rf packages/node-commitlint/dist
	rm -rf packages/node-commitlint/node_modules
	rm -rf packages/python-gitlint/build
	rm -rf packages/python-gitlint/dist
	rm -rf packages/python-gitlint/*.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	@echo "Clean complete!"

test-node:
	@echo "Running Node tests..."
	cd packages/node-commitlint && npm test

test-python:
	@echo "Running Python tests..."
	cd packages/python-gitlint && pytest tests/

test: test-node test-python
	@echo ""
	@echo "✅ All tests passed!"

lint-node:
	@echo "Running Node linter..."
	cd packages/node-commitlint && npm run lint

lint-python:
	@echo "Checking Python code with black..."
	cd packages/python-gitlint && black --check .
	@echo "Checking Python imports with isort..."
	cd packages/python-gitlint && isort --check-only .

lint: lint-node lint-python
	@echo ""
	@echo "✅ All linting passed!"

format-node:
	@echo "Formatting Node code..."
	npm run format

format-python:
	@echo "Formatting Python code with black..."
	cd packages/python-gitlint && black .
	@echo "Sorting Python imports with isort..."
	cd packages/python-gitlint && isort .

format: format-node format-python
	@echo ""
	@echo "✅ All code formatted!"

build-node:
	@echo "Building Node package..."
	cd packages/node-commitlint && npm run build

build: build-node
	@echo ""
	@echo "✅ Build complete!"

validate: lint test build
	@echo ""
	@echo "=========================================="
	@echo "✅ VALIDATION COMPLETE - ALL CHECKS PASSED"
	@echo "=========================================="
