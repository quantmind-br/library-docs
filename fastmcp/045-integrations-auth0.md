---
title: "Auth0 OAuth \U0001F91D FastMCP - FastMCP"
url: https://gofastmcp.com/integrations/auth0
source: crawler
fetched_at: 2026-01-22T22:21:59.585153506-03:00
rendered_js: false
word_count: 203
summary: This document explains how to secure a FastMCP server using Auth0 OAuth authentication, covering initial configuration, client testing, and production-ready persistent storage setup.
tags:
    - fastmcp
    - auth0
    - oauth
    - authentication
    - security
    - oidc
    - python
category: guide
---

New in version `2.12.4` This guide shows you how to secure your FastMCP server using **Auth0 OAuth**. While Auth0 does have support for Dynamic Client Registration, it is not enabled by default so this integration uses the [**OIDC Proxy**](https://gofastmcp.com/servers/auth/oidc-proxy) pattern to bridge Auth0’s dynamic OIDC configuration with MCP’s authentication requirements.

## Configuration

### Prerequisites

Before you begin, you will need:

1. An [**Auth0 Account**](https://auth0.com/) with access to create Applications
2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)

### Step 1: Create an Auth0 Application

Create an Application in your Auth0 settings to get the credentials needed for authentication:

### Step 2: FastMCP Configuration

Create your FastMCP server using the `Auth0Provider`.

```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.auth0 import Auth0Provider

# The Auth0Provider utilizes Auth0 OIDC configuration
auth_provider = Auth0Provider(
    config_url="https://.../.well-known/openid-configuration",  # Your Auth0 configuration URL
    client_id="tv2ObNgaZAWWhhycr7Bz1LU2mxlnsmsB",               # Your Auth0 application Client ID
    client_secret="vPYqbjemq...",                               # Your Auth0 application Client Secret
    audience="https://...",                                     # Your Auth0 API audience
    base_url="http://localhost:8000",                           # Must match your application configuration
    # redirect_path="/auth/callback"                            # Default value, customize if needed
)

mcp = FastMCP(name="Auth0 Secured App", auth=auth_provider)

# Add a protected tool to test authentication
@mcp.tool
async def get_token_info() -> dict:
    """Returns information about the Auth0 token."""
    from fastmcp.server.dependencies import get_access_token

    token = get_access_token()

    return {
        "issuer": token.claims.get("iss"),
        "audience": token.claims.get("aud"),
        "scope": token.claims.get("scope")
    }
```

## Testing

### Running the Server

Start your FastMCP server with HTTP transport to enable OAuth flows:

```
fastmcp run server.py --transport http --port 8000
```

Your server is now running and protected by Auth0 authentication.

### Testing with a Client

Create a test client that authenticates with your Auth0-protected server:

```
from fastmcp import Client
import asyncio

async def main():
    # The client will automatically handle Auth0 OAuth flows
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        # First-time connection will open Auth0 login in your browser
        print("✓ Authenticated with Auth0!")

        # Test the protected tool
        result = await client.call_tool("get_token_info")
        print(f"Auth0 audience: {result['audience']}")

if __name__ == "__main__":
    asyncio.run(main())
```

When you run the client for the first time:

1. Your browser will open to Auth0’s authorization page
2. After you authorize the app, you’ll be redirected back
3. The client receives the token and can make authenticated requests

## Production Configuration

New in version `2.13.0` For production deployments with persistent token management across server restarts, configure `jwt_signing_key`, and `client_storage`:

```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.auth0 import Auth0Provider
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet

# Production setup with encrypted persistent token storage
auth_provider = Auth0Provider(
    config_url="https://.../.well-known/openid-configuration",
    client_id="tv2ObNgaZAWWhhycr7Bz1LU2mxlnsmsB",
    client_secret="vPYqbjemq...",
    audience="https://...",
    base_url="https://your-production-domain.com",

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

mcp = FastMCP(name="Production Auth0 App", auth=auth_provider)
```