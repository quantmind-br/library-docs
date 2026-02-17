---
title: Supported Cron Syntax
url: https://coolify.io/docs/knowledge-base/cron-syntax.md
source: llms
fetched_at: 2026-02-17T14:40:36.059467-03:00
rendered_js: false
word_count: 119
summary: This document outlines the supported cron syntax and predefined schedule aliases used for automating tasks such as backups and cleanups within Coolify.
tags:
    - coolify
    - cron-syntax
    - task-scheduling
    - automation
    - predefined-schedules
category: reference
---

# Supported Cron Syntax

Coolify supports scheduling automated tasks like cleanups, backups, and more using cron syntax.

## Supported Syntax

### Standard Cron Format

Coolify supports the complete standard cron syntax format (`* * * * *`).

### Predefined Schedules

For convenience, Coolify also supports the following predefined schedule strings:

#### Without @ Prefix

* `every_minute` - Runs every minute
* `hourly` - Runs once per hour
* `daily` - Runs once per day
* `weekly` - Runs once per week
* `monthly` - Runs once per month
* `yearly` - Runs once per year

#### With @ Prefix

* `@every_minute` - Runs every minute
* `@hourly` - Runs once per hour
* `@daily` - Runs once per day
* `@weekly` - Runs once per week
* `@monthly` - Runs once per month
* `@yearly` - Runs once per year