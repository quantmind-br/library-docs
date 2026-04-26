---
title: Quickstart | Mistral Docs
url: https://docs.mistral.ai/studio-api/observability/quickstart
source: sitemap
fetched_at: 2026-04-26T04:13:23.351208066-03:00
rendered_js: false
word_count: 776
summary: This guide details the Observability workflow in Mistral Studio, covering how to explore production traffic, configure automated judges for evaluation, run analysis campaigns, and curate annotated datasets.
tags:
    - observability
    - data-curation
    - ai-evaluation
    - production-monitoring
    - mistral-studio
    - campaign-management
    - machine-learning-ops
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

This guide walks through the Observability workflow in [Studio](http://console.mistral.ai).

> [!info]
> Each step includes an `API & SDK Implementation` callout showing exact SDK methods for the same action.

**By the end you will have:**
- A **filtered view** of production traffic showing relevant conversations
- A **Judge** that automatically identifies and scores/labels these conversations
- A completed **Campaign** that applies the Judge across your traffic at scale
- A **Dataset** built from Campaign results

**Prerequisites:**
- **Enterprise-tier** Organization
- **Admin access** to Observability features
- Production traffic with **chat completion events**

## Step 1: Explore Traffic

Click **Observe** then open **Explorer** in the sidebar.

Goal: find a filter combination that surfaces relevant conversations (failure modes, low-quality responses, specific behaviors).

1. Start with a **broad time range** (e.g., last 7 days) and **one model** (e.g., `mistral-medium-2508`).
2. **Experiment with filters** until you find a suitable combination:
   - `invoked_tools includes "web_search"` to isolate tool-using conversations
   - `last_user_message_preview contains "reset password"` for specific topics
   - `total_time_elapsed > 5` for slow responses
3. **Click into individual events** to inspect messages, tool calls, and metadata.

> [!tip]
> Refining filters **improves Judge and Campaign accuracy**. Define "relevant" before automating evaluations.

![Explorer view with filter bar showing model and date range](https://docs.mistral.ai/img/observability_explorer_ui.png)

**API & SDK:** Use `chat_completion_events.search()` to filter events programmatically. [SDK docs](https://docs.mistral.ai/studio-api/observability/explorer#sdk-access)

## Step 2: Create a Judge

Create a Judge to **evaluate conversations automatically**.

1. Go to **Judges** in the sidebar → click **Create Judge**.
2. **Select a model** from available options.
3. Provide clear **evaluation instructions**.
4. **Add tools** (optional):
   - **Web Search**: give the Judge internet access
   - **Code Interpreter**: let the Judge run Python code
5. **Select Judge type** and provide labels/score ranges:
   - **Classification**: discrete labels (e.g., `helpful` / `not helpful`)
   - **Regression**: numeric score (e.g., 0 to 5)
6. Click **Create Judge**, provide name and description.

![Judge creation form](https://docs.mistral.ai/img/observability_judges_create.png)

> [!warning]
> [Test your Judge](https://docs.mistral.ai/studio-api/observability/judges#validation-before-scale) on real records **before running a Campaign**.

**API & SDK:** Use `judges.create()` with instructions and parameters. [SDK docs](https://docs.mistral.ai/studio-api/observability/judges#sdk-access)

## Step 3: Run a Campaign

A **Campaign** evaluates filtered events and **applies your Judge**.

1. Go to **Campaigns** in the sidebar → click **Create Campaign**.
2. In the Campaign creation form:
   - Select the **Judge** from Step 2
   - Select a **time range** (e.g., last 7 days)
   - **Define filters** (reuse from Step 1 or widen scope)
   - Limit **number of events** (100 to 10,000)
3. Click **Create Campaign**, provide name and description.

**Campaigns run in the background**. Check the [Campaigns dashboard](https://console.mistral.ai/observability/campaigns) for results.

![Campaign detail view](https://docs.mistral.ai/img/observability_campaign_run.png)

**API & SDK:** Use `campaigns.create()` to define filters and attach your Judge. Monitor with `campaigns.fetch_status()`. [SDK docs](https://docs.mistral.ai/studio-api/observability/campaigns#sdk-access)

## Step 4: Build a Dataset

Campaign completes → all events are **annotated with Judge output**.

1. **Select relevant events** (apply additional filters as needed).
2. Click **Actions** → add to a **new Dataset** or append to an existing one.

Campaign annotations are linked to original events. View anytime in [Explorer](https://docs.mistral.ai/studio-api/observability/explorer).

**API & SDK:** Use `campaigns.list_events()` then `datasets.import_from_explorer()`. [SDK docs](https://docs.mistral.ai/studio-api/observability/campaigns#sdk-access) & [Datasets](https://docs.mistral.ai/studio-api/observability/datasets#sdk-access)

## Outcome

Congratulations! You created a **curated, annotated Dataset** built from **real production data**.

## Next Steps

- [**Explorer**](https://docs.mistral.ai/studio-api/observability/explorer): Query specific events and filter production logs
- [**Judges**](https://docs.mistral.ai/studio-api/observability/judges): Design complex instructions, schemas, and validation techniques
- [**Campaigns**](https://docs.mistral.ai/studio-api/observability/campaigns): Annotate thousands of production events in bulk
- [**Datasets**](https://docs.mistral.ai/studio-api/observability/datasets): Manage record structures, curation, and file imports

#observability #ai-evaluation #production-monitoring