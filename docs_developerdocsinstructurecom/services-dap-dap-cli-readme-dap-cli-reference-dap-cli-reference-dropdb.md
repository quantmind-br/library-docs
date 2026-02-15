---
title: dap dropdb | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/dap-cli-readme/dap-cli-reference/dap-cli-reference-dropdb
source: sitemap
fetched_at: 2026-02-15T08:57:19.555096-03:00
rendered_js: false
word_count: 245
summary: This document provides a technical reference for the `dap dropdb` command, which is used to delete tables and their associated synchronization metadata from a target database.
tags:
    - dap-cli
    - database-management
    - table-deletion
    - command-line-interface
    - data-synchronization
    - instructure-dap
category: reference
---

With the `dap dropdb` command, you can completely drop a table from your database that was previously created with `dap initdb`. An error is triggered if the given table does not exist in the target database.

This command not only drops the specified table from the target database but also removes meta-information used for synchronization.

```
dap [arguments] dropdb [flags]
```

`--client-id <string>` Client ID obtained from the Identity Service. Skip, if `DAP_CLIENT_ID` environment variable is set.

`--client-secret <string>` Client Secret obtained from the Identity Service. Skip, if `DAP_CLIENT_SECRET` environment variable is set.

`--namespace <string>` Specifies the data source (namespace). Available options: {canvas, canvas\_log, catalog}.

`--table <string>` Specifies the table(s) to delete. Can be a single table name, a comma separated list of table names or the special `all` keyword to delete all tables in the namespace.

`--connection-string <string>` The connection string used to connect to the target database. It must follow RFC 3986 format: `dialect://username:password@host:port/database`. Skip, if `DAP_CONNECTION_STRING` environment variable is set.

`-h, --help` Displays help information for the command.

Drop the `courses` table from your database: `$ dap dropdb --namespace canvas --table courses`

Drop all locally present tables of the namespace from your database: `$ dap dropdb --namespace canvas --table all`

[](https://developerdocs.instructure.com/services/dap/key-concepts)

Get familiar with the key concepts in DAP.

[](https://developerdocs.instructure.com/services/dap/limits-policies)

Learn more about the limits and our policies in DAP.

[](https://developerdocs.instructure.com/services/dap/dataset)

Discover the available namespaces and tables.

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).