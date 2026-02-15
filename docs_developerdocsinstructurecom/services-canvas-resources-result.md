---
title: Result | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/result
source: sitemap
fetched_at: 2026-02-15T09:04:44.655739-03:00
rendered_js: false
word_count: 149
summary: This document outlines the technical specifications for the Canvas LMS Result API, describing the Result object structure and endpoints for retrieving student assignment outcomes within LTI Assignment and Grade Services.
tags:
    - canvas-lms
    - lti-advantage
    - assignment-and-grade-services
    - grading-api
    - ims-global
category: api
---

Result API for 1EdTech (IMS) [Assignment and Grade Services](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.assignment_tools).

**A Result object looks like:**

```
{
  // The fully qualified URL for showing the Result
"id": "http://institution.canvas.com/api/lti/courses/5/line_items/2/results/1",
  // The lti_user_id or the Canvas user_id
"userId": "50 | 'abcasdf'",
  // The score of the result as defined by Canvas, scaled to the resultMaximum
"resultScore": 50,
  // Maximum possible score for this result; 1 is the default value and will be
  // assumed if not specified otherwise. Minimum value of 0 required.
"resultMaximum": 50,
  // Comment visible to the student about the result.
"comment": null,
  // URL of the line item this belongs to
"scoreOf": "http://institution.canvas.com/api/lti/courses/5/line_items/2"
}
```

[Lti::Ims::ResultsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/results_controller.rb)

`GET /api/lti/courses/:course_id/line_items/:line_item_id/results`

**Scope:** `url:GET|/api/lti/courses/:course_id/line_items/:line_item_id/results`

Show existing Results of a line item. Can be used to retrieve a specific student’s result by adding the user\_id (defined as the lti\_user\_id or the Canvas user\_id) as a query parameter (i.e. user\_id=1000). If user\_id is included, it will return only one Result in the collection if the result exists, otherwise it will be empty. May also limit number of results by adding the limit query param (i.e. limit=100)

Returns a [Result](https://developerdocs.instructure.com/services/canvas/resources/result#result) object.

[Lti::Ims::ResultsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/results_controller.rb)

`GET /api/lti/courses/:course_id/line_items/:line_item_id/results/:id`

**Scope:** `url:GET|/api/lti/courses/:course_id/line_items/:line_item_id/results/:id`

Show existing Result of a line item.

Returns a [Result](https://developerdocs.instructure.com/services/canvas/resources/result#result) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).