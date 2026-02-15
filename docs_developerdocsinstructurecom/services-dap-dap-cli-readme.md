---
title: Command Line (DAP CLI) | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/dap-cli-readme
source: sitemap
fetched_at: 2026-02-15T09:11:37.798936-03:00
rendered_js: false
word_count: 680
summary: This document provides an overview of the Data Access Platform (DAP) CLI, a tool for fetching snapshots and synchronizing educational data with supported databases. It details installation requirements, execution modes, logging configurations, and usage for data integration tasks.
tags:
    - dap-cli
    - data-synchronization
    - educational-data
    - python
    - command-line-tool
    - data-integration
    - incremental-updates
category: guide
---

The Data Access Platform (DAP) CLI is a command-line tool that enables efficient access to large volumes of educational data with high fidelity and low latency. It adheres to a canonical data model and integrates with various educational products.

Built on top of the [Query API](https://developerdocs.instructure.com/services/dap/query-api), DAP CLI allows you to:

- Fetch initial snapshots of data.
- Track incremental changes.
- Initialize and synchronize a supported database with [DAP data](https://developerdocs.instructure.com/services/dap/dataset).

Before using DAP CLI, it is recommended to familiarize yourself with the [key concepts of DAP](https://developerdocs.instructure.com/services/dap/key-concepts).

For developers, a [Python library](https://developerdocs.instructure.com/services/dap/lib-index) implementing the Query API is also available. The CLI is essentially a wrapper around this [library](https://developerdocs.instructure.com/services/dap/lib-index), offering the same robust functionality in a command-line interface for ease of use.

- **Supported Database Integrations:** PostgreSQL 16.3+, MySQL 8.2+, Microsoft SQL Server 2019+
- **Supported Python Versions:** Python 3.11+

The basic syntax is:

```
dap [arguments] [command][flags]
```

Refer to [Reference](https://developerdocs.instructure.com/services/dap/dap-cli-readme/dap-cli-reference) section in the sidebar for a list of available commands. Or, run the `dap --help` command to get this information right in the terminal.

To ensure optimal performance, always use the latest version of DAP CLI. Check your current version with:

To upgrade to the latest version, run:

```
pip install --upgrade instructure-dap-client
pip install --upgrade "instructure-dap-client[postgresql,mysql]"
```

DAP CLI follows the [rate limiting policies of DAP](https://developerdocs.instructure.com/services/dap/limits-policies). Be mindful of these limits when making requests.

Two output modes are supported: `interactive` is meant for human consumption, `non-interactive` is meant for usage in scripts. The output in non-interactive mode is the same as in versions up to `1.4.0`. The content of output streams depends on what mode is set:

command output for scripts

user-friendly messages about execution status

logs according to loglevel

logs according to loglevel

logs according to loglevel

The mode and additional customizations can be set using the following command line options:

- switch from default interactive mode to non-interactive using `--non-interactive`.
- in non-interactive mode logging to console can be disabled with `--no-log-to-console`, using this only the command output on stdout is emitted
- in interactive mode set colors using `--console-theme`, default is `dark` to best fit the usual black terminal background

The default log level is `info`, and messages are printed to the console. To change the log level or save logs to a file, use the following parameters:

```
dap --loglevel debug --logfile dap.log initdb --namespace canvas --table accounts
```

Logs can be written in different formats, the default is `plain` text format. Specifying the `json` format:

```
dap--logformatjsonsyncdb--namespacecanvas--tableaccounts
```

The log lines in the console and the log file will have the exact same content, the content is determined by `--loglevel` and `--logformat`. In `json` format some additional fields are added to all log records, such as the namespace, table and clientId. These additional fields can also be used for filtering when logs are ingested and queried by some services such as Splunk. For unambiguous processing by these services the timestamp format in `json` logs is ISO 8601 with UTC time zone.

The DAP Client sends usage analytics data to pendo.io. By default tracking is enabled and an **opt out** feature is added using the `--no-tracking` command line switch or the `DAP_TRACKING` environment variable. Valid values for `DAP_TRACKING` are: `true`, `false`, `1`, `0`, `yes`, `no`, `on`, `off`. When using as a library set tracking with the `tracking` parameter of `class DAPClient` constructor. The exact list of tracked data is logged on debug loglevel.

When executing the DAP CLI from a shell or other script the exit code can be used to determine if there were errors during execution, only the exit code `0` indicates a successful execution.

When executing on multiple tables it might happen that it fails for some tables, in this case the exit code will be non zero even if it failed only on a single table.

Ideally only output to `stdout` should be used by scripts and not rely on the content of logs in `stderr` as logs may change in the future.

[](https://community.canvaslms.com/t5/Data-and-Analytics-Group/gh-p/data)

Visit our forums to connect with the community and learn more about DAP.

[](mailto:canvasdatahelp@instructure.com)

To report bugs or request new features, open a ticket for our Support Team.

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).