---
title: Amp Owner’s Manual
url: https://ampcode.com/manual
source: crawler
fetched_at: 2026-02-06T02:07:29.896618339-03:00
rendered_js: false
word_count: 6853
summary: This document provides a comprehensive guide to installing and utilizing the Amp coding agent, covering its operational modes, prompting best practices, and configuration through AGENTS.md files.
tags:
    - amp-coding-agent
    - ai-assistant
    - cli-installation
    - vs-code-extension
    - prompt-engineering
    - developer-tools
category: guide
---

## **Congratulations** on installing Amp. This manual helps you get the most out of it.

## Why Amp?[#](#why-amp)[#](#why-amp)

Amp is the frontier coding agent for your terminal and editor.

- **Multi-Model:** Opus 4.6, GPT-5.2, fast models—Amp uses them all, for what each model is best at.
- **Opinionated:** You’re always using the good parts of Amp. If we don’t use and love a feature, we kill it.
- **On the Frontier:** Amp goes where the models take it. No backcompat, no legacy features.
- **Threads:** You can save and share your interactions with Amp. You wouldn’t code without version control, would you?

Amp has 2 modes: `smart` (unconstrained state-of-the-art model use) and `rush` (faster, cheaper, suited for small, well-defined tasks). New users receive a $10 daily grant for free usage across all modes.

