---
title: "AWS Cognito OAuth \U0001F91D FastMCP - FastMCP"
url: https://gofastmcp.com/integrations/aws-cognito
source: crawler
fetched_at: 2026-01-22T22:22:01.602849487-03:00
rendered_js: false
word_count: 365
summary: This guide explains how to secure FastMCP servers using AWS Cognito and the OAuth Proxy pattern for enterprise-grade authentication.
tags:
    - fastmcp
    - aws-cognito
    - oauth
    - authentication
    - security
    - jwt-validation
    - python
category: guide
---

New in version `2.12.4` This guide shows you how to secure your FastMCP server using **AWS Cognito user pools**. Since AWS Cognito doesn’t support Dynamic Client Registration, this integration uses the [**OAuth Proxy**](https://gofastmcp.com/servers/auth/oauth-proxy) pattern to bridge AWS Cognito’s traditional OAuth with MCP’s authentication requirements. It also includes robust JWT token validation, ensuring enterprise-grade authentication.

## Configuration

### Prerequisites

Before you begin, you will need:

1. An [**AWS Account**](https://aws.amazon.com/) with access to create AWS Cognito user pools
2. Basic familiarity with AWS Cognito concepts (user pools, app clients)
3. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)

### Step 1: Create an AWS Cognito User Pool and App Client

Set up AWS Cognito user pool with an app client to get the credentials needed for authentication:

### Step 2: FastMCP Configuration

Create your FastMCP server using the `AWSCognitoProvider`, which handles AWS Cognito’s JWT tokens and user claims automatically:

```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.aws import AWSCognitoProvider
from fastmcp.server.dependencies import get_access_token

# The AWSCognitoProvider handles JWT validation and user claims
auth_provider = AWSCognitoProvider(
    user_pool_id="eu-central-1_XXXXXXXXX",   # Your AWS Cognito user pool ID
    aws_region="eu-central-1",               # AWS region (defaults to eu-central-1)
    client_id="your-app-client-id",          # Your app client ID
    client_secret="your-app-client-secret",  # Your app client Secret
    base_url="http://localhost:8000",        # Must match your callback URL
    # redirect_path="/auth/callback"         # Default value, customize if needed
)

mcp = FastMCP(name="AWS Cognito Secured App", auth=auth_provider)

# Add a protected tool to test authentication
@mcp.tool
async def get_access_token_claims() -> dict:
    """Get the authenticated user's access token claims."""
    token = get_access_token()
    return {
        "sub": token.claims.get("sub"),
        "username": token.claims.get("username"),
        "cognito:groups": token.claims.get("cognito:groups", []),
    }
```

## Testing

### Running the Server

Start your FastMCP server with HTTP transport to enable OAuth flows:

```
fastmcp run server.py --transport http --port 8000
```

Your server is now running and protected by AWS Cognito OAuth authentication.

### Testing with a Client

Create a test client that authenticates with Your AWS Cognito-protected server:

```
from fastmcp import Client
import asyncio

async def main():
    # The client will automatically handle AWS Cognito OAuth
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        # First-time connection will open AWS Cognito login in your browser
        print("✓ Authenticated with AWS Cognito!")

        # Test the protected tool
        print("Calling protected tool: get_access_token_claims")
        result = await client.call_tool("get_access_token_claims")
        user_data = result.data
        print("Available access token claims:")
        print(f"- sub: {user_data.get('sub', 'N/A')}")
        print(f"- username: {user_data.get('username', 'N/A')}")
        print(f"- cognito:groups: {user_data.get('cognito:groups', [])}")

if __name__ == "__main__":
    asyncio.run(main())
```

When you run the client for the first time:

1. Your browser will open to AWS Cognito’s hosted UI login page
2. After you sign in (or sign up), you’ll be redirected back to your MCP server
3. The client receives the JWT token and can make authenticated requests

## Production Configuration

New in version `2.13.0` For production deployments with persistent token management across server restarts, configure `jwt_signing_key`, and `client_storage`:

```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.aws import AWSCognitoProvider
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet

# Production setup with encrypted persistent token storage
auth_provider = AWSCognitoProvider(
    user_pool_id="eu-central-1_XXXXXXXXX",
    aws_region="eu-central-1",
    client_id="your-app-client-id",
    client_secret="your-app-client-secret",
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

mcp = FastMCP(name="Production AWS Cognito App", auth=auth_provider)
```

## Features

### JWT Token Validation

The AWS Cognito provider includes robust JWT token validation:

- **Signature Verification**: Validates tokens against AWS Cognito’s public keys (JWKS)
- **Expiration Checking**: Automatically rejects expired tokens
- **Issuer Validation**: Ensures tokens come from your specific AWS Cognito user pool
- **Scope Enforcement**: Verifies required OAuth scopes are present

### User Claims and Groups

Access rich user information from AWS Cognito JWT tokens:

```
from fastmcp.server.dependencies import get_access_token

@mcp.tool
async def admin_only_tool() -> str:
    """A tool only available to admin users."""
    token = get_access_token()
    user_groups = token.claims.get("cognito:groups", [])

    if "admin" not in user_groups:
        raise ValueError("This tool requires admin access")

    return "Admin access granted!"
```

### Enterprise Integration

Perfect for enterprise environments with:

- **Single Sign-On (SSO)**: Integrate with corporate identity providers
- **Multi-Factor Authentication (MFA)**: Leverage AWS Cognito’s built-in MFA
- **User Groups**: Role-based access control through AWS Cognito groups
- **Custom Attributes**: Access custom user attributes defined in your AWS Cognito user pool
- **Compliance**: Meet enterprise security and compliance requirements