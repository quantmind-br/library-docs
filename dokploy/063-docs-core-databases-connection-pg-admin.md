---
title: PG Admin | Dokploy
url: https://docs.dokploy.com/docs/core/databases/connection/pg-admin
source: crawler
fetched_at: 2026-02-14T14:19:03.73347-03:00
rendered_js: true
word_count: 141
summary: This guide provides step-by-step instructions for connecting the pgAdmin management tool to a PostgreSQL database hosted on Dokploy using external credentials.
tags:
    - dokploy
    - postgresql
    - pgadmin
    - database-management
    - external-access
    - server-configuration
category: guide
---

This guide will cover how to connect from pgAdmin to your postgres databases in dokploy.

1. Download and install pgAdmin [pgAdmin](https://www.pgadmin.org/download/).
2. Go to your `postgres` databases.
3. In External Credentials, enter the `External Port (Internet)` make sure the port is not in use by another service eg. `5433` and click `Save`.
4. It will display the `External Connection URL` eg. `postgres://user:password@1.2.4.5:5433/database`.

Open pgAdmin and follow the steps:

1. Click on `Add New Server`.
2. Enter the `Server Name` eg. `dokploy`.
3. Enter to `Connection`.
4. In Hostname/Address enter the IP from the server where the database is hosted eg. `1.2.4.5`.
5. In Port enter the port where the database is running eg. `5433`.
6. In Database enter the name of the database eg. `database`.
7. In Username enter the username eg. `user`.
8. In Password enter the password eg. `password`.
9. Click on `Save`.

Done! now you can manage the database from pgAdmin.