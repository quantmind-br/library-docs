---
title: Slash Command - Factory Documentation
url: https://docs.factory.ai/cli/features/readiness-report
source: sitemap
fetched_at: 2026-01-13T19:03:40.740925003-03:00
rendered_js: false
word_count: 385
summary: Explains how to use the /readiness-report command to evaluate repository maturity against the Autonomy Maturity Model, interpret scoring, and implement actionable improvements.
tags:
    - slash-commands
    - repository-analysis
    - autonomy-maturity
    - code-quality
    - cli-tools
    - development-workflow
category: guide
---

The `/readiness-report` slash command evaluates your current repository against the Autonomy Maturity Model, scoring it across five maturity levels and providing actionable recommendations to improve.

* * *

## Prerequisites

Before using this command:

- Enable the feature in `/settings` → `Experimental` → `Readiness Report`

* * *

## Usage

To use the command, navigate to the repo you’d like to evaluate and run:

```
droid
> /readiness-report
```

The evaluation runs against your current repo directory.

* * *

## What Happens

When you run `/readiness-report`, the droid performs a comprehensive evaluation of the repository:

1. **Language Detection** — Identifies repository languages (JavaScript/TypeScript, Python, Rust, Go, Java, Ruby) based on configuration files and source code
2. **Sub-application Discovery** — Determines whether the repository is a mono-repo, or a single service/package/library. For mono-repos, this step identifies all independently deployable applications within the repo
3. **Criteria Evaluation** — Checks the criteria across all five maturity levels
4. **Report Storage** — Persists the evaluation results for visualization in the Factory app
5. **Summary Output** — Prints a human-readable report with results from the evaluation
6. **Remediation *(Coming soon)*** — Option to select and automatically fix failing criteria

* * *

## Understanding the Output

After evaluation, you’ll see a structured report:

### Level Achieved

Your repository’s current maturity level (1-5):

- **Level 1: Functional** — Basic tooling in place
- **Level 2: Documented** — Process and documentation established
- **Level 3: Standardized** — Security and observability configured
- **Level 4: Optimized** — Fast feedback and continuous measurement
- **Level 5: Autonomous** — Self-improving systems

### Applications Discovered

For monorepos, the report lists each application found with a brief description:

```
Example:
1. apps/web - Main Next.js application for user interface
2. apps/api - Backend API service
```

### Criteria Results

Each evaluated criterion is assigned a score and rationale:

```
**Style & Validation**
- Linter Configuration: 2/2 - ESLint configured in both applications
- Type Checker: 2/2 - TypeScript strict mode enabled
- Pre-commit Hooks: 0/1 - No husky or lint-staged configuration found
```

The score for each criterion is formatted as `numerator/denominator`, where:

- **numerator:** The number of sub-applications that pass the criteria
- **denominator:** The number of sub-applications that were evaluated

### Action Items

The report concludes with 2-3 highest-impact recommendations to reach the next level:

```
Action Items:
- Add pre-commit hooks with husky to enforce linting and formatting
- Configure branch protection rules on the main branch
- Add AGENTS.md with setup and development instructions
```

* * *

## Viewing Historical Reports

All readiness reports are automatically saved and can be viewed in the [web dashboard](https://docs.factory.ai/web/agent-readiness/dashboard). This allows you to:

- Track readiness progression over time
- Compare scores across repositories
- Share results with your team

* * *

After running `/readiness-report`, you’ll soon be able to automatically fix failing criteria directly from the CLI:

1. Review the evaluation results
2. Select which failing criteria you’d like to remediate
3. The droid will implement the fixes (e.g., add pre-commit hooks, create AGENTS.md, configure branch protection)

This turns the report from a diagnostic tool into an automated improvement workflow.