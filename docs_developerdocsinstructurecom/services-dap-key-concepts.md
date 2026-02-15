---
title: Key Concepts | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/key-concepts
source: sitemap
fetched_at: 2026-02-15T09:11:54.99053-03:00
rendered_js: false
word_count: 490
summary: This document provides an overview of the Canvas Data 2 (DAP) platform, explaining its data structure, available access tools, and the differences between snapshot and incremental queries.
tags:
    - canvas-data-2
    - data-access-platform
    - query-api
    - dap-cli
    - incremental-queries
    - snapshot-queries
category: concept
---

In this and other documentation, CD2 (Canvas Data 2) and DAP (Data Access Platform) are used interchangeably and refer to the same platform. Whether a feature is labeled as CD2 or DAP, it serves the same function within this system.

Datasets are the core data sources in DAP. Data is stored in tables, which are organized into namespaces. For example, the Canvas tables such as `assignments`, `content_tags`, and `submissions` are part of the `canvas` namespace, while the `web_logs` table is under the `canvas_logs` namespace. Other products have their own namespaces, such as `catalog`.

Data within datasets cannot be accessed directly; it is only available through the Query API, DAP CLI, or Client Library.

#### Entity Relationship Diagram (ERD)

The Entity Relationship Diagram (ERD) is a lightweight tool for exploring datasets in DAP. It helps you understand the data structure, table schemas, and relationships between tables.

The DAP Query API is a robust RESTful API that enables seamless, programmatic access to data within the Data Access Platform (DAP). Designed to handle large-scale data retrieval, it supports secure, flexible interactions with Instructure datasets. This API is a read-only API.

The DAP CLI is a command-line tool that provides efficient access to large volumes of data with high fidelity and low latency. It offers a convenient way to interact with the Query API, synchronize data to your database, or export data in various file formats.

The Client Library comes bundled with the DAP CLI installation. Similar to the command-line tool, it offers a seamless way to interact with the Query API. Written in Python, it allows you to build custom solutions tailored to your data needs.

These queries generate a complete and comprehensive snapshot of the entire dataset at a given point in time.

Snapshot queries are ideal for creating an initial full copy of the dataset or for occasional full updates. This approach ensures that you have a full, standalone version of the data, which can be useful for comprehensive analyses, audits, and backups.

Note that for the `canvas_logs` dataset, particularly the `web_logs` table, there is a 30-day data retention policy, so the snapshot will not cover the entire dataset but only the last 30 days of data.

Incremental queries retrieve only the changes or updates that have occurred since the last query. This method is more efficient and resource-effective as it minimizes data transfer by only fetching new or modified records.

Incremental queries are ideal for keeping your dataset up-to-date with minimal overhead, enabling near-real-time data updates and reducing the need for frequent full dataset downloads.

Regular use of snapshots is not recommended, as they are resource-intensive for the API and costly to process on the client side. It is recommended taking a snapshot exactly once (as an initialization step) and then using incremental queries thereafter.

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).