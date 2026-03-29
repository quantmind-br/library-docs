---
title: FastMCP Updates - FastMCP
url: https://gofastmcp.com/updates
source: crawler
fetched_at: 2026-01-22T22:21:41.483858162-03:00
rendered_js: false
word_count: 268
summary: This release note details version 2.13 of FastMCP, focusing on production-ready features such as persistent storage backends, enhanced OAuth security, and response caching middleware.
tags:
    - fastmcp
    - release-notes
    - oauth-authentication
    - persistent-storage
    - caching-middleware
    - server-lifespan
category: reference
---

[FastMCP 2.13 “Cache Me If You Can” represents a fundamental maturation of the framework. After months of community feedback on authentication and state management, this release delivers the infrastructure FastMCP needs to handle production workloads: persistent storage, response caching, and pragmatic OAuth improvements that reflect real-world deployment challenges.💾 **Pluggable storage backends** bring persistent state to FastMCP servers. Built on](https://github.com/jlowin/fastmcp/releases/tag/v2.13.0) [py-key-value-aio](https://github.com/strawgate/py-key-value), a new library from FastMCP maintainer Bill Easton ([@strawgate](https://github.com/strawgate)), the storage layer provides encrypted disk storage by default, platform-aware token management, and a simple key-value interface for application state. We’re excited to bring this elegantly designed library into the FastMCP ecosystem - it’s both powerful and remarkably easy to use, including wrappers to add encryption, TTLs, caching, and more to backends ranging from Elasticsearch, Redis, DynamoDB, filesystem, in-memory, and more!🔐 **OAuth maturity** brings months of production learnings into the framework. The new consent screen prevents confused deputy and authorization bypass attacks discovered in earlier versions, while the OAuth proxy now issues its own tokens with automatic key derivation. RFC 7662 token introspection support enables enterprise auth flows, and path prefix mounting enables OAuth-protected servers to integrate into existing web applications. FastMCP now supports out-of-the-box authentication with [WorkOS](https://gofastmcp.com/integrations/workos) and [AuthKit](https://gofastmcp.com/integrations/authkit), [GitHub](https://gofastmcp.com/integrations/github), [Google](https://gofastmcp.com/integrations/google), [Azure](https://gofastmcp.com/integrations/azure) (Entra ID), [AWS Cognito](https://gofastmcp.com/integrations/aws-cognito), [Auth0](https://gofastmcp.com/integrations/auth0), [Descope](https://gofastmcp.com/integrations/descope), [Scalekit](https://gofastmcp.com/integrations/scalekit), [JWTs](https://gofastmcp.com/servers/auth/token-verification#jwt-token-verification), and [RFC 7662 token introspection](https://gofastmcp.com/servers/auth/token-verification#token-introspection-protocol).⚡ **Response Caching Middleware** dramatically improves performance for expensive operations, while **Server lifespans** provide proper initialization and cleanup hooks that run once per server instance instead of per client session.✨ **Developer experience improvements** include Pydantic input validation, icon support, RFC 6570 query parameters for resource templates, improved Context API methods, and async file/directory resources.