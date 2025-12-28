import sys

from gitlint.cli import cli


def main():
    if "--extra-path" not in sys.argv:
        sys.argv.insert(1, "--extra-path")
        sys.argv.insert(2, "gitlint_rai")
    sys.exit(cli())


if __name__ == "__main__":
    main()
