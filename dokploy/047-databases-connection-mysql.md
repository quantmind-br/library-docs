---
title: MySQL | Dokploy
url: https://docs.dokploy.com/docs/core/databases/connection/mysql
source: crawler
fetched_at: 2026-02-08T04:02:26.888513184-03:00
rendered_js: false
word_count: 108
summary: This guide provides step-by-step instructions for connecting the Beekeeper Studio database management tool to a MySQL database hosted on Dokploy using external connection credentials.
tags:
    - dokploy
    - mysql
    - beekeeper-studio
    - database-connection
    - remote-access
    - external-credentials
category: guide
---

This guide will cover how to connect from Beekeeper Studio to your mysql databases in dokploy.

1. Download and install Beekeeper Studio [Beekeeper Studio](https://www.beekeeperstudio.io/get).
2. Go to your `mysql` databases.
3. In External Credentials, enter the `External Port (Internet)` make sure the port is not in use by another service eg. `3306` and click `Save`.
4. It will display the `External Connection URL` eg. `mysql://user:password@1.2.4.5:3306/database`.

Open Beekeeper Studio and follow the steps:

1. Click on `Add New Server`.
2. Select `MySQL` as the `Database Type`.
3. Use `Import URL` to enter the `External Connection URL` from Dokploy eg. `mysql://user:password@1.2.4.5:3306/database`.
4. Click on `Connect`.
5. Click on `Save`.

Done! now you can manage the database from Beekeeper Studio.