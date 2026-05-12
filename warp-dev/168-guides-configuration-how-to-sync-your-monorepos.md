---
title: Sync Your Monorepos | Guides | Warp
url: https://docs.warp.dev/guides/configuration/how-to-sync-your-monorepos
source: sitemap
fetched_at: 2026-04-29T15:06:39.645889575-03:00
rendered_js: false
word_count: 141
summary: This tutorial explains how to use Warp's Rules system to automate synchronization of types and schemas across multiple inter-related repositories.
tags:
    - automation
    - monorepo
    - type-safety
    - repository-management
    - workflow-optimization
    - schema-sync
category: tutorial
optimized: true
optimized_at: 2026-04-29T15:06:39.645889575-03:00
---
Use Warp's Rules system to link interrelated repositories and automate type/schema updates across your stack.

## The Problem

Splitting projects across repos (backend, client, shared schema) causes manual sync errors. Developers forget to propagate type changes.

## The Solution

Define **global Rules** in Warp that teach your agent the relationships between repos. Warp automatically updates types and schemas when you change one place.

## Rule Setup

Describe each repository and its connection:

```
We have three inter-related projects in ~/Repos:
warp-internal (client-side application)
warp-server (server application)
warp-proto-apis (shared API schemas for each)
When you update the schema types, push to git and update the installed types in the server and client by the commit hash.
```

### When Schema Updates — Update Server Types

`cd` into the server repository and run commands to regenerate/update server-side types.

### When Schema Updates — Update Client Types

`cd` into the client repository and run commands to regenerate/update client-side types.

## Benefits

- Keeps **schema, server, and client** perfectly in sync
- Reduces merge conflicts and version drift
- Saves manual steps when committing or deploying

#monorepo #type-safety #workflow-optimization
