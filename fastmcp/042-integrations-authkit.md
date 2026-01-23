---
title: "AuthKit \U0001F91D FastMCP - FastMCP"
url: https://gofastmcp.com/integrations/authkit
source: crawler
fetched_at: 2026-01-22T22:21:58.800166062-03:00
rendered_js: false
word_count: 179
summary: This guide explains how to secure a FastMCP server using WorkOS AuthKit for user authentication and Remote OAuth token validation.
tags:
    - fastmcp
    - workos
    - authkit
    - authentication
    - remote-oauth
    - security
category: guide
---

New in version `2.11.0` This guide shows you how to secure your FastMCP server using WorkOS’s **AuthKit**, a complete authentication and user management solution. This integration uses the [**Remote OAuth**](https://gofastmcp.com/servers/auth/remote-oauth) pattern, where AuthKit handles user login and your FastMCP server validates the tokens.

## Configuration

### Prerequisites

Before you begin, you will need:

1. A [**WorkOS Account**](https://workos.com/) and a new **Project**.
2. An [**AuthKit**](https://www.authkit.com/) instance configured within your WorkOS project.
3. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`).

### Step 1: AuthKit Configuration

In your WorkOS Dashboard, enable AuthKit and configure the following settings:

### Step 2: FastMCP Configuration

Create your FastMCP server file and use the `AuthKitProvider` to handle all the OAuth integration automatically:

```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.workos import AuthKitProvider

# The AuthKitProvider automatically discovers WorkOS endpoints
# and configures JWT token validation
auth_provider = AuthKitProvider(
    authkit_domain="https://your-project-12345.authkit.app",
    base_url="http://localhost:8000"  # Use your actual server URL
)

mcp = FastMCP(name="AuthKit Secured App", auth=auth_provider)
```

## Testing

To test your server, you can use the `fastmcp` CLI to run it locally. Assuming you’ve saved the above code to `server.py` (after replacing the `authkit_domain` and `base_url` with your actual values!), you can run the following command:

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

For production deployments, load sensitive configuration from environment variables:

```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.workos import AuthKitProvider

# Load configuration from environment variables
auth = AuthKitProvider(
    authkit_domain=os.environ.get("AUTHKIT_DOMAIN"),
    base_url=os.environ.get("BASE_URL", "https://your-server.com")
)

mcp = FastMCP(name="AuthKit Secured App", auth=auth)
```