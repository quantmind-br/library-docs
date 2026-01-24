---
title: PyIceberg · Cloudflare R2 docs
url: https://developers.cloudflare.com/r2/data-catalog/config-examples/pyiceberg/index.md
source: llms
fetched_at: 2026-01-24T15:35:39.863134573-03:00
rendered_js: false
word_count: 49
summary: This document provides a step-by-step guide and code example for integrating PyIceberg with the Cloudflare R2 Data Catalog to manage Apache Iceberg tables.
tags:
    - pyiceberg
    - cloudflare-r2
    - data-catalog
    - apache-iceberg
    - python
    - pyarrow
category: tutorial
---

Below is an example of using [PyIceberg](https://py.iceberg.apache.org/) to connect to R2 Data Catalog.

## Prerequisites

* Sign up for a [Cloudflare account](https://dash.cloudflare.com/sign-up/workers-and-pages).
* [Create an R2 bucket](https://developers.cloudflare.com/r2/buckets/create-buckets/) and [enable the data catalog](https://developers.cloudflare.com/r2/data-catalog/manage-catalogs/#enable-r2-data-catalog-on-a-bucket).
* [Create an R2 API token](https://developers.cloudflare.com/r2/api/tokens/) with both [R2 and data catalog permissions](https://developers.cloudflare.com/r2/api/tokens/#permissions).
* Install the [PyIceberg](https://py.iceberg.apache.org/#installation) and [PyArrow](https://arrow.apache.org/docs/python/install.html) libraries.

## Example usage

```py
import pyarrow as pa
from pyiceberg.catalog.rest import RestCatalog
from pyiceberg.exceptions import NamespaceAlreadyExistsError


# Define catalog connection details (replace variables)
WAREHOUSE = "<WAREHOUSE>"
TOKEN = "<TOKEN>"
CATALOG_URI = "<CATALOG_URI>"


# Connect to R2 Data Catalog
catalog = RestCatalog(
    name="my_catalog",
    warehouse=WAREHOUSE,
    uri=CATALOG_URI,
    token=TOKEN,
)


# Create default namespace
catalog.create_namespace("default")


# Create simple PyArrow table
df = pa.table({
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
})


# Create an Iceberg table
test_table = ("default", "my_table")
table = catalog.create_table(
    test_table,
    schema=df.schema,
)
```