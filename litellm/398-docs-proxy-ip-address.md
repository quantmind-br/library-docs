---
title: IP Address Filtering | liteLLM
url: https://docs.litellm.ai/docs/proxy/ip_address
source: sitemap
fetched_at: 2026-01-21T19:52:44.646071187-03:00
rendered_js: false
word_count: 30
summary: This document explains how to restrict access to LiteLLM proxy endpoints by configuring a list of allowed IP addresses.
tags:
    - litellm
    - ip-restriction
    - access-control
    - security
    - proxy-configuration
category: configuration
---

info

You need a LiteLLM License to unlock this feature. [Grab time](https://calendly.com/d/4mp-gd3-k5k/litellm-1-1-onboarding-chat), to get one today!

Restrict which IP's can call the proxy endpoints.

```
general_settings:
allowed_ips:["192.168.1.1"]
```

**Expected Response** (if IP not listed)

```
{
    "error": {
        "message": "Access forbidden: IP address not allowed.",
        "type": "auth_error",
        "param": "None",
        "code": 403
    }
}
```