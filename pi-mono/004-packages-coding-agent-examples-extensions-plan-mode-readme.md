---
title: Plan Mode Extension
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/examples/extensions/plan-mode/README.md
source: git
fetched_at: 2026-05-03T09:31:41.357456535-03:00
rendered_js: false
word_count: 322
summary: Read-only exploration mode for safe code analysis with explicit step tracking and bash allowlist.
tags:
    - plan-mode
    - read-only-tools
    - task-execution
    - workflow-automation
    - code-analysis
    - bash-allowlist
category: concept
optimized: true
optimized_at: 2026-05-03T12:31:00Z
---
# Plan Mode Extension

Read-only exploration mode for safe code analysis.

## Features

- **Read-only tools**: Restricts to `read`, `bash`, `grep`, `find`, `ls`, `question`
- **Bash allowlist**: Only safe read-only commands allowed
- **Plan extraction**: Parses numbered steps from `Plan:` sections
- **Progress tracking**: Widget shows completion status during execution
- **`[DONE:n]` markers**: Explicit step completion tracking
- **Session persistence**: State survives session resume

## Commands

| Command | Description |
|---------|-------------|
| `/plan` | Toggle plan mode |
| `/todos` | Show current plan progress |
| `Ctrl+Alt+P` | Toggle plan mode (shortcut) |

## Usage

1. Enable plan mode: `/plan` or `--plan` flag
2. Ask agent to analyze code and create a plan
3. Agent outputs numbered plan under `Plan:` header:

```
Plan:
1. First step
2. Second step
3. Third step
```

4. Choose "Execute the plan" when prompted
5. Agent marks steps with `[DONE:n]` tags during execution
6. Progress widget displays completion status

## How It Works

### Plan Mode (Read-Only)
- Only read-only tools available
- Bash commands filtered through allowlist
- Agent creates plan without making changes

### Execution Mode
- Full tool access restored
- Agent executes steps in order
- `[DONE:n]` markers track completion
- Widget shows progress

## Bash Allowlist

### Allowed Commands

| Category | Commands |
|----------|----------|
| File inspection | `cat`, `head`, `tail`, `less`, `more` |
| Search | `grep`, `find`, `rg`, `fd` |
| Directory | `ls`, `pwd`, `tree` |
| Git read | `git status`, `git log`, `git diff`, `git branch` |
| Package info | `npm list`, `npm outdated`, `yarn info` |
| System info | `uname`, `whoami`, `date`, `uptime` |

### Blocked Commands

| Category | Blocked |
|----------|---------|
| File modification | `rm`, `mv`, `cp`, `mkdir`, `touch` |
| Git write | `git add`, `git commit`, `git push` |
| Package install | `npm install`, `yarn add`, `pip install` |
| System | `sudo`, `kill`, `reboot` |
| Editors | `vim`, `nano`, `code` |

#plan-mode #read-only-tools #task-execution
