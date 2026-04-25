---
title: Github Code Review | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/github/github-github-code-review
source: crawler
fetched_at: 2026-04-24T17:05:32.428746018-03:00
rendered_js: false
word_count: 861
summary: This document provides a comprehensive reference on how the Hermes Agent performs code reviews, detailing processes for analyzing local Git changes before pushing and reviewing open Pull Requests on GitHub using either the gh CLI or direct REST API calls.
tags:
    - github-code-review
    - git-diff
    - pull-request-workflow
    - local-review
    - api-interaction
category: reference
---

Review code changes by analyzing git diffs, leaving inline comments on PRs, and performing thorough pre-push review. Works with gh CLI or falls back to git + GitHub REST API via curl.

SourceBundled (installed by default)Path`skills/github/github-code-review`Version`1.1.0`AuthorHermes AgentLicenseMITTags`GitHub`, `Code-Review`, `Pull-Requests`, `Git`, `Quality`Related skills[`github-auth`](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/github/github-github-auth), [`github-pr-workflow`](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/github/github-github-pr-workflow)

## Reference: full SKILL.md[​](#reference-full-skillmd "Direct link to Reference: full SKILL.md")

info

The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.

## GitHub Code Review

Perform code reviews on local changes before pushing, or review open PRs on GitHub. Most of this skill uses plain `git` — the `gh`/`curl` split only matters for PR-level interactions.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

- Authenticated with GitHub (see `github-auth` skill)
- Inside a git repository

### Setup (for PR interactions)[​](#setup-for-pr-interactions "Direct link to Setup (for PR interactions)")

```bash
ifcommand-v gh &>/dev/null && gh auth status &>/dev/null;then
AUTH="gh"
else
AUTH="git"
if[-z"$GITHUB_TOKEN"];then
if[-f ~/.hermes/.env ]&&grep-q"^GITHUB_TOKEN=" ~/.hermes/.env;then
GITHUB_TOKEN=$(grep"^GITHUB_TOKEN=" ~/.hermes/.env |head-1|cut-d=-f2|tr-d'\n\r')
elifgrep-q"github.com" ~/.git-credentials 2>/dev/null;then
GITHUB_TOKEN=$(grep"github.com" ~/.git-credentials 2>/dev/null |head-1|sed's|https://[^:]*:\([^@]*\)@.*|\1|')
fi
fi
fi

REMOTE_URL=$(git remote get-url origin)
OWNER_REPO=$(echo"$REMOTE_URL"|sed-E's|.*github\.com[:/]||; s|\.git$||')
OWNER=$(echo"$OWNER_REPO"|cut -d/ -f1)
REPO=$(echo"$OWNER_REPO"|cut -d/ -f2)
```

* * *

## 1. Reviewing Local Changes (Pre-Push)[​](#1-reviewing-local-changes-pre-push "Direct link to 1. Reviewing Local Changes (Pre-Push)")

This is pure `git` — works everywhere, no API needed.

### Get the Diff[​](#get-the-diff "Direct link to Get the Diff")

```bash
# Staged changes (what would be committed)
gitdiff--staged

# All changes vs main (what a PR would contain)
gitdiff main...HEAD

# File names only
gitdiff main...HEAD --name-only

# Stat summary (insertions/deletions per file)
gitdiff main...HEAD --stat
```

### Review Strategy[​](#review-strategy "Direct link to Review Strategy")

1. **Get the big picture first:**

```bash
gitdiff main...HEAD --stat
git log main..HEAD --oneline
```

2. **Review file by file** — use `read_file` on changed files for full context, and the diff to see what changed:

```bash
gitdiff main...HEAD -- src/auth/login.py
```

3. **Check for common issues:**

```bash
# Debug statements, TODOs, console.logs left behind
gitdiff main...HEAD |grep-n"print(\|console\.log\|TODO\|FIXME\|HACK\|XXX\|debugger"

# Large files accidentally staged
gitdiff main...HEAD --stat|sort -t'|'-k2-rn|head-10

# Secrets or credential patterns
gitdiff main...HEAD |grep-in"password\|secret\|api_key\|token.*=\|private_key"

# Merge conflict markers
gitdiff main...HEAD |grep-n"<<<<<<\|>>>>>>\|======="
```

4. **Present structured feedback** to the user.

### Review Output Format[​](#review-output-format "Direct link to Review Output Format")

When reviewing local changes, present findings in this structure:

