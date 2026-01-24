---
title: Build a distributed configuration store · Cloudflare Workers KV docs
url: https://developers.cloudflare.com/kv/examples/distributed-configuration-with-workers-kv/index.md
source: llms
fetched_at: 2026-01-24T15:16:25.128869151-03:00
rendered_js: false
word_count: 505
summary: Explains how to use Workers KV for storing application configuration data, covering both writing data from external sources via the REST API and reading it within a Worker to personalize applications.
tags:
    - workers-kv
    - configuration-management
    - cloudflare-workers
    - rest-api
    - node-js
    - database-sync
category: tutorial
---

Storing application configuration data is an ideal use case for Workers KV. Configuration data can include data to personalize an application for each user or tenant, enable features for user groups, restrict access with allow-lists/deny-lists, etc. These use-cases can have high read volumes that are highly cacheable by Workers KV, which can ensure low-latency reads from your Workers application.

In this example, application configuration data is used to personalize the Workers application for each user. The configuration data is stored in an external application and database, and written to Workers KV using the REST API.

## Write your configuration from your external application to Workers KV

In some cases, your source-of-truth for your configuration data may be stored elsewhere than Workers KV. If this is the case, use the Workers KV REST API to write the configuration data to your Workers KV namespace.

The following external Node.js application demonstrates a simple scripts that reads user data from a database and writes it to Workers KV using the REST API library.

* index.js

  ```js
  const postgres = require('postgres');
  const { Cloudflare } = require('cloudflare');
  const { backOff } = require('exponential-backoff');


  if(!process.env.DATABASE_CONNECTION_STRING || !process.env.CLOUDFLARE_EMAIL || !process.env.CLOUDFLARE_API_KEY || !process.env.CLOUDFLARE_WORKERS_KV_NAMESPACE_ID || !process.env.CLOUDFLARE_ACCOUNT_ID) {
  console.error('Missing required environment variables.');
  process.exit(1);
  }


  // Setup Postgres connection
  const sql = postgres(process.env.DATABASE_CONNECTION_STRING);


  // Setup Cloudflare REST API client
  const client = new Cloudflare({
  apiEmail: process.env.CLOUDFLARE_EMAIL,
  apiKey: process.env.CLOUDFLARE_API_KEY,
  });


  // Function to sync Postgres data to Workers KV
  async function syncPreviewStatus() {
  console.log('Starting sync of user preview status...');


      try {
        // Get all users and their preview status
        const users = await sql`SELECT id, preview_features_enabled FROM users`;


        console.log(users);


        // Create the bulk update body
        const bulkUpdateBody = users.map(user => ({
          key: user.id,
          value: JSON.stringify({
            preview_features_enabled: user.preview_features_enabled
          })
        }));


        const response = await backOff(async () => {
          console.log("trying to update")
          try{
            const response = await client.kv.namespaces.bulkUpdate(process.env.CLOUDFLARE_WORKERS_KV_NAMESPACE_ID, {
              account_id: process.env.CLOUDFLARE_ACCOUNT_ID,
              body: bulkUpdateBody
            });
          }
          catch(e){
            // Implement your error handling and logging here
            console.log(e);
            throw e; // Rethrow the error to retry
          }
        });


        console.log(`Sync complete. Updated ${users.length} users.`);
      } catch (error) {
        console.error('Error syncing preview status:', error);
      }


  }


  // Run the sync function
  syncPreviewStatus()
  .catch(console.error)
  .finally(() => process.exit(0));
  ```

* .env

  ```md
  DATABASE_CONNECTION_STRING = <DB_CONNECTION_STRING_HERE>
  CLOUDFLARE_EMAIL = <CLOUDFLARE_EMAIL_HERE>
  CLOUDFLARE_API_KEY = <CLOUDFLARE_API_KEY_HERE>
  CLOUDFLARE_ACCOUNT_ID = <CLOUDFLARE_ACCOUNT_ID_HERE>
  CLOUDFLARE_WORKERS_KV_NAMESPACE_ID = <CLOUDFLARE_WORKERS_KV_NAMESPACE_ID_HERE>
  ```

