---
title: Learning | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/canvas/file.data_service_canvas_learning
source: sitemap
fetched_at: 2026-02-15T09:06:25.95044-03:00
rendered_js: false
word_count: 1737
summary: This document provides a technical reference for event notification schemas triggered by the creation and modification of learning outcomes, outcome groups, and outcome links within the Canvas LMS.
tags:
    - canvas-lms
    - learning-outcomes
    - event-metadata
    - webhooks
    - json-payload
    - api-reference
category: reference
---

**Definition:** The event is emitted anytime a outcome is created in the account by an end user or API request.

**Trigger:** Triggered when a new learning outcome is created.

```
{
"metadata":{
"event_name":"learning_outcome_created",
"event_time":"2019-11-05T10:03:37.526Z",
"job_id":"1020020528469291",
"job_tag":"Canvas::Migration::Worker::CourseCopyWorker#perform",
"producer":"canvas",
"root_account_id":"21070000000000001",
"root_account_lti_guid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
"root_account_uuid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs"
},
"body":{
"calculation_int":65,
"calculation_method":"highest",
"context_id":"1234",
"context_type":"Course",
"description":"Develop understanding of molecular and cell biology.",
"display_name":"Learn molecular biology",
"learning_outcome_id":"12345",
"short_description":"Molecular biology knowledge",
"title":"Molecular biology knowledge",
"vendor_guid":"1",
"workflow_state":"active",
"rubric_criterion":{
"description":"Molecular biology knowledge",
"mastery_points":2,
"points_possible":3,
"ratings":[
{
"description":"The student shows fluency.",
"points":3
},
{
"description":"The student shows proficiency.",
"points":2
},
{
"description":"The student understands the fundamentals.",
"points":1
},
{
"description":"The student does not meet the requirements.",
"points":0
}
]
}
}
}
```

Defines the variable value used by the calculation\_method. Included only if calculation\_method uses it.

The method used to calculate student score.

The ID of the context the learning\_outcome is used in.

The type of context the learning\_outcome is used in.

Description of the outcome.

Optional friendly name for reporting.

The local Canvas ID of the learning outcome.

Also the title of the outcome.

The title of the learning outcome or learning outcome group.

A custom GUID for the learning standard.

Workflow status of the learning outcome (e.g. active, deleted).

{"description" =&gt; "Also the title of the outcome.", "mastery\_points" =&gt; "The number of points necessary for a rating to be considered mastery.", "points\_possible" =&gt; "The maximum level of points of any rating.", "ratings" =&gt; "Array of objects with (points, description) describing each of the outcoming ratings."}

### learning\_outcome\_group\_created

**Definition:** The event is emitted anytime a new outcome group is created in the account by an end user or API request.

**Trigger:** Triggered when a new group of learning outcomes is created.

```
{
  "metadata": {
    "event_name": "learning_outcome_group_created",
    "event_time": "2019-11-01T18:42:34.373Z",
    "job_id": "1020020528469291",
    "job_tag": "OutcomeImport#run",
    "producer": "canvas",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs"
  },
  "body": {
    "context_id": "32054",
    "context_type": "Course",
    "description": "<h3>Outcome</h3>Hello outcome",
    "learning_outcome_group_id": "75033",
    "parent_outcome_group_id": "75032",
    "title": "Official Standards for K-12 Math Education",
    "vendor_guid": "123",
    "workflow_state": "active"
  }
}
```

The ID of the context the learning outcome is used in.

The type of context the learning outcome is used in, usually Course.

Description of the learnning outcome group.

**learning\_outcome\_group\_id**

The local Canvas ID of the learning outcome group.

The local Canvas ID of the group's parent outcome group.

Title of the learning outcome group.

A custom GUID for the learning standard.

Workflow status of the learning outcome group, defaults to active.

### learning\_outcome\_group\_updated

**Definition:** The event is emitted anytime an existing outcome group is updated by an end user or API request. Only changes to the fields included in the body of the event payload will emit the `updated` event.

