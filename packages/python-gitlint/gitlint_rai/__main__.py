import sys

from gitlint.cli import cli


def main():
    if "--extra-path" not in sys.argv:
        sys.argv.append("--extra-path")
        sys.argv.append("gitlint_rai")
    sys.exit(cli())


if __name__ == "__main__":
    main()
