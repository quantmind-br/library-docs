---
title: dap list | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/dap-cli-readme/dap-cli-reference/dap-cli-reference-list
source: sitemap
fetched_at: 2026-02-15T09:11:28.032954-03:00
rendered_js: false
word_count: 144
summary: This document provides instructions and parameter details for using the 'dap list' command to retrieve a list of available tables within a specified namespace.
tags:
    - dap-cli
    - table-listing
    - data-access-platform
    - command-line-interface
    - namespace-management
category: reference
---

Get a list of available tables within a selected namespace. This can help you identify which tables are available for further operations, such as snapshots or incremental updates.

```
dap [arguments] list [flags]
```

`--client-id <string>` Client ID obtained from the Identity Service. Skip, if `DAP_CLIENT_ID` environment variable is set.

`--client-secret <string>` Client Secret obtained from the Identity Service. Skip, if `DAP_CLIENT_SECRET` environment variable is set.

`--namespace <string>` Specifies the data source (namespace). Available options: {canvas, canvas\_log, catalog}.

`-h, --help` Displays help information for the command.

List tables from the `canvas` namespace `$ dap list --namespace canvas`

[](https://developerdocs.instructure.com/services/dap/key-concepts)

Get familiar with the key concepts in DAP.

[](https://developerdocs.instructure.com/services/dap/limits-policies)

Learn more about the limits and our policies in DAP.

[](https://developerdocs.instructure.com/services/dap/dataset)

Discover the available namespaces and tables.

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).