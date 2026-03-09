---
title: Readiness Dashboard
url: https://docs.factory.ai/web/agent-readiness/dashboard.md
source: llms
fetched_at: 2026-03-03T01:14:53.641292-03:00
rendered_js: false
word_count: 706
summary: This document explains how to use the Readiness Dashboard to track and analyze organization-wide Agent Readiness scores and repository-specific metrics. It covers navigating the dashboard, interpreting readiness levels, and triggering manual evaluations via the web interface or CLI.
tags:
    - readiness-dashboard
    - agent-readiness
    - analytics
    - repository-metrics
    - performance-tracking
    - factory-app
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Readiness Dashboard

> Track and analyze your organization's Agent Readiness scores in the Factory app.

The Agent Readiness dashboard provides a centralized view of your organization's readiness scores across all repositories, with historical trends and detailed breakdowns.

<img src="https://mintcdn.com/factory/kzR-NJaHOumGnO-_/images/web/readiness-dashboard.png?fit=max&auto=format&n=kzR-NJaHOumGnO-_&q=85&s=9507568483134ee420e7b0d75ce3fe11" alt="Agent Readiness Dashboard" data-og-width="1724" width="1724" data-og-height="1121" height="1121" data-path="images/web/readiness-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/factory/kzR-NJaHOumGnO-_/images/web/readiness-dashboard.png?w=280&fit=max&auto=format&n=kzR-NJaHOumGnO-_&q=85&s=22bae653fdd114f010be2023392592cc 280w, https://mintcdn.com/factory/kzR-NJaHOumGnO-_/images/web/readiness-dashboard.png?w=560&fit=max&auto=format&n=kzR-NJaHOumGnO-_&q=85&s=1533ea2a6c252d83290e31d72d5c4b44 560w, https://mintcdn.com/factory/kzR-NJaHOumGnO-_/images/web/readiness-dashboard.png?w=840&fit=max&auto=format&n=kzR-NJaHOumGnO-_&q=85&s=e40296495357b999c9bdb9f08fa438ca 840w, https://mintcdn.com/factory/kzR-NJaHOumGnO-_/images/web/readiness-dashboard.png?w=1100&fit=max&auto=format&n=kzR-NJaHOumGnO-_&q=85&s=6b01888025344ca80ae51c0b7c095a24 1100w, https://mintcdn.com/factory/kzR-NJaHOumGnO-_/images/web/readiness-dashboard.png?w=1650&fit=max&auto=format&n=kzR-NJaHOumGnO-_&q=85&s=7f444c3293fae51810c8be9e588a3bf0 1650w, https://mintcdn.com/factory/kzR-NJaHOumGnO-_/images/web/readiness-dashboard.png?w=2500&fit=max&auto=format&n=kzR-NJaHOumGnO-_&q=85&s=f0c154537fc8d3e277eb6f9df5b9aa9e 2500w" />

***

## Accessing the Dashboard

Navigate to **Settings → Analytics → Agent Readiness** in the Factory app.

***

## Main Dashboard View

The dashboard shows an organization-level overview with three main sections:

### Summary Cards

At the top, you'll see key metrics:

| Metric                   | Description                                                                  |
| :----------------------- | :--------------------------------------------------------------------------- |
| **Organization Score**   | Average readiness level across all measured repositories (rounded down)      |
| **Repositories Tracked** | Number of repositories with readiness reports vs. total enabled repositories |
| **Last Updated**         | Time since the most recent readiness evaluation                              |

### Progress Graph

A time-series chart showing your organization's readiness level over time. Use the period filters to view different time ranges:

* **7d** — Last 7 days
* **1m** — Last month
* **6m** — Last 6 months
* **1y** — Last year
* **all** — All time

### Repositories Table

A searchable, paginated table of all repositories showing:

* **Repository name** — Click to view details
* **Level** — Current readiness level (1-5)
* **Progress** — Percentage complete toward next level
* **Last Update** — When the repository was last evaluated

Use the search bar to filter repositories by name or URL.

***

## Repository Detail Page

Click any repository row to view its detailed readiness breakdown.

