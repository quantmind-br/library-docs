---
title: Changelog - FastMCP
url: https://gofastmcp.com/v2/changelog
source: crawler
fetched_at: 2026-01-22T22:22:07.235208229-03:00
rendered_js: false
word_count: 447
summary: This document announces the release of FastMCP v2.13.0, detailing new features such as pluggable storage backends, hardened OAuth implementations, and response caching middleware.
tags:
    - fastmcp
    - release-notes
    - oauth
    - caching
    - persistent-storage
    - python
category: reference
---

[**v2.13.0: Cache Me If You Can**](https://github.com/jlowin/fastmcp/releases/tag/v2.13.0)FastMCP 2.13 “Cache Me If You Can” represents a fundamental maturation of the framework. After months of community feedback on authentication and state management, this release delivers the infrastructure FastMCP needs to handle production workloads: persistent storage, response caching, and pragmatic OAuth improvements that reflect real-world deployment challenges.💾 **Pluggable storage backends** bring persistent state to FastMCP servers. Built on [py-key-value-aio](https://github.com/strawgate/py-key-value), a new library from FastMCP maintainer Bill Easton ([@strawgate](https://github.com/strawgate)), the storage layer provides encrypted disk storage by default, platform-aware token management, and a simple key-value interface for application state. We’re excited to bring this elegantly designed library into the FastMCP ecosystem - it’s both powerful and remarkably easy to use, including wrappers to add encryption, TTLs, caching, and more to backends ranging from Elasticsearch, Redis, DynamoDB, filesystem, in-memory, and more! OAuth providers now automatically persist tokens across restarts, and developers can store arbitrary state without reaching for external databases. This foundation enables long-running sessions, cached credentials, and stateful applications built on MCP.🔐 **OAuth maturity** brings months of production learnings into the framework. The new consent screen prevents confused deputy and authorization bypass attacks discovered in earlier versions while providing a clean UX with customizable branding. The OAuth proxy now issues its own tokens with automatic key derivation from client secrets, and RFC 7662 token introspection support enables enterprise auth flows. Path prefix mounting enables OAuth-protected servers to integrate into existing web applications under custom paths like `/api`, and MCP 1.17+ compliance with RFC 9728 ensures protocol compatibility. Combined with improved error handling and platform-aware token storage, OAuth is now production-ready and security-hardened for serious applications.FastMCP now supports out-of-the-box authentication with:

- [**WorkOS**](https://gofastmcp.com/integrations/workos) and [**AuthKit**](https://gofastmcp.com/integrations/authkit)
- [**GitHub**](https://gofastmcp.com/integrations/github)
- [**Google**](https://gofastmcp.com/integrations/google)
- [**Azure**](https://gofastmcp.com/integrations/azure) (Entra ID)
- [**AWS Cognito**](https://gofastmcp.com/integrations/aws-cognito)
- [**Auth0**](https://gofastmcp.com/integrations/auth0)
- [**Descope**](https://gofastmcp.com/integrations/descope)
- [**Scalekit**](https://gofastmcp.com/integrations/scalekit)
- [**JWTs**](https://gofastmcp.com/servers/auth/token-verification#jwt-token-verification)
- [**RFC 7662 token introspection**](https://gofastmcp.com/servers/auth/token-verification#token-introspection-protocol)

⚡ **Response Caching Middleware** dramatically improves performance for expensive operations. Cache tool and resource responses with configurable TTLs, reducing redundant API calls and speeding up repeated queries.🔄 **Server lifespans** provide proper initialization and cleanup hooks that run once per server instance instead of per client session. This fixes a long-standing source of confusion in the MCP SDK and enables proper resource management for database connections, background tasks, and other server-level state. Note: this is a breaking behavioral change if you were using the `lifespan` parameter.✨ **Developer experience improvements** include Pydantic input validation for better type safety, icon support for richer UX, RFC 6570 query parameters for resource templates, improved Context API methods (list\_resources, list\_prompts, get\_prompt), and async file/directory resources.This release includes contributions from **20** new contributors and represents the largest feature set in a while. Thank you to everyone who tested preview builds and filed issues - your feedback shaped these improvements!**Full Changelog**: [v2.12.5…v2.13.0](https://github.com/jlowin/fastmcp/compare/v2.12.5...v2.13.0)