**Trigger:** Triggered when a group of learning outcomes is modified.

```
{
  "metadata": {
    "event_name": "learning_outcome_group_updated",
    "event_time": "2019-11-01T13:49:07.504Z",
    "job_id": "1020020528469291",
    "job_tag": "OutcomeImport#run",
    "producer": "canvas",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs"
  },
  "body": {
    "context_id": "32054",
    "context_type": "Course",
    "description": "<h3>Outcome</h3>Hello outcome",
    "learning_outcome_group_id": "75033",
    "parent_outcome_group_id": "75032",
    "title": "Official Standards for K-12 Math Education",
    "updated_at": "2019-11-05T13:38:00.218Z",
    "vendor_guid": "123",
    "workflow_state": "active"
  }
}
```

The ID of the context the learning outcome is used in.

The type of context the learning outcome is used in, usually Course.

Description of the learnning outcome group.

**learning\_outcome\_group\_id**

The local Canvas ID of the learning outcome group.

The local Canvas ID of the group's parent outcome group.

Title of the learning outcome group.

The time at which this group was last modified in any way.

A custom GUID for the learning standard.

Workflow status of the learning outcome group, defaults to active.

### learning\_outcome\_link\_created

**Definition:** The event is emitted anytime an outcome is linked to a context by an end user or API request. Only changes to the fields included in the body of the event payload will emit the `updated` event.

**Trigger:** Triggered when an outcome is linked inside of a context.

```
{
  "metadata": {
    "client_ip": "93.184.216.34",
    "context_account_id": "21070000000000079",
    "context_id": "21070000000000565",
    "context_role": "TeacherEnrollment",
    "context_sis_source_id": "2017.100.101.101-1",
    "context_type": "Course",
    "event_name": "learning_outcome_link_created",
    "event_time": "2019-11-01T19:12:01.333Z",
    "hostname": "oxana.instructure.com",
    "http_method": "POST",
    "producer": "canvas",
    "referrer": "https://oxana.instructure.com/courses/565/outcomes",
    "request_id": "1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
    "session_id": "ef686f8ed684abf78cbfa1f6a58112b5",
    "time_zone": "America/Sao_Paulo",
    "url": "https://oxana.instructure.com/api/v1/courses/565/outcome_groups/123456/outcomes",
    "user_account_id": "21070000000000001",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "user_id": "21070000000000001",
    "user_login": "oxana@example.com",
    "user_sis_id": "456-T45"
  },
  "body": {
    "context_id": "565",
    "context_type": "Course",
    "learning_outcome_group_id": "123456",
    "learning_outcome_id": "1201234",
    "learning_outcome_link_id": "12345678",
    "workflow_state": "active"
  }
}
```

The Canvas ID of the context the learning outcome is used in.

The type of context the learning outcome is used in, usually Course.

**learning\_outcome\_group\_id**

The local Canvas id of the related learning outcome group.

The local Canvas id of the related learning outcome.

The local Canvas id of the new learning outcome link.

The workflow status of the learning outcome link, by default active.

### learning\_outcome\_link\_updated

**Definition:** The event is emitted anytime an outcome context link is changed by an end user or API request.

**Trigger:** Triggered when an outcome link is changed inside of a context.

```
{
  "metadata": {
    "client_ip": "93.184.216.34",
    "context_account_id": "21070000000000079",
    "context_id": "21070000000000565",
    "context_role": "TeacherEnrollment",
    "context_sis_source_id": "2017.100.101.101-1",
    "context_type": "Course",
    "event_name": "learning_outcome_link_updated",
    "event_time": "2019-11-01T19:12:12.060Z",
    "hostname": "oxana.instructure.com",
    "http_method": "POST",
    "producer": "canvas",
    "referrer": "https://oxana.instructure.com/courses/565/outcomes",
    "request_id": "1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
    "session_id": "ef686f8ed684abf78cbfa1f6a58112b5",
    "time_zone": "America/Sao_Paulo",
    "url": "https://oxana.instructure.com/api/v1/courses/565/outcome_groups/1001/outcomes",
    "user_account_id": "21070000000000001",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "user_id": "21070000000000001",
    "user_login": "oxana@example.com",
    "user_sis_id": "456-T45"
  },
  "body": {
    "context_id": "565",
    "context_type": "Course",
    "learning_outcome_group_id": "1001",
    "learning_outcome_id": "1234",
    "learning_outcome_link_id": "12345",
    "updated_at": "2019-11-01T19:12:12.060Z",
    "workflow_state": "active"
  }
}
```