```text
## Code Review Summary

### Critical
- **src/auth.py:45** — SQL injection: user input passed directly to query.
  Suggestion: Use parameterized queries.

### Warnings
- **src/models/user.py:23** — Password stored in plaintext. Use bcrypt or argon2.
- **src/api/routes.py:112** — No rate limiting on login endpoint.

### Suggestions
- **src/utils/helpers.py:8** — Duplicates logic in `src/core/utils.py:34`. Consolidate.
- **tests/test_auth.py** — Missing edge case: expired token test.

### Looks Good
- Clean separation of concerns in the middleware layer
- Good test coverage for the happy path
```

* * *

## 2. Reviewing a Pull Request on GitHub[​](#2-reviewing-a-pull-request-on-github "Direct link to 2. Reviewing a Pull Request on GitHub")

### View PR Details[​](#view-pr-details "Direct link to View PR Details")

**With gh:**

```bash
gh pr view 123
gh prdiff123
gh prdiff123 --name-only
```

**With git + curl:**

```bash
PR_NUMBER=123

# Get PR details
curl-s\
-H"Authorization: token $GITHUB_TOKEN"\
  https://api.github.com/repos/$OWNER/$REPO/pulls/$PR_NUMBER\
| python3 -c"
import sys, json
pr = json.load(sys.stdin)
print(f\"Title: {pr['title']}\")
print(f\"Author: {pr['user']['login']}\")
print(f\"Branch: {pr['head']['ref']} -> {pr['base']['ref']}\")
print(f\"State: {pr['state']}\")
print(f\"Body:\n{pr['body']}\")"

# List changed files
curl-s\
-H"Authorization: token $GITHUB_TOKEN"\
  https://api.github.com/repos/$OWNER/$REPO/pulls/$PR_NUMBER/files \
| python3 -c"
import sys, json
for f in json.load(sys.stdin):
    print(f\"{f['status']:10} +{f['additions']:-4} -{f['deletions']:-4}  {f['filename']}\")"
```

### Check Out PR Locally for Full Review[​](#check-out-pr-locally-for-full-review "Direct link to Check Out PR Locally for Full Review")

This works with plain `git` — no `gh` needed:

```bash
# Fetch the PR branch and check it out
git fetch origin pull/123/head:pr-123
git checkout pr-123

# Now you can use read_file, search_files, run tests, etc.

# View diff against the base branch
gitdiff main...pr-123
```

**With gh (shortcut):**

**General PR comment — with gh:**

```bash
gh pr comment 123--body"Overall looks good, a few suggestions below."
```

**General PR comment — with curl:**

```bash
curl-s-X POST \
-H"Authorization: token $GITHUB_TOKEN"\
  https://api.github.com/repos/$OWNER/$REPO/issues/$PR_NUMBER/comments \
-d'{"body": "Overall looks good, a few suggestions below."}'
```

**Single inline comment — with gh (via API):**

```bash
HEAD_SHA=$(gh pr view 123--json headRefOid --jq'.headRefOid')

gh api repos/$OWNER/$REPO/pulls/123/comments \
--method POST \
-fbody="This could be simplified with a list comprehension."\
-fpath="src/auth/login.py"\
-fcommit_id="$HEAD_SHA"\
-fline=45\
-fside="RIGHT"
```

**Single inline comment — with curl:**

```bash
# Get the head commit SHA
HEAD_SHA=$(curl-s\
-H"Authorization: token $GITHUB_TOKEN"\
  https://api.github.com/repos/$OWNER/$REPO/pulls/$PR_NUMBER \
| python3 -c "import sys,json; print(json.load(sys.stdin)['head']['sha'])")

curl-s-X POST \
-H"Authorization: token $GITHUB_TOKEN"\
  https://api.github.com/repos/$OWNER/$REPO/pulls/$PR_NUMBER/comments \
-d"{
\"body\": \"This could be simplified with a list comprehension.\",
\"path\": \"src/auth/login.py\",
\"commit_id\": \"$HEAD_SHA\",
\"line\": 45,
\"side\": \"RIGHT\"
  }"
```

### Submit a Formal Review (Approve / Request Changes)[​](#submit-a-formal-review-approve--request-changes "Direct link to Submit a Formal Review (Approve / Request Changes)")

**With gh:**

```bash
gh pr review 123--approve--body"LGTM!"
gh pr review 123 --request-changes --body"See inline comments."
gh pr review 123--comment--body"Some suggestions, nothing blocking."
```

**With curl — multi-comment review submitted atomically:**

