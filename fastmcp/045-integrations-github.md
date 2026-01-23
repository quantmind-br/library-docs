---
title: "GitHub OAuth \U0001F91D FastMCP - FastMCP"
url: https://gofastmcp.com/integrations/github
source: crawler
fetched_at: 2026-01-22T22:22:01.970487863-03:00
rendered_js: false
word_count: 203
summary: This guide explains how to secure a FastMCP server using GitHub OAuth authentication via the GitHubProvider and OAuth Proxy pattern. It covers configuration steps for development and production environments, including token management and client integration.
tags:
    - fastmcp
    - github-oauth
    - authentication
    - security
    - oauth-proxy
    - token-management
    - python
category: guide
---

New in version `2.12.0` This guide shows you how to secure your FastMCP server using **GitHub OAuth**. Since GitHub doesn’t support Dynamic Client Registration, this integration uses the [**OAuth Proxy**](https://gofastmcp.com/servers/auth/oauth-proxy) pattern to bridge GitHub’s traditional OAuth with MCP’s authentication requirements.

## Configuration

### Prerequisites

Before you begin, you will need:

1. A [**GitHub Account**](https://github.com/) with access to create OAuth Apps
2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)

### Step 1: Create a GitHub OAuth App

Create an OAuth App in your GitHub settings to get the credentials needed for authentication:

### Step 2: FastMCP Configuration

Create your FastMCP server using the `GitHubProvider`, which handles GitHub’s OAuth quirks automatically:

```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.github import GitHubProvider

# The GitHubProvider handles GitHub's token format and validation
auth_provider = GitHubProvider(
    client_id="Ov23liAbcDefGhiJkLmN",  # Your GitHub OAuth App Client ID
    client_secret="github_pat_...",     # Your GitHub OAuth App Client Secret
    base_url="http://localhost:8000",   # Must match your OAuth App configuration
    # redirect_path="/auth/callback"   # Default value, customize if needed
)

mcp = FastMCP(name="GitHub Secured App", auth=auth_provider)

# Add a protected tool to test authentication
@mcp.tool
async def get_user_info() -> dict:
    """Returns information about the authenticated GitHub user."""
    from fastmcp.server.dependencies import get_access_token

    token = get_access_token()
    # The GitHubProvider stores user data in token claims
    return {
        "github_user": token.claims.get("login"),
        "name": token.claims.get("name"),
        "email": token.claims.get("email")
    }
```

## Testing

### Running the Server

Start your FastMCP server with HTTP transport to enable OAuth flows:

```
fastmcp run server.py --transport http --port 8000
```

Your server is now running and protected by GitHub OAuth authentication.

### Testing with a Client

Create a test client that authenticates with your GitHub-protected server:

```
from fastmcp import Client
import asyncio

async def main():
    # The client will automatically handle GitHub OAuth
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        # First-time connection will open GitHub login in your browser
        print("✓ Authenticated with GitHub!")

        # Test the protected tool
        result = await client.call_tool("get_user_info")
        print(f"GitHub user: {result['github_user']}")

if __name__ == "__main__":
    asyncio.run(main())
```

When you run the client for the first time:

1. Your browser will open to GitHub’s authorization page
2. After you authorize the app, you’ll be redirected back
3. The client receives the token and can make authenticated requests

## Production Configuration

New in version `2.13.0` For production deployments with persistent token management across server restarts, configure `jwt_signing_key` and `client_storage`:

```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.github import GitHubProvider
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet

# Production setup with encrypted persistent token storage
auth_provider = GitHubProvider(
    client_id="Ov23liAbcDefGhiJkLmN",
    client_secret="github_pat_...",
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

mcp = FastMCP(name="Production GitHub App", auth=auth_provider)
```