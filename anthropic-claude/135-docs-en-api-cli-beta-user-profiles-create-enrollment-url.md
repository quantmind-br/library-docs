---
title: Create Enrollment URL (Beta) (cli)
url: https://platform.claude.com/docs/en/api/cli/beta/user_profiles/create_enrollment_url.md
source: llms
fetched_at: 2026-04-16T22:40:33.66408777-03:00
rendered_js: false
word_count: 49
summary: This document provides the API specification for generating a unique enrollment URL for a specific user profile using the Anthropic CLI.
tags:
    - api-reference
    - user-profiles
    - enrollment-url
    - cli-command
    - beta-features
category: api
---

## Create Enrollment URL

`$ ant beta:user-profiles create-enrollment-url`

**post** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `--user-profile-id: string`

  Path parameter user_profile_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_user_profile_enrollment_url: object { expires_at, type, url }`

  - `expires_at: string`

    A timestamp in RFC 3339 format

  - `type: "enrollment_url"`

    Object type. Always `enrollment_url`.

    - `"enrollment_url"`

  - `url: string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```cli
ant beta:user-profiles create-enrollment-url \
  --api-key my-anthropic-api-key \
  --user-profile-id uprof_011CZkZCu8hGbp5mYRQgUmz9
```