---
title: "Google OAuth \U0001F91D FastMCP - FastMCP"
url: https://gofastmcp.com/integrations/google
source: crawler
fetched_at: 2026-01-22T22:21:59.410794787-03:00
rendered_js: false
word_count: 219
summary: This document provides a comprehensive guide on implementing Google OAuth authentication for FastMCP servers using the GoogleProvider and OAuth Proxy pattern. It covers environment setup, server configuration, and production-ready persistent token storage.
tags:
    - fastmcp
    - google-oauth
    - authentication
    - security
    - python
    - mcp-server
    - oauth-proxy
    - token-storage
category: guide
---

New in version `2.12.0` This guide shows you how to secure your FastMCP server using **Google OAuth**. Since Google doesn’t support Dynamic Client Registration, this integration uses the [**OAuth Proxy**](https://gofastmcp.com/servers/auth/oauth-proxy) pattern to bridge Google’s traditional OAuth with MCP’s authentication requirements.

## Configuration

### Prerequisites

Before you begin, you will need:

1. A [**Google Cloud Account**](https://console.cloud.google.com/) with access to create OAuth 2.0 Client IDs
2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)

### Step 1: Create a Google OAuth 2.0 Client ID

Create an OAuth 2.0 Client ID in your Google Cloud Console to get the credentials needed for authentication:

### Step 2: FastMCP Configuration

Create your FastMCP server using the `GoogleProvider`, which handles Google’s OAuth flow automatically:

```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.google import GoogleProvider

# The GoogleProvider handles Google's token format and validation
auth_provider = GoogleProvider(
    client_id="123456789.apps.googleusercontent.com",  # Your Google OAuth Client ID
    client_secret="GOCSPX-abc123...",                  # Your Google OAuth Client Secret
    base_url="http://localhost:8000",                  # Must match your OAuth configuration
    required_scopes=[                                  # Request user information
        "openid",
        "https://www.googleapis.com/auth/userinfo.email",
    ],
    # redirect_path="/auth/callback"                  # Default value, customize if needed
)

mcp = FastMCP(name="Google Secured App", auth=auth_provider)

# Add a protected tool to test authentication
@mcp.tool
async def get_user_info() -> dict:
    """Returns information about the authenticated Google user."""
    from fastmcp.server.dependencies import get_access_token

    token = get_access_token()
    # The GoogleProvider stores user data in token claims
    return {
        "google_id": token.claims.get("sub"),
        "email": token.claims.get("email"),
        "name": token.claims.get("name"),
        "picture": token.claims.get("picture"),
        "locale": token.claims.get("locale")
    }
```

## Testing

### Running the Server

Start your FastMCP server with HTTP transport to enable OAuth flows:

```
fastmcp run server.py --transport http --port 8000
```

Your server is now running and protected by Google OAuth authentication.

### Testing with a Client

Create a test client that authenticates with your Google-protected server:

```
from fastmcp import Client
import asyncio

async def main():
    # The client will automatically handle Google OAuth
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        # First-time connection will open Google login in your browser
        print("✓ Authenticated with Google!")

        # Test the protected tool
        result = await client.call_tool("get_user_info")
        print(f"Google user: {result['email']}")
        print(f"Name: {result['name']}")

if __name__ == "__main__":
    asyncio.run(main())
```

When you run the client for the first time:

1. Your browser will open to Google’s authorization page
2. Sign in with your Google account and grant the requested permissions
3. After authorization, you’ll be redirected back
4. The client receives the token and can make authenticated requests

## Production Configuration

New in version `2.13.0` For production deployments with persistent token management across server restarts, configure `jwt_signing_key` and `client_storage`:

```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.google import GoogleProvider
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet

# Production setup with encrypted persistent token storage
auth_provider = GoogleProvider(
    client_id="123456789.apps.googleusercontent.com",
    client_secret="GOCSPX-abc123...",
    base_url="https://your-production-domain.com",
    required_scopes=["openid", "https://www.googleapis.com/auth/userinfo.email"],

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

mcp = FastMCP(name="Production Google App", auth=auth_provider)
```