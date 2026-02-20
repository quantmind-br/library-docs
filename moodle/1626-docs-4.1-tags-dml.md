---
title: 2 docs tagged with "DML" | Moodle Developer Resources
url: https://moodledev.io/docs/4.1/tags/dml
source: sitemap
fetched_at: 2026-02-17T14:52:14.144936-03:00
rendered_js: false
word_count: 49
summary: This document introduces Moodle's native database drivers and explains how delegated transactions are used to manage atomic CRUD operations and rollbacks.
tags:
    - moodle-dml
    - database-drivers
    - delegated-transactions
    - crud-operations
    - database-management
category: api
---

## [DML drivers](https://moodledev.io/docs/4.1/apis/core/dml/drivers)

A number of native drivers are included with Moodle, including those with support for:

## [Transactions](https://moodledev.io/docs/4.1/apis/core/dml/delegated-transactions)

Moodle allows data manipulation to take place within a database transaction, known as a Delegated transaction. This allows you to perform CRUD operations, and roll them back if a failure takes place.