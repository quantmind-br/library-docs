---
title: Access a private API or website · Cloudflare Workers VPC
url: https://developers.cloudflare.com/workers-vpc/examples/private-api/index.md
source: llms
fetched_at: 2026-01-24T15:33:39.490192304-03:00
rendered_js: false
word_count: 339
summary: This guide explains how to securely connect Cloudflare Workers to private REST APIs using Cloudflare Tunnel and the Workers VPC Service. It covers the setup of a secure tunnel, VPC service configuration, and implementation of Worker bindings to access internal network resources.
tags:
    - cloudflare-workers
    - vpc-service
    - cloudflare-tunnel
    - private-api
    - internal-networking
    - wrangler-config
category: guide
---

This example demonstrates how to access a private REST API that is not exposed to the public internet. In this guide, we will configure a VPC Service for an internal API, create a Worker that makes requests to that API, and deploy the Worker to validate our changes.

## Prerequisites

* A virtual machine/EC2 instance running in your VPC/virtual network
* A private API or website running in your VPC/virtual network with security rules allowing access to the virtual machine that will be running `cloudflared`
* Workers account with Workers VPC access

## 1. Set up Cloudflare Tunnel

A Cloudflare Tunnel creates a secure connection from your private network to Cloudflare. This tunnel will allow Workers to securely access your private resources.

1. Navigate to the [Workers VPC dashboard](https://dash.cloudflare.com/?to=/:account/workers/vpc/tunnels) and select the **Tunnels** tab.

2. Select **Create** to create a new tunnel.

3. Enter a name for your tunnel (for example, `private-api-tunnel`) and select **Save tunnel**.

4. Choose your operating system and architecture. The dashboard will provide specific installation instructions for your environment.

5. Follow the provided commands to download and install `cloudflared` on your VM, and execute the service installation command with your unique token.

The dashboard will confirm when your tunnel is successfully connected. Note the tunnel ID for the next step.

## 2. Create the Workers VPC Service

First, create a Workers VPC Service for your internal API:

```bash
npx wrangler vpc service create api-service \
  --type http \
  --tunnel-id <YOUR_TUNNEL_ID> \
  --ipv4 10.0.1.50 \
  --http-port 8080
```

You can also create a VPC Service for a service using its hostname:

```bash
npx wrangler vpc service create api-service \
  --type http \
  --tunnel-id <YOUR_TUNNEL_ID> \
  --hostname internal-hostname.example.com
```

Note the service ID returned for the next step.

## 3. Configure your Worker

Update your `wrangler.toml`:

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "name": "private-api-gateway",
    "main": "src/index.js",
    "compatibility_date": "2024-01-01",
    "vpc_services": [
      {
        "binding": "INTERNAL_API",
        "service_id": "<YOUR_SERVICE_ID>",
        "remote": true
      }
    ]
  }
  ```

* wrangler.toml

  ```toml
  name = "private-api-gateway"
  main = "src/index.js"
  compatibility_date = "2024-01-01"


  [[vpc_services]]
  binding = "INTERNAL_API"
  service_id = "<YOUR_SERVICE_ID>"
  remote = true
  ```

## 4. Implement the Worker

In your Workers code, use the VPC Service binding in order to send requests to the service:

```js
export default {
  async fetch(request, env, ctx) {
    try {
      // Fetch data from internal API and process it before returning
      const response = await env.INTERNAL_API.fetch("http://10.0.1.50:8080/api/data");


      // Use the response of the private API to perform more logic in Workers, before returning the final response
      return response;
    } catch (error) {
      return new Response("Service unavailable", { status: 503 });
    }
  },
};
```

This guide demonstrates how you could create a simple proxy in your Workers. However, you could use VPC Services to fetch APIs directly and manipulate the responses to enable you to build more full-stack and backend functionality on Workers.

## 5. Deploy and test

Now, you can deploy and test your Worker that you have created:

```bash
npx wrangler deploy
```

```bash
# Test GET request
curl https://private-api-gateway.workers.dev
```

## Next steps

* Add [authentication and authorization](https://developers.cloudflare.com/workers/examples/auth-with-headers/)
* Implement [rate limiting](https://developers.cloudflare.com/durable-objects/api/)
* Set up [monitoring and alerting](https://developers.cloudflare.com/analytics/analytics-engine/)
* Explore [other examples](https://developers.cloudflare.com/workers-vpc/examples/)