*Want to go much deeper? Watch our [Raising an Agent podcast](https://ampcode.com/podcast) that chronicles the first few months of building Amp, and see our [FIF](https://ampcode.com/fif).*

![Amp in VS Code](https://static.ampcode.com/content/amp-vscode-1.png)

## Get Started[#](#get-started)[#](#get-started)

1. Sign into [ampcode.com/install](https://ampcode.com/install).
2. Follow the instructions to install the Amp CLI and editor extensions for VS Code, Cursor, Antigravity, JetBrains, Neovim, and other editors.

You’re ready to [start using Amp](#usage)!

### From the Command Line[#](#getting-started-command-line-interface)[#](#getting-started-command-line-interface)

Our recommended install method for macOS, Linux and WSL. It supports auto-updating and fast launch via Bun.

Install the Amp CLI:

```
curl -fsSL https://ampcode.com/install.sh | bash
```

Run interactively (will prompt for login on first run):

```
amp
```

You can also [install via npm](https://www.npmjs.com/package/@sourcegraph/amp) if necessary.

### From Your Editor[#](#getting-started-editor)[#](#getting-started-editor)

Sign into [ampcode.com/install](https://ampcode.com/install) and follow the instructions, or:

- **VS Code, Cursor, Antigravity (and other forks):** Install the `sourcegraph.amp` extension from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=sourcegraph.amp) or [Open VSX Registry](https://open-vsx.org/extension/sourcegraph/amp).
- **JetBrains (IntelliJ, WebStorm, GoLand, etc.):** Install the Amp CLI, then run `amp --jetbrains`.
- **Neovim:** Install the Amp CLI and the [Amp Neovim plugin](https://github.com/sourcegraph/amp.nvim), then run `amp`.

## Using Amp[#](#usage)[#](#usage)

### Agent Modes[#](#agent-modes)[#](#agent-modes)

Amp has 3 modes:

- **`smart`** : Uses state-of-the-art models without constraints for maximum capability and autonomy.
- **`rush`** : Faster, cheaper, and less capable, suitable for small, well-defined tasks. See [Rush Mode](https://ampcode.com/news/rush-mode).
- **`deep`** : Deep reasoning with GPT-5.2 Codex for extended thinking on complex problems.

*There’s one more that’s hidden: [`large` mode](https://ampcode.com/news/large-mode).*

See [Models](https://ampcode.com/models) for the models used by each mode.

Switch modes in the CLI by opening the command palette (`Ctrl+O`) and typing `mode`, or select the mode in the prompt field of the editor extension.

### How to Prompt[#](#how-to-prompt)[#](#how-to-prompt)

Amp currently uses Claude Opus 4.6 for most tasks, with up to 200k tokens of context. For the best results, follow these guidelines:

- Be explicit with what you want. Instead of “can you do X?”, try “do X.”
- Keep it short, keep it focused. Break very large tasks up into smaller sub-tasks, one per thread. Do not ask the agent to write database migrations in the same thread as it previously changed CSS for a documentation page.
- Don’t try to make the model guess. If you know something about how to achieve what you want the agent to do — which files to look at, which commands to run — put it in your prompt.
- If you want the model to not write any code, but only to research and plan, say so: “Only plan how to implement this. Do NOT write any code.”
- Use [`AGENTS.md` files](#AGENTS.md) to guide Amp on how to run your tests and build steps and to avoid common mistakes.
- Abandon threads if they accumulated too much noise. Sometimes things go wrong and failed attempts with error messages clutter up the context window. In those cases, it’s often best to start with a new thread and a clean context window.
- Tell the agent how to best review its work: what command or test to run, what URL to open, which logs to read. Feedback helps agents as much as it helps us.

The first prompt in the thread carries a lot of weight. It sets the direction for the rest of the conversation. We encourage you to be deliberate with it. That’s why we use `Cmd/Ctrl+Enter` to submit a message in Amp — it’s a reminder to put effort into a prompt.

Here are some examples of prompts we’ve used with Amp:

- “Make `observeThreadGuidanceFiles` return `Omit<ResolvedGuidanceFile, 'content'>[]` and remove that field from its return value, and update the tests. Note that it is omitted because this is used in places that do not need the file contents, and this saves on data transferred over the view API.” ([See Thread](https://ampcode.com/threads/T-9219191b-346b-418a-b521-7dc54fcf7f56))
- “Run `<build command>` and fix all the errors”
- “Look at `<local development server url>` to see this UI component. Then change it so that it looks more minimal. Frequently check your work by screenshotting the URL”
- “Run git blame on the file I have open and figure out who added that new title”
- “Convert these 5 files to use Tailwind, use one subagent per file”
- “Take a look at `git diff` — someone helped me build a debug tool to edit a Thread directly in JSON. Please analyze the code and see how it works and how it can be improved. \[…]” ([See Thread](https://ampcode.com/threads/T-39dc399d-08cc-4b10-ab17-e6bac8badea7))
- “Check `git diff --staged` and remove the debug statements someone added” ([See Thread](https://ampcode.com/threads/T-66beb0de-7f02-4241-a25e-50c0dc811788))
- “Find the commit that added this using git log, look at the whole commit, then help me change this feature”
- “Explain the relationship between class AutoScroller and ViewUpdater using a diagram”
- “Run `psql` and rewire all the `threads` in the databaser to my user (email starts with thorsten)” ([See Thread](https://ampcode.com/threads/T-f810ef79-ba0e-4338-87c6-dbbb9085400a))

Also see Thorsten Ball’s [How I Use Amp](https://ampcode.com/how-i-use-amp).

If you’re in a workspace, use Amp’s [thread sharing](#thread-sharing) to learn from each other.

### AGENTS.md[#](#AGENTS.md)[#](#AGENTS.md)

Amp looks in `AGENTS.md` files for guidance on codebase structure, build/test commands, and conventions.

FileExamples`AGENTS.md`  
in cwd, parent dirs, & subtreesArchitecture, build/test commands, overview of internal APIs, review and release steps`$HOME/.config/amp/AGENTS.md`  
`$HOME/.config/AGENTS.md`Personal preferences, device-specific commands, and guidance that you're testing locally before committing to your repository

Amp includes `AGENTS.md` files automatically:

- `AGENTS.md` files in the current working directory (or editor workspace roots) *and* parent directories (up to `$HOME`) are always included.
- Subtree `AGENTS.md` files are included when the agent reads a file in the subtree.
- Both `$HOME/.config/amp/AGENTS.md` and `$HOME/.config/AGENTS.md` are included if they exist.

If no `AGENTS.md` exists in a directory, but a file named `AGENT.md` (without an `S`) or `CLAUDE.md` does exist, that file will be included.

In a large repository with multiple subprojects, we recommend keeping the top-level `AGENTS.md` general and creating more specific `AGENTS.md` files in subtrees for each subproject.

To see the agent files that Amp is using, select agents-md list from the command palette or hover the X% of 168k indicator after you’ve sent the first message in a thread (editor extension).

#### Writing AGENTS.md Files[#](#writing-agentsmd-files)[#](#writing-agentsmd-files)

Amp offers to generate an `AGENTS.md` file for you if none exists. You can create or update any `AGENTS.md` files manually or by asking Amp (*“Update AGENTS.md based on what I told you in this thread”*).

To include other files as context, @-mention them in agent files. For example:

```
See @doc/style.md and @specs/**/*.md.

When making commits, see @doc/git-commit-instructions.md.
```

- Relative paths are interpreted relative to the agent file containing the mention.
- Absolute paths and `@~/some/path` are also supported.
- @-mentions in code blocks are ignored, to avoid false positives.
- Glob patterns are supported (such as `@doc/*.md` or `@.agent/**/*.md`).

#### Granular Guidance[#](#granular-guidance)[#](#granular-guidance)

To provide guidance that only applies when working with certain files, you can specify `globs` in YAML front matter of mentioned files.

For example, to apply language-specific coding rules:

1. Put `See @docs/*.md` anywhere in your `AGENTS.md` file.
2. Create a file `docs/typescript-conventions.md` with:
   
   ```
   ---
   globs:
     - '**/*.ts'
     - '**/*.tsx'
   ---
   
   Follow these TypeScript conventions:
   
   - Never use the `any` type
   - ...
   ```
3. Repeat for other languages.

Mentioned files with `globs` will only be included if Amp has read a file matching any of the globs (in the example above, any TypeScript file). If no `globs` are specified, the file is always included when @-mentioned.

Globs are implicitly prefixed with `**/` unless they start with `../` or `./`, in which case they refer to paths relative to the mentioned file.

Other examples:

- Frontend-specific guidance: `globs: ["src/components/**", "**/*.tsx"]`
- Backend guidance: `globs: ["server/**", "api/**"]`
- Test guidance: `globs: ["*.test.ts", "__tests__/*"]`

#### Migrating to AGENTS.md

[#](#migrating-to-agentsmd)[#](#migrating-to-agentsmd)

- From Claude Code: `mv CLAUDE.md AGENTS.md && ln -s AGENTS.md CLAUDE.md`, and repeat for subtree `CLAUDE.md` files
- From Cursor: `mv .cursorrules AGENTS.md && ln -s AGENTS.md .cursorrules` and then add `@.cursor/rules/*.mdc` anywhere in `AGENTS.md` to include all Cursor rules files.
- From existing AGENT.md: `mv AGENT.md AGENTS.md` (optional - both filenames continue to work)

### Handoff[#](#handoff)[#](#handoff)

Amp works best when you keep threads small and focused on a single task

To continue your work from one thread in a new thread, use the `handoff` command from the command palette to draft a new thread with relevant files and context from the original thread.

Provide some help to the handoff command to direct the new prompt. For example:

- `now implement this for teams as well, not just individual users`
- `execute phase one of the created plan`
- `check the rest of the codebase and find other places that need this fix`

See [Handoff (No More Compaction)](https://ampcode.com/news/handoff) for why Amp doesn’t support compaction.

### Referencing Other Threads[#](#referencing-threads)[#](#referencing-threads)

You can reference other Amp threads by thread URL (e.g., `https://ampcode.com/threads/T-7f395a45-7fae-4983-8de0-d02e61d30183`) or thread ID (e.g., `@T-7f395a45-7fae-4983-8de0-d02e61d30183`) in your prompt.

Type `@@` to search for a thread to mention.

For each mentioned thread, Amp will read and extract relevant information to your current task. This is useful to continue work from or reuse techniques from a previous thread.

Examples:

- `Implement the plan from https://ampcode.com/threads/T-7f395a45-7fae-4983-8de0-d02e61d30183`
- `Apply the same fix from @T-7f395a45-7fae-4983-8de0-d02e61d30183 to the form here`

### Finding Threads[#](#finding-threads)[#](#finding-threads)

Amp can search through your past threads and your workspace members’ threads to find relevant conversations. Ask Amp to find threads by keyword, file path, repository, author, date, or task.

Examples:

- `Find threads where we discussed the monorepo migration`
- `Show me threads that modified src/server/index.ts`
- `Find Thorsten's threads on the indexing logic`
- `Show me my recent threads from the last week`
- `Which threads worked on task 142?`
- `Find threads related to this one` (via handoff or thread references)

### Archiving Threads[#](#archiving)[#](#archiving)

When you archive a thread, it no longer appears in your list of active threads but can still be viewed on the web and [referenced by @-mention](#referencing-threads).

To archive a thread, from the command palette, run `thread: archive and exit` in the CLI or `Thread: Archive` in the editor extension.

### Attaching Images[#](#images)[#](#images)

You can attach images (such as screenshots and diagrams) to your messages.

In the CLI, press `Ctrl+V` to paste an image from the clipboard. Note that you must use `Ctrl+V`, not `Cmd+V`, even on macOS.

In the editor extension, paste an image using `Cmd+V`/`Ctrl+V`, or hold `Shift` and drag an image over the message field.

You can also @-mention images by file path.

### Mentioning Files[#](#mentioning-files)[#](#mentioning-files)

Type `@` to search for a file to mention.

### Edit & Undo[#](#edit-undo)[#](#edit-undo)

Editing a prior message in a thread automatically reverts any changes the agent made *after* that message.

To edit a prior message in the CLI, press `Tab` to navigate to prior messages. In the editor extension, scroll up in the thread and click on a prior message.

You can also revert individual file changes by clicking the `N files changed` indicator.

### Queueing Messages[#](#queueing-messages)[#](#queueing-messages)

You can queue messages to be sent to the agent once it ends its turn, without interrupting its current work. To queue a message:

- In the editor extension, type your message and press `Cmd-Shift-Enter` (macOS) or `Ctrl-Shift-Enter` (Windows/Linux).
- In the CLI, use the `queue` command from the command palette.

### Keyboard Shortcuts[#](#shortcuts)[#](#shortcuts)

##### Platform and Editor Selection

##### Shortcuts for macOS and VS Code

CommandShortcutNew Thread

`CmdL`

Focus/Hide Amp Sidebar

`CmdI`

Switch to Thread

`CmdK`

Go to Next Thread

`CmdShift]`

Go to Previous Thread

`CmdShift[`

##### Shortcuts for macOS and Cursor

CommandShortcutNew Thread

`CmdOptionJ`

Focus/Hide Amp Sidebar

`CmdOptionU`

Switch to Thread

`CmdK`

Go to Next Thread

`CmdShift]`

Go to Previous Thread

`CmdShift[`

##### Shortcuts for macOS and Windsurf

CommandShortcutNew Thread

`CmdOptionJ`

Focus/Hide Amp Sidebar

`CmdOptionU`

Switch to Thread

`CmdK`

Go to Next Thread

`CmdShift]`

Go to Previous Thread

`CmdShift[`

##### Shortcuts for macOS and Antigravity

CommandShortcutNew Thread

`CmdOptionJ`

Focus/Hide Amp Sidebar

`CmdOptionU`

Switch to Thread

`CmdK`

Go to Next Thread

`CmdShift]`

Go to Previous Thread

`CmdShift[`

##### Shortcuts for Windows and VS Code

CommandShortcutNew Thread

`CtrlL`

Focus/Hide Amp Sidebar

`CtrlI`

Switch to Thread

`CtrlK`

Go to Next Thread

`CtrlShift]`

Go to Previous Thread

`CtrlShift[`

##### Shortcuts for Windows and Cursor

CommandShortcutNew Thread

`CtrlAltJ`

Focus/Hide Amp Sidebar

`CtrlAltU`

Switch to Thread

`CtrlK`

Go to Next Thread

`CtrlShift]`

Go to Previous Thread

`CtrlShift[`

##### Shortcuts for Windows and Windsurf

CommandShortcutNew Thread

`CtrlAltJ`

Focus/Hide Amp Sidebar

`CtrlAltU`

Switch to Thread

`CtrlK`

Go to Next Thread

`CtrlShift]`

Go to Previous Thread

`CtrlShift[`

##### Shortcuts for Windows and Antigravity

CommandShortcutNew Thread

`CtrlAltJ`

Focus/Hide Amp Sidebar

`CtrlAltU`

Switch to Thread

`CtrlK`

Go to Next Thread

`CtrlShift]`

Go to Previous Thread

`CtrlShift[`

##### Shortcuts for Linux and VS Code

CommandShortcutNew Thread

`CtrlL`

Focus/Hide Amp Sidebar

`CtrlI`

Switch to Thread

`CtrlK`

Go to Next Thread

`CtrlShift]`

Go to Previous Thread

`CtrlShift[`

##### Shortcuts for Linux and Cursor

CommandShortcutNew Thread

`CtrlAltJ`

Focus/Hide Amp Sidebar

`CtrlAltU`

Switch to Thread

`CtrlK`

Go to Next Thread

`CtrlShift]`

Go to Previous Thread

`CtrlShift[`

##### Shortcuts for Linux and Windsurf

CommandShortcutNew Thread

`CtrlAltJ`

Focus/Hide Amp Sidebar

`CtrlAltU`

Switch to Thread

`CtrlK`

Go to Next Thread

`CtrlShift]`

Go to Previous Thread

`CtrlShift[`

##### Shortcuts for Linux and Antigravity

CommandShortcutNew Thread

`CtrlAltJ`

Focus/Hide Amp Sidebar

`CtrlAltU`

Switch to Thread

`CtrlK`

Go to Next Thread

`CtrlShift]`

Go to Previous Thread

`CtrlShift[`

Amp runs tools and shell commands on your behalf to inspect code, run tests, and iterate quickly.

To keep that workflow fast, Amp ships with **built-in permission rules** that allow common development commands (`ls`, `git status`, `npm test`, `cargo build`, and many others) to run **without prompting**. Commands that look destructive or sensitive, like `git push` or `rm -rf`, will ask for confirmation first.

You can see exactly what’s allowed by default:

```
$ amp permissions list --builtin
```

These defaults can be overridden with your own rules. See [Permissions](#permissions) for details.

Amp acts on content in your workspace. Untrusted repositories, MCP servers, and other external inputs can influence what Amp does, including running commands on the built-in allow list. If you regularly work with untrusted sources, consider tightening your [permissions](#permissions) or using an isolated development environment.

### Built-in Tools[#](#built-in-tools)[#](#built-in-tools)

You can see Amp’s builtin tools by running `amp tools list` in the CLI or in the extension’s settings panel.

### Toolboxes[#](#toolboxes)[#](#toolboxes)

Toolboxes allow you to extend Amp with simple scripts instead of needing to provide an MCP server.

When Amp starts it invokes each executable in the directory indicated by `AMP_TOOLBOX`, with the environment variable `TOOLBOX_ACTION` set to `describe`.

The tool is expected to write its description to `stdout` as a list of key-value pairs, one per line.

```
#!/usr/bin/env bun

const action = process.env.TOOLBOX_ACTION

if (action === 'describe') showDescription()
else if (action === 'execute') runTests()

function showDescription() {
	process.stdout.write(
		[
			'name: run-tests',
			'description: use this tool instead of Bash to run tests in a workspace',
			'dir: string the workspace directory',
		].join('\n'),
	)
}
```

When Amp decides to use your tool it runs the executable again, setting `TOOLBOX_ACTION` to `execute`.

The tool receives parameters in the same format on `stdin` and then performs its work:

```
function runTests() {
	let dir = require('fs')
		.readFileSync(0, 'utf-8')
		.split('\n')
		.filter((line) => line.startsWith('dir: '))

	dir = dir.length > 0 ? dir[0].replace('dir: ', '') : '.'

	require('child_process').spawnSync('pnpm', ['-C', dir, 'run', 'test', '--no-color', '--run'], {
		stdio: 'inherit',
	})
}
```

If your tool needs object or array parameters, the executable can write its [tool schema](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#tool) as JSON instead to `stdout`. In this case it’ll also receive inputs as JSON.

We recommend using tools to express specific, deterministic and project-local behavior, like:

- querying a development database,
- running test and build actions in the project,
- exposing CLIs tools in a controlled manner.

See the [Appendix](https://ampcode.com/manual/appendix#toolboxes-reference) for the full technical reference.

### Agent Skills[#](#agent-skills)[#](#agent-skills)

Skills are packages of instructions and resources that teach the agent how to perform specific tasks. Amp includes built-in skills, and you can install or create your own—either project-specific (`.agents/skills/`) or user-wide (`~/.config/agents/skills/`).

#### Creating Skills[#](#creating-skills)[#](#creating-skills)

Amp has a built-in `building-skills` skill that can create skills tailored to your codebase, workflow, and systems. To create one, just ask:

```
Create a skill for deploying to staging
```

Ask for a “project-specific skill” to save it to the current project, or a “user-wide skill” for personal use across all your projects. Project skills live in `.agents/skills/` and can be committed to git so your team gets them automatically.

Skill precedence (first wins):

- `~/.config/agents/skills/`
- `~/.config/amp/skills/`
- `.agents/skills/`
- `.claude/skills/`
- `~/.claude/skills/`
- Plugins, toolbox directories, and built-in skills

#### Installing Skills[#](#installing-skills)[#](#installing-skills)

You can find and share skills on GitHub, internal repos, or anywhere with a git URL. To install a skill, use the command palette (`Ctrl+O` in CLI, `Cmd+Shift+P` in VS Code):

- **skill: add** — Install from GitHub, git URL, or local path
- **skill: list** — View installed skills
- **skill: remove** — Remove a skill

You can also use `amp skill` from the command line to manage skills, e.g. adding [tmux](https://github.com/ampcode/amp-contrib/blob/main/.agents/skills/tmux/skill.md) from [amp-contrib](https://github.com/ampcode/amp-contrib):

```
amp skill add ampcode/amp-contrib/tmux
```

#### Skill Format[#](#skill-format)[#](#skill-format)

Each skill is a directory containing a `SKILL.md` file with YAML frontmatter:

```
---
name: my-skill
description: A description of what this skill does
---

# My Skill Instructions

Detailed instructions for the agent...
```

The `name` and `description` are always visible to the model and determine when it invokes the skill. Names must be unique—project-specific skills take priority over user-wide, and both override built-in skills. The rest of the `SKILL.md` content is only loaded on demand when the skill is invoked.

Skills can include bundled resources (scripts, templates, etc.) in the same directory, which the agent can access relative to the skill file.

#### MCP Servers in Skills[#](#mcp-servers-in-skills)[#](#mcp-servers-in-skills)

Skills can bundle MCP servers by including an `mcp.json` file in the skill directory. The servers start when Amp launches, but their tools remain hidden until the skill is loaded. This is the recommended way to use MCP servers—it keeps the tool list clean and reduces context bloat compared to adding servers directly to your Amp configuration.

**Example `mcp.json` (local command-based server):**

```
{
	"chrome-devtools": {
		"command": "npx",
		"args": ["-y", "chrome-devtools-mcp@latest"],
		"includeTools": ["navigate_*", "take_screenshot", "click", "fill*"]
	}
}
```

**Example `mcp.json` (remote HTTP server):**

```
{
	"linear": {
		"url": "https://mcp.linear.app/sse",
		"includeTools": ["list_issues", "create_issue", "update_issue"]
	}
}
```

**Fields for local servers:**

- `command` (`string`) — the command to run
- `args` (`string[]`, optional) — command arguments
- `env` (`object`, optional) — environment variables

**Fields for remote servers:**

- `url` (`string`) — the server endpoint
- `headers` (`object`, optional) — HTTP headers to send with requests

**Common fields:**

- `includeTools` (`string[]`, optional but recommended) — tool names or glob patterns to filter which tools are exposed

### Subagents[#](#subagents)[#](#subagents)

Amp can spawn subagents (via the Task tool) for complex tasks that benefit from independent execution. Each subagent has its own context window and access to tools like file editing and terminal commands.

Subagents are most useful for multi-step tasks that can be broken into independent parts, operations producing extensive output not needed after completion, parallel work across different code areas, and keeping the main thread’s context clean while coordinating complex work.

However, subagents work in isolation — they can’t communicate with each other, you can’t guide them mid-task, they start fresh without your conversation’s accumulated context, and the main agent only receives their final summary rather than monitoring their step-by-step work.

Amp may use subagents automatically for suitable tasks, or you can encourage their use by mentioning subagents or suggesting parallel work.

### Oracle[#](#oracle)[#](#oracle)

Amp has access to a powerful “second opinion” model that’s better suited for complex reasoning or analysis tasks, at the cost of being slightly slower, slightly more expensive, and less suited to day-to-day code editing tasks than the main agent’s model.

This model is available to Amp’s main agent through a tool called `oracle`, and it currently uses GPT-5.2, with reasoning level medium (which we’ve found to work well without taking an inordinate amount of time).

The main agent can autonomously decide to ask the oracle for help when debugging or reviewing a complex piece of code. We intentionally do not force the main agent to *always* use the oracle, due to higher costs and slower inference speed.

We recommend explicitly asking Amp’s main agent to use the oracle when you think it will be helpful. Here are some examples from our own usage of Amp:

- “Use the oracle to review the last commit’s changes. I want to make sure that the actual logic for when an idle or requires-user-input notification sound plays has not changed.”
- “Ask the oracle whether there isn’t a better solution.”
- “I have a bug in these files: … It shows up when I run this command: … Help me fix this bug. Use the oracle as much as possible, since it’s smart.”
- “Analyze how the functions `foobar` and `barfoo` are used. Then I want you to work a lot with the oracle to figure out how we can refactor the duplication between them while keeping changes backwards compatible.”

See [the GPT-5 oracle announcement](https://ampcode.com/news/gpt-5-oracle) for more information.

### Librarian[#](#librarian)[#](#librarian)

Amp can search remote codebases with the use of the Librarian subagent. The Librarian can search and read all public code on GitHub as well as your private GitHub repositories, and can also connect to Bitbucket Enterprise instances.

Tell Amp to summon the Librarian when you need to do cross-repository research, or, for example, when you want it to read the code of the frameworks and libraries you’re using. The Librarian’s answers are typically longer and more detailed as we built it to provide in-depth explanations. The Librarian will only search code on the default branch of the repository.

You might need to prompt the main agent explicitly to use the Librarian. Here are some examples:

- “Explain how new versions of our documentation are deployed when we release. Search our docs and infra repositories to see how they get to X.Y.sourcegraph.com.”
- “I have a bug in this validation code using Zod, it’s throwing a weird error. Ask the Librarian to investigate why the error is happening and show me the logic causing it.”
- “Use the Librarian to investigate the `foo` service - were there any recent changes to the API endpoints I am using in `bar`? If so, what are they and when were they merged?”

See [the Librarian announcement](https://ampcode.com/news/librarian) for more information.

#### GitHub[#](#github)[#](#github)

You need to configure a connection to GitHub in [your settings](https://ampcode.com/settings#code-host-connections) to use it. If you want the Librarian to be able to see your private repositories, you need to select them when configuring your GitHub connection. See GitHub’s documentation on [installing](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party) and [authorizing](https://docs.github.com/en/apps/using-github-apps/authorizing-github-apps) GitHub apps for more information.

#### Bitbucket Enterprise[#](#bitbucket-enterprise)[#](#bitbucket-enterprise)

The Librarian can also search and read code on Bitbucket Enterprise (Bitbucket Data Center / Server) instances. To set it up, add your connection to your [configuration file](#configuration):

```
"amp.bitbucket.enterprise.connections": [
  {
    "instanceUrl": "https://bitbucket.your-company.com",
    "accessToken": "YOUR_PERSONAL_ACCESS_TOKEN"
  }
]
```

To create a Personal Access Token, go to your Bitbucket Enterprise instance → **Account** → **HTTP access tokens** → **Create a token** with **Repository read** permissions.

In VS Code, you can also configure this via the `amp.bitbucket.enterprise.connections` setting.

### Painter[#](#painter)[#](#painter)

Amp can generate and edit images using the Painter tool, powered by Gemini 3 Pro Image.

Tell Amp to use the Painter when you need to create UI mockups, app icons, hero images, or edit existing images such as redacting sensitive information from screenshots. You can also provide up to 3 reference images for style guidance or editing by @-mentioning image files in your prompt.

You might need to prompt the Amp explicitly to use the Painter. Here are some examples:

- “Use the painter to create a UI mockup for my settings page.”
- “Use the painter to generate an app icon for my CLI tool. Dark background with a glowing terminal cursor in cyan.”
- “Use the painter to redact any visible API keys or passwords in this terminal screenshot.”

See [the Painter announcement](https://ampcode.com/news/painter) for more information.

### Code Review[#](#code-review)[#](#code-review)

Amp can review your code for bugs, security issues, performance problems, and style violations—run `amp review` in the CLI or simply ask the main agent to review your changes.

#### Checks[#](#checks)[#](#checks)

Checks are user-defined review criteria scoped to specific parts of your codebase. They let you codify team conventions, security invariants, and best practices that linters don’t catch. During code review, Amp spawns a separate subagent for each check.

Create Markdown files in `.agents/checks/` directories with YAML frontmatter:

FieldRequiredDescription`name`YesIdentifier for the check`description`NoBrief explanation shown when listing checks`severity-default`NoDefault severity: `low`, `medium`, `high`, or `critical``tools`NoArray of tool names the check subagent can use

**Example** (`.agents/checks/perf.md`):

```
---
name: performance
description: Flags common performance anti-patterns
severity-default: medium
tools: [Grep, Read]
---

Look for these patterns:

- Nested loops over the same collection (O(n²) → O(n) with a Set/Map)
- Repeated `array.includes()` in a loop
- Sorting inside a loop
- String concatenation in a loop (use array + join)

Report the line, why it matters, and how to fix it.
```

Checks apply to files in and below the directory containing `.agents/`:

- `.agents/checks/` — applies to entire codebase
- `api/.agents/checks/` — applies only to files under `api/`

Closer checks override same-named checks from parent directories.

### MCP[#](#mcp)[#](#mcp)

You can add additional tools using [MCP (Model Context Protocol)](https://modelcontextprotocol.io) servers, which can be either local or remote.

For most use cases, we recommend [bundling MCP servers in skills](#agent-skills) via `mcp.json` instead of adding them to your user settings. This keeps the tool list clean and loads MCP tools only when needed.

If loading the MCP via skills isn’t suitable (if it must be always available in the context window), add it via the CLI or + Add MCP Server in VS Code settings:

```
$ amp mcp add context7 -- npx -y @upstash/context7-mcp
$ amp mcp add linear https://mcp.linear.app/sse
```

MCP servers use the same configuration fields as [MCP servers in skills](#agent-skills)—`command`/`args`/`env` for local servers, `url`/`headers` for remote. You can also configure `amp.mcpServers` directly in your [configuration file](#configuration), using `${VAR_NAME}` syntax for environment variables:

```
"amp.mcpServers": {
    "playwright": {
        "command": "npx",
        "args": ["-y", "@playwright/mcp@latest", "--headless"]
    },
    "linear": {
        "url": "https://mcp.linear.app/sse"
    },
    "sourcegraph": {
        "url": "${SRC_ENDPOINT}/.api/mcp/v1",
        "headers": { "Authorization": "token ${SRC_ACCESS_TOKEN}" }
    }
}
```

Many remote servers handle authentication automatically via [OAuth](#mcp-oauth). For servers requiring manual auth, pass headers directly or use [manual OAuth registration](#mcp-oauth).

#### MCP Server Loading Order[#](#mcp-loading-order)[#](#mcp-loading-order)

When the same MCP server name appears in multiple places, Amp uses this precedence (highest to lowest):

1. CLI flags (`--mcp-config`)
2. User/workspace config (`amp.mcpServers`)
3. Skills (only loaded if not already configured above)

This means you can override skill-provided MCP servers with your own configuration if needed.

#### Workspace MCP Server Trust[#](#mcp-trust)[#](#mcp-trust)

MCP servers in workspace settings (`.amp/settings.json`) require explicit approval before they can run. This prevents untrusted code from executing automatically when you open a project.

When a workspace MCP server is awaiting approval, you’ll see `awaiting approval` in `amp mcp doctor` output. To approve:

```
$ amp mcp approve my-server
```

In VS Code or the TUI, you’ll be prompted to approve workspace servers when they’re first detected.

MCP servers in your global settings (`~/.config/amp/settings.json`) or passed via `--mcp-config` do not require approval.

#### MCP Best Practices[#](#mcp-best-practices)[#](#mcp-best-practices)

Too many available tools can reduce model performance, so for best results, be selective:

- [Bundle MCP servers in skills](#agent-skills) instead of adding them globally—tools stay hidden until the skill loads.
- Use MCP servers that expose a small number of high-level tools with high-quality descriptions.
- Disable MCP tools you aren’t using, or consider using CLI tools instead.

#### OAuth for Remote MCP Servers[#](#mcp-oauth)[#](#mcp-oauth)

Some MCP servers like [Linear](https://linear.app/changelog/2025-05-01-mcp) support automatic OAuth client registration. When you add such a server, Amp will automatically start the OAuth flow in your browser upon startup.

**Manual OAuth Client Registration**

For servers that require manual OAuth client configuration:

1. Create an OAuth client in the server’s admin interface with:
   
   - Redirect URI: `http://localhost:8976/oauth/callback`
   - Required scopes for your use case
2. Add the MCP server to your configuration:

```
$ amp mcp add my-server https://example.com/.api/mcp/v1
```

3. Register your OAuth credentials:

```
$ amp mcp oauth login my-server \
  --server-url https://example.com/.api/mcp/v1 \
  --client-id your-client-id \
  --client-secret your-client-secret \
  --scopes "openid,profile,email,user:all"
```

Upon startup, Amp will open your browser to complete the authentication flow.

OAuth tokens are stored securely in `~/.amp/oauth/` and are automatically refreshed when needed.

### Permissions[#](#permissions)[#](#permissions)

Before invoking a tool, Amp checks the user’s list of permissions for the first matching entry to decide whether to run the tool.

If no match is found, Amp scans through its built-in permission list, rejecting the tool use in case no match is found there either.

The matched entry tells Amp to either *allow* the tool use without asking, *reject* the tool use outright, *ask* the operator, or *delegate* the decision to another program.

Permissions are configured in your [configuration file](#configuration) under the entry `amp.permissions`:

```
"amp.permissions": [
  // Ask before running command line containing git commit
  { "tool": "Bash", "matches": { "cmd": "*git commit*" }, "action": "ask"},
  // Reject command line containing python or python3
  { "tool": "Bash", "matches": { "cmd": ["*python *", "*python3 *"] }, "action": "reject"},
  // Allow all playwright MCP tools
  { "tool": "mcp__playwright_*", "action": "allow"},
  // Ask before running any other MCP tool
  { "tool": "mcp__*", "action": "ask"},
  // Delegate everything else to a permission helper (must be on $PATH)
  { "tool": "*", "action": "delegate", "to": "my-permission-helper"}
]
```

#### Using Permissions in VS Code[#](#permissions-vscode)[#](#permissions-vscode)

Complex objects must be configured in VS Code’s Settings JSON.

A JSON schema for permissions is integrated into VS Code to offer guidance when editing permissions.

Rules with action `ask` show a confirmation dialog in VS Code before the tool runs.

#### Using Permissions in the CLI[#](#permissions-cli)[#](#permissions-cli)

Using `amp permissions edit` you can edit your permissions rules programmatically and interactively using `$EDITOR`.

The `amp permissions test` command evaluates permission rules without actually running any tools, providing a safe way for verifying that your rules work as intended.

```
$ amp permissions edit <<'EOF'
allow Bash --cmd 'git status' --cmd 'git diff*'
ask Bash --cmd '*'
EOF
$ amp permission test Bash --cmd 'git diff --name-only'
tool: Bash
arguments: {"cmd":"git diff --name-only"}
action: allow
matched-rule: 0
source: user
$ amp permission test Bash --cmd 'git push'
tool: Bash
arguments: {"cmd":"push"}
action: ask
matched-rule: 1
source: user
```

Running `amp permissions list` displays known permissions rules in the same format understood by `amp permissions edit`:

```
$ amp permissions list
allow Bash --cmd 'git status' --cmd 'git diff*'
ask Bash --cmd '*'
```

Refer to the output of `amp permissions --help` for the full set of available operations.

#### Delegating Permissions Decisions to an External Program[#](#delegating-permissions-decisions-to-an-external-program)[#](#delegating-permissions-decisions-to-an-external-program)

For full control, you can tell Amp to consult another program before invoking a tool:

```
{ "action": "delegate", "to": "amp-permission-helper", "tool": "Bash" }
```

Now every time Amp wants to run a shell command, it will invoke `amp-permission-helper`:

```
#!/usr/bin/env python3
import json, sys, os

tool_name = os.environ.get("AGENT_TOOL_NAME")
tool_arguments = json.loads(sys.stdin.read())

# allow all other tools
if tool_name != "Bash":
    sys.exit(0)

# reject git push outright - stderr is passed to the model
if 'git push' in tool_arguments.get('cmd', ''):
    print("Output the correct command line for pushing changes instead", file=sys.stderr)
    sys.exit(2)

# ask in any other case
sys.exit(1)
```

The error code and stderr are used to tell Amp how to proceed.

See the [Appendix](https://ampcode.com/manual/appendix#permissions-reference) for the full technical reference.

## Thread Sharing[#](#thread-sharing)[#](#thread-sharing)

Threads are conversations with the agent, containing all your messages, context, and tool calls. Your threads are visible at [ampcode.com/threads](https://ampcode.com/threads).

We find it useful to include Amp thread links in code reviews to give the reviewer more context. Reading and searching your team’s threads can also help you see what’s going on and how other people are using Amp.

To change who you’re sharing a thread with:

- In the CLI, type `/` for the command palette, then select `thread: set visibility`.
- In the editor extension or on the web, use the sharing menu at the top.

A thread’s visibility level can be set to:

- Public: visible to anyone on your public profile (`ampcode.com/@your-username`), and publicly searchable
- Unlisted: visible to anyone on the internet with the link, and shared with your workspace
- Workspace-shared: visible to all members of your workspace
- Group-shared: visible to members of specific groups you choose; Enterprise workspaces only
- Private: visible only to you

If you are not in a workspace, your threads are only visible to you by default.

If you’re in a workspace, your threads are shared by default with your workspace members. [Enterprise](#enterprise) workspaces can configure additional sharing controls; see [Workspace Thread Visibility Controls](https://ampcode.com/manual/appendix#workspace-thread-visibility-controls).

## CLI[#](#cli)[#](#cli)

After [installing](#getting-started-command-line-interface) and signing in, run `amp` to start the Amp CLI.

Without any arguments, it runs in interactive mode:

```
$ amp
```

If you pipe input to the CLI, it uses the input as the first user message in interactive mode:

```
$ echo "commit all my changes" | amp
```

Use `-x` or `--execute` to start the CLI in execute mode. In this mode, it sends the message provided to `-x` to the agent, waits until the agent ended its turn, prints its final message, and exits:

```
$ amp -x "what files in this folder are markdown files? Print only the filenames."
README.md
AGENTS.md
```

(Note: Execute mode (`amp -x`) consumes paid credits only, not [ad-supported free-tier](https://ampcode.com/free) credits, because we can’t display ads in programmatic or non-interactive contexts.)

You can also pipe input when using `-x`:

```
$ echo "what package manager is used here?" | amp -x
cargo
```

If you want to use `-x` with the agent using tools that might require approval, make sure to either use `--dangerously-allow-all` or [configure Amp to allow them](#permissions):

```
$ amp --dangerously-allow-all -x "Run `sed` to replace 2024 with 2025 in README."
Done. Replaced 8 occurrences of 2024 in README.md
```

Execute mode is automatically turned on when you redirect stdout:

```
$ echo "what is 2+2?" | amp > response.txt
```

When you pipe input and provide a prompt with `-x`, the agent can see both:

````
$ cat ~/.vimrc | amp -x "which colorscheme is used?"
The colorscheme used is **gruvbox** with dark background and hard contrast.

```vim
set background=dark
let g:gruvbox_contrast_dark = "hard"
colorscheme gruvbox
```
````

You can use the `--mcp-config` flag with `-x` commands to specify an MCP server without modifying your configuration file.

```
$ amp --mcp-config '{"everything": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-everything"]}}' -x "What tools are available to you?"
```

To see more of what the CLI can do, run `amp --help`.

### Keybindings[#](#cli-keybindings)[#](#cli-keybindings)

The most important keybinding is `Ctrl+O` to open the command palette. Other keybindings worth remembering:

- `Ctrl+G` to open the current prompt in your editor (requires \`$EDITOR\`)
- `Ctrl+S` to switch agent modes
- `Ctrl+R` for prompt history
- `↑`/`↓` to move to previous messages and edit them
- `Alt+T` to expand thinking/tool blocks
- `Alt+D` to toggle deep reasoning effort (deep, deep², deep³)
- `@` to mention files

Use `Ctrl+O` to open the command palette and run `amp: help` to see more keybindings.

### Non-Interactive Environments[#](#cli-non-interactive-environments)[#](#cli-non-interactive-environments)

For non-interactive environments (e.g. scripts, CI/CD pipelines), set your [access token](https://ampcode.com/settings) in an environment variable:

```
export AMP_API_KEY=your-access-token-here
```

### CLI–IDE Integration[#](#cli-editor-integration)[#](#cli-editor-integration)

The Amp CLI integrates with VS Code, JetBrains, and Neovim (see [ampcode.com/install](https://ampcode.com/install) to install), which lets the Amp CLI:

- Read diagnostics, such as typechecker and linter errors
- See the current open file and selection, so Amp can understand the context of your prompt better
- Edit files through your IDE, with full undo support

The CLI automatically detects when you have an Amp editor extension running in most cases. If you are using JetBrains and run the Amp CLI from a terminal *other than* JetBrains’ builtin terminal, you need to run `amp --jetbrains` to detect it.

### Shell Mode[#](#cli-shell-mode)[#](#cli-shell-mode)

Execute shell commands directly in the CLI by starting your message with `$`. The command and its output will be included in the context window for the next message to the agent.

Use `$$` to activate incognito shell mode, where commands execute but aren’t included in the context. This is useful for noisy commands or quick checks you’d normally run in a separate terminal.

### Writing Prompts in the CLI[#](#cli-writing-prompts)[#](#cli-writing-prompts)

In modern terminal emulators, such as Ghostty, Wezterm, Kitty, or iTerm2, you can use `shift-enter` to insert a newline in your prompts.

Additionally you can also use type `\` followed by `return` to insert a newline.

If you have the environment variable `$EDITOR` set, you can use the `editor` command from the command palette to open your editor to write a prompt.

### Streaming JSON[#](#cli-streaming-json)[#](#cli-streaming-json)

Amp’s CLI supports streaming JSON output format, one object per line on stdout, for programmatic integration and real-time conversation monitoring.

Use the `--stream-json` flag with `--execute` mode to output in stream JSON format instead of plain text. If you want assistant thinking blocks in the JSON output, add `--stream-json-thinking` (this extends the schema and is not Claude Code compatible).

Basic usage with argument:

```
$ amp --execute "what is 3 + 5?" --stream-json
```

Combining —stream-json with `amp threads continue`:

```
$ amp threads continue --execute "now add 8 to that" --stream-json
```

With stdin input:

```
$ echo "analyze this code" | amp --execute --stream-json
```

You can find [the schema for the JSON output in the Appendix](https://ampcode.com/manual/appendix?preview#message-schema).

Input can be also be provided on stdin with the `--stream-json-input` flag:

```
$ echo '{
  "type": "user",
  "message": {
    "role": "user",
    "content": [
      {
        "type": "text",
        "text": "what is 2+2?"
      }
    ]
  }
}' | amp -x --stream-json --stream-json-input
```

The `--stream-json` flag requires `--execute` mode. It cannot be used standalone. `--stream-json-input` requires `--stream-json`, and `--stream-json-thinking` implies `--stream-json`.

When using `--stream-json-input`, the behavior of `--execute` changes in that Amp will only exit once both the assistant is done *and* stdin has been closed.

This allows for programmatic use of the Amp CLI to have conversations with multiple user messages.

```
#!/usr/bin/env bash

send_message() {
  local text="$1"
  echo '{"type":"user","message":{"role":"user","content":[{"type":"text","text":"'$text'"}]}}'
}

{
  send_message "what's 2+2?"
  sleep 10

  send_message "now add 8 to that"
  sleep 10

  send_message "now add 5 to that"
} | amp --execute --stream-json --stream-json-input
```

See the [Appendix](https://ampcode.com/manual/appendix#stream-json-output) for the schema of the output, example output, and more usage examples.

### Themes[#](#cli-themes)[#](#cli-themes)

The Amp CLI ships with several built-in themes:

- `terminal`, default, uses your terminal colors and preserves transparency
- `dark`
- `light`
- `catppuccin-mocha`
- `solarized-dark`
- `solarized-light`
- `gruvbox-dark-hard`
- `nord`

You can switch themes using the command palette (`Ctrl+O`) and selecting `theme: switch`.

You can also set the theme in your settings:

```
{
  "amp.terminal.theme": "catppuccin-mocha"
}
```

#### Creating Custom Themes[#](#creating-custom-themes)[#](#creating-custom-themes)

Create a custom theme by adding a `colors.toml` file in `~/.config/amp/themes/<name>/`:

```
~/.config/amp/themes/
└── my-theme/
    └── colors.toml
```

**Minimal theme (6 required colors):**

```
name = "My Theme"

[colors]
background = "#1e1e2e"
foreground = "#cdd6f4"
primary = "#89b4fa"
success = "#a6e3a1"
warning = "#f9e2af"
destructive = "#f38ba8"
```

All other colors are derived automatically. Dark/light mode is detected from background luminance.

**Transparent background:**

To preserve your terminal’s transparency (for terminals with background images or blur effects), use `"none"` as the background color:

```
name = "My Transparent Theme"

[colors]
background = "none"
foreground = "#cdd6f4"
primary = "#89b4fa"
success = "#a6e3a1"
warning = "#f9e2af"
destructive = "#f38ba8"
```

The built-in `terminal` theme uses a transparent background by default.

**Full theme (all options):**

```
name = "My Theme"
mode = "dark"  # optional - auto-detected from background

[colors]
background = "#1e1e2e"
foreground = "#cdd6f4"
primary = "#89b4fa"
secondary = "#74c7ec"
accent = "#f5c2e7"
success = "#a6e3a1"
warning = "#f9e2af"
info = "#89b4fa"
destructive = "#f38ba8"

[ui]
cursor = "#cdd6f4"
border = "#6c7086"
selection = "#585b70"
muted_foreground = "#a6adc8"

[syntax]
keyword = "#cba6f7"
string = "#a6e3a1"
number = "#fab387"
comment = "#7f849c"
function = "#89b4fa"
variable = "#cdd6f4"
type = "#f9e2af"
operator = "#94e2d5"
```

Custom themes appear in the theme switcher alongside built-in themes.

## Configuration[#](#configuration)[#](#configuration)

Amp can be configured through settings in your editor extension (e.g. `.vscode/settings.json`) and the CLI configuration file.

The CLI configuration file location varies by operating system:

- macOS: `~/.config/amp/settings.json`
- Linux: `~/.config/amp/settings.json`
- Windows: `%USERPROFILE%\.config\amp\settings.json`

All settings use the `amp.` prefix.

### Settings[#](#core-settings)[#](#core-settings)

#### Editor Extension and CLI[#](#editor-extension-and-cli)[#](#editor-extension-and-cli)

- **`amp.anthropic.thinking.enabled`**
  
  **Type:** `boolean`, **Default:** `true`
  
  Enable Claude’s extended thinking capabilities
- **`amp.experimental.compaction`**
  
  **Type:** `boolean` or `number`, **Default:** `false`
  
  Enable auto-compaction when the context window is nearly full. When triggered, Amp creates a new thread with a summary of older messages plus recent messages, then navigates to the new thread. The old thread is preserved for history access. Set to `true` for 90% threshold, or a number 0-100 for a custom percentage threshold.
- **`amp.fuzzy.alwaysIncludePaths`**
  
  **Type:** `array`, **Default:** `[]`
  
  Glob patterns for paths that should always be included in fuzzy file search, even if they are gitignored. Useful for build output directories or generated files you want to reference with `@` mentions.
  
  Examples: `["dist/**", "node_modules/@myorg/**"]`
- **`amp.permissions`**
  
  **Type:** `array`, **Default:** `[]`
  
  Configures which tool uses are allowed, rejected or ask for approval. See [Permissions](#permissions).
- **`amp.showCosts`**
  
  **Type:** `boolean`, **Default:** `true`
  
  Show cost information for threads in the CLI and editor extension while working. Workspace admins can also hide costs for all workspace members in [workspace settings](https://ampcode.com/workspace).
- **`amp.git.commit.ampThread.enabled`**
  
  **Type:** `boolean`, **Default:** `true`
  
  Enable adding Amp-Thread trailer in git commits. When disabled, commits made with the commit tool will not include the `Amp-Thread: <thread-url>` trailer.
- **`amp.git.commit.coauthor.enabled`**
  
  **Type:** `boolean`, **Default:** `true`
  
  Enable adding Amp as co-author in git commits. When disabled, commits made with the commit tool will not include the `Co-authored-by: Amp <amp@ampcode.com>` trailer.
- **`amp.mcpServers`**
  
  **Type:** `object`
  
  Model Context Protocol servers that expose tools. See [Custom Tools (MCP) documentation](#mcp).
- **`amp.bitbucket.enterprise.connections`**
  
  **Type:** `array`, **Default:** `[]`
  
  Local Bitbucket Enterprise connections used by librarian tools. Each entry is an object with:
  
  - `instanceUrl` (string)
  - `accessToken` (string)
- **`amp.notifications.enabled`**
  
  **Type:** `boolean`, **Default:** `true`
  
  Play notification sounds when the agent completes a task or is blocked waiting for user input.
- **`amp.skills.path`**
  
  **Type:** `string`
  
  Path to additional directories containing skills. Supports colon-separated paths (semicolon on Windows). Use `~` for home directory. Example: `~/my-skills:/shared/team-skills`
- **`amp.terminal.commands.nodeSpawn.loadProfile`**
  
  **Type:** `string`, **Default:** `"always"`, **Options:** `"always"` | `"never"` | `"daily"`
  
  Before running commands (including MCP servers), whether to load environment variables from the user’s profile (`.bashrc`, `.zshrc`, `.envrc`) as visible from the workspace root directory
- **`amp.tools.disable`**
  
  **Type:** `array`, **Default:** `[]`
  
  Disable specific tools by name. Use ‘builtin:toolname’ to disable only the builtin tool with that name (allowing an MCP server to provide a tool by that name). Glob patterns using `*` are supported.
- **`amp.tools.stopTimeout`**
  
  **Type:** `number`, **Default:** `300`
  
  How many seconds to wait before canceling a running tool
- **`amp.mcpPermissions`**
  
  **Type:** `array`, **Default:** `[]`
  
  Allow or block MCP servers that match a designated pattern. The first rule that matches is applied. If no rule matches an MCP server, the server will be allowed.
  
  - **Remote MCP server**: Use the `url` key to specify a matching criterion for the server endpoint
  - **Local MCP server**: Use the `command` and `args` keys to match an executable command and its arguments
  
  Here are some examples:
  
  ```
  "amp.mcpPermissions": [
    // Allow specific trusted MCP servers
    { "matches": { "command": "npx", "args": "* @playwright/mcp@*" }, "action": "allow" },
    { "matches": { "url": "https://mcp.trusted.com/mcp" }, "action": "allow" },
    // Block potentially risky MCP servers
    { "matches": { "command": "python", "args": "*bad_command*" }, "action": "reject" },
    { "matches": { "url": "*/malicious.com*" }, "action": "reject" },
  ]
  ```
  
  The following rules will block all MCP servers:
  
  ```
  "amp.mcpPermissions": [
    { "matches": { "command": "*" }, "action": "reject" },
    { "matches": { "url": "*" }, "action": "reject" }
  ]
  ```
- **`amp.workerUrl`**
  
  **Type:** `string`
  
  URL to the Cloudflare Worker for agent loop operations. For local development, this defaults to `http://localhost:8787`. In production, this points to the deployed Cloudflare Workers endpoint.

#### CLI-only[#](#cli-only)[#](#cli-only)

- **`amp.updates.mode`**
  
  **Type:** `string`, **Default:** `"auto"`
  
  Control update checking behavior: `"warn"` shows update notifications, `"disabled"` turns off checking, `"auto"` automatically runs update. Note: Setting `AMP_SKIP_UPDATE_CHECK=1` environment variable will override this setting and disable all update checking.
- **`amp.internal.deepReasoningEffort`**
  
  **Type:** `string`, **Default:** `"medium"`, **Options:** `"medium"` | `"high"` | `"xhigh"`
  
  Override the default reasoning effort for GPT-5.2 Codex in `deep` mode.

### Enterprise Managed Settings[#](#enterprise-managed-policy-settings)[#](#enterprise-managed-policy-settings)

[Enterprise](#enterprise) workspace administrators can enforce settings that override user and workspace settings by deploying their policies to the following locations on machines running Amp:

- **macOS**: `/Library/Application Support/ampcode/managed-settings.json`
- **Linux**: `/etc/ampcode/managed-settings.json`
- **Windows**: `C:\ProgramData\ampcode\managed-settings.json`

This managed settings file uses the same schema as [regular settings](#core-settings) files, with one additional field:

amp.admin.compatibilityDate `string`

Date field used for determining what migrations need to be applied for settings backward compatibility. Expected format: YYYY-MM-DD (e.g., '2024-01-15').

### Proxies and Certificates[#](#proxies-and-certificates)[#](#proxies-and-certificates)

When using the Amp CLI in corporate networks with proxy servers or custom certificates, set these standard Node.js environment variables in your shell profile or CI environment as needed:

```
export HTTP_PROXY=your-proxy-url
export HTTPS_PROXY=your-proxy-url
export NODE_EXTRA_CA_CERTS=/path/to/your/certificates.pem
```

## Pricing[#](#pricing)[#](#pricing)

To check your usage and credits balance, visit [user settings](https://ampcode.com/settings), run `amp usage`, or open the settings panel in the editor extension.

### Free[#](#free)[#](#free)

Amp gives most users a $10 free daily grant for usage of all modes and models, including Opus 4.6. This is supported by ads and may change.

Your daily grant meets all of the stringent [security standards](https://ampcode.com/security) of paid usage. You are not required to share your data for training.

One account per person. Any behavior that looks like circumventing your usage limits or violating our [Acceptable Use Policy](https://ampcode.com/terms/aup) will result in your account being suspended.

### Paid Usage[#](#paid-usage)[#](#paid-usage)

After you’ve used up your daily free grant (or if you’ve disabled it or are ineligible), Amp consumes paid credits.

You can buy more credits in [user settings](https://ampcode.com/settings) for yourself, or for your team in [workspace settings](https://ampcode.com/workspace). Upon signup, most users receive $10 USD in free credits.

Usage is consumed based on LLM usage and usage of certain other tools (like web search) that cost us to serve. We pass these costs through to you directly with no markup, for individuals and non-enterprise workspaces.

Workspace credits are pooled and shared by all workspace members. All unused credits expire after one year of account inactivity.

Invoices are issued through Stripe, which supports adding your VAT ID or other tax information.

### Enterprise[#](#enterprise)[#](#enterprise)

Enterprise usage is 50% more expensive than individual and team plans, and includes access to:

- SSO (Okta, SAML, etc.) and directory sync
- Zero data retention for text inputs in LLM inference
- Advanced [thread visibility controls](https://ampcode.com/manual/appendix#workspace-thread-visibility-controls)
- [Entitlements](https://ampcode.com/manual/appendix#workspace-entitlements) for per-user cost controls
- [MCP registry allowlists](https://ampcode.com/manual/appendix#mcp-registry-allowlist)
- [Managed user settings](#enterprise-managed-policy-settings)
- APIs for workspace analytics and data management
- User groups for cost attribution and per-group thread visibility options (on request)
- Configurable thread retention (on request)
- IP allowlisting for workspace access (on request, extra charges apply)

For more information about Amp Enterprise security features, see the [Amp Security Reference](https://ampcode.com/security).

To start using Amp Enterprise, go to [your workspace](https://ampcode.com/workspace) and click **Plan** in the top right. This requires a special one-time $1,000 USD purchase, which grants your workspace $1,000 USD of Amp Enterprise usage and upgrades your workspace to Enterprise.

Contact [amp-devs@ampcode.com](mailto:amp-devs@ampcode.com) for access to these purchasing options and for general information about Amp Enterprise.

## Support[#](#support)[#](#support)

For general help with Amp, post on X and mention [@AmpCode](https://x.com/AmpCode), or email [amp-devs@ampcode.com](mailto:amp-devs@ampcode.com). You can also join our community [Build Crew](https://buildcrew.team) to discuss Amp and share tips with others.

For billing and account help, contact [amp-devs@ampcode.com](mailto:amp-devs@ampcode.com).

### Supported Platforms[#](#platforms)[#](#platforms)

Amp supports macOS, Linux, and Windows (WSL recommended).

Amp’s JetBrains integration supports all JetBrains IDEs (IntelliJ, WebStorm, GoLand, etc.) on versions 2025.1+ (2025.2.2+ is recommended).