<img src="https://mintcdn.com/factory/kzR-NJaHOumGnO-_/images/web/readiness-criteria.png?fit=max&auto=format&n=kzR-NJaHOumGnO-_&q=85&s=2f5ed9dfcc053c89e29769780ab26fb2" alt="Repository Detail Page" data-og-width="1721" width="1721" data-og-height="1234" height="1234" data-path="images/web/readiness-criteria.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/factory/kzR-NJaHOumGnO-_/images/web/readiness-criteria.png?w=280&fit=max&auto=format&n=kzR-NJaHOumGnO-_&q=85&s=ec183b6596db426731247ea13e835f11 280w, https://mintcdn.com/factory/kzR-NJaHOumGnO-_/images/web/readiness-criteria.png?w=560&fit=max&auto=format&n=kzR-NJaHOumGnO-_&q=85&s=3d1291d572d3a956f9451fd959efba8b 560w, https://mintcdn.com/factory/kzR-NJaHOumGnO-_/images/web/readiness-criteria.png?w=840&fit=max&auto=format&n=kzR-NJaHOumGnO-_&q=85&s=3f13c1aaa769718947ab1eefb1ee5651 840w, https://mintcdn.com/factory/kzR-NJaHOumGnO-_/images/web/readiness-criteria.png?w=1100&fit=max&auto=format&n=kzR-NJaHOumGnO-_&q=85&s=1a02baf6745e69337d89ec5a9077308d 1100w, https://mintcdn.com/factory/kzR-NJaHOumGnO-_/images/web/readiness-criteria.png?w=1650&fit=max&auto=format&n=kzR-NJaHOumGnO-_&q=85&s=02a0d44214a30cdf8fcf3c11871d4257 1650w, https://mintcdn.com/factory/kzR-NJaHOumGnO-_/images/web/readiness-criteria.png?w=2500&fit=max&auto=format&n=kzR-NJaHOumGnO-_&q=85&s=c71fc02f3ec5fa634eddbb576ca03c0c 2500w" />

### Header

Shows the repository name, current level achieved, last evaluation time, and a **Refresh** button to trigger a new evaluation.

### Level Accordions

Each readiness level (Functional through Autonomous) has an expandable accordion section showing:

* **Percentage complete** — How much of that level's criteria are passing
* **Lock status** — Levels are locked until the previous level reaches 80%

### Criterion Rows

Within each level, individual criteria display:

| Element       | Description                                        |
| :------------ | :------------------------------------------------- |
| **Name**      | The criterion being evaluated                      |
| **Score**     | Format `[X/Y]` — numerator/denominator             |
| **Status**    | Pass (green) or fail (red) indicator               |
| **Rationale** | Click to expand and see the evaluation explanation |

### Remediation (Coming Soon)

Soon, failing criteria will display a **Fix** button that triggers automated remediation. Select the criteria you want to fix, and the system will implement the necessary changes to your repository.

***

## Triggering a Refresh

There are two ways to refresh a readiness evaluation:

### From the Web Dashboard

1. Navigate to the repository detail page
2. Click the **Refresh** button in the header
3. A new session starts to evaluate the repository
4. Once done, the dashboard will update with results from the latest report

### From the CLI

Run the `/readiness-report` [slash command](/cli/features/readiness-report) in the Factory CLI while in the repository directory:

```bash  theme={null}
droid
> /readiness-report
```

<Note>
  Re-evaluations run the full readiness assessment against the current state of
  your repository. This is useful after making infrastructure improvements or
  merging changes that can affect a readiness criterion.
</Note>

***

## Understanding the Metrics

### Organization Level Calculation

The organization-level score is calculated as the **average of all repository levels, rounded down**. For example:

* Repo A: Level 3
* Repo B: Level 2
* Repo C: Level 3

Organization Level = floor((3 + 2 + 3) / 3) = floor(2.67) = **Level 2**

### Repository Level Calculation

A repository's level is determined by the **80% threshold system**:

1. Start at Level 1
2. If 80% of Level 1 criteria pass → achieve Level 2
3. If 80% of Level 2 criteria pass → achieve Level 3
4. Continue through Level 5

The percentage shown for each level indicates progress toward completing that level's criteria.

***

## Best Practices

* **Regular evaluations:** Run readiness reports after significant infrastructure changes
* **Focus on current level:** Address failing criteria in your current level before jumping ahead to focus on foundational improvements first
* **Track trends:** Use the progress graph to monitor improvement over time
* **Prioritize high-impact fixes:** The action items in CLI reports highlight the most impactful improvements