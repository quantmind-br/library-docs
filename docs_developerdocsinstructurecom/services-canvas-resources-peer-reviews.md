---
title: Peer Reviews | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/peer_reviews
source: sitemap
fetched_at: 2026-02-15T08:58:07.237598-03:00
rendered_js: false
word_count: 170
summary: This document defines the PeerReview object structure and provides technical specifications for API endpoints used to manage and allocate peer reviews within Canvas LMS assignments.
tags:
    - canvas-lms
    - peer-reviews
    - api-documentation
    - rest-api
    - assignment-management
category: api
---

**A PeerReview object looks like:**

```
{
  // The assessors user id
"assessor_id": 23,
  // The id for the asset associated with this Peer Review
"asset_id": 13,
  // The type of the asset
"asset_type": "Submission",
  // The id of the Peer Review
"id": 1,
  // The user id for the owner of the asset
"user_id": 7,
  // The state of the Peer Review, either 'assigned' or 'completed'
"workflow_state": "assigned",
  // the User object for the owner of the asset if the user include parameter is
  // provided (see user API) (optional)
"user": "User",
  // The User object for the assessor if the user include parameter is provided
  // (see user API) (optional)
"assessor": "User",
  // The submission comments associated with this Peer Review if the
  // submission_comment include parameter is provided (see submissions API)
  // (optional)
"submission_comments": "SubmissionComment"
}
```

[PeerReviewsApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/peer_reviews_api_controller.rb)

`GET /api/v1/courses/:course_id/assignments/:assignment_id/peer_reviews`

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/peer_reviews`

`GET /api/v1/sections/:section_id/assignments/:assignment_id/peer_reviews`

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/peer_reviews`

`GET /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

**Scope:** `url:GET|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

`GET /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

**Scope:** `url:GET|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

Get a list of all Peer Reviews for this assignment

**Request Parameters:**

Associations to include with the peer review.

Allowed values: `submission_comments`, `user`

Returns a list of [PeerReview](https://developerdocs.instructure.com/services/canvas/resources/peer_reviews#peerreview) objects.

[PeerReviewsApiController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/peer_reviews_api_controller.rb)

`POST /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

`POST /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

**Scope:** `url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

Create a peer review for the assignment

**Request Parameters:**

user\_id to assign as reviewer on this assignment

Returns a [PeerReview](https://developerdocs.instructure.com/services/canvas/resources/peer_reviews#peerreview) object.

[PeerReviewsApiController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/peer_reviews_api_controller.rb)

`DELETE /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

`DELETE /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

**Scope:** `url:DELETE|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:submission_id/peer_reviews`

Delete a peer review for the assignment

**Request Parameters:**

user\_id to delete as reviewer on this assignment

Returns a [PeerReview](https://developerdocs.instructure.com/services/canvas/resources/peer_reviews#peerreview) object.

[PeerReviewsApiController#allocatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/peer_reviews_api_controller.rb)

`POST /api/v1/courses/:course_id/assignments/:assignment_id/allocate`

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/allocate`

Allocates a submission for the current user to peer review

Returns a [PeerReview](https://developerdocs.instructure.com/services/canvas/resources/peer_reviews#peerreview) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 2 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).