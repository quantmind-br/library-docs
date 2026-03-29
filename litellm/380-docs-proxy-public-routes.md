---
title: Control Public & Private Routes | liteLLM
url: https://docs.litellm.ai/docs/proxy/public_routes
source: sitemap
fetched_at: 2026-01-21T19:53:23.044100354-03:00
rendered_js: false
word_count: 154
summary: This document explains how to configure route access controls for the LiteLLM proxy, including setting public, admin-only, and allowed routes using direct paths or wildcard patterns.
tags:
    - litellm-proxy
    - route-management
    - authentication
    - access-control
    - security-configuration
    - wildcard-patterns
category: configuration
---

Control which routes require authentication and which routes are publicly accessible.

## Route Types[​](#route-types "Direct link to Route Types")

Route TypeRequires AuthDescription`public_routes`NoRoutes accessible without any authentication`admin_only_routes`Yes (Admin only)Routes only accessible by [Proxy Admin](https://docs.litellm.ai/docs/proxy/self_serve#available-roles)`allowed_routes`YesRoutes exposed on the proxy. If not set, all routes are exposed

## Quick Start[​](#quick-start "Direct link to Quick Start")

### Make Routes Public[​](#make-routes-public "Direct link to Make Routes Public")

Allow specific routes to be accessed without authentication:

```
general_settings:
master_key: sk-1234
public_routes:["LiteLLMRoutes.public_routes","/spend/calculate"]
```

### Restrict Routes to Admin Only[​](#restrict-routes-to-admin-only "Direct link to Restrict Routes to Admin Only")

Restrict certain routes to only be accessible by Proxy Admin:

```
general_settings:
master_key: sk-1234
admin_only_routes:["/key/generate","/key/delete"]
```

### Limit Available Routes[​](#limit-available-routes "Direct link to Limit Available Routes")

Only expose specific routes on the proxy:

```
general_settings:
master_key: sk-1234
allowed_routes:["/chat/completions","/embeddings","LiteLLMRoutes.public_routes"]
```

## Usage Examples[​](#usage-examples "Direct link to Usage Examples")

### Define Public, Admin Only, and Allowed Routes[​](#define-public-admin-only-and-allowed-routes "Direct link to Define Public, Admin Only, and Allowed Routes")

```
general_settings:
master_key: sk-1234
public_routes:["LiteLLMRoutes.public_routes","/spend/calculate"]
admin_only_routes:["/key/generate"]
allowed_routes:["/chat/completions","/spend/calculate","LiteLLMRoutes.public_routes"]
```

`LiteLLMRoutes.public_routes` is an ENUM corresponding to the default public routes on LiteLLM. [View the source](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/_types.py).

### Testing[​](#testing "Direct link to Testing")

- Test public\_routes
- Test admin\_only\_routes
- Test allowed\_routes

```
curl --request POST \
  --url 'http://localhost:4000/spend/calculate' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hey, how'\''s it going?"}]
  }'
```

This endpoint works without an `Authorization` header.

## Advanced: Wildcard Patterns[​](#advanced-wildcard-patterns "Direct link to Advanced: Wildcard Patterns")

Use wildcard patterns to match multiple routes at once.

### Syntax[​](#syntax "Direct link to Syntax")

PatternDescriptionExample`/path/*`Matches any route starting with `/path/``/api/*` matches `/api/users`, `/api/users/123`

### Examples[​](#examples "Direct link to Examples")

#### Make All Routes Under a Path Public[​](#make-all-routes-under-a-path-public "Direct link to Make All Routes Under a Path Public")

```
general_settings:
master_key: sk-1234
public_routes:
-"LiteLLMRoutes.public_routes"
-"/api/v1/*"# All routes under /api/v1/
-"/health/*"# All health check routes
```

#### Restrict Admin Routes with Wildcards[​](#restrict-admin-routes-with-wildcards "Direct link to Restrict Admin Routes with Wildcards")

```
general_settings:
master_key: sk-1234
admin_only_routes:
-"/admin/*"# All admin routes
-"/internal/*"# All internal routes
```

### Testing Wildcard Routes[​](#testing-wildcard-routes "Direct link to Testing Wildcard Routes")

**Config:**

```
general_settings:
master_key: sk-1234
public_routes:
-"/public/*"
```

**Test:**

```
# This works without auth (matches /public/*)
curl http://localhost:4000/public/status

# This also works without auth (matches /public/*)
curl http://localhost:4000/public/health/detailed

# This requires auth (doesn't match /public/*)
curl http://localhost:4000/private/data
```