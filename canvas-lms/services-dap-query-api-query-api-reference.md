---
title: Reference | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/query-api/query-api-reference
source: sitemap
fetched_at: 2026-02-15T09:12:17.211239-03:00
rendered_js: false
word_count: 1590
summary: This document outlines the procedures for executing asynchronous data queries, managing job lifecycles, and distinguishing between snapshot and incremental data retrieval methods.
tags:
    - api-endpoints
    - data-querying
    - snapshot-queries
    - incremental-queries
    - job-management
    - async-operations
    - authentication
category: api
---

Jobs (and all objects they created) are deleted 24 hours after the job was started. Deleted jobs are no longer returned by this endpoint.

AuthorizationstringRequired

Authenticates a request by verifying a JWT (JSON Web Token) passed in the `Authorization` HTTP header.

idstringRequired

Unique identifier returned when the job was started by querying data.

200

A snapshot query that has completed with success. **OR** An incremental query that has completed with success. **OR** A data access job that has terminated with failure.

202

A data access job in progress.

401

Client lacks valid authentication credentials.

404

The job does not exist or has expired.

500

The requested account has not been onboarded yet. **OR** The requested account has been onboarded but client access has been restricted. **OR** Internal server error.

504

Gateway timeout error, usually should be handled with retry logic.

In contrast to objects, which have a longer lifetime, pre-signed URLs are valid for a shorter duration, typically 15 minutes.

File paths returned by this endpoint do not adhere to any specification. While they may contain auxiliary information such as job ID or part counter, these are only informative. Downstream systems should not depend on any specific patterns of file names, or make any assumptions how much data each file contains.

AuthorizationstringRequired

Authenticates a request by verifying a JWT (JSON Web Token) passed in the `Authorization` HTTP header.

Bodyobject · Areferencetoabinaryortextobjectpersistedinobjectstorage,suchasaCSV,JSON,orParquetfile.\[]

The lifetime of the object depends on the operation that created it but typically lasts for 24 hours. Object identifiers can be traded for pre-signed URLs via an authenticated endpoint operation while the object exists.

idstringRequired

Uniquely identifies the object.

200

A list of pre-signed URLs.

401

Client lacks valid authentication credentials.

404

Objects do not exist or have expired.

500

The requested account has not been onboarded yet. **OR** The requested account has been onboarded but client access has been restricted. **OR** Internal server error.

504

Gateway timeout error, usually should be handled with retry logic.

This is an asynchronous operation. Calling this endpoint will start a new job and return immediately with status information. However, the operation will continue running on the server. The caller can poll the status of the job to find out when it is ready.

If a job with the same query parameters already exists, its details are returned rather than starting a new job.

If no scope is specified, then the endpoint uses the default scope of the authenticated user. Returns an error if the user has access to several scopes and the scope is not explicitly specified.

For incremental queries, the output uses a special metadata field called `action` to identify whether a record is *upserted* (inserted or updated) or *(hard) deleted* (`U` corresponds to upsert, and `D` to delete):

```
{ "meta": { "action": "U", ... }, "key": { "pkey": 1 }, "value": { "prop1": "value1", "prop2": 42 } }
{ "meta": { "action": "U", ... }, "key": { "pkey": 2 }, "value": { "prop1": "value2", "prop2": null } }
{ "meta": { "action": "D", ... }, "key": { "pkey": 3 } }
```

Upserted records have the primary key fields present in the sub-object `key` and all other data fields in the sub-object `value`. Deleted records only have the primary key fields in the `key` property, and lack the `value` property.

Hard deletes are infrequent. They only take place when a record is irreversibly deleted from the source database, e.g. to comply with privacy or legal requirements.

In most cases, records are *soft-deleted*, i.e. they are updated in such a way as to be understood *deleted* or *inactive* though the record is retained in the database, e.g. by setting a `workflow_state` column to the value `inactive` or `deleted`. In this context, soft deletes are equivalent to an update, and are denoted with a `U`, and all field values are included in the output.

In the rare event that inserting a record is quickly followed by a hard delete in the source database between two successive incremental queries, a record might appear with a new (so far unseen) `key`, no `value` and an `action` of `D`.

For snapshot queries, deleted records are not included in the output:

```
{ "meta": { ... }, "key": { "pkey": 1 }, "value": { "prop1": "value1", "prop2": 42 } }
{ "meta": { ... }, "key": { "pkey": 2 }, "value": { "prop1": "value2", "prop2": null } }
```

This is a rate-limited endpoint. If excessive data volume is requested repeatedly using this endpoint (e.g. a full snapshot every hour), future requests may be denied. We encourage making use of incremental queries, which substantially reduce the amount of data returned.

### Difference between snapshot and incremental Queries:

Snapshot queries and incremental queries serve different purposes in data retrieval and management within the DAP environment.

