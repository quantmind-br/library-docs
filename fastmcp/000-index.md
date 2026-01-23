---
description: Auto-generated documentation index for FastMCP
generated: 2026-01-22T22:24:00Z
source: https://gofastmcp.com/
total_docs: 78
categories: 13
---

# FastMCP Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.
> FastMCP is a Python framework for building Model Context Protocol (MCP) servers and clients.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://gofastmcp.com/ |
| **Generated** | 2026-01-22 |
| **Total Documents** | 78 |
| **Strategy** | crawler |
| **Main Version** | 3.0 (files 001-063) |
| **Legacy Version** | 2.0 (files 064-078) |

---

## Document Index

### 1. Getting Started (001-003)
*Introduction to FastMCP, installation, and quickstart guide*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-getting-started-welcome.md` | Welcome to FastMCP 3.0! | Python framework for building MCP applications connecting LLMs to tools and data | fastmcp, mcp-server, python-framework, llm-integration |
| 002 | `002-getting-started-installation.md` | Installation | Install FastMCP and verify setup, upgrade from previous versions | installation, python, upgrade-guide, dependency-management |
| 003 | `003-getting-started-quickstart.md` | Quickstart | Create FastMCP server, register tools, run via transports, deploy to Prefect Horizon | fastmcp, mcp-server, deployment, mcp-tooling |

### 2. Server Core (004-007)
*Core server class and primary component types: tools, resources, prompts*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 004 | `004-servers-server.md` | The FastMCP Server | Core FastMCP class for building MCP servers, tools, resources, prompts, lifecycle | mcp-server, python-api, http-transport, server-orchestration |
| 005 | `005-servers-tools.md` | Tools | Define Python functions as executable capabilities for MCP clients | mcp-protocol, llm-tools, type-annotations, pydantic-validation |
| 006 | `006-servers-resources.md` | Resources & Templates | Expose static/dynamic data sources with URIs, content types, visibility controls | mcp-resources, resource-templates, uri-handling, python-sdk |
| 007 | `007-servers-prompts.md` | Prompts | Create reusable parameterized prompt templates for MCP clients | mcp-prompts, prompt-engineering, message-templates, llm-integration |

### 3. Server Providers (008-014)
*Component providers for sourcing tools, resources, and prompts from various sources*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 008 | `008-servers-providers-overview.md` | Providers Overview | Component provider abstraction, aggregating from multiple sources | component-providers, server-composition, proxying, transforms |
| 009 | `009-servers-providers-local.md` | Local Provider | Default provider for decorator-registered components | localprovider, component-registration, visibility-control |
| 010 | `010-servers-providers-filesystem.md` | Filesystem Provider | Auto-discovery of components from Python files in directories | filesystemprovider, tool-discovery, resource-registration |
| 011 | `011-servers-providers-proxy.md` | MCP Proxy Provider | Source components from other MCP servers, transport bridging | mcp-proxy, transport-bridging, session-isolation, server-aggregation |
| 012 | `012-servers-providers-mounting.md` | Mounting Servers | Compose servers by mounting one inside another | server-mounting, modular-architecture, namespacing, proxy-mounting |
| 013 | `013-servers-providers-custom.md` | Custom Providers | Build providers sourcing from databases, APIs, external systems | custom-providers, lifecycle-management, backend-integration |
| 014 | `014-servers-providers-skills.md` | Skills Provider | Expose agent skill directories as MCP resources | mcp-resources, agent-skills, claude-code, cursor |

### 4. Server Transforms (015-019)
*Modify components as they flow through your server*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 015 | `015-servers-transforms-transforms.md` | Transforms Overview | Implement transforms to modify tools, resources, prompts | transforms, middleware, component-modification |
| 016 | `016-servers-transforms-namespace.md` | Namespace Transform | Prefix component names to prevent conflicts | namespacing, server-composition, mcp-tools |
| 017 | `017-servers-transforms-tool-transformation.md` | Tool Transformation | Modify tool schemas, rename arguments, customize behavior | tool-transformation, schema-modification, api-design |
| 018 | `018-servers-transforms-prompts-as-tools.md` | Prompts as Tools | Expose prompts to tool-only clients | prompts-as-tools, interoperability, tool-calling |
| 019 | `019-servers-transforms-resources-as-tools.md` | Resources as Tools | Expose resources to tool-only clients | resources-as-tools, api-bridging, server-configuration |

### 5. Server Auth & Security (020-024)
*Authentication, authorization, and visibility control*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 020 | `020-servers-auth-authentication.md` | Authentication | Authentication patterns from API keys to full OAuth 2.1 integration | mcp-protocol, authentication, oauth-2-0, token-validation |
| 021 | `021-servers-auth-token-verification.md` | Token Verification | Validate bearer tokens via JWKS, symmetric keys, static public keys | token-verification, jwt, authentication, bearer-token |
| 022 | `022-servers-auth-full-oauth-server.md` | Full OAuth Server | Build self-contained auth system managing users, tokens | oauth-server, authentication, authorization, oauth-2-1 |
| 023 | `023-servers-authorization.md` | Authorization | Callable-based authorization checks filtering visibility and permissions | authorization, middleware, auth-context, access-control |
| 024 | `024-servers-visibility.md` | Component Visibility | Dynamically manage component availability at runtime | dynamic-visibility, feature-flags, access-control |

### 6. Server Features (025-029)
*Advanced server capabilities: middleware, lifespan, pagination, tasks, icons*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 025 | `025-servers-middleware.md` | Middleware | Cross-cutting functionality for logging, auth, request transformation | middleware, request-pipeline, server-hooks |
| 026 | `026-servers-lifespan.md` | Lifespans | Server-level setup/teardown with composable lifespans | lifespan-events, server-lifecycle, context-management |
| 027 | `027-servers-pagination.md` | Pagination | Control how servers return large component lists to clients | pagination, api-design, cursor-handling |
| 028 | `028-servers-tasks.md` | Background Tasks | Run long-running operations asynchronously with progress tracking | background-tasks, redis, task-scheduler, progress-reporting |
| 029 | `029-servers-icons.md` | Icons | Add visual icons to servers, tools, resources, prompts | icon-implementation, user-interface, data-uri |

### 7. Clients (030-040)
*FastMCP client for interacting with MCP servers*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 030 | `030-clients-client.md` | The FastMCP Client | Programmatic client for MCP servers, connection lifecycle | mcp-client, python-sdk, connection-management, transport-layer |
| 031 | `031-clients-transports.md` | Client Transports | Configure STDIO, HTTP, in-memory connections | transport-layer, stdio-transport, http-transport |
| 032 | `032-clients-tools.md` | Calling Tools | Execute server-side tools, handle structured results | tool-execution, mcp-client, error-handling |
| 033 | `033-clients-resources.md` | Reading Resources | Access static/templated data sources via URIs | resource-handling, uri-templates, data-fetching |
| 034 | `034-clients-prompts.md` | Getting Prompts | Retrieve rendered message templates with argument serialization | mcp-prompts, llm-interaction, argument-serialization |
| 035 | `035-clients-roots.md` | Client Roots | Provide local context and resource boundaries to servers | roots, client-configuration, local-resources |
| 036 | `036-clients-logging.md` | Server Logging | Receive and handle log messages from MCP servers | logging, log-handler, structured-logging |
| 037 | `037-clients-progress.md` | Progress Monitoring | Handle progress notifications from long-running operations | progress-tracking, event-handlers, long-running-tasks |
| 038 | `038-clients-sampling.md` | LLM Sampling | Handle server-initiated LLM completion requests | llm-sampling, openai-integration, anthropic-integration |
| 039 | `039-clients-elicitation.md` | User Elicitation | Handle server requests for structured user input | user-elicitation, interactive-tools, input-handling |
| 040 | `040-clients-auth-bearer.md` | Bearer Token Authentication | Authenticate client with bearer tokens, BearerAuth helper | bearer-authentication, jwt, api-keys |

### 8. Integrations (041-050)
*OAuth integrations with identity providers*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 041 | `041-integrations-auth0.md` | Auth0 OAuth | Secure FastMCP server with Auth0 OAuth | auth0, oauth, oidc, authentication |
| 042 | `042-integrations-authkit.md` | AuthKit (WorkOS) | Secure with AuthKit by WorkOS, Remote OAuth pattern | workos, authkit, remote-oauth |
| 043 | `043-integrations-workos.md` | WorkOS Connect | Authenticate with WorkOS Connect via OAuth Proxy pattern | workos-connect, oauth-authentication, token-management |
| 044 | `044-integrations-google.md` | Google OAuth | Secure with Google OAuth via GoogleProvider | google-oauth, oauth-proxy, token-storage |
| 045 | `045-integrations-github.md` | GitHub OAuth | Secure with GitHub OAuth via GitHubProvider | github-oauth, oauth-proxy, token-management |
| 046 | `046-integrations-azure.md` | Azure (Microsoft Entra ID) | Secure with Azure OAuth and Microsoft Entra ID | azure-oauth, microsoft-entra-id, jwt-validation |
| 047 | `047-integrations-aws-cognito.md` | AWS Cognito OAuth | Secure with AWS Cognito user pools | aws-cognito, oauth, jwt-validation |
| 048 | `048-integrations-descope.md` | Descope | Secure with Descope via Remote OAuth pattern | descope, remote-oauth, jwt-validation |
| 049 | `049-integrations-scalekit.md` | Scalekit | Secure with Scalekit via ScalekitProvider | scalekit, oauth-2-1, jwt-validation |
| 050 | `050-integrations-openai.md` | OpenAI API | Connect FastMCP servers to OpenAI Responses API | openai-api, tool-calling, remote-tools |

### 9. Deployment (051-054)
*Running and deploying FastMCP servers*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 051 | `051-deployment-running-server.md` | Running Your Server | Run locally via STDIO, HTTP, CLI for development/testing | stdio-transport, http-transport, python-cli, local-development |
| 052 | `052-deployment-http.md` | HTTP Deployment | Deploy as remote HTTP services, ASGI apps, security config | remote-deployment, asgi, cors, health-checks |
| 053 | `053-deployment-server-configuration.md` | Project Configuration | Use fastmcp.json for declarative configuration | fastmcp-json, configuration-management, json-schema |
| 054 | `054-deployment-prefect-horizon.md` | Prefect Horizon | Deploy to Prefect Horizon platform for managed hosting | prefect-horizon, deployment, server-management |

### 10. Patterns (055-057)
*CLI usage, testing, and community modules*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 055 | `055-patterns-cli.md` | FastMCP CLI | Command-line interface for managing, running, developing servers | cli-reference, command-line-interface, dependency-management |
| 056 | `056-patterns-testing.md` | Testing your FastMCP Server | Test servers with Pytest and FastMCP Client | pytest, testing, async-testing |
| 057 | `057-patterns-contrib.md` | Contrib Modules | Community-contributed modules extending FastMCP | contrib-package, community-modules, extension-usage |

### 11. Development (058-061)
*Contributing, testing, releases, and upgrade guides*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 058 | `058-development-tests.md` | Tests | Testing patterns and requirements for FastMCP development | testing, pytest, unit-testing, integration-testing |
| 059 | `059-development-contributing.md` | Contributing | Development workflow, design principles, PR requirements | contributing, development-standards, pull-requests |
| 060 | `060-development-releases.md` | Releases | Versioning policy and release process | semantic-versioning, release-policy, breaking-changes |
| 061 | `061-development-upgrade-guide.md` | Upgrade Guide | Migration instructions between FastMCP versions | migration-guide, breaking-changes, version-upgrade |

### 12. Changelog & Updates (062-063)
*Release notes and version updates*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 062 | `062-changelog.md` | Changelog | Release notes for FastMCP versions | release-notes, oauth, caching, persistent-storage |
| 063 | `063-updates.md` | FastMCP Updates | Version 2.13 features: storage backends, OAuth, caching | release-notes, oauth-authentication, caching-middleware |

---

## V2 Legacy Documentation (064-078)
*Documentation for FastMCP 2.0 - refer to main docs (001-063) for current version*

### 13. V2 Getting Started (064-066)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 064 | `064-v2-getting-started-welcome.md` | Welcome to FastMCP 2.0! | V2 introduction to FastMCP Python framework | fastmcp, model-context-protocol, python-framework |
| 065 | `065-v2-getting-started-installation.md` | Installation (V2) | V2 install, verify, upgrade instructions | installation, python-sdk, versioning-policy |
| 066 | `066-v2-getting-started-quickstart.md` | Quickstart (V2) | V2 quickstart for creating, running, deploying servers | mcp-server, http-transport, stdio-transport |

### 14. V2 Server (067)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 067 | `067-v2-servers-server.md` | The FastMCP Server (V2) | V2 server class for tools, resources, prompts | mcp-server, server-configuration, api-integration |

### 15. V2 Patterns (068-072)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 068 | `068-v2-patterns-cli.md` | FastMCP CLI (V2) | V2 CLI for managing and running MCP servers | cli-reference, dependency-management, server-deployment |
| 069 | `069-v2-patterns-testing.md` | Testing (V2) | V2 testing with Pytest and FastMCP Client | pytest, testing, asyncio |
| 070 | `070-v2-patterns-contrib.md` | Contrib Modules (V2) | V2 community-contributed modules | contrib-package, community-extensions |
| 071 | `071-v2-patterns-decorating-methods.md` | Decorating Methods (V2) | Use decorators with instance, class, static methods | python-decorators, method-binding, tool-registration |
| 072 | `072-v2-patterns-tool-transformation.md` | Tool Transformation (V2) | Create enhanced tool variants with modified schemas | tool-transformation, argument-modification |

### 16. V2 Development (073-076)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 073 | `073-v2-development-tests.md` | Tests (V2) | V2 testing patterns and procedures | testing, pytest, unit-testing, integration-testing |
| 074 | `074-v2-development-contributing.md` | Contributing (V2) | V2 contribution guidelines and standards | contributing-guide, pull-requests, code-quality |
| 075 | `075-v2-development-releases.md` | Releases (V2) | V2 versioning strategy and release process | versioning, semantic-versioning, api-stability |
| 076 | `076-v2-development-upgrade-guide.md` | Upgrade Guide (V2) | V2 migration between versions 2.13.0 and 2.14.0 | migration-guide, breaking-changes, versioning |

### 17. V2 Changelog (077-078)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 077 | `077-v2-changelog.md` | Changelog (V2) | V2 release notes: v2.13.0 features | release-notes, oauth, caching, persistent-storage |
| 078 | `078-v2-updates.md` | FastMCP Updates (V2) | V2 version 2.13 release details | release-notes, persistent-storage, oauth-authentication |

---

## Quick Reference

### By Topic

| Topic | File Range |
|-------|------------|
| **Getting Started** | 001-003 |
| **Server Development** | 004-029 |
| **Client Development** | 030-040 |
| **OAuth & Security** | 020-024, 041-049 |
| **Deployment** | 051-054 |
| **CLI & Testing** | 055-056 |
| **V2 Legacy Docs** | 064-078 |

### By Concept

| Concept | Files |
|---------|-------|
| **Tools** | 005, 017, 018, 032 |
| **Resources** | 006, 019, 033 |
| **Prompts** | 007, 018, 034 |
| **Authentication** | 020-022, 040-049 |
| **Providers** | 008-014 |
| **Transforms** | 015-019 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read files **001-003** for introduction, installation, and quickstart
- Understand the core server class in file **004**

### Level 2: Core Components
- Learn about Tools in file **005**
- Learn about Resources in file **006**
- Learn about Prompts in file **007**

### Level 3: Server Architecture
- Explore Providers in files **008-014**
- Understand Transforms in files **015-019**

### Level 4: Security & Auth
- Implement Authentication with files **020-024**
- Add OAuth integrations from files **041-050**

### Level 5: Client Development
- Build clients using files **030-040**

### Level 6: Deployment
- Deploy servers using files **051-054**
- Use CLI patterns from file **055**

### Level 7: Advanced & Reference
- Testing patterns in files **056, 058**
- Contributing guidelines in file **059**
- Changelog and updates in files **062-063**

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression. Main documentation (001-063) covers FastMCP 3.0; legacy V2 documentation is in files 064-078.*