The Canvas ID of the context the learning outcome is used in.

The type of context the learning outcome is used in, usually Course.

**learning\_outcome\_group\_id**

The local Canvas id of the related learning outcome group.

The local Canvas id of the related learning outcome.

The local Canvas id of the learning outcome link that was updated.

The time that the learning outcome link was last modified.

The workflow status of the learning outcome link (e.g. active, deleted)

### learning\_outcome\_result\_created

**Definition:** The event is emitted anytime a submission is assessed against an outcome. The following setup should be enabled in Canvas in order for the event to be triggered:

1. Administrator has set up learning outcomes at the account/sub-account level
2. Instructor has added outcome to assignment rubric
3. Student submitted a rubric based assignment
4. Instructor graded a rubric based assignment at the outcome level =&gt; there is a result associated with assignment outcome

**Trigger:** Triggered when a submission is rated against an outcome.

```
{
  "metadata": {
    "event_name": "learning_outcome_result_created",
    "event_time": "2019-08-09T21:35:05Z",
    "job_id": "1020020528469291",
    "job_tag": "Quizzes::SubmissionGrader#update_outcomes",
    "producer": "canvas",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs"
  },
  "body": {
    "id": "1",
    "assessed_at": "2019-08-09T21:35:05Z",
    "attempt": 1,
    "created_at": "2019-08-09T21:35:05Z",
    "learning_outcome_id": "1",
    "learning_outcome_context_uuid": "9dewFPr6uKGaiVxchQSsqV6YZy5HBtlq8O2vqp45",
    "result_context_id": "1",
    "result_context_type": "Course",
    "result_context_uuid": "c3JwFPr6uKGaiVxchQSsqV6YZy5HBtlq8O2vqNNN",
    "mastery": true,
    "original_mastery": false,
    "original_possible": 5,
    "original_score": 5,
    "percent": 1,
    "possible": 5,
    "score": 5,
    "user_uuid": "elXwFPr6uKGaiVxchQSsqV6YZy5HBtlq8O2vqMXM",
    "artifact_id": "22",
    "artifact_type": "RubricAssessment",
    "artifact_updated_at": "2019-08-09T21:33:05Z",
    "artifact_created_at": "2019-08-09T21:33:05Z",
    "associated_asset_id": "56",
    "associated_asset_type": "Assignment"
  }
}
```

The local Canvas ID of the learning outcome result.

The date when the outcome was last assessed.

The submission attempt number.

Time when the result was created.

The local Canvas ID of the learning outcome.

**learning\_outcome\_context\_uuid**

The uuid of the context associated with the learning outcome.

The local Canvas ID of the context associated with the learning outcome result.

The type of the context associated with the learning outcome result. Value will be one of the following: Account or Course.

The uuid of the context associated with the learning outcome result.

True if student achieved mastery.

True if student achieved mastery on the first attempt.

Possible points on the first attempt.

Score on the first attempt.

Percent of maximum points possible for an outcome, scaled to reflect any custom mastery levels that differ from the learning outcome.

Total number of points possible.

The unique identifier for the user that the outcome was assessed.

The id of the artifact that contains the outcome assessment. Value will be an string representation of an integer or nil.

The type of artifact that contains the outcome assessment. Value will be one of the following: RubricAssessment, Submission, Quizzes::QuizSubmission, LiveAssessments::Submission or nil.

The date when the artifact was last updated or nil.

The date when the artifact was created or nil.

The id of the asset that the outcome is aligned to. Value will be an string representation of an integer or nil.

The type of the asset that the outcome is aligned to. Value will be one of the following: AssessmentQuestion, Assignment, Quizzes::Quiz, LiveAssessments::Assessment or nil.

### learning\_outcome\_result\_updated

**Definition:** The event is emitted anytime a existing outcome rating for a submission is updated. Only changes to the fields included in the body of the event payload will emit the `updated` event.

**Trigger:** Triggered when a submission outcome rating is updated.

```
{
  "metadata": {
    "event_name": "learning_outcome_result_updated",
    "event_time": "2019-08-09T21:35:05Z",
    "job_id": "1020020528469291",
    "job_tag": "RubricAssessment#update_outcomes_for_assessment",
    "producer": "canvas",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs"
  },
  "body": {
    "id": "1",
    "assessed_at": "2019-08-09T21:35:05Z",
    "attempt": 1,
    "created_at": "2019-08-09T21:35:05Z",
    "learning_outcome_id": "1",
    "learning_outcome_context_uuid": "9dewFPr6uKGaiVxchQSsqV6YZy5HBtlq8O2vqp45",
    "result_context_id": "1",
    "result_context_type": "Course",
    "result_context_uuid": "c3JwFPr6uKGaiVxchQSsqV6YZy5HBtlq8O2vqNNN",
    "mastery": true,
    "original_mastery": false,
    "original_possible": 5,
    "original_score": 5,
    "percent": 1,
    "possible": 5,
    "score": 5,
    "updated_at": "2019-11-01T00:21:24Z",
    "user_uuid": "elXwFPr6uKGaiVxchQSsqV6YZy5HBtlq8O2vqMXM",
    "artifact_id": "22",
    "artifact_type": "RubricAssessment",
    "artifact_updated_at": "2019-08-09T21:33:05Z",
    "artifact_created_at": "2019-08-09T21:33:05Z",
    "associated_asset_id": "56",
    "associated_asset_type": "Assignment"
  }
}
```

The local Canvas ID of the learning outcome result.

The date when the outcome was last assessed.

The submission attempt number.

Time when the result was created.

The local Canvas ID of the learning outcome.

**learning\_outcome\_context\_uuid**

The uuid of the context associated with the learning outcome.

The local Canvas ID of the context associated with the learning outcome result.

The type of the context associated with the learning outcome result. Value will be one of the following: Account or Course.

The uuid of the context associated with the learning outcome result.

True if student achieved mastery.

True if student achieved mastery on the first attempt.

Possible points on the first attempt.

Score on the first attempt.

Percent of maximum points possible for an outcome, scaled to reflect any custom mastery levels that differ from the learning outcome.

Total number of points possible.

Time the learning outcome result was updated at.

The uuid of the user that the outcome was assessed.

The id of the artifact that contains the outcome assessment. Value will be an string representation of an integer or nil.

The type of artifact that contains the outcome assessment. Value will be one of the following: RubricAssessment, Submission, Quizzes::QuizSubmission, LiveAssessments::Submission or nil.

The date when the artifact was last updated or nil.

The date when the artifact was created or nil.

The id of the asset that the outcome is aligned to. Value will be an string representation of an integer or nil.

The type of the asset that the outcome is aligned to. Value will be one of the following: AssessmentQuestion, Assignment, Quizzes::Quiz, LiveAssessments::Assessment or nil.

**Definition:** The event is emitted anytime an outcome is updated by an end user or API request. Only changes to the fields included in the body of the event payload will emit the `updated` event.

**Trigger:** Triggered when an outcome is updated.

