
from gitlint.git import GitContext

# Create a context with a commit message
context = GitContext("feat: foo\n\nAuthored-by: Me <me@example.com>")
commit = context.commits[0]

print("Dir of commit.message:", dir(commit.message))
if hasattr(commit.message, 'footers'):
    print("commit.message.footers:", commit.message.footers)
else:
    print("commit.message.footers does not exist")
