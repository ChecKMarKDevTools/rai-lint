from gitlint.git import GitCommit
from gitlint.config import LintConfig

# Create a dummy commit
message = "feat: test\n\nAuthored-by: Me <me@example.com>"
commit = GitCommit(context=None, message=message, sha=None)

print("Dir of commit.message:", dir(commit.message))
# Check if footers exists
if hasattr(commit.message, "footers"):
    print("commit.message.footers:", commit.message.footers)
else:
    print("commit.message.footers does not exist")

# Check if trailers exists (git terminology)
if hasattr(commit.message, "trailers"):
    print("commit.message.trailers:", commit.message.trailers)
