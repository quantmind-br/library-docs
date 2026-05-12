---
title: Set Up Self-Serve Data Analytics with Skills | Guides | Warp
url: https://docs.warp.dev/guides/configuration/how-to-set-up-self-serve-data-analytics-with-skills
source: sitemap
fetched_at: 2026-04-29T15:06:38.074140744-03:00
rendered_js: false
word_count: 768
summary: This guide provides instructions for setting up a self-serve data analytics workflow by configuring automated agent skills for BigQuery and dbt to handle data queries and reproducible analysis.
tags:
    - data-analytics
    - bigquery
    - dbt
    - automation
    - agent-workflow
    - self-serve
    - data-engineering
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Self-serve data analytics means anyone on your team can ask a data question and get a trustworthy answer, without pinging the data team. This guide sets up that workflow using two community Skills that chain together: one resolves vague questions to the right BigQuery tables, and the other structures deep-dive analyses into reproducible folders. Plan on about 10 minutes for initial setup, plus time to customize the model index for your warehouse.

## Prerequisites

| Requirement | Description |
|-------------|-------------|
| BigQuery data warehouse with dbt models | Skills assume BigQuery and dbt. Adaptable to Snowflake, Redshift, Databricks, or non-dbt setups. |
| BigQuery CLI (`bq`) | Installed as part of [Google Cloud SDK](https://cloud.google.com/sdk/docs/install). Agents call it directly to query the warehouse. |
| Git repository | Warp auto-discovers Skills from `.agents/skills/` in your current working directory up through the repo root. |

## Walkthrough video

40-minute livestream demonstrating the workflow end-to-end, including the two Skills and a third pattern (running Skills from Slack via an Oz cloud agent). Feel free to skip ahead if you prefer the written steps.

## 1. Install the two Skills

Warp automatically discovers any Skill stored under `.agents/skills/` in your repo, so committing the two directories makes them available to every teammate's Agent runs.

1. Clone the public [warpdotdev/oz-skills](https://github.com/warpdotdev/oz-skills) repo
2. Copy the two Skill directories into your own dbt repo
3. Verify both Skills landed
4. Commit the Skills

## 2. Customize the dbt model index

The [`dbt-model-index`](https://github.com/warpdotdev/oz-skills/blob/main/.agents/skills/dbt-model-index/SKILL.md) Skill is a template you fill in with details about your own models. This Skill teaches the Agent which tables answer which question types.

Open `.agents/skills/dbt-model-index/SKILL.md` and replace template placeholders with real models. For each entry, include:

- The table name (backtick-formatted)
- 1- to 2-sentence description of its grain
- "Useful for:" bullets covering question types it answers

**Example entry:**

```markdown
`events.activity`
- One row per user per day they were active.
- Useful for:
  - DAU/WAU/MAU calculations
  - User engagement trends
  - Feature adoption rates
```

Fill in domains covering your most common questions first (typically Users, Activity, and Revenue). Expand the index over time as you notice the Agent guessing at tables.

> [!warning]
> Don't skip the **Important Notes** section. Document standard filters (e.g., `where not is_internal_user`), fully-qualified project path, partition fields, and any plan or tier values. This prevents the Agent from accidentally fanning out joins or scanning entire partitioned tables.

## 3. Review the analysis-artifacts Skill

The [`analysis-artifacts`](https://github.com/warpdotdev/oz-skills/blob/main/.agents/skills/analysis-artifacts/SKILL.md) Skill is workflow scaffolding. It tells the Agent how to structure a deep-dive analysis:

- Plan first
- Save every material SQL query to `assets/queries/`
- Save visualizations to `assets/visualizations/`
- Write a README with Problem Statement, TL;DR, Cohorts Definition, per-step sections, and Key Takeaways

No customization needed to start. The resulting directory structure:

```
analyses/<name>/
├── README.md
├── assets/
│   ├── queries/
│   │   └── *.sql
│   └── visualizations/
│       └── *.png
```

## 4. Ask a simple data question

Start with a concrete lookup prompt to exercise `dbt-model-index` without the deep-dive workflow:

```
How many DAU did we have in the last 30 days?
```

The Agent will:
1. Consult `dbt-model-index` to find the right activity table
2. Write a BigQuery query, applying any documented standard filters
3. Run the query via the `bq` CLI
4. Return a single number along with the SQL it ran

Verify the result by reviewing the query. If it used the wrong table or skipped a standard filter, update the `dbt-model-index` entries.

## 5. Run a deep-dive analysis

Try a prompt that goes beyond a single lookup:

```
What is the difference in mobile vs desktop engagement over the last 90 days?
```

The Agent will:
1. Use `dbt-model-index` to resolve the right activity and OS dimensions
2. Invoke `analysis-artifacts`, propose a plan, and wait for your approval
3. Execute the plan step by step, saving queries and visualizations as artifacts
4. Write a README summarizing the analysis

Commit the new `analyses/<name>/` directory to your repo.

## Adapting to your stack

Both Skills were written for BigQuery and dbt, but the pattern generalizes:

| Change | Action |
|--------|--------|
| Non-BigQuery warehouse | Update **Important Notes** with your warehouse's table reference format, partition conventions, and standard filters. Replace `bq` with your warehouse's CLI. |
| No dbt | The `dbt-model-index` Skill works for any warehouse schema. Rename if desired — treat entries as a map over raw tables, views, or your semantic layer. |
| Different modeling conventions | Document grain, tier/plan values, and internal-user filters explicitly. Agents follow documented rules well, but guess poorly. |

The `analysis-artifacts` Skill is largely stack-agnostic — it structures outputs, not queries.

## Next steps

**Extend to Slack.** Wire the same two Skills into an Oz cloud agent configured with your dbt repo, and teammates can ask data questions by @-mentioning Oz in a Slack channel. See [Slack integration docs](https://docs.warp.dev/agent-platform/cloud-agents/integrations/slack) and [Skills as Agents](https://docs.warp.dev/agent-platform/cloud-agents/skills-as-agents).

**Related guides:**
- [Create project rules](https://docs.warp.dev/guides/configuration/how-to-create-project-rules-for-an-existing-project-astro-+-typescript-+-tailwind) — pair Skills with Rules to steer Agent behavior
- [Skills](https://docs.warp.dev/agent-platform/warp-agents/skills) — full reference on Skills, discovery, arguments, and slash-command invocation
