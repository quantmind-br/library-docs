---
title: Mongo Compass | Dokploy
url: https://docs.dokploy.com/docs/core/databases/connection/mongo-atlas
source: crawler
fetched_at: 2026-02-14T14:19:01.741982-03:00
rendered_js: true
word_count: 96
summary: This guide provides step-by-step instructions for configuring and connecting MongoDB Compass to a database hosted on Dokploy using external credentials.
tags:
    - mongodb
    - mongo-compass
    - dokploy
    - database-connection
    - remote-access
    - external-port
category: guide
---

This guide will cover how to configure a Mongo Compass connection for your applications in dokploy or panel.

1. Download and install Mongo Compass [Mongo Compass](https://www.mongodb.com/try/download/compass).
2. Go to your `MongoDB` databases.
3. In External Credentials, enter the `External Port (Internet)` make sure the port is not in use by another service eg. `27017` and click `Save`.
4. It will display the `External Connection URL` eg. `mongodb://user:password@1.2.4.5:27017/database`.

Open Mongo Compass and follow the steps:

1. Click on `Add Connection`.
2. Copy and paste the `External Connection URL` eg. `mongodb://user:password@1.2.4.5:27017/database`.
3. Click on `Connect`.

Done! now you can manage the database from Mongo Compass.