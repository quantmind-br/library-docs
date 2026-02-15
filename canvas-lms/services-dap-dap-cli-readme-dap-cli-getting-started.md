---
title: Getting Started | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/dap-cli-readme/dap-cli-getting-started
source: sitemap
fetched_at: 2026-02-15T09:11:01.772411-03:00
rendered_js: false
word_count: 543
summary: This document provides step-by-step instructions for installing and configuring the Data Access Platform (DAP) CLI to sync Canvas data with external databases. It details the process of managing credentials, setting environment variables, and using commands for full snapshots and incremental data updates.
tags:
    - canvas-data-2
    - dap-cli
    - database-sync
    - credential-management
    - api-setup
    - data-integration
category: guide
---

## 1. Get API Client ID and Secret

To access the DAP API, you will need a Client ID and Secret. These are generated via the Instructure Identity Services.

1. Select your institution from the drop-down menu and log in.
2. Once authorized, navigate to the dashboard and click **Add New Key**.
3. Enter a name for the key and set the expiration time.
4. Copy the **Client ID** and **Secret** when they appear. **Note:** These are displayed only once. If you lose them, you will need to generate new ones.

## 2. Install DAP CLI on Your Computer

The DAP CLI tool allows you to interact with the Canvas Data 2 API. Installation steps differ slightly depending on your operating system.

1. Install Xcode Developer Tools:
2. Install PIP (if not installed by default):
3. Install the DAP CLI tool with PostgreSQL support:
   
   ```
   pip3install"instructure-dap-client[postgresql]"
   ```

<!--THE END-->

1. Install the DAP CLI tool using the Windows command prompt:
   
   ```
   pip3 install "instructure-dap-client[postgresql]"
   ```
   
   If you miss installing an extra feature, the library will not be able to synchronize data with a database, and you may get an error message similar to the following:
   
   `ERROR - missing dependency: asyncpg;`
   
   In this case you may need to run
   
   ```
   pip install pysqlsync[postgresql]
   ```

## 3. Store Client Credentials in Environment Variables

For secure access to the API, it's recommended to store your credentials as environment variables. This prevents sensitive information from being exposed in command-line arguments.

1. Open Terminal and run the following commands, replacing placeholders with your actual Client ID and Secret:
   
   ```
   export DAP_CLIENT_ID='your_canvas_data_client_id'
   export DAP_CLIENT_SECRET='your_canvas_data_secret'
   ```
2. Restart Terminal for changes to take effect.

Follow this [guide to setting environment variablesarrow-up-right](https://www.computerhope.com/issues/ch000549.htm) or use the `set` command in the Windows command line:

```
set DAP_CLIENT_ID=your_canvas_data_client_id
set DAP_CLIENT_SECRET=your_canvas_data_secret
```

Unless you set environment variables, you need to pass Client ID and Secret to the dap command explicitly:

```
dap --client-id=us-east-1#0c59cade-...-2ac120002 --client-secret=xdEC0lI...4X4QBOhM incremental --namespace canvas --table accounts --since 2022-07-13T09:30:00+02:00
```

DAP CLI allows you to interact with PostgreSQL, MySQL or MSSQL databases. You will need the connection string of your database for DAP to function correctly.

#### Connection String Format:

```
protocol://username:password@host:port/database_name
```

```
postgresql://user:password@host:5432/mydatabase
mysql://user:password@host:3306/mydatabase
mssql://user:password@host:1433/mydatabase
```

### Store Connection String in Environment Variables

1. Open Terminal and run the following commands, replacing placeholders with your actual Client ID and Secret:
   
   ```
   export DAP_CONNECTION_STRING=postgresql://user:password@localhost:5432/mydatabase
   ```
2. Restart Terminal for changes to take effect.

Follow this [guide to setting environment variablesarrow-up-right](https://www.computerhope.com/issues/ch000549.htm) or use the `set` command in the Windows command line:

```
set DAP_CONNECTION_STRING=postgresql://user:password@localhost:5432/mydatabase
```

### Obtain Full Snapshots of Tables

Use the [`dap initdb`](https://developerdocs.instructure.com/services/dap/dap-cli-readme/dap-cli-reference/dap-cli-reference-initdb) command to download full snapshots of tables and store them in your database.

```
dap initdb --connection-string postgresql://user:password@localhost/mydb --namespace canvas --table accounts,users
```

Regular use of snapshots is not recommended, as they are resource-intensive for the API and costly to process on the client side.

### Synchronize Data of Tables

After obtaining snapshots, keep your database updated with the [`dap syncdb`](https://developerdocs.instructure.com/services/dap/dap-cli-readme/dap-cli-reference/dap-cli-reference-syncdb) command. This ensures incremental changes are applied to your tables.

```
dap syncdb --connection-string postgresql://user:password@localhost/mydb --namespace canvas --table accounts,users
```

### Changing the Temporary Storage Location

If you need to change the temporary storage directory for data processing, you can configure the location using the following command-line option:

```
dap syncdb --temp-dir /new/temp/location --connection-string postgresql://user:password@localhost/mydb --namespace canvas --table accounts,users
```

You can export data using either the snapshot or incremental methods, depending on your use case.

Use [`dap snapshot`](https://developerdocs.instructure.com/services/dap/dap-cli-readme/dap-cli-reference/dap-cli-reference-snapshot) command to download a full copy of tables at a point in time.

```
dap snapshot --namespace canvas --table accounts
```

Regular use of snapshots is not recommended, as they are resource-intensive for the API and costly to process on the client side.

The [`dap incremental`](https://developerdocs.instructure.com/services/dap/dap-cli-readme/dap-cli-reference/dap-cli-reference-incremental) commands captures only the data that has changed since your last export.

```
dap incremental --namespace canvas --table accounts --since YYYY-MM-DDTHH:MM:SSZ
```

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).