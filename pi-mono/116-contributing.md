---
title: CONTRIBUTING
url: https://github.com/badlogic/pi-mono/blob/main/CONTRIBUTING.md
source: git
fetched_at: 2026-05-03T09:30:50.443580968-03:00
rendered_js: false
word_count: 639
summary: Contribution requirements, quality standards, and submission workflow for the pi project.
tags:
    - contribution-guidelines
    - pull-request-policy
    - issue-management
    - project-governance
    - developer-workflow
category: guide
optimized: true
optimized_at: 2026-05-03T12:31:00Z
---
# Contributing to pi

## The One Rule

**You must understand your code.** If you cannot explain what your changes do and how they interact with the rest of the system, your PR will be closed.

Using AI to write code is fine. Submitting AI-generated slop without understanding it is not.

If you use an agent, run it from the `pi-mono` root directory so it picks up `AGENTS.md` automatically. Your agent must follow the rules in that file.

## Contribution Gate

All issues and PRs from new contributors are auto-closed by default.

Issues submitted Friday through Sunday are not reviewed. For urgent matters, ask on [Discord](https://discord.com/invite/3cU7Bz4UPx).

Maintainers review auto-closed issues daily and reopen worthwhile ones. Issues not meeting the quality bar will not be reopened or receive a reply.

### Approval Comments

| Comment | Grants |
|---------|--------|
| `lgtmi` | Future issues will not be auto-closed |
| `lgtm` | Future issues AND PRs will not be auto-closed |

`lgtmi` does not grant rights to submit PRs. Only `lgtm` grants PR rights.

## Quality Bar For Issues

Use one of the two GitHub issue templates.

### Requirements

- **Concise**: If it doesn't fit on one screen, it's too long
- **Your voice**: Write in your own voice
- **Clear**: State the bug or request clearly
- **Justified**: Explain why it matters
- **Optional**: If you want to implement the change yourself, say so

If the issue is real and written well, a maintainer may reopen it, reply `lgtmi`, or reply `lgtm`.

## Blocking

| Violation | Consequence |
|-----------|-------------|
| Ignore this document twice | Permanent GitHub account block |
| Spam tracker with agent-generated issues | Permanent GitHub account block |
| Large volume of issues through automation | Permanent GitHub account block |

No exceptions.

## Before Submitting a PR

Do not open a PR unless you have been approved with `lgtm`.

### Pre-submission Checklist

```bash
npm run check
./test.sh
```

Both must pass.

> [!note]
> Do not edit `CHANGELOG.md`. Changelog entries are added by maintainers.

If adding a new provider to `packages/ai`, see `AGENTS.md` for required tests.

## Philosophy

pi's core is minimal. If your feature does not belong in the core, it should be an extension. PRs that bloat the core will likely be rejected.

## Questions

Ask on [Discord](https://discord.com/invite/nKXTsAcmbT).

## FAQ

### Why are new issues and PRs auto-closed?

pi receives more issues than maintainers can responsibly review. Many reports don't meet the quality bar or don't follow CONTRIBUTING.md. Some are submitted via agent without being reviewed by the person. Auto-closing lets maintainers review on their own schedule.

### Why are weekend issues not reviewed?

Maintainers need uninterrupted time away from the tracker. Issues submitted Friday through Sunday are auto-closed and not part of the Monday review queue. For urgent problems, ask on Discord with: short version, repro, relevant logs.

### Why do some issues get no reply?

A reply is maintenance work. Low-signal issues, unclear reports, duplicates, and issues not following this guide may be closed without discussion. This keeps time for reproducible bugs, thoughtful requests, and contributors who did the work to make reports actionable.

### Why not let AI triage everything?

AI can help group duplicates, summarize reports, and spot missing information. It is not trusted to make final maintainer decisions. Polished AI-generated issues can still be wrong, misleading, or expensive to investigate. Human review remains the final gate.

### Is this hostile to contributors?

No. It is a guardrail against burnout and tracker spam. Short, concrete, reproducible issues are welcome. Thoughtful contributions are welcome. Automated slop, entitlement, and large volumes of low-effort reports are not.

## Related

- [[021-agents.md|AGENTS]] — Technical standards and development rules
- [[017-.pi-prompts-cl.md|cl]] — Changelog audit before release
- [[017-.pi-prompts-is.md|is]] — Investigate issues independently
- [[019-.pi-prompts-pr.md|pr]] — Pull request review procedure
- [[020-.pi-prompts-wr.md|wr]] — Task finalization workflow

#contribution-guidelines #pull-request-policy #issue-management
