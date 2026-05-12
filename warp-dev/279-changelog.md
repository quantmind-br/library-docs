---
title: Changelog | Warp
url: https://docs.warp.dev/changelog
source: sitemap
fetched_at: 2026-04-29T15:05:35.604597702-03:00
rendered_js: false
word_count: 21615
summary: This document lists the release notes for version 0.2026.04.22 of the Warp terminal, detailing new features, performance improvements, and bug fixes related to AI agents, MCP integration, and UI enhancements.
tags:
    - release-notes
    - terminal
    - ai-agents
    - mcp
    - software-update
    - cli-tools
category: other
optimized: true
optimized_at: 2026-04-29T18:30:00Z
---
Submit bugs and feature requests on our [GitHub board](https://github.com/warpdotdev/Warp/issues/new/choose).

## 2026.04.22 (v0.2026.04.22.08.46)

### New features
- Toolbar chips can be rearranged via right-click → "Rearrange toolbar items" in the top bar.
- Mermaid diagrams now render in markdown notebooks.

### Improvements
- Pasting images into the rich input editor works with CLI agents (Claude Code, Codex).
- Typing `_text_` or `__text__` in code review/rich-text comments renders as italic/bold, matching `*text*`/`**text**`.
- \[Windows] "Start Warp at login" toggle under **Settings** → **Features** → **General**.
- View menu entries with keyboard shortcuts for Global Search and Agent Conversations left panel items on macOS.
- \[Windows] Added 408 new PowerShell cmdlet completions; improved suggestion quality for existing PowerShell completions.
- Added completions for `pprof`.
- `/fork` opens forked conversation in a new pane (Enter) or new tab (Cmd+Enter).
- Right-click URL or file-path link inside AI response to copy directly via context menu.
- Setting to hide added/removed line counts from the code review button in the tab bar.
- Reorganized settings into subpages for Agents, Code, and Cloud platform; improved settings search.
- Wired branch completion into `git log` argument position.
- Notifications for OpenCode's "Ask user question" tool.
- Discount chip on models with active promotions in the model picker.
- Per-query image limit bumped to 20 (from 5); per-conversation image limit bumped to 200 (from 20).
- Performance improvement preventing lagginess after logging in with many Warp Drive objects.
- File artifacts in agent conversations with download functionality and filtering options.

### Bug fixes
- \[Windows] Fixed image paste into CLI coding agents (Claude Code, OpenCode, etc.).
- Fixed MCP server tags overflowing off-screen when a server has many chips (e.g. GitHub MCP with many repo scopes).
- Fixed MCP gallery items not being alphabetized consistently in MCP servers settings page.
- Fixed artifacts card clipping the "Continue locally" button on narrow panes.
- Fixed code review submit button incorrectly disabled when terminal working directory casing didn't match on-disk repo path on macOS.
- Fixed new accounts not being marked as onboarded on server when signing up after completing onboarding slides from a non-login-slide entrypoint.
- Fixed Project Explorer getting stuck in loading state when opened after connecting to a remote SSH session.
- Fixed agent's `read_files` tool returning extensionless text files as binary content.
- Fixed MCP settings page file-based server badges growing unbounded and incorrectly labelling Warp-scoped servers as ".warp" instead of "global".
- Fixed missing in-progress indicator in agent panes when a shell command is running but no agent message has been sent yet.
- Fixed MCP OAuth authentication failing with providers enforcing strict redirect URI matching (e.g. Hydra/ORY).
- Fixed MCP tool calls with integer-typed parameters failing due to serialization as floats.
- Fixed file edit tool dropping the end of a line when the LLM's search block ended with a partial line match.
- First find match now correctly selected when using the code editor with vim mode.
- Fixed code review comments being silently dropped when sent after cancelling a running agent command with Ctrl+C.
- Toolbar chips in the coding agent footer no longer hard to read when running alt-screen CLI agents like OpenCode.
- Fixed MCP servers (e.g. Figma) requiring re-authentication on every app restart.
- \[Windows] Fixed race condition causing auto-updates to fail with file-in-use errors when Warp hadn't fully exited before installer ran.
- Improved reliability of Rich Input submission flow for Copilot CLI.
- \[Windows] Fixed unbounded memory growth when rendering large amounts of CJK text with a primary font that doesn't include CJK glyphs.
- Fixed settings search bar text overflowing when typing long queries.
- Fixed Oz CLI hanging after command completes when network unavailable.
- Fixed Ctrl+C not terminating the Oz CLI during shutdown.
- Fixed `~` not being expanded to the home directory in the `/open-file` slash command.
- Fixed orchestration events breaking tool call ordering when a CLI subagent is active.

### Oz updates
- Bundled Claude API skill for Claude API and Anthropic SDK development guidance.
- Support for `--share public:{access_level}` to oz CLI for setting public access level on oz cloud runs.
- `/feedback` skill now adds `in-app-feedback` label to issues for tracking.
- `start_agent` no longer rejects remote child agents when `environment_id` is omitted; within a remote parent, child inherits parent's environment automatically.

---

## 2026.04.15 (v0.2026.04.15.08.45)

### Improvements
- Agent Mode shows "Last seen by agent at" indicator for long-running commands.
- Added completions for npm package search, nx, brew, aws s3, tree, awk, sort, ip, uv, nmap; added pnpm workspace filter support.
- Skill invocations display with the same purple highlighted text as slash commands in input and prompt views.
- Added completions for `timedatectl`, `ack`, `watch`, `lsof`, `systemctl`, `ros2`, `nextflow`, `tsh`, `codex`, `asdf`, `sdk`, `pass`, `az`, `oc`, `scp`, `claude`, `git show`, `git rm`, `gsutil`, `aws ec2`, `docker-compose`, `yarn`, `docker run`; improved `git switch`, `git diff`, `aws` static flags, `gt`, `kubectl`, `tf`, `pnpm`, `kubectl`, SSH host completions; added `apt` repo package generator.
- Code review comment buttons remain visible when AI is disabled; comments can be sent to CLI agent terminals (e.g. Claude Code).
- Review comments can be sent to any available terminal in the tab, not just the focused one.
- Skills searchable from @-context menu in Agent Mode, inserting `/{skill_name}` into prompt.
- File-based MCP servers configurable via `~/.agents/.mcp.json` (global) or `.agents/.mcp.json` (project-local).

### Bug fixes
- Fixed longer prompts for Claude Code not being fully submitted when using Rich Input in Warp.
- Fixed settings being reset to defaults when a logged-out user creates a new account.
- Updated openh264 dependency to resolve heap overflow security vulnerability (GHSA-5pmw-9j92-3c4c).
- Show "Resume Conversation" shortcut when agent conversations fail with transport or server errors.
- Fixed `kubectl` resource completion breaking when `-n`/`--namespace` or other flags placed before subcommand.
- Fixed markdown files with animated GIFs and WebPs using excessive memory by rendering as first-frame previews.
- Fixed autosuggestions and completions not appearing after shell bootstrap completes.
- Fixed excessive CPU usage from redundant `git status` processes when multiple terminal tabs open in the same repository.
- Fixed conversations stalling if a long-running command finished while user was in control.
- Fixed thought block headers having a click area extending to full width of pane; now only text and chevron are clickable.
- Fixed global search using excessive memory when matching files with very long lines.
- Window title respects custom tab names instead of always showing the generated name.
- Fixed `git push` branch completion for force-push and refspec prefixes, HTML entity rendering in completion specs, `npm i` short-form command priority.
- Fixed repeated 403 errors when indexing large codebases.
- Fixed ask-question option rows changing cursor shape while hovering over option text.

### Oz updates
- Local child agents inherit parent agent's AI profile (model and permissions).

---

## 2026.04.08 (v0.2026.04.08.08.36)

### New features
- Vertical tabs available, offering a sidebar layout for organizing terminal tabs.
- Tab configs allow saving and sharing workspace setup as customizable configurations.
- Create new worktrees with autogenerated branch names, saved as tab configs.
- New Rich Input available in third-party CLI agents (Claude Code, Codex, Gemini CLI, OpenCode, etc.).
- Revamped notifications UI; support for notifications for Claude Code and OpenCode.
- Added support for the coding agent toolbar for auggie and pie.
- Settings entry for the ask question tool to configure when it pauses for user input.

### Improvements
- Conversation search shows what it is searching for and its current activity.
- Added `warp://settings/appearance` deep link to open Appearance settings directly.
- Improved AI @context menu to prioritize blocks from active terminal session and rank items by recency.
- Added support for rendering markdown tables in notebooks and Warp's built-in Markdown viewer.
- Command palette file opener supports `~` expansion to home directory when searching for files.
- Added completions for `timedatectl`, `ack`, `watch`, `lsof`, `systemctl`, `ros2`, `nextflow`, `tsh`, `codex`, `asdf`, `sdk`, `pass`, `az`, `oc`, `scp`, `claude`, `git show`, `git rm`, `gsutil`, `aws ec2`, `docker-compose`, `yarn`, `docker run`.
- Improved dynamic completions for `git switch`, `git diff`, `gt`, `kubectl`, `tf`, `pnpm`, `apt`, SSH hosts.

### Bug fixes
- Added prompt changes to avoid agents getting stuck navigating pagers in Full Terminal Use.
- Removed web inactivity logout that could sign out authenticated users unnecessarily.
- Skip ask-user-question prompts while auto-approve is enabled in Agent Mode.
- Fixed `git push` branch completion for force-push and refspec prefixes.
- Fixed HTML entity rendering in completion specs.
- Fixed `npm i` short-form command priority.

### Oz updates
- Added `oz whoami` command to get user information.

---

## 2026.04.01 (v0.2026.04.01.08.39)

### New features
- \[macOS] Right-clicking text files in Finder allows opening in Warp's code editor.
- Send code review comments, attach diff hunks as context, send substrings as context (Cmd+L) to 3rd party CLI tools (Claude Code, Codex, Opencode, etc.).
- Oz agents can ask users clarifying questions during Agent Mode interactions.
- Warp's agent suggests followups when done.

### Improvements
- Replaced warpify banner for subshell and SSH sessions with a footer.
- Improved error messaging when session sharing times out via CLI `--share` flag.
- Added "Copy file path" option to overflow menu in file viewer for code and markdown files.
- Added "Sign up" option to settings gear menu for non-logged-in users.
- MCP config files edited by agent show an 'Open config' button in code diff header.
- Added `/skills` support in CLI agent rich input for browsing and invoking agent-specific skills.
- Sandboxed Oz agents have dedicated autonomy settings instead of inheriting team-level defaults.
- Updated settings info icon tooltips to clarify they open documentation.
- Improved quality and latency of prompt suggestions and suggested code diffs.
- Cloud agents accept images and file attachments as context.

### Bug fixes
- Fixed stale fallback model messaging persisting across new user queries.
- Fixed scroll behavior when editing code review comments.
- Fixed WebSocket proxy connections timing out when proxy listens on port 80.
- Fixed PowerShell aliases and functions matched case-insensitively.
- Fixed conversation search temp directory paths using mixed separators on Windows.
- Fixed keyboard shortcuts settings panel empty when first navigated to via search.
- Fixed `@` context menu dismissing after typing ~6 characters when filtering categories.
- Fixed crash with Oz CLI commands that read from stdin.
- Fixed production WebAssembly crash caused by native repository detection code.
- Fixed links in blocklist code review comments not opening when clicked.
- Fixed "Out of credits" alert not dismissing when users provide their own API keys.
- Fixed link detection offset in AI conversations after conversation summaries or hidden reasoning blocks.
- Simplified file explorer lazy-loaded folder handling; fixed transitions between standalone folders and indexed git repositories.
- Fixed inline code snippet colors and underline colors not updating when switching editor themes in notebooks.
- \[Windows] Fix rendering on additional set of older Intel iGPU drivers.
- Fixed web auth flows so session-cookie-authenticated clients can call authenticated server APIs without requiring Authorization header.

### Oz updates
- Fixed Oz session sharing failing behind HTTP proxies on port 80.
- `OZ_RUN_ID` environment variable now available inside agent terminal sessions, set to current task ID.
- Improved error messages when agent session sharing fails.
- Oz agents can ask users clarifying questions during Agent Mode interactions.

---

## 2026.03.25 (v0.2026.03.25.08.24)

### New features
- `/pr-comments` fetches Pull Request comments from GitHub.
- Warp supports the Kitty Keyboard Protocol.

### Improvements
- Onboarding shows premium model tiers as disabled with an upgrade path for free users.
- All inline menus are resizable; some have tabs.
- New built-in `edit-figma-design` skill for users with Figma's remote MCP server installed.
- MCP server templates can use dropdown selectors for enums.
- Customizable toolbelt for agent input footer — drag and drop to rearrange context chips and controls.
- \[macOS] Migrated to Apple's newest icon format, adapting to "Icon & Widget Style" preference.
- Code review comments can be sent directly to running CLI agents (Claude Code, Gemini CLI, etc.) from code review panel.
- Pressing `esc` dismisses an empty code review comment composer.
- Added ability to always show or always hide agent thinking blocks in **Settings** → **AI** → **Other**.
- Added `/changelog` command for reopening latest changelog; update toast stays visible until dismissed.
- Added syntax highlighting for Dockerfiles in file editor.
- Setting to hide agent-executed commands from shell history, now enabled by default.
- MCP servers detected from third-party agents (Claude, Codex) visible and spawnable from MCP servers page.

### Bug fixes
- Fixed visual jitter in agent toolbelt when opening rich input composer.
- Clarified `/fork` slash command description.
- MCP resource reads respect autonomy settings instead of always prompting for approval.
- Completions, syntax highlighting, and hover descriptions work when flag/value pairs are `=`-separated.
- Fixed stale go-to-definition and symbol outlines when using code review with multiple tabs.
- Fixed issue where selecting a shell command from command search while in Agent Mode with auto-detection disabled treated command as agent prompt.
- Fixed `ctrl-c` not working during conversation search.
- Fixed follow-up prompt in `/compact-and` and `/fork-and-compact` silently lost when summarization failed or cancelled.
- Fixed dismiss button and `ctrl-c` not working on suggested unit tests banner.
- Git diff chip appears in remote and subshell sessions.
- Fixed input scrolling bug where clicks were sometimes applied one line up.
- Fixed rendering of programs using synchronized output VT extension in shared sessions (e.g. Claude Code).

### Oz updates
- Updated `create-skill` bundled skill with latest upstream version adding eval/iteration workflow, benchmarking, description optimization.
- New chip in AI input mode for GitHub pull requests when you have a PR open for your current branch.

---

## 2026.03.18 (v0.2026.03.18.08.24)

### New features
- Warp automatically detects global and project-scoped MCP servers configured with `claude` or `codex`. Toggle **File-based MCP servers** in **Settings** → **AI** to auto-spawn servers.
- Added Go to Line dialog in code editor (`Ctrl+G`) with line:column support.

### Improvements
- Added "Leave Agent Thinking expanded" setting to keep agent thinking blocks expanded after streaming.
- Added "All" and "Current Directory" tabs to inline conversations menu.
- Updated settings copy to consistently use "Oz" instead of "the Agent" in MCP Servers and Rules sections.
- Improved performance of loading and rendering large AI conversations.
- Added inline plan selector for conversations with multiple plans.
- \[macOS] Window traffic light buttons look correct at different zoom levels.
- Kitty keyboard protocol support available on Preview builds.
- Warp agent management view links to associated skills for cloud agents.
- `Ctrl-R` command search includes AI query history from all past conversations, not just those currently open.
- Enabled Kitty keyboard protocol support on dev builds.
- Improved ranking of items listed in @ context by considering recency.
- Added new built-in skills `generate-figma-content` and `pull-figma-content` for users with Figma's remote MCP server installed.
- Hidden directories and files appear at top of Project Explorer.
- Updated setup command placeholder to show `cd my-repo &&` example.

### Bug fixes
- Fixed "for terminal" text in pane header becoming bold when disabled, causing layout shift.
- Fixed notebook find bar showing `?/n` instead of proper match counter.
- Fixed bug where editing a tab title always started with pane title.
- Fixed "View latest changelog" action not appearing in command palette.
- Fixed issue where artifacts from cloud agent runs did not update live in conversation details pane.
- Fixed intermittent "Failed to update plan" toast appearing without user action.
- Fixed tooltip for branch name in code review panel overlapping truncated text.
- Fixed `Ctrl+G` not bound by default for "Go to line" in code editor.
- Fixed `cmd-O` files palette not toggling off when pressed again.
- Fixed code review panel unnecessarily resetting scroll position and cached state when switching tabs.
- Fixed some saved prompts not appearing in slash command menu when searching with a single character.
- Fixed SSH warpification not triggering when using shell aliases for SSH commands.
- Fixed bug where SSH sessions run by agent would incorrectly trigger warpification UI.
- Fixed issue where New Window/New Tab menu items and keybindings occasionally became disabled when using global hotkey window.
- Fixed code review branch dropdown only showing "Uncommitted changes" after closing and reopening panel.
- Fixed "New environment" button in Environment settings not opening setup mode selector popup.
- Fixed onboarding slides cutting off navigation buttons when window is too short.
- \[Windows] Fixed path inconsistencies causing codebases to fail indexing.
- Show tooltip on codebase indexing toggle when disabled by admin policy.
- \[Windows] Fixed rendering issues on old Intel UHD integrated GPUs.
- Fixed bug where only first plan was shown inline when restoring a conversation with multiple plans created.
- Fixed resume-conversation keybinding not working when long-running command subagent is active.
- Fixed broken documentation links in agent tips, settings, and onboarding content.
- Fixed AI queries in `Ctrl-R` history not being sorted by time.

### Oz updates
- Conversation search uses real file tools for faster, more accurate history search.
- Added `/open-repo` slash command for switching between indexed codebases.
- Added tabs to up-arrow history menu to filter to commands or prompts.
- `oz agent run` prints run ID with link to Oz dashboard.

---

## 2026.03.11 / 2026.03.04 (v0.2026.03.04.08.20)

### Bug fixes
- Terminal input automatically detects references to Figma and encourages use of Figma MCP. Images exported from Figma are also detected.

---

## 2026.03.05 (v0.2026.03.04.08.20)

### New features
- Adds prompt customization for the new Warp prompt.

### Improvements
- Adds new built-in skills `generate-figma-content` and `pull-figma-content` for users with Figma's remote MCP server installed.
- Selected text no longer auto-attached as agent context; requires right-click → attach as agent context.
- Cloud conversations appear in @conversations context menu.
- When **Settings** → **MCP Servers** → **File-based MCP servers** is toggled on, Warp automatically detects and spawns global and project-scoped MCP servers installed via `codex`.
- Global search pre-populates with active text selection from code, terminal, notebook, and plan views.
- Warp prompt has separate chips for git branch and git diff stats.
- Show pending prompt indicator when using `/fork-and-compact` or `/compact-and` with follow-up prompt.
- Oz permission notifications now use "Oz" branding instead of "Agent Mode".
- \[macOS] Window traffic light buttons look correct at different zoom levels.
- Added "Copy plan ID" option to plan document overflow menu.

### Bug fixes
- Fixed issue where changing directories from prompt chip dropdown cleared terminal input.
- Fixed LSP error diagnostics persisting on valid symbols after workspace reanalysis.
- Resolved issue where duplicate skills installed across multiple provider directories would appear twice.
- Fixed git diff stats chip incorrectly appearing in non-git directories.
- Fixed global hotkey window opening on wrong screen after sleep/wake when pinned to specific display.
- Fixed cursor position queries not working when connected via tmux control mode (`-CC`).
- Fixed agent driver not waiting for automatic error retry on network failures.
- Fixed incorrect ANSI colors in Adeberry theme.
- Fixed bug where some MCP servers would fail to connect due to unsupported `resources/list` method.
- CLI exits immediately with error when credentials are invalid instead of timing out while syncing Warp Drive.
- Fixed crash when selecting text during rapid terminal output.
- Fixed ephemeral MCP servers not included in multi-agent API requests.
- Fixed settings page not updating profile picture after auth state changes.
- Fixed "Open in Warp" button not working for code snippets in restored and forked AI conversations.
- Hide free cloud credits banner on shared sessions and WASM builds.
- Fixed case where newest plan created by agent would not visually replace a previous plan that was open.
- "Plan synced to Warp Drive" toast no longer appears when synced plan is in different tab.
- Fixed "open file" button in code review diff view not working when pane is maximized.
- Fixed git metadata background operations after terminal is closed.
- Mobile soft keyboard works for LRCs.
- Oz agents report more detailed information about session-sharing failures.

### Oz updates
- Oz agent tasks report structured error codes to server, enabling better error tracking and retryability handling.
- Fixed Oz cloud agent not waiting for automatic error retry on network failures.
- Added support for passing arguments to skill invocations (`$ARGUMENTS`, `$N`) and including user queries with invocation.

---

## 2026.02.25 (v0.2026.02.25.08.24)

### New features
(None)

### Improvements
- Reintroduced customization support for the Warp prompt.
- Maximizing Code Review panel opens the file list.
- Docker image inputs in environment settings show link to Docker Hub page when available.
- Added `/compact-and` slash command to trigger conversation compaction and automatically send a follow-up prompt.
- Added `/profile` command to switch between profiles using an inline menu.
- Oz CLI outputs direct link to Oz webapp run page when spawning cloud agents.

### Bug fixes
- Fixed bug where Oz CLI would open Warp GUI app rather than printing help output.
- Fixed broken documentation links on Referrals settings page and AI settings page.
- Fixed CLI agent footer detection when commands prefixed with env var assignments (e.g. `OPENCODE_EXPERIMENTAL_PLAN_MODE=1 opencode`).
- Fixed rendering of codebase search tool calls when restoring conversations.
- Local-only slash commands such as `/open-file` now disabled automatically in remote sessions.
- Fixed "View all cloud runs" button linking to specific run instead of runs list page.
- Fix tab alignment in monospace text blocks using fixed-width tab stops.
- Improve cloud-mode modal routing for concurrent-limit vs out-of-credits states.
- Fix cloud-mode out-of-credits modal flicker and compact CTA alignment.
- \[Linux] `oz` CLI package renamed to `oz-stable`.

### Oz updates
- Add "Default mode for new sessions" setting to open new tabs and panes in agent view by default.

---

## 2026.02.18 (v0.2026.02.18.08.22)

### New features
- Agents can fetch and read content directly from URLs provided in your query.

### Improvements
- Enabled multi-select in Notebooks and code editors.
- Added new setting under **Appearance** → **Tabs** to preserve active tab's color when creating new tabs.

### Bug fixes
- Fixed Escape key closing up-arrow menu instead of transitioning to normal mode when in vim insert mode.
- Fixed Option-left and Option-right keys not working for word navigation in code review comments editor.

---

## 2026.02.11 (v0.2026.02.11.08.23)

### Improvements
- Updated tabs UI to be cleaner, more readable, and to make tab focus clearer.

### Bug fixes
- Show Input Type setting (Warp/PS1) regardless of global AI setting.

---

## 2026.02.10 (v0.2026.02.10.11.37)

### New features

#### Introducing Oz: orchestration for cloud agents

Oz is Warp's orchestration platform for cloud agents: launch parallel agents, automate recurring engineering work, and build apps on top of agents with full visibility and control.

[Read the launch post →](https://www.warp.dev/blog/oz-orchestration-platform-cloud-agents)

#### Oz Cloud Agents

- **Run Cloud Agents from anywhere with built-in tracking** — start agents from Warp or via CLI, triggers, or schedules. Every run is auditable and steerable. [Cloud Agents docs →](https://docs.warp.dev/agent-platform/cloud-agents/overview)
- **Cloud environments for consistent execution** — configure Docker-based environments and run agents in isolated cloud sandboxes. [Environments docs →](https://docs.warp.dev/agent-platform/cloud-agents/environments)
- **Track agents from the web** — manage runs, create schedules, configure environments, set up integrations at [oz.warp.dev](https://oz.warp.dev).
- **Schedule agents based on Skills** — run agents automatically on a cron schedule for code cleanup, dependency updates, issue triage. [Scheduled Agents docs →](https://docs.warp.dev/agent-platform/cloud-agents/triggers/scheduled-agents)
- **Programmable by default** — orchestrate agents via CLI and integrate Oz into tools/services via API/SDK. [API and CLI reference →](https://docs.warp.dev/reference)

#### Warp Upgrades

- **Agent Modality** — two distinct modes: clean terminal for commands, dedicated conversation view for multi-turn agent workflows.
- **Cloud-Synced Conversations** — agent conversations sync to cloud and persist across devices. Share via link, view on web, continue locally.

#### Agent Capabilities

- **Skills** — reusable instruction sets that agents auto-discover from project or home directory. Invoke with `/{skill-name}` or run as scheduled cloud agents. [Skills docs →](https://docs.warp.dev/agent-platform/warp-agents/skills)
- **Computer Use** — agents interact with desktop environments in sandboxed cloud containers. [Computer Use docs →](https://docs.warp.dev/agent-platform/warp-agents/computer-use)

---

## 2026.02.04 (v0.2026.02.04.08.20)

### New features
- Full support for Kitty keyboard enhancement protocol, enabling TUI applications like OpenCode to detect and use enhanced keyboard input.
- Support agent footer when running Copilot CLI.
- New paid plan, **Max**, with 12× more monthly credits than Build. Upgrade in `Settings > Billing and Usage`.

### Improvements
- Improved environment update handling with better timestamp tracking and immediate UI refresh after edits.
- `@` menu shows function definitions when NLD is disabled.
- Conversation deep links open in a new tab instead of a new window.
- Renamed `edit` slash command to `open`.
- Fixed race condition when using API keys with Oz CLI.
- Improved robustness of MCP connections (especially using legacy SSE transport). "Transport closed" errors now trigger reconnection.
- New setting to keep opened/closed state of tool panel consistent across tabs in the same window.

### Bug fixes
- Fixed "Sharing in Warp Drive" onboarding block appearing mid-stream during agent responses.
- Disabled codebase indexing on non-agent run commands.
- Fixed scrolling behavior when typing in long-running commands.
- Fixed sharing dialog copy link icon being slightly larger than text.
- Fixed issue where code review panel would get stuck on "Loading open changes" when multiple repositories open in same tab.
- Fixed crash caused by orphaned wide character flags in terminal grid.
- Fixed clipping issue in terminal message bar.

---

## 2026.01.28 (v0.2026.01.28.08.14)

### Improvements
- Files opened from code review panel, project explorer, global search respect your external editor setting.
- Toggling plan while pane is maximized restores layout to show plan.
- Added "copy path" button to file headers in code review panel.
- Pasting images into input enters Agent Mode, matching drag and drop behavior.

### Bug Fixes
- Fixed issue where conversations could break when agent read large images from directories.
- Fixed input buttons overflowing into adjacent panes in narrow layouts.
- Fixed text in MCP tool call details not copyable.
- Fixed status indicator incorrectly showing for empty conversations in tab headers.
- Fixed Drive team section header displaying in all caps.
- Fixed Enter key not working in MCP installation modal.
- Fixed slash command text not highlighting correctly in some cases.
- Fixed input mode detection occasionally switching unexpectedly.
- Fixed `/edit` command failing when filename had trailing whitespace.

---

## 2026.01.21 (v0.2026.01.21.08.14)

### New Features
- Global search in files across your current directories. Use `Cmd+F`/`Ctrl+Shift+F` to open.
- Expanded web search support to additional models.

### Improvements
- Save AI prompts as Agent Mode workflows via context menu.
- `/init` generates AGENTS.md instead of WARP.md.
- Added horizontal autoscrolling when jumping to line/column.
- Better language detection for syntax highlighting.

### Bug Fixes
- Fixed memory leak when making Agent Mode request.
- Fixed issue where "waiting for a password" notifications triggered incorrectly when launching certain terminal apps like neovim.
- Fixed duplicate entries appearing in agent management view for Slack-triggered conversations.
- Fixed alias expansion being triggered in AI input when it should only apply to shell commands.
- Fixed issue where multiple shell commands could enter long-running mode in same request batch.
- Hide AI options in command palette when AI is disabled.
- Stopped highlighting search matches in reasoning blocks.
- Fixed session viewer input being cleared when agent runs commands.

---

## 2026.01.14 (v0.2026.01.14.08.15)

### New features
- Added footer for third party CLIs.
- Added onboarding flow for new users.

### Improvements
- Fixed duplicate rule suggestions on dismiss and save.
- @-context search matches on both name and content for notebooks, rules, and workflows.
- Updated checkbox checkmark to use foreground color for better theme consistency.
- Filter selections in cloud agent management view persist across app restarts.
- MCP servers with OAuth authentication can be used in warp agent run if previously authenticated in desktop app.

### Bug fixes
- Fixed bug where text in MCP tool call detail wasn't selectable.
- Fixed agent thread banner text overflow on smaller screens.

---

## 2026.01.07 (v0.2026.01.07.08.13)

### New Features
- Added agent tips under warping indicator.

### Improvements
- Users can create team-scoped API keys.
- Agent tip leads with `WARP.md` when mentioning project-scoped rule files.
- `oz agent run-cloud` can create cloud agent tasks shared with team members.
- Updated agent profile switching tip to better explain why users would want to switch profiles.
- Comments in code review flow render full width when there are 4 or fewer comments.
- When completions menu is opened (tab), no completion item is selected by default. Pressing enter while no completion is selected directly runs the command in input.
- `oz agent run-cloud` command supports saved prompts.
- Added full terminal use model selector in agents profile page for selecting specific model for full terminal use work.

### Bug fixes
- Improved out-of-memory handling for cloud agents.
- Fixed configuration error creating team-scoped Warp-managed secrets.
- Fixed 'parameter not set' error in zsh when users have setopt nounset enabled.
- Fixed issue where up arrow history could be ordered incorrectly on quit or restart Warp.

---

## 2025.12.17 (v0.2025.12.17.17.17)

### Improvements
- Warp specifies what different models were used for in credit transparency footer.
- Choose whether forked conversations open in split pane or new tab.
- `warp mcp list`, `warp environment list`, `warp agent profile list` support plain-text and JSON output.
- MCP server configurations displayed in integration details (`warp integration list`).
- Added support for configuring MCP servers in integrations.

### Bug fixes
- Fixed bug where Oz CLI runs could get stuck trying to run a denylisted command.

---

## 2025.12.10 (v0.2025.12.10.08.12)

### Improvements
- Added 'Initialize codebase' button to Code Review when in uninitialized repo.
- Added new sub-menu in model picker for selecting reasoning level of reasoning models.
- Added syntax highlighting for Vue template files.
- Added support for specifying custom models for agents, integrations, scheduled agents using `--model` flag.
- Added support for custom HTTP headers in MCP Streamable HTTP or SSE server connections.
- Added `/conversations` slash command with clock-rewind icon to open conversation history palette.
- Warp integrations proactively signal if agent is blocked.

### Bug fixes
- Fixed bug where credit denomination wasn't set properly for teams with auto-reload on in **Settings** → **Billing and usage**.
- Code editor opens to the right of active tab when "Choose a layout to open files in Warp" set to "New tab".
- Fixed mouse reporting for apps not using alternate screen buffer (e.g. Radare2).

---

## 2025.12.03 (v0.2025.12.03.08.12)

### Improvements
- Oz CLI displays more detailed information when agent tries to take a prohibited action.
- Drag file paths from Project Explorer into active terminal commands like claude code and gemini.

### Bug fixes
- Fixed bug causing unbounded memory growth when using Warpified subshells or legacy SSH Warpify implementation.
- Fixed bug causing `comm` errors in Warpified subshells.
- \[Windows] Fixed keybinding for "find in code editor" — now `Ctrl+Shift+F`.
- Ensured Oz CLI available automatically on macOS.
- Fixed toast messages showing "Notebook" instead of "Plan" when taking actions on Plans in Warp Drive.

---

## 2025.11.19 (v0.2025.11.19.08.12)

### New features
- MCP server configurations can be shared with team members.
- Warp provides out-of-box MCP servers for common services like Github and Linear, installable with a single click.
- Find works in code review pane.

---

## 2025.11.18 (v0.2025.11.18.12.24)

### New features
- [Full Terminal Use](https://docs.warp.dev/agent-platform/warp-agents/full-terminal-use): Let the agent use the terminal as you would.
- [`/plan`](https://docs.warp.dev/agent-platform/warp-agents/planning): Spec-driven development in Warp.
- [Interactive Code Review](https://docs.warp.dev/agent-platform/warp-agents/interactive-code-review): Review agent's code like a teammate's.
- [Slack and Linear integrations](https://docs.warp.dev/agent-platform/cloud-agents/integrations): Ask the agent to get to work from tools you already use.
- Warp's Agents can [search the web](https://docs.warp.dev/agent-platform/warp-agents/web-search) when relevant.

---

## 2025.11.12 (v0.2025.11.12.08.12)

### Improvements
- \[Vim mode] Paragraph text objects supported (e.g. `dip` to delete a paragraph).
- \[Vim mode] Press `K` over part of a command to inspect it in terminal mode.
- Agent notifications reference conversations' titles instead of queries.

### Bug Fixes
- Copy link button works as expected after shared sessions closed.

---

## 2025.11.05 (v0.2025.11.05.08.12)

### New Features
- From code review panel, add file diffs or entire diff set as context to agent conversation.

### Improvements
- Warp defaults to requiring approval before agent executes a command.
- Shared session links open in new tab by default.
- Display summarization tokens when conversation summarization triggered.

---

## 2025.10.29 (v0.2025.10.29.08.12)

### Improvements
- Display conversation summaries when summarization triggered.
- Added completions for Oz CLI.
- Updated community links from Discord to Slack throughout app.

### Bug Fixes
- Reduce padding on restored Agent Mode blocks and expanded shell commands.
- Add support for delete key in vim mode in code editors.
- Fix rendering for multi-line Agent Mode shell commands.

---

## 2025.10.22 (v0.2025.10.22.08.13)

### New Features
- Warp suggests new unit tests in addition to code fixes via Suggested Code Banners.

### Improvements
- Fixed issue where model specs menu would get cut off.

### Bug Fixes
- Fixed close icon becoming too small on Warp Drive notebook viewer.
- Fixed issue where CLI would report invalid debug IDs in troubleshooting output.

---

## 2025.10.15 (v0.2025.10.15.08.12)

### New Features
- Warp supports scaling entire application. Change zoom level in `Settings > Appearance > Window` or press `Cmd++` (macOS) / `Ctrl++` (Windows/Linux).

### Improvements
- Code review pane can show diffs against other base branches.
- Added confirmation dialog when cancelling AI summarization requests.
- Expand Suggested Code Diffs further on down arrow.
- Restore closed panes using `Cmd+Shift+T` or `Ctrl+Alt+T` (Windows/Linux) within 60 seconds.
- Added shell completions for Oz CLI.
- Warp Drive Environment Variables supported on Windows (PowerShell, Git Bash, WSL).
- Enriched model picker to include detailed specs of each model's intelligence, speed, cost.

### Bug Fixes
- Fixed custom window size setting not reliably applying on startup.

---

## 2025.10.08 (v0.2025.10.08.08.12)

### Improvements
- Added ability to sort team members by usage in **Settings** → **Billing and usage**.
- Added UI indication when Agent Mode conversation summarization in progress.
- Made sizing for headings consistent across all collapsible blocks.
- `@` menu no longer appears when running JS package manager subcommands.
- \[macOS] Resolved issue re-mapping keybindings conflicting with macOS keybindings.

### Bug Fixes
- Agent Mode requested command previews show only first line of multi-line commands.
- Removed misleading "auto-approve" button while Warp generates fix for failed terminal commands.

---

## 2025.10.01 (v0.2025.10.01.08.12)

### Improvements
- Editing suggested file changes takes place in same pane instead of new tab.
- When using `@` context menu outside a repo, current folder's contents listed.
- Code mode file picker displays gitignored files.
- \[macOS] Warp stores session restoration data in more-secure application container.

---

## 2025.09.24 (v0.2025.09.24.08.11)

### New features
- Create new files directly in Warp. Search "New File" in command palette. macOS users find it in app menu under "File".

### Improvements
- Changed "Reject" label to "Refine" for code diffs and plans.
- Added realtime form validation to Environment Variables when secret redaction enabled.
- Avoid showing `@` context completions menu when typing package name (covers JS, Python, Ruby, Go, PHP installers).
- Added "auto-approve" option with keyboard shortcut for requested commands and MCP tool calls.

### Bug fixes
- Fixed error with fish shell v4.
- Avoid showing multiple "stopped task" banners when toggling resumed conversation back to stopped before agent begins responding.
- Fix input problems with Russian on PowerShell.

---

## 2025.09.17 (v0.2025.09.17.08.11)

### New Features
- Added support for custom Regex names in Enterprise Secret Redaction.

### Improvements
- @ context menu can be activated outside Git repositories for actions like attaching blocks/workflows.
- Move auto-approve button alongside agent "stop" button for easier access.
- Move "stop" button alongside "Warping..." indicator.
- Added right-click context menu to code review pane with split pane controls.
- Files selected in file tree open in preview mode until interacted with.
- Warp's agent shows reasoning traces from reasoning models.
- Ctrl-c during long-running command run by agent also stops agent.

### Bug Fixes
- Fixed nested lists in agent markdown output sometimes not rendering properly.
- Fix slow scrolling on macOS Tahoe.
- Fix todo lists overflowing off screen for 10 or more items.
- Fix code review maximize button appearing outside split pane mode.
- Fix stop button unexpectedly disappearing when accepting "start a new conversation" suggestion.

---

## 2025.09.10 (v0.2025.09.10.08.11)

### Improvements
- Added support for ignoring input suggestions. Click X next to item in up-arrow history menu to hide. Also enable `Show autosuggestion ignore button` setting.
- Git UI detects more changes in git worktrees.
- Rename/delete items in file picker and open with system file explorer.
- Combine "refine" and "cancel" buttons into single "reject" button.
- Switch node versions by clicking on node version chip.
- Added "New Agent" button to agent management panel.

### Bug fixes
- Fixed issue where agent output in code block inserted at wrong place.
- Fixed code review diff buttons incorrectly receiving mouse events.
- Avoid auto-expanding agent's requested commands while using voice dictation.
- Add back auto-approve button for classic input mode.
- Fixed keyboard navigation of chip menus in input while agent running.
- Properly reset context when user sends query to agent.

---

## 2025.09.03 (v0.2025.09.03.08.11)

### Improvements
- Added support for rendering H4-H6 in markdown.

---

## 2025.09.01 (v0.2025.09.01.20.54)

### New features
- Revert diff hunks directly from Code Review Pane.
- Add lines of file to context of conversation from Warp code editor.
- Search and restore Agent conversations in history using `conversations:` prefix.
- Search and navigate to indexed codebases using `repos:` prefix.

### Improvements
- Voice transcriptions no longer cut off when unfocusing input editor.
- Can select `$EDITOR` environment variable as default application for opening file links.
- Added new header treatment for unfocused Warp windows.
- \[macOS] New dock icon option — the Cow icon! (`Appearance > Icon` to change).
- Pasting images in terminal input switches to Agent Mode and attaches image as context.
- Added support for Streamable HTTP transport for MCP servers.

### Bug fixes
- \[Windows/Linux] Fixed keybinding conflict for split pane down action.
- Fixed tab tooltips displaying unwanted leading and trailing whitespace.
- Pressing up key while model picker open no longer opens command history.

---

## 2025.08.27 (v0.2025.08.27.08.11)

### New Features
- New pane to view changes to Git repository.
- Files open in tabbed viewer.
- Syntax highlighting for Scala files.

### Bug Fixes
- Fix paths not inserted when pasted images are not attached.

---

## 2025.08.20 (v0.2025.08.20.08.11)

### New features
- [Suggested Code Diffs](https://docs.warp.dev/agent-platform/warp-agents/active-ai#suggested-code-diffs) — Warp suggests fixes for simple errors (e.g. compiler errors). Toggle in `Settings > Active AI`.

### Improvements
- Added setting to hide fixed prompt suggestions.
- Updated default input type from 'Classic' to 'Universal'.
- Improved styling and usability of tabs for narrow windows.

### Bug fixes
- Fix failures to start zsh sessions when using prezto.
- Agent status indicator no longer disappears while command running.
- Selecting workflow correctly closes workflows menu.
- Don't auto-attach image if file pasted as plaintext.
- Fixed issue with drag-drop images.
- Fixed display of completions with special characters.

---

## 2025.08.13 (v0.2025.08.13.08.12)

### New Features
- Agent Mode displays interactive code blocks when referencing snippets from codebase.
- Added support for defining project-scoped rules with WARP.md file. See [Rules](https://docs.warp.dev/knowledge-and-collaboration/rules#project-scoped-rules).
- Added Slash Commands (/) in Agent Mode or Auto-Detection Mode. See [Slash Commands](https://docs.warp.dev/agent-platform/warp-agents/slash-commands).

### Improvements
- Added syntax highlighting for SQL in Warp's code editor.
- Added button to dismiss suggestions footer.
- \[Linux and Windows] Added support for drag-dropping multiple images.
- New files in Warp open in pane by default. Configure in `Settings > Features > General > Choose a layout to open files in Warp`.
- Input stays in Agent Mode after image attached instead of switching to shell mode.

### Bug Fixes
- Fixed behavior when clicking Agents chip in Classic input mode.
- Repository-scoped Warp features available in git worktrees.
- Fixed drag-drop of images for long-running commands (e.g. Claude Code, vim).
- \[Linux and Windows] Fixed attaching images from pasted files.
- Fixed "Find in selected block" feature after clicking active running block.
- Fixed text overlap on narrow panes with Classic Warp Prompt with Same Line Prompt.
- \[macOS] Fixed bug causing text to disappear for very long Agent Mode prompts.

---

## 2025.08.06 (v0.2025.08.06.08.12)

### New Features
- GPT-5 now available to all users. Use model selector in input bar.
- \[macOS] Attach images as context by drag-and-drop or pasting from clipboard.

### Improvements
- Open any files within Warp's editor (including txt/csv files).
- Warp can edit Bazel files, `.bashrc`, `.zshrc` files.
- Added `Always show secrets` to Secret Redaction for less obtrusive secret redaction mode.
- Added reset time to Billing and usage menu.

### Bug Fixes
- Fix fish version <= 3.7 when vi keybindings activated.
- Fixed bug affecting "Open in Markdown Viewer by default" setting.
- Fixed issue where typeahead for next command could be lost if typed really quickly after hitting enter.
- Resolved issue where stopping voice recording via button would interrupt transcription.

---

## 2025.07.30 (v0.2025.07.30.08.12)

### New Features
- Configurable block size limit for higher scrollback limits! Configure in `Settings > Features > Session > Maximum rows in a block`.
- \[Linux] Added support for pasting images as context.

### Improvements
- "Open in Warp" banner supports code files.
- User-configured redaction rules applied to contents of diffs and files in addition to terminal blocks.
- Added SHIFT-ENTER keybinding. Claude Code users can add linefeeds to prompt.
- Added overflow menu button in top right of AI blocks for copying contents.

### Bug Fixes
- Deleted files no longer appear in @-context selection box.
- Users with Turkish locale no longer see extra letter "i" between commands.
- \[Windows] Restored windows no longer positioned with title bar above top of display.

---

## 2025.07.23 (v0.2025.07.23.08.12)

### New Features
- \[Windows] Added support for pasting images from clipboard into Agent Mode context.

### Improvements
- Added image filename when pasting images into Agent Mode context.
- Added support for restarting MCP servers when Warp restarts.
- Added support for copying AI block and conversation contents via context menu.
- Added Node.js prompt chip.

### Bug Fixes
- Fixed bug where attaching block as AI context would reset input state.
- Fixed spacing issue with horizontal scrollbars in agent planning view.
- Added support for auto-expanding manually executed Agent Mode suggested commands.
- Fixed bug where Warp would hang while updating code symbols in @-context menu.
- Modified secret redaction regexes to be case sensitive.
- Modified Universal Input to no longer exit conversation via "backspace".

---

## 2025.07.16 (v0.2025.07.16.08.12)

### New Features
- \[macOS] Support pasting images from clipboard into Agent Mode context.
- Migrated Warp's built-in set of Secret Redaction regexes into user's regexes.
- Added support for Find and Replace using `Cmd+F` when viewing diffs or editing files in built-in code editor.

### Improvements
- Removed lock icon from Secret Redaction in favor of asterisks when ligatures enabled.
- Added individual keybinding shortcuts to change input modes.

### Bug Fixes
- Fixed issue where hover tooltip for disabled prompt suggestions didn't render or was hard to read.
- Fixed background color of inline code in restored AI blocks.

---

## 2025.07.09 (v0.2025.07.09.08.11)

### New Features
- New secret redaction strikethrough UI with `Settings > Privacy > Hide secrets in block list` setting (defaults to off).

### Improvements
- Resume stopped AI conversations: `Ctrl-C` to stop, `Cmd+Shift+R` (macOS) or `Ctrl+Shift+R` (Windows/Linux) to resume.
- Code Diff view's default Edit and Revise keybindings changed and made configurable.
- Added syntax highlighting for PowerShell, Kotlin, Swift.

### Bug Fixes
- Fixed issue with `.inc` file chunking.
- Clicking on active, long-running block focuses input instead of selecting block.

---

## 2025.07.02 (v0.2025.07.02.08.36)

### New features
- Tab close button can now be set to the left.

### Improvements
- Added syntax highlighting for TOML, PHP, Lua, Ruby, Groovy (with Java syntax).
- Added conda chip support to new Universal Input prompt.
- Increased color contrast on tabs.
- Added "Upgrade" menu item for free users and "Billing and Usage" menu item for paid users.

### Bug fixes
- When AI disabled, ESC no longer enters Agent Mode.
- Fixed issue on WSL where files created by Agent Mode would have CRLF line endings.
- \[macOS] Tweaked autoupdate logic to more reliably remove old applications off disk.
- Fixed "Manage plan suggestion setting" link.

---

## 2025.06.25 (v0.2025.06.25.08.12)

### New Features
- Git branch and directory chip now searchable.

### Improvements
- Added support for HCL syntax highlighting in Terraform files.

### Bug Fixes
- Fixed potential crash when displaying context chips with Unicode characters in file paths.
- Fixed rendering issue with line numbers in suggested diffs.
- Attach context chip no longer appears if no context you can attach.

---

## 2025.06.20 (v0.2025.06.20.22.47)

### New Features

**Warp 2.0 is here - The Agentic Development Environment**

Built from the ground up for agentic workflows, Warp is the most powerful tool for prompting, coding, and collaborating with multiple agents.

**Multithread yourself with agents**

- Launch intelligent tasks (agents) with a prompt. Agents gather context using CLI commands, MCP, Warp Drive, Codebase Context.
- New Agent Management Panel to monitor, multitask, and intervene across multiple agents.
- Set autonomy controls and get notified when agents need your help.

**A state-of-the-art coding platform**

- 70% on SWE-bench, #1 on Terminal-Bench — highest quality coding agent available.
- Codebase Context: Warp indexes and understands codebase, allowing you to debug and write code faster without storing any code on Warp's servers.
- Review and edit diffs directly in Warp's native code editor.

**Still a great command-line**

- New Universal Input: run commands or prompt agents from a single interface.
- Choose model, continue conversation, attach images, link URLs, reference files using `@`.
- Modern, IDE-like terminal experience with completions, predictions, mouse support, all built natively in Rust for performance.

**Context for teammates and agents**

- Knowledge store for configuring MCP, defining Rules, storing shared commands, notebooks, env vars, prompts as context.

All of this comes with higher AI usage limits on Pro and Turbo plans, plus new pay-as-you-go overages.

---

## 2025.06.11 (v0.2025.06.11.08.11)

### New Features
- Attach images as context for Agent Mode using image icon.

### Improvements
- \[Linux] Added support for standard installed Zed and Zed Preview as default code editors.
- \[macOS] Added support for Zed Preview as default code editor.
- Added syntax highlighting support for TSX and JSX.
- Increased visibility of non-focused diff hunks when navigating diffs.
- New Agent Mode output no longer force-scrolls.

### Bug Fixes
- Fixed keybinding missing for editing requested commands.
- Removed keybindings for zero-state prompt suggestions to avoid conflicting with tab switching keybindings.

---

## 2025.06.04 (v0.2025.06.04.08.11)

### New Features
- Sonnet 4 now available (enabled by default in "auto" model).

### Improvements
- Press fast-forward button to auto-execute all Agent actions until task completes.
- Added ability to share session via right-click on tab.
- Give Agent permission to auto-execute MCP tool calls.

### Bug Fixes
- Fixed issue where Agent Mode would sometimes not find untracked files in Git repos.
- Fixed Agent Mode file editor randomly scrolling to first line of file.

---

## 2025.05.28 (v0.2025.05.28.08.11)

### New Features
- Added MCP server support. Extend Agent Mode capabilities using programs that support the [Model Context Protocol](https://docs.warp.dev/knowledge-and-collaboration/mcp).

---

## 2025.05.21 (v0.2025.05.21.08.11)

### New Features
- Set new Agent Mode permissions around executing commands, reading files, coding, planning in AI settings.

### Improvements
- Choose coding model behind Agent Mode.
- Agent Mode conversations can be paused via hovering control panel.
- Improved maximum block output capacity to 50k lines.

### Bug Fixes
- Fix edit icon positioning for shared sessions.

---

## 2025.05.14 (v0.2025.05.14.08.11)

### Improvements
- Introduced refining functionality for requested commands.
- Added ability to continue previous Agent Mode conversations directly from response blocks.
- Overhauled editing experience for suggested plans.
- Renamed input auto-detection setting to "natural language detection" in Command Palette.
- Zero-state prompt suggestion chips now horizontally clipped instead of individually shrunk.

### Bug Fixes
- Fixed incorrect ordering in history of executed commands and Agent Mode queries.
- Copying text from Agent Mode plans and suggested code changes now works more reliably.
- \[Windows] Reduced false-positives from virus scanners.

---

## 2025.05.07 (v0.2025.05.07.08.12)

### Improvements
- Redesigned env var collection block UX.
- Added ability to embed Warp Drive Prompts inside Notebooks.
- Added AI block loading animation.
- Added ability to select and continue previous Agent Mode conversations.
- \[macOS] Improved time to update and relaunch Warp.

### Bug Fixes
- Fixed bug where escape was clearing autosuggestions in Vim's insert mode.
- Stopped showing unexpected block in planning output for o3.
- \[Windows] Fixed bug when hovering symlinks in WSL sessions.
- Fixed terminal input remaining hidden after cancelling env var block.
- Prevented unexpected empty code fences in Agent Mode when using Gemini 2.5 Pro or o3.

---

## 2025.04.30 (v0.2025.04.30.08.11)

### New Features
- Added desktop notifications for Agent Mode. Get notified when agent completes task or needs attention. Configure in `Features > Notifications`.

### Improvements
- Agent Mode more robust at applying code diffs.
- Redesigned requested commands UX.
- Improved readability for "needs password prompt" desktop notifications.

---

## 2025.04.23 (v0.2025.04.23.08.11)

### Improvements
- Restored Agent Mode conversations can be continued.
- Agent Mode has access to filepath search tool for coding tasks.
- Improved reliability and positioning of suggestion dialogs for rules and Agent Mode workflows.
- Reworked command palette search.

### Bug Fixes
- Fix XML parse errors complaining that "thought" cannot be empty.
- \[Windows] Fixed issue where Agent Mode would fail to search in WSL or Git Bash.
- Show "copy" button and text selection tools when right-clicking selected environment variable text.
- Fixed old shortcuts icon appearing in new tab page if recommended AI prompts disabled.
- Fish commands containing syntax errors correctly "finish" block.

---

## 2025.04.16 (v0.2025.04.16.08.11)

### New features
- After editing a code diff, returned to original Agent Mode conversation.
- Commands with certain invalid arguments no longer suggested (file paths, git branches, docker images).
- \[Windows/Linux] Open launch configurations in current window with `Shift+Enter` or `Ctrl+Enter` on Command Palette.
- Added more default regexes for Secret Redaction pertaining to AI API keys.
- Typing `ESC` in terminal input editor clears any autosuggestions.

### Bug Fixes
- Fixed issue with rendering performance for file links in AI output.
- Fixed issue causing Warp to crash when Agent Mode outputs broken links.
- New tab page no longer falls back to email if display name not set.
- Fixed prompt chips not clickable in new session with prompt pinned to top.
- Agent Mode properly greps for queries containing double quotes.

---

## 2025.04.09 (v0.2025.04.09.08.11)

### New features
- Recommended AI prompts shown in new tabs. Disable in `Settings > Features`.

### Improvements
- Agent Mode better at searching for exact function/symbol names.
- Fix text selection for environment variable blocks.
- Attach selected text in a code block as Agent Mode context.
- Warp supports marked text in IME (non-English keyboards).
- Text selectable for non-expandable command outputs (e.g. failed agent tasks).
- Zero-state chips no longer shown when entering AI input with non-empty input buffer.

### Bug fixes
- Fixed bug preventing copying of selected text of code block when Agent Mode enabled.
- Fixed bug allowing selection in code block and text simultaneously.
- \[macOS] Fixed shells installed via Homebrew not appearing in list of available shells.

---

## 2025.04.02 (v0.2025.04.02.08.11)

### Improvements
- Improved login item management to respect when users manually remove Warp from login items.
- Input editor supports `Cmd+Shift+Up/Down` (macOS) or `Ctrl+Shift+Home/End` (Windows) to move and select to top/bottom of text buffer.
- Removed 3-hour conversation timeout; AI conversations remain active indefinitely.
- Show popup when users at AI limits have quota reset.
- Display notification when AI request quota resets after hitting limit in previous billing cycle.
- \[Windows] Added "Open Warp in new tab / window" item in File Explorer context menu under "Show more options".

### Bug fixes
- Minor fixes for iTerm and Kitty images.
- Fixed regression related to using keyboard shortcuts to navigate command in empty split pane.
- Fixed some issues with Agent Mode failing to read files.
- Click targets in scroll views click more reliably while moving mouse.
- \[Linux] Window corners correctly rounded with themes having background images.
- Fixed common failure modes for Agent Mode response deserialization errors.

---

## 2025.03.26 (v0.2025.03.26.08.10)

### New features
- Kitty Image Protocol supported on macOS and Linux.

### Improvements
- Agents may suggest using Dispatch to create a plan for complex tasks. Disable in `Settings > AI > Dispatch`.
- Resume auto-execution of previously dispatched plan if follow-up query set to "Dispatch".
- Added keyboard shortcut to accept most recent command correction.
- Zero-state suggestions not shown when using saved Prompt or past AI query.
- Tabs not resize while hovered, making closing multiple tabs easier.
- Warning dialog for closing sessions responds to `ENTER` and `ESC` keys.
- Selected text within Agent responses can be copied via right-click menu.
- \[Windows/Linux] Toggle whether block selected using `Ctrl+Click`.

### Bug fixes
- Fixed issue causing Agent Mode blocks incorrectly highlighted when performing rectangular selection.
- Fixed issue where duplicate cloud preferences could be created during sync operations.
- Fixed keyboard shortcut padding for prompt suggestions.
- Fixed color contrast issues with light themes for Pair & Dispatch chip in Prompt Editor.
- Agent Mode no longer defaults to Windows-style line endings when creating new file on macOS or Linux.
- PowerShell sessions start even if profile has terminating error.
- Numpad `ENTER` key behaves like `ENTER` key in Agent Mode.
- \[macOS] Fixed scenario where Warp would beachball while updating.
- \[Windows] In WSL, show completions for symlinked files.
- \[Windows] Fixed completions with `.exe` suffixes.
- \[Windows] Fixed setting Git Bash custom shell paths.

---

## 2025.03.12 (v0.2025.03.12.08.02)

### New features
- Agent Mode output rendered with Markdown formatting.
- Change font used for Agent Mode output (`Settings > Appearance`).

### Improvements
- \[Windows] Significantly improved pseudoconsole throughput (~3x improvement).
- Agent Mode model automatically selects best model based on task.
- Ordered lists in Markdown use alphabetical or Roman numeral labels when nested.
- \[Windows] Search more locations for PowerShell executable.
- Reduced size of Markdown headings.

### Bug fixes
- Control whether Warp starts at login via setting in `Settings > Features > Start Warp at login` (macOS only).
- \[Windows] Fixed issue where dynamic enums commands weren't being executed.
- Fixed bug with mouse cursor when hovering over buttons.
- Fixed bug causing high CPU load with codebase context.

---

## 2025.03.05 (v0.2025.03.05.08.02)

### New features
- iTerm Image Protocol supported on macOS and Linux.
- \[macOS] Warp starts at login (disable in System Settings > Login Items and Extensions).

### Improvements
- Input mode automatically returns to command mode when command detected in AI follow-up request.
- Text selections can be attached to Agent Mode queries as context.
- \[Windows] Window transparency works when using DirectX 12.
- \[Windows] Added "Open Warp Here" item in File Explorer context menu under "Show more options".

### Bug fixes
- Fixed issue where `bazel` completions could use up a lot of CPU.
- \[macOS] Fixed regression where title bar would be transparent in fullscreen windows.
- \[Windows] Fixed children of shell processes not always exiting properly at shell termination.
- \[Windows] Fixed Warpification for custom-built WSL distributions.
- \[Windows] Fixed Ctrl+Up and Ctrl+Down shortcuts not working in alt screen programs (e.g. vim, emacs).
- \[Windows] Fixed last line of output getting truncated with some prompt configs in WSL.
- \[Windows] Fixed issue where `.` would turn into n in ZSH when using ohmyzsh in WSL with Italian keyboard layout.

---

## 2025.02.26 (v0.2025.02.26.08.02)

### New features
- Add codebase context support to Agent Mode. Currently enabled for Git repositories only.
- \[macOS] Customize [App Icon](https://docs.warp.dev/terminal/appearance/app-icons) in `Settings > Appearance > Icon`.
- Show default suggestions in Agent Mode input.

### Bug fixes
- Multicursor input is now `ALT` on Linux and Windows.
- Fix prompt chip misalignment for certain fonts.
- Autosuggestions remain visible when input not focused to prevent height flickering.

---

## 2025.02.19 (v0.2025.02.19.08.02)

### New features
- Create and store AI memories to use as Agent Mode context.

### Improvements
- Expanded Prompt Suggestions to cover more use cases.

### Bug fixes
- Fixed Warp Prompt clipping issues with certain fonts.
- Fixed inverse and double-underline cell styling persisting through session restoration.

---

## 2025.02.12 (v0.2025.02.12.16.51)

### New features
- `Ctrl+Tab` configurable under `Settings > Features` to cycle between most recently used sessions.

### Improvements
- LLM menu keyboard-navigable.

### Bug fixes
- Clearing Blocks clears any active Prompt Suggestions.
- Fix Kali Linux `.bashrc` breaking Warp.
- Fix bug with Agent Mode in PowerShell sessions with multi-line commands.
- Fixed bug preventing Autosuggestions from being accepted and Agent Mode model from being selected while up arrow history open.
- Fixed cases where dragged Warp tabs would get stuck.
- Restores subshell Warpification script.
- \[macOS] Fix hotkey keybinding not triggering on non-US keyboard input source.

---

## 2025.02.05 (v0.2025.02.05.08.02)

### New features
- Talk to Warp to transcribe Agent Mode prompts or any other text. Set up hotkey in `Settings > AI > Voice` or use microphone button in AI input mode.

### Improvements
- Autosuggestions in input now soft-wrap.
- Attach default environment variables to a workflow.

---

## 2025.01.29 (v0.2025.01.29.08.02)

### New features
- Added support for DeepSeek R1 and V3 in Agent Mode.
- Agent Mode can auto-execute readonly requested commands. Commands can also be explicitly allowlisted or denylisted. Configure in `Settings > AI > Autonomy`.

### Improvements
- Use `j`/`k` keys to navigate up and down Warp Drive.
- Added Agent Mode chip to Warp prompt.
- Next Command preferred over Command Corrections when Corrections has less confidence.
- Moved Settings modal to its own tab.

### Bug fixes
- Fixed bug causing double-clicking to select incorrect range of text when non-ASCII characters present.
- Saving workflow aliases no longer deletes aliases from other workflows.
- Fixed cases where small part of bottom of editor cut off at certain appearance settings.

---

## 2025.01.22 (v0.2025.01.22.08.02)

### New features
- Generate input for any interactive CLI using `⌘I` (macOS) and `Ctrl+Shift+I` (Linux).
- Dynamically populate arguments in Workflows with shell commands.
- Added support for rectangular selection when holding `⌘⌥` (macOS) and `Ctrl+Alt` (Linux).

### Improvements
- Settings searchable and rendered in separate tab.
- Terminal font weight configurable.
- Launch Configurations save focused window state and active pane.
- Autosuggestions in input now soft-wrap.

### Bug fixes
- Fixed several issues where hovering over URLs in blocklist sometimes resulted in URLs only partially detected or not detected.
- Fixed issue with Prompt Suggestions occasionally remaining visible after subsequent command execution.
- \[macOS] Changed download location for new Warp updates to prevent corruption.

---

## 2025.01.15 (v0.2025.01.15.08.02)

### New features
- Font ligatures in grids! Enable in `Settings > Appearance > Text`.
- Define aliases that expand to Warp Drive workflows.

### Improvements
- Launch configurations save focused tab state.
- Added support for Windsurf as external editor.
- macOS-only: added new AI app menu.

### Bug fixes
- Fixed pane navigation when panes not overlapping.
- Fixed bug where Agent Mode LLM choices weren't populated correctly upon logging in.
- Fixed bug with drag-and-drop files causing duplicated filepaths.

---

## 2025.01.08 (v0.2025.01.08.08.02)

### New features
- Cloud syncing of Warp settings gradually enabled under `Settings > Account`.
- Setting to hide tab bar (Zen mode). See [documentation](https://docs.warp.dev/terminal/appearance/tabs-behavior).
- New profile menu.

### Improvements
- Removed Command Corrections banner.
- Implemented `_`, `+`, `-` motions in Vim mode.
- Warp shows warning before closing session with long-running process.
- Pasting multiple lines into terminal's `Find` feature converts to single line.
- Titles of notebooks imported from Markdown files no longer end in `.md`.
- "What's new" no longer shows on update.
- Added ability to hide blocklist lines.
- Consolidated top bar navigation items.
- Settings in profile menu.
- Scrollbars and pane controls only show on hover.

### Bug fixes
- Fixed rendering of keyboard shortcuts at larger font sizes.
- Tab completion menu closes after selecting single remaining suggestion.
- Warp displays error if relaunching to apply update failed.
- Old prompt suggestions won't reappear when issuing AI queries rapidly or after clearing blocklist.
- Accepting 'What happened here?' autosuggestion no longer clears AI context blocks.
- `Alt` key sends meta control codes to shell in long-running blocks and alt screen.
- When secret redaction disabled, secrets not redacted in command corrections.
- \[macOS] Fixed bug where assigning `cmd+shift+left` and `cmd+shift+right` to action sometimes wouldn't work.

---

## 2025.01.02 / 2024.12.18 (v0.2024.12.18.08.02)

### Improvements
- Immediately show error when trying to Warpify unsupported shells over SSH.

### Bug fixes
- Fixed blank lines being appended to some blocks on resize.
- Fixed issue where AI context disappears when accepting default autosuggestion.

---

## 2024.12.19 (v0.2024.12.18.08.02)

### New features
- Introducing: Next Command! Suggests next command to run based on active terminal session and command history. Visit `Settings > AI`.
- Added support for block and underline-styled cursors in input editor (vim mode disabled).

### Improvements
- Clarified default permission information for sessions and Warp Drive objects.
- F11 (configurable) toggles fullscreen on Linux and Windows.
- PowerShell environment variables recognized in completions.
- Cursor shape more responsive to clickable buttons.

### Bug fixes
- Characters from unhandled keystrokes no longer handled as typed characters in alt screen.
- Fixed issue with copying secrets when secret redaction disabled.
- kubectl completions respect kubeconfig specified through environment variables or command line flag.
- ssh commands with permission issues no longer suggest sudo.
- Fixed issue with lazygit entering blank screen.
- \[macOS] Fixed bug where Warp disk images volumes might not be unmounted after update.
- \[macOS] Improved robustness of autoupdate process.

---

## 2024.12.13 / 2024.12.11 (v0.2024.12.10.15.55)

### New features
- Prompt Suggestions may appear above input to help activate Agent Mode. Configure in `Settings > AI > Agent Mode`.
- Warp supports Claude 3.5 Sonnet and Haiku. Choose model in dropdown menu above Agent Mode prompts.
- Agent Mode can leverage Warp Drive contents for personal and team developer workflows.
- Shell Selector dropdown next to 'New tab' button to pick from available shells.
- Agent Mode can suggest code changes in built-in code editor.
- \[macOS] Configure whether closing last window quits app in `Settings > Features`.

### Improvements
- Settings to manage Warp's AI integration and permissions in `Settings > AI`.
- Single-window launch configs launched into active window from launch config palette using `Cmd+Enter` or `Ctrl+Enter`.
- Set `PS1` with `PROMPT_COMMAND` in bash.

### Bug fixes
- Fixed issue where 'Git Uncommitted File Count' prompt chip did not work on fish on Linux.
- Fixed highlighting for arguments in workflows with multibyte characters.
- Hitting ENTER within Launch Config Save Modal works as expected.
- Fixed issue with copying secrets when secret redaction disabled.

---

## 2024.12.05 (v0.2024.12.03.08.02)

### New features
- Share shared sessions directly with Warp team, another Warp user, non-Warp users via URL.
- Share Warp Drive objects directly with others via email or URL.
- Padding in alt-screen manually adjustable. Defaults to no padding.

### Improvements
- Improved PTY throughput by ~13% through more efficient dirty region computation.

---

## 2024.12.02 (v0.2024.12.02.15.50)

### Bug fixes
- Warp no longer uses so much CPU.

---

## 2024.11.27 / 2024.11.26 / 2024.11.25 / 2024.11.22 (v0.2024.11.19.08.02)

### Improvements
- \[Agent Mode] Code outputs no longer show confusing code diff UI.
- Sort Warp Drive objects by type with folders on top.

### Bug fixes
- \[Agent Mode] Single-line code suggestions no longer hidden behind horizontal scrollbar.
- Fixed crash interacting with Env Vars in command palette.
- Fixed bug where `command substitution: ignored null byte in input` would appear as output while using Bash subshell.

---

## 2024.11.19 (v0.2024.11.19.08.02)

### New features
- Use Warp without login.

---

## 2024.11.18 (v0.2024.11.18.16.37)

### Improvements
- Added padding after expanded Agent Mode requested command.
- Improved quality of autosuggestions.
- Warp Drive workflow links open in active terminal session rather than new tab.
- On web, Warp Drive workflows have button to quickly open in Warp's desktop app.

### Bug fixes
- Fixed Graphite CLI (`gt`) completions.
- Fixed completion and syntax highlighting behavior for arguments containing backslashes in PowerShell.
- Fixed issue where opening Warp Drive in browser could cause tab to stop responding.

---

## 2024.11.12 (v0.2024.11.12.08.02)

### Improvements
- Added padding after expanded Agent Mode requested command.
- Improved quality of autosuggestions.
- Warp Drive workflow links open in active terminal session.
- On web, Warp Drive workflows have button to open in desktop app.
- \[Linux] Increased app icon size.

### Bug fixes
- Fixed Graphite CLI (`gt`) completions.
- Fixed completion and syntax highlighting for arguments with backslashes in PowerShell.
- Fixed issue where opening Warp Drive in browser could cause tab to stop responding.
- \[Linux] Tightened timeout for looking up system color scheme at app startup.
- \[macOS] Fixed crash when starting app or opening new window.

---

## 2024.11.11 / 2024.11.05 (v0.2024.11.05.08.02)

### Improvements
- Fixed bug where Warpifying subshells could crash with input typed.
- Renamed Subshells tab to Warpify in Settings.

### Bug fixes
- Fixed issue where kubectl resource names wouldn't complete given prefix.
- Fixed bug causing not all memory to be immediately freed when clearing blocklist.
- \[macOS] Fixed crash when starting app or opening new window.

---

## 2024.10.23 (v0.2024.10.29.08.02)

### Bug fixes
- Improved command completions to no longer use error messages as valid options.
- Fixed kubectl completions not working as intended.

---

## 2024.10.17 / 2024.10.10 (v0.2024.10.08.08.02)

### Improvements
- Setting allowing focus to follow mouse hover.
- Automatically switch to shell command input mode if accepting shell command autosuggestion from Agent Mode.
- \[macOS] Adjusted default font smoothing configuration to improve text legibility.

### Bug fixes
- Alt-screen find doesn't beachball when scrolling through find matches.
- Select individual cells in alt-screen.
- All find matches correctly highlighted in alt-screen.
- Hitting ENTER within Launch Config Save Modal works.
- Clearing terminal input via ctrl-c closes command search.
- \[macOS] Access Warp Drive features from mac menus.
- \[macOS] Click mouse middle-button to paste from clipboard.
- Removed node prompt chip due to slow performance.
- Fixed issue on Linux where Warp took long time to start up.

---

## 2024.10.11 (v0.2024.10.08.08.02)

### Improvements
- Tab key always accepts active autosuggestions in zero-state.
- Command suggestions from Agent Mode are ghosted autosuggestions instead of direct buffer text.
- Warp shows warning when closing tab with running commands or shared sessions.
- New Agent Mode panes open to useful minimum width if Warp window big enough.
- Clearing terminal input via ctrl-c closes command search.
- \[macOS] Access Warp Drive features from mac menus.
- \[macOS] Middle-button paste from clipboard.

### Bug fixes
- Agent Mode queries de-duplicated in up-arrow history and Command Search.
- `Ctrl-d` can signal EOF when shell bootstrapping.
- Double-clicking tab bar toggles maximizing Warp window even when AI block present.
- Hovering over block insertion menu at bottom of notebook no longer causes Warp to hang.
- Fixed crash when search result in alt screen scrolled out of view.
- Fixed broken `Cmd+Shift+R`/`Ctrl+Shift+R` keybinding for accessing Workflows view.

---

## 2024.09.24 (v0.2024.09.24.08.02)

### New features
- Powershell supported! Make `pwsh` default shell or select in `Settings > Features > Startup shell for new sessions`.
- Agent Mode blocks and queries restored across sessions.

### Improvements
- Secret redaction applies to AI Blocks in addition to Command Blocks.
- New Agent Mode panes always open to the right.
- Navigate trash index via keyboard.

### Bug fixes
- `fish` config no longer sourced twice during shell startup.
- First window after launching Warp uses custom window size if set.
- Opening launch configuration, Warp respects restored and custom window sizes.

---

## 2024.09.17 (v0.2024.09.17.08.02)

### New features
- \[Linux] Warp supports Wayland. Configure window system in `Settings > Features > System`.

### Improvements
- Command Palette action "Export all Warp Drive objects" for bulk export.
- Completion suggestions for git commit hashes sorted reverse-chronologically.
- History shows working directory where Agent Mode query made.
- Agent Mode Blocks surfaced in Find.

### Bug fixes
- Fixed infinite loop bug that could lead to runaway memory usage and hanging.
- Fixed regression where Setup Guide didn't work.

---

## 2024.09.05 / 2024.09.10 (v0.2024.09.10.08.02)

### Improvements
- Links detected in Agent Mode responses.

### Bug fixes
- Fixed infinite loop bug causing runaway memory usage and hanging.

---

## 2024.08.29 (v0.2024.08.27.08.02)

### Bug fixes
- Link highlights correctly disappear when making changes in alt-screen programs.

---

## 2024.08.22 (v0.2024.08.20.08.02)

### New Features
- Specify cursor color in Warp themes.

### Improvements
- Warp restores fullscreen windows to fullscreen.

### Bug fixes
- \[macOS] Completions for commands work when typing command name with capital letters (not aliases).

---

## 2024.08.14 (v0.2024.08.13.08.02)

### New Features
- New enums for Workflow arguments. Set suggested options for any argument in workflow. Learn more in [Workflows](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/workflows#working-with-arguments).

---

## 2024.08.07 (v0.2024.08.06.08.01)

### New Features
- Find past Agent Mode queries in Command Search (`Ctrl+R`).

### Improvements
- Completions-as-you-type works in AI input for filepath completions.

### Bug Fixes
- Warp recognizes more escape codes for toggling alternate screen mode.

---

## 2024.07.30 (v0.2024.07.30.08.02)

### Improvements
- Easier to find and configure AI settings from command line. Enable/disable natural language detection or input hint text under `Settings > AI`.

---

## 2024.07.24 (v0.2024.07.23.08.02)

### New features
- Find AI queries from other sessions in up-arrow history.

### Improvements
- Clicking attached block on AI block no longer affects pending query's context selection.
- Clicking terminal input box no longer removes selected blocks.
- Added support for smart selections in AI blocks.
- Increased priority of command matches when searching for workflow.

### Bug fixes
- Opening file links with line and column numbers in Zed now works.

---

## 2024.07.19 / 2024.07.18 (v0.2024.07.16.08.02)

### Improvements
- Completions for git push origin include tags in addition to branches.
- "Open in Warp" feature requires running command to open Warpified Docker subshell.

### Bug fixes
- Warp prompt text respects custom line height settings.
- Scroll positions stable when hitting block line limits.
- Fish commands containing syntax errors correctly "finish" block.
- Fixed binaries listed directly in `PATH` being automatically executed when running commands in Bash.

---

## 2024.07.11 (v0.2024.07.09.08.01)

### New features
- Same line prompt. Choose prompt on new line or same line as commands (classic terminal). Visit `Settings > Appearance > Prompt`. Learn more in [Prompts](https://docs.warp.dev/terminal/appearance/prompt#same-line-prompt).

### Improvements
- Added support for completions while using Agent Mode input.
- Semantic selection works in AI blocks.
- Shift+click selects text for alternate screen apps in SGR mouse mode.

### Bug fixes
- Pressing Esc in Vim insert mode no longer closes history menu.
- Terminal context menus close when opening settings modal.

---

## 2024.06.27 (v0.2024.06.25.08.02)

### New features
- Warp's new Pro plan includes higher AI requests for individuals or small teams.

### Bug fixes
- Text selection in full screen apps changes as you scroll.
- \[macOS] Meta shortcuts (e.g. `Opt+U`, `Opt+I`) no longer ignored.

---

## 2024.06.21 / 2024.06.20 (v0.2024.06.18.08.02)

### Improvements
- Glyph over cursor takes high-contrast color for legibility.
- Dragging word or line selection in notebook extends selection.

### Bug fixes
- Fixes crash where text layout would not expect BOM marker at beginning of string.
- \[Linux] Fix middle-click paste doubling text.

---

## 2024.06.17 (v0.2024.06.11.08.02)

### New features
- New Agent Mode in Warp AI: Use plain English on command line to accomplish multi-step workflows.

---

## 2024.06.13 (v0.2024.06.11.08.02)

### Improvements
- Brackets and quotes autocompleted in workflow editor.
- Improved support for editing multi-line workflows.

---

## 2024.06.06 (v0.2024.06.04.08.02)

### Improvements
- Warp supports Unicode emoji presentation selectors when rendering glyphs.
- Removed default keybindings for Warp Drive object creation actions to free keyboard shortcut options. Assign custom keybindings in `Settings > Keyboard shortcuts`.

### Bug fixes
- When editing with Vim visual line mode and cursor at end of line, operators affect only correct lines.

---

## 2024.05.30 (v0.2024.05.28.08.02)

### Improvements
- Warp renders terminal text ANSI colors as specified by theme without dimming.

---

## 2024.05.23 (v0.2024.05.21.16.09)

### Bug fixes
- Fixed bug where terminal session could get stuck in bad state if SSH connection lost while alternate screen in use (e.g. tmux, TUI programs, pagers).
- Fixed bug where `00~` and `01~` characters could be erroneously added to user-submitted commands after SSH connection lost.

---

## 2024.05.16 (v0.2024.05.14.08.01)

### New features
- Team admins can make teams discoverable to colleagues from same custom email domain. Configure in `Settings > Teams`.

### Bug fixes
- Prompt and command no longer overlap output for multi-line commands in Bash versions earlier than 4.4.

---

## 2024.05.09 (v0.2024.05.07.08.02)

### Bug fixes
- Vim-related settings no longer appear in Command Palette when editing with Vim keybindings disabled.
- Warp's Input Editor immediately reflects any changes to Vim status bar settings.
- Fixed bug when handling URLs with parentheses in notebooks and Warp AI.

---

## 2024.05.02 (v0.2024.04.30.08.02)

### Bug fixes
- In Notebooks, code block menus no longer overlap with rich text menus.
- Fixed issue causing Warp to display invisible/empty window.
- Fixed crash when unindenting multiple lines within Input Editor.
- Fixed Vim Mode bug when "cutting word left" while up-arrow history menu open.
- \[Linux] Fixed flicker on Intel UHD 620 drivers when using Vulkan.
- \[Linux] Fixed regression in input latency.

---

## 2024.04.18 (v0.2024.04.16.08.02)

### Improvements
- Navigate and expand folders in Warp Drive with left/right arrow keys.

### Bug fixes
- Middle-click works even when mouse within prompt area.
- Already-open notebooks no longer open in new tab.
- Fixed issue where autocd completions incorrect for file paths starting with `~`.
- Opening Workflow through link focuses it even while in trash view.
- Fixed bug handling carriage returns in notebooks, markdown viewer, Warp AI.

---

## 2024.04.11 (v0.2024.04.09.08.01)

### Improvements
- Improved Warp's prompt performance for large repositories.
- When switching panes directionally, Warp automatically selects most recently focused pane in that direction.

### Bug fixes
- Fixed pane management bug where dragging pane to new location wouldn't initiate drop option.

---

## 2024.04.04 (v0.2024.04.02.08.02)

### New features
- Notebooks in Warp Drive. Create and share interactive runbooks with your team. [Learn more](https://www.warp.dev/blog/notebooks-in-warp-drive)

### Improvements
- Export workflows and notebooks from Warp Drive.
- Middle-clicking to paste automatically focuses Input Editor.
- Warp no longer automatically expands aliases escaped using backslash.
- \[Linux] Added support for Android Studio, DataGrip, DataSpell, Goland, Pycharm, Rider, Rubymine, Sublime Text as external editors.

### Bug fixes
- \[Linux] Warp case-sensitively parses top-level commands on Linux.
- \[Linux] Fixed issue where middle-click paste could paste across multiple panes.

---

## 2024.03.21 (v0.2024.03.19.08.01)

### Bug fixes
- Symlinks to directory properly treated as directory.
- \[Linux] Warp's windows no longer escalated into urgent state in tiling window managers after Warp URL opened.

---

## 2024.03.14 (v0.2024.03.12.08.02)

### Improvements
- Warp supports primary selection protocol for paste with middle click.
- Filter out unwanted lines from block using "invert filter" toggle in block filtering menu.
- Continuous block selections rendered with single border.
- `\b` and `^` patterns supported in Warp's regex search.
- \[Linux] Hotkey window has unique instance name on X11.

### Bug fixes
- "Copy on Select" works within alt-screens.

---

## 2024.03.07 (v0.2024.03.05.08.02)

### Improvements
- Adjust number of lines mouse wheel scrolls. Configure in `Settings > Features > General > Lines Scrolled by Mouse Wheel Interval`.
- Close Warp window using Command Palette (`Shift+Cmd+W` for Mac).
- Quit Warp using Command Palette.
- \[Linux] Warp can automatically hide window's traffic lights when using tiling manager.
- \[Linux] Improved rounded corners when using tiling manager.
- \[Linux] Move tabs left/right using keyboard shortcuts. `Shift+Ctrl+PageUp` to move tab left, `Shift+Ctrl+PageDown` to move right.

### Bug fixes
- Fixed bug where Warp could crash due to invalid Vim command.
- \[Linux] Fixed bug where errors running `pacman-key` could lead to invalid pacman repository configuration.

---

## 2024.03.05 (v0.2024.03.05.08.02)

### Improvements
- Improved Warp's appearance and behavior when running in some tiling window managers.

### Bug fixes
- Fixed crash when dragging mouse.

---

## 2024.02.29 (v0.2024.02.27.08.01)

### Improvements
- Added completion support for `dnf`.
- Configuring global hotkey window settings (Quake Mode) updates window in real time.
- \[Linux] `Ctrl+Click` to open file.
- \[Linux] Added support for IntelliJ, CLion, Webstorm, PhpStorm.

### Bug fixes
- Fix issue with typeahead commands overlapping prompt's content.
- Command X-Ray recognizes builtins and functions; hover over command in Input Editor to see description.
- Fixed issue where shell couldn't accept pasted text when rc file expected user input.
- \[Linux] Modified pacman-key invocation during Arch Linux auto-update.
- \[Linux] Fixed crash if device missing symlink from libX11.so to libX11.so.6.
- \[Linux] Fixed issues where opening external links would cause Firefox 123 to use 100% CPU.
- \[Linux] X11 Users can open links when default browser is Firefox.
- \[Linux] Fix some global hotkey combinations crashing app.

---

## 2024.02.26 (v0.2024.02.20.08.01)

### New features
- Warp is now available for Linux!

### Improvements
- Completions for apt-get, aptitude, pacman.
- Search fonts in font picker in `Settings > Appearance`.

---

## 2024.02.16 / 2024.02.14 (v0.2024.02.14.15.46)

### New features
- Warp on Linux (Private Beta): Added support for Input Mode Editor (IME).

---

## 2023.02.08 (v0.2024.02.13.08.02)

### Bug fixes
- Fix inputted command sometimes overlapping rprompt.

---

## 2023.02.01 (v0.2024.01.30.16.52)

### Improvements
- Improved UX for pasting auth token to complete sign-in flow.
- Subversion (svn) information available in Warp's prompt.

---

## 2023.01.18 (v0.2024.01.16.16.31)

### New features
- Warp on Linux (Private Beta): System fonts load as expected.

### Bug fixes
- Warp on Linux (Private Beta): `Alt+Tab` no longer incorrectly inserts 4 spaces into Input Editor.

---

## 2023.01.11 (v0.2024.01.09.08.02)

### New features
- New workflow metadata for shared workflows in Warp Drive. Hover over workflow to see execution recency, last editor, last edited date.

---

## 2023.12.21 (v0.2024.01.02.08.02)

### Improvements
- Toolbelt displayed when hovering over background Blocks has solid background.

### Bug fixes
- Markdown Viewer respects start number of ordered lists.
- Completing path with tilde (`~`) character works as expected.
- Fixed issue where Warp could quit before saving changes to Warp Drive.
- Fix Warp hanging when using 'Insert into Input' context menu action.

---

## 2023.12.14 (v0.2023.12.12.08.02)

### New features
- Editing with Vim keybindings now out of beta and generally available. Warp detects vi mode in shell settings and suggests Vim keybindings.

### Improvements
- Use `Cmd+F` to search text in Markdown Viewer.

### Bug fixes
- Block hover buttons have solid background when overlapping with prompt.
- Block filter editor has clear button.
- `J` and `K` (Vim Mode) for navigation within multi-line command.
- Fixed left alignment of tab bar in full-screen mode on macOS.
- Fixed triple-click selection when filtering Block.
- Fixed potential crash when using find bar.
- Fixed potential crash when retrieving accessibility contents.
- Fix bug where "R" erroneously inserted into input in zsh sessions.

---

## 2023.12.07 (v0.2023.12.05.08.02)

### Improvements
- Markdown file links configurable to open with default external editor or Warp's built-in markdown viewer.
- Warp Drive folders keep opened/closed state through app restarts.

### Bug fixes
- Input Editor refocuses correctly after pasting terminal contents and running command.
- Fixed issue with missing toolbelt buttons when using fish with Vim Mode.

---

## 2023.11.30 (v0.2023.11.28.08.02)

### Improvements
- Warp's custom prompt builder includes context chip for Kubernetes context.
- Improved completions for kubectl including resource, global options, namespaces.

### Bug fixes
- Fixed UI bug in workflows editor where editor for arguments overflowing.
- Search bar focuses as expected when opening Launch Configurations with Command Palette.

---

## 2023.11.16 (v0.2023.11.14.08.02)

### Bug fixes
- Informational block showing workflow metadata resizes with Warp window.
- Scrolling speed standardized across Warp.

---

## 2023.11.09 (v0.2023.11.07.08.02)

### New features
- New Markdown Viewer: Open `.md` files and run shell commands within them.
- Block Filtering: Filter block output (`Shift+Opt+F`) to find matching lines.

### Improvements
- Removed workflow button from toolbelt section (still accessible through right-click menu and `Cmd+S`).
- Improved performance of Warp Drive team and state syncing.

---

## 2023.11.02 (v0.2023.10.31.08.03)

### Improvements
- Invite new team members to shared Warp Drive by email address and revoke invitations.

---

## 2023.10.23 / 2023.10.19 (v0.2023.10.17.08.03)

### Improvements
- Indicators in tab bar when current pane maximized (full-screen icon) and when command exits with error.
- Git context chip shows commit hash instead of "HEAD" when in detached state.
- Easier to add and remove allowlisted domains when inviting teammates to Warp Drive.
- Menu option for copying workflow command to clipboard.

---

## 2023.10.12 (v0.2023.10.10.08.06)

### Improvements
- Warp can support macOS's proxy settings.
- Toggle whether to render Warp using integrated GPU for dual GPU Macs.
- Warp escapes file path of executable loaded from Finder.

### Bug fixes
- Fixed crash on startup for some users on macOS Sonoma.
- Workflow info box refreshes when edited.

---

## 2023.10.05 (v0.2023.10.03.08.03)

### New features
- Use Vim keybindings to edit text on command line. Navigate to `Settings > Features > Editor` and enable "Edit commands with Vim keybindings." (Beta)

### Improvements
- Admins control whether team invite link accessible for other team members to copy and share.
- Add 24-hour timestamp to Warp prompt with context chips in prompt editor.
- Free preview for Warp AI and Warp Drive for teams extended. [Learn More](https://www.warp.dev/blog/free-preview-extended)

---

## 2023.09.28 (v0.2023.09.26.08.09)

### New features
- Set Cursor as default code editor under `Settings > Features > General`.

### Improvements
- Enhanced user accessibility by adding tab bar button as new entry point for command palette.
- Improved user guidance by displaying warning when attempting to run workflow while another command in progress.

### Bug fixes
- Resolved issue where autosuggestions not being inserted when bound to certain keybindings.
- Fixed bug affecting Input Method Editor functionality on non-English keyboards.

---

## 2023.09.14 (v0.2023.09.19.08.04)

### New features
- Edit keybindings to scroll up and down by one line.

### Improvements
- Input editor remains visible in inactive panes when using split panes.

### Bug fixes
- Resolved regression where filled bookmark icon didn't display on bookmarked blocks unless hovered on.
- Fixed `Tab` key not cycling through fields in Workflow editor.
- Restored functionality of keybinding for "New Tab" to work even when no windows open.

---

## 2023.09.07 (v0.2023.09.06.18.09)

### Improvements
- New tab keyboard shortcut (`Cmd+T` by default) now re-mappable.
- Warp Drive shows loading indicator when syncing.

### Bug fixes
- Command timestamp tooltip no longer hidden when Input Editor pinned to top.

---

## 2023.08.31 (v0.2023.08.29.08.04)

### Improvements
- Delete custom themes from Warp UI.
- Scroll to top or bottom of selected block from Command Palette.

### Bug fixes
- Fixed issue where CPU used up by git processes.
- Fixed Zsh bug where `set sh_word_split` could break Warp's bootstrapping.

---

## 2023.08.24 (v0.2023.08.22.08.03)

### New features
- Secret Redaction - Warp automatically redacts secrets and sensitive information in terminal output (passwords, IP addresses, API keys, PII). Enable from Command Palette or `Settings > Privacy > Secret Redaction`.

### Improvements
- Special keys with `META` (e.g. `Meta+Delete`) work within alt-screen.
- Line height for text within Input Editor changes when custom height in `Settings > Appearance > Text > Line Height` updated.
- Alias abbreviations in fish no longer show red error underline.
- Reduced bottom padding within Input Editor when Warp in Compact Mode.

---

## 2023.08.17 (v0.2023.08.15.08.03)

### New features
- Warp displays richer metadata for each command in history (exit code, working directory, git branch, workflow status).
- Warp's native prompt customizable with drag-and-drop Context Chips (`Settings > Appearance > Prompt`).

### Improvements
- Warp supports xterm's escape codes for focus reporting.
- Command Palette searches workflows with Warp Drive folder name.
- Auto-generating custom themes from starting images works even with missing `~/.warp/themes` directory.
- "New Workflow" modal supports more text for longer commands.

---

## 2023.08.10 (v0.2023.08.08.08.04)

### New features
- Automatically create new themes based on background image! Click `+` in theme picker or search "Open Theme Picker" in Command Palette.

### Improvements
- Warp Drive workflows and folders sortable alphabetically and by last updated.
- Multiple JetBrains IDEs supported as external editors.
- Command Palette shows which folders a Workflow is in (breadcrumbs).
- Aliases like `...` and `....` no longer incorrectly have error underline.

---

## 2023.08.03 (v0.2023.08.01.08.05)

### New features
- Reopen closed tabs with `Shift+Cmd+T` for up to one minute. Configure in `Settings > Features > Enable reopening of closed sessions`.
- Auto-generate descriptions for Workflows in Warp Drive using Warp AI.

### Improvements
- Nested folders in Warp Drive collapsible all at once.
- Fixed issue where fish abbreviation expansion would include comments.
- Fixed regression with fish history becoming inaccessible.

---

## 2023.07.27 (v0.2023.07.25.08.03)

### Improvements
- Fixed issue where `$PATH` could be overwritten in Bash subshells.
- Fixed issue where completions for file-paths broken when using Named Flags (e.g. `ls --color=auto`).
- Fixed issue where Warp Drive objects could get stuck in sync state.
- Down arrow correctly moves cursor within Warp AI's text editor.

---

## 2023.07.20 (v0.2023.07.18.08.03)

### New features
- Configure whether `Tab` accepts autosuggestions or opens completions menu via `Settings > Features > Editor`.
- Improved completions behavior with better common prefix detection, case sensitivity.
- Natively draw some Unicode block element characters instead of using font glyphs.
- Warp's Resource Center displays new features and improvements.

### Improvements
- Increased maximum blur radius from 18 to 64.

---

## 2023.07.13 (v0.2023.07.11.08.03)

### New features
- Warp Drive items that failed to sync can be retried.
- Workflows in Warp Drive can be edited with workflow execution modal.

### Improvements
- Fixed bug where git information could sometimes be missing from prompt.
- Adjusted colors throughout Warp — replaced gradients with solid colors.

---

## 2023.07.06 (v0.2023.07.04.08.03)

### New features
- New AI Command Search experience translates natural language to shell commands, integrates with workflows! Type `#` in input to try.

### Improvements
- Fixed bug where Warp not recognizing some single character commands and aliases.
- Fixed bug where command output sometimes cut off after finishing.
- Fixed bug where two prompts could appear for remote Bash sessions.

---

## 2023.06.29 (v0.2023.06.27.19.34)

### New features
- App links `warp://launch/<launch_configuration_name>` open launch configuration directly.
- New setting for creating windows with specific size in rows and columns.

### Improvements
- Fix rendering of multiple ANSI styles on same character (fixes Vim and emacs rendering).
- Fix tabs sometimes inserted into Input Editor when completions menu should open.
- Added tooltip for "New tab" button.
- "Launch Configurations" sub-menu updates dynamically.
- Find bar matches double-width unicode characters including CJK and emojis.
- Fixed crash when pasting command in workflow editor.

---

## 2023.06.20 (v0.2023.06.20.08.04)

### New features
- Bring Powerlevel10k (P10K) prompt to Warp! Need latest version of P10K.
- Right-side prompts supported in Zsh and fish.
- Warp AI commands can be executed as workflows.

### Bug fixes
- Clicking on inactive Warp window focuses underlying pane correctly.

---

## 2023.06.08 (v0.2023.06.13.08.03)

### New features
- Settings page for upgraded referral system with new swag options.
- Right-click highlighted file path to show in Finder.
- Command Palette searches through Warp sessions, actions, launch configurations.

### Bug fixes
- Completions menu supports fish abbreviations.
- Fixed issue where certain aliases incorrect after expansion.
- Fixed command search ignoring extra whitespace.
- Restored background Blocks no longer create blank history entries.
- Fixed issue where enabling "Open completions as you type" could break path completions.
- Fixed issue where Zsh could fail to bootstrap when `$PATH` in bad state.
- Fixed issue where Warp's bootstrap logic could leak into Zsh's history.
- Fix properly underlining hyperlinks in lists or spanning multiple lines.

---

## 2023.06.01 (v0.2023.05.30.08.03)

### New features
- Right-click New Tab (`+`) button to select saved Launch Configurations.
- Page Up/Down in Command Palette for faster navigation.
- Added support for Zed as default code editor.
- Referral counts updated to only include referrals who've onboarded.

### Bug fixes
- Quake Mode window properly retains size.
- Fixed issue where command output temporarily cut off when resizing Warp.
- Fixed Sticky Command Header covering content for pager commands.
- Fixed tabs showing stale text when renamed.
- Clicking Mac menu bar item with sub-menu no longer incorrectly closes menu.
- Warp automatically focuses shortcut search bar when keyboard shortcuts pane opened (`Cmd+/`).
- Fixed regression where Warp's native prompt no longer showed virtual environment.

---

## 2023.05.25 (v0.2023.05.23.08.05)

### Bug fixes
- Improved shell startup performance after system restarts for users with Xcode installed.
- Fixed issue with Warpifying pipenv shell subshell from zsh.
- Fixed issue with updating git status prompt indicator in remote subshells.

---

## 2023.05.18 (v0.2023.05.18.01.08)

### New features
- Warp supports subshells in Zsh, Bash, fish. Configure commands to "Warpify" under `Settings > Subshells`.

### Bug fixes
- Fixed issue with Warp's completions when using flags starting with single dash (e.g. `-namespace`).
- Fixed issue with Synchronized Inputs where switching from alt-screens focused incorrect terminal session.
- Fixed issue where command history suggestions could cause Synchronized Inputs to get out of sync.

---

## 2023.05.11 (v0.2023.05.09.08.03)

### New features
- Warp sends output of background shell processes into new (distinct) Blocks.
- Synchronize (broadcast) input across multiple panes in single tab or multiple tabs (`Mac Menu > Edit > Synchronize Inputs`).
- Option to enable audible terminal bell (disabled by default). Configure in `Settings > Features > Terminal`.
- New windows open with same position and size as most recently closed window.
- Fish aliases supported in completions menu.

### Bug fixes
- Support `Shift+Up` and `Shift+Down` within alt-screen editors.
- Fixed incorrect alt-screen scrolling behavior with scroll reporting enabled.
- `Shift+Tab` correctly sends ANSI backward-tab escape sequence.
- SSH wrapper loads `/etc/profile` and supports login-like prompts and MOTD.

---

## 2023.05.04 (v0.2023.05.02.08.03)

### New features
- Indicate when Warp downloading update in `Settings > Account > About Warp`.
- Support alias expansion for bash/zsh aliases.

---

## 2023.04.27 (v0.2023.04.25.08.05)

### New features
- Support for Fish abbreviations.
- Right-click within Input Editor to open context menu (split panes, etc.).

### Bug fixes
- Starting command with whitespace in Workflow creation dialog no longer breaks argument parser.
- Fixed bug when commands aliased to `comm` due to naming clash with Warp's wrapper.
- `Cut word left` (`Ctrl+W`) and `Cut word right` (`Opt+D`) use shell clipboard.

---

## 2023.04.13 (v0.2023.04.11.08.03)

### New features
- Navigation by subword within Input Editor with `Ctrl+Opt+Left` and `Ctrl+Opt+Right`.
- View prior Warp AI questions using `Up` arrow even after transcript cleared.

### Bug fixes
- Fixed bug in proxied SSH while not on default shell.
- Background blur applies to windows opened via drag-and-drop from Finder.
- Sticky Command Header no longer cuts off text for pagers.

---

## 2023.04.06 (v0.2023.04.04.08.03)

### New features
- Configure position of input and direction of terminal output. Configure in `Settings > Appearance > Input Position`.
- Button for "jumping to bottom" of hovered Block. Configure in `Settings > Appearance > Blocks`.
- Warp AI transcripts navigable via keyboard (`Up`/`Down` arrows).
- Right-click context menu in alt-screen (respects mouse reporting and SGR_MOUSE).
- Past prompts accessible via `Up` in Warp AI.
- `Cmd+Enter` within Warp AI inputs selected command into Input Editor.

### Bug fixes
- Workflows searchable by description in Command Search.
- Consolidated "Ask Warp AI" keybindings into one.
- Fixed issue causing "Move cursor by word" and "Select left/right by word" to not work if "Left/Right Option key is Meta" enabled.
- Unset cursor navigation bindings within executing command.

---

## 2023.03.30 (v0.2023.03.28.08.03)

### New features
- Warning if known-incompatible custom prompt detected.
- Keybindings for cursor navigation in REPLs and subshells (e.g. `⌥←`, `⌥→`, `⌥⌫`, `⌘←`, `⌘→`, `⌘⌫`, `⌘fn⌫`).

### Bug fixes
- Fixed issue where input suggestion tooltip could overflow outside visible window.
- Fixed keybinding conflict with Warp AI.
- Fixed completion and syntax highlighting when local paths contain separators not in prefix.

---

## 2023.03.23 (v0.2023.03.21.08.02)

### New features
- Added VSCode Insiders as supported code editor.
- Added completions for pnpm.

### Bug fixes
- Fixed issue where AI command results with multiple commands all render on same line.
- Configurable width of Universal Search persists (doesn't reset in new sessions).
- "Copy Prompt" correctly respects PS1 prompt if enabled.
- Fixed automatic command corrections for cargo.

---

## 2023.03.20 (v0.2023.03.14.08.03)

### New features
- Added support for configuring which shell Warp uses. Configure under `Settings > Features > Session`.
- Tabs can be renamed via mouse double-click.

### Bug fixes
- Launch configuration templates support use of `~` in `cwd` field.
- Double-clicking button/tab in title bar no longer resizes whole window.
- Context menus in blocklist more pronounced and easier to dismiss.
- Increased clickable area of small search boxes.
- Keyboard shortcut can be registered to clear all blocks.
- Fixed locale-related issues due to use of `LC_ALL` environment variable.
- Xterm escape code OSC 4 no longer crashes app when in PS1.
- Fixed crash when resizing windows after dismissing notification banner.
- Fixed crash if keybinding for keyboard shortcuts side panel unset.
- Added Warp AI to resource center.

---

## 2023.03.16 (v0.2023.03.07.08.02)

### New features
- Introducing Warp AI ⚡ Get explanations for errors and outputs, ask for help with complicated workflows and scripts, execute suggested commands — all without leaving Warp!

---

## 2023.03.09 (v0.2023.03.07.08.02)

### New features
- Added support for clearing keybinding for action.
- Added support for showing/hiding Warp windows with system-wide Activation hotkey.
- Improved scroll speed for Sidebar menu 'Warp Essentials'/'Keyboard Shortcuts'.
- Set custom keybinding to open completions menu.
- Enabling/disabling mouse reporting no longer bound to `Cmd+R` by default.
- Toggling mouse reporting enabled shows banner.

### Bug fixes
- Fixed SSH wrapper hanging forever when SSH host is Arch Linux with latest bash package.
- Fixed Bash commands having escape codes in last 20 characters producing incorrect output.
- Fixed bug with bash prompt expansion on recent macOS versions.

---

## 2023.02.28 (v0.2023.02.28.08.03)

### New features
- Warp suggests URL for creating GitHub PR on `git push`.
- Command Search and Workflow menus horizontally resizable.

### Bug fixes
- Fixed bug where Warp doesn't correctly Auto-Raise.
- Fixed issue where formatting lost when pasting into nano.
- Fixed issue where Warp doesn't detect process termination when exiting `info`.
- Fixed bug with bash prompt expansion not working on v4.4 or earlier.
- Fixed bug where profile pictures don't show in Account menu.
- Fixed Syntax Highlighting and Error Underlining's handling of multi-byte characters.
- Fixed issue where 'Checking for Update' doesn't reflect current status.

---

## 2023.02.23 (v0.2023.02.21.08.03)

### New features
- Support for configuring initial working directory for new sessions. Configure in `Settings > Features > Session`.

### Bug fixes
- Warp supports syntax highlighting and error underlining for multi-line inputs with multibyte characters.
- Fixed bug where update status in Warp's About Section was incorrect.
- Improved GPU memory consumption when multiple windows open.

---

## 2023.02.16 (v0.2023.02.14.08.05)

### New features
- Improved double-click selection. Smart selects patterns like file paths, URLs, email addresses.

### Bug fixes
- Warp no longer hangs after exiting alt-screen having searched using Find.
- Block-list scrolls to correct position after returning from alt-screen.
- Clicking above scroll-bar no longer incorrectly changes scroll position.
- Terminal cell dimensions update immediately after modifying Font size.
- Hyperlinks no longer incorrectly highlight on hover when Warp not focused.
- Input Method Editor (non-English keyboards) correctly positioned in alt-screen and running Blocks.
- When no windows open, clicking `New Tab` from Mac menu creates new window.

---

## 2023.02.09 (v0.2023.02.07.08.03)

### Bug fixes
- Warp sets Mac window title; right-click on dock icon shows name of active tab.
- Fixed bug where navigating theme picker with arrow keys leads to crash when no theme matches search.
- Input Editor refocuses correctly after clicking hyperlinks.
- Custom keybindings incorporating `SPACE` key persist after closing Warp.
- Input Method Editor (non-English keyboards) positions correctly within Input Editor.

---

## 2023.01.26 (v0.2023.01.24.08.03)

### New features
- Warp can dim inactive terminal panes. Navigate to `Settings > Appearance > Panes > Dim inactive panes`.

### Bug fixes
- Fixed crash when selecting multiple occurrences of multi-byte characters using `Ctrl+G`.

---

## 2023.01.19 (v0.2023.01.17.08.03)

### New features
- Copy current Git branch using Command Palette (`Cmd+P`).

### Bug fixes
- Fixed bug where some keybinding actions applied to wrong terminal pane.
- Warp checks input values for font size and line height and ignores if too small or large.
- "Missing update permissions banner" can be dismissed.
- Fixed rare crash when closing panes created by launch configuration.

---

## 2023.01.12 (v0.2023.01.10.08.02)

### New features
- Support setting window background transparency and blur radius via `Settings > Appearance`.
- Revamped resource center! Click Warp icon in top right for keyboard shortcuts and documentation.
- Quit modal: Quitting or closing Warp while session running triggers warning prompt with view of running sessions.
- Toggle to disable cursor blinking.

### Bug fixes
- Support completions with escaped paths.
- Support background images with paths starting with `~`.
- Properly restore Warp window's position when using multiple monitors.
- Commands from restored sessions run on local machine no longer appear in SSH server's history.
- Fixed issues SSHing into RHEL/Fedora machines with PackageKit-command-not-found installed.
- Fixed incorrect handling of `->` as user's prompt.
- Fixed ls completions when using `--color` option.

---

## 2023.01.05 (v0.2023.01.03.08.03)

### Bug fixes
- Trailing periods no longer considered part of URL.
- Fixed regression where "autocomplete symbols" setting not respected.

---

## 2022.12.15 (v0.2022.12.13.08.04)

### New features
- Reorder and drag tabs around with mouse!

### Bug fixes
- Welcome Block works when using Fish shell.
- AI Command Search no longer crashes from multi-byte characters when opened via `#` prefix.
- Warp no longer crashes when starting new session in deleted or inaccessible directory.
- Resolved rendering bugs and hangs in full-screen applications like 'k9s' and 'less'.
- Added login failure notification.

---

## 2022.12.06 / 2022.12.02 (v0.2022.12.06.08.03)

### New features
- Opt out of telemetry (app analytics and crash reporting).
- Added 'Tail Warp network log' workflow for viewing logs of all app network activity.

### Bug fixes
- Full-screen CLI commands like mitmproxy correctly span entire view.
- Improved styling and organization of Features page in settings.
- Completions While Typing menu closes while generating new results.
- Added hidden completion result for root dir.
- Warp consumes less memory when session has many blocks.
- Fixed issue over SSH where logs inserted into input.
- Mitigated issue where running command over SSH emitted spurious output.

---

## 2022.12.01 (v0.2022.11.29.08.03)

### New features
- Find bar works within alt-screen! `Cmd+F` opens find in vim, less, other alt-screen apps!

### Bug fixes
- Respect symlinks in Warp configuration directories (themes and workflows).
- Fixed unwanted text appearing in Input Editor when RPROMPT set.
- Fixed emoji composer not working properly.
- Fixed crash when hovering over multiple byte text within Input Editor.
- Fixed "command not found: sed" and "command not found: tr" issues with SSH wrapper.
- Fixed issue where tab completions and command search could be visible simultaneously.
- Move Backward/Forward One Word bindings can be overridden.

---

## 2022.11.15 (v0.2022.11.14.14.55)

### New features
- Command Search: `Ctrl+R` opens panel to search history, workflows, command execution-related items.
- Sticky command header: Warp pins prompt/command section of Block to top of screen. Configure in `Settings > Features > Show Sticky Command Header`.
- Input Editor supports soft wrapping; long commands fully visible!

### Bug fixes
- Warp sets `TERM_PROGRAM` environment variable correctly in wrapped SSH sessions.

---

## 2022.11.10 (v0.2022.11.08.08.07)

### New features
- Command Corrections! Warp suggests corrections for errors in previous console commands.
- Warp detects invalid file paths — underlined red when error underlining enabled.
- Toggle in `Settings > Appearance` to configure minimum contrast enforcement.

### Bug fixes
- Fixed issue where toggling default prompt did not update immediately.
- Improved positioning of `Tab` completions menu when using split panes.

---

## 2022.11.03 (v0.2022.11.01.08.03)

### New features
- Warp's prompt shows number of modified files on local git branch! Toggle by searching "changed file count" in Command Palette or right-clicking Prompt.

### Bug fixes
- Dim-styled colors properly restored.

---

## 2022.10.27 (v0.2022.10.25.08.06)

### Bug fixes
- Fixed bug when hovering over hover icons.

---

## 2022.10.20 (v0.2022.10.18.08.10)

### Bug fixes
- Modifying mouse and scroll reporting settings applies immediately.
- Fixed cursor not blinking when starting shell instance.
- Fixed temporarily flashing wrong prompt while Warp bootstrapping.
- Removed duplicate entry for toggling error underlining and syntax highlighting in Command Palette.

---

## 2022.10.13 (v0.2022.10.11.08.13)

### New features
- Input Editor has Syntax Highlighting and Error Underlining, no configuration needed!
- Warp uses pointer cursor when hovering over links.

### Bug fixes
- Git branches in completions menu bold correctly.
- Warp no longer crashes when `/bin/bash` missing.

---

## 2022.10.06 (v0.2022.10.04.08.05)

### New features
- Drag and drop folder or file onto Warp dock icon to open new tab in directory.
- Dividers between Blocks in compact mode.
- Shell keywords supported for completions and Command Inspector.

### Bug fixes
- Accessibility support for context menu keybinding.
- Keystrokes typed while command executing no longer dropped.
- Link recognition no longer includes trailing quotes.
- Find search results continue to be highlighted after clearing screen during long-running command.
- Fixed completions for commands prefixed with environment variables.
- Warp's resource center center aligned.

---

## 2022.09.29 (v0.2022.09.27.08.11)

### New features
- Extend selected text within Blocks with `Shift+Left`, `Shift+Right`, `Shift+Up`, `Shift+Down`.
- Double-click and drag to select text in Input Editor.
- Insert last word of previous command with `Meta+.`.
- Toggle to enable mouse and scroll reporting in `Settings > Features`.

### Bug fixes
- `clear` command no longer appears in snackbar at top of window.
- Completions support executables in remote sessions.
- Fixed subcommand completions for commands with proper prefixes.
- Completion spec for `lsd` supports files.

---

## 2022.09.22 (v0.2022.09.20.08.08)

### New features
- Press `Ctrl+M` to open context menu for selected Block.
- Execute commands in tab completions menu and history menu directly with `Cmd+Enter`.
- Completions support shell builtins, git aliases, npm aliases.

### Bug fixes
- Command Palette includes most useful features at top.
- Improved flag completions for cargo.

---

## 2022.09.15 (v0.2022.09.13.08.15)

### New features
- Warp Resource Center — explore Warp features and documentation via `?` icon or `Shift+Ctrl+?`.
- New icons in completion menu denoting flags, folders, branches, etc.

### Bug fixes
- Press `Cmd+Enter` within history menu to directly execute highlighted command.
- Fixed crash when opening many tabs.
- Fixed crash when laying out RTL text.

---

## 2022.09.08 (v0.2022.09.07.14.56)

### New features
- Global hotkey window can float above full-screen apps.
- Tabs can have color customized via right-clicking.
- Terminal line height configurable via `Settings > Appearance`.

---

## 2022.09.01 (v0.2022.08.31.18.11)

### New features
- Tab completions support fuzzy string matching.
- Improved completions for over 450 commands (docker, kubernetes, cargo, node, git).

### Bug fixes
- Properly send C0 control codes for `<ctrl+[2-8]>` keystrokes.
- Session restoration persists bold, underline, italic, strikethrough formatting.
- Inspect mode works for changelog modal.
- Fixed crash when highlighting link.
- Fixed Find occasionally returning only partial results.
- Fixed occasional crash when loading images.
- Fixed display issue in Mac Menu for keyboard shortcuts with special keys.

---

## 2022.08.25 (v0.2022.08.23.08.06)

### New features
- Experimental feature: always-on completions. Enable via `Settings > Features`.

### Bug fixes
- Custom tab titles no longer overwritten when using multiple panes.
- Block's execution duration formatted in hours, minutes, seconds.
- Improved rendering of 'Current session' text in Navigation Palette.
- Warp properly hides cursor when CLI sends respective escape sequence.
- Warp stays focused after closing Share Block menu and context menu.
- Warp no longer lags when `Ctrl-R` menu opened.
- Confirming tab suggestion appends space to buffer.

---

## 2022.08.18 (v0.2022.08.16.10.16)

### New features
- Launch Configurations — save configuration of windows, tabs, panes to open later with `Ctrl+Cmd+L`.
- Session Navigation — navigate to any session in Warp with `Shift+Cmd+P`.
- Added exclusive theme for users who joined Warp through referral.

### Bug fixes
- Prompt shows Git SHA instead of HEAD when not on a branch.
- Filepath completions include current directory ('.') and parent directory ('..').
- Support `Shift+Home` and `Shift+End` keybindings to select text to line start and end.
- Items in Command Palette highlight when hovered.
- Improved how Warp cleans up warptmp directory for Zsh SSH sessions.
- Already open dropdown menus properly closed when clicked.
- Warp no longer crashes when dragging window running htop.
- Warp no longer crashes when find bar open.

---

## 2022.08.10 (v0.2022.08.08.09.21)

### New features
- Middle-click tab to close it.
- Additional tab reordering options via Mac Menu, Command Palette, tab's context menu.

### Bug fixes
- Toggle for maximizing panes in Mac Menu.
- Switch panes using keyboard shortcuts even when pane maximized.
- Support for opening file paths with RubyMine, PhpStorm, WebStorm.
- Fixed crash when highlighting links.
- Fixed issue where `HISTCONTROL` environment variable ignored in bash.
- Pressing `Ctrl+R` to open history search no longer crashes Warp with multiple cursors.

---

## 2022.08.03 (v0.2022.08.01.09.12)

### New features
- Updated Mac menus to make Warp actions more discoverable.
- Warp supports opening file links and URLs via `Cmd+Click`.

### Bug fixes
- Various CLI tools no longer hang (Bazel, Maven).
- Command Inspector hover no longer crashes with UTF-8 encoded strings.
- Opening find/search bar (`Cmd+F`) automatically selects text.
- Tab titles no longer reset when changing panes.

---

## 2022.07.27 (v0.2022.07.25.09.05)

### Bug fixes
- Closing and re-opening Command Palette resets selected item.
- Cursor's position restored after exiting Command History Search (`Ctrl+R`) menu.
- Shorthand and longhand flags correctly surfaced in tab completions.
- Added voiceover support for `Backspace` and `Delete` keystrokes within Input Editor.

---

## 2022.07.20 (v0.2022.07.18.09.06)

### New features
- Command Inspector — hover over any piece of command in Input Editor to surface documentation or press `Cmd+I` to inspect at cursor location.
- Improved ordering in tab completions menu.

### Bug fixes
- Font color for links in light mode (themes) set correctly.
- Moving forward by word no longer moves farther than expected.
- Warp no longer hangs when passing invalid file path.
- Fixed issues with persisting selected theme when "Sync with OS" enabled.
- Fixed issues with text input after clearing Blocks (`Cmd+K`) while in REPL environment.
- Fixed shortcut for select-left-by-word, select-right-by-word, select-line-to-end, select-line-to-start.

---

## 2022.07.13 (v0.2022.07.11.09.11)

### Bug fixes
- Improved startup time for Fish shells.
- Find Bar no longer crashes on selected text.
- Scrollbar supports jumping to where clicked.
- Fixed bug with referral link for sharing Warp not loading.

---

## 2022.07.07 / 2022.07.06 (v0.2022.07.04.09.08)

### New features
- Bookmark Block for quick access via scroll-bar.
- Referral counter in Settings > Account screen and referral screen.
- Support for rendering text with lower visual weight. Enable thin strokes option in `Settings > Appearance` (default for low-DPI displays).
- Togglable settings, overflow menu items, settings pages accessible through Command Palette.
- CLI options surfaced by default without needing to type '-'.
- Press `Shift+Cmd+C` in VSCode to open new Warp session.

### Bug fixes
- Fixed referral links and share by email.
- Fixed hang when connecting with SSH.
- Support requesting media permissions (camera, audio, etc).
- Correctly parse Git commit SHAs in completion menus.
- Improved tab completion support for arguments behind flags.

---

## 2022.06.29 (v0.2022.06.27.09.14)

### Bug fixes
- Cursor changes when hovering over clickable UI elements and Input Editor.
- Dim colors render correctly.

---

## 2022.06.27 / 2022.06.22 (v0.2022.06.20.09.15)

### New features
- Improved auto-focus behavior when closing panes by keeping track of history when navigating or clicking around panes.
- Performance improvements when executing Blocks: Warp no longer flashes on every command!

### Bug fixes
- Input Editor re-focuses after renaming tab.
- Reduced visual weight of active tab title for improved legibility.
- Improved blending along inside edge of rounded corners.
- Global Hotkey Window (Quake Mode) correctly respects active screen setting.
- Completions for flag arguments support absolute and relative file paths.
- Git checkout `<TAB>` completes branches with remote prefixed.
- Pressing `Arrow-up` when Input Editor non-empty opens command history with prefix filtering.
- Button to copy app version moved to main settings page.

---

## 2022.06.17 / 2022.06.15 (v0.2022.06.13.09.15)

### New features
- Keyboard shortcuts to reorder tabs (`Ctrl+Shift+Left` and `Ctrl+Shift+Right`).

### Bug fixes
- Warp no longer crashes on macOS 13 (Ventura).
- Global Hotkey Window no longer overlaps Spotlight, Raycast, Alfred, macOS Dock.
- Correctly display user and hostname in Prompt after exiting SSH session.
- Fixed memory leak on window close.

---

## 2022.06.08 (v0.2022.06.06.09.05)

### New features
- Rename tabs via right-click on tab title.
- Enable custom prompt from prompt context menu.
- Split panes (left and right) via context menu and Command Palette.
- `Ctrl+Click` as alternative to right-clicking.

### Bug fixes
- Improved completions support for arguments nested under options.
- Modified files included in addition to commit SHAs for `git diff`.

---

## 2022.06.01 (v0.2022.05.30.09.10)

### New features
- Added information about rewards to referral screen.
- Button to toggle regex search in Find Bar.
- Added completion support for shell functions.

### Bug fixes
- Hotfix — regression that caused Warp to stall when using nano.
- Improved kerning throughout app.
- Added hyperlink to changelog history in Changelog modal.
- Multiline commands without output no longer cut off.

---

## 2022.05.26 (v0.2022.05.23.09.07)

### New features
- Warp can send desktop notifications for long-running commands and password prompts.
- Added keybinding to toggle fullscreen mode.

### Bug fixes
- Stopped prepending `\` before `~` in tab titles for older versions of Bash.
- Added support for `Cmd+G` and `Shift+Cmd+G` to tab between results in Find Bar.

---

## 2022.05.18 (v0.2022.05.16.09.01)

### New features
- Added exclusive theme available to anyone who has referred someone to Warp. (Open Theme Picker > Warp Referral).

### Bug fixes
- Improved rendering of rounded corners throughout app.
- Fixed cell dimension computation for some fonts.
- Fixed labels rendering incorrectly in font selector dropdown.
- Fixed Bash remote sessions missing tab titles.
- Reduced UI flickering after executing commands.
- Fixed errors when sshing into remote machines without xxd available.
- Fixed some anti-aliased glyphs getting clipped during rasterization.
- Fixed search bar stealing focus after command execution.

---

## 2022.05.11 (v0.2022.05.09.09.06)

### New features
- Filepath completions without needing to cd.
- Support for any font (not just monospaced).

### Bug fixes
- Tab completions (cd) with international characters properly escaped.
- Improved rendering performance when many tabs open.
- Fixed race condition with autoupdate a11y announcements.
- Fixed regression that would cut off output of some long-running Blocks.

---

## 2022.05.04 (v0.2022.05.02.09.00)

### New features
- Added default tab titles for Bash.
- Improved default tab title in Zsh.
- Maximize a split pane.
- Support rcfiles that check PS1 to determine if interactive shell.

### Bug fixes
- History shows results after hitting Esc when Block is focused.
- Fixed crash when quitting AI Command Search while command being generated.
- Global keybindings with function keys and numeric keys properly registered.
- Warp no longer jumps up and down for single-line commands that take more than 50ms.

---

## 2022.05.02 / 2022.04.27 (v0.2022.04.25.09.59)

### New features
- Quake Mode setting for auto-hide when losing focus.
- Quake Mode setting for which screen to pin Warp on.
- Expanded keybindings supported by Quake Mode/Global Hotkey Window.

### Bug fixes
- Commands prepended with space stored in history if hist_ignore_space not set.
- Support dotfile configurations with non-English quotation marks.
- Improved reliability of login and auth within app.
- Improved performance for commands with large outputs.
- Improved performance for long running commands.
- Improved text alignment within inline banners.

---

## 2022.04.20 (v0.2022.04.18.09.08)

### New features
- Support logging into Warp by pasting auth URL when "Take me to Warp" fails in browser.

### Bug fixes
- Improved reliability of login and auth within app.
- Buttons within find bar properly shaded for gradient themes.
- Workflows with default values registered by Warp.
- Fixed bootstrapping bug affecting Fish versions older than 3.2.0.
- Fixed memory leak when new tabs opened or panes split.

---

## 2022.04.15 / 2022.04.13 (v0.2022.04.11.09.09)

### Bug fixes
- Support parsing PS1's exit codes and improved PS1 parsing for newer Bash versions (4.4+).
- Improved parsing of Zsh default prompts.
- Opening find bar automatically selects existing text.

---

## 2022.04.08 (v0.2022.04.04.09.07)

### Bug fixes
- Block sharing dialog scrolls properly.

---

## 2022.04.01 (v0.2022.04.01.01.37)

### New features
- Warm welcome!
- A.I. Command Search.

### Bug fixes
- Warp properly registers `SPACE` and `SHIFT` modifier keys for Global Hotkey Windows.
- Page Up and Page Down keys work correctly in vim and fullscreen apps.
- SSH supports bootstrapping if bash-preexec included in Debian VM's system rcfiles.
- Corrected keyboard shortcut for split pane in context menu.

---

## 2022.03.30 (v0.2022.03.29.02.23)

### New features
- Workflows: easier way to share, parameterize, execute commands.

### Bug fixes
- Magnet, Swish, ALT-Tab window managers work with Warp.
- SSH handles verbose mode, no longer leaks into Input Editor as typeahead.
- SSH boots normally for POSIX shells not supported by Warp's wrapper.

---

## 2022.03.24 (v0.2022.03.23.22.10)

### New features
- Basic screenreader support (Voiceover) — Warp is an accessible terminal!
- Toggle in settings to disable SSH wrapper.

### Bug fixes
- Hitting tab with text selection shows tab completions instead of indenting.
- SSH no longer hangs when /tmp not writable for Zsh.
- SSH no longer bootstrap shell if not meant to be interactive session.
- SSH supports Starship and Zsh's $PROMPT variable.
- Import themes in subdirectories (e.g. `~/.warp/themes/subdirectory/theme.yaml`).

---

## 2022.03.16 (v0.2022.03.14.08.49)

### New features
- Case-sensitive search.

### Bug fixes
- SSH no longer returns `0~` and `1~` after executing commands for Zsh 5.0.8 or older.
- SSH over Zsh no longer depends on configuring locales on remote machine.
- SSH sources /etc/bash.bashrc which is extra rcfile in Debian and other Linux distributions.
- Improved completions stability when multiple panes on same remote machine.
- Vim and other alt-screen apps properly expand to take up full window.
- Clicking into Warp from other foreground window focuses clicked pane.
- Warp respects ignore-space history options for Zsh and Bash.
- Warp creates `~/.warp` folder to persist custom keybindings.

---

## 2022.03.09 (v0.2022.03.07.08.51)

### Bug fixes
- Added missing actions to Command Palette.
- Option is meta now in settings menu.
- Fix for SSH hanging when Zsh is remote login shell.
- Fix for SSH with Zsh that would break with certain rcfiles because of incorrectly set ZDOTDIR.

---

## 2022.03.02 (v0.2022.02.28.08.45)

### New features
- Edit keybindings for arrow navigation (Up/Down/Left/Right).
- Edit keybindings for activating specific tabs (by number `Cmd+1`, `Cmd+2`, …).

### Bug fixes
- Crash in theme chooser.
- Fix for tab completion sometimes deleting characters.

---

## 2022.02.23 (v0.2022.02.21.08.55)

### New features
- Zsh support over SSH.
- Partially complete autosuggestion (by word) using `Ctrl+Right` and `Alt+Right`.
- Copy URL menu item after right-clicking URL.
- Indicator for conflicting keybindings in keyboard customization UI.

### Bug fixes
- Fill-in longest common prefix after filtering tab completions.
- Block completion causes Input Editor to steal focus from find bar.
- `Up-arrow` in history menu sometimes scrolls more than one item.
- `Cmd+F` opens no-op find bar in alt screen.

---

## 2022.02.16 (v0.2022.02.14.08.44)

### New features
- Customizable key bindings (accessible via settings menu).
- Opt to use shell's prompt rather than Warp's default (Honor PS1 toggle under settings menu).
- Timestamp showing Block runtime duration; hover to see start and end date + time.
- `Ctrl+E` and `Cmd+Right` accept autosuggestions when at end of buffer.
- Allow input height to expand to half pane height.

### Bug fixes
- Arrow keys cycle themes in theme picker.
- Esc keypress exits theme picker.
- `Cmd+Down` when on most recent block to focus input clears Block selection.
- Fixed bug where resizing pane while command running made it impossible to scroll to bottom of pane.
- Fixed bug where resizing pane could cause Warp to show blank screen.
- Parentheses, quotes, brackets auto-close after typing alphanumeric character.
- Remapped multi-cursor key bindings to `Ctrl+Shift+Up` and `Ctrl+Shift+Down`.
- Restored `Opt+Cmd+Up` and `Opt+Cmd+Down` for switching panes up and down.

---

## 2022.02.02 (v0.2022.01.31.09.03)

### New features
- Multi-cursor keybindings for adding cursors above and below current selections with `Opt+Cmd+Up/Down`.

### Bug fixes
- Double clicking top of window maximizes app.
- Icon, cursor, selection contrast fixes.
- Scrolling performance improvements with bg image themes.
- Changelog visual glitch.
- Resize bug — losing scroll position when viewing blocks with long output.

---

## 2022.01.26 (v0.2022.01.24.08.55)

### New features
- Auto-close symbols (parentheses, quotes, brackets) like VSCode.

### Bug fixes
- Right-clicking Block now focuses that Block.
- Mouse dragging in vim.
- Restoring history bug on session restore.
- Automatically focus last active window on session restore.

---

## 2022.01.19 (v0.2022.01.17.08.48)

### New features
- Restore block contents.
- Longest common prefix in completions menu auto-fills Input Editor.
- Right-click prompt and copy: git branch, prompt, cwd.

### Bug fixes
- Fixed bug where venv inserted into input editor.
- Improved URL detection.

---

## 2022.01.12 (v0.2022.01.10.17.24)

### New features
- Added Changelog page to documentation.

### Bug fixes
- Double clicking text in URL highlights word instead of whole URL.
- Double clicking string with underscores selects whole string not just subword.
- Selection updates correctly when block hit max line length.
- Close Command Palette using `Cmd+P`.
- Fixes tabs not opening in new windows when autoupdate pending.
- Fix regression with input box not focused on app relaunch.

---

## 2022.01.05 (v0.2022.01.03.09.07)

### New features
- Native undo and redo in text editor using `Cmd+Z`.
- Added open source licenses to Warp Documentation.
- Split pane focus indicator — triangle in top left corner of pane in focus.

### Bug fixes
- `Ctrl+Space` properly passed to Emacs and other terminal apps.
- Copy on select setting persists across sessions and does not reset after updates.

---

## 2021.12.29 (v0.2021.12.27.09.04)

### New features
- Find in block (plus other find improvements).

---

## 2021.12.22 (v0.2021.12.20.09.04)

### New features
- Windows, tabs, panes restored whenever you reopen Warp.
- Warp supports completions for over 300 commands using Fig's completion specs.
- Switch to next pane and previous pane with `Cmd+[` and `Cmd+]`.
- Copy and paste file directory into Warp from Finder.
- When last Block selected, re-focus input editor using `Cmd+Down` key.
- Arrow down scrolls to bottom of last block.

### Bug fixes
- Copying selected text to clipboard creates new entry for each selected character.
- Needed extra backspace to escape `Ctrl+R` / history menu.
- VIM performance improvements.

**Updates to Mac Menu Bar (Window)**
- Zoom
- Minimize
- Tile Window to Left of Screen
- Tile Window to Right of Screen
- Move to X screen
- Enter Full Screen
- Bring All to Front

---

## 2021.12.15 (v0.2021.12.13.08.40)

### New features
- Fuzzy search in `Ctrl+R` and Command Palette.
- Shared links to blocks allow up to 5 recipients to download Warp's beta.

### Bug fixes
- Fix bug where opening `file://` URLs would not include query params.
- More prominent highlights in `Ctrl+R`, Command Palette, tab completion.
- Vim bug fixes and performance improvements.

---

## 2021.12.08 (v0.2021.12.06.19.09)

### New features
- Added send invite button in account section of settings dialog.
- Request more invites in invite modal.

### Bug fixes
- Copy on select persistence bug.

---

## 2021.12.01 (v0.2021.11.29.18.59)

### New features
- Added 15 extra invites for everyone!
- Copy on select (highlighting text automatically copies to clipboard). Disable in settings.

### Bug fixes
- Highlight and copy sections of URL without it automatically opening.

---

## 2021.11.24 (v0.2021.11.23.17.55)

### New features
- Background images + gradients in themes. Define your own via yaml file in `~/.warp/themes`.
- Changelog dialog.
- Improved settings dialog.

### Bug fixes
- Properly escapes whitespace when dragging and dropping files.

---

## 2021.11.17 (v0.2021.11.16.20.05)

### New features
(None)

---

## 2021.11.10 (v0.2021.11.09.19.46)

### New features
- Autosuggestions: Warp suggests commands as you type, similar to Fish or Gmail.

### Bug fixes
- Conda info locking input editor.
- `Ctrl+D` deletes forward one character.

---

## 2021.11.03 (v0.2021.11.02.00.38)

### New features
- CJK (Chinese, Japanese, Korean) character support.
- Autocompletions for missing tar commands.

### Bug fixes
- Runaway memory usage from font loading on initial run.
- Directories with non-English filenames not rendering.
- App crashes from missing current working directory.
- Pure Prompt inserted as typeahead into editor.

---

## 2021.10.27 (v0.2021.10.25.22.47)

### New features
- Ability to unshare blocks in settings modal.
- Link to documentation in kebab menu.

### Bug fixes
- Double character entry after input editor loses focus.

---

## 2021.10.20 (v0.2021.10.19.21.38)

### New features
- Toggles instead of buttons in settings!
- Link to Custom themes documentation in settings.

### Bug fixes
- IME support (non-English keyboards better supported).
- Show banner when app startup takes longer than expected.
- `git log` and similar commands no longer treated as failed block.

---

## 2021.10.13 (v0.2021.10.12.19.34)

### Bug fixes
- Shell bootstrapping should be a lot faster.
- Support 3-char color representation for hex colors in theme.
- Fix crashes relating to reading history files.
- Prevent block completion from stealing focus.
- Fix broken click handling for showing and hiding overflow menu.

---

## 2021.10.06 (v0.2021.10.05.20.07)

### Bug fixes
- Split pane navigation when 'Left / Right Option is Meta' settings enabled.
- Crash when opening new window.

---

## 2021.09.29 (v0.2021.09.29.13.26)

### New features
- Split panes: create multiple panes in same tab via shortcuts, Command Palette, or right-clicking.
- Custom themes via files in `~/.warp/themes`. See [GitHub repo](https://github.com/warpdotdev/themes).

### Bug fixes
- Add better messaging when Warp does not have permission to autoupdate.
- Crash if tab completion result accepted after cursor moved to beginning of editor.

---

## 2021.09.22 (v0.2021.09.21.20.54)

### New features
- Theme picker available from Command Palette.

### Bug fixes
- Occasional crash when opening new Warp window.
- Font selection dropdown didn't respect theme choice.
- Issues with padding and hover detection when toggling Compact Mode.

---

## 2021.09.15 (v0.2021.09.14.21.25)

### Bug fixes
- Crash when closing full-screen window.
- Executables in path not appearing for completions in Bash.
- Completions menu overlaps theme picker.

---

## 2021.09.09 (v0.2021.09.09.0.0)

### New features
- New themes for Warp (Dracula, Solarized, Gruvbox)! Access via Settings.
- `Cmd+,` opens Settings menu.

### Bug fixes
- Fixed crash when failing to load font or scrolling through fonts.
- Fixed visual artifacts around windows and modals jumping.
- Fixed crash when `Cmd+F` while selecting already selected text.

---

## 2021.08.31 (v0.2021.08.31.0.0)

### New features
- Support emacs bindings in input box.
- History up menu performs prefix search based on input.

### Bug fixes
- Warp not rendering after executing long-running command.
- Stop powerlevel10k instant prompt from hanging on bootstrap.
- Changing font-size via `Ctrl+-` and `Ctrl+0` stays in sync with settings.
- Bracketed paste mode bug: `0~ ~1` on every command when ssh-ing.
- Crash when tab completing with multibyte characters.
- Download page doesn't render correctly on Safari.
- Login broken for some users using Chrome.
- Make it more prominent in onboarding that telemetry collected during beta.

---

## 2021.08.25 (v0.2021.08.25.0.0)

### New features
- Custom fonts.
- Completions for aliases and environment variables.

### Bug fixes
- Completions loose ends including paths with spaces and commands separated by `&&`.
- Function key support within running programs (such as htop).
- Editor text respects zoom level.
- Regression causing URLs not highlighted.
- Opening new window required Internet connection.

---

## 2021.08.18 (v0.2021.08.18.0.0)

### New features
- Re-run with sudo.

### Bug fixes
- Crash caused by pressing `Cmd+K`.
- Completion not working when cursor mid-line.
- Re-input of multi-line commands.
- Selection showing after closing and re-opening alt-screen.

---

## 2021.08.09 (v0.2021.08.09.0.0)

### New features
- New settings modal to set font size, toggle light/dark mode, compact/normal mode.
- `Ctrl+U` and `Ctrl+K` cut to clipboard.
- Typeahead: characters typed in long-running command show up in input box when command completes.

### Bug fixes
- Handle arrow keys with modifiers (option and command) in CLIs and full-screen apps.
- Straightening text baseline.
- Translucent colors (e.g. for diff-so-fancy) correct.
- Dotfile path completions + Completions improvements.
- Artifacts when rendering SVGs especially on low res monitors. Overflow menu looks better!

---

## 2021.07.28 (v0.2021.07.28.0.0)

### New features
- Compact Mode.
- Support for mouse events in Vim and other programs that handle mouse input.
- Completions for npm / yarn scripts.

### Bug fixes
- Major improvements to consistency of completions especially for commands with multiple arguments (e.g. `rm -rf`).
- Proper path completions for absolute paths.
- Hang when `PROMPT_COMMAND` set for shell.
- Context Menu not closing when clicking outside.
- Crashes after executing multi-line commands and on older versions of macOS.

---

## 2021.07.21 (v0.2021.07.21.0.0)

### New features
- Support for numpad ENTER.
- More npm & yarn completions.

### Bug fixes
- Down arrow sends unrecognized escape sequence to Github CLI.
- Can't use `Up` arrow if item in history is multiple lines.
- Crash when closing tab when multiple tabs.
- File-only completion signatures should also show directories.

---

## 2021.07.13 (v0.2021.07.13.0.0)

### New features
- New invite system to add users to Warp.
- URLs in terminal screen auto-linkified.
- Double-clicking title bar maximizes/minimizes window.

### Bug fixes
- Various Command Palette bugs.
- Find box populated with user's text selection.
- 3 second latency when changing prompt upon first SSHing.

---

## 2021.07.07 (v0.2021.07.07.0.0)

### New features
- Command Palette for most keyboard shortcuts (`Cmd+P`).
- Tab completion descriptions displayed in floating box.
- Switch tabs using `Ctrl+Tab` and `Ctrl+Shift+Tab`.

### Bug fixes
- Intermittent crashes with Zsh sessions and switching tabs.
- Always fall back to path suggestions for completions.
- Various bugs related to completions.

---

## 2021.06.29 (v0.2021.06.29.0.0)

### New features
- Multiple window support.
- New completions UI and inline documentation for commands and flags.
- Horizontal scrolling of input box to support long commands.

### Bug fixes
- Crash when exiting from logout or exit when background process.
- Crash when bootstrapping from detecting incorrect shell name.
- Various bugs related to completions.

---

## 2021.06.15 (v0.2021.06.15.19.04)

### New features
- Mac File and Edit menus along with Mac standard menu items.

### Bug fixes
- Crash when closing last window.
- `Cmd+F`: when no matches display 0/0.
- `Cmd+F` should not scroll away if navigating to match on same row.
- `Cmd+F`: render yellow rectangle at layer of rendering cell.
- Unable to move cursor upwards on multi-line previous command.
- Warp bootstrap commands showing up in history over SSH.
- Accept input via input box before terminal bootstrapped.
- New tab button should have hover and click state.
- Output stops midway through session on iMac running Mojave 10.14.6.
- Backspace doesn't work while holding shift.
- Clipping issue in share dialog.
- Input suggestions closes if you click on scrollbar.
- Hitting up/down while input suggestions open causes menu to move.
- Paste not working for full screen apps.
- Underline does not render with Hack font.

---

## 2021.06.09 (v0.2021.06.09.15.14)

### New features
- SSH support (Warp works the same when you SSH as locally!).
- Improved completions snappier and more intelligent for options and arguments.
- Find: `Cmd+F` brings up find view to search text in terminal.

### Bug fixes
- Text rendering was faded on certain monitors.