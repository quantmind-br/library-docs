---
title: Token Efficiency Strategies - Factory Documentation
url: https://docs.factory.ai/guides/power-user/token-efficiency
source: sitemap
fetched_at: 2026-01-13T19:03:31.483495465-03:00
rendered_js: false
word_count: 661
summary: This guide explains how to optimize token usage and reduce costs when working with AI coding agents by improving project configuration, selecting appropriate models, and implementing efficient workflow patterns.
tags:
    - token-optimization
    - ai-agents
    - cost-management
    - project-setup
    - model-selection
category: guide
---

Token usage isn’t just about cost—it’s about feedback loop speed and context window limits. This guide shows you how to get more done with fewer tokens through project optimization, smart model selection, and workflow patterns.

* * *

## Understanding Token Usage

Tokens are consumed in three main areas:

```
┌──────────────────────────────────────────────────────────┐
│                    Token Consumption                      │
├────────────────┬────────────────┬────────────────────────┤
│   Context      │   Tool Calls   │   Model Output         │
│   (Input)      │   (Overhead)   │   (Response)           │
├────────────────┼────────────────┼────────────────────────┤
│ • AGENTS.md    │ • Read files   │ • Explanations         │
│ • Memories     │ • Grep/search  │ • Generated code       │
│ • Conversation │ • Execute cmds │ • Analysis             │
│ • File content │ • Each retry   │ • Thinking tokens      │
└────────────────┴────────────────┴────────────────────────┘
```

**High token usage often means:**

- Too much exploration (unclear instructions)
- Multiple attempts (missing context or failing tests)
- Verbose output (no format constraints)

* * *

## Project Setup for Efficiency

The biggest token savings come from project configuration that prevents wasted cycles.

### 1. Fast, Reliable Tests

Test CharacteristicImpact on TokensFast tests (&lt; 30s)Droid verifies changes immediatelySlow tests (&gt; 2min)Droid may skip verification or waste context waitingFlaky testsFalse failures cause debugging cyclesNo testsDroid can’t verify changes, more back-and-forth

**Action items:**

```
## In your AGENTS.md

## Testing
- Run single file: `npm test -- path/to/file.test.ts`
- Run fast smoke tests: `npm test -- --testPathPattern=smoke`
- Full suite takes ~3 minutes, use `--bail` for early exit on failure
```

### 2. Linting and Type Checking

When Droid can catch errors immediately, it fixes them in the same turn instead of waiting for you to report them.

```
## In your AGENTS.md

## Validation Commands
- Lint (auto-fix): `npm run lint:fix`
- Type check: `npm run typecheck`
- Full validation: `npm run validate` (lint + typecheck + test)

Always run `npm run lint:fix` after making changes.
```

### 3. Clear Project Structure

Document your file organization so Droid doesn’t waste tokens exploring:

```
## In your AGENTS.md

## Project Structure
- `src/components/` - React components (one per file)
- `src/hooks/` - Custom React hooks
- `src/services/` - API and business logic
- `src/types/` - TypeScript type definitions
- `tests/` - Test files mirror src/ structure

When adding a new component:
1. Create component in `src/components/ComponentName/`
2. Add index.ts for exports
3. Add ComponentName.test.tsx in same directory
```

* * *

## Agent Readiness Checklist