```bash
HEAD_SHA=$(curl-s\
-H"Authorization: token $GITHUB_TOKEN"\
  https://api.github.com/repos/$OWNER/$REPO/pulls/$PR_NUMBER \
| python3 -c "import sys,json; print(json.load(sys.stdin)['head']['sha'])")

curl-s-X POST \
-H"Authorization: token $GITHUB_TOKEN"\
  https://api.github.com/repos/$OWNER/$REPO/pulls/$PR_NUMBER/reviews \
-d"{
\"commit_id\": \"$HEAD_SHA\",
\"event\": \"COMMENT\",
\"body\": \"Code review from Hermes Agent\",
\"comments\": [
      {\"path\": \"src/auth.py\", \"line\": 45, \"body\": \"Use parameterized queries to prevent SQL injection.\"},
      {\"path\": \"src/models/user.py\", \"line\": 23, \"body\": \"Hash passwords with bcrypt before storing.\"},
      {\"path\": \"tests/test_auth.py\", \"line\": 1, \"body\": \"Add test for expired token edge case.\"}
    ]
  }"
```

Event values: `"APPROVE"`, `"REQUEST_CHANGES"`, `"COMMENT"`

The `line` field refers to the line number in the *new* version of the file. For deleted lines, use `"side": "LEFT"`.

* * *

## 3. Review Checklist[​](#3-review-checklist "Direct link to 3. Review Checklist")

When performing a code review (local or PR), systematically check:

### Correctness[​](#correctness "Direct link to Correctness")

- Does the code do what it claims?
- Edge cases handled (empty inputs, nulls, large data, concurrent access)?
- Error paths handled gracefully?

### Security[​](#security "Direct link to Security")

- No hardcoded secrets, credentials, or API keys
- Input validation on user-facing inputs
- No SQL injection, XSS, or path traversal
- Auth/authz checks where needed

### Code Quality[​](#code-quality "Direct link to Code Quality")

- Clear naming (variables, functions, classes)
- No unnecessary complexity or premature abstraction
- DRY — no duplicated logic that should be extracted
- Functions are focused (single responsibility)

### Testing[​](#testing "Direct link to Testing")

- New code paths tested?
- Happy path and error cases covered?
- Tests readable and maintainable?

### Performance[​](#performance "Direct link to Performance")

- No N+1 queries or unnecessary loops
- Appropriate caching where beneficial
- No blocking operations in async code paths

### Documentation[​](#documentation "Direct link to Documentation")

- Public APIs documented
- Non-obvious logic has comments explaining "why"
- README updated if behavior changed

* * *

## 4. Pre-Push Review Workflow[​](#4-pre-push-review-workflow "Direct link to 4. Pre-Push Review Workflow")

When the user asks you to "review the code" or "check before pushing":

1. `git diff main...HEAD --stat` — see scope of changes
2. `git diff main...HEAD` — read the full diff
3. For each changed file, use `read_file` if you need more context
4. Apply the checklist above
5. Present findings in the structured format (Critical / Warnings / Suggestions / Looks Good)
6. If critical issues found, offer to fix them before the user pushes

* * *

## 5. PR Review Workflow (End-to-End)[​](#5-pr-review-workflow-end-to-end "Direct link to 5. PR Review Workflow (End-to-End)")

When the user asks you to "review PR #N", "look at this PR", or gives you a PR URL, follow this recipe:

### Step 1: Set up environment[​](#step-1-set-up-environment "Direct link to Step 1: Set up environment")

```bash
source"${HERMES_HOME:-$HOME/.hermes}/skills/github/github-auth/scripts/gh-env.sh"
# Or run the inline setup block from the top of this skill
```

### Step 2: Gather PR context[​](#step-2-gather-pr-context "Direct link to Step 2: Gather PR context")

Get the PR metadata, description, and list of changed files to understand scope before diving into code.

**With gh:**

```bash
gh pr view 123
gh prdiff123 --name-only
gh pr checks 123
```

**With curl:**

```bash
PR_NUMBER=123

# PR details (title, author, description, branch)
curl-s-H"Authorization: token $GITHUB_TOKEN"\
  https://api.github.com/repos/$GH_OWNER/$GH_REPO/pulls/$PR_NUMBER

# Changed files with line counts
curl-s-H"Authorization: token $GITHUB_TOKEN"\
  https://api.github.com/repos/$GH_OWNER/$GH_REPO/pulls/$PR_NUMBER/files
```

### Step 3: Check out the PR locally[​](#step-3-check-out-the-pr-locally "Direct link to Step 3: Check out the PR locally")

