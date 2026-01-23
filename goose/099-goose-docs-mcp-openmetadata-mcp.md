---
title: OpenMetadata Extension | goose
url: https://block.github.io/goose/docs/mcp/openmetadata-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:34.636742188-03:00
rendered_js: true
word_count: 392
summary: This document explains how the OpenMetadata MCP Server extension enables natural language interactions for managing metadata, glossaries, and data lineage within the goose agent.
tags:
    - openmetadata
    - mcp-server
    - goose
    - data-lineage
    - metadata-management
    - ai-agent
category: guide
---

The [OpenMetadata MCP Server](https://open-metadata.org/mcp) extension allows goose to interact directly with your OpenMetadata, enabling operations for OpenMetadata assets, glossaries, and lineage. This makes it easy to work with your metadata stored in OpenMetadata through natural language interactions.

The OpenMetadata MCP server connects to an OpenMetadata instance using OpenMetadata's embedded MCP server. We're using `http://localhost:8585` as an example here to access a local OpenMetadata instance, but you can configure this for your own environment. AUTH\_HEADER here would an [OpenMetadata Personal Access Token (PAT)](https://docs.open-metadata.org/latest/how-to-guides/mcp#adding-a-personal-access-token-to-your-mcp-client).

The OpenMetadata extension provides comprehensive metadata management capabilities through natural language interactions. You can perform a wide range of operations including:

Just describe what you want to accomplish in natural language, and goose will help you execute the appropriate OpenMetadata operations safely and efficiently.

In this example, goose looks at the metadata for a Redshift table named `customers` stored in OpenMetadata, particularly its lineage. If the lineage does not show that a Databricks table named `customerinfo` is used to build `customers`, goose will add it.

```
which tables are used to create my customers table in redshift? if the databricks table customerinfo is not already, add it to the customers table lineage.
```

```
Based on my analysis, I found your Redshift customers table at `redshift prod.dev.dbt_jaffle.customers`. Here are the tables currently used to create it:

##### Current Upstream Tables for Redshift Customers Table
###### Direct Dependencies:
1. `redshift prod.dev.dbt_jaffle.stg_customers` (Staging Table for Customers)
2. `redshift prod.dev.dbt_jaffle.stg_payments`
3. `redshift prod.dev.dbt_jaffle.stg_orders`

######Indirect Dependencies (Raw Tables):
4. `redshift prod.dev.dbt_jaffle.raw_customers` → feeds into `stg_customers`
5. `redshift prod.dev.dbt_jaffle.raw_payments` → feeds into `stg_payments`
6. `redshift prod.dev.dbt_jaffle.raw_orders` → feeds into `stg_orders`

######Missing Databricks CustomerInfo Table
I found your Databricks `customerinfo` table at:

`DatabricksBanking.demo.mssqlbanking_customer.customerinfo`
This table is NOT currently connected to your Redshift customers table lineage.

I have successfully created the lineage between the Databricks customerinfo table and the Redshift customers table. Here's what I accomplished:
######Lineage Created Successfully
Source Table (Databricks):

Name: `customerinfo`
Full Name: `DatabricksBanking.demo.mssqlbanking_customer.customerinfo`
Platform: Databricks
Columns: customerid, firstname, lastname, dateofbirth, email, phonenumber, _fivetran_deleted, _fivetran_synced

Target Table (Redshift):

Name: `customers`
Full Name: `redshift prod.dev.dbt_jaffle.customers`
Platform: Redshift
Columns: customer_id, first_name, last_name, first_order, most_recent_order, number_of_orders, customer_lifetime_value

The lineage relationship now shows that the Databricks customerinfo table is an upstream source that feeds data to create the Redshift customers table. This relationship will be visible in OpenMetadata's lineage view, helping you track data flow and understand dependencies between your Databricks and Redshift systems.
You can now view this lineage in the OpenMetadata UI by navigating to either table and checking the "Lineage" tab to see the connection between these customer data assets.
```