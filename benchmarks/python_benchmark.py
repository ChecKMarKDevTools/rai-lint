import time
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "packages" / "python-gitlint"))

from gitlint_rai.rules import RaiFooterExists



class MockCommit:
    class MockMessage:
        def __init__(self, text):
            self.full = text
            lines = text.split("\n")
            self.title = lines[0] if lines else ""
            self.body = lines[1:] if len(lines) > 1 else []

    def __init__(self, text):
        self.message = self.MockMessage(text)


def benchmark_validation(message, name, valid, iterations=10000):
    rule = RaiFooterExists()
    commit = MockCommit(message)

    # Determine expected validity using the actual rule logic to avoid hard-coded checks.
    initial_result = rule.validate(commit)
    assert isinstance(initial_result, list), f"Expected list, got {type(initial_result)}"

    start = time.perf_counter()
    for _ in range(iterations):
        result = rule.validate(commit)
        assert isinstance(result, list), f"Expected list, got {type(result)}"
        if valid:
            assert len(result) == 0, f"Expected no violations for valid footer, got {result}"
        else:
            assert len(result) > 0, f"Expected violations for invalid footer, got {result}"
    end = time.perf_counter()

    total_time = (end - start) * 1000
    avg_time = total_time / iterations

    print(f"{name}: {iterations} iterations in {total_time:.2f}ms")
    print(f"Average: {avg_time:.4f}ms per validation")
    print()


if __name__ == "__main__":
    print("RAI Footer Validation Benchmark\n")

    benchmark_validation(
        "feat: add feature\n\nGenerated-by: GitHub Copilot <copilot@github.com>",
        "AI-Generated validation",
        valid=True,
    )

    benchmark_validation(
        "fix: resolve bug\n\nAssisted-by: GitHub Copilot <copilot@github.com>",
        "AI-Assisted validation",
        valid=True,
    )

    benchmark_validation(
        "chore: update\n\nGenerated-by: Verdent AI <verdent@verdent.ai>",
        "Verdent AI validation",
        valid=True,
    )

    benchmark_validation(
        "feat: add feature\n\nNo RAI footer",
        "Invalid footer validation",
        valid=False,
    )
