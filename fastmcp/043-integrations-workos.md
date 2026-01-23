---
title: "WorkOS \U0001F91D FastMCP - FastMCP"
url: https://gofastmcp.com/integrations/workos
source: crawler
fetched_at: 2026-01-22T22:21:59.064339887-03:00
rendered_js: false
word_count: 190
summary: This document explains how to secure a FastMCP server using WorkOS Connect authentication via the OAuth Proxy pattern. It provides step-by-step instructions for development setup, client testing, and production-grade configuration with persistent token storage.
tags:
    - fastmcp
    - workos-connect
    - oauth-authentication
    - security-configuration
    - mcp-server
    - token-management
category: guide
---

New in version `2.12.0` Secure your FastMCP server with WorkOS Connect authentication. This integration uses the OAuth Proxy pattern to handle authentication through WorkOS Connect while maintaining compatibility with MCP clients.

## Configuration

### Prerequisites

Before you begin, you will need:

1. A [**WorkOS Account**](https://workos.com/) with access to create OAuth Apps
2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)

### Step 1: Create a WorkOS OAuth App

Create an OAuth App in your WorkOS dashboard to get the credentials needed for authentication:

### Step 2: FastMCP Configuration

Create your FastMCP server using the `WorkOSProvider`:

```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.workos import WorkOSProvider

# Configure WorkOS OAuth
auth = WorkOSProvider(
    client_id="client_YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    authkit_domain="https://your-app.authkit.app",
    base_url="http://localhost:8000",
    required_scopes=["openid", "profile", "email"]
)

mcp = FastMCP("WorkOS Protected Server", auth=auth)

@mcp.tool
def protected_tool(message: str) -> str:
    """This tool requires authentication."""
    return f"Authenticated user says: {message}"

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
```

## Testing

### Running the Server

Start your FastMCP server with HTTP transport to enable OAuth flows:

```
fastmcp run server.py --transport http --port 8000
```

Your server is now running and protected by WorkOS OAuth authentication.

### Testing with a Client

Create a test client that authenticates with your WorkOS-protected server:

```
from fastmcp import Client
import asyncio

async def main():
    # The client will automatically handle WorkOS OAuth
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        # First-time connection will open WorkOS login in your browser
        print("✓ Authenticated with WorkOS!")

        # Test the protected tool
        result = await client.call_tool("protected_tool", {"message": "Hello!"})
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

When you run the client for the first time:

1. Your browser will open to WorkOS’s authorization page
2. After you authorize the app, you’ll be redirected back
3. The client receives the token and can make authenticated requests

## Production Configuration

New in version `2.13.0` For production deployments with persistent token management across server restarts, configure `jwt_signing_key`, and `client_storage`:

```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.workos import WorkOSProvider
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet

# Production setup with encrypted persistent token storage
auth = WorkOSProvider(
    client_id="client_YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    authkit_domain="https://your-app.authkit.app",
    base_url="https://your-production-domain.com",
    required_scopes=["openid", "profile", "email"],

    # Production token management
    jwt_signing_key=os.environ["JWT_SIGNING_KEY"],
    client_storage=FernetEncryptionWrapper(
        key_value=RedisStore(
            host=os.environ["REDIS_HOST"],
            port=int(os.environ["REDIS_PORT"])
        ),
        fernet=Fernet(os.environ["STORAGE_ENCRYPTION_KEY"])
    )
)

mcp = FastMCP(name="Production WorkOS App", auth=auth)
```

## Configuration Options