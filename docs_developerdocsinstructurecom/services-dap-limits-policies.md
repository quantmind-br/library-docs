---
title: Rate Limits & Policies | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/limits-policies
source: sitemap
fetched_at: 2026-02-15T09:11:49.154577-03:00
rendered_js: false
word_count: 243
summary: This document outlines the usage policies, rate limits, and data retention rules for the DAP Query API and its associated namespaces.
tags:
    - dap-query-api
    - rate-limits
    - data-retention
    - incremental-queries
    - canvas-data
    - api-policies
category: reference
---

To maintain fair usage and performance, the following rate limits have been implemented on the [DAP Query API](https://developerdocs.instructure.com/services/dap/query-api).

POST `/query/{namespace}/table/{table}/data`

GET `/query/{namespace}/table`

GET `/query/{namespace}/table/{table}/schema`

These limits are independent for each endpoint. Reaching the limit for one request type or endpoint does not impact the limits for other types or endpoints. For example, reaching the limit for GET requests on `/dap/query/canvas/table` will not affect your ability to make POST requests or use other GET endpoints.

Since the CLI and Client Library are built on top of the Query API and use its endpoints, these rate limits apply to them as well.

If you anticipate needing higher limits, please contact your Customer Success Manager to discuss your requirements.

Data in DAP is refreshed every 4 hours.

### Canvas and Catalog Namespaces

The DAP API does not support time-travel queries, meaning it only provides access to the latest state of the data. To retrieve the current dataset, you can use a snapshot query to capture a copy of the data as it exists at that moment. Afterward, use incremental queries to keep this data up-to-date by fetching only new, updated, or deleted records as changes occur within the Data Access Platform.

Logs older than 30 days are no longer available via DAP API.

Learn more details about [Instructure's Canvas API policiesarrow-up-right](https://www.instructure.com/policies/canvas-api-policy).

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).