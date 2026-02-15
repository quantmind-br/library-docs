---
title: Proficiency Ratings | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/proficiency_ratings
source: sitemap
fetched_at: 2026-02-15T09:09:23.462077-03:00
rendered_js: false
word_count: 194
summary: This document describes the API endpoints and data structures for creating, updating, and retrieving proficiency ratings within the Canvas LMS platform. It explains how to manage rating scales for accounts and courses, including point values and mastery thresholds.
tags:
    - canvas-lms
    - api-documentation
    - proficiency-ratings
    - learning-outcomes
    - account-management
    - educational-technology
category: api
---

API for customizing proficiency ratings

**A ProficiencyRating object looks like:**

```
{
  // The description of the rating
"description": "Exceeds Mastery",
  // A non-negative number of points for the rating
"points": 4,
  // Indicates the rating where mastery is first achieved
"mastery": false,
  // The hex color code of the rating
"color": "02672D"
}
```

**A Proficiency object looks like:**

```
{
  // An array of proficiency ratings. See the ProficiencyRating specification
  // above.
"ratings": []
}
```

[OutcomeProficiencyApiController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_proficiency_api_controller.rb)

`POST /api/v1/accounts/:account_id/outcome_proficiency`

**Scope:** `url:POST|/api/v1/accounts/:account_id/outcome_proficiency`

`POST /api/v1/courses/:course_id/outcome_proficiency`

**Scope:** `url:POST|/api/v1/courses/:course_id/outcome_proficiency`

Create or update account-level proficiency ratings. These ratings will apply to all sub-accounts, unless they have their own account-level proficiency ratings defined.

**Request Parameters:**

The description of the rating level.

The non-negative number of points of the rating level. Points across ratings should be strictly decreasing in value.

Indicates the rating level where mastery is first achieved. Only one rating in a proficiency should be marked for mastery.

The color associated with the rating level. Should be a hex color code like ‘00FFFF’.

**Example Request:**

```
curl 'https://<canvas>/api/v1/accounts/<account_id>/outcome_proficiency' \
     -X POST \
     -F 'ratings[][description]=Exceeds Mastery' \
     -F 'ratings[][points]=4' \
     -F 'ratings[][color]=02672D' \
     -F 'ratings[][mastery]=false' \
     -F 'ratings[][description]=Mastery' \
     -F 'ratings[][points]=3' \
     -F 'ratings[][color]=03893D' \
     -F 'ratings[][mastery]=true' \
     -F 'ratings[][description]=Near Mastery' \
     -F 'ratings[][points]=2' \
     -F 'ratings[][color]=FAB901' \
     -F 'ratings[][mastery]=false' \
     -F 'ratings[][description]=Below Mastery' \
     -F 'ratings[][points]=1' \
     -F 'ratings[][color]=FD5D10' \
     -F 'ratings[][mastery]=false' \
     -F 'ratings[][description]=Well Below Mastery' \
     -F 'ratings[][points]=0' \
     -F 'ratings[][color]=E62429' \
     -F 'ratings[][mastery]=false' \
     -H "Authorization: Bearer <token>"
```

Returns a [Proficiency](https://developerdocs.instructure.com/services/canvas/resources/proficiency_ratings#proficiency) object.

[OutcomeProficiencyApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_proficiency_api_controller.rb)

`GET /api/v1/accounts/:account_id/outcome_proficiency`

**Scope:** `url:GET|/api/v1/accounts/:account_id/outcome_proficiency`

`GET /api/v1/courses/:course_id/outcome_proficiency`

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_proficiency`

Get account-level proficiency ratings. If not defined for this account, it will return proficiency ratings for the nearest super-account with ratings defined. Will return 404 if none found.

```
Examples:
  curl https://<canvas>/api/v1/accounts/<account_id>/outcome_proficiency \
      -H 'Authorization: Bearer <token>'
```

Returns a [Proficiency](https://developerdocs.instructure.com/services/canvas/resources/proficiency_ratings#proficiency) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).