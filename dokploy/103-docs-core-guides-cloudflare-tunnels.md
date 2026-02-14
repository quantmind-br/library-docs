---
title: Cloudflare Tunnels | Dokploy
url: https://docs.dokploy.com/docs/core/guides/cloudflare-tunnels
source: crawler
fetched_at: 2026-02-14T14:18:15.166285-03:00
rendered_js: true
word_count: 877
summary: This document provides instructions for integrating Cloudflare Tunnels with Dokploy to securely expose applications without opening inbound firewall ports. It covers the deployment of the cloudflared connector, SSL/TLS configuration, and routing traffic via Traefik for wildcard subdomain support.
tags:
    - cloudflare-tunnel
    - dokploy
    - zero-trust
    - networking
    - traefik
    - secure-access
    - deployment-guide
category: tutorial
---

Learn how to use Cloudflare Tunnels to securely expose your Dokploy applications without opening ports on your server.

Cloudflare Tunnels provide a secure way to connect your applications to the internet without exposing ports on your server. This is particularly useful for home servers or networks where you can't easily configure port forwarding or want enhanced security.

Cloudflare Tunnels (formerly Argo Tunnels) create an encrypted tunnel between your origin server and Cloudflare's global network. Instead of opening ports 80 and 443 on your server, the tunnel establishes an outbound-only connection to Cloudflare, which then routes traffic to your applications.

### [Benefits](#benefits)

- **Enhanced Security**: No need to open inbound ports on your firewall
- **Simple Setup**: Works behind NAT and restrictive firewalls
- **DDoS Protection**: Traffic is routed through Cloudflare's network
- **Free Tier Available**: Included with free Cloudflare accounts
- **Wildcard Support**: Route multiple subdomains through a single tunnel

Before setting up Cloudflare Tunnels with Dokploy, ensure you have:

- A domain managed by Cloudflare (free tier works)
- Dokploy installed and running
- Access to Cloudflare dashboard

When using Cloudflare Tunnels, you should **disable Let's Encrypt** in Dokploy and use HTTP instead of HTTPS for internal connections. Cloudflare handles SSL/TLS termination at their edge.

### [Step 1: Create a Tunnel in Cloudflare](#step-1-create-a-tunnel-in-cloudflare)

- Log in to your [Cloudflare Dashboard](https://dash.cloudflare.com/)
- Navigate to **Zero Trust** (or **Access** in older dashboards)
- Go to **Networks** → **Connectors**
- Click **Create a tunnel**
- Choose **Cloudflared** as the connector type
- Give your tunnel a name (e.g., `dokploy-tunnel`)
- Copy the **Tunnel Token** that's generated (you'll need this later)

Keep your tunnel token secure! It provides access to route traffic to your server.

### [Step 2: Configure SSL/TLS Settings](#step-2-configure-ssltls-settings)

For Cloudflare Tunnels to work properly with Dokploy:

- In Cloudflare Dashboard, go to **SSL/TLS**
- Set the encryption mode to **Full** or **Full (Strict)**

Do not use "Flexible" mode as it may cause redirect loops with Traefik.

### [Step 3: Create Cloudflare Service in Dokploy](#step-3-create-cloudflare-service-in-dokploy)

1. Create a new application
2. Select Docker Provider and set the Image name as `cloudflare/cloudflared`
3. Go to the Environments tab and add the token you copied: `TUNNEL_TOKEN="TOKEN-YOU-COPIED"`
4. Go to the Advanced tab, in the Arguments field add 2 entries: first `tunnel`, second `run`, then click save
5. Deploy the application. You should see the container in healthy status in the logs section

### [Step 4: Configuring Public Hostnames (Domains)](#step-4-configuring-public-hostnames-domains)

After deploying cloudflared, you need to configure which domains route through the tunnel.

#### [Understanding Traefik Routing vs Direct Access](#understanding-traefik-routing-vs-direct-access)

Dokploy uses **Traefik** as its reverse proxy to route traffic to your applications. When configuring Cloudflare Tunnels, you have two options:

**Option 1: Route through Traefik (Recommended)**

- **Traffic flow**: Cloudflare → Tunnel → Traefik → Your Apps
- **Benefits**:
  
  - Support for multiple applications with a single tunnel (wildcard domains)
  - Leverage all Dokploy domain configurations (redirects, path rewrites, etc.)
  - Traefik automatically routes based on the domain you configured in Dokploy
  - Configure once, works for all apps

**Option 2: Direct Container Access**

- **Traffic flow**: Cloudflare → Tunnel → Your App (bypasses Traefik)
- **Benefits**:
  
  - Simpler setup for single applications
  - Slightly lower latency (one less hop)
- **When to use**: For single dedicated services or special cases
- **Note**: You'll need a separate public hostname in Cloudflare for each container

#### [For Applications (via Traefik)](#for-applications-via-traefik)

- In Cloudflare Dashboard, go to your tunnel
- Click **Configure**
- Go to the **Published application routes** tab
- Click **Add a published application route**
- Configure:
  
  - **Subdomain**: Your subdomain (e.g., `app`)
  - **Domain**: Your domain (e.g., `example.com`) - Select from dropdown
  - **Service**:
    
    - **Type**: HTTP
    - **URL**: `dokploy-traefik:80`
- Click **Save**

With this setup, Traefik will route the request to the correct application based on the domain you configured in Dokploy's domain settings.

**Example:**

To test this, let's create a minimal app:

1. Create a simple application
2. Select Docker Provider and set the image name to `nginx`
3. Click on Deploy
4. Go to the Domains tab
5. Create a new domain (Important: make sure to use the same domain you created in Cloudflare dashboard under `Published application routes`)
6. Set the correct port where your application is running (nginx runs on port `80` by default)
7. Don't enable HTTPS toggle or select any certificate provider (this can cause conflicts with Cloudflare SSL)

#### [For Direct Container Access](#for-direct-container-access)

If you prefer to bypass Traefik and connect directly to a container:

- Configure the public hostname with:
  
  - **Service**:
    
    - **Type**: HTTP
    - **URL**: `appName:port` (e.g., `dokploy:3000`, `my-app:8080`)

Note: The app name in Dokploy is shown under the service name, usually formatted as `project-serviceName-hash`

When using direct access, you bypass Traefik completely. Domain configurations in Dokploy won't apply, and you'll need to configure each container separately in Cloudflare.

### [For Wildcard Subdomains (Multiple Apps)](#for-wildcard-subdomains-multiple-apps)

To support multiple applications/subdomains with a single tunnel configuration:

**Note:** You need to create a manual CNAME wildcard record in your Cloudflare DNS configuration.

1. Go to the **Connectors** section and copy the **Tunnel ID** value
2. Go to **DNS Records** of your domain
3. Create a new record:
   
   - **Type**: CNAME
   - **Name**: `*`
   - **Content**: `your-tunnel-id.cfargotunnel.com` (replace `your-tunnel-id` with the ID you copied)
4. Click Save

Then, go to the configuration of your tunnel under **Published application routes**:

- Add a public hostname with:
  
  - **Subdomain**: `*` (asterisk for wildcard)
  - **Domain**: Your domain (e.g., `example.com`)
  - **Service**:
    
    - **Type**: HTTP
    - **URL**: `dokploy-traefik:80`

This allows all subdomains (`app1.example.com`, `app2.example.com`, etc.) to route through Traefik, which then directs traffic to the appropriate container based on your Dokploy domain configurations.

With wildcard routing, you only need ONE public hostname in Cloudflare Tunnel. Traefik handles routing to different apps based on the domain configured in Dokploy.