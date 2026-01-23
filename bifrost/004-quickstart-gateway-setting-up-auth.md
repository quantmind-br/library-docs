---
title: Setting up auth
url: https://docs.getbifrost.ai/quickstart/gateway/setting-up-auth.md
source: llms
fetched_at: 2026-01-21T19:44:54.204445132-03:00
rendered_js: false
word_count: 543
summary: This document provides instructions for enabling and managing basic authentication to secure the Bifrost dashboard and administrative API endpoints.
tags:
    - bifrost-security
    - authentication-setup
    - dashboard-access
    - api-security
    - basic-auth
    - security-configuration
category: configuration
---

# Setting up auth

> Learn how to enable basic authentication for the Bifrost dashboard to secure your admin interface and API endpoints.

## Overview

Bifrost provides built-in authentication to protect your dashboard and admin API endpoints. When enabled, users must log in with credentials before accessing the dashboard or making admin API calls. This feature helps secure your Bifrost instance, especially when deployed in production environments.

## Enabling Authentication

### Step 1: Navigate to Security Settings

1. Open your Bifrost dashboard
2. Go to **Workspace** → **Config** → **Security** tab
3. Scroll to the **Password protect the dashboard** section

<img src="https://mintcdn.com/bifrost/GKKX5IubjuB02wGm/media/setting-up-dashboard-auth.png?fit=max&auto=format&n=GKKX5IubjuB02wGm&q=85&s=9ddd5368ff59d1371af3c3585661f6b9" alt="Setting up auth" data-og-width="3444" width="3444" data-og-height="2052" height="2052" data-path="media/setting-up-dashboard-auth.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/GKKX5IubjuB02wGm/media/setting-up-dashboard-auth.png?w=280&fit=max&auto=format&n=GKKX5IubjuB02wGm&q=85&s=0c484709cefa3771e65ebe30948d206a 280w, https://mintcdn.com/bifrost/GKKX5IubjuB02wGm/media/setting-up-dashboard-auth.png?w=560&fit=max&auto=format&n=GKKX5IubjuB02wGm&q=85&s=7fea841fa1931077361ebe2883c9c9bb 560w, https://mintcdn.com/bifrost/GKKX5IubjuB02wGm/media/setting-up-dashboard-auth.png?w=840&fit=max&auto=format&n=GKKX5IubjuB02wGm&q=85&s=986db7775f3b1a2e060d9d32502eac7d 840w, https://mintcdn.com/bifrost/GKKX5IubjuB02wGm/media/setting-up-dashboard-auth.png?w=1100&fit=max&auto=format&n=GKKX5IubjuB02wGm&q=85&s=708cc51b1b738c109e4a95bbf0db4cc5 1100w, https://mintcdn.com/bifrost/GKKX5IubjuB02wGm/media/setting-up-dashboard-auth.png?w=1650&fit=max&auto=format&n=GKKX5IubjuB02wGm&q=85&s=d2265cb97f8004093cdf304fe9253073 1650w, https://mintcdn.com/bifrost/GKKX5IubjuB02wGm/media/setting-up-dashboard-auth.png?w=2500&fit=max&auto=format&n=GKKX5IubjuB02wGm&q=85&s=4ec8393fa753836d531dc0e107eab957 2500w" />

### Step 2: Enable Authentication

1. Toggle the **Password protect the dashboard** switch to enable authentication
2. Enter your **Username** in the admin username field
3. Enter your **Password** in the admin password field

<Note>
  The username and password fields are only enabled when the authentication toggle is turned on. Make sure to use a strong password for security.
</Note>

### Step 3: Configure Inference Call Authentication (Optional)

By default, when authentication is enabled, all API calls (including inference calls) require authentication. You can optionally disable authentication for inference calls while keeping it enabled for the dashboard and admin API:

1. Enable the **Disable authentication on inference calls** toggle
2. When enabled:
   * Dashboard and admin API calls will still require authentication
   * Inference API calls (chat completions, embeddings, etc.) will not require authentication
   * MCP tool execution calls will still require authentication

<Note>
  This option is useful if you want to protect your dashboard and admin functions while allowing public access to inference endpoints.
</Note>

### Step 4: Save Changes

1. Click **Save Changes** to apply your authentication settings
2. Changes take effect immediately - no restart required

## Logging In

Once authentication is enabled:

1. Navigate to your Bifrost dashboard URL
2. You will be automatically redirected to the login page
3. Enter your configured username and password
4. Click **Sign in**

After successful login, you'll be redirected to the dashboard. Your session will remain active for 30 days, and you'll need to log in again after the session expires.

## Authentication Methods

Bifrost supports different authentication methods depending on the type of request:

### Dashboard Access

* **Bearer Token Authentication**: The dashboard uses Bearer token authentication
* Tokens are automatically managed through the login session
* Tokens are stored in browser localStorage and sent with each API request

### API Calls

When authentication is enabled, API calls can use:

* **Basic Authentication**: For inference calls, you can use HTTP Basic Auth with your username and password
* **Bearer Token**: For admin API calls, use the Bearer token obtained from the login session

### Example: Using Basic Auth for API Calls

```bash  theme={null}
# Using curl with Basic Auth
curl -X POST http://localhost:8080/v1/chat/completions \
  -u "your-username:your-password" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-4o",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## Important Notes

* **No Restart Required**: Authentication changes take effect immediately without requiring a server restart
* **Session Duration**: Login sessions last for 30 days
* **Password Security**: Passwords are hashed and stored securely in the database
* **Inference Calls**: If you disable authentication on inference calls, only dashboard and admin API endpoints will be protected

## Disabling Authentication

To disable authentication:

1. Navigate to **Workspace** → **Config** → **Security**
2. Toggle off the **Password protect the dashboard** switch
3. Click **Save Changes**

After disabling, the dashboard will be accessible without authentication immediately.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt