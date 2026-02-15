---
title: Data Formats | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/data-formats
source: sitemap
fetched_at: 2026-02-15T09:11:56.668891-03:00
rendered_js: false
word_count: 1279
summary: This document specifies the supported data output formats and metadata structures for API responses, including detailed rules for CSV, JSON Lines, and Parquet.
tags:
    - dap-api
    - data-formats
    - csv
    - json-lines
    - parquet
    - metadata
    - serialization
category: reference
---

Text format is a simple tabular format in which each record (table row) occupies a single line.

- Output always begins with a header row, which lists all metadata and data field names.
- Fields (table columns) are delimited by *tab* characters.
- Non-printable characters and special values are escaped with *backslash* (`\`), as shown below:

Carriage return (ASCII 13)

Backslash (single character)

This format allows data to be easily imported into a database engine, e.g. with PostgreSQL [COPYarrow-up-right](https://www.postgresql.org/docs/current/sql-copy.html).

Output in this format is transmitted as media type `text/plain` in UTF-8 encoding.

## Comma-separated values (CSV)

Comma-separated values (CSV) output follows [RFC 4180arrow-up-right](https://www.ietf.org/rfc/rfc4180.html) with a few extensions:

- Output always begins with a header row, which lists all metadata and data field names.
- Strings are quoted with double quotes (`"`) if they contain special characters such as the double quote itself, the comma delimiter, a newline, a carriage return, a tab character, etc.
- Empty strings are always represented as `""` to avoid ambiguity with missing values.
- Missing values (a.k.a. `NULL`) are represented with no data (no characters between delimiters).
- Each row has the same number of fields.

These extensions allow differentiating empty strings (`""`) from missing values (a.k.a. `NULL`, represented as no data), for which RFC 4180 defines no rules. If a field is missing, the comma separators are still included, i.e. multiple comma separators may follow one another in a row if there is no data in subsequent fields.

Double quotes act as escape sequences inside a quoted string. If there are two consecutive double quote characters (i.e. `""`), the sequence is interpreted as a single double quote character (`"`). If a string contains newline or carriage return characters, they are emitted verbatim (in compliance with RFC 4180). As such, a record may be broken into several lines if the data contains newlines. (Some applications might not interpret these flawlessly, double-check your integration when you deal with CSV files.)

The following example demonstrates some of the above:

```
meta.action,key.pkey,value.prop1,value.prop2
U,1,a string,42
U,2,"a string, but in ""quotes"".",
D,3,,
U,4,"a multi-line
string",
```

Output in this format is transmitted as media type `text/csv` in UTF-8 encoding.

When the output data is represented in the [JSON Linesarrow-up-right](https://jsonlines.org/) format, each record (table row) occupies a single line. Each line is a JSON object, which can be validated against the JSON schema returned by DAP API.

Output in this format is transmitted as media type `application/jsonlines` in UTF-8 encoding.

Please note that JSONL skip values if they have value `NULL`.

Parquet is a columnar storage format that provides efficient data compression and encoding schemes. It is highly optimized for querying large datasets and widely supported.

- **Data Structure**:
  
  - Parquet format stores data in a binary columnar format.
  - It supports complex nested structures, including arrays and maps, efficiently storing schema and data side-by-side.
  - Parquet is self-describing, meaning the schema of the data is embedded in the file, eliminating the need for separate metadata files.
- **File Header**:
  
  - Parquet files do not have a simple header row as seen in TSV or CSV formats. Instead, each file contains the schema embedded at the top.
  - The schema defines the column names, data types, and structural relationships in a format that can be read by various systems (e.g., Apache Hive, Apache Spark).
- **Compression**:
  
  - Data in Parquet files is compressed, and the format supports various compression methods, including Snappy, Gzip, and LZO.
  - Parquet files are compressed in a columnar manner, meaning that each column's values are compressed separately, which improves compression rates.
- **Field Handling**:
  
  - Parquet supports **nullable** fields, and **NULL values** are encoded according to the specified data type.
  - Fields in Parquet are stored using their native data type. For instance, strings are stored as UTF-8 encoded, while integers are stored as binary encoded integers.
- **Use Case**:
  
  - Parquet is ideal for handling **large datasets**, particularly for analytics workloads in big data environments.
  - It is commonly used in conjunction with distributed processing systems such as Apache Spark and Apache Drill.
- **Media Type**:
  
  - Parquet files are transmitted with the media type `application/parquet` when sent over HTTP, and they are typically stored in file systems that support columnar data formats, such as HDFS or AWS S3.
- **Example**: Suppose a Parquet file contains the following dataset:
  
  In Parquet, the schema and data are both embedded. The schema for this file would indicate that `pkey` is an integer, `prop1` is a string, and `prop2` is an integer or null. The data itself would be stored in a columnar format for efficient reading.
- **NULL Handling**:
  
  - Parquet uses **nullable columns** for missing data and stores them efficiently.

Output of DAP API may include record-level metadata in addition to table data.

In tabular formats (such as text and CSV), metadata are included in the output as additional columns. Consider the following example:

```
meta.action,key.pkey,value.prop1,value.prop2
U,1,"value1",42
U,2,"value2",NULL
D,3,,
```

This CSV output has a metadata section (`meta`), a primary key section (`key`) and a record value section (`value`). The metadata section contains a single field called `action`. The key and value sections comprise of several fields: `pkey`, `prop1` and `prop2`.

In the JSON Lines format, metadata, key and value sections are top-level properties `meta`, `key` and `value`, and have properties of their own:

```
{ "meta": { "action": "U", ... }, "key": { "pkey": 1 }, "value": { "prop1": "value1", "prop2": 42 } }
{ "meta": { "action": "U", ... }, "key": { "pkey": 2 }, "value": { "prop1": "value2", "prop2": null } }
{ "meta": { "action": "D", ... }, "key": { "pkey": 3 } }
```

The set of metadata fields returned depends on the context. Some contexts may produce fields that other contexts do not. If output would contain no metadata fields, the section is omitted entirely.

The metadata field `action` identifies whether a record is *upserted* (inserted or updated) or *(hard) deleted* for an incremental query. In the result of a snapshot query, all records are to be understood as upserted.

- Upserted records (denoted by `U`) have all fields present in the data.
- Deleted records (denoted by `D`) only have the primary key field in their data, other field values are missing.

Occasionally, the term *soft delete* is used, which in this context is equivalent to an update, and is denoted with a `U`, and all field values are included in the output.

The metadata field `ts` indicates when a record was last updated in the underlying transactional data lake table. For an incremental query with `since` and `until` timestamp parameters, `ts` for all returned records is always strictly greater than `since`, and always less than or equal to `until`.

The timestamp may correlate to but does not correspond to the real time when the event took place (e.g. when a student enrolled to a course). If you need to know when the event happened, use the timestamp embedded in the data. Specifically, many tables have timestamp data columns such as `created_at` or `updated_at`, which are controlled by the product or application that generates the event (e.g. Canvas).

Timestamps are stored in fields of JSON type `string`, are formatted as per ISO-8601, and are to be understood as in time zone UTC. This is aligned with how timestamps are represented in the OpenAPI format `date-time` as per [RFC 3339arrow-up-right](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14).

Tabular data formats such as CSV cannot capture the hierarchy that JSON can represent easily. Nested JSON objects are flattened before they are included in the output. For example, consider the JSON data:

```
{
    "id": 1,
    "question": {
        "headline": "title",
        "text": "some text"
    },
    "answers": [
        { "answer": "A", "score": 0 },
        { "answer": "B", "score": 1 },
        { "answer": "C", "score": 0 }
    ]
}
```

Here, the property `question` with two fixed sub-properties can be flattened into CSV columns `question.headline` and `question.text`. However, the property `answers` cannot be flattened because the list has an indeterminate cardinality. Items with indeterminate cardinality are transmitted as a JSON string. (Cardinality check is performed on the data (JSON) schema, not the actual data.)

This is how text output would look like after flattening (tabs are shown as four spaces):

```
data.id    data.question.headline    data.question.text    data.answers
1    title    some text    [{"answer":"A","score":0},{"answer":"B","score":1},{"answer":"C","score":0}]
```

In a similar fashion, this is how CSV output would look after flattening:

```
data.id,data.question.headline,data.question.text,data.answers
1,title,some text,"[{""answer"":""A"",""score"":0},{""answer"":""B"",""score"":1},{""answer"":""C"",""score"":0}]"
```

If you wish to avoid format transformations entirely, use the JSON Lines data format.

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).