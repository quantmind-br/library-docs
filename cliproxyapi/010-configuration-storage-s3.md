---
title: Object Storage-backed Configuration and Token Store
url: https://help.router-for.me/configuration/storage/s3
source: crawler
fetched_at: 2026-01-14T22:09:57.343925374-03:00
rendered_js: false
word_count: 170
summary: This document explains how to configure an object storage service, like S3, to store configuration and authentication records for a system. It details the necessary environment variables and the process by which the system interacts with the object storage.
tags:
    - object-storage
    - configuration
    - authentication
    - s3-compatible
    - environment-variables
category: configuration
---

## Object Storage-backed Configuration and Token Store [​](#object-storage-backed-configuration-and-token-store)

An S3-compatible object storage service can host configuration and authentication records.

**Environment Variables**

VariableRequiredDefaultDescription`MANAGEMENT_PASSWORD`YesPassword for the management web UI (required when remote management is enabled).`OBJECTSTORE_ENDPOINT`YesObject storage endpoint. Include `http://` or `https://` to force the protocol (omitted scheme → HTTPS).`OBJECTSTORE_BUCKET`YesBucket that stores `config/config.yaml` and `auths/*.json`.`OBJECTSTORE_ACCESS_KEY`YesAccess key ID for the object storage account.`OBJECTSTORE_SECRET_KEY`YesSecret key for the object storage account.`OBJECTSTORE_LOCAL_PATH`NoCurrent working directoryRoot directory for the local mirror; the server writes to `<value>/objectstore`. If unset, defaults to current CWD.

**How it Works**

1. **Startup:** The endpoint is parsed (respecting any scheme prefix), a MinIO-compatible client is created in path-style mode, and the bucket is created when missing.
2. **Local Mirror:** A writable cache at `<OBJECTSTORE_LOCAL_PATH or CWD>/objectstore` mirrors `config/config.yaml` and `auths/`.
3. **Bootstrapping:** When `config/config.yaml` is absent in the bucket, the server copies `config.example.yaml`, uploads it, and uses it as the initial configuration.
4. **Sync:** Changes to configuration or auth files are uploaded to the bucket, and remote updates are mirrored back to disk, keeping watchers and management APIs in sync.