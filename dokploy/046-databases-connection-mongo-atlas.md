---
title: Mongo Compass | Dokploy
url: https://docs.dokploy.com/docs/core/databases/connection/mongo-atlas
source: crawler
fetched_at: 2026-02-08T04:02:25.470610958-03:00
rendered_js: false
word_count: 96
summary: This document provides step-by-step instructions for configuring an external MongoDB Compass connection to manage databases hosted on Dokploy or Panel.
tags:
    - mongodb
    - mongodb-compass
    - dokploy
    - external-access
    - database-management
    - connection-setup
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