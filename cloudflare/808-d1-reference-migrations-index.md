---
title: Migrations · Cloudflare D1 docs
url: https://developers.cloudflare.com/d1/reference/migrations/index.md
source: llms
fetched_at: 2026-01-24T15:12:20.855424598-03:00
rendered_js: false
word_count: 322
summary: This document explains how to version and manage database changes using the D1 migration system, covering how to create, list, and apply SQL migration files.
tags:
    - cloudflare-d1
    - database-migrations
    - wrangler-config
    - sql-migrations
    - database-versioning
category: guide
---

Database migrations are a way of versioning your database. Each migration is stored as an `.sql` file in your `migrations` folder. The `migrations` folder is created in your project directory when you create your first migration. This enables you to store and track changes throughout database development.

## Features

Currently, the migrations system aims to be simple yet effective. With the current implementation, you can:

* [Create](https://developers.cloudflare.com/workers/wrangler/commands/#d1-migrations-create) an empty migration file.
* [List](https://developers.cloudflare.com/workers/wrangler/commands/#d1-migrations-list) unapplied migrations.
* [Apply](https://developers.cloudflare.com/workers/wrangler/commands/#d1-migrations-apply) remaining migrations.

Every migration file in the `migrations` folder has a specified version number in the filename. Files are listed in sequential order. Every migration file is an SQL file where you can specify queries to be run.

Binding name vs Database name

When running a migration script, you can use either the binding name or the database name.

However, the binding name can change, whereas the database name cannot. Therefore, to avoid accidentally running migrations on the wrong binding, you may wish to use the database name for D1 migrations.

## Wrangler customizations

By default, migrations are created in the `migrations/` folder in your Worker project directory. Creating migrations will keep a record of applied migrations in the `d1_migrations` table found in your database.

This location and table name can be customized in your Wrangler file, inside the D1 binding.

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "d1_databases": [
      {
        "binding": "<BINDING_NAME>",
        "database_name": "<DATABASE_NAME>",
        "database_id": "<UUID>",
        "preview_database_id": "<UUID>",
        "migrations_table": "<d1_migrations>",
        "migrations_dir": "<FOLDER_NAME>"
      }
    ]
  }
  ```

* wrangler.toml

  ```toml
  [[ d1_databases ]]
  binding = "<BINDING_NAME>" # i.e. if you set this to "DB", it will be available in your Worker at `env.DB`
  database_name = "<DATABASE_NAME>"
  database_id = "<UUID>"
  preview_database_id = "<UUID>"
  migrations_table = "<d1_migrations>" # Customize this value to change your applied migrations table name
  migrations_dir = "<FOLDER_NAME>" # Specify your custom migration directory
  ```

## Foreign key constraints

When applying a migration, you may need to temporarily disable [foreign key constraints](https://developers.cloudflare.com/d1/sql-api/foreign-keys/). To do so, call `PRAGMA defer_foreign_keys = true` before making changes that would violate foreign keys.

Refer to the [foreign key documentation](https://developers.cloudflare.com/d1/sql-api/foreign-keys/) to learn more about how to work with foreign keys and D1.