---
title: Canvas Career Experiences | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/canvas_career_experiences
source: sitemap
fetched_at: 2026-02-15T08:56:56.681675-03:00
rendered_js: false
word_count: 158
summary: This document outlines the Canvas Career Experiences API, which allows for managing and switching between academic and career-focused user experiences and roles.
tags:
    - canvas-lms
    - career-experience
    - api-endpoints
    - user-roles
    - experience-management
category: api
---

## Canvas Career Experiences API

API for managing user career experience and role preferences in Canvas.

**An ExperienceSummary object looks like:**

```
{
  // The current active experience. One of: 'academic', 'career_learner',
  // 'career_learning_provider'.
"current_app": "career_learner",
  // List of available experiences for the user. Can include: 'academic',
  // 'career_learner', 'career_learning_provider'.
"available_apps": ["academic","career_learner"]
}
```

[CareerExperienceController#enabledarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/career_experience_controller.rb)

`GET /api/v1/career/enabled`

**Scope:** `url:GET|/api/v1/career/enabled`

Returns whether the root account has Canvas Career (Horizon) enabled in at least one subaccount.

**Example Request:**

```
curlhttps://<canvas>/api/v1/career/enabled\
-H'Authorization: Bearer <token>'
```

**Example Response:**

[CareerExperienceController#experience\_summaryarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/career_experience_controller.rb)

`GET /api/v1/career/experience_summary`

**Scope:** `url:GET|/api/v1/career/experience_summary`

Returns the current user’s active experience and available experiences they can switch to.

**Example Request:**

```
curl https://<canvas>/api/v1/career/experience_summary \
  -H 'Authorization: Bearer <token>'
```

Returns an [ExperienceSummary](https://developerdocs.instructure.com/services/canvas/resources/canvas_career_experiences#experiencesummary) object.

[CareerExperienceController#switch\_experiencearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/career_experience_controller.rb)

`POST /api/v1/career/switch_experience`

**Scope:** `url:POST|/api/v1/career/switch_experience`

Switch the current user’s active experience to the specified one.

**Request Parameters:**

The experience to switch to.

Allowed values: `academic`, `career`

**Example Request:**

```
curl-XPOSThttps://<canvas>/api/v1/career/switch_experience\
-H'Authorization: Bearer <token>'\
-d'experience=academic'
```

[CareerExperienceController#switch\_rolearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/career_experience_controller.rb)

`POST /api/v1/career/switch_role`

**Scope:** `url:POST|/api/v1/career/switch_role`

Switch the current user’s role within the current experience.

**Request Parameters:**

The role to switch to.

Allowed values: `learner`, `learning_provider`

**Example Request:**

```
curl-XPOSThttps://<canvas>/api/v1/career/switch_role\
-H'Authorization: Bearer <token>'\
-d'role=learner'
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).