This gives you full access to `read_file`, `search_files`, and the ability to run tests.

```bash
git fetch origin pull/$PR_NUMBER/head:pr-$PR_NUMBER
git checkout pr-$PR_NUMBER
```

### Step 4: Read the diff and understand changes[​](#step-4-read-the-diff-and-understand-changes "Direct link to Step 4: Read the diff and understand changes")

```bash
# Full diff against the base branch
gitdiff main...HEAD

# Or file-by-file for large PRs
gitdiff main...HEAD --name-only
# Then for each file:
gitdiff main...HEAD -- path/to/file.py
```

For each changed file, use `read_file` to see full context around the changes — diffs alone can miss issues visible only with surrounding code.

### Step 5: Run automated checks locally (if applicable)[​](#step-5-run-automated-checks-locally-if-applicable "Direct link to Step 5: Run automated checks locally (if applicable)")

```bash
# Run tests if there's a test suite
python -m pytest 2>&1|tail-20
# or: npm test, cargo test, go test ./..., etc.

# Run linter if configured
ruff check .2>&1|head-30
# or: eslint, clippy, etc.
```

### Step 6: Apply the review checklist (Section 3)[​](#step-6-apply-the-review-checklist-section-3 "Direct link to Step 6: Apply the review checklist (Section 3)")

Go through each category: Correctness, Security, Code Quality, Testing, Performance, Documentation.

### Step 7: Post the review to GitHub[​](#step-7-post-the-review-to-github "Direct link to Step 7: Post the review to GitHub")

Collect your findings and submit them as a formal review with inline comments.

**With gh:**

```bash
# If no issues — approve
gh pr review $PR_NUMBER--approve--body"Reviewed by Hermes Agent. Code looks clean — good test coverage, no security concerns."

# If issues found — request changes with inline comments
gh pr review $PR_NUMBER --request-changes --body"Found a few issues — see inline comments."
```

**With curl — atomic review with multiple inline comments:**

```bash
HEAD_SHA=$(curl-s-H"Authorization: token $GITHUB_TOKEN"\
  https://api.github.com/repos/$GH_OWNER/$GH_REPO/pulls/$PR_NUMBER \
| python3 -c "import sys,json; print(json.load(sys.stdin)['head']['sha'])")

# Build the review JSON — event is APPROVE, REQUEST_CHANGES, or COMMENT
curl-s-X POST \
-H"Authorization: token $GITHUB_TOKEN"\
  https://api.github.com/repos/$GH_OWNER/$GH_REPO/pulls/$PR_NUMBER/reviews \
-d"{
\"commit_id\": \"$HEAD_SHA\",
\"event\": \"REQUEST_CHANGES\",
\"body\": \"## Hermes Agent Review\n\nFound 2 issues, 1 suggestion. See inline comments.\",
\"comments\": [
      {\"path\": \"src/auth.py\", \"line\": 45, \"body\": \"🔴 **Critical:** User input passed directly to SQL query — use parameterized queries.\"},
      {\"path\": \"src/models.py\", \"line\": 23, \"body\": \"⚠️ **Warning:** Password stored without hashing.\"},
      {\"path\": \"src/utils.py\", \"line\": 8, \"body\": \"💡 **Suggestion:** This duplicates logic in core/utils.py:34.\"}
    ]
  }"
```

In addition to inline comments, leave a top-level summary so the PR author gets the full picture at a glance. Use the review output format from `references/review-output-template.md`.

**With gh:**

```bash
gh pr comment $PR_NUMBER--body"$(cat<<'EOF'
## Code Review Summary

**Verdict: Changes Requested** (2 issues, 1 suggestion)

### 🔴 Critical
- **src/auth.py:45** — SQL injection vulnerability

### ⚠️ Warnings
- **src/models.py:23** — Plaintext password storage

### 💡 Suggestions
- **src/utils.py:8** — Duplicated logic, consider consolidating

### ✅ Looks Good
- Clean API design
- Good error handling in the middleware layer

---
*Reviewed by Hermes Agent*
EOF
)"
```

### Step 9: Clean up[​](#step-9-clean-up "Direct link to Step 9: Clean up")

```bash
git checkout main
git branch -D pr-$PR_NUMBER
```

- **Approve** — no critical or warning-level issues, only minor suggestions or all clear
- **Request Changes** — any critical or warning-level issue that should be fixed before merge
- **Comment** — observations and suggestions, but nothing blocking (use when you're unsure or the PR is a draft)