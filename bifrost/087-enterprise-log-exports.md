---
title: Log Exports
url: https://docs.getbifrost.ai/enterprise/log-exports.md
source: llms
fetched_at: 2026-01-21T19:43:28.495761109-03:00
rendered_js: false
word_count: 168
summary: This document explains how to configure and automate log exports from Bifrost to various storage destinations and data warehouses for monitoring and compliance.
tags:
    - log-export
    - data-retention
    - cloud-storage
    - telemetry-data
    - enterprise-features
    - data-warehouse
category: configuration
---

# Log Exports

> Export and analyze request logs, traces, and telemetry data from Bifrost with enterprise-grade data export capabilities for compliance, monitoring, and analytics.

# Log Exports

Bifrost Enterprise provides comprehensive log export capabilities, allowing you to automatically export request logs, traces, and telemetry data to various storage systems and data lakes on configurable schedules.

## Overview

The log export system enables:

* **Scheduled Exports**: Daily, weekly, or monthly automated exports
* **Multiple Destinations**: Object stores, data warehouses, and data lakes
* **Format Flexibility**: JSON, CSV, Parquet, and custom formats
* **Filtering & Transformation**: Export specific data subsets with custom transformations
* **Compliance**: Meet data retention and audit requirements

## Supported Export Destinations

### Object Storage

#### Amazon S3

```json  theme={null}
{
  "export": {
    "destination": "s3",
    "config": {
      "bucket": "bifrost-logs",
      "region": "us-west-2",
      "prefix": "logs/{year}/{month}/{day}/",
      "credentials": {
        "access_key_id": "${AWS_ACCESS_KEY_ID}",
        "secret_access_key": "${AWS_SECRET_ACCESS_KEY}"
      }
    }
  }
}
```

#### Google Cloud Storage

```json  theme={null}
{
  "export": {
    "destination": "gcs",
    "config": {
      "bucket": "bifrost-logs",
      "prefix": "logs/{year}/{month}/{day}/",
      "credentials": {
        "service_account_key": "${GCP_SERVICE_ACCOUNT_KEY}"
      }
    }
  }
}
```

#### Azure Blob Storage

```json  theme={null}
{
  "export": {
    "destination": "azure_blob",
    "config": {
      "container": "bifrost-logs",
      "account_name": "${AZURE_ACCOUNT_NAME}",
      "account_key": "${AZURE_ACCOUNT_KEY}",
      "prefix": "logs/{year}/{month}/{day}/"
    }
  }
}
```

### Data Warehouses & Lakes

#### Snowflake

```json  theme={null}
{
  "export": {
    "destination": "snowflake",
    "config": {
      "account": "your-account.snowflakecomputing.com",
      "database": "BIFROST_LOGS",
      "schema": "PUBLIC",
      "table": "request_logs",
      "warehouse": "COMPUTE_WH",
      "credentials": {
        "username": "${SNOWFLAKE_USERNAME}",
        "password": "${SNOWFLAKE_PASSWORD}"
      }
    }
  }
}
```

#### Amazon Redshift

```json  theme={null}
{
  "export": {
    "destination": "redshift",
    "config": {
      "cluster": "bifrost-cluster",
      "database": "bifrost_logs",
      "schema": "public",
      "table": "request_logs",
      "region": "us-west-2",
      "credentials": {
        "username": "${REDSHIFT_USERNAME}",
        "password": "${REDSHIFT_PASSWORD}"
      }
    }
  }
}
```

#### Google BigQuery

```json  theme={null}
{
  "export": {
    "destination": "bigquery",
    "config": {
      "project_id": "your-project-id",
      "dataset": "bifrost_logs",
      "table": "request_logs",
      "credentials": {
        "service_account_key": "${GCP_SERVICE_ACCOUNT_KEY}"
      }
    }
  }
}
```

## Export Schedules

### Daily Exports

```json  theme={null}
{
  "export": {
    "schedule": "daily",
    "time": "02:00",
    "timezone": "UTC"
  }
}
```

### Weekly Exports

```json  theme={null}
{
  "export": {
    "schedule": "weekly",
    "day": "sunday",
    "time": "03:00",
    "timezone": "UTC"
  }
}
```

### Monthly Exports

```json  theme={null}
{
  "export": {
    "schedule": "monthly",
    "day": 1,
    "time": "04:00",
    "timezone": "UTC"
  }
}
```

