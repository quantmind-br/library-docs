---
title: dap syncdb | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/dap-cli-readme/dap-cli-reference/dap-cli-reference-syncdb
source: sitemap
fetched_at: 2026-02-15T08:57:26.36755-03:00
rendered_js: false
word_count: 324
summary: This document explains how to use the dap syncdb command to perform incremental data synchronization between a specified namespace and a target database using atomic transactions.
tags:
    - dap-client
    - data-synchronization
    - cli-command
    - incremental-updates
    - database-integration
    - metadata-management
category: reference
---

Automatically retrieves incremental updates of a table, connects to your database, and applies these updates to the target table. This process is handled within a single atomic transaction, ensuring that, in case of an error, the data in your database remains consistent. Only tables that were created by `dap initdb` can be synchronized using `dap syncdb`.

The timestamp for performing incremental queries is stored in the `dap_meta` table, along with other metadata about synchronized tables. The `dap_meta` table is maintained by the DAP client library and should not be modified or dropped.

```
dap [arguments] syncdb [flags]
```

`--client-id <string>` Client ID obtained from the Identity Service. Skip, if `DAP_CLIENT_ID` environment variable is set.

`--client-secret <string>` Client Secret obtained from the Identity Service. Skip, if `DAP_CLIENT_SECRET` environment variable is set.

`--namespace <string>` Specifies the data source (namespace). Available options: {canvas, canvas\_log, catalog}.

`--table <string>` Specifies the table(s) to fetch data from. Can be a single table name, a comma separated list of table names or the special `all` keyword to fetch all tables in the namespace.

`--connection-string <string>` The connection string used to connect to the target database. It must follow RFC 3986 format: `dialect://username:password@host:port/database`. Skip, if `DAP_CONNECTION_STRING` environment variable is set.

`-h, --help` Displays help information for the command.

Get new or modified records of the `courses` table from the `canvas` namespace and insert into your database: `$ dap syncdb --namespace canvas --table courses`

Get new or modified records of multiple tables or all tables of the `canvas` namespace: `$ dap snapshot --namespace canvas --table courses,users,wikis` `$ dap snapshot --namespace canvas --table all`

Same example with the connection string defined in the command `$dap syncdb --namespace canvas --table courses --connection-string postgresql://scott:password@server.example.com/testdb`

[](https://developerdocs.instructure.com/services/dap/key-concepts)

Get familiar with the key concepts in DAP.

[](https://developerdocs.instructure.com/services/dap/limits-policies)

Learn more about the limits and our policies in DAP.

[](https://developerdocs.instructure.com/services/dap/dataset)

Discover the available namespaces and tables.

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).