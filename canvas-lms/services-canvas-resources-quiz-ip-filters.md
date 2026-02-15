---
title: Quiz IP Filters | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/quiz_ip_filters
source: sitemap
fetched_at: 2026-02-15T09:08:58.981106-03:00
rendered_js: false
word_count: 79
summary: This document outlines the API endpoint for retrieving a list of available IP filters associated with a specific quiz in Canvas LMS.
tags:
    - canvas-lms
    - quiz-api
    - ip-filters
    - rest-api
    - network-security
category: api
---

API for accessing quiz IP filters

**A QuizIPFilter object looks like:**

```
{
  // A unique name for the filter.
"name": "Current Filter",
  // Name of the Account (or Quiz) the IP filter is defined in.
"account": "Some Quiz",
  // An IP address (or range mask) this filter embodies.
"filter": "192.168.1.1/24"
}
```

[Quizzes::QuizIpFiltersController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_ip_filters_controller.rb)

`GET /api/v1/courses/:course_id/quizzes/:quiz_id/ip_filters`

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/ip_filters`

Get a list of available IP filters for this Quiz.

**200 OK** response code is returned if the request was successful.

**Example Response:**

```
{
"quiz_ip_filters": [QuizIPFilter]
}
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).