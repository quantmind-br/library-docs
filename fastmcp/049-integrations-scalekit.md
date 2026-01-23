---
title: "Scalekit \U0001F91D FastMCP - FastMCP"
url: https://gofastmcp.com/integrations/scalekit
source: crawler
fetched_at: 2026-01-22T22:22:01.229622748-03:00
rendered_js: false
word_count: 259
summary: This document explains how to integrate Scalekit authentication into a FastMCP server using the ScalekitProvider and the Remote OAuth pattern for JWT validation.
tags:
    - fastmcp
    - scalekit
    - authentication
    - oauth-2-1
    - jwt-validation
    - remote-oauth
    - python-sdk
    - security
category: tutorial
---

New in version `2.13.0` Install auth stack to your FastMCP server with [Scalekit](https://scalekit.com) using the [Remote OAuth](https://gofastmcp.com/servers/auth/remote-oauth) pattern: Scalekit handles user authentication, and the MCP server validates issued tokens.

### Prerequisites

Before you begin

1. Get a [Scalekit account](https://app.scalekit.com/) and grab your **Environment URL** from *Dashboard &gt; Settings* .
2. Have your FastMCP server’s base URL ready (can be localhost for development, e.g., `http://localhost:8000/`)

### Step 1: Configure MCP server in Scalekit environment

### Step 2: Add auth to FastMCP server

Create your FastMCP server file and use the ScalekitProvider to handle all the OAuth integration automatically:

> **Warning:** The legacy `mcp_url` and `client_id` parameters are deprecated and will be removed in a future release. Use `base_url` instead of `mcp_url` and remove `client_id` from your configuration.

```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.scalekit import ScalekitProvider

# Discovers Scalekit endpoints and set up JWT token validation
auth_provider = ScalekitProvider(
    environment_url=SCALEKIT_ENVIRONMENT_URL,    # Scalekit environment URL
    resource_id=SCALEKIT_RESOURCE_ID,            # Resource server ID
    base_url=SERVER_URL,                         # Public MCP endpoint
    required_scopes=["read"],                    # Optional scope enforcement
)

# Create FastMCP server with auth
mcp = FastMCP(name="My Scalekit Protected Server", auth=auth_provider)

@mcp.tool
def auth_status() -> dict:
    """Show Scalekit authentication status."""
    # Extract user claims from the JWT
    return {
        "message": "This tool requires authentication via Scalekit",
        "authenticated": True,
        "provider": "Scalekit"
    }

```

## Testing

### Start the MCP server

Use any MCP client (for example, mcp-inspector, Claude, VS Code, or Windsurf) to connect to the running serve. Verify that authentication succeeds and requests are authorized as expected.

## Production Configuration

For production deployments, load configuration from environment variables:

```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.scalekit import ScalekitProvider

# Load configuration from environment variables
auth = ScalekitProvider(
    environment_url=os.environ.get("SCALEKIT_ENVIRONMENT_URL"),
    resource_id=os.environ.get("SCALEKIT_RESOURCE_ID"),
    base_url=os.environ.get("BASE_URL", "https://your-server.com")
)

mcp = FastMCP(name="My Scalekit Protected Server", auth=auth)

@mcp.tool
def protected_action() -> str:
    """A tool that requires authentication."""
    return "Access granted via Scalekit!"
```

## Capabilities

Scalekit supports OAuth 2.1 with Dynamic Client Registration for MCP clients and enterprise SSO, and provides built‑in JWT validation and security controls. **OAuth 2.1/DCR**: clients self‑register, use PKCE, and work with the Remote OAuth pattern without pre‑provisioned credentials. **Validation and SSO**: tokens are verified (keys, RS256, issuer, audience, expiry), and SAML, OIDC, OAuth 2.0, ADFS, Azure AD, and Google Workspace are supported; use HTTPS in production and review auth logs as needed.

## Debugging

Enable detailed logging to troubleshoot authentication issues:

```
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Token inspection

You can inspect JWT tokens in your tools to understand the user context:

```
from fastmcp.server.context import request_ctx
import jwt

@mcp.tool
def inspect_token() -> dict:
    """Inspect the current JWT token claims."""
    context = request_ctx.get()

    # Extract token from Authorization header
    if hasattr(context, 'request') and hasattr(context.request, 'headers'):
        auth_header = context.request.headers.get('authorization', '')
        if auth_header.startswith('Bearer '):
            token = auth_header[7:]
            # Decode without verification (already verified by provider)
            claims = jwt.decode(token, options={"verify_signature": False})
            return claims

    return {"error": "No token found"}
```