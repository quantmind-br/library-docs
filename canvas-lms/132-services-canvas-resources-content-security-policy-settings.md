---
title: Content Security Policy Settings | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/content_security_policy_settings
source: sitemap
fetched_at: 2026-02-15T08:58:02.366052-03:00
rendered_js: false
word_count: 535
summary: This document outlines the API endpoints for managing Content Security Policy (CSP) settings, including domain whitelisting and inheritance rules for accounts and courses.
tags:
    - content-security-policy
    - csp-settings
    - security-api
    - domain-whitelisting
    - canvas-lms
    - account-configuration
category: api
---

## Content Security Policy Settings API

BETA: This API resource is not finalized, and there could be breaking changes before its final release.

API for enabling/disabling the use of Content Security Policy headers and configuring allowed domains

[CspSettingsController#get\_csp\_settingsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/csp_settings_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`GET /api/v1/courses/:course_id/csp_settings`

**Scope:** `url:GET|/api/v1/courses/:course_id/csp_settings`

`GET /api/v1/accounts/:account_id/csp_settings`

**Scope:** `url:GET|/api/v1/accounts/:account_id/csp_settings`

Update multiple modules in an account.

**API response field:**

Whether CSP is enabled.

Whether the current CSP settings are inherited from a parent account.

Whether current CSP settings can be overridden by sub-accounts and courses.

If enabled, lists the currently allowed domains (includes domains automatically allowed through external tools).

(Account-only) Lists the automatically allowed domains with their respective external tools

- current\_account\_whitelist

(Account-only) Lists the current list of domains explicitly allowed by this account. (Note: this list will not take effect unless CSP is explicitly enabled on this account)

[CspSettingsController#set\_csp\_settingarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/csp_settings_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`PUT /api/v1/courses/:course_id/csp_settings`

**Scope:** `url:PUT|/api/v1/courses/:course_id/csp_settings`

`PUT /api/v1/accounts/:account_id/csp_settings`

**Scope:** `url:PUT|/api/v1/accounts/:account_id/csp_settings`

Either explicitly sets CSP to be on or off for courses and sub-accounts, or clear the explicit settings to default to those set by a parent account

Note: If “inherited” and “settings\_locked” are both true for this account or course, then the CSP setting cannot be modified.

**Request Parameters:**

If set to “enabled” for an account, CSP will be enabled for all its courses and sub-accounts (that have not explicitly enabled or disabled it), using the allowed domains set on this account. If set to “disabled”, CSP will be disabled for this account or course and for all sub-accounts that have not explicitly re-enabled it. If set to “inherited”, this account or course will reset to the default state where CSP settings are inherited from the first parent account to have them explicitly set.

Allowed values: `enabled`, `disabled`, `inherited`

[CspSettingsController#set\_csp\_lockarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/csp_settings_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`PUT /api/v1/accounts/:account_id/csp_settings/lock`

**Scope:** `url:PUT|/api/v1/accounts/:account_id/csp_settings/lock`

Can only be set if CSP is explicitly enabled or disabled on this account (i.e. “inherited” is false).

**Request Parameters:**

Whether sub-accounts and courses will be prevented from overriding settings inherited from this account.

[CspSettingsController#add\_domainarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/csp_settings_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`POST /api/v1/accounts/:account_id/csp_settings/domains`

**Scope:** `url:POST|/api/v1/accounts/:account_id/csp_settings/domains`

Adds an allowed domain for the current account. Note: this will not take effect unless CSP is explicitly enabled on this account.

**Request Parameters:**

[CspSettingsController#add\_multiple\_domainsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/csp_settings_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`POST /api/v1/accounts/:account_id/csp_settings/domains/batch_create`

**Scope:** `url:POST|/api/v1/accounts/:account_id/csp_settings/domains/batch_create`

Adds multiple allowed domains for the current account. Note: this will not take effect unless CSP is explicitly enabled on this account.

**Request Parameters:**

[CspSettingsController#remove\_domainarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/csp_settings_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`DELETE /api/v1/accounts/:account_id/csp_settings/domains`

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/csp_settings/domains`

Removes an allowed domain from the current account.

**Request Parameters:**

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 2 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).