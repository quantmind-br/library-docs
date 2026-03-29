---
title: Upgrade Guide - FastMCP
url: https://gofastmcp.com/v2/development/upgrade-guide
source: crawler
fetched_at: 2026-01-22T22:23:00.342086847-03:00
rendered_js: false
word_count: 336
summary: This document provides migration instructions and explains breaking changes for upgrading between FastMCP versions 2.13.0 and 2.14.0.
tags:
    - fastmcp
    - migration-guide
    - breaking-changes
    - openapi-parser
    - oauth-security
    - versioning
category: guide
---

This guide provides migration instructions for breaking changes and major updates when upgrading between FastMCP versions.

## v2.14.0

### OpenAPI Parser Promotion

The experimental OpenAPI parser is now the standard implementation. The legacy parser has been removed. **If you were using the legacy parser:** No code changes required. The new parser is a drop-in replacement with improved architecture. **If you were using the experimental parser:** Update your imports from the experimental module to the standard location:

The experimental imports will continue working temporarily but will show deprecation warnings. The `FASTMCP_EXPERIMENTAL_ENABLE_NEW_OPENAPI_PARSER` environment variable is no longer needed and can be removed.

### Deprecated Features Removed

The following deprecated features have been removed in v2.14.0: **BearerAuthProvider** (deprecated in v2.11):

**Context.get\_http\_request()** (deprecated in v2.2.11):

**Top-level Image import** (deprecated in v2.8.1):

**FastMCP dependencies parameter** (deprecated in v2.11.4):

**Legacy resource prefix format**: The `resource_prefix_format` parameter and “protocol” format have been removed. Only the “path” format is supported (this was already the default). **FastMCPProxy client parameter**:

**output\_schema=False**:

## v2.13.0

### OAuth Token Key Management

The OAuth proxy now issues its own JWT tokens to clients instead of forwarding upstream provider tokens. This improves security by maintaining proper token audience boundaries. **What changed:** The OAuth proxy now implements a token factory pattern - it receives tokens from your OAuth provider (GitHub, Google, etc.), encrypts and stores them, then issues its own FastMCP JWT tokens to clients. This requires cryptographic keys for JWT signing and token encryption. **Default behavior (development):** By default, FastMCP automatically manages keys based on your platform:

- **Mac/Windows**: Keys are auto-managed via system keyring, surviving server restarts with zero configuration. Suitable **only** for development and local testing.
- **Linux**: Keys are ephemeral (random salt at startup, regenerated on each restart).

This works fine for development and testing where re-authentication after restart is acceptable. **For production:** Production deployments must provide explicit keys and use persistent storage. Add these three things:

```
auth = GitHubProvider(
    client_id=os.environ["GITHUB_CLIENT_ID"],
    client_secret=os.environ["GITHUB_CLIENT_SECRET"],
    base_url="https://your-server.com",

    # Explicit keys (required for production)
    jwt_signing_key=os.environ["JWT_SIGNING_KEY"],

    # Persistent network storage (required for production)
    client_storage=RedisStore(host="redis.example.com", port=6379)
)
```

**More information:**

- [OAuth Token Security](https://gofastmcp.com/v2/deployment/http#oauth-token-security) - Complete production setup guide
- [Key and Storage Management](https://gofastmcp.com/v2/servers/auth/oauth-proxy#key-and-storage-management) - Detailed explanation of defaults and production requirements
- [OAuth Proxy Parameters](https://gofastmcp.com/v2/servers/auth/oauth-proxy#configuration-parameters) - Parameter documentation