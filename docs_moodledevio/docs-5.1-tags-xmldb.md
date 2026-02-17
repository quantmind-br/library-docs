---
title: 4 docs tagged with "XMLDB" | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/tags/xmldb
source: sitemap
fetched_at: 2026-02-17T15:33:42.412209-03:00
rendered_js: false
word_count: 131
summary: This document provides an overview of Moodle's core APIs and resources for managing database structures, manipulating data, and handling plugin upgrades.
tags:
    - moodle-development
    - database-api
    - dml
    - ddl
    - plugin-upgrades
    - database-schema
category: reference
---

## [Data definition API](https://moodledev.io/docs/5.1/apis/core/dml/ddl)

In this page you'll access to the available functions under Moodle to be able to handle DB structures (tables, fields, indexes...).

## [Data manipulation API](https://moodledev.io/docs/5.1/apis/core/dml)

This page describes the functions available to access data in the Moodle database. You should exclusively use these functions in order to retrieve or modify database content because these functions provide a high level of abstraction and guarantee that your database manipulation will work against different RDBMSes.

## [Database schema](https://moodledev.io/docs/5.1/apis/core/dml/database-schema)

The files available here are in DBDesigner4 format. DBDesigner4 is a schema drawing program released under GPL.

## [Plugin Upgrades](https://moodledev.io/docs/5.1/guides/upgrade)

The Upgrade API is a core API which allows your plugin to manage features of its own installation, and upgrade. Every plugin includes a version which allows the Upgrade API to apply only the required changes.