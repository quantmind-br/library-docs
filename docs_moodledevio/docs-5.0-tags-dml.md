---
title: 2 docs tagged with "DML" | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/tags/dml
source: sitemap
fetched_at: 2026-02-17T15:18:25.510573-03:00
rendered_js: false
word_count: 49
summary: This document introduces Moodle's native Database Manipulation Layer (DML) drivers and explains how delegated transactions manage CRUD operations and rollbacks.
tags:
    - moodle
    - dml-drivers
    - database-transactions
    - delegated-transactions
    - crud
    - database-api
category: api
---

## [DML drivers](https://moodledev.io/docs/5.0/apis/core/dml/drivers)

A number of native drivers are included with Moodle, including those with support for:

## [Transactions](https://moodledev.io/docs/5.0/apis/core/dml/delegated-transactions)

Moodle allows data manipulation to take place within a database transaction, known as a Delegated transaction. This allows you to perform CRUD operations, and roll them back if a failure takes place.