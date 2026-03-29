---
title: Azure Database · Cloudflare Hyperdrive docs
url: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/azure/index.md
source: llms
fetched_at: 2026-01-24T15:14:49.517581155-03:00
rendered_js: false
word_count: 562
summary: This document provides instructions on how to connect Cloudflare Hyperdrive to an Azure Database for PostgreSQL instance, including network configuration and Worker integration.
tags:
    - cloudflare-hyperdrive
    - azure-postgresql
    - cloudflare-workers
    - database-pooling
    - postgresql
    - wrangler-cli
category: tutorial
---

This example shows you how to connect Hyperdrive to an Azure Database for PostgreSQL instance.

## 1. Allow Hyperdrive access

To allow Hyperdrive to connect to your database, you will need to ensure that Hyperdrive has valid credentials and network access.

Note

To allow Hyperdrive to connect to your database, you must allow Cloudflare IPs to be able to access your database. You can either allow-list all IP address ranges (0.0.0.0 - 255.255.255.255) or restrict your IP access control list to the [IP ranges used by Hyperdrive](https://developers.cloudflare.com/hyperdrive/configuration/firewall-and-networking-configuration/).

Alternatively, you can connect to your databases over in your private network using [Cloudflare Tunnels](https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database/).

### Azure Portal

#### Public access networking

To connect to your Azure Database for PostgreSQL instance using public Internet connectivity:

1. In the [Azure Portal](https://portal.azure.com/), select the instance you want Hyperdrive to connect to.
2. Expand **Settings** > **Networking** > ensure **Public access** is enabled > in **Firewall rules** add `0.0.0.0` as **Start IP address** and `255.255.255.255` as **End IP address**.
3. Select **Save** to persist your changes.
4. Select **Overview** from the sidebar and note down the **Server name** of your instance.

With the username, password, server name, and database name (default: `postgres`), you can now create a Hyperdrive database configuration.

#### Private access networking

To connect to a private Azure Database for PostgreSQL instance, refer to [Connect to a private database using Tunnel](https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database/).

## 2. Create a database configuration

To configure Hyperdrive, you will need:

* The IP address (or hostname) and port of your database.
* The database username (for example, `hyperdrive-demo`) you configured in a previous step.
* The password associated with that username.
* The name of the database you want Hyperdrive to connect to. For example, `postgres`.

Hyperdrive accepts the combination of these parameters in the common connection string format used by database drivers:

```txt
postgres://USERNAME:PASSWORD@HOSTNAME_OR_IP_ADDRESS:PORT/database_name
```

Most database providers will provide a connection string you can directly copy-and-paste directly into Hyperdrive.

* Dashboard

  To create a Hyperdrive configuration with the Cloudflare dashboard:

  1. In the Cloudflare dashboard, go to the **Hyperdrive** page.

     [Go to **Hyperdrive**](https://dash.cloudflare.com/?to=/:account/workers/hyperdrive)

  2. Select **Create Configuration**.

  3. Fill out the form, including the connection string.

  4. Select **Create**.

* Wrangler CLI

  To create a Hyperdrive configuration with the [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/install-and-update/):

  1. Open your terminal and run the following command. Replace `<NAME_OF_HYPERDRIVE_CONFIG>` with a name for your Hyperdrive configuration and paste the connection string provided from your database host, or replace `user`, `password`, `HOSTNAME_OR_IP_ADDRESS`, `port`, and `database_name` placeholders with those specific to your database:

     ```sh
     npx wrangler hyperdrive create <NAME_OF_HYPERDRIVE_CONFIG> --connection-string="postgres://user:password@HOSTNAME_OR_IP_ADDRESS:PORT/database_name"
     ```

  2. This command outputs a binding for the [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/):

     * wrangler.jsonc

       ```jsonc
       {
         "$schema": "./node_modules/wrangler/config-schema.json",
         "name": "hyperdrive-example",
         "main": "src/index.ts",
         "compatibility_date": "2024-08-21",
         "compatibility_flags": [
           "nodejs_compat"
         ],
         "hyperdrive": [
           {
             "binding": "HYPERDRIVE",
             "id": "<ID OF THE CREATED HYPERDRIVE CONFIGURATION>"
           }
         ]
       }
       ```

     * wrangler.toml

       ```toml
       name = "hyperdrive-example"
       main = "src/index.ts"
       compatibility_date = "2024-08-21"
       compatibility_flags = ["nodejs_compat"]


       # Pasted from the output of `wrangler hyperdrive create <NAME_OF_HYPERDRIVE_CONFIG> --connection-string=[...]` above.
       [[hyperdrive]]
       binding = "HYPERDRIVE"
       id = "<ID OF THE CREATED HYPERDRIVE CONFIGURATION>"
       ```

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "name": "hyperdrive-example",
    "main": "src/index.ts",
    "compatibility_date": "2024-08-21",
    "compatibility_flags": [
      "nodejs_compat"
    ],
    "hyperdrive": [
      {
        "binding": "HYPERDRIVE",
        "id": "<ID OF THE CREATED HYPERDRIVE CONFIGURATION>"
      }
    ]
  }
  ```

* wrangler.toml

  ```toml
  name = "hyperdrive-example"
  main = "src/index.ts"
  compatibility_date = "2024-08-21"
  compatibility_flags = ["nodejs_compat"]


  # Pasted from the output of `wrangler hyperdrive create <NAME_OF_HYPERDRIVE_CONFIG> --connection-string=[...]` above.
  [[hyperdrive]]
  binding = "HYPERDRIVE"
  id = "<ID OF THE CREATED HYPERDRIVE CONFIGURATION>"
  ```

Note

Hyperdrive will attempt to connect to your database with the provided credentials to verify they are correct before creating a configuration. If you encounter an error when attempting to connect, refer to Hyperdrive's [troubleshooting documentation](https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/) to debug possible causes.

## 3. Use Hyperdrive from your Worker

Install the `node-postgres` driver:

* npm

  ```sh
  npm i pg@>8.16.3
  ```

* yarn

  ```sh
  yarn add pg@>8.16.3
  ```

* pnpm

  ```sh
  pnpm add pg@>8.16.3
  ```

Note

The minimum version of `node-postgres` required for Hyperdrive is `8.16.3`.

If using TypeScript, install the types package:

* npm

  ```sh
  npm i -D @types/pg
  ```

* yarn

  ```sh
  yarn add -D @types/pg
  ```

* pnpm

  ```sh
  pnpm add -D @types/pg
  ```

Add the required Node.js compatibility flags and Hyperdrive binding to your `wrangler.jsonc` file:

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "compatibility_flags": [
      "nodejs_compat"
    ],
    "compatibility_date": "2024-09-23",
    "hyperdrive": [
      {
        "binding": "HYPERDRIVE",
        "id": "<your-hyperdrive-id-here>"
      }
    ]
  }
  ```

* wrangler.toml

  ```toml
  # required for database drivers to function
  compatibility_flags = ["nodejs_compat"]
  compatibility_date = "2024-09-23"


  [[hyperdrive]]
  binding = "HYPERDRIVE"
  id = "<your-hyperdrive-id-here>"
  ```

Create a new `Client` instance and pass the Hyperdrive `connectionString`:

```ts
// filepath: src/index.ts
import { Client } from "pg";


export default {
  async fetch(
    request: Request,
    env: Env,
    ctx: ExecutionContext,
  ): Promise<Response> {
    // Create a new client instance for each request.
    const client = new Client({
      connectionString: env.HYPERDRIVE.connectionString,
    });


    try {
      // Connect to the database
      await client.connect();
      console.log("Connected to PostgreSQL database");


      // Perform a simple query
      const result = await client.query("SELECT * FROM pg_tables");


      return Response.json({
        success: true,
        result: result.rows,
      });
    } catch (error: any) {
      console.error("Database error:", error.message);


      new Response("Internal error occurred", { status: 500 });
    }
  },
};
```

## Next steps

* Learn more about [How Hyperdrive Works](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/).
* Refer to the [troubleshooting guide](https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/) to debug common issues.
* Understand more about other [storage options](https://developers.cloudflare.com/workers/platform/storage-options/) available to Cloudflare Workers.