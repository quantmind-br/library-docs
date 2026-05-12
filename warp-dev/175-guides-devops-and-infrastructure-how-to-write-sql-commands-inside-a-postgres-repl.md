---
title: Write SQL Commands in a Postgres REPL | Guides | Warp
url: https://docs.warp.dev/guides/devops-and-infrastructure/how-to-write-sql-commands-inside-a-postgres-repl
source: sitemap
fetched_at: 2026-04-29T15:07:11.630418786-03:00
rendered_js: false
word_count: 232
summary: This tutorial explains how to use Warp's AI input feature to translate natural-language prompts into executable commands within interactive shell environments like Postgres, Python, and Node.js.
tags:
    - warp-terminal
    - ai-command-generation
    - natural-language-processing
    - repl-workflow
    - sql-automation
    - shell-productivity
category: tutorial
optimized: true
optimized_at: 2026-04-29T15:07:11.630418786-03:00
---
Use **Warp's AI input** to translate plain English into executable SQL inside an interactive Postgres REPL. Works with Node.js, Python, MySQL, and other shells.

## Quick Start

1. Open Warp and connect to Postgres:
   ```bash
   psql -U postgres -d my_database
   ```

2. Open AI input with **Cmd + I** (macOS) or **Ctrl + I** (Windows/Linux)

3. Type or speak natural language requests — Warp translates to SQL

## Basic Queries

**Request:** "Show me our users table and our teams table"

**Generated SQL:**
```sql
SELECT * FROM users;
SELECT * FROM teams;
```

## Context Learning

As you run queries, Warp's AI **learns your database structure** from REPL output. Subsequent prompts become more accurate.

**Example:**
```
Show me all users who joined Warp in the last 90 days from public email accounts
(Gmail, Yahoo, Hotmail) and are on teams of more than two people.
```

**Generated SQL:**
```sql
SELECT *
FROM users
WHERE email LIKE '%gmail.com%'
   OR email LIKE '%yahoo.com%'
   OR email LIKE '%hotmail.com%'
  AND joined_at > NOW() - INTERVAL '90 days'
  AND team_size > 2;
```

## Supported REPLs

| Environment | Supported |
|-------------|-----------|
| PostgreSQL | ✓ |
| Node.js | ✓ |
| Python | ✓ |
| MySQL | ✓ |
| GDB (GNU Debugger) | ✓ |

> [!note]
> Warp automatically detects the active REPL — no need to specify "SQL" or "Python".

## Key Takeaways

- **Cmd + I** activates AI input within any interactive shell
- Warp understands natural language and produces valid commands for the current REPL
- It learns from context — subsequent prompts improve
- Works beyond Postgres: Node, Python, MySQL, and others
- Query or explore systems without memorizing syntax

> [!tip]
> Next time you're stuck remembering a command in Postgres or Python, hit **Cmd + I** and ask Warp in plain English.

#repl-workflow #sql-automation #shell-productivity
