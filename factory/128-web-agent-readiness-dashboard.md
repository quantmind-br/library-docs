---
title: Readiness Dashboard - Factory Documentation
url: https://docs.factory.ai/web/agent-readiness/dashboard
source: sitemap
fetched_at: 2026-01-13T19:03:38.125017188-03:00
rendered_js: false
word_count: 541
summary: Explains how to use the Agent Readiness dashboard to track and analyze organization-wide readiness scores, including accessing the interface, viewing historical trends, and refreshing evaluations.
tags:
    - readiness-dashboard
    - analytics
    - scoring
    - repository-metrics
    - factory-cli
category: guide
---

The Agent Readiness dashboard provides a centralized view of your organization’s readiness scores across all repositories, with historical trends and detailed breakdowns. ![Agent Readiness Dashboard](https://mintcdn.com/factory/kzR-NJaHOumGnO-_/images/web/readiness-dashboard.png?fit=max&auto=format&n=kzR-NJaHOumGnO-_&q=85&s=9507568483134ee420e7b0d75ce3fe11)

* * *

## Accessing the Dashboard

Navigate to **Settings → Analytics → Agent Readiness** in the Factory app.

* * *

## Main Dashboard View

The dashboard shows an organization-level overview with three main sections:

### Summary Cards

At the top, you’ll see key metrics:

MetricDescription**Organization Score**Average readiness level across all measured repositories (rounded down)**Repositories Tracked**Number of repositories with readiness reports vs. total enabled repositories**Last Updated**Time since the most recent readiness evaluation

### Progress Graph

A time-series chart showing your organization’s readiness level over time. Use the period filters to view different time ranges:

- **7d** — Last 7 days
- **1m** — Last month
- **6m** — Last 6 months
- **1y** — Last year
- **all** — All time

### Repositories Table

A searchable, paginated table of all repositories showing:

- **Repository name** — Click to view details
- **Level** — Current readiness level (1-5)
- **Progress** — Percentage complete toward next level
- **Last Update** — When the repository was last evaluated

Use the search bar to filter repositories by name or URL.

* * *

## Repository Detail Page

Click any repository row to view its detailed readiness breakdown. ![Repository Detail Page](https://mintcdn.com/factory/kzR-NJaHOumGnO-_/images/web/readiness-criteria.png?fit=max&auto=format&n=kzR-NJaHOumGnO-_&q=85&s=2f5ed9dfcc053c89e29769780ab26fb2)

Shows the repository name, current level achieved, last evaluation time, and a **Refresh** button to trigger a new evaluation.

### Level Accordions

Each readiness level (Functional through Autonomous) has an expandable accordion section showing:

- **Percentage complete** — How much of that level’s criteria are passing
- **Lock status** — Levels are locked until the previous level reaches 80%

### Criterion Rows

Within each level, individual criteria display:

ElementDescription**Name**The criterion being evaluated**Score**Format `[X/Y]` — numerator/denominator**Status**Pass (green) or fail (red) indicator**Rationale**Click to expand and see the evaluation explanation

### Remediation (Coming Soon)

Soon, failing criteria will display a **Fix** button that triggers automated remediation. Select the criteria you want to fix, and the system will implement the necessary changes to your repository.

* * *

## Triggering a Refresh

There are two ways to refresh a readiness evaluation:

### From the Web Dashboard

1. Navigate to the repository detail page
2. Click the **Refresh** button in the header
3. A new session starts to evaluate the repository
4. Once done, the dashboard will update with results from the latest report

### From the CLI

Run the `/readiness-report` [slash command](https://docs.factory.ai/cli/features/readiness-report) in the Factory CLI while in the repository directory:

```
droid
> /readiness-report
```

* * *

## Understanding the Metrics

### Organization Level Calculation

The organization-level score is calculated as the **average of all repository levels, rounded down**. For example:

- Repo A: Level 3
- Repo B: Level 2
- Repo C: Level 3

Organization Level = floor((3 + 2 + 3) / 3) = floor(2.67) = **Level 2**

### Repository Level Calculation

A repository’s level is determined by the **80% threshold system**:

1. Start at Level 1
2. If 80% of Level 1 criteria pass → achieve Level 2
3. If 80% of Level 2 criteria pass → achieve Level 3
4. Continue through Level 5

The percentage shown for each level indicates progress toward completing that level’s criteria.

* * *

## Best Practices

- **Regular evaluations:** Run readiness reports after significant infrastructure changes
- **Focus on current level:** Address failing criteria in your current level before jumping ahead to focus on foundational improvements first
- **Track trends:** Use the progress graph to monitor improvement over time
- **Prioritize high-impact fixes:** The action items in CLI reports highlight the most impactful improvements