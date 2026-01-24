---
title: Environments · Cloudflare D1 docs
url: https://developers.cloudflare.com/d1/configuration/environments/index.md
source: llms
fetched_at: 2026-01-24T15:11:49.640391444-03:00
rendered_js: false
word_count: 174
summary: This document explains how to configure Cloudflare D1 database bindings for multiple environments using Wrangler configuration files. It provides specific syntax for defining separate database connections for staging and production environments.
tags:
    - cloudflare-d1
    - wrangler-configuration
    - environment-management
    - database-bindings
    - toml
    - jsonc
category: configuration
---

[Environments](https://developers.cloudflare.com/workers/wrangler/environments/) are different contexts that your code runs in. Cloudflare Developer Platform allows you to create and manage different environments. Through environments, you can deploy the same project to multiple places under multiple names.

To specify different D1 databases for different environments, use the following syntax in your Wrangler file:

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "env": {
      "staging": {
        "d1_databases": [
          {
            "binding": "<BINDING_NAME_1>",
            "database_name": "<DATABASE_NAME_1>",
            "database_id": "<UUID1>"
          }
        ]
      },
      "production": {
        "d1_databases": [
          {
            "binding": "<BINDING_NAME_2>",
            "database_name": "<DATABASE_NAME_2>",
            "database_id": "<UUID2>"
          }
        ]
      }
    }
  }
  ```

* wrangler.toml

  ```toml
  # This is a staging environment
  [env.staging]
  d1_databases = [
      { binding = "<BINDING_NAME_1>", database_name = "<DATABASE_NAME_1>", database_id = "<UUID1>" },
  ]


  # This is a production environment
  [env.production]
  d1_databases = [
      { binding = "<BINDING_NAME_2>", database_name = "<DATABASE_NAME_2>", database_id = "<UUID2>" },
  ]
  ```

In the code above, the `staging` environment is using a different database (`DATABASE_NAME_1`) than the `production` environment (`DATABASE_NAME_2`).

## Anatomy of Wrangler file

If you need to specify different D1 databases for different environments, your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) may contain bindings that resemble the following:

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "production": {
      "d1_databases": [
        {
          "binding": "DB",
          "database_name": "DATABASE_NAME",
          "database_id": "DATABASE_ID"
        }
      ]
    }
  }
  ```

* wrangler.toml

  ```toml
  [[production.d1_databases]]
  binding = "DB"
  database_name = "DATABASE_NAME"
  database_id = "DATABASE_ID"
  ```

In the above configuration:

* `[[production.d1_databases]]` creates an object `production` with a property `d1_databases`, where `d1_databases` is an array of objects, since you can create multiple D1 bindings in case you have more than one database.
* Any property below the line in the form `<key> = <value>` is a property of an object within the `d1_databases` array.

Therefore, the above binding is equivalent to:

```json
{
  "production": {
    "d1_databases": [
      {
        "binding": "DB",
        "database_name": "DATABASE_NAME",
        "database_id": "DATABASE_ID"
      }
    ]
  }
}
```

### Example

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "env": {
      "staging": {
        "d1_databases": [
          {
            "binding": "BINDING_NAME_1",
            "database_name": "DATABASE_NAME_1",
            "database_id": "UUID_1"
          }
        ]
      },
      "production": {
        "d1_databases": [
          {
            "binding": "BINDING_NAME_2",
            "database_name": "DATABASE_NAME_2",
            "database_id": "UUID_2"
          }
        ]
      }
    }
  }
  ```

* wrangler.toml

  ```toml
  [[env.staging.d1_databases]]
  binding = "BINDING_NAME_1"
  database_name = "DATABASE_NAME_1"
  database_id = "UUID_1"


  [[env.production.d1_databases]]
  binding = "BINDING_NAME_2"
  database_name = "DATABASE_NAME_2"
  database_id = "UUID_2"
  ```

The above is equivalent to the following structure in JSON:

```json
{
  "env": {
    "production": {
      "d1_databases": [
        {
          "binding": "BINDING_NAME_2",
          "database_id": "UUID_2",
          "database_name": "DATABASE_NAME_2"
        }
      ]
    },
    "staging": {
      "d1_databases": [
        {
          "binding": "BINDING_NAME_1",
          "database_id": "UUID_1",
          "database_name": "DATABASE_NAME_1"
        }
      ]
    }
  }
}
```