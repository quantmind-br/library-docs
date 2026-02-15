---
title: Masquerading | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/basics/file.masquerading
source: sitemap
fetched_at: 2026-02-15T09:13:10.84293-03:00
rendered_js: false
word_count: 219
summary: This document explains how to perform API calls on behalf of other users using the masquerading feature in Canvas LMS, including permission requirements and implementation methods.
tags:
    - canvas-api
    - masquerading
    - user-impersonation
    - authentication
    - permissions
    - sis-ids
category: guide
---

Masquerading is making an API call on behalf of another user. It will behave as if the target user had made the API call with their own access token (even if they don't have one), including permission checks, enrollments, etc. In order to masquerade via the API, the calling user must have the "Become other users" permission. If the target user is also an admin, the calling user must additionally have every permission that the target user has. For auditing purposes, all calls log both the calling user and the target user.

To masquerade, add an as\_user\_id parameter to any request. It can be either a Canvas user ID, or an SIS user ID (as described in [SIS IDs](https://developerdocs.instructure.com/services/canvas/basics/file.object_ids)):

```
curl'https://<canvas>/api/v1/users/self/activity_stream?as_user_id=sis_user_id:brian'\
-H"Authorization: Bearer <token>"
```

Masquerading could be useful in a number of use cases:

- For developing an admin tool
- For accessing APIs that can only be called on self (i.e. the activity stream as shown above)
- For a portal type application that's already tightly integrated with an SIS and is managed by the school, to avoid going through the OAuth flow for every student

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).