```
{
  "metadata": {
    "client_ip": "93.184.216.34",
    "event_name": "learning_outcome_updated",
    "event_time": "2019-11-01T21:42:55.950Z",
    "hostname": "oxana.instructure.com",
    "http_method": "PUT",
    "producer": "canvas",
    "referrer": "https://oxana.instructure.com/courses/1234/outcomes",
    "request_id": "1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
    "session_id": "ef686f8ed684abf78cbfa1f6a58112b5",
    "time_zone": "America/Denver",
    "url": "https://oxana.instructure.com/api/v1/outcomes/12345",
    "user_account_id": "21070000000000001",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "user_id": "21070000000000001",
    "user_login": "oxana@example.com",
    "user_sis_id": "456-T45"
  },
  "body": {
    "calculation_int": 65,
    "calculation_method": "highest",
    "context_id": "1234",
    "context_type": "Course",
    "description": "Develop understanding of molecular and cell biology.",
    "display_name": "Learn molecular biology",
    "learning_outcome_id": "12345",
    "short_description": "Molecular biology knowledge",
    "title": "Molecular biology knowledge",
    "updated_at": "2019-11-01T21:42:55Z",
    "vendor_guid": "1",
    "workflow_state": "active",
    "rubric_criterion": {
      "description": "Molecular biology knowledge",
      "mastery_points": 3,
      "points_possible": 5,
      "ratings": [
        {
          "description": "Exceeds Expectations",
          "points": 5
        },
        {
          "description": "Proficient",
          "points": 4
        },
        {
          "description": "Meets Expectations",
          "points": 3
        },
        {
          "description": "Nearing Expectations",
          "points": 2
        },
        {
          "description": "Developing",
          "points": 1
        },
        {
          "description": "Does Not Meet Expectations",
          "points": 0
        }
      ]
    }
  }
}
```

Defines the variable value used by the calculation\_method. Included only if calculation\_method uses it.

The method used to calculate student score.

The ID of the context the learning\_outcome is used in.

The type of context the learning\_outcome is used in.

Description of the outcome.

Optional friendly name for reporting.

The local Canvas ID of the learning outcome.

Also the title of the outcome.

The title of the learning outcome or learning outcome group.

The time at which this outcome was last modified in any way.

A custom GUID for the learning standard.

Workflow status of the learning outcome. Defaults to active

{"description" =&gt; "Also the title of the outcome.", "mastery\_points" =&gt; "The number of points necessary for a rating to be considered mastery.", "points\_possible" =&gt; "The maximum level of points of any rating.", "ratings" =&gt; "Array of objects with (points, description) describing each of the outcoming ratings."}

### outcome\_proficiency\_created

**Definition:** The event is emitted anytime a new outcome\_proficiency (mastery scale) is created by an end user or API request.

**Trigger:** Triggered when a new outcome\_proficiency is saved.

```
{
  "metadata": {
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "7db438071375c02373713c12c73869ff2f470b68.oxana.instructure.com",
    "user_login": "oxana@instructure.com",
    "user_account_id": "21070000000000001",
    "user_sis_id": "456-T45",
    "user_id": "21070000000000001",
    "time_zone": "America/Denver",
    "context_type": "Account",
    "context_id": "21070000000000144",
    "context_sis_source_id": "2017.100.101.101-1",
    "context_account_id": "21070000000000079",
    "request_id": "1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
    "session_id": "ef686f8ed684abf78cbfa1f6a58112b5",
    "hostname": "oxana.instructure.com",
    "http_method": "POST",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "client_ip": "93.184.216.34",
    "url": "https://oxana.instructure.com/accounts/1/outcome_proficiency",
    "referrer": null,
    "producer": "canvas",
    "event_name": "outcome_proficiency_created",
    "event_time": "2020-08-18T23:28:24.396Z"
  },
  "body": {
    "outcome_proficiency_id": "1",
    "context_type": "Account",
    "context_id": "1",
    "workflow_state": "active",
    "outcome_proficiency_ratings": [
      {
        "outcome_proficiency_rating_id": "1",
        "description": "Exceeds Mastery",
        "points": 4.0,
        "mastery": false,
        "color": "02672D",
        "workflow_state": "active"
      },
      {
        "outcome_proficiency_rating_id": "2",
        "description": "Mastery",
        "points": 3.0,
        "mastery": true,
        "color": "03893D",
        "workflow_state": "active"
      },
      {
        "outcome_proficiency_rating_id": "3",
        "description": "Near Mastery",
        "points": 2.0,
        "mastery": false,
        "color": "FAB901",
        "workflow_state": "active"
      },
      {
        "outcome_proficiency_rating_id": "4",
        "description": "Below Mastery",
        "points": 1.0,
        "mastery": false,
        "color": "FD5D10",
        "workflow_state": "active"
      },
      {
        "outcome_proficiency_rating_id": "5",
        "description": "Well Below Mastery",
        "points": 0.0,
        "mastery": false,
        "color": "E62429",
        "workflow_state": "active"
      }
    ]
  }
}
```