The [Agent Readiness Report](https://docs.factory.ai/cli/features/readiness-report) evaluates your project against criteria that directly impact token efficiency.

### High-Impact Criteria

CriterionToken ImpactWhy It Matters**Linter Configuration**🟢 HighCatches errors immediately, no debugging cycles**Type Checker**🟢 HighPrevents runtime errors, clearer code**Unit Tests Runnable**🟢 HighVerification in same turn**AGENTS.md**🟢 HighContext upfront, less exploration**Build Command Documentation**🟡 MediumNo guessing, fewer failed attempts**Dependencies Pinned**🟡 MediumReproducible builds**Pre-commit Hooks**🟡 MediumAutomatic quality enforcement

Run the readiness report to identify gaps:

```
droid
> /readiness-report
```

* * *

## Model Selection Strategy

Different models have different cost multipliers and capabilities. Match the model to the task:

### Cost Multipliers

ModelMultiplierBest ForGLM-4.6 (Droid Core)0.25×Bulk automation, simple tasksClaude Haiku 4.50.4×Quick edits, routine workGPT-5.1 / GPT-5.1-Codex0.5×Implementation, debuggingGemini 3 Pro0.8×Research, analysisClaude Sonnet 4.51.2×Balanced quality/costClaude Opus 4.52×Complex reasoning, architectureClaude Opus 4.16×Maximum capability (use sparingly)

### Task-Based Model Selection

```
Simple edit, formatting      → Haiku 4.5 (0.4×)
Implement feature from spec  → GPT-5.1-Codex (0.5×)
Debug complex issue          → Sonnet 4.5 (1.2×)
Architecture planning        → Opus 4.5 (2×)
Bulk file processing         → Droid Core (0.25×)
```

### Reasoning Effort Impact

Higher reasoning = more “thinking” tokens but often fewer retries.

ReasoningWhen to UseToken Trade-offOff/NoneSimple, clear tasksLowest per-turn, may need more turnsLowStandard implementationGood balanceMediumComplex logic, debuggingHigher per-turn, fewer retriesHighArchitecture, analysisHighest per-turn, best first-attempt

**Rule of thumb:** Use higher reasoning for tasks where a wrong first attempt would be expensive to fix.

* * *

## Workflow Patterns for Efficiency

### Pattern 1: Spec Mode for Complex Work

Use [Specification Mode](https://docs.factory.ai/cli/user-guides/specification-mode) (`Shift+Tab` or `/spec`) to plan before implementing. **Without Spec Mode:**

```
Turn 1: Start implementing → wrong approach → wasted tokens
Turn 2: Undo and try different approach → more tokens
Turn 3: Finally get it right
Total: 3 turns of implementation tokens
```

**With Spec Mode:**

```
Turn 1: Plan with exploration → correct approach identified
Turn 2: Implement correctly
Total: 1 turn of planning + 1 turn of implementation
```

### Pattern 2: IDE Plugin for Context

Without IDE plugin, Droid must read files to understand context:

```
Read file A → Read file B → Read file C → Understand context → Work
(4 tool calls before actual work)
```

With IDE plugin, context is immediate:

```
Work (IDE provides open files, errors, selection)
(0 extra tool calls for context)
```

### Pattern 3: Specific Over General

**Expensive prompt:**

```
"Fix the bug in the auth module"
```

→ Droid reads multiple files to find the bug, explores different possibilities **Efficient prompt:**

```
"Fix the timeout bug in src/auth/session.ts line 45 where the session expires after 5 minutes instead of 24 hours"
```

→ Droid goes directly to the issue

### Pattern 4: Batch Similar Work

**Expensive:**

```
Turn 1: "Add logging to userService"
Turn 2: "Add logging to orderService"
Turn 3: "Add logging to paymentService"
(3 turns, context rebuilt each time)
```

**Efficient:**

```
Turn 1: "Add structured logging to all services in src/services/. Use the pattern from src/lib/logger.ts. Services: user, order, payment."
(1 turn, pattern established once)
```

* * *

## Reducing Token Waste

### Common Waste Patterns

PatternCauseFixMultiple exploration cyclesUnclear requirementsBe specific upfrontRepeated file readsMissing IDE contextInstall IDE pluginFailed attemptsNo tests/lintingAdd validation toolsVerbose explanationsNo format constraintAsk for concise outputWrong architectureMissing contextUse Spec Mode

### Format Constraints

Ask for specific output formats to reduce verbosity:

```
"Add the feature. Return only the changed code, no explanations unless something is unclear."
```

```
"Review this code. Format: bullet list of issues only, no preamble."
```

```
"Debug this test failure. Show me the fix, then explain in 2-3 sentences."
```

* * *

## Monitoring Your Usage

### Check Current Session Cost

This shows token usage for the current session.

### Track Over Time

Review your usage patterns:

1. **After each session**, note the `/cost` output
2. **Identify expensive sessions**: What made them expensive?
3. **Refine approach**: More context? Different model? Better prompts?

### Usage Red Flags

Watch for these patterns:

- 🚩 **High read count**: Droid is exploring too much (add AGENTS.md context)
- 🚩 **Multiple grep/search calls**: Unclear what to look for (be more specific)
- 🚩 **Repeated similar edits**: Failed attempts (check tests/linting)
- 🚩 **Very long conversations**: Scope creep (break into smaller tasks)

* * *

## Quick Wins Checklist

Implement these for immediate token savings:

- **Install IDE plugin** - Eliminates context-gathering tool calls
- **Create AGENTS.md** - Droid knows build/test commands upfront
- **Configure linting** - Errors caught immediately
- **Fast test command** - Verification in same turn
- **Use Spec Mode** - Prevents expensive false starts
- **Be specific** - Reduces exploration cycles
- **Match model to task** - Don’t use Opus for simple edits

* * *

## Token Budget Guidelines

Rough guidelines for common tasks:

Task TypeTypical Token RangeNotesQuick edit5k-15kSimple, specific changesFeature implementation30k-80kWith Spec Mode planningComplex debugging50k-150kMay need multiple attemptsArchitecture planning20k-50kHigh-reasoning modelCode review30k-60kDepends on PR sizeBulk refactoring50k-200kMany files, use efficient model

If you’re significantly exceeding these ranges, review the waste patterns above.

* * *

## Summary: The Token-Efficient Workflow

```
1. Set up your project
   └─ AGENTS.md with commands
   └─ Fast tests
   └─ Linting configured
   └─ IDE plugin installed

2. Start each task right
   └─ Use Spec Mode for complex work
   └─ Be specific about the goal
   └─ Reference existing patterns

3. Choose the right model
   └─ Simple → Haiku/Droid Core
   └─ Standard → Codex/Sonnet
   └─ Complex → Opus (with reasoning)

4. Monitor and adjust
   └─ Check /cost periodically
   └─ Identify expensive patterns
   └─ Refine your approach
```

* * *

## Next Steps