- **Snapshot Queries:** These queries generate a complete and comprehensive snapshot of the entire dataset at a given point in time. However, note that for the canvas\_logs dataset, particularly the web\_logs table, there is a 30-day data retention policy, so the snapshot will not cover the entire dataset but only the last 30 days of data. Snapshot queries are ideal for creating an initial full copy of the dataset or for occasional full updates. It is not recommended to request snapshots regularly, as it is resource-intensive on the API side and expensive to process on the client side. This approach ensures that you have a full, standalone version of the data, which can be useful for comprehensive analyses, audits, and backups.
- **Incremental Queries:** In contrast, incremental queries retrieve only the changes or updates that have occurred since the last query. This method is more efficient and resource-effective as it minimizes data transfer by only fetching new or modified records. Incremental queries are ideal for keeping your dataset up-to-date with minimal overhead, enabling near-real-time data updates and reducing the need for frequent full dataset downloads.

It is recommended taking a snapshot exactly once (as an initialization step) and then using incremental queries thereafter. By utilizing snapshot queries for initial data load and incremental queries for subsequent updates, users can maintain up-to-date datasets efficiently and effectively.

AuthorizationstringRequired

Authenticates a request by verifying a JWT (JSON Web Token) passed in the `Authorization` HTTP header.

namespacestringRequired

Identifies the domain or product that the request pertains to, e.g. `canvas`.

tablestringRequired

Canonical name of the table whose data to return.

scopestringOptional

Identifies the scope to access, e.g. a root account UUID for Canvas, or a district ID for Mastery.

200

A snapshot query that has completed with success. **OR** An incremental query that has completed with success. **OR** A data access job that has terminated with failure.

202

A data access job in progress.

400

The input is malformed. **OR** There is no data in the requested range. **OR** Raised when data is queried outside of the allowed time range, and the table was reloaded recently.

401

Client lacks valid authentication credentials.

404

The namespace or table does not exist.

500

The requested account has not been onboarded yet. **OR** The requested account has been onboarded but client access has been restricted. **OR** Internal server error.

504

Gateway timeout error, usually should be handled with retry logic.

/query/{namespace}/table/{table}/data

If no scope is specified, then the endpoint uses the default scope of the authenticated user. Returns an error if the user has access to several scopes and the scope is not explicitly specified.

AuthorizationstringRequired

Authenticates a request by verifying a JWT (JSON Web Token) passed in the `Authorization` HTTP header.

namespacestringRequired

Identifies the domain or product that the request pertains to, e.g. `canvas`.

scopestringOptional

Identifies the scope to access, e.g. a root account UUID for Canvas, or a district ID for Mastery.

200

A list of tables in the given scope.

401

Client lacks valid authentication credentials.

404

The namespace does not exist.

500

The requested account has not been onboarded yet. **OR** The requested account has been onboarded but client access has been restricted. **OR** Internal server error.

504

Gateway timeout error, usually should be handled with retry logic.

If data is returned in JSON Lines format (`*.jsonl`) then the schema applies to the JSON object obtained by combining the sub-objects accessed via the `key` and `value` properties, respectively, of JSON items.

Assume the schema reads as follows:

```
{
    "type": "object",
    "properties": {
        "pkey": {
            "type": "integer",
            "format": "int64"
        },
        "prop1": {
            "type": "string"
        },
        "prop2": {
            "type": "integer"
        },
        "additionalProperties": false,
        "required": [
            "pkey",
            "prop1"
        ]
    }
}
```

Suppose we have the following JSON output:

```
{ "meta": { "action": "U", ... }, "key": { "pkey": 1 }, "value": { "prop1": "value1", "prop2": 42 } }
{ "meta": { "action": "U", ... }, "key": { "pkey": 2 }, "value": { "prop1": "value2", "prop2": null } }
{ "meta": { "action": "D", ... }, "key": { "pkey": 3 } }
```

In the example directly above, the first and second items (`update` records) would both validate against the pre-defined schema. The validator would check the following synthesized JSON objects:

```
{ "pkey": 1, "prop1": "value1", "prop2": 42 }
{ "pkey": 2, "prop1": "value2", "prop2": null }
```

The third item (a `delete` record) does not have to validate because it indicates that the client is to remove the item.

If data is returned in Comma-Separated Values format (`*.csv`) then the schema type constraints apply to CSV `key` and `value` columns, respectively, but not CSV `meta` columns. For example, assume we have the following CSV output:

```
meta.action,key.pkey,value.prop1,value.prop2
U,1,"value1",42
U,2,"value2",
D,3,,
```

Then the schema would read the same as in the JSON example above.

Nested JSON objects are flattened to simple fields, with composite names constructed using the dot notation (`parent.child`).

If no scope is specified, then the endpoint uses the default scope of the authenticated user. Returns an error if the user has access to several scopes and the scope is not explicitly specified.

AuthorizationstringRequired

Authenticates a request by verifying a JWT (JSON Web Token) passed in the `Authorization` HTTP header.

namespacestringRequired

Identifies the domain or product that the request pertains to, e.g. `canvas`.

tablestringRequired

Canonical name of the table whose schema to return.

scopestringOptional

Identifies the scope to access, e.g. a root account UUID for Canvas, or a district ID for Mastery.

200

The versioned JSON schema specification for the table.

401

Client lacks valid authentication credentials.

404

The namespace or table does not exist.

500

The requested account has not been onboarded yet. **OR** The requested account has been onboarded but client access has been restricted. **OR** Internal server error.

504

Gateway timeout error, usually should be handled with retry logic.

/query/{namespace}/table/{table}/schema

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).