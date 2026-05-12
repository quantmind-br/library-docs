---
title: Rules
url: https://developers.openai.com/codex/rules.md
source: llms
fetched_at: 2026-04-30T10:16:01.541708799-03:00
rendered_js: false
word_count: 515
summary: This document explains how to configure and manage security rules in Codex to control command execution outside the sandbox using prefix-based matching and Starlark-based policy files.
tags:
    - codex
    - security-policy
    - command-execution
    - sandbox-configuration
    - starlark
    - access-control
category: configuration
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Rules

Control which commands Codex can run outside the sandbox.

> [!warning]
> Experimental and may change.

## Create a rules file

1. Create a `.rules` file under `rules/` next to an active config layer (e.g., `~/.codex/rules/default.rules`).
2. Add a rule. Example: prompt before allowing `gh pr view` outside the sandbox.

```python
prefix_rule(
    pattern = ["gh", "pr", "view"],
    decision = "prompt",
    justification = "Viewing PRs is allowed with approval",
    match = [
        "gh pr view 7888",
        "gh pr view --repo openai/codex",
        "gh pr view 7888 --json title,body,comments",
    ],
    not_match = [
        # Does not match: pattern must be exact prefix
        "gh pr --repo openai/codex view 7888",
    ],
)
```

3. Restart Codex.

Codex scans `rules/` under every active config layer at startup, including [[009-enterprise-admin-setup#team-config|Team Config]] locations and user layer at `~/.codex/rules/`. Project-local rules under `<repo>/.codex/rules/` load only when project `.codex/` layer is trusted.

When you add a command to the allow list in the TUI, Codex writes to `~/.codex/rules/default.rules` so future runs skip the prompt.

When Smart approvals are enabled (default), Codex may propose a `prefix_rule` during escalation requests. Review suggested prefix carefully before accepting.

Admins can also enforce restrictive `prefix_rule` entries from [[018-enterprise-managed-configuration#admin-enforced-requirements-requirementstoml|requirements.toml]].

## Rule fields

`prefix_rule()` supports:

- `pattern` **(required)**: non-empty list defining command prefix to match. Each element is:
  - literal string (e.g., `"pr"`)
  - union of literals (e.g., `["view", "list"]`) for alternatives at that position
- `decision` (default `"allow"`): action when rule matches. Most restrictive wins when multiple rules match: `forbidden` > `prompt` > `allow`
  - `allow`: run without prompting
  - `prompt`: prompt before each matching invocation
  - `forbidden`: block without prompting
- `justification` (optional): human-readable reason surfaced in approval prompts or rejection messages. For `forbidden`, include recommended alternative (e.g., `"Use \`rg\` instead of \`grep\`.")")
- `match` / `not_match` (default `[]`): inline unit tests validated when rules load. Catch mistakes before a rule takes effect.

Codex compares command's argument list to `pattern`. Internally treats command as list of arguments (like `execvp(3)` receives).

## Shell wrappers and compound commands

Tools wrapping several shell commands into one invocation, e.g.:
```text
["bash", "-lc", "git add . && rm -rf /"]
```

Codex treats `bash -lc`, `bash -c`, and `zsh`/`sh` equivalents specially.

### When Codex can safely split the script

If script is linear chain of commands made only of:
- plain words (no variable expansion, no `VAR=...`, `$FOO`, `*`, etc.)
- joined by safe operators (`&&`, `||`, `;`, `|`)

Then Codex parses (using tree-sitter) and splits into individual commands before applying rules.

Example `bash -lc "git add . && rm -rf /"` becomes:
- `["git", "add", "."]`
- `["rm", "-rf", "/"]`

Each command evaluated separately; most restrictive result wins. Even if you allow `["git", "add"]`, `git add . && rm -rf /` won't auto-allow because `rm -rf /` prevents it.

### When Codex does not split the script

If script uses:
- redirection (`>`, `>>`, `<`)
- substitutions (`$(...)`, `` `...` ``)
- environment variables (`FOO=bar`)
- wildcard patterns (`*`, `?`)
- control flow (`if`, `for`, `&&` with assignments, etc.)

Then Codex doesn't interpret or split it. Entire invocation treated as `["bash", "-lc", "<full script>"]` and rules applied to that **single** invocation.

Per-command evaluation when safe; conservative behavior when not.

## Test a rule file

```shell
codex execpolicy check --pretty \
  --rules ~/.codex/rules/default.rules \
  -- gh pr view 7888 --json title,body,comments
```

Emits JSON showing strictest decision and matching rules. Combine multiple `--rules` flags. Add `--pretty` to format.

## Rules language

`.rules` files use `Starlark` ([language spec](https://github.com/bazelbuild/starlark/blob/master/spec.md)). Python-like syntax designed to be safe: rules engine runs it without side effects (no filesystem access).

#rules #security #sandbox #starlark #command-execution #codex