The Canvas id of the outcome proficiency.

The type of context the outcome proficiency is used in.

The id of the context the outcome proficiency is used in.

Workflow state of the outcome proficiency. E.g active, deleted.

**outcome\_proficiency\_ratings**

An array of the associated ratings with this proficiency. Description, points, mastery, color, workflow\_state, and outcome\_proficiency\_rating\_id are required keys.

### outcome\_proficiency\_updated

**Definition:** The event is emitted anytime an outcome\_proficiency (mastery scale) is updated or its associated ratings are updated by an end user or API request.

**Trigger:** Triggered when an outcome\_proficiency is saved.

```
{
"metadata":{
"root_account_uuid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
"root_account_id":"21070000000000001",
"root_account_lti_guid":"7db438071375c02373713c12c73869ff2f470b68.oxana.instructure.com",
"user_login":"oxana@instructure.com",
"user_account_id":"21070000000000001",
"user_sis_id":"456-T45",
"user_id":"21070000000000001",
"time_zone":"America/Denver",
"context_type":"Account",
"context_id":"21070000000000144",
"context_sis_source_id":"2017.100.101.101-1",
"context_account_id":"21070000000000079",
"request_id":"1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
"session_id":"ef686f8ed684abf78cbfa1f6a58112b5",
"hostname":"oxana.instructure.com",
"http_method":"POST",
"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"client_ip":"93.184.216.34",
"url":"https://oxana.instructure.com/accounts/1/outcome_proficiency",
"referrer":null,
"producer":"canvas",
"event_name":"outcome_proficiency_updated",
"event_time":"2020-08-18T23:28:24.396Z"
},
"body":{
"outcome_proficiency_id":"1",
"context_type":"Account",
"context_id":"1",
"workflow_state":"active",
"updated_at":"2020-08-18T17:24:46-06:00",
"outcome_proficiency_ratings":[
{
"outcome_proficiency_rating_id":"1",
"description":"Exceeds Mastery",
"points":4.0,
"mastery":false,
"color":"02672D",
"workflow_state":"active"
},
{
"outcome_proficiency_rating_id":"2",
"description":"Mastery",
"points":3.0,
"mastery":true,
"color":"03893D",
"workflow_state":"active"
},
{
"outcome_proficiency_rating_id":"3",
"description":"Near Mastery",
"points":2.0,
"mastery":false,
"color":"FAB901",
"workflow_state":"active"
},
{
"outcome_proficiency_rating_id":"4",
"description":"Below Mastery",
"points":1.0,
"mastery":false,
"color":"FD5D10",
"workflow_state":"active"
},
{
"outcome_proficiency_rating_id":"5",
"description":"Well Below Mastery",
"points":0.0,
"mastery":false,
"color":"E62429",
"workflow_state":"active"
}
]
}
}
```

The Canvas id of the outcome proficiency.

The type of context the outcome proficiency is used in.

The id of the context the outcome proficiency is used in.

Workflow state of the outcome proficiency. E.g active, deleted.

The time at which this proficiency was last modified in any way.

**outcome\_proficiency\_ratings**

An array of the associated ratings with this proficiency. Description, points, mastery, color, workflow\_state, and outcome\_proficiency\_rating\_id are required keys.

Note: Timestamps will be in ISO8601 format, including an offset. Be sure to take that into account when parsing, since it’s unspecified which offset timestamps will use, and the offset may even change between different timestamps within a single event.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).