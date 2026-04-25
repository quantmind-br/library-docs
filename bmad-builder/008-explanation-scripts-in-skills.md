---
title: Scripts in Skills
url: https://bmad-builder-docs.bmad-method.org/explanation/scripts-in-skills/
source: sitemap
fetched_at: 2026-04-08T11:33:05.383575207-03:00
rendered_js: false
word_count: 821
summary: This document outlines the best practice of using external scripts for deterministic tasks within AI skills, allowing Large Language Models (LLMs) to focus on judgment and creativity. It details when to use scripting over LLM prompting, emphasizes Python's benefits over Bash, and describes modern dependency management via PEP 723.
tags:
    - scripting-vs-llm
    - determinism
    - python-best-practices
    - dependency-management
    - ai-skill-design
category: guide
---

Scripts handle work that has clear right-and-wrong answers (validation, transformation, extraction, counting) so the LLM can focus on judgment, synthesis, and creative reasoning.

## The Problem: LLMs Do Too Much

[Section titled “The Problem: LLMs Do Too Much”](#the-problem-llms-do-too-much)

Without scripts, every operation in a skill runs through the LLM. That means:

- **Non-deterministic results.** Ask an LLM to count tokens in a file three times and you may get three different numbers. Ask a script and you get the same answer every time.
- **Wasted tokens and time.** Parsing a JSON file, checking if a directory exists, or comparing two strings are mechanical operations. Running them through the LLM burns context window and adds latency for no gain.
- **Harder to test.** You can write unit tests for a script. You cannot write unit tests for an LLM prompt.

The pattern shows up everywhere: skills that try to LLM their way through structural validation are slower, less reliable, and more expensive than skills that offload those checks to scripts.

## The Determinism Boundary

[Section titled “The Determinism Boundary”](#the-determinism-boundary)

The design principle is **intelligence placement**: put each operation where it belongs.

Scripts HandleLLM HandlesValidate structure, format, schemaInterpret meaning, evaluate qualityCount, parse, extract, transformClassify ambiguous input, make judgment callsCompare, diff, check consistencySynthesize insights, generate creative outputPre-process data into compact formAnalyze pre-processed data with domain reasoning

**The test:** Given identical input, will this operation always produce identical output? If yes, it belongs in a script. Could you write a unit test with expected output? Definitely a script. Requires interpreting meaning, tone, or context? Keep it as an LLM prompt.

## Why Python, Not Bash

[Section titled “Why Python, Not Bash”](#why-python-not-bash)

Skills must work across macOS, Linux, and Windows. Bash is not portable.

FactorBashPython**macOS / Linux**WorksWorks**Windows (native)**Fails or behaves inconsistentlyWorks identically**Windows (WSL)**Works, but can conflict with Git Bash on PATHWorks identically**Error handling**Limited, fragileRich exception handling**Testing**DifficultStandard unittest/pytest**Complex logic**Quickly becomes unreadableClean, maintainable

Even basic commands like `sed -i` behave differently on macOS vs Linux. Piping, `jq`, `grep`, `awk`. All of these have cross-platform pitfalls that Python’s standard library avoids entirely.

**Safe bash commands** that work everywhere and remain fine to use directly:

CommandPurpose`git`, `gh`Version control and GitHub CLI`uv run`Python script execution`npm`, `npx`, `pnpm`Node.js ecosystem`mkdir -p`Directory creation

Everything beyond that list should be a Python script.

## Standard Library First

[Section titled “Standard Library First”](#standard-library-first)

Python’s standard library covers most script needs without any external dependencies. Stdlib-only scripts run with plain `python3`, need no special tooling, and have zero supply-chain risk.

NeedStandard LibraryJSON parsing`json`Path handling`pathlib`Pattern matching`re`CLI interface`argparse`Text comparison`difflib`Counting, grouping`collections`Source analysis`ast`Data formats`csv`, `xml.etree`

Only reach for external dependencies when the stdlib genuinely cannot do the job: `tiktoken` for accurate token counting, `pyyaml` for YAML parsing, `jsonschema` for schema validation. Each external dependency adds install-time cost, requires `uv` to be available, and expands the supply-chain surface. The BMad builders require explicit user approval for any external dependency during the build process.

## Zero-Friction Dependencies with PEP 723

[Section titled “Zero-Friction Dependencies with PEP 723”](#zero-friction-dependencies-with-pep-723)

Python scripts in skills use [PEP 723](https://peps.python.org/pep-0723/) inline metadata to declare their dependencies directly in the file. Combined with `uv run`, this gives you `npx`-like behavior: dependencies are silently cached in an isolated environment, no global installs, no user prompts.

```python

#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6.0"]
# ///
import yaml
# script logic here
```

When a skill invokes this script with `uv run scripts/analyze.py`, the dependency (`pyyaml` in this example) is automatically resolved. The user never sees an install prompt, never needs to manage a virtual environment, and never pollutes their global Python installation.

Without PEP 723, skills that need libraries like `pyyaml` or `tiktoken` would force users to run `pip install`, a jarring experience that makes people hesitate to adopt the skill.

## Graceful Degradation

[Section titled “Graceful Degradation”](#graceful-degradation)

Skills run in multiple environments: CLI terminals, desktop apps, IDE extensions, and web interfaces like claude.ai. Not all environments can execute Python scripts.

The principle: **scripts are the fast, reliable path, but the skill must still deliver its outcome when execution is unavailable.**

When a script cannot run, the LLM performs the equivalent work directly. This is slower and less deterministic, but the user still gets a result. The script’s `--help` output documents what it checks, making the fallback natural. The LLM reads the help to understand the script’s purpose and replicates the logic.

Frame script steps as outcomes in the SKILL.md, not just commands:

ApproachExample**Good**”Validate path conventions (run `scripts/scan-paths.py --help` for details)“**Fragile**”Execute `python3 scripts/scan-paths.py`” with no context

The good version tells the LLM both what to accomplish and where to find the details, enabling graceful degradation without additional instructions.

## When to Reach for a Script

[Section titled “When to Reach for a Script”](#when-to-reach-for-a-script)

Look for these signal verbs in a skill’s requirements; they indicate script opportunities:

SignalScript Type”validate”, “check”, “verify”Validation”count”, “tally”, “aggregate”Metrics”extract”, “parse”, “pull from”Data extraction”convert”, “transform”, “format”Transformation”compare”, “diff”, “match against”Comparison”scan for”, “find all”, “list all”Pattern scanning

The builders guide you through script opportunity discovery during the build process. If you find yourself writing detailed validation logic in a prompt, it almost certainly belongs in a script instead.