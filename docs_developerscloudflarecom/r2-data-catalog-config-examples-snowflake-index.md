---
title: Snowflake · Cloudflare R2 docs
url: https://developers.cloudflare.com/r2/data-catalog/config-examples/snowflake/index.md
source: llms
fetched_at: 2026-01-24T15:35:42.490697607-03:00
rendered_js: false
word_count: 72
summary: This document provides a step-by-step guide and SQL examples for connecting Snowflake to the Cloudflare R2 Data Catalog to query Iceberg tables.
tags:
    - snowflake
    - cloudflare-r2
    - r2-data-catalog
    - apache-iceberg
    - sql-integration
    - external-volume
category: tutorial
---

Below is an example of using [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg-configure-catalog-integration-rest) to connect and query data from R2 Data Catalog (read-only).

## Prerequisites

* Sign up for a [Cloudflare account](https://dash.cloudflare.com/sign-up/workers-and-pages).
* [Create an R2 bucket](https://developers.cloudflare.com/r2/buckets/create-buckets/) and [enable the data catalog](https://developers.cloudflare.com/r2/data-catalog/manage-catalogs/#enable-r2-data-catalog-on-a-bucket).
* [Create an R2 API token](https://developers.cloudflare.com/r2/api/tokens/) with both [R2 and data catalog permissions](https://developers.cloudflare.com/r2/api/tokens/#permissions).
* A [Snowflake](https://www.snowflake.com/) account with the necessary privileges to create external volumes and catalog integrations.

## Example usage

In your Snowflake [SQL worksheet](https://docs.snowflake.com/en/user-guide/ui-snowsight-worksheets-gs) or [notebook](https://docs.snowflake.com/en/user-guide/ui-snowsight/notebooks), run the following commands:

```sql
-- Create a database (if you don't already have one) to organize your external data
CREATE DATABASE IF NOT EXISTS r2_example_db;


-- Create an external volume pointing to your R2 bucket
CREATE OR REPLACE EXTERNAL VOLUME ext_vol_r2
    STORAGE_LOCATIONS = (
        (
            NAME = 'my_r2_storage_location'
            STORAGE_PROVIDER = 'S3COMPAT'
            STORAGE_BASE_URL = 's3compat://<bucket-name>'
            CREDENTIALS = (
                AWS_KEY_ID = '<access_key>'
                AWS_SECRET_KEY = '<secret_access_key>'
            )
            STORAGE_ENDPOINT = '<account_id>.r2.cloudflarestorage.com'
        )
    )
    ALLOW_WRITES = FALSE;


-- Create a catalog integration for R2 Data Catalog (read-only)
CREATE OR REPLACE CATALOG INTEGRATION r2_data_catalog
    CATALOG_SOURCE = ICEBERG_REST
    TABLE_FORMAT = ICEBERG
    CATALOG_NAMESPACE = 'default'
    REST_CONFIG = (
        CATALOG_URI = '<catalog_uri>'
        CATALOG_NAME = '<warehouse_name>'
    )
    REST_AUTHENTICATION = (
        TYPE = BEARER
        BEARER_TOKEN = '<token>'
    )
    ENABLED = TRUE;


-- Create an Apache Iceberg table in your selected Snowflake database
CREATE ICEBERG TABLE my_iceberg_table
    CATALOG = 'r2_data_catalog'
    EXTERNAL_VOLUME = 'ext_vol_r2'
    CATALOG_TABLE_NAME = 'my_table';  -- Name of existing table in your R2 data catalog


-- Query your Iceberg table
SELECT * FROM my_iceberg_table;
```