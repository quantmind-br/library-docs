---
title: What is stored in the DB | liteLLM
url: https://docs.litellm.ai/docs/proxy/db_info
source: sitemap
fetched_at: 2026-01-21T19:51:42.879208697-03:00
rendered_js: false
word_count: 90
summary: This document explains how LiteLLM Proxy utilizes a PostgreSQL database for logging and provides instructions for configuring log settings and performing database migrations.
tags:
    - litellm-proxy
    - postgresql
    - logging
    - database-migration
    - configuration
category: configuration
---

The LiteLLM Proxy uses a PostgreSQL database to store various information. Here's are the main features the DB is used for:

You can disable spend\_logs and error\_logs by setting `disable_spend_logs` and `disable_error_logs` to `True` on the `general_settings` section of your proxy\_config.yaml file.

```
general_settings:
disable_spend_logs:True# Disable writing spend logs to DB
disable_error_logs:True# Only disable writing error logs to DB, regular spend logs will still be written unless `disable_spend_logs: True`
```

If you need to migrate Databases the following Tables should be copied to ensure continuation of services and no downtime