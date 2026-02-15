---
title: Plagiarism Detection Platform Assignments | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/plagiarism_detection_platform_assignments
source: sitemap
fetched_at: 2026-02-15T09:05:14.278054-03:00
rendered_js: false
word_count: 113
summary: This document details the Plagiarism Detection Platform Assignments API endpoint used to retrieve specific Canvas assignment data using JWT access tokens. It defines the LtiAssignment object structure and provides the request parameters for fetching individual assignments by ID.
tags:
    - canvas-lms
    - assignments-api
    - plagiarism-detection
    - lti-integration
    - jwt-authentication
    - rest-api
category: api
---

## Plagiarism Detection Platform Assignments API

**Plagiarism Detection Platform API for Assignments (Must use** [**JWT access tokens**](https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/file.jwt_access_tokens) **with this API).**

**A LtiAssignment object looks like:**

```
// A Canvas assignment
{
"id": 4,
"name": "Midterm Review",
"description": "<p>Do the following:</p>...",
"points_possible": 10,
  // The due date for the assignment. If a user id is supplied and an assignment
  // override is in place this field will reflect the due date as it applies to
  // the user.
"due_at": "2012-07-01T23:59:00-06:00",
"lti_id": "86157096483e6b3a50bfedc6bac902c0b20a824f",
"course_id": 10000000000060,
"lti_course_id": "66157096483e6b3a50bfedc6bac902c0b20a8241"
}
```

[Lti::PlagiarismAssignmentsApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/plagiarism_assignments_api_controller.rb)

`GET /api/lti/assignments/:assignment_id`

**Scope:** `url:GET|/api/lti/assignments/:assignment_id`

Get a single Canvas assignment by Canvas id or LTI id. Tool providers may only access assignments that are associated with their tool.

**Request Parameters:**

The id of the user. Can be a Canvas or LTI id for the user.

Returns a [LtiAssignment](https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/plagiarism_detection_platform_assignments#ltiassignment) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).