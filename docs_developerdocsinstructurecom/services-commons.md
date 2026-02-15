---
title: Commons | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/commons
source: sitemap
fetched_at: 2026-02-15T09:14:35.604071-03:00
rendered_js: false
word_count: 134
summary: This document provides an overview of the Canvas Commons REST API, detailing authentication requirements, rate limiting policies, and regional endpoint URLs for external data access.
tags:
    - canvas-commons
    - rest-api
    - api-authentication
    - rate-limiting
    - regional-endpoints
category: api
---

Canvas Commons includes a REST API for accessing and modifying data externally from the main application, in your own programs and scripts. This documentation describes the resources that make up the API.

Most API requests require a valid session. To create a session, see the Create a Session Documentation under the the Sessions section.

API requests are limited at a rate of 2500 requests per hour per user.

The endpoints have regional hosts, pick yours from the list below based on you region.

- US/LATAM:
  
  - https://lor.instructure.com/api
  - https://lor-beta.instructure.com/api
- EMEA (hosted in Germany):
  
  - https://commons.eu-central.canvaslms.com/api
  - https://commons-fra-beta.instructure.com/api
- Canada:
  
  - https://commons.ca-central.canvaslms.com/api
  - https://commons-yul-beta.instructure.com/api
- Australia/NZ (hosted in Australia):
  
  - https://commons.sydney.canvaslms.com/api
  - https://commons-syd-beta.instructure.com/api
- Asia Pacific (hosted in Singapore):
  
  - https://commons.singapore.canvaslms.com/api
  - https://commons-sin-beta.instructure.com/api

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).