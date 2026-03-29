---
title: DuckDB · Cloudflare R2 docs
url: https://developers.cloudflare.com/r2/data-catalog/config-examples/duckdb/index.md
source: llms
fetched_at: 2026-01-24T15:35:38.344941711-03:00
rendered_js: false
word_count: 86
summary: This document explains how to connect DuckDB to the Cloudflare R2 Data Catalog to manage and query Iceberg tables using the Iceberg REST extension.
tags:
    - duckdb
    - cloudflare-r2
    - data-catalog
    - iceberg
    - sql
    - cloud-storage
category: tutorial
---

Below is an example of using [DuckDB](https://duckdb.org/) to connect to R2 Data Catalog. For more information on connecting to R2 Data Catalog with DuckDB, refer to [DuckDB documentation](https://duckdb.org/docs/stable/core_extensions/iceberg/iceberg_rest_catalogs#r2-catalog).

## Prerequisites

* Sign up for a [Cloudflare account](https://dash.cloudflare.com/sign-up/workers-and-pages).
* [Create an R2 bucket](https://developers.cloudflare.com/r2/buckets/create-buckets/) and [enable the data catalog](https://developers.cloudflare.com/r2/data-catalog/manage-catalogs/#enable-r2-data-catalog-on-a-bucket).
* [Create an R2 API token](https://developers.cloudflare.com/r2/api/tokens/) with both [R2 and data catalog permissions](https://developers.cloudflare.com/r2/api/tokens/#permissions).
* Install [DuckDB](https://duckdb.org/docs/installation/).
  * Note: [DuckDB 1.4.0](https://github.com/duckdb/duckdb/releases/tag/v1.4.0) or greater is required to attach and write to [Iceberg REST Catalogs](https://duckdb.org/docs/stable/core_extensions/iceberg/iceberg_rest_catalogs).

## Example usage

In the [DuckDB CLI](https://duckdb.org/docs/stable/clients/cli/overview.html) (Command Line Interface), run the following commands:

```sql
-- Install the iceberg DuckDB extension (if you haven't already) and load the extension.
INSTALL iceberg;
LOAD iceberg;


-- Install and load httpfs extension for reading/writing files over HTTP(S).
INSTALL httpfs;
LOAD httpfs;


-- Create a DuckDB secret to store R2 Data Catalog credentials.
CREATE SECRET r2_secret (
    TYPE ICEBERG,
    TOKEN '<token>'
);


-- Attach R2 Data Catalog with the following ATTACH statement.
ATTACH '<warehouse_name>' AS my_r2_catalog (
    TYPE ICEBERG,
    ENDPOINT '<catalog_uri>'
);


-- Create the default schema in the catalog and set it as the active schema.
CREATE SCHEMA my_r2_catalog.default;
USE my_r2_catalog.default;


-- Create and populate a sample Iceberg table with data.
CREATE TABLE my_iceberg_table AS SELECT a FROM range(4) t(a);


-- Show all available tables.
SHOW ALL TABLES;


-- Query the Iceberg table you just created.
SELECT * FROM my_r2_catalog.default.my_iceberg_table;
```