---
number: 29
category: guide
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/learn/best-practices.md
word_count: 856
---
# Best Practices

> **BLUF:** Core habits for effective Codex usage — strong prompts, plan first, reusable `AGENTS.md`, proper configuration, testing/review loops, MCP for external context, skills for repeatable work, automations for stable workflows, session management.

## Strong First Use: Context + Prompts

Codex works even without perfect prompts. For reliable results in large/high-stakes tasks, include four things:

| Element | What It Covers |
|---------|---------------|
| **Goal** | What to change or build |
| **Context** | Relevant files, folders, docs, errors, `@` mentions |
| **Constraints** | Standards, architecture, conventions, safety requirements |
| **Done when** | Success criteria (tests pass, behavior changes, bug fixed) |

Choose reasoning level based on task difficulty:
- **Low** — fast, well-scoped tasks
- **Medium/High** — complex changes, debugging
- **Extra High** — long, agentic, reasoning-heavy tasks

## Plan First for Complex Tasks

Use `/plan` or `Shift+Tab` to toggle plan mode. Codex gathers context, asks clarifying questions, builds plan before implementation.

Alternatives:
- Ask Codex to interview you → turns fuzzy idea into concrete spec
- Use `PLANS.md` template for multi-step/longer work (see [Execution Plans guide](https://developers.openai.com/cookbook/articles/codex_exec_plans))

## AGENTS.md: Reusable Guidance

`AGENTS.md` is an open-format README for agents — auto-loaded into context. Best place to encode team/repo conventions.

**What to include:**
- Repo layout, important directories
- How to run the project
- Build, test, lint commands
- Engineering conventions, PR expectations
- Constraints and do-nots
- Definition of done + verification steps

**Scaffolding:** `/init` in CLI → generates starter `AGENTS.md`.

**Scope hierarchy:** User (`~/.codex`) → repo root → subdirectory. More specific wins.

**Tips:**
- Keep it practical — short + accurate beats long + vague
- Reference task-specific files (review guide, architecture doc) rather than expanding main file
- After Codex makes same mistake twice, ask for retrospective → update `AGENTS.md`

## Configure for Consistency

| Layer | Path | Purpose |
|-------|------|--------|
| Personal defaults | `~/.codex/config.toml` | Sandbox, approvals, model, MCP, profiles |
| Repo-specific | `.codex/config.toml` | Shared standards |
| CLI overrides | `--` flags | One-off situations |

> All surfaces (CLI, IDE, App) share the same config layers.

Start with default permissions. Keep approval/sandbox tight by default; loosen for trusted repos once need is clear. Configure real environment early — many quality issues are setup issues.

## Testing + Review Loop

Don't stop at code generation. Ask Codex to:

- Write/update tests for the change
- Run relevant test suites
- Check lint, formatting, type checks
- Confirm behavior matches request
- Review diff for bugs, regressions, risks

**Review options** via `/review`:
- Review against base branch (PR-style)
- Review uncommitted changes
- Review a commit
- Custom review instructions

Keep a `code_review.md` referenced from `AGENTS.md` for consistent team review behavior. With GitHub Cloud, enable Codex [code review for PRs](https://developers.openai.com/codex/integrations/github). At OpenAI, Codex reviews 100% of PRs.

## MCP: External Context

Use MCP when context lives outside the repo, data changes frequently, or you need repeatable integration.

MCP supports STDIO and Streamable HTTP servers with OAuth.

Add tools only when they unlock real workflows. Start with 1-2 tools that clearly remove a manual loop you do often.

## Skills: Repeatable Work

A skill packages instructions + resources + optional scripts so Codex follows a workflow consistently.

**Good candidates:** log triage, release notes, PR review, migration planning, telemetry summaries, standard debugging flows.

- **Trigger:** explicit (`$skill-name` in prompt) or implicit (task matches description)
- **Create:** `$skill-creator` → answer questions → instruction-only by default
- **Store:** `$HOME/.agents/skills` (personal), `.agents/skills` (repo-scoped, team-shared)
- **Distribute:** package as [[034-plugins-build|plugin]] for broader sharing

> Rule: if you keep reusing same prompt or correcting same workflow → turn into skill.

## Automations: Stable Workflows

Automations schedule Codex to run recurring tasks (project + prompt + cadence + environment).

**Good candidates:** summarize commits, scan bugs, draft release notes, check CI failures, produce standup summaries.

**Rule:** skills define method, automations define schedule. Turn into skill first if still needs steering → automate once predictable.

## Session Management

| Command | Use |
|---------|-----|
| `/experimental` | Toggle experimental features |
| `/resume` | Resume saved conversation |
| `/fork` | New thread, preserve original |
| `/compact` | Summarize thread, free tokens |
| `/agent` | Switch between agent threads |
| `/status` | Inspect session state |

- **One thread per coherent unit** of work — not per project
- **Fork only when work truly branches** — staying in same thread preserves reasoning trail
- Use [[043-concepts-subagents|subagents]] for bounded exploration, tests, triage

## Common Mistakes

| Mistake | Better Approach |
|---------|-----------------|
| Overload prompt with durable rules | Move to `AGENTS.md` or skill |
| Don't let agent see how to run/verify | Include build/test commands |
| Skip planning on multi-step tasks | Use `/plan` |
| Grant full permission before understanding | Start with defaults |
| Run live threads on same files | Use Git worktrees |
| Automate before reliable manually | Stabilize workflow first |
| Watch step by step | Use Codex in parallel with own work |
| One thread per project | One thread per task |

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/learn/best-practices.md)*