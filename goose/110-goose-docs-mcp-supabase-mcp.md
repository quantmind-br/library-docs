---
title: Supabase Extension | goose
url: https://block.github.io/goose/docs/mcp/supabase-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:54.059600043-03:00
rendered_js: true
word_count: 0
summary: This document outlines the database schema for a project, detailing table structures, column definitions, row counts, and relational foreign keys.
tags:
    - database-schema
    - postgresql
    - row-level-security
    - table-definitions
    - metadata
category: reference
---

```
Tables in my project (public schema):

1. users
   - RLS Enabled: Yes
   - Row count: 150
   - Columns: id (uuid), email (text), name (text), created_at (timestamptz), role (text)
   - Primary Key: id
   - Foreign Keys: Referenced by posts.user_id, profiles.user_id

2. posts
   - RLS Enabled: Yes
   - Row count: 342
   - Columns: id (uuid), user_id (uuid), title (text), content (text), created_at (timestamptz)
   - Primary Key: id
   - Foreign Keys: References users.id, referenced by comments.post_id

3. comments
   - RLS Enabled: Yes
   - Row count: 1089
   - Columns: id (uuid), post_id (uuid), user_id (uuid), content (text), created_at (timestamptz)
   - Primary Key: id
   - Foreign Keys: References posts.id, references users.id

4. profiles
   - RLS Enabled: Yes
   - Row count: 150
   - Columns: id (uuid), user_id (uuid), bio (text), avatar_url (text), updated_at (timestamptz)
   - Primary Key: id
   - Foreign Keys: References users.id

5. categories
   - RLS Enabled: No
   - Row count: 12
   - Columns: id (uuid), name (text), description (text), created_at (timestamptz)
   - Primary Key: id

Would you like to query data from any of these tables?
```