---
title: dap snapshot | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/dap-cli-readme/dap-cli-reference/dap-cli-reference-snapshot
source: sitemap
fetched_at: 2026-02-15T09:11:42.018387-03:00
rendered_js: false
word_count: 301
summary: This document provides documentation for the dap snapshot command, detailing its usage, available flags, and parameters for downloading full dataset snapshots.
tags:
    - dap-cli
    - data-snapshots
    - command-line-interface
    - canvas-data
    - dataset-extraction
category: reference
---

The `dap snapshot` command downloads full snapshots of datasets at a specific point in time. This is ideal for creating an initial full copy of the dataset or performing occasional full updates. Snapshots are useful for comprehensive analyses, audits, and backups.

Regular use of snapshots is not recommended, as they are resource-intensive for the API and costly to process on the client side.

```
dap [arguments] snapshot [flags]
```

`--client-id <string>` Client ID obtained from the Identity Service. Skip, if `DAP_CLIENT_ID` environment variable is set.

`--client-secret <string>` Client Secret obtained from the Identity Service. Skip, if `DAP_CLIENT_SECRET` environment variable is set.

`--namespace <string>` Specifies the data source (namespace). Available options: {canvas, canvas\_log, catalog}.

`--table <string>` Specifies the table(s) to fetch data from. Can be a single table name, a comma separated list of table names or the special `all` keyword to fetch all tables in the namespace.

`--format <string> (default: JSONL)` Defines the output format. Available options: {CSV, JSONL, Parquet, TSV}.

`--output-directory <string>` Specifies the absolute or relative path to the output directory where the snapshot will be stored.

`-h, --help` Displays help information for the command.

Get a snapshot of the `courses` table from the `canvas` namespace: `$ dap snapshot --namespace canvas --table courses`

Get a snapshot of multiple tables or all tables of the `canvas` namespace: `$ dap snapshot --namespace canvas --table courses,users,wikis` `$ dap snapshot --namespace canvas --table all`

Get a snapshot of the `web_logs` table from `canvas_log` namespace in CSV format `$ dap snapshot --namespace canvas_logs --table web_logs --format csv`

[](https://developerdocs.instructure.com/services/dap/key-concepts)

Get familiar with the key concepts in DAP.

[](https://developerdocs.instructure.com/services/dap/limits-policies)

Learn more about the limits and our policies in DAP.

[](https://developerdocs.instructure.com/services/dap/dataset)

Discover the available namespaces and tables.

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).