* db.sql

  ```sql
  -- Create users table with preview_features_enabled flag
  CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    preview_features_enabled BOOLEAN DEFAULT false
  );


  -- Insert sample users
  INSERT INTO users (username, email, preview_features_enabled) VALUES
  ('alice', 'alice@example.com', true),
  ('bob', 'bob@example.com', false),
  ('charlie', 'charlie@example.com', true);
  ```

In this code snippet, the Node.js application reads user data from a Postgres database and writes the user data to be used for configuration in our Workers application to Workers KV using the Cloudflare REST API Node.js library. The application also uses exponential backoff to handle retries in case of errors.

## Use configuration data from Workers KV in your Worker application

With the configuration data now in the Workers KV namespace, we can use it in our Workers application to personalize the application for each user.

* index.ts

  ```js
  // Example configuration data stored in Workers KV:
  // Key: "user-id-abc" | Value: {"preview_features_enabled": false}
  // Key: "user-id-def" | Value: {"preview_features_enabled": true}


  interface Env {
    USER_CONFIGURATION: KVNamespace;
  }


  export default {
    async fetch(request, env) {
      // Get user ID from query parameter
      const url = new URL(request.url);
      const userId = url.searchParams.get('userId');


      if (!userId) {
        return new Response('Please provide a userId query parameter', {
          status: 400,
          headers: { 'Content-Type': 'text/plain' }
        });
      }




      const userConfiguration = await env.USER_CONFIGURATION.get<{
        preview_features_enabled: boolean;
      }>(userId, {type: "json"});


      console.log(userConfiguration);


      // Build HTML response
      const html = `
        <!DOCTYPE html>
        <html>
          <head>
            <title>My App</title>
            <style>
              body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
              }
              .preview-banner {
                background-color: #ffeb3b;
                padding: 10px;
                text-align: center;
                margin-bottom: 20px;
                border-radius: 4px;
              }
            </style>
          </head>
          <body>
            ${userConfiguration?.preview_features_enabled ? `
              <div class="preview-banner">
                🎉 You have early access to preview features! 🎉
              </div>
            ` : ''}
            <h1>Welcome to My App</h1>
            <p>This is the regular content everyone sees.</p>
          </body>
        </html>
      `;


      return new Response(html, {
        headers: { "Content-Type": "text/html; charset=utf-8" }
      });
    }
  } satisfies ExportedHandler<Env>;
  ```

* wrangler.jsonc

  ```json
  {
    "$schema": "node_modules/wrangler/config-schema.json",
    "name": "<ENTER_WORKER_NAME>",
    "main": "src/index.ts",
    "compatibility_date": "2025-03-03",
    "observability": {
      "enabled": true
    },
    "kv_namespaces": [
      {
        "binding": "USER_CONFIGURATION",
        "id": "<YOUR_BINDING_ID>"
      }
    ]
  }
  ```

This code will use the path within the URL and find the file associated to the path within the KV store. It also sets the proper MIME type in the response to inform the browser how to handle the response. To retrieve the value from the KV store, this code uses `arrayBuffer` to properly handle binary data such as images, documents, and video/audio files.

## Optimize performance for configuration

To optimize performance, you may opt to consolidate values in fewer key-value pairs. By doing so, you may benefit from higher caching efficiency and lower latency.

For example, instead of storing each user's configuration in a separate key-value pair, you may store all users' configurations in a single key-value pair. This approach may be suitable for use-cases where the configuration data is small and can be easily managed in a single key-value pair (the [size limit for a Workers KV value is 25 MiB](https://developers.cloudflare.com/kv/platform/limits/)).

## Related resources

* [Rust support in Workers](https://developers.cloudflare.com/workers/languages/rust/)
* [Using KV in Workers](https://developers.cloudflare.com/kv/get-started/)