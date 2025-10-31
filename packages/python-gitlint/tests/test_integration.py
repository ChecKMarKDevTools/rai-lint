import subprocess
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root / "packages" / "python-gitlint"))


def test_commit(message: str) -> tuple[int, str]:
    try:
        result = subprocess.run(
            ["gitlint"],
            input=message,
            capture_output=True,
            text=True,
            cwd=str(project_root),
        )
        return result.returncode, result.stderr
    except Exception as e:
        return 1, str(e)


def test_valid_ai_generated():
    exit_code, output = test_commit("feat: add feature\n\n🛡️ RAI: AI-Generated")
    assert exit_code == 0, f"Expected success but got: {output}"


def test_valid_ai_assisted():
    exit_code, output = test_commit("fix: resolve bug\n\n🛡️ RAI: AI-Assisted")
    assert exit_code == 0, f"Expected success but got: {output}"


def test_valid_verdent_ai():
    exit_code, output = test_commit(
        "chore: update\n\nGenerated-by: Verdent AI <verdent@verdent.ai>"
    )
    assert exit_code == 0, f"Expected success but got: {output}"


def test_invalid_no_footer():
    exit_code, output = test_commit("feat: add feature\n\nNo footer")
    assert exit_code != 0, "Expected failure but got success"
    assert "RAI footer" in output


def test_invalid_malformed():
    exit_code, output = test_commit("feat: add feature\n\n🛡️ RAI: AI-Something")
    assert exit_code != 0, "Expected failure but got success"


def test_case_insensitive():
    exit_code, output = test_commit("feat: add feature\n\n🛡️ rai: ai-generated")
    assert exit_code == 0, f"Expected success but got: {output}"


def test_with_additional_footers():
    exit_code, output = test_commit(
        "feat: add feature\n\nDescription\n\nCloses #123\n\n🛡️ RAI: AI-Assisted"
    )
    assert exit_code == 0, f"Expected success but got: {output}"


if __name__ == "__main__":
    test_valid_ai_generated()
    test_valid_ai_assisted()
    test_valid_verdent_ai()
    test_invalid_no_footer()
    test_invalid_malformed()
    test_case_insensitive()
    test_with_additional_footers()
    print("All integration tests passed!")
