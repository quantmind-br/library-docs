---
title: 2 docs tagged with "DML" | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/tags/dml
source: sitemap
fetched_at: 2026-02-17T15:39:36.579423-03:00
rendered_js: false
word_count: 49
summary: This document introduces Moodle's native database drivers and explains the implementation of delegated transactions for managing database operations and rollbacks.
tags:
    - moodle-dml
    - database-drivers
    - delegated-transactions
    - database-api
    - crud-operations
category: api
---

## [DML drivers](https://moodledev.io/docs/5.2/apis/core/dml/drivers)

A number of native drivers are included with Moodle, including those with support for:

## [Transactions](https://moodledev.io/docs/5.2/apis/core/dml/delegated-transactions)

Moodle allows data manipulation to take place within a database transaction, known as a Delegated transaction. This allows you to perform CRUD operations, and roll them back if a failure takes place.