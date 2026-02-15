---
title: dap initdb | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/dap-cli-readme/dap-cli-reference/dap-cli-reference-initdb
source: sitemap
fetched_at: 2026-02-15T09:11:38.135872-03:00
rendered_js: false
word_count: 282
summary: This document explains how to use the dap initdb command to automatically fetch schemas and data from the Data Access Platform to initialize a local database.
tags:
    - dap-cli
    - database-initialization
    - schema-sync
    - command-line-interface
    - data-migration
category: reference
---

The `dap initdb` command automatically fetches the schema and data from DAP, connects to your specified database, creates the necessary table based on the schema, and inserts the data into the table. This process simplifies the initialization of a database with DAP data.

**Type juggling is not supported.** The data types specified in the schema from the DAP API must be strictly followed during table creation and data insertion.

```
dap [arguments] initdb [flags]
```

`--client-id <string>` Client ID obtained from the Identity Service. Skip, if `DAP_CLIENT_ID` environment variable is set.

`--client-secret <string>` Client Secret obtained from the Identity Service. Skip, if `DAP_CLIENT_SECRET` environment variable is set.

`--namespace <string>` Specifies the data source (namespace). Available options: {canvas, canvas\_log, catalog}.

`--table <string>` Specifies the table(s) to fetch data from. Can be a single table name, a comma separated list of table names or the special `all` keyword to fetch all tables in the namespace.

`--connection-string <string>` The connection string used to connect to the target database. It must follow RFC 3986 format: `dialect://username:password@host:port/database`. Skip, if `DAP_CONNECTION_STRING` environment variable is set.

`-h, --help` Displays help information for the command.

Get a snapshot of the `courses` and `users` tables from the `canvas` namespace and insert into your database: `$ dap initdb --namespace canvas --table courses,users`

Example with all tables in the namespace and the connection string defined in the command: `$dap initdb --namespace canvas --table all --connection-string postgresql://scott:password@server.example.com/testdb`

[](https://developerdocs.instructure.com/services/dap/key-concepts)

Get familiar with the key concepts in DAP.

[](https://developerdocs.instructure.com/services/dap/limits-policies)

Learn more about the limits and our policies in DAP.

[](https://developerdocs.instructure.com/services/dap/dataset)

Discover the available namespaces and tables.

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).