---
title: Client Library | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/lib-index
source: sitemap
fetched_at: 2026-02-15T09:11:51.606366-03:00
rendered_js: false
word_count: 203
summary: This document introduces the DAP Python Client Library, outlining its features for data retrieval, database synchronization, and supported file formats for developers and data analysts.
tags:
    - dap-client
    - python-library
    - data-retrieval
    - database-synchronization
    - instructure-dap
    - oauth-authentication
category: guide
---

The **Data Access Platform (DAP) Python Client Library** provides a convenient way to interact with DAP’s data resources. Designed for developers, data analysts, and IT admins, this library allows efficient access to datasets, enabling streamlined data queries, transformations, and integrations with other data tools.

Built on top of the [Query API](https://developerdocs.instructure.com/services/dap/query-api), DAP Library provides the following features:

- **Data Retrieval**: Supports both **snapshot** and **incremental** queries for up-to-date data access.
- **Multiple Output Formats**: Retrieves data in popular formats, including **CSV**, **TSV**, **JSONL**, and **Parquet**.
- **Automatic Authentication**: Simplifies OAuth-based access with built-in authentication using client credentials.
- **Synchronize to local databases**: Replicate data to supported SQL databases

Before using DAP Library, it is recommended to familiarize yourself with the [key concepts of DAP](https://developerdocs.instructure.com/services/dap/key-concepts).

- **Supported Database Integrations:** PostgreSQL 16.3+, MySQL 8.2+, Microsoft SQL Server 2019+
- **Supported Python Versions:** Python 3.11+

Get the latest source code on [Pypiarrow-up-right](https://pypi.org/project/instructure-dap-client/#files)

Or install it using pip

```
pip3install"instructure-dap-client"
```

[](https://community.canvaslms.com/t5/Data-and-Analytics-Group/gh-p/data)

Visit our forums to connect with the community and learn more about DAP.

[](mailto:canvasdatahelp@instructure.com)

To report bugs or request new features, open a ticket for our Support Team.

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).