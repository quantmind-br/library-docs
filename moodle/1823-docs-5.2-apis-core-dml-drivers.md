---
title: DML drivers | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/apis/core/dml/drivers
source: sitemap
fetched_at: 2026-02-17T15:43:28.232867-03:00
rendered_js: false
word_count: 151
summary: This document outlines the native database drivers supported by Moodle's DML layer and provides instructions for configuring query logging.
tags:
    - moodle
    - database-drivers
    - dml
    - query-logging
    - configuration
    - performance
category: guide
---

A number of native drivers are included with Moodle, including those with support for:

- MySQLi
- MariaDB
- PostgreSQL
- Oracle
- Microsoft SQL Server

These drivers are supported using DML Database Driver layer, which has a number of discreet benefits:

- more optimised and probably faster
- consume less memory
- better possibility to improve logging, debugging, profiling, etc.
- less code, easier to fix and maintain
- and more

## Query logging[​](#query-logging "Direct link to Query logging")

The native DML drivers support logging of database queries to database table, which can be enabled in config.php:

config.php

```
$CFG->dboptions=[
'dbpersist'=>0,
//'logall'   => true,
'logslow'=>5,
'logerrors'=>true,
];
```

- `logall` - log all queries - suitable only for developers, causes high server loads
- `logslow` - log queries that take longer than specified number of seconds (float values are accepted)
- `logerrors` - log all error queries

## See also[​](#see-also "Direct link to See also")

- [DML functions](https://moodledev.io/docs/5.2/apis/core/dml): Where all the functions used to handle DB data ([DML](https://en.wikipedia.org/wiki/Data_Manipulation_Language)) are defined.
- [DML exceptions](https://moodledev.io/docs/5.2/apis/core/dml/exceptions): New DML code is throwing exceptions instead of returning false if anything goes wrong