## Export Configuration

### Complete Export Configuration Example

```json  theme={null}
{
  "log_exports": {
    "enabled": true,
    "exports": [
      {
        "name": "daily_s3_export",
        "enabled": true,
        "schedule": {
          "frequency": "daily",
          "time": "02:00",
          "timezone": "UTC"
        },
        "destination": {
          "type": "s3",
          "config": {
            "bucket": "bifrost-logs-prod",
            "region": "us-west-2",
            "prefix": "daily-exports/{year}/{month}/{day}/",
            "credentials": {
              "access_key_id": "${AWS_ACCESS_KEY_ID}",
              "secret_access_key": "${AWS_SECRET_ACCESS_KEY}"
            }
          }
        },
        "data": {
          "format": "parquet",
          "compression": "gzip",
          "include": [
            "request_logs",
            "response_logs",
            "error_logs"
          ],
          "filters": {
            "date_range": "last_24_hours",
            "status_codes": [200, 400, 401, 403, 404, 500]
          }
        }
      },
      {
        "name": "weekly_bigquery_export",
        "enabled": true,
        "schedule": {
          "frequency": "weekly",
          "day": "sunday",
          "time": "03:00",
          "timezone": "UTC"
        },
        "destination": {
          "type": "bigquery",
          "config": {
            "project_id": "your-analytics-project",
            "dataset": "bifrost_analytics",
            "table": "weekly_logs",
            "credentials": {
              "service_account_key": "${GCP_SERVICE_ACCOUNT_KEY}"
            }
          }
        },
        "data": {
          "format": "json",
          "include": [
            "request_logs",
            "metrics",
            "traces"
          ],
          "transformations": [
            {
              "type": "aggregate",
              "group_by": ["provider", "model", "customer_id"],
              "metrics": ["total_requests", "avg_latency", "error_rate"]
            }
          ]
        }
      }
    ]
  }
}
```

## Data Formats

### JSON Format

```json  theme={null}
{
  "timestamp": "2024-01-15T10:30:00Z",
  "request_id": "req_123456789",
  "customer_id": "cust_abc123",
  "provider": "openai",
  "model": "gpt-4",
  "endpoint": "/v1/chat/completions",
  "method": "POST",
  "status_code": 200,
  "latency_ms": 1250,
  "input_tokens": 100,
  "output_tokens": 150,
  "cost_usd": 0.0045
}
```

### CSV Format

```csv  theme={null}
timestamp,request_id,customer_id,provider,model,endpoint,method,status_code,latency_ms,input_tokens,output_tokens,cost_usd
2024-01-15T10:30:00Z,req_123456789,cust_abc123,openai,gpt-4,/v1/chat/completions,POST,200,1250,100,150,0.0045
```

### Parquet Schema

```
message log_record {
  required int64 timestamp;
  required binary request_id (UTF8);
  required binary customer_id (UTF8);
  required binary provider (UTF8);
  required binary model (UTF8);
  required binary endpoint (UTF8);
  required binary method (UTF8);
  required int32 status_code;
  required int32 latency_ms;
  optional int32 input_tokens;
  optional int32 output_tokens;
  optional double cost_usd;
}
```

## Data Filtering & Transformation

### Filtering Options

```json  theme={null}
{
  "filters": {
    "date_range": {
      "start": "2024-01-01T00:00:00Z",
      "end": "2024-01-31T23:59:59Z"
    },
    "providers": ["openai", "anthropic", "azure"],
    "models": ["gpt-4", "claude-3-sonnet"],
    "status_codes": [200, 201, 400, 401, 403, 404, 500],
    "customers": ["cust_123", "cust_456"],
    "min_latency_ms": 100,
    "max_latency_ms": 10000,
    "has_errors": true
  }
}
```

### Transformation Options

```json  theme={null}
{
  "transformations": [
    {
      "type": "aggregate",
      "group_by": ["provider", "model", "date"],
      "metrics": [
        "count",
        "avg_latency",
        "p95_latency",
        "total_tokens",
        "total_cost",
        "error_rate"
      ]
    },
    {
      "type": "anonymize",
      "fields": ["customer_id", "request_id"],
      "method": "hash"
    },
    {
      "type": "enrich",
      "add_fields": {
        "export_timestamp": "${EXPORT_TIMESTAMP}",
        "export_version": "${EXPORT_VERSION}"
      }
    }
  ]
}
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt