---
title: Query API | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/query-api
source: sitemap
fetched_at: 2026-02-15T09:12:14.054175-03:00
rendered_js: false
word_count: 232
summary: This document introduces the DAP Query API, providing fundamental information on endpoints, HTTP methods, rate limiting, and standard response codes for programmatic data retrieval.
tags:
    - dap-query-api
    - rest-api
    - data-access-platform
    - instructure
    - api-endpoints
    - response-codes
category: api
---

The DAP Query API is a robust RESTful API that enables seamless, programmatic access to data within the Data Access Platform (DAP). Designed to handle large-scale data retrieval, it supports secure, flexible interactions with Instructure datasets.

Before using they Query API, it is recommended to familiarize yourself with the [key concepts of DAP](https://developerdocs.instructure.com/services/dap/key-concepts).

The Query API can be accessed via the following endpoint:

```
https://api-gateway.instructure.com/dap/
```

The HTTP method used in an endpoint determines the type of action performed on a resource. Common methods include `GET`, `POST`, `DELETE`, and `PATCH`. Refer to the REST API reference documentation for details on the HTTP methods for each endpoint.

DAP CLI follows the [rate limiting policies](https://developerdocs.instructure.com/services/dap/limits-policies) of DAP. Be mindful of these limits when making requests.

The Query API uses standard HTTP response codes to indicate the success or failure of requests:

- Codes in the `2xx` range indicate success.
- Codes in the `4xx` range indicate incorrect or incomplete parameters (e.g. invalid authentication credentials, non-exist namespace etc.).
- Codes in the `5xx` range indicate a server-side issue (e.g. gateway timeout error, restricted client access etc.).

[](https://community.canvaslms.com/t5/Data-and-Analytics-Group/gh-p/data)

Visit our forums to connect with the community and learn more about DAP.

[](mailto:canvasdatahelp@instructure.com)

To report bugs or request new features, open a ticket for our Support Team.

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).