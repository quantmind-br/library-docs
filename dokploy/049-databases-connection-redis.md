---
title: Redis | Dokploy
url: https://docs.dokploy.com/docs/core/databases/connection/redis
source: crawler
fetched_at: 2026-02-08T04:02:27.115275434-03:00
rendered_js: false
word_count: 99
summary: This document provides a step-by-step guide on how to connect the RedisInsight desktop application to a Redis database hosted on the Dokploy platform using external connection credentials.
tags:
    - redis
    - redis-insight
    - dokploy
    - database-management
    - external-access
category: guide
---

This guide will cover how to connect from RedisInsight to your redis databases in dokploy.

1. Download and install RedisInsight [RedisInsight](https://redis.io/insight/).
2. Go to your `redis` databases.
3. In External Credentials, enter the `External Port (Internet)` make sure the port is not in use by another service eg. `6379` and click `Save`.
4. It will display the `External Connection URL` eg. `redis://user:password@1.2.4.5:6379/database`.

Open RedisInsight and follow the steps:

1. Add Redis Database.
2. Enter the `Host` eg. `1.2.4.5`.
3. Enter the `Port` eg. `6379`.
4. Enter the username eg. `default`.
5. Enter the `Password` eg. `password`.
6. Click on `Save`.

Done! now you can manage the database from RedisInsight.