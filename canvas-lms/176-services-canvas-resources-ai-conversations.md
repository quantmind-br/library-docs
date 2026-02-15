---
title: AI Conversations | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/ai_conversations
source: sitemap
fetched_at: 2026-02-15T08:56:18.682015-03:00
rendered_js: false
word_count: 124
summary: This document outlines the API endpoints for managing AI-driven conversations within Canvas LMS, including creating, retrieving, and interacting with AI experiences.
tags:
    - canvas-lms
    - ai-conversations
    - rest-api
    - api-documentation
    - messaging
    - educational-technology
category: api
---

API for managing conversations with AI Experiences.

[AiConversationsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/ai_conversations_controller.rb)

`GET /api/v1/courses/:course_id/ai_experiences/:ai_experience_id/conversations/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/ai_experiences/:ai_experience_id/conversations/:id`

Get a specific conversation by ID (for teachers viewing student conversations)

[AiConversationsController#active\_conversationarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/ai_conversations_controller.rb)

`GET /api/v1/courses/:course_id/ai_experiences/:ai_experience_id/conversations`

**Scope:** `url:GET|/api/v1/courses/:course_id/ai_experiences/:ai_experience_id/conversations`

Get the active conversation for the current user and AI experience

[AiConversationsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/ai_conversations_controller.rb)

`POST /api/v1/courses/:course_id/ai_experiences/:ai_experience_id/conversations`

**Scope:** `url:POST|/api/v1/courses/:course_id/ai_experiences/:ai_experience_id/conversations`

Initialize a new conversation with the AI experience

[AiConversationsController#post\_messagearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/ai_conversations_controller.rb)

`POST /api/v1/courses/:course_id/ai_experiences/:ai_experience_id/conversations/:id/messages`

**Scope:** `url:POST|/api/v1/courses/:course_id/ai_experiences/:ai_experience_id/conversations/:id/messages`

Send a message to an existing conversation and get the AI response

**Request Parameters:**

The user’s message to send to the AI

[AiConversationsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/ai_conversations_controller.rb)

`DELETE /api/v1/courses/:course_id/ai_experiences/:ai_experience_id/conversations/:id`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/ai_experiences/:ai_experience_id/conversations/:id`

Mark a conversation as completed/deleted

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).