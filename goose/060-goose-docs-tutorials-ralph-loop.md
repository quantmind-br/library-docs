---
title: Ralph Loop | goose
url: https://block.github.io/goose/docs/tutorials/ralph-loop
source: github_pages
fetched_at: 2026-01-22T22:16:21.414550911-03:00
rendered_js: true
word_count: 663
summary: This document explains the Ralph Loop, an iterative development pattern for AI agents that utilizes fresh context and cross-model review to complete complex tasks. It provides a step-by-step tutorial on configuring the worker and reviewer models and running the process via the goose CLI.
tags:
    - ralph-loop
    - goose-ai
    - iterative-development
    - agentic-workflows
    - cross-model-review
    - ai-coding
category: tutorial
---

Ralph Loop, based on [Geoffrey Huntley's Ralph Wiggum technique](https://ghuntley.com/ralph/), is an iterative development pattern that keeps goose working on a task until it's genuinely complete.

Standard agent loops suffer from context accumulation. Every failed attempt stays in the conversation history, which means that after a few iterations, the model must process a long history of noise before it can focus on the task. Ralph Loop solves this by starting each iteration with fresh context, the core insight behind Geoffrey's approach. This implementation extends the technique with cross-model review: one model does the work, a different model reviews it, and the loop continues until the task is ready to ship.

After each iteration, the worker and reviewer models store a summary and feedback in files. These files persist between iterations but the conversation history does not. This allows a new session to start where the next model reads the files to pick up exactly where the last iteration left off.

In this tutorial, we'll use Ralph Loop to build a simple Electron-based browser and see how the iteration cycle catches missing features before shipping.

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

- [Install the goose CLI](https://block.github.io/goose/docs/getting-started/installation) because the Ralph Loop runs via the terminal.
- [Configure two models](https://block.github.io/goose/docs/getting-started/providers) to serve as the worker and reviewer. Using different models is recommended for higher quality reviews, though the loop still works if you use the same model for both roles.

Download the Ralph Loop Recipes

Cost Warning

Ralph Loop runs your agent multiple times in a loop (up to 10 iterations by default). Monitor your usage and adjust `RALPH_MAX_ITERATIONS` if needed.

### Step 1: Start the Loop[​](#step-1-start-the-loop "Direct link to Step 1: Start the Loop")

To start the process, run the script from your terminal and provide your prompt in quotes. This command triggers the first iteration of the worker and reviewer cycle:

```
~/.config/goose/recipes/ralph-loop.sh "Create a simple browser using Electron and React"
```

For Complex Tasks

You can pass a file path instead of a string. This works well for PRDs, detailed specs, or any multi-step task that benefits from iterative development:

```
~/.config/goose/recipes/ralph-loop.sh ./prd.md
```

### Step 2: Configure Models[​](#step-2-configure-models "Direct link to Step 2: Configure Models")

The script will ask you to set your environment variables for the session:

```
Worker model [gpt-4o]: 
Worker provider [openai]: 
Reviewer model (should be different from worker): claude-sonnet-4-20250514
Reviewer provider: anthropic
Max iterations [10]: 

⚠️  Cost Warning: This will run up to 10 iterations, each using both models.
    Estimated token usage could be significant depending on your task.

Continue? [y/N]: y
```

VariableDescriptionWorker modelThe model that does the actual coding work. Defaults to `GOOSE_MODEL` if set.Worker providerThe provider for the worker model (e.g., `openai`, `anthropic`). Defaults to `GOOSE_PROVIDER` if set.Reviewer modelThe model that reviews the work. Should be different from the worker for best results.Reviewer providerThe provider for the reviewer model.Max iterationsHow many work/review cycles before giving up. Defaults to 10.

Directly Set Environment Variables

You can skip the interactive prompts by setting environment variables directly

```
RALPH_WORKER_MODEL="gpt-4o" \
RALPH_WORKER_PROVIDER="openai" \
RALPH_REVIEWER_MODEL="claude-sonnet-4-20250514" \
RALPH_REVIEWER_PROVIDER="anthropic" \
~/.config/goose/recipes/ralph-loop.sh "Create a simple browser using Electron and React"
```

### Step 3: Watch It Run[​](#step-3-watch-it-run "Direct link to Step 3: Watch It Run")

The terminal will show goose moving through the worker and reviewer phases. Each iteration starts with a fresh session to keep the context clean. Here's what a successful run looks like:

```
═══════════════════════════════════════════════════════════════
  Ralph Loop - Multi-Model Edition
═══════════════════════════════════════════════════════════════

  Task: Create a simple browser using Electron and React
  Worker: gpt-4o (openai)
  Reviewer: claude-sonnet-4-20250514 (anthropic)
  Max Iterations: 10

───────────────────────────────────────────────────────────────
  Iteration 1 / 10
───────────────────────────────────────────────────────────────

▶ WORK PHASE
... (goose creates initial implementation) ...

▶ REVIEW PHASE
... (goose reviews the work) ...

↻ REVISE - Feedback for next iteration:
Missing error handling for invalid URLs. Also needs back/forward navigation buttons.

───────────────────────────────────────────────────────────────
  Iteration 2 / 10
───────────────────────────────────────────────────────────────

▶ WORK PHASE
... (goose addresses feedback) ...

▶ REVIEW PHASE
... (goose reviews again) ...

═══════════════════════════════════════════════════════════════
  ✓ SHIPPED after 2 iteration(s)
═══════════════════════════════════════════════════════════════
```

## How It Works[​](#how-it-works "Direct link to How It Works")

```
Iteration 1:
  WORK PHASE  → Model A does work, writes to files
  REVIEW PHASE → Model B reviews the work
    → SHIP? Exit successfully ✓
    → REVISE? Write feedback, continue to iteration 2

Iteration 2:
  WORK PHASE  → Model A reads feedback, fixes things (fresh context!)
  REVIEW PHASE → Model B reviews again
    → SHIP? Exit successfully ✓
    → REVISE? Continue...

... repeats until SHIP or max iterations
```

### State Files[​](#state-files "Direct link to State Files")

Ralph Loop uses files in `.goose/ralph/` to persist state between iterations. This is how the worker knows what to do and the reviewer knows what was done, even though each iteration starts with fresh context.

FilePurpose`task.md`The task description`iteration.txt`Current iteration number`work-summary.txt`What the worker did this iteration`work-complete.txt`Exists when worker claims done`review-result.txt``SHIP` or `REVISE``review-feedback.txt`Feedback for next iteration`.ralph-complete`Created on successful completion`RALPH-BLOCKED.md`Created if worker is stuck

### Recipe Files[​](#recipe-files "Direct link to Recipe Files")

The Ralph Loop uses three files: a bash script that orchestrates the work/review cycle, a work recipe that tells the worker model how to make progress, and a review recipe that tells the reviewer model how to evaluate the work. Below are the contents of each file. You can [download](#prerequisites) them or copy directly from here.

The Bash Wrapper (`ralph-loop.sh`)

Work Phase Recipe (`ralph-work.yaml`)

Review Phase Recipe (`ralph-review.yaml`)

## Usage Tips[​](#usage-tips "Direct link to Usage Tips")

### When to Use Ralph Loop[​](#when-to-use-ralph-loop "Direct link to When to Use Ralph Loop")

Ralph Loop works best for:

- **Complex, multi-step tasks** that benefit from iteration
- **Tasks with clear completion criteria** (tests pass, builds succeed)
- **Situations where you want quality gates** before shipping

It's overkill for:

- Simple one-shot tasks
- Interactive/exploratory work
- Tasks without verifiable completion criteria

### Resetting[​](#resetting "Direct link to Resetting")

If you want to start a completely new task, or if a previous run got stuck and you want to start over, you can clear the state directory: