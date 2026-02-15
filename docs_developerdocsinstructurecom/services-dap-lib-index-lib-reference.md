---
title: Reference | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/lib-index/lib-reference
source: sitemap
fetched_at: 2026-02-15T09:11:31.120745-03:00
rendered_js: false
word_count: 3239
summary: Technical reference for the Data Access Platform (DAP) client proxy, detailing classes and methods for authentication, session management, and data retrieval.
tags:
    - dap-api
    - client-library
    - authentication
    - data-retrieval
    - session-management
    - python-sdk
category: reference
---

A JWT access token. This object is immutable.

The access token counts as sensitive information not to be exposed (e.g. in logs).

#### \_\_init\__ ( self, jwt\_token: str ) → None

Creates a new JWT access token.

Returns the string representation of the JWT access token.

#### is\_expiring ( self ) → bool

Checks if the token is about to expire.

**Returns:** (bool) - True if the token is about to expire.

Client proxy for the Data Access Platform (DAP) server-side API.

In order to invoke high-level functionality such as initializing and synchronizing a database or data warehouse, or low-level functionality such as triggering a snapshot or incremental query, you need to instantiate a client, which acts as a proxy to DAP API.

Tracking for usage analytics is done here as it is needed for both CLI and library use cases, additionally this way it's tied to operations where the DAP service is used (e.g. no tracking for local dropdb)

#### \_\_aenter\__ ( self ) → [DAPSession](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.api.dapsession)

Initiates a new client session.

#### \_\_aexit\__ ( self, exc\_type: Type\[BaseException] | None, exc\_val: BaseException | None, exc\_tb: traceback | None ) → None

Terminates a client session.

#### \_\_init\__ ( self, base\_url: str | None, credentials: [Credentials](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.credentials) | None, tracking: bool | None ) → None

Initializes a new client proxy to communicate with the DAP back-end.

**Bases:** RuntimeError

Represents an authenticated session to DAP.

#### \_\_init\__ ( self, session: ClientSession, base\_url: str, credentials: [Credentials](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.credentials), tracking\_data: TrackingData | None ) → None

Creates a new logical session by encapsulating a network connection.

#### authenticate ( self ) → None

Authenticates with API key to receive a JWT.

Wait until a job terminates.

**Parameters:**

**Returns:** ([TableJob](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.tablejob) | [CompleteSnapshotJob](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.completesnapshotjob) | [CompleteIncrementalJob](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.completeincrementaljob) | [FailedJob](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.failedjob)) - A job that has completed with success or terminated with failure.

Closes the underlying network sockets.

#### download\_object ( self, object: [Object](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.object), output\_directory: str, decompress: bool, progress: JobProgress | None ) → str

Save a single remote file to a local directory.

**Parameters:**

- **object** ([Object](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.object)) - Object to download.
- **output\_directory** (str) - Path of the target directory to save the downloaded file.
- **decompress** (bool) - If True, the file will be decompressed after downloading. Default is False.
- **progress** (JobProgress | None) - A progress bar to update during the download.

**Returns:** (str) - A path of the file saved in the local file system.

#### download\_objects ( self, objects: List\[[Object](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.object)], output\_directory: str, decompress: bool ) → List\[str]

Save data stored remotely into a local directory.

**Parameters:**

- **objects** (List\[[Object](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.object)]) - List of output objects to be downloaded.
- **output\_directory** (str) - Path to the target directory to save downloaded files to.
- **decompress** (bool) - If True, the file will be decompressed after downloading. Default is False.

**Returns:** (List\[str]) - A list of paths to files saved in the local file system.

#### download\_resource ( self, resource: [Resource](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.resource), output\_directory: str, decompress: bool ) → str

Save a single remote file to a local directory.

**Parameters:**

- **resource** ([Resource](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.resource)) - Resource to download.
- **output\_directory** (str) - Path of the target directory to save the downloaded file.
- **decompress** (bool) - If True, the file will be decompressed after downloading. Default is False.

**Returns:** (str) - A path of the file saved in the local file system.

#### download\_resources ( self, resources: List\[[Resource](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.resource)], output\_directory: str, decompress: bool ) → List\[str]

Save data stored remotely into a local directory.

**Parameters:**

- **resources** (List\[[Resource](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.resource)]) - List of output resources to be downloaded.
- **output\_directory** (str) - Path to the target directory to save downloaded files to.
- **decompress** (bool) - If True, the file will be decompressed after downloading. Default is False.

**Returns:** (List\[str]) - A list of paths to files saved in the local file system.

#### download\_table\_data ( self, namespace: str, table: str, query: [SnapshotQuery](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.snapshotquery) | [IncrementalQuery](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.incrementalquery), output\_directory: str, decompress: bool ) → [DownloadTableDataResult](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.downloadtabledataresult)

Executes a query job and downloads data to a local directory.

**Parameters:**

- **namespace** (str) - A namespace identifier such as `canvas` or `mastery`.
- **table** (str) - A table identifier such as `submissions`, `quizzes`, or `users`.
- **output\_directory** (str) - Path to the directory to save downloaded files to.
- **decompress** (bool) - If True, the file will be decompressed after downloading. Default is False.

**Returns:** ([DownloadTableDataResult](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.downloadtabledataresult)) - Result of the query, including a list of paths to files saved in the local file system.

#### download\_table\_schema ( self, namespace: str, table: str, output\_directory: str ) → None

Saves the schema as a JSON file into a local directory.

**Parameters:**

- **namespace** (str) - A namespace identifier such as `canvas` or `mastery`.
- **table** (str) - A table identifier such as `submissions`, `quizzes`, or `users`.
- **output\_directory** (str) - Path to the directory to save the JSON file to.

Start a query job and wait until it terminates.

#### execute\_operation\_on\_tables ( self, namespace: str, tables: str, operation\_name: str, operation: Callable\[\[str, str], Awaitable\[T]] ) → None

Executes given operation on multiple tables in the given namespace. The operations are currently executed in a sequential manner, independently of each other but some error types stop the execution of subsequent operations since in these cases they would also fail.

**Parameters:**

- **namespace** (str) - A namespace identifier such as `canvas` or `mastery`.
- **tables** (str) - A single table, a comma separated list of table names or the special "all".
- **operation\_name** (str) - The CLI command that is being executed.
- **operation** (Callable\[\[str, str], Awaitable\[T]]) - The operation to execute on a single table.

Retrieve job status.

#### get\_job\_status ( self, job\_id: str ) → [JobStatus](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.jobstatus)

Retrieve job status.

#### get\_objects ( self, job\_id: str ) → List\[[Object](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.object)]

Retrieve object IDs once the query is completed successfully.

#### get\_resources ( self, objects: List\[[Object](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.object)] ) → Dict\[str, [Resource](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.resource)]

Retrieve URLs to data stored remotely.

#### get\_table\_data ( self, namespace: str, table: str, query: [SnapshotQuery](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.snapshotquery) | [IncrementalQuery](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.incrementalquery) ) → [GetTableDataResult](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.gettabledataresult)

Executes a query job on a given table.

**Parameters:**

- **namespace** (str) - A namespace identifier such as `canvas` or `mastery`.
- **table** (str) - A table identifier such as `submissions`, `quizzes`, or `users`.

**Returns:** ([GetTableDataResult](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.gettabledataresult)) - Result of the query, including metadata.

#### get\_table\_list ( self, namespace: str, table\_param: str ) → List\[str]

Returns a list of tables on which an operation should be performed. In case of "all" the list of tables for that namespace is retrieved.

**Parameters:**

- **namespace** (str) - A namespace identifier such as `canvas` or `mastery`.
- **table\_param** (str) - can be a single table, a comma separated list of table names or the special "all".

#### get\_table\_schema ( self, namespace: str, table: str ) → [VersionedSchema](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.versionedschema)

Retrieves the versioned schema of a table.

**Parameters:**

- **namespace** (str) - A namespace identifier such as `canvas` or `mastery`.
- **table** (str) - A table identifier such as `submissions`, `quizzes`, or `users`.

**Returns:** ([VersionedSchema](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.versionedschema)) - The schema of the table as exposed by DAP API.

#### get\_tables ( self, namespace: str ) → List\[str]

Retrieves the list of tables available for querying.

**Parameters:**

- **namespace** (str) - A namespace identifier such as `canvas` or `mastery`.

**Returns:** (List\[str]) - A list of tables available for querying in the given namespace.

#### query\_incremental ( self, namespace: str, table: str, query: [IncrementalQuery](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.incrementalquery) ) → [TableJob](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.tablejob) | [CompleteSnapshotJob](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.completesnapshotjob) | [CompleteIncrementalJob](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.completeincrementaljob) | [FailedJob](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.failedjob)

Starts an incremental query.

#### query\_snapshot ( self, namespace: str, table: str, query: [SnapshotQuery](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.snapshotquery) ) → [TableJob](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.tablejob) | [CompleteSnapshotJob](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.completesnapshotjob) | [CompleteIncrementalJob](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.completeincrementaljob) | [FailedJob](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.failedjob)

Starts a snapshot query.

#### stream\_resource ( self, resource: [Resource](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.resource) ) → AsyncIterator\[StreamReader]

Creates a stream reader for the given resource.

**Parameters:**

- **resource** ([Resource](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.resource)) - Resource to download.

**Bases:** [DAPClientError](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.api.dapclienterror)

## Synchronizing a local database

Encapsulates logic that drops table(s) from the SQL database.

#### drop ( self, namespace: str, table\_names: str ) → None

Drops the given database tables.

Encapsulates logic that replicates changes acquired from DAP API in a SQL database.

**Bases:** [CompleteJob](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.completejob)

An incremental query that has completed with success.

**Properties:**

- **since** (datetime) - Start timestamp (in UTC); only those records are returned that have been persisted since the specified date and time.
- **until** (datetime) - End timestamp (in UTC); only those records are returned that have been persisted before the specified date and time. This can be used as a starting point for future incremental queries.

**Bases:** [TableJob](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.tablejob)

A data access job that has completed with success.

**Properties:**

- **objects** (List\[[Object](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.object)]) - The list of objects generated by the job.
- **schema\_version** (int) - Version of the schema that records in the table conform to.

**Bases:** [CompleteJob](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.completejob)

A snapshot query that has completed with success.

**Properties:**

- **at** (datetime) - Timestamp (in UTC) that identifies the table state. This can be used as a starting point for future incremental queries.

Credentials to be passed to Instructure API Gateway.

All Instructure Platform Services go through the API Gateway. Access to credentials is managed via the Instructure Identity Service.

**Properties:**

- **basic\_credentials** (str) - Encoded credentials.
- **client\_id** (str) - The OAuth Client ID.
- **client\_region** (str) - The client's region decoded from the Client ID key.

**Bases:** [TableDataResult](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.tabledataresult)

The result of downloading the output of a snapshot or an incremental query to the local file system.

**Properties:**

- **downloaded\_files** (List\[str]) - A list of paths to files containing the downloaded table data.

**Bases:** [TableJob](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.tablejob)

A data access job that has terminated with failure.

**Properties:**

- **error** ([ProcessingError](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_error.processingerror)) - Provides more details on the error that occurred.

Identifies the format of the data returned, e.g. TSV, CSV, JSON Lines, or Parquet.

Tab-separated values (TSV) is a simple tabular format in which each record (table row) occupies a single line.

- Output always begins with a header row, which lists all metadata and data field names.
- Fields (table columns) are delimited by *tab* characters.
- Non-printable characters and special values are escaped with *backslash* (`\\`).

Comma-separated values (CSV) output follows [RFC 4180arrow-up-right](https://www.ietf.org/rfc/rfc4180.html) with a few extensions:

- Output always begins with a header row, which lists all metadata and data field names.
- Strings are quoted with double quotes (`"`) if they contain special characters such as the double quote itself, the comma delimiter, a newline, a carriage return, a tab character, etc., or if their string representation would be identical to a special value such as NULL.
- Empty strings are always represented as `""`.
- NULL values are represented with the unquoted literal string `NULL`.
- Missing values are presented as an empty string (no characters between delimiters).
- Each row has the same number of fields.

When the output data is represented in the [JSON Linesarrow-up-right](https://jsonlines.org/) format, each record (table row) occupies a single line. Each line is a JSON object, which can be validated against the corresponding JSON schema.

Properties with `null` values are omitted in JSON.

Parquet files are compatible with Spark version 3.0 and later.

**Members:**

- **TSV** = `'tsv'` - Tab-separated values, in compliance with PostgreSQL COPY.
- **CSV** = `'csv'` - Comma-separated values, as per RFC 4180.
- **JSONL** = `'jsonl'` - JSON lines format, with a single JSON object occupying each line.
- **Parquet** = `'parquet'` - Parquet format, as generated by Spark.

**Bases:** [TableDataResult](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.tabledataresult)

The result of fetching the output of a snapshot or an incremental query.

**Properties:**

- **objects** (List\[[Object](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.object)]) - The list of objects generated by the job, which can be traded for resource URLs.

**Bases:** [TableQuery](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.tablequery)

Incremental queries return consolidated updates to a table, and help update a previous state to the present state.

If only a *since* timestamp is given (recommended), the operation returns all changes since the specified point in time. If multiple updates took place to a record since the specified time, only the most recent version of the record is returned.

If both a *since* and an *until* timestamp is given, the operation returns all records that have changed since the start timestamp of the interval but have not been altered after the end timestamp of the interval. Any records that have been updated after the *until* timestamp are not included in the query result. This functionality is useful to break up larger batches of changes but cannot be reliably used as a means of reconstructing a database state in the past (i.e. a point-in-time query or a backup of a previous state).

The range defined by *since* and *until* is inclusive for the *since* timestamp but exclusive for the *until* timestamp.

You would normally use incremental queries to fetch changes since a snapshot query or a previous incremental query. If issued as a follow-up to a snapshot query, the *since* timestamp of the incremental query would be equal to the *at* timestamp of the snapshot query. If issued as a follow-up to an incremental query, you would chain the *until* timestamp returned by the previous query job with the *since* timestamp of the new query request.

**Properties:**

- **since** (datetime) - Start timestamp (in UTC); only those records are returned that have been persisted since the specified date and time. This typically equals `at` returned by a previous snapshot query job, or `until` returned by a previous incremental query job.
- **until** (datetime | None) - End timestamp (in UTC); only those records are returned that have not been changed after the specified date and time. If omitted (recommended), defaults to the commit time of the latest record.

Tracks the lifetime of a job from creation to termination (with success or failure).

**Members:**

Output generation mode controls how nested fixed-cardinality fields are expanded into columns.

Mode `expanded` lays out nested fixed-cardinality fields into several columns. Consider the following example for TSV:

```
meta.ts               meta.action  [key.id](key.id)  value.plain  value.nested.sub1  value.nested.sub2  value.nested.sub3
2023-10-23T01:02:03Z  U            1       string       1                  multi-\nline        \N
```

Mode `condensed` keeps nested fields together. Observe how a nested field becomes a single JSON-valued field:

```
meta.ts               meta.action  [key.id](key.id)  value.plain  value.nested
2023-10-23T01:02:03Z  U            1       string       {"sub1": 1, "sub2": "multi-\\nline"}
```

In case both JSON and the output format (e.g. CSV or TSV) define escaping rules, they are applied consecutively. This is why there are multiple backslash characters in the example above: JSON escapes a newline character as `\n`, and then TSV escapes the backslash character to make the sequence `\\n`.

Properties with `null` values are omitted in condensed nested fields, as in JSON.

If all nested values are *NULL*, the tabular result is empty, not `{}` (empty JSON object). Specifically, TSV would write `\N` (*NULL*) and CSV would write no value (blank field).

Output generation mode does not affect fields `meta` and `key`, which are always expanded. Likewise, variable-cardinality fields (e.g. JSON `array` or `object`) are unaffected by `mode`, and are always exported as JSON.

**Members:**

- **expanded** = `'expanded'` - Nested fixed-cardinality fields are expanded into several columns.
- **condensed** = `'condensed'` - Nested fixed-cardinality fields are exported as embedded JSON.

A reference to a binary or text object persisted in object storage, such as a CSV, JSON, or Parquet file.

The lifetime of the object depends on the operation that created it but typically lasts for 24 hours. Object identifiers can be traded for pre-signed URLs via an authenticated endpoint operation while the object exists.

**Properties:**

- **id** (str) - Uniquely identifies the object.

A pre-signed URL to a binary or text object persisted in object storage, such as a CSV, JSON or Parquet file.

The lifetime of the pre-signed URL depends on the operation that created it but typically lasts for 15 minutes. No authentication is required to fetch the object via the pre-signed URL.

**Properties:**

- **url** ([URL](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.url)) - URL to the object.

Associates object identifiers with pre-signed URLs to output resources.

**Properties:**

- **urls** (Dict\[str, [Resource](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.resource)]) - A dictionary of key-value pairs consisting of an ObjectID and the corresponding resource URL.

**Bases:** [TableQuery](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.tablequery)

Snapshot queries return the present state of the table.

Snapshot queries help populate an empty database. After the initial snapshot query, you would use incremental queries to get the most up-to-date version of the data.

The result of a table query operation.

**Properties:**

- **schema\_version** (int) - Version of the schema that records in the table conform to.
- **timestamp** (datetime) - Timestamp (in UTC) that identifies the table state.
- **job\_id** (str) - The ID of the executed backend job.

A data access job in progress.

**Properties:**

- **id** (str) - Opaque unique identifier of the job.
- **status** ([JobStatus](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.jobstatus)) - The current status of the job.
- **expires\_at** (datetime | None) - The time when job will no longer be available.

A list of tables that exist in the organization domain.

**Properties:**

- **tables** (List\[str]) - A list of table names.

Encapsulates a query request to retrieving data from a table.

**Properties:**

- **format** ([Format](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.format)) - The format of the data to be returned.
- **mode** ([Mode](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_types.mode) | None) - Output generation mode.

An authentication/authorization token issued by API Gateway.

**Properties:**

- **access\_token** (str) - A base64-encoded access token string with header, payload and signature parts.
- **expires\_in** (int) - Expiry time (in sec) of the access token. This field is informational, the timestamp is also embedded in the access token.
- **scope** (str) - List of services accessible by the client. Informational field, as the scope is also embedded in the access token.
- **token\_type** (str) - Type of the access token.

A Uniform Resource Locator (URL).

**Properties:**

- **url** (str) - The URL string.

The state of the schema at a specific point in time.

Schemas are backwards compatible. They receive strictly monotonically increasing version numbers as schema evolution takes place.

**Properties:**

- **schema** (Dict\[str, None | bool | int | float | str | Dict\[str, JsonType] | List\[JsonType]]) - The JSON Schema object to validate against.
- **version** (int) - The version of the schema.

**Bases:** [OperationError](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_error.operationerror)

Raised when the client is onboarded but access is forbidden.

**Bases:** [OperationError](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_error.operationerror)

Raised when the client is not onboarded.

### AccountUnderMaintenanceError

**Bases:** [OperationError](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_error.operationerror)

Raised when account disabled because of maintenance

**Bases:** [OperationError](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_error.operationerror)

Raised when the client fails to provide valid authentication credentials.

**Bases:** Exception

Raised when received timeout from gateway.

**Properties:**

- **message** (str) - Always the same message signaling that a timeout received.

Refers to a location in parsable text input (e.g. JSON, YAML or structured text).

**Properties:**

- **line** (int) - Line number (1-based).
- **column** (int) - Column number w.r.t. the beginning of the line (1-based).
- **character** (int) - Character number w.r.t. the beginning of the input (1-based).

**Bases:** [OperationError](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_error.operationerror)

Raised when an entity does not exist or has expired.

**Properties:**

- **id** (str) - The identifier of the entity not found, e.g. the name of a table or the UUID of a job.
- **kind** (str) - The entity that is not found such as a namespace, table, object or job.

**Bases:** Exception

Encapsulates an error from an endpoint operation.

**Properties:**

- **type** (str) - A machine-processable identifier for the error. Typically corresponds to the fully-qualified exception class, as per the type system of the language that emitted the message (e.g. Java, Python or Scala exception type).
- **uuid** (str) - Unique identifier of the error. This identifier helps locate the exact source of the error (e.g. find the log entry in the server log stream). Make sure to include this identifier when contacting support.
- **message** (str) - A human-readable description for the error for informational purposes. The exact format of the message is unspecified, and implementations should not rely on the presence of any specific information.

**Bases:** [OperationError](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_error.operationerror)

Raised when data is queried outside of the allowed time range.

**Properties:**

- **since** (datetime) - The earliest permitted timestamp.
- **until** (datetime | None) - The latest permitted timestamp.

**Bases:** [OperationError](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_error.operationerror)

Raised when a job has terminated due to an unexpected error.

**Bases:** Exception

An error returned by the server.

**Properties:**

- **body** (Any) - Unspecified content returned by the server.

**Bases:** [OperationError](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_error.operationerror)

Raised when data is queried outside of the allowed time range, and the table was reloaded recently. A new snapshot is required to keep data consistency.

**Properties:**

- **since** (datetime) - The earliest permitted timestamp.
- **until** (datetime | None) - The latest permitted timestamp.

**Bases:** [OperationError](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_error.operationerror)

Raised when a JSON validation error occurs.

**Properties:**

- **location** ([Location](https://developerdocs.instructure.com/services/dap/lib-index/lib-reference#cli.dap.dap_error.location)) - Location of where invalid input was found.

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).