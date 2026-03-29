---
title: Getting Started with UI Logs | liteLLM
url: https://docs.litellm.ai/docs/proxy/ui_logs
source: sitemap
fetched_at: 2026-01-21T19:53:55.286525524-03:00
rendered_js: false
word_count: 215
summary: This document explains how to configure and manage logging in LiteLLM, including tracking spend and token usage while providing instructions for data retention and privacy settings.
tags:
    - litellm
    - logging
    - spend-tracking
    - token-usage
    - data-retention
    - proxy-configuration
category: configuration
---

View Spend, Token Usage, Key, Team Name for Each Request to LiteLLM

## Overview[​](#overview "Direct link to Overview")

Log TypeTracked by DefaultSuccess Logs✅ YesError Logs✅ YesRequest/Response Content Stored❌ No by Default, **opt in with `store_prompts_in_spend_logs`**

**By default LiteLLM does not track the request and response content.**

## Tracking - Request / Response Content in Logs Page[​](#tracking---request--response-content-in-logs-page "Direct link to Tracking - Request / Response Content in Logs Page")

If you want to view request and response content on LiteLLM Logs, you need to opt in with this setting

```
general_settings:
store_prompts_in_spend_logs:true
```

## Stop storing Error Logs in DB[​](#stop-storing-error-logs-in-db "Direct link to Stop storing Error Logs in DB")

If you do not want to store error logs in DB, you can opt out with this setting

```
general_settings:
disable_error_logs:True# Only disable writing error logs to DB, regular spend logs will still be written unless `disable_spend_logs: True`
```

## Stop storing Spend Logs in DB[​](#stop-storing-spend-logs-in-db "Direct link to Stop storing Spend Logs in DB")

If you do not want to store spend logs in DB, you can opt out with this setting

```
general_settings:
disable_spend_logs:True# Disable writing spend logs to DB
```

## Automatically Deleting Old Spend Logs[​](#automatically-deleting-old-spend-logs "Direct link to Automatically Deleting Old Spend Logs")

If you're storing spend logs, it might be a good idea to delete them regularly to keep the database fast.

LiteLLM lets you configure this in your `proxy_config.yaml`:

```
general_settings:
maximum_spend_logs_retention_period:"7d"# Delete logs older than 7 days

# Optional: how often to run cleanup
maximum_spend_logs_retention_interval:"1d"# Run once per day
```

You can control how many logs are deleted per run using this environment variable:

`SPEND_LOG_RUN_LOOPS=200 # Deletes up to 200,000 logs in one run`

Set `SPEND_LOG_CLEANUP_BATCH_SIZE` to control how many logs are deleted per batch (default `1000`).

For detailed architecture and how it works, see [Spend Logs Deletion](https://docs.litellm.ai/docs/proxy/spend_logs_deletion).

## What gets logged?[​](#what-gets-logged "Direct link to What gets logged?")

[Here's a schema](https://github.com/BerriAI/litellm/blob/1cdd4065a645021aea931afb9494e7694b4ec64b/schema.prisma#L285) breakdown of what gets logged.