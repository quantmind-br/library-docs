---
title: Error Reports | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/error_reports
source: sitemap
fetched_at: 2026-02-15T09:07:31.777193-03:00
rendered_js: false
word_count: 159
summary: This document describes the API endpoint for creating error reports in the Canvas LMS, outlining the required parameters and the structure of the error report object.
tags:
    - canvas-lms
    - error-reporting
    - api-endpoint
    - post-request
    - error-management
category: api
---

**An ErrorReport object looks like:**

```
// A collection of information around a specific notification of a problem
{
  // The users problem summary, like an email subject line
"subject": "File upload breaking",
  // long form documentation of what was witnessed
"comments": "When I went to upload a .mov file to my files page, I got an error.  Retrying didn't help, other file types seem ok",
  // categorization of how bad the user thinks the problem is.  Should be one of
  // [just_a_comment, not_urgent, workaround_possible, blocks_what_i_need_to_do,
  // extreme_critical_emergency].
"user_perceived_severity": "just_a_comment",
  // the email address of the reporting user
"email": "name@example.com",
  // URL of the page on which the error was reported
"url": "https://canvas.instructure.com/courses/1",
  // string describing the asset being interacted with at the time of error. 
  // Formatted '[type]_[id]'
"context_asset_string": "user_1",
  // comma seperated list of roles the reporting user holds.  Can be one
  // [student], or many [teacher,admin]
"user_roles": "user,teacher,admin"
}
```

[ErrorsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/errors_controller.rb)

`POST /api/v1/error_reports`

**Scope:** `url:POST|/api/v1/error_reports`

Create a new error report documenting an experienced problem

Performs the same action as when a user uses the “help -&gt; report a problem” dialog.

**Request Parameters:**

The summary of the problem

URL from which the report was issued

Email address for the reporting user

The long version of the story from the user one what they experienced

A collection of metadata about the users’ environment. If not provided, canvas will collect it based on information found in the request. (Doesn’t have to be HTTPENV info, could be anything JSON object that can be serialized as a hash, a mobile app might include relevant metadata for itself)

**Example Request:**

```
# Create error report
curl 'https://<canvas>/api/v1/error_reports' \
      -X POST \
      -F 'error[subject]="things are broken"' \
      -F 'error[url]=http://<canvas>/courses/1' \
      -F 'error[description]="All my thoughts on what I saw"' \
      -H 'Authorization: Bearer <token>'
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).