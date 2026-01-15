---
title: PostgreSQL-backed Configuration and Token Store
url: https://help.router-for.me/configuration/storage/pgsql
source: crawler
fetched_at: 2026-01-14T22:09:56.860716179-03:00
rendered_js: false
word_count: 172
summary: This document explains how to configure CLIProxyAPI to use a PostgreSQL database for persisting configuration and authentication data, detailing environment variables and the internal workings of this setup.
tags:
    - postgresql
    - configuration
    - token-store
    - cli-proxy-api
    - environment-variables
    - database-persistence
category: configuration
---

## PostgreSQL-backed Configuration and Token Store [​](#postgresql-backed-configuration-and-token-store)

You can also persist configuration and authentication data in PostgreSQL when running CLIProxyAPI in hosted environments that favor managed databases over local files.

**Environment Variables**

VariableRequiredDefaultDescription`MANAGEMENT_PASSWORD`YesPassword for the management web UI (required when remote management is enabled).`PGSTORE_DSN`YesPostgreSQL connection string (e.g. `postgresql://user:pass@host:5432/db`).`PGSTORE_SCHEMA`NopublicSchema where the tables will be created. Leave empty to use the default schema.`PGSTORE_LOCAL_PATH`NoCurrent working directoryRoot directory for the local mirror; the server writes to `<value>/pgstore`. If unset and CWD is unavailable, `/tmp/pgstore` is used.

**How it Works**

1. **Initialization:** On startup the server connects via `PGSTORE_DSN`, ensures the schema exists, and creates the `config_store` / `auth_store` tables when missing.
2. **Local Mirror:** A writable cache at `<PGSTORE_LOCAL_PATH or CWD>/pgstore` mirrors `config/config.yaml` and `auths/` so the rest of the application can reuse the existing file-based logic.
3. **Bootstrapping:** If no configuration row exists, `config.example.yaml` seeds the database using the fixed identifier `config`.
4. **Token Sync:** Changes flow both ways—file updates are written to PostgreSQL and database records are mirrored back to disk so watchers and management APIs continue to operate.