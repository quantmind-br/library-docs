---
title: dap schema | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/dap-cli-readme/dap-cli-reference/dap-cli-reference-schema
source: sitemap
fetched_at: 2026-02-15T08:57:18.435849-03:00
rendered_js: false
word_count: 206
summary: This document provides technical specifications and usage instructions for the 'dap schema' command used to download JSON table schemas from specific namespaces.
tags:
    - dap-cli
    - schema-generation
    - data-access-platform
    - json-schema
    - instructure
    - command-line-interface
category: reference
---

This command generates and downloads the schema of a specific table within a specified namespace in JSON format.

```
dap [arguments] schema [flags]
```

`--client-id <string>` Client ID obtained from the Identity Service. Skip, if `DAP_CLIENT_ID` environment variable is set.

`--client-secret <string>` Client Secret obtained from the Identity Service. Skip, if `DAP_CLIENT_SECRET` environment variable is set.

`--namespace <string>` Specifies the data source (namespace). Available options: {canvas, canvas\_log, catalog}.

`--table <string>` Specifies the tables whose schemas to fetch. Can be a single table name, a comma separated list of table names or the special `all` keyword to fetch all tables in the namespace.

`--output-directory <string> (default: downloads)` Specifies the absolute or relative path to the output directory where the snapshot will be stored.

`-h, --help` Displays help information for the command.

Get schema of `courses` and `users` tables from the `canvas` namespace: `$ dap schema --namespace canvas --table courses,users`

Get schema of all tables from the `canvas` namespace: `$ dap schema --namespace canvas --table all`

[](https://developerdocs.instructure.com/services/dap/key-concepts)

Get familiar with the key concepts in DAP.

[](https://developerdocs.instructure.com/services/dap/limits-policies)

Learn more about the limits and our policies in DAP.

[](https://developerdocs.instructure.com/services/dap/dataset)

Discover the available namespaces and tables.

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).