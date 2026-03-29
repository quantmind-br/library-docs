---
title: DataHub Extension | goose
url: https://block.github.io/goose/docs/mcp/datahub-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:00.274949056-03:00
rendered_js: true
word_count: 732
summary: This document provides instructions for integrating the DataHub MCP Server with goose to enable AI-driven data discovery and metadata exploration. It covers environment setup, installation, and practical usage examples for data lineage and SQL generation.
tags:
    - datahub
    - mcp-server
    - goose-extension
    - data-lineage
    - metadata-management
    - ai-agents
category: tutorial
---

🎥Plug & Play

Watch the demo

* * *

This tutorial covers how to add the [DataHub MCP Server](https://github.com/acryldata/mcp-server-datahub) as a goose extension to enable AI-powered data discovery, lineage exploration, and metadata querying across your data ecosystem.

TLDR

- goose Desktop
- goose CLI

**Environment Variables**

```
DATAHUB_GMS_URL: <your-datahub-url>
DATAHUB_GMS_TOKEN: <your-datahub-token>
```

## What is DataHub?[​](#what-is-datahub "Direct link to What is DataHub?")

[DataHub](https://datahub.com/) is an open-source metadata platform that provides a unified view of your data ecosystem, cataloging datasets, dashboards, pipelines, and more with rich metadata including ownership, lineage, usage statistics, and data quality information.

The DataHub MCP Server enables AI agents to:

- **Find trustworthy data** using natural language search with trust signals like popularity, quality, and lineage
- **Explore data lineage** to understand upstream and downstream dependencies at table and column level
- **Understand business context** through glossaries, domains, data products, and organizational metadata
- **Generate SQL queries** with help from documentation, lineage, and popular query patterns

Learn more: [DataHub MCP Server Guide](https://docs.datahub.com/docs/features/feature-guides/mcp) | [GitHub Repository](https://github.com/acryldata/mcp-server-datahub)

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before using the DataHub MCP Server, ensure you have:

- **Python 3.10+** and [**uv**](https://docs.astral.sh/uv/#installation) package manager installed
- A **DataHub instance**: [DataHub Cloud](https://www.datahub.com) or [self-hosted DataHub](https://docs.datahub.com/docs/quickstart)
- A [**Personal Access Token**](https://docs.datahub.com/docs/authentication/personal-access-tokens) from your DataHub instance

## Configuration[​](#configuration "Direct link to Configuration")

info

Note that you'll need [uv](https://docs.astral.sh/uv/#installation) installed on your system to run this command, as it uses `uvx`.

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](goose://extension?cmd=uvx&arg=mcp-server-datahub%40latest&id=datahub-mcp&name=DataHub&description=Data%20discovery%20and%20metadata%20platform%20integration&env=DATAHUB_GMS_URL%3DDataHub%20GMS%20URL%20%28e.g.%2C%20https%3A%2F%2Fyour-instance.acryl.io%20or%20http%3A%2F%2Flocalhost%3A8080%29&env=DATAHUB_GMS_TOKEN%3DDataHub%20Personal%20Access%20Token)
2. Click `Yes` to confirm the installation
3. Get your [DataHub Personal Access Token](https://docs.datahub.com/docs/authentication/personal-access-tokens) and paste it in
4. Click `Add Extension`
5. Click the button in the top-left to open the sidebar
6. Navigate to the chat

## Example Usage[​](#example-usage "Direct link to Example Usage")

### Finding Trustworthy Data[​](#finding-trustworthy-data "Direct link to Finding Trustworthy Data")

Find datasets related to your project by describing what you need in natural language.

#### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

> *Find all datasets related to customer transactions that are owned by the analytics team*

#### goose Output[​](#goose-output "Direct link to goose Output")

Desktop

The DataHub extension will search across your data catalog and return relevant datasets with their metadata, including:

- Dataset names and descriptions
- Column names, types, descriptions, and labels
- Owners
- Tags, properties, and glossary terms
- Usage statistics
- Data quality status

### Exploring Data Lineage[​](#exploring-data-lineage "Direct link to Exploring Data Lineage")

I want to remove the "timestamp\_seconds" column from the customer\_orders table. What will break?

#### goose Prompt[​](#goose-prompt-1 "Direct link to goose Prompt")

> *Show me the upstream lineage for the customer\_orders table*

#### goose Output[​](#goose-output-1 "Direct link to goose Output")

Desktop

The extension will traverse the lineage graph and show any:

- Source tables and datasets
- Transformation pipelines
- ETL jobs and workflows
- Downstream columns

That would be impacted by removing the column.

### Generating SQL Queries[​](#generating-sql-queries "Direct link to Generating SQL Queries")

How do I calculate the number of orders made in the USA last year?

#### goose Prompt[​](#goose-prompt-2 "Direct link to goose Prompt")

> *What are the most common queries run against the customer\_orders dataset?*

#### goose Output[​](#goose-output-2 "Direct link to goose Output")

Desktop

The extension will retrieve SQL query history showing:

- Frequently executed queries
- Common join patterns
- Filter conditions
- Aggregation patterns

In addition to column names, types, descriptions, and any labels. This will enable the agent to generate high quality SQL to answer the question.

### Understanding Data Quality & Freshness[​](#understanding-data-quality--freshness "Direct link to Understanding Data Quality & Freshness")

Determine whether a dataset is trustworthy before using it.

#### goose Prompt[​](#goose-prompt-3 "Direct link to goose Prompt")

> *Is the customer\_orders table fresh and free of data quality issues?*

#### goose Output[​](#goose-output-3 "Direct link to goose Output")

Desktop

The extension will fetch:

- Latest data quality assertions and test results
- Freshness / staleness metrics
- Schema change history
- SLA or SLO metadata
- Owner-provided health status

Allowing the agent to warn the user or confirm data trustworthiness.

## Capabilities[​](#capabilities "Direct link to Capabilities")

The DataHub MCP Server provides the following tools:

**`search`**

Search DataHub using structured keyword search (/q syntax) with boolean logic, filters, pagination, and optional sorting by usage metrics.

**`get_lineage`**

Retrieve upstream or downstream lineage for any entity (datasets, columns, dashboards, etc.) with filtering, query-within-lineage, pagination, and hop control.

**`get_dataset_queries`**

Fetch real SQL queries referencing a dataset or column—manual or system-generated—to understand usage patterns, joins, filters, and aggregation behavior.

**`get_entities`**

Fetch detailed metadata for one or more entities by URN; supports batch retrieval for efficient inspection of search results.

**`list_schema_fields`**

List schema fields for a dataset with keyword filtering and pagination, useful when search results truncate fields or when exploring large schemas.

**`get_lineage_paths_between`**

Retrieve the exact lineage paths between two assets or columns, including intermediate transformations and SQL query information.

## Resources[​](#resources "Direct link to Resources")

- [DataHub MCP Server GitHub](https://github.com/acryldata/mcp-server-datahub)
- [DataHub Documentation](https://docs.datahub.com/docs/)
- [DataHub MCP Server Guide](https://docs.datahub.com/docs/features/feature-guides/mcp)
- [Demo Video](https://youtu.be/VXRvHIZ3Eww?t=1878)

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Connection Issues[​](#connection-issues "Direct link to Connection Issues")

If you're having trouble connecting to DataHub:

1. Verify your `DATAHUB_GMS_URL` is correct:
   
   - For DataHub Cloud: `https://your-tenant.acryl.io`
   - For local instances: `http://localhost:8080`
   - For on-premises: `https://datahub.your-company.com`
2. Confirm your Personal Access Token is valid and has appropriate permissions
3. Check network connectivity and firewall rules

### Installation Issues[​](#installation-issues "Direct link to Installation Issues")

If `uvx` is not found:

1. Ensure `uv` is installed: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Restart your terminal or source your shell configuration
3. Verify installation: `which uvx`