---
title: 5 docs tagged with "core_dml" | Moodle Developer Resources
url: https://moodledev.io/docs/4.1/tags/core-dml
source: sitemap
fetched_at: 2026-02-17T14:51:42.775818-03:00
rendered_js: false
word_count: 136
summary: This document provides an overview of Moodle's database APIs, covering Data Definition (DDL) for structure management and Data Manipulation (DML) for database content interactions. It also details supported database drivers, exception handling, and the implementation of delegated transactions.
tags:
    - moodle-development
    - database-api
    - dml
    - ddl
    - data-manipulation
    - database-drivers
    - transactions
category: api
---

## [Data definition API](https://moodledev.io/docs/4.1/apis/core/dml/ddl)

In this page you'll access to the available functions under Moodle to be able to handle DB structures (tables, fields, indexes...).

## [Data manipulation API](https://moodledev.io/docs/4.1/apis/core/dml)

This page describes the functions available to access data in the Moodle database. You should exclusively use these functions in order to retrieve or modify database content because these functions provide a high level of abstraction and guarantee that your database manipulation will work against different RDBMSes.

## [DML drivers](https://moodledev.io/docs/4.1/apis/core/dml/drivers)

A number of native drivers are included with Moodle, including those with support for:

## [DML exceptions](https://moodledev.io/docs/4.1/apis/core/dml/exceptions)

The DML API uses a selection of exceptions to indicate errors.

## [Transactions](https://moodledev.io/docs/4.1/apis/core/dml/delegated-transactions)

Moodle allows data manipulation to take place within a database transaction, known as a Delegated transaction. This allows you to perform CRUD operations, and roll them back if a failure takes place.