---
title: SQL coding style | Moodle Developer Resources
url: https://moodledev.io/general/development/policies/codingstyle/sql
source: sitemap
fetched_at: 2026-02-17T15:59:06.209341-03:00
rendered_js: false
word_count: 126
summary: This document outlines the recommended coding style and best practices for writing SQL queries and fragments, focusing on parameterization and formatting for readability.
tags:
    - sql-coding-style
    - database-queries
    - placeholder-usage
    - sql-formatting
    - best-practices
category: guide
---

This page describes recommended coding style for complex database queries.

Full SQL queries are used in `$DB->get_records_sql()`, `$DB->get_recordset_sql()`, or `$DB->execute()`.

SQL fragments may be used in DML method with \_select() suffix.

All sql queries and fragments should be enclosed in double quotes, do not concat SQL from multiple parts if possible. The single quotes are used for sql strings, it also helps with visual highlighting and SQL code completion in some IDEs.

All variable query parameters must be specified via placeholders. It is possible to use three different types of placeholders: `:named`, `?` and `$1`. It is recommended to use named parameters if there is more than one parameter.

```
$sql="SELECT *
          FROM {some_table}
         WHERE id > :above";
$records=$DB->get_records_sql($sql,['above'=>111]);
```

There are no strict rules for subquery indentation, the deciding factor is good readability - see [MDLSITE-1914](https://moodle.atlassian.net/browse/MDLSITE-1914).