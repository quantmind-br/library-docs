---
title: Brand Configs | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/brand_configs
source: sitemap
fetched_at: 2026-02-15T09:05:28.107836-03:00
rendered_js: false
word_count: 150
summary: This document outlines the API endpoints for retrieving brand configuration variables in Canvas LMS, providing access to account or course-specific branding through redirecting URLs. It details the request formats, scope requirements, and the static nature of the resulting JSON data.
tags:
    - canvas-lms
    - api-documentation
    - brand-variables
    - account-management
    - rest-api
category: api
---

[BrandConfigsApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/brand_configs_api_controller.rb)

`GET /api/v1/brand_variables`

**Scope:** `url:GET|/api/v1/brand_variables`

Will redirect to a static json file that has all of the brand variables used by this account. Even though this is a redirect, do not store the redirected url since if the account makes any changes it will redirect to a new url. Needs no authentication.

**Example Request:**

```
curl'https://<canvas>/api/v1/brand_variables'
```

[BrandConfigsApiController#show\_contextarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/brand_configs_api_controller.rb)

`GET /api/v1/accounts/:account_id/brand_variables`

**Scope:** `url:GET|/api/v1/accounts/:account_id/brand_variables`

`GET /api/v1/courses/:course_id/brand_variables`

**Scope:** `url:GET|/api/v1/courses/:course_id/brand_variables`

Will redirect to a static json file that has all of the brand variables used by the provided context. Even though this is a redirect, do not store the redirected url since if the sub-account makes any changes it will redirect to a new url.

**Example Request:**

```
curl'https://<canvas>/api/v1/accounts/123/brand_variables'
-H'Authorization: Bearer <token>'
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).