---
title: "Descope \U0001F91D FastMCP - FastMCP"
url: https://gofastmcp.com/integrations/descope
source: crawler
fetched_at: 2026-01-22T22:22:00.82710014-03:00
rendered_js: false
word_count: 171
summary: This guide explains how to secure a FastMCP server by integrating Descope authentication using the Remote OAuth pattern. It covers environment configuration, implementing the DescopeProvider for token validation, and testing protected server access.
tags:
    - fastmcp
    - descope
    - authentication
    - remote-oauth
    - security
    - jwt-validation
    - python
category: guide
---

New in version `2.12.4` This guide shows you how to secure your FastMCP server using [**Descope**](https://www.descope.com), a complete authentication and user management solution. This integration uses the [**Remote OAuth**](https://gofastmcp.com/servers/auth/remote-oauth) pattern, where Descope handles user login and your FastMCP server validates the tokens.

## Configuration

### Prerequisites

Before you begin, you will need:

1. To [sign up](https://www.descope.com/sign-up) for a Free Forever Descope account
2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:3000`)

### Step 1: Configure Descope

### Step 2: Environment Setup

Create a `.env` file with your Descope configuration:

```
DESCOPE_CONFIG_URL=https://.../v1/apps/agentic/P.../M.../.well-known/openid-configuration     # Your Descope Well-Known URL
SERVER_URL=http://localhost:3000     # Your server's base URL
```

### Step 3: FastMCP Configuration

Create your FastMCP server file and use the DescopeProvider to handle all the OAuth integration automatically:

```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.descope import DescopeProvider

# The DescopeProvider automatically discovers Descope endpoints
# and configures JWT token validation
auth_provider = DescopeProvider(
    config_url=https://.../.well-known/openid-configuration,        # Your MCP Server .well-known URL
    base_url=SERVER_URL,                  # Your server's public URL
)

# Create FastMCP server with auth
mcp = FastMCP(name="My Descope Protected Server", auth=auth_provider)

```

## Testing

To test your server, you can use the `fastmcp` CLI to run it locally. Assuming you’ve saved the above code to `server.py` (after replacing the environment variables with your actual values!), you can run the following command:

```
fastmcp run server.py --transport http --port 8000
```

Now, you can use a FastMCP client to test that you can reach your server after authenticating:

```
from fastmcp import Client
import asyncio

async def main():
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        assert await client.ping()

if __name__ == "__main__":
    asyncio.run(main())
```

## Production Configuration

For production deployments, load configuration from environment variables:

```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.descope import DescopeProvider

# Load configuration from environment variables
auth = DescopeProvider(
    config_url=os.environ.get("DESCOPE_CONFIG_URL"),
    base_url=os.environ.get("BASE_URL", "https://your-server.com")
)

mcp = FastMCP(name="My Descope Protected Server", auth=auth)
```