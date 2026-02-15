---
title: Examples | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/lib-index/lib-examples
source: sitemap
fetched_at: 2026-02-15T09:11:30.982656-03:00
rendered_js: false
word_count: 1134
summary: This document explains how to use the asynchronous DAP Python client library to retrieve schemas, perform snapshot and incremental data queries, and synchronize data with local databases.
tags:
    - python
    - dap-client
    - asynchronous-programming
    - data-replication
    - sql-replicator
    - incremental-query
    - data-synchronization
category: tutorial
---

DAP client library is following the [asynchronous programming paradigmarrow-up-right](https://docs.python.org/3/library/asyncio.html), and makes use of the new Python keywords `async` and `await`. The examples below have to be executed in an asynchronous context. You can [enter an asynchronous contextarrow-up-right](https://docs.python.org/3/library/asyncio-runner.html#running-an-asyncio-program) by invoking `asyncio.run`. By default, a Python script runs in a synchronous context; you must wrap the examples below into an `async` function, or you will get a syntax error.

First, we need to instantiate the `DAPClient` class:

```
import os
from dap.api import DAPClient
from dap.dap_types import Credentials
from dap.log import configure_logging
client_id:str= os.environ["DAP_CLIENT_ID"]
client_secret:str= os.environ["DAP_CLIENT_SECRET"]
credentials = Credentials.create(client_id=client_id,client_secret=client_secret)
configure_logging()
asyncwithDAPClient(credentials=credentials)as session:
...
```

However, `DAPClient` can automatically extract the value of these parameters from the above environment variables, allowing us to write:

```
asyncwithDAPClient()as session:
...
```

Note that `DAPClient` uses an asynchronous context manager. Keywords such as `async with` are permitted only in an asynchronous context. We can enter such a context by invoking `asyncio.run(my_function(arg1, arg2, ...))`.

Let’s explore a few common use cases with `DAPClient`.

## Obtaining the latest schema

Before we obtain data, we need to get the latest schema of a table. The following example retrieves the JSON schema of the table `accounts` in the namespace `canvas` as a JSON schema object. A JSON object is a recursive Python data structure whose outermost layer is a Python `dict` whose keys are strings (type `str`) and values are JSON objects. We can use the Python package [jsonschemaarrow-up-right](https://python-jsonschema.readthedocs.io/en/stable/) to validate data against this JSON schema.

```
from dap.api import DAPClient
async with DAPClient() as session:
    schema = await session.get_table_schema("canvas", "accounts")
```

We can also save the schema to a file.

```
import os
from dap.api import DAPClient
from dap.log import configure_logging
output_directory: str = os.getcwd()
configure_logging()
async with DAPClient() as session:
    tables = await session.get_tables("canvas")
    for table in tables:
        await session.download_table_schema("canvas", table, output_directory)
```

## Fetching table data with a snapshot query

In order to get an initial copy of the full table contents, we need to perform a snapshot query. The parameter `format` determines the output data format, including CSV, TSV, JSONL and Parquet. We recommend JSONL or Parquet. For JSONL, each line in the output can be parsed into a JSON object, conforming to the JSON schema returned above.

```
import os
from dap.api import DAPClient
from dap.dap_types import Format, SnapshotQuery
from dap.log import configure_logging
output_directory = os.getcwd()
configure_logging()
async with DAPClient() as session:
    query = SnapshotQuery(format=Format.JSONL, mode=None)
    await session.download_table_data(
        "canvas", "accounts", query, output_directory, decompress=True
    )
```

## Getting latest changes with an incremental query

Once an initial snapshot has been obtained, we need to keep the data synchronized with DAP. This is possible with incremental queries. The following, more complex example gets all changes since a specified `since` timestamp, and saves each data file on the server to an output file in the local filesystem. The `last_seen` timestamp is typically the `until` returned by a previous incremental query.

```
import os
from datetime import datetime, timezone
from urllib.parse import ParseResult, urlparse
import aiofiles
from dap.api import DAPClient
from dap.dap_types import Format, IncrementalQuery
from dap.log import configure_logging
configure_logging()
# timestamp returned by last snapshot or incremental query
last_seen = datetime(2023, 2, 1, 0, 0, 0, tzinfo=timezone.utc)
async with DAPClient() as session:
    query = IncrementalQuery(
        format=Format.JSONL,
        mode=None,
        since=last_seen,
        until=None,
    )
    result = await session.get_table_data("canvas", "accounts", query)
    resources = await session.get_resources(result.objects)
    for resource in resources.values():
        components: ParseResult = urlparse(str(resource.url))
        file_path = os.path.join(
            os.getcwd(), "data", os.path.basename(components.path)
        )
        async for stream in session.stream_resource(resource):
            async with aiofiles.open(file_path, "wb") as file:
                # save gzip data to file without decompressing
                async for chunk in stream.iter_chunked(64 * 1024):
                    await file.write(chunk)
```

## Replicating data to a database

Earlier sections have shown how to obtain the latest schema, fetch data with a snapshot query, or get the latest changes with an incremental query. These are low-level operations that give you full control over what you do with the data.

However, in most cases we want high-level operations that ensure our database (either running locally or in the cloud) is synchronized with the data in DAP, without paying attention to specifics of data transfer. This is possible with two operations that

1. initialize a database, and
2. synchronize a database with the data in DAP.

In order to replicate data in DAP locally, we must first initialize a database:

```
from dap.api import DAPClient
from dap.integration.database import DatabaseConnection, DatabaseConnectionConfig
from dap.replicator.sql import SQLReplicator
from dap.log import configure_logging
configure_logging()
# Define connection parameters as an object
connection_params = DatabaseConnectionConfig(
    dialect="postgresql",
    host="server.example.com",
    port=5432,
    username="scott",
    password="password",
    database="testdb"
)
# Initialize database connection with the object-based parameters
db_connection = DatabaseConnection(connection_params)
# Use the DAPClient and SQLReplicator
async with DAPClient() as session:
    sql_replicator = SQLReplicator(session, db_connection)
    await sql_replicator.version_upgrade()
    await sql_replicator.initialize(namespace, table_name)
```

Initialization creates a database schema for the DAP namespace, and a corresponding database table for each DAP table. In addition, it creates a *meta-table*, which is a special database table that holds synchronization information, e.g. the last time the data was synchronized with DAP, and the schema version that the locally stored data conforms to. Finally, it issues a snapshot query to DAP API, and populates the database table with output returned by the snapshot query.

## Synchronizing data with a database

Once the table has been initialized, it can be kept up to date using the synchronize operation:

```
db_connection = DatabaseConnection(connection_params)
async with DAPClient() as session:
    sql_replicator = SQLReplicator(session, db_connection)
    await sql_replicator.version_upgrade()
    await sql_replicator.synchronize(namespace, table_name)
```

This inspects the information in the meta-table, and issues an incremental query to DAP API with a `since` timestamp corresponding to the last synchronization time. Based on the results of the incremental query, it inserts new records, updates existing records, and deletes records that have been added to, updated in, or removed from the DAP service.

If the local schema version in the meta-table is identical to the remote schema version in DAP, inserting, updating and deleting records proceeds normally. However, if there is a mismatch, the table structure of the local database has to evolve to match the current structure of the data in DAP. This includes the following schema changes in the back-end:

- A new required (a.k.a. non-nullable) field (column) is added. The new field has a default value assigned to it in the schema.
- A new optional (a.k.a. nullable) field (column) is added to a table.
- A new enumeration value is added to an existing enumeration type.
- A new enumeration type is introduced.
- A field (column) is removed from a table.

Behind the scenes, the client library uses SQL commands such as `ALTER TABLE ... ADD COLUMN ...` or `ALTER TYPE ... ADD VALUE ...` to replicate schema changes in DAP in our local database. If the JSON schema change couldn’t be mapped to a series of these SQL statements, the client library wouldn’t be able to synchronize with DAP using incremental queries, and would have to issue an expensive snapshot query.

Once the local database table structure has been reconciled with the new schema in DAP, and the meta-table has been updated, data synchronization proceeds normally with insert, update and delete SQL statements.

## Dropping data from a database

If some tables are no longer needed, these can be dropped from the database using the following code:

```
db_connection = DatabaseConnection(connection_params)
await SQLDrop(db_connection).drop(namespace, table_names)
```

## Executing operations on multiple tables

Using the `session` operations can be executed on multiple tables (stored in `table_names` string) sequentially:

```
async with DAPClient() as session:
    sql_replicator = SQLReplicator(session, db_connection)
    await sql_replicator.version_upgrade()
    async def replicate_table_fn(namespace: str, table: str) -> None:
        await sql_replicator.initialize(namespace, table)
    await session.execute_operation_on_tables(
        namespace, table_names, "export", replicate_table_fn
    )
```

The `table_names` string can be a single table name, a comma separated list of table names or `all` for all tables in the namespace. The `execute_operation_on_tables` will be run on all tables sequentially regardless of success or failure but will raise an aggregate exception which contains all failures as sub-exceptions in case the operation failed on any individual table. In the future this may change to support running operations on tables concurrently.

The client library uses the Python logging module to log messages. To set up logging either use the `dap.log` utility functions or use the python `logging` module directly. Using the `dap.log` logs can be set up to be exactly the same as in the command line case with a single function call, for example set up `DEBUG` log level, `json` log format and use a log file:

```
configure_logging(
    level="DEBUG",
    format="json",
    file="my_client_app.log",
    namespace="canvas",
    table="accounts",
    client_id=client_id,
)
```

The default log level is `INFO` which will be used if the `level` parameter is omitted, also all other parameters have default values. Using this setup will also ensure that all used modules will log in the same format with the same content, this is especially important if we want to process the logs or send them to a service. If the logging setup in `dap.log` does not cover your requirements then the `logging` module can be used directly.

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).