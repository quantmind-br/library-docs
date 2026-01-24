---
title: Drizzle ORM · Cloudflare Hyperdrive docs
url: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/drizzle-orm/index.md
source: llms
fetched_at: 2026-01-24T15:14:45.180135223-03:00
rendered_js: false
word_count: 406
summary: This document provides a step-by-step guide for integrating Drizzle ORM with PostgreSQL databases in Cloudflare Workers using Hyperdrive.
tags:
    - drizzle-orm
    - cloudflare-workers
    - postgresql
    - hyperdrive
    - typescript
    - orm
category: tutorial
---

[Drizzle ORM](https://orm.drizzle.team/) is a lightweight TypeScript ORM with a focus on type safety. This example demonstrates how to use Drizzle ORM with PostgreSQL via Cloudflare Hyperdrive in a Workers application.

## Prerequisites

* A Cloudflare account with Workers access
* A PostgreSQL database
* A [Hyperdrive configuration to your PostgreSQL database](https://developers.cloudflare.com/hyperdrive/get-started/#3-connect-hyperdrive-to-a-database)

## 1. Install Drizzle

Install the Drizzle ORM and its dependencies such as the [postgres](https://github.com/porsager/postgres) driver:

```sh
# postgres 3.4.5 or later is recommended
npm i drizzle-orm postgres dotenv
npm i -D drizzle-kit tsx @types/node
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

## 2. Configure Drizzle

### 2.1. Define a schema

With Drizzle ORM, we define the schema in TypeScript rather than writing raw SQL.

1. Create a folder `/db/` in `/src/`.

2. Create a `schema.ts` file.

3. In `schema.ts`, define a `users` table as shown below.

   ```ts
   // src/db/schema.ts
   import { pgTable, serial, varchar, timestamp } from "drizzle-orm/pg-core";


   export const users = pgTable("users", {
     id: serial("id").primaryKey(),
     name: varchar("name", { length: 255 }).notNull(),
     email: varchar("email", { length: 255 }).notNull().unique(),
     createdAt: timestamp("created_at").defaultNow(),
   });
   ```

### 2.2. Connect Drizzle ORM to the database with Hyperdrive

Use your Hyperdrive configuration for your database when using the Drizzle ORM.

Populate your `index.ts` file as shown below.

```ts
// src/index.ts
import { drizzle } from "drizzle-orm/postgres-js";
import postgres from "postgres";
import { users } from "./db/schema";


export interface Env {
  HYPERDRIVE: Hyperdrive;
}


export default {
  async fetch(request, env, ctx): Promise<Response> {
    // Create a database client with postgres.js driver connected via Hyperdrive
    const sql = postgres(env.HYPERDRIVE.connectionString, {
      // Limit the connections for the Worker request to 5 due to Workers' limits on concurrent external connections
      max: 5,
      // If you are not using array types in your Postgres schema, disable `fetch_types` to avoid an additional round-trip (unnecessary latency)
      fetch_types: false,
    });


    // Create the Drizzle client with the postgres.js connection
    const db = drizzle(sql);


    // Sample query to get all users
    const allUsers = await db.select().from(users);


    return Response.json(allUsers);
  },
} satisfies ExportedHandler<Env>;
```

Note

You may use [node-postgres](https://orm.drizzle.team/docs/get-started-postgresql#node-postgres) or [Postgres.js](https://orm.drizzle.team/docs/get-started-postgresql#postgresjs) when using Drizzle ORM. Both are supported and compatible.

### 2.3. Configure Drizzle-Kit for migrations (optional)

Note

You need to set up the tables in your database so that Drizzle ORM can make queries that work.

If you have already set it up (for example, if another user has applied the schema to your database), or if you are starting to use Drizzle ORM and the schema matches what already exists in your database, then you do not need to run the migration.

You can generate and run SQL migrations on your database based on your schema using Drizzle Kit CLI. Refer to [Drizzle ORM docs](https://orm.drizzle.team/docs/get-started/postgresql-new) for additional guidance.

1. Create a `.env` file the root folder of your project, and add your database connection string. The Drizzle Kit CLI will use this connection string to create and apply the migrations.

   ```toml
   # .env
   # Replace with your direct database connection string
   DATABASE_URL='postgres://user:password@db-host.cloud/database-name'
   ```

2. Create a `drizzle.config.ts` file in the root folder of your project to configure Drizzle Kit and add the following content:

   ```ts
   // drizzle.config.ts
   import "dotenv/config";
   import { defineConfig } from "drizzle-kit";
   export default defineConfig({
     out: "./drizzle",
     schema: "./src/db/schema.ts",
     dialect: "postgresql",
     dbCredentials: {
       url: process.env.DATABASE_URL!,
     },
   });
   ```

3. Generate the migration file for your database according to your schema files and apply the migrations to your database.

   Run the following two commands:

   ```bash
   npx drizzle-kit generate
   ```

   ```bash
   No config path provided, using default 'drizzle.config.ts'
   Reading config file 'drizzle.config.ts'
   1 tables
   users 4 columns 0 indexes 0 fks


   [✓] Your SQL migration file ➜ drizzle/0000_mysterious_queen_noir.sql 🚀
   ```

   ```bash
   npx drizzle-kit migrate
   ```

   ```bash
   No config path provided, using default 'drizzle.config.ts'
   Reading config file 'drizzle.config.ts'
   Using 'postgres' driver for database querying
   ```

## 3. Deploy your Worker

Deploy your Worker.

```bash
npx wrangler deploy
```

## Next steps

* Learn more about [How Hyperdrive Works](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/).
* Refer to the [troubleshooting guide](https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/) to debug common issues.
* Understand more about other [storage options](https://developers.cloudflare.com/workers/platform/storage-options/) available to Cloudflare Workers.