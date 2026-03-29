---
title: Glossary · Cloudflare D1 docs
url: https://developers.cloudflare.com/d1/reference/glossary/index.md
source: llms
fetched_at: 2026-01-24T15:12:19.08565421-03:00
rendered_js: false
word_count: 214
summary: This document provides a glossary of key terms and definitions used throughout Cloudflare D1 documentation, including database instances, replication, and query management.
tags:
    - cloudflare-d1
    - database-terminology
    - read-replicas
    - glossary
    - database-concepts
category: reference
---

Review the definitions for terms used across Cloudflare's D1 documentation.

| Term | Definition |
| - | - |
| bookmark | A bookmark represents the state of a database at a specific point in time.- Bookmarks are lexicographically sortable. Sorting orders a list of bookmarks from oldest-to-newest. |
| primary database instance | The primary database instance is the original instance of a database. This database instance only exists in one location in the world. |
| query planner | A component in a database management system which takes a user query and generates the most efficient plan of executing that query (the query plan). For example, the query planner decides which indices to use, or which table to access first. |
| read replica | A read replica is an eventually-replicated copy of the primary database instance which only serve read requests. There may be multiple read replicas for a single primary database instance. |
| replica lag | The time it takes for the primary database instance to replicate its changes to a specific read replica. |
| session | A session encapsulates all the queries from one logical session for your application. For example, a session may correspond to all queries coming from a particular web browser session. |