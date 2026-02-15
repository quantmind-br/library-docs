---
title: AI Experiences | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/ai_experiences
source: sitemap
fetched_at: 2026-02-15T08:56:12.571698-03:00
rendered_js: false
word_count: 325
summary: This document defines the REST API endpoints and data structures for managing AI-powered interactive learning experiences and monitoring student conversation history within courses.
tags:
    - canvas-lms
    - ai-experiences
    - interactive-learning
    - api-documentation
    - course-management
    - educational-technology
category: api
---

API for creating, accessing and updating AI Experiences. AI Experiences are used to create interactive AI-powered learning scenarios within courses.

**An AiExperience object looks like:**

```
// An AI Experience for interactive learning
{
  // The ID of the AI experience
"id": 234,
  // The title for the AI experience
"title": "Customer Service Simulation",
  // The description of the AI experience
"description": "Practice customer service skills in a simulated environment",
  // The AI facts for the experience (optional)
"facts": "You are a customer service representative...",
  // The learning objectives for this experience
"learning_objective": "Students will practice active listening and problem-solving",
  // The pedagogical guidance for the experience
"pedagogical_guidance": "A customer is calling about a billing issue",
  // The current published state of the AI experience
"workflow_state": "published",
  // The course this experience belongs to
"course_id": 1578941
}
```

[AiExperiencesController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/ai_experiences_controller.rb)

`GET /api/v1/courses/:course_id/ai_experiences`

**Scope:** `url:GET|/api/v1/courses/:course_id/ai_experiences`

Retrieve the paginated list of AI experiences for a course

**Request Parameters:**

Only return experiences with the specified workflow state. Allowed values: published, unpublished, deleted

Returns a list of [AiExperience](https://developerdocs.instructure.com/services/canvas/resources/ai_experiences#aiexperience) objects.

[AiExperiencesController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/ai_experiences_controller.rb)

`GET /api/v1/courses/:course_id/ai_experiences/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/ai_experiences/:id`

Retrieve an AI experience by ID

Returns an [AiExperience](https://developerdocs.instructure.com/services/canvas/resources/ai_experiences#aiexperience) object.

[AiExperiencesController#newarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/ai_experiences_controller.rb)

`GET /api/v1/courses/:course_id/ai_experiences/new`

**Scope:** `url:GET|/api/v1/courses/:course_id/ai_experiences/new`

Display the form for creating a new AI experience

[AiExperiencesController#editarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/ai_experiences_controller.rb)

`GET /api/v1/courses/:course_id/ai_experiences/:id/edit`

**Scope:** `url:GET|/api/v1/courses/:course_id/ai_experiences/:id/edit`

Display the form for editing an existing AI experience

[AiExperiencesController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/ai_experiences_controller.rb)

`POST /api/v1/courses/:course_id/ai_experiences`

**Scope:** `url:POST|/api/v1/courses/:course_id/ai_experiences`

Create a new AI experience for the specified course

**Request Parameters:**

The title of the AI experience.

The description of the AI experience.

The AI facts for the experience.

The learning objectives for this experience.

The pedagogical guidance for the experience.

The initial state of the experience. Defaults to ‘unpublished’. Allowed values: published, unpublished

Returns an [AiExperience](https://developerdocs.instructure.com/services/canvas/resources/ai_experiences#aiexperience) object.

[AiExperiencesController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/ai_experiences_controller.rb)

`PUT /api/v1/courses/:course_id/ai_experiences/:id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/ai_experiences/:id`

Update an existing AI experience

**Request Parameters:**

The title of the AI experience.

The description of the AI experience.

The AI facts for the experience.

The learning objectives for this experience.

The pedagogical guidance for the experience.

The state of the experience. Allowed values: published, unpublished

Returns an [AiExperience](https://developerdocs.instructure.com/services/canvas/resources/ai_experiences#aiexperience) object.

[AiExperiencesController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/ai_experiences_controller.rb)

`DELETE /api/v1/courses/:course_id/ai_experiences/:id`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/ai_experiences/:id`

Delete an AI experience (soft delete - marks as deleted)

Returns an [AiExperience](https://developerdocs.instructure.com/services/canvas/resources/ai_experiences#aiexperience) object.

[AiExperiencesController#ai\_conversations\_indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/ai_experiences_controller.rb)

`GET /api/v1/courses/:course_id/ai_experiences/:id/ai_conversations`

**Scope:** `url:GET|/api/v1/courses/:course_id/ai_experiences/:id/ai_conversations`

Retrieve the latest AI conversation for each student in the course for this AI experience. Only available to teachers and course managers.

[AiExperiencesController#ai\_conversation\_showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/ai_experiences_controller.rb)

`GET /api/v1/courses/:course_id/ai_experiences/:id/ai_conversations/:conversation_id`

**Scope:** `url:GET|/api/v1/courses/:course_id/ai_experiences/:id/ai_conversations/:conversation_id`

Retrieve a specific student’s AI conversation with full message history. Only available to teachers and course managers.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).