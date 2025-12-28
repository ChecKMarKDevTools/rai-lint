import time
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "packages" / "python-gitlint"))

from gitlint_rai.rules import RaiFooterExists
from gitlint.tests.base import BaseTestCase


class MockCommit:
    class MockMessage:
        def __init__(self, text):
            self.full = text

    def __init__(self, text):
        self.message = self.MockMessage(text)


def benchmark_validation(message, name, iterations=10000):
    rule = RaiFooterExists()
    commit = MockCommit(message)

    start = time.perf_counter()
    for _ in range(iterations):
        rule.validate(commit)
    end = time.perf_counter()

    total_time = (end - start) * 1000
    avg_time = total_time / iterations

    print(f"{name}: {iterations} iterations in {total_time:.2f}ms")
    print(f"Average: {avg_time:.4f}ms per validation")
    print()


if __name__ == "__main__":
    print("RAI Footer Validation Benchmark\n")

    benchmark_validation(
        "feat: add feature\n\n🛡️ RAI: AI-Generated",
        "AI-Generated validation",
    )

    benchmark_validation(
        "fix: resolve bug\n\n🛡️ RAI: AI-Assisted",
        "AI-Assisted validation",
    )

    benchmark_validation(
        "chore: update\n\nGenerated-by: Verdent AI <verdent@verdent.ai>",
        "Verdent AI validation",
    )

    benchmark_validation(
        "feat: add feature\n\nNo RAI footer",
        "Invalid footer validation",
    )
