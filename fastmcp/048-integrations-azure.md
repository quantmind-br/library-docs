---
title: "Azure (Microsoft Entra ID) OAuth \U0001F91D FastMCP - FastMCP"
url: https://gofastmcp.com/integrations/azure
source: crawler
fetched_at: 2026-01-22T22:22:00.911602745-03:00
rendered_js: false
word_count: 309
summary: This guide explains how to secure a FastMCP server using Azure OAuth and Microsoft Entra ID through the AzureProvider. It covers app registration, scope configuration, client authentication, and production setup for persistent token storage.
tags:
    - fastmcp
    - azure-oauth
    - microsoft-entra-id
    - authentication
    - security
    - python
    - jwt-validation
    - oauth-proxy
category: guide
---

New in version `2.13.0` This guide shows you how to secure your FastMCP server using **Azure OAuth** (Microsoft Entra ID). Since Azure doesn’t support Dynamic Client Registration, this integration uses the [**OAuth Proxy**](https://gofastmcp.com/servers/auth/oauth-proxy) pattern to bridge Azure’s traditional OAuth with MCP’s authentication requirements. FastMCP validates Azure JWTs against your application’s client\_id.

## Configuration

### Prerequisites

Before you begin, you will need:

1. An [**Azure Account**](https://portal.azure.com/) with access to create App registrations
2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)
3. Your Azure tenant ID (found in Azure Portal under Microsoft Entra ID)

### Step 1: Create an Azure App Registration

Create an App registration in Azure Portal to get the credentials needed for authentication:

### Step 2: FastMCP Configuration

Create your FastMCP server using the `AzureProvider`, which handles Azure’s OAuth flow automatically:

```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.azure import AzureProvider

# The AzureProvider handles Azure's token format and validation
auth_provider = AzureProvider(
    client_id="835f09b6-0f0f-40cc-85cb-f32c5829a149",  # Your Azure App Client ID
    client_secret="your-client-secret",                 # Your Azure App Client Secret
    tenant_id="08541b6e-646d-43de-a0eb-834e6713d6d5", # Your Azure Tenant ID (REQUIRED)
    base_url="http://localhost:8000",                   # Must match your App registration
    required_scopes=["your-scope"],                 # At least one scope REQUIRED - name of scope from your App
    # identifier_uri defaults to api://{client_id}
    # identifier_uri="api://your-api-id",
    # Optional: request additional upstream scopes in the authorize request
    # additional_authorize_scopes=["User.Read", "offline_access", "openid", "email"],
    # redirect_path="/auth/callback"                  # Default value, customize if needed
    # base_authority="login.microsoftonline.us"      # For Azure Government (default: login.microsoftonline.com)
)

mcp = FastMCP(name="Azure Secured App", auth=auth_provider)

# Add a protected tool to test authentication
@mcp.tool
async def get_user_info() -> dict:
    """Returns information about the authenticated Azure user."""
    from fastmcp.server.dependencies import get_access_token

    token = get_access_token()
    # The AzureProvider stores user data in token claims
    return {
        "azure_id": token.claims.get("sub"),
        "email": token.claims.get("email"),
        "name": token.claims.get("name"),
        "job_title": token.claims.get("job_title"),
        "office_location": token.claims.get("office_location")
    }
```

### Scope Handling

FastMCP automatically prefixes `required_scopes` with your `identifier_uri` (e.g., `api://your-client-id`) since these are your custom API scopes. Scopes in `additional_authorize_scopes` are sent as-is since they target external resources like Microsoft Graph. **`required_scopes`** — Your custom API scopes, defined in Azure “Expose an API”:

You writeSent to AzureValidated on tokens`mcp-read``api://xxx/mcp-read`✓`my.scope``api://xxx/my.scope`✓`openid``openid`✗ (OIDC scope)`api://xxx/read``api://xxx/read`✓

**`additional_authorize_scopes`** — External scopes (e.g., Microsoft Graph) for server-side use:

You writeSent to AzureValidated on tokens`User.Read``User.Read`✗`Mail.Send``Mail.Send`✗

## Testing

### Running the Server

Start your FastMCP server with HTTP transport to enable OAuth flows:

```
fastmcp run server.py --transport http --port 8000
```

Your server is now running and protected by Azure OAuth authentication.

### Testing with a Client

Create a test client that authenticates with your Azure-protected server:

```
from fastmcp import Client
import asyncio

async def main():
    # The client will automatically handle Azure OAuth
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        # First-time connection will open Azure login in your browser
        print("✓ Authenticated with Azure!")

        # Test the protected tool
        result = await client.call_tool("get_user_info")
        print(f"Azure user: {result['email']}")
        print(f"Name: {result['name']}")

if __name__ == "__main__":
    asyncio.run(main())
```

When you run the client for the first time:

1. Your browser will open to Microsoft’s authorization page
2. Sign in with your Microsoft account (work, school, or personal based on your tenant configuration)
3. Grant the requested permissions
4. After authorization, you’ll be redirected back
5. The client receives the token and can make authenticated requests

## Production Configuration

New in version `2.13.0` For production deployments with persistent token management across server restarts, configure `jwt_signing_key` and `client_storage`:

```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.azure import AzureProvider
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet

# Production setup with encrypted persistent token storage
auth_provider = AzureProvider(
    client_id="835f09b6-0f0f-40cc-85cb-f32c5829a149",
    client_secret="your-client-secret",
    tenant_id="08541b6e-646d-43de-a0eb-834e6713d6d5",
    base_url="https://your-production-domain.com",
    required_scopes=["your-scope"],

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

mcp = FastMCP(name="Production Azure App", auth=auth_provider)
```