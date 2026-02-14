---
title: MariaDB | Dokploy
url: https://docs.dokploy.com/docs/core/databases/connection/mariadb
source: crawler
fetched_at: 2026-02-14T14:13:27.161209-03:00
rendered_js: true
word_count: 108
summary: This guide provides instructions for establishing a connection between Beekeeper Studio and a MariaDB database hosted on Dokploy using external connection credentials.
tags:
    - beekeeper-studio
    - mariadb
    - dokploy
    - database-management
    - external-access
category: guide
---

This guide will cover how to connect from Beekeeper Studio to your mariadb databases in dokploy.

1. Download and install Beekeeper Studio [Beekeeper Studio](https://www.beekeeperstudio.io/get).
2. Go to your `mariadb` databases.
3. In External Credentials, enter the `External Port (Internet)` make sure the port is not in use by another service eg. `3307` and click `Save`.
4. It will display the `External Connection URL` eg. `mysql://user:password@1.2.4.5:3306/database`.

Open Beekeeper Studio and follow the steps:

1. Click on `Add New Server`.
2. Select `MariaDB` as the `Database Type`.
3. Use `Import URL` to enter the `External Connection URL` from Dokploy eg. `mysql://user:password@1.2.4.5:3306/database`.
4. Click on `Connect`.
5. Click on `Save`.

Done! now you can manage the database from Beekeeper Studio.