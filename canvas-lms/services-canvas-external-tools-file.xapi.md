---
title: xAPI | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/external-tools/file.xapi
source: sitemap
fetched_at: 2026-02-15T09:13:15.460274-03:00
rendered_js: false
word_count: 217
summary: This document explains how external tools can integrate with Canvas using the xAPI callback URL to report user interactions and log activity time for course analytics. It outlines the specific LTI parameters, authentication requirements, and JSON payload structure needed to record page views.
tags:
    - xapi
    - canvas-lms
    - lti-integration
    - activity-tracking
    - analytics
    - callback-url
category: guide
---

Canvas has implemented a small piece of xAPI (Tin Can API). [Go here to learn more about xAPIarrow-up-right](https://www.adlnet.gov/experience-api).

An external tool can ask for an xAPI callback URL, and then POST back an interaction activity to Canvas. This will update the activity time for the user in Canvas, and add a page view for that tool. Page views will show up in the course analytics section as activity.

- The external tool should use the substitution parameter of `$Canvas.xapi.url` in its LTI launch parameters.
- The tool can then save the url value that is given when launched.
- The tool POSTs to that url and signs the request with the LTI OAuth parameters.
- The content-type should be `application/json`, with an xAPI body.
- The `object.id` will be logged as the page view URL.
- `result.duration` must be an [ISO 8601 durationarrow-up-right](http://en.wikipedia.org/wiki/ISO_8601#Durations) if supplied.
  
  - Canvas page views cap at 5 minutes for now. So any value greater than that is just logged as 5 minutes.

Here is an example of the minimum JSON that would log 3 minutes of activity for `http://example.com`:

```
{
"id":"12345678-1234-5678-1234-567812345678",
"actor":{
"account":{
"homePage":"http://www.instructure.com/",
"name":"unique_name_for_user_of_some_kind_maybe_lti_user_id"
}
},
"verb":{
"id":"http://adlnet.gov/expapi/verbs/interacted",
"display":{
"en-US":"interacted"
}
},
"object":{
"id":"http://example.com/"
},
"result":{
"duration":"PT3M0S"
}
}
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).