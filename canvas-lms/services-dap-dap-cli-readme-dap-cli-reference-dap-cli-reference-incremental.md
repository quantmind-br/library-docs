---
title: dap incremental | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/dap-cli-readme/dap-cli-reference/dap-cli-reference-incremental
source: sitemap
fetched_at: 2026-02-15T08:57:25.37426-03:00
rendered_js: false
word_count: 285
summary: This document explains how to use the dap incremental command to efficiently download only new or modified data records from specific namespaces and tables within a specified timeframe.
tags:
    - dap-cli
    - incremental-data
    - data-access-platform
    - command-line-tool
    - data-synchronization
category: reference
---

Generates and downloads only the new or modified records of a table within a specified timeframe. This efficient, resource-effective approach helps keep datasets up-to-date with minimal overhead. Incremental queries enable near-real-time updates, reducing the need for frequent full dataset downloads.

```
dap [arguments] incremental [flags]
```

`--client-id <string>` Client ID obtained from the Identity Service. Skip, if `DAP_CLIENT_ID` environment variable is set.

`--client-secret <string>` Client Secret obtained from the Identity Service. Skip, if `DAP_CLIENT_SECRET` environment variable is set.

`--namespace <string>` Specifies the data source (namespace). Available options: {canvas, canvas\_log, catalog}.

`--table <string>` Specifies the table(s) to fetch data from. Can be a single table name, a comma separated list of table names or the special `all` keyword to fetch all tables in the namespace.

`--since <datetime>` Start timestamp for the incremental query. Examples: `2024-12-01T09:30:00Z`

`--until <datetime>` End timestamp for the incremental query. Examples: `2024-12-01T09:30:00Z`

`--format <string> (default: JSONL)` Defines the output format. Available options: {CSV, JSONL, Parquet, TSV}.

`--output-directory <string> (default: downloads)` Specifies the absolute or relative path to the output directory where the snapshot will be stored.

`-h, --help` Displays help information for the command.

Get new or modified records of the `courses` table from the `canvas` namespace since October 1, 2024: `$ dap incremental --namespace canvas --table courses --since 2024-11-01T00:00:00`

Get new or modified records of all tables from the `canvas` namespace between October 1, 2024, and October 31, 2024: `$ dap incremental --namespace canvas --table all --since 2024-11-01T00:00:00 --then 2024-11-01T00:00:00`

[](https://developerdocs.instructure.com/services/dap/key-concepts)

Get familiar with the key concepts in DAP.

[](https://developerdocs.instructure.com/services/dap/limits-policies)

Learn more about the limits and our policies in DAP.

[](https://developerdocs.instructure.com/services/dap/dataset)

Discover the available namespaces and tables.

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).