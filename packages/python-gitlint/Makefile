.PHONY: test test-coverage format lint check

test:
	uv run pytest tests/

test-coverage:
	uv run pytest tests/ --cov=checkmark_rai_lint --cov-report=html --cov-report=term-missing

format:
	uv run black checkmark_rai_lint/ tests/
	uv run isort checkmark_rai_lint/ tests/

lint:
	uv run black --check checkmark_rai_lint/ tests/
	uv run isort --check-only checkmark_rai_lint/ tests/

check: lint test-coverage
