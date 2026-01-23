---
title: Control Model Access with OIDC (Azure AD/Keycloak/etc.) | liteLLM
url: https://docs.litellm.ai/docs/proxy/jwt_auth_arch
source: sitemap
fetched_at: 2026-01-21T19:52:44.812160423-03:00
rendered_js: false
word_count: 90
summary: This document explains how to configure JWT authentication and role-based access control (RBAC) for LiteLLM Proxy using external identity providers like Azure AD and Keycloak.
tags:
    - litellm-proxy
    - jwt-authentication
    - rbac
    - azure-ad
    - keycloak
    - identity-provider
    - access-control
category: configuration
---

## Example Token[​](#example-token "Direct link to Example Token")

- Azure AD
- Keycloak

```
{
  "sub": "1234567890",
  "name": "John Doe",
  "email": "john.doe@example.com",
  "roles": ["basic_user"] # 👈 ROLE
}
```

## Proxy Configuration[​](#proxy-configuration "Direct link to Proxy Configuration")

- Azure AD
- Keycloak

```
general_settings:
enable_jwt_auth:True
litellm_jwtauth:
user_roles_jwt_field:"roles"# the field in the JWT that contains the roles 
user_allowed_roles:["basic_user"]# roles that map to an 'internal_user' role on LiteLLM 
enforce_rbac:true# if true, will check if the user has the correct role to access the model

role_permissions:# control what models are allowed for each role
-role: internal_user
models:["anthropic-claude"]

model_list:
-model: anthropic-claude
litellm_params:
model: claude-3-5-haiku-20241022
-model: openai-gpt-4o
litellm_params:
model: gpt-4o
```

## How it works[​](#how-it-works "Direct link to How it works")

1. Specify JWT\_PUBLIC\_KEY\_URL - This is the public keys endpoint of your OpenID provider. For Azure AD it's `https://login.microsoftonline.com/{tenant_id}/discovery/v2.0/keys`. For Keycloak it's `{keycloak_base_url}/realms/{your-realm}/protocol/openid-connect/certs`.
2. Map JWT roles to LiteLLM roles - Done via `user_roles_jwt_field` and `user_allowed_roles`
   
   - Currently just `internal_user` is supported for role mapping.
3. Specify model access:
   
   - `role_permissions`: control what models are allowed for each role.
     
     - `role`: the LiteLLM role to control access for. Allowed roles = \["internal\_user", "proxy\_admin", "team"]
     - `models`: list of models that the role is allowed to access.
   - `model_list`: parent list of models on the proxy. [Learn more](https://docs.litellm.ai/docs/proxy/configs#llm-configs-model_list)
4. Model Checks: The proxy will run validation checks on the received JWT. [Code](https://github.com/BerriAI/litellm/blob/3a4f5b23b5025b87b6d969f2485cc9bc741f9ba6/litellm/proxy/auth/user_api_key_auth.py#L284)