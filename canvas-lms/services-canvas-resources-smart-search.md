---
title: Smart Search | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/smart_search
source: sitemap
fetched_at: 2026-02-15T08:57:59.590481-03:00
rendered_js: false
word_count: 170
summary: This document describes the Smart Search API endpoint for Canvas LMS, which enables AI-powered, meaning-based searching of course content like assignments and pages.
tags:
    - canvas-lms
    - api-endpoint
    - semantic-search
    - smart-search
    - course-content
category: api
---

BETA: This API resource is not finalized, and there could be breaking changes before its final release.

API for AI-powered course content search. NOTE: This feature has limited availability at present.

**A SearchResult object looks like:**

```
// Reference to an object that matches a smart search
{
  // The ID of the matching object.
"content_id": 2,
  // The type of the matching object.
"content_type": "WikiPage",
  // The title of the matching object.
"title": "Nicolaus Copernicus",
  // The body of the matching object.
"body": "Nicolaus Copernicus was a Renaissance-era mathematician and astronomer who...",
  // The Canvas URL of the matching object.
"html_url": "https://canvas.example.com/courses/123/pages/nicolaus-copernicus",
  // The distance between the search query and the result. Smaller numbers
  // indicate closer matches.
"distance": 0.212
}
```

[SmartSearchController#searcharrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/smart_search_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`GET /api/v1/courses/:course_id/smartsearch`

**Scope:** `url:GET|/api/v1/courses/:course_id/smartsearch`

Find course content using a meaning-based search

**Request Parameters:**

Types of objects to search. By default, all supported types are searched. Supported types include `pages`, `assignments`, `announcements`, and `discussion_topics`.

Optional information to include with each search result:

- modules
  
  An array of module objects that the search result belongs to.
- status
  
  The published status for all results and the due\_date for all assignments.

Allowed values: `status`, `modules`

Returns a list of [SearchResult](https://developerdocs.instructure.com/services/canvas/resources/smart_search#searchresult) objects.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 2 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).