.PHONY: test test-coverage format lint check

test:
	uv run --active pytest tests/

test-coverage:
	uv run --active pytest tests/ --cov=checkmark_rai_lint --cov-report=html --cov-report=term-missing

format:
	uv run --active black checkmark_rai_lint/ tests/
	uv run --active isort checkmark_rai_lint/ tests/

lint:
	uv run --active black --check checkmark_rai_lint/ tests/
	uv run --active isort --check-only checkmark_rai_lint/ tests/

check: lint test-coverage
