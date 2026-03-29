---
title: ✨ Event Hooks for SSO Login | liteLLM
url: https://docs.litellm.ai/docs/proxy/custom_sso
source: sitemap
fetched_at: 2026-01-21T19:51:35.318459744-03:00
rendered_js: false
word_count: 131
summary: This document explains how to implement custom SSO login handlers and integrate OAuth proxies with the LiteLLM Admin UI using Python.
tags:
    - litellm
    - sso-authentication
    - oauth-proxy
    - custom-handler
    - admin-ui
category: guide
---

Use this when you have an **OAuth proxy in front of LiteLLM** that has already authenticated the user and passes user information via request headers.

This handler parses request headers and returns user information as an OpenID object:

```
from fastapi import Request
from fastapi_sso.sso.base import OpenID
from litellm.integrations.custom_sso_handler import CustomSSOLoginHandler


classMyCustomSSOLoginHandler(CustomSSOLoginHandler):
"""
    Custom handler for parsing OAuth proxy headers

    Use this when you have an OAuth proxy (like oauth2-proxy, Vouch, etc.) 
    in front of LiteLLM that adds user info to request headers
    """
asyncdefhandle_custom_ui_sso_sign_in(
        self,
        request: Request,
)-> OpenID:
# Parse headers from your OAuth proxy
        request_headers =dict(request.headers)

# Extract user info from headers (adjust header names for your proxy)
        user_id = request_headers.get("x-forwarded-user")or request_headers.get("x-user")
        user_email = request_headers.get("x-forwarded-email")or request_headers.get("x-email")
        user_name = request_headers.get("x-forwarded-preferred-username")or request_headers.get("x-preferred-username")

# Return OpenID object with user information
return OpenID(
id=user_id or"unknown",
            email=user_email or"unknown@example.com",
            first_name=user_name or"Unknown",
            last_name="User",
            display_name=user_name or"Unknown User",
            picture=None,
            provider="oauth-proxy",
)

# Create an instance to be used by LiteLLM
custom_ui_sso_sign_in_handler = MyCustomSSOLoginHandler()
```

When a user attempts navigating to the LiteLLM Admin UI, the request will be routed to your custom UI SSO sign-in handler.

Use this if you want to run your own code **after** a user signs on to the LiteLLM UI using standard SSO providers (Google, Microsoft, etc.)

Make sure the response type follows the `SSOUserDefinedValues` pydantic object. This is used for logging the user into the Admin UI:

```
from fastapi import Request
from fastapi_sso.sso.base import OpenID

from litellm.proxy._types import LitellmUserRoles, SSOUserDefinedValues
from litellm.proxy.management_endpoints.internal_user_endpoints import(
    new_user,
    user_info,
)
from litellm.proxy.management_endpoints.team_endpoints import add_new_member


asyncdefcustom_sso_handler(userIDPInfo: OpenID)-> SSOUserDefinedValues:
try:
print("inside custom sso handler")# noqa
print(f"userIDPInfo: {userIDPInfo}")# noqa

if userIDPInfo.idisNone:
raise ValueError(
f"No ID found for user. userIDPInfo.id is None {userIDPInfo}"
)


#################################################
# Run your custom code / logic here
# check if user exists in litellm proxy DB
        _user_info =await user_info(user_id=userIDPInfo.id)
print("_user_info from litellm DB ", _user_info)# noqa
#################################################

return SSOUserDefinedValues(
            models=[],# models user has access to
            user_id=userIDPInfo.id,# user id to use in the LiteLLM DB
            user_email=userIDPInfo.email,# user email to use in the LiteLLM DB
            user_role=LitellmUserRoles.INTERNAL_USER.value,# role to use for the user 
            max_budget=0.01,# Max budget for this UI login Session
            budget_duration="1d",# Duration of the budget for this UI login Session, 1d, 2d, 30d ...
)
except Exception as e:
raise Exception("Failed custom auth")
```

Pass the filepath to the config.yaml.

e.g. if they're both in the same dir - `./config.yaml` and `./custom_sso.py`, this is what it looks like: