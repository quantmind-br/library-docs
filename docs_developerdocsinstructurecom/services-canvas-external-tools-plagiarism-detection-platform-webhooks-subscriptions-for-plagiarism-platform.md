---
title: Webhooks Subscriptions for Plagiarism Platform | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/webhooks_subscriptions_for_plagiarism_platform
source: sitemap
fetched_at: 2026-02-15T09:05:20.466394-03:00
rendered_js: false
word_count: 470
summary: This document provides technical specifications for the LTI API used to manage webhook subscriptions within the Canvas Plagiarism Detection Platform, enabling automated event notifications via HTTPS or AWS SQS.
tags:
    - plagiarism-platform
    - webhook-subscriptions
    - lti-api
    - canvas-lms
    - event-notifications
    - api-endpoints
    - webhooks
category: api
---

## Webhooks Subscriptions for Plagiarism Platform API

**LTI API for Webhook Subscriptions (Must use** [**JWT access tokens**](https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/file.jwt_access_tokens) **with this API).**

This is intended for use with Canvas' [Plagiarism Detection Platform](https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/file.plagiarism_platform). For general-purpose event subscriptions see [Live Events](https://developerdocs.instructure.com/services/canvas/data-services/live-events/overview/file.data_service_introduction).

The tool proxy must also have the appropriate enabled capabilities (See appendix).

Webhooks from Canvas are your way to know that a change (e.g. new or updated submission, new or updated assignment, etc.) has taken place.

Webhooks are available via HTTPS to an endpoint you own and specify, or via an AWS SQS queue that you provision, own, and specify. We recommend SQS for the most robust integration, but do support HTTPS for lower volume applications.

We do not deduplicate or batch messages before transmission. Avoid creating multiple identical subscriptions. Webhooks always identify the ID of the subscription that caused them to be sent, allowing you to identify problematic or high volume subscriptions.

We cannot guarantee the transmission order of webhooks. If order is important to your application, you must check the "event\_time" attribute in the "metadata" hash to determine sequence.

[Lti::SubscriptionsApiController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/subscriptions_api_controller.rb)

`POST /api/lti/subscriptions`

**Scope:** `url:POST|/api/lti/subscriptions`

Creates a webook subscription for the specified event type and context.

**Request Parameters:**

The id of the context for the subscription.

`subscription[ContextType]`

The type of context for the subscription. Must be ‘assignment’, ‘account’, or ‘course’.

Array of strings representing the event types for the subscription.

Format to deliver the live events. Must be ‘live-event’ or ‘caliper’.

`subscription[TransportMetadata]`

An object with a single key: ‘Url’. Example: { “Url”: “sqs.example” }

`subscription[TransportType]`

Must be either ‘sqs’ or ‘https’.

[Lti::SubscriptionsApiController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/subscriptions_api_controller.rb)

`DELETE /api/lti/subscriptions/:id`

**Scope:** `url:DELETE|/api/lti/subscriptions/:id`

[Lti::SubscriptionsApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/subscriptions_api_controller.rb)

`GET /api/lti/subscriptions/:id`

**Scope:** `url:GET|/api/lti/subscriptions/:id`

[Lti::SubscriptionsApiController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/subscriptions_api_controller.rb)

`PUT /api/lti/subscriptions/:id`

**Scope:** `url:PUT|/api/lti/subscriptions/:id`

This endpoint uses the same parameters as the create endpoint

[Lti::SubscriptionsApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/subscriptions_api_controller.rb)

`GET /api/lti/subscriptions`

**Scope:** `url:GET|/api/lti/subscriptions`

This endpoint returns a paginated list with a default limit of 100 items per result set. You can retrieve the next result set by setting a ‘StartKey’ header in your next request with the value of the ‘EndKey’ header in the response.

Example use of a ‘StartKey’ header object:

```
{ "Id":"71d6dfba-0547-477d-b41d-db8cb528c6d1","DeveloperKey":"10000000000001" }
```

#### Appendix: Webhook Subscription Required Capabilities

A tool must have certain capabilities enabled in order to create webhook subscriptions for a given event type in a given context. These capabilities can only be obtained through the use of a custom tool consumer profile.

All available event types are listed bellow along with the capability that will allow creating subscriptions of the associated type.

#### `QUIZ_SUBMITTED` Event Type

- vnd.instructure.webhooks.root\_account.quiz\_submitted
- vnd.instructure.webhooks.assignment.quiz\_submitted

<!--THE END-->

- vnd.instructure.webhooks.root\_account.grade\_change

#### `ATTACHMENT_CREATED` Event Type

- vnd.instructure.webhooks.root\_account.attachment\_created
- vnd.instructure.webhooks.assignment.attachment\_created

#### `SUBMISSION_CREATED` Event Type

- vnd.instructure.webhooks.root\_account.submission\_created
- vnd.instructure.webhooks.assignment.submission\_created

#### `SUBMISSION_UPDATED` Event Type

- vnd.instructure.webhooks.root\_account.submission\_updated
- vnd.instructure.webhooks.assignment.submission\_updated

#### `PLAGIARISM_RESUBMIT` Event Type

- vnd.instructure.webhooks.root\_account.plagiarism\_resubmit
- vnd.instructure.webhooks.assignment.plagiarism\_resubmit

<!--THE END-->

- vnd.instructure.webhooks.root\_account.all

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).