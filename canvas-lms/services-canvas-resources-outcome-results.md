---
title: Outcome Results | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/outcome_results
source: sitemap
fetched_at: 2026-02-15T08:56:26.700119-03:00
rendered_js: false
word_count: 662
summary: This document provides the API specification for retrieving learning outcome results, rollups, and contributing scores for students within a course.
tags:
    - learning-outcomes
    - canvas-lms-api
    - student-assessment
    - outcome-rollups
    - api-reference
category: api
---

API for accessing learning outcome results

**An OutcomeResult object looks like:**

```
// A student's result for an outcome
{
  // A unique identifier for this result
"id": 42,
  // The student's score
"score": 6,
  // The datetime the resulting OutcomeResult was submitted at, or absent that,
  // when it was assessed.
"submitted_or_assessed_at": "2013-02-01T00:00:00-06:00",
  // Unique identifiers of objects associated with this result
"links": {"user":"3","learning_outcome":"97","alignment":"53"},
  // score's percent of maximum points possible for outcome, scaled to reflect any
  // custom mastery levels that differ from the learning outcome
"percent": 0.65
}
```

**An OutcomeRollupScoreLinks object looks like:**

```
{
  // The id of the related outcome
  "outcome": 42
}
```

**An OutcomeRollupScore object looks like:**

```
{
  // The rollup score for the outcome, based on the student alignment scores
  // related to the outcome. This could be null if the student has no related
  // scores.
  "score": 3,
  // The number of alignment scores included in this rollup.
  "count": 6,
  "links": {"outcome":"42"}
}
```

**An OutcomeRollupLinks object looks like:**

```
{
  // If an aggregate result was requested, the course field will be present.
  // Otherwise, the user and section field will be present (Optional) The id of
  // the course that this rollup applies to
  "course": 42,
  // (Optional) The id of the user that this rollup applies to
  "user": 42,
  // (Optional) The id of the section the user is in
  "section": 57
}
```

**An OutcomeRollup object looks like:**

```
{
  // an array of OutcomeRollupScore objects
  "scores": null,
  // The name of the resource for this rollup. For example, the user name.
  "name": "John Doe",
  "links": {"course":42,"user":42,"section":57}
}
```

**An OutcomeAlignment object looks like:**

```
// An asset aligned with this outcome
{
  // A unique identifier for this alignment
  "id": "quiz_3",
  // The name of this alignment
  "name": "Big mid-term test",
  // (Optional) A URL for details about this alignment
  "html_url": null
}
```

**An OutcomePath object looks like:**

```
// The full path to an outcome
{
  // A unique identifier for this outcome
  "id": 42,
  // an array of OutcomePathPart objects
  "parts": null
}
```

**An OutcomePathPart object looks like:**

```
// An outcome or outcome group
{
  // The title of the outcome or outcome group
  "name": "Spelling out numbers"
}
```

[OutcomeResultsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_results_controller.rb)

`GET /api/v1/courses/:course_id/outcome_results`

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_results`

Gets the outcome results for users and outcomes in the specified context.

used in sLMGB

**Request Parameters:**

If specified, only the users whose ids are given will be included in the results. SIS ids can be used, prefixed by “sis\_user\_id:”. It is an error to specify an id for a user who is not a student in the context.

If specified, only the outcomes whose ids are given will be included in the results. it is an error to specify an id for an outcome which is not linked to the context.

If true, results that are hidden from the learning mastery gradebook and student rollup scores will be included

**Example Response:**

```
{
  outcome_results: [OutcomeResult]
}
```

[OutcomeResultsController#outcome\_orderarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_results_controller.rb)

`POST /api/v1/courses/:course_id/assign_outcome_order`

**Scope:** `url:POST|/api/v1/courses/:course_id/assign_outcome_order`

Saves the ordering of outcomes in LMGB for a user

[OutcomeResultsController#rollupsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_results_controller.rb)

`GET /api/v1/courses/:course_id/outcome_rollups`

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_rollups`

Gets the outcome rollups for the users and outcomes in the specified context.

**Request Parameters:**

If specified, instead of returning one rollup for each user, all the user rollups will be combined into one rollup for the course that will contain the average (or median, see below) rollup score for each outcome.

Allowed values: `course`

If aggregate rollups requested, then this value determines what statistic is used for the aggregate. Defaults to “mean” if this value is not specified.

Allowed values: `mean`, `median`

If specified, only the users whose ids are given will be included in the results or used in an aggregate result. it is an error to specify an id for a user who is not a student in the context

If specified, only the outcomes whose ids are given will be included in the results. it is an error to specify an id for an outcome which is not linked to the context.

Specify additional values to exclude. “missing\_user\_rollups” excludes rollups for users without results. “missing\_outcome\_results” excludes outcomes without results.

Allowed values: `missing_user_rollups`, `missing_outcome_results`, \`\`

If specified, sorts outcome result rollups. “student” sorting will sort by a user’s sortable name. “outcome” sorting will sort by the given outcome’s rollup score. The latter requires specifying the “sort\_outcome\_id” parameter. By default, the sort order is ascending.

Allowed values: `student`, `outcome`

If outcome sorting requested, then this determines which outcome to use for rollup score sorting.

If sorting requested, then this allows changing the default sort order of ascending to descending.

Allowed values: `asc`, `desc`

If defaults are requested, then color and mastery level defaults will be added to outcome ratings in the rollup. This will only take effect if the Account Level Mastery Scales FF is DISABLED

**DEPRECATED**: This parameter is deprecated. Use the separate GET /api/v1/courses/:course\_id/outcomes/:outcome\_id/contributing\_scores endpoint instead to fetch contributing scores for a specific outcome. If contributing scores are requested, then each individual outcome score will also include all graded artifacts that contributed to the outcome score

**Example Response:**

```
{
  "rollups": [OutcomeRollup],
  "linked": {
    // (Optional) Included if include[] has outcomes
    "outcomes": [Outcome],
    // (Optional) Included if aggregate is not set and include[] has users
    "users": [User],
    // (Optional) Included if aggregate is 'course' and include[] has courses
    "courses": [Course]
    // (Optional) Included if include[] has outcome_groups
    "outcome_groups": [OutcomeGroup],
    // (Optional) Included if include[] has outcome_links
    "outcome_links": [OutcomeLink]
    // (Optional) Included if include[] has outcome_paths
    "outcome_paths": [OutcomePath]
    // (Optional) Included if include[] has outcomes.alignments
    "outcomes.alignments": [OutcomeAlignment]
  }
}
```

[OutcomeResultsController#contributing\_scoresarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_results_controller.rb)

`GET /api/v1/courses/:course_id/outcomes/:outcome_id/contributing_scores`

**Scope:** `url:GET|/api/v1/courses/:course_id/outcomes/:outcome_id/contributing_scores`

Gets the contributing scores for a specific outcome and set of users. Contributing scores are the individual assignment/quiz scores that contributed to the outcome score for each user.

Returns all alignments for the outcome in the course context.

**Request Parameters:**

If specified, only the users whose ids are given will be included in the results. It is an error to specify an id for a user who is not a student in the context.

`only_assignment_alignments`

If specified, only assignment alignments will be included in the results.

`show_unpublished_assignments`

If true, unpublished assignments will be included in the results. Defaults to false.

**Example Response:**

```
{
  "outcome": {
    "id": "1",
    "title": "Outcome 1"
  },
  "alignments": [
    {
      "alignment_id": "123",
      "associated_asset_id": "456",
      "associated_asset_name": "Assignment 1",
      "associated_asset_type": "Assignment"
    }
  ],
  "scores": [
    {
      "user_id": "1",
      "alignment_id": "123",
      "score": 3.5
    }
  ]
}
```

[OutcomeResultsController#enqueue\_outcome\_rollup\_calculationarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_results_controller.rb)

`POST /api/v1/enqueue_outcome_rollup_calculation`

**Scope:** `url:POST|/api/v1/enqueue_outcome_rollup_calculation`

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).