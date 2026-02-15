---
title: Outcome Groups | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/outcome_groups
source: sitemap
fetched_at: 2026-02-15T09:09:40.60891-03:00
rendered_js: false
word_count: 1226
summary: This document defines the API endpoints and object schemas for managing learning outcome groups and links within global, account, and course contexts.
tags:
    - canvas-lms
    - learning-outcomes
    - outcome-groups
    - outcome-links
    - rest-api
    - educational-data
category: api
---

API for accessing learning outcome group information.

Learning outcome groups organize outcomes within a context (or in the global "context" for global outcomes). Every outcome is created in a particular context (that context then becomes its "owning context") but may be linked multiple times in one or more related contexts. This allows different accounts or courses to organize commonly defined outcomes in ways appropriate to their pedagogy, including having the same outcome discoverable at different locations in the organizational hierarchy.

While an outcome can be linked into a context (such as a course) multiple times, it may only be linked into a particular group once.

**An OutcomeGroup object looks like:**

```
{
  // the ID of the outcome group
"id": 1,
  // the URL for fetching/updating the outcome group. should be treated as opaque
"url": "/api/v1/accounts/1/outcome_groups/1",
  // an abbreviated OutcomeGroup object representing the parent group of this
  // outcome group, if any. omitted in the abbreviated form.
"parent_outcome_group": null,
  // the context owning the outcome group. may be null for global outcome groups.
  // omitted in the abbreviated form.
"context_id": 1,
"context_type": "Account",
  // title of the outcome group
"title": "Outcome group title",
  // description of the outcome group. omitted in the abbreviated form.
"description": "Outcome group description",
  // A custom GUID for the learning standard.
"vendor_guid": "customid9000",
  // the URL for listing/creating subgroups under the outcome group. should be
  // treated as opaque
"subgroups_url": "/api/v1/accounts/1/outcome_groups/1/subgroups",
  // the URL for listing/creating outcome links under the outcome group. should be
  // treated as opaque
"outcomes_url": "/api/v1/accounts/1/outcome_groups/1/outcomes",
  // the URL for importing another group into this outcome group. should be
  // treated as opaque. omitted in the abbreviated form.
"import_url": "/api/v1/accounts/1/outcome_groups/1/import",
  // whether the current user can update the outcome group
"can_edit": true
}
```

**An OutcomeLink object looks like:**

```
{
  // the URL for fetching/updating the outcome link. should be treated as opaque
  "url": "/api/v1/accounts/1/outcome_groups/1/outcomes/1",
  // the context owning the outcome link. will match the context owning the
  // outcome group containing the outcome link; included for convenience. may be
  // null for links in global outcome groups.
  "context_id": 1,
  "context_type": "Account",
  // an abbreviated OutcomeGroup object representing the group containing the
  // outcome link.
  "outcome_group": null,
  // an abbreviated Outcome object representing the outcome linked into the
  // containing outcome group.
  "outcome": null,
  // whether this outcome has been used to assess a student in the context of this
  // outcome link.  In other words, this will be set to true if the context is a
  // course, and a student has been assessed with this outcome in that course.
  "assessed": true,
  // whether this outcome link is manageable and is not the last link to an
  // aligned outcome
  "can_unlink": null
}
```

[OutcomeGroupsApiController#redirectarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

`GET /api/v1/global/root_outcome_group`

**Scope:** `url:GET|/api/v1/global/root_outcome_group`

`GET /api/v1/accounts/:account_id/root_outcome_group`

**Scope:** `url:GET|/api/v1/accounts/:account_id/root_outcome_group`

`GET /api/v1/courses/:course_id/root_outcome_group`

**Scope:** `url:GET|/api/v1/courses/:course_id/root_outcome_group`

Convenience redirect to find the root outcome group for a particular context. Will redirect to the appropriate outcome group’s URL.

[OutcomeGroupsApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

`GET /api/v1/accounts/:account_id/outcome_groups`

**Scope:** `url:GET|/api/v1/accounts/:account_id/outcome_groups`

`GET /api/v1/courses/:course_id/outcome_groups`

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_groups`

Returns a list of all outcome groups in the specified context.

Returns a list of [OutcomeGroup](https://developerdocs.instructure.com/services/canvas/resources/outcome_groups#outcomegroup) objects.

[OutcomeGroupsApiController#link\_indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

`GET /api/v1/accounts/:account_id/outcome_group_links`

**Scope:** `url:GET|/api/v1/accounts/:account_id/outcome_group_links`

`GET /api/v1/courses/:course_id/outcome_group_links`

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_group_links`

Returns a list of all outcome links in the specified context.

**Request Parameters:**

The detail level of the outcomes. Defaults to “abbrev”. Specify “full” for more information.

The detail level of the outcome groups. Defaults to “abbrev”. Specify “full” for more information.

Returns a list of [OutcomeLink](https://developerdocs.instructure.com/services/canvas/resources/outcome_groups#outcomelink) objects.

[OutcomeGroupsApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

`GET /api/v1/global/outcome_groups/:id`

**Scope:** `url:GET|/api/v1/global/outcome_groups/:id`

`GET /api/v1/accounts/:account_id/outcome_groups/:id`

**Scope:** `url:GET|/api/v1/accounts/:account_id/outcome_groups/:id`

`GET /api/v1/courses/:course_id/outcome_groups/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_groups/:id`

Returns detailed information about a specific outcome group.

Returns an [OutcomeGroup](https://developerdocs.instructure.com/services/canvas/resources/outcome_groups#outcomegroup) object.

[OutcomeGroupsApiController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

`PUT /api/v1/global/outcome_groups/:id`

**Scope:** `url:PUT|/api/v1/global/outcome_groups/:id`

`PUT /api/v1/accounts/:account_id/outcome_groups/:id`

**Scope:** `url:PUT|/api/v1/accounts/:account_id/outcome_groups/:id`

`PUT /api/v1/courses/:course_id/outcome_groups/:id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/outcome_groups/:id`

Modify an existing outcome group. Fields not provided are left as is; unrecognized fields are ignored.

When changing the parent outcome group, the new parent group must belong to the same context as this outcome group, and must not be a descendant of this outcome group (i.e. no cycles allowed).

**Request Parameters:**

The new outcome group title.

The new outcome group description.

A custom GUID for the learning standard.

The id of the new parent outcome group.

**Example Request:**

```
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/2.json' \
     -X PUT \
     -F 'title=Outcome Group Title' \
     -F 'description=Outcome group description' \
     -F 'vendor_guid=customid9000' \
     -F 'parent_outcome_group_id=1' \
     -H "Authorization: Bearer <token>"
```

```
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/2.json' \
     -X PUT \
     --data-binary '{
           "title": "Outcome Group Title",
           "description": "Outcome group description",
           "vendor_guid": "customid9000",
           "parent_outcome_group_id": 1
         }' \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <token>"
```

Returns an [OutcomeGroup](https://developerdocs.instructure.com/services/canvas/resources/outcome_groups#outcomegroup) object.

[OutcomeGroupsApiController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

`DELETE /api/v1/global/outcome_groups/:id`

**Scope:** `url:DELETE|/api/v1/global/outcome_groups/:id`

`DELETE /api/v1/accounts/:account_id/outcome_groups/:id`

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/outcome_groups/:id`

`DELETE /api/v1/courses/:course_id/outcome_groups/:id`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/outcome_groups/:id`

Deleting an outcome group deletes descendant outcome groups and outcome links. The linked outcomes themselves are only deleted if all links to the outcome were deleted.

Aligned outcomes cannot be deleted; as such, if all remaining links to an aligned outcome are included in this group’s descendants, the group deletion will fail.

**Example Request:**

```
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/2.json' \
     -X DELETE \
     -H "Authorization: Bearer <token>"
```

Returns an [OutcomeGroup](https://developerdocs.instructure.com/services/canvas/resources/outcome_groups#outcomegroup) object.

[OutcomeGroupsApiController#outcomesarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

`GET /api/v1/global/outcome_groups/:id/outcomes`

**Scope:** `url:GET|/api/v1/global/outcome_groups/:id/outcomes`

`GET /api/v1/accounts/:account_id/outcome_groups/:id/outcomes`

**Scope:** `url:GET|/api/v1/accounts/:account_id/outcome_groups/:id/outcomes`

`GET /api/v1/courses/:course_id/outcome_groups/:id/outcomes`

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_groups/:id/outcomes`

A paginated list of the immediate OutcomeLink children of the outcome group.

**Request Parameters:**

The detail level of the outcomes. Defaults to “abbrev”. Specify “full” for more information.

Returns a list of [OutcomeLink](https://developerdocs.instructure.com/services/canvas/resources/outcome_groups#outcomelink) objects.

[OutcomeGroupsApiController#linkarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

`POST /api/v1/global/outcome_groups/:id/outcomes`

**Scope:** `url:POST|/api/v1/global/outcome_groups/:id/outcomes`

`PUT /api/v1/global/outcome_groups/:id/outcomes/:outcome_id`

**Scope:** `url:PUT|/api/v1/global/outcome_groups/:id/outcomes/:outcome_id`

`POST /api/v1/accounts/:account_id/outcome_groups/:id/outcomes`

**Scope:** `url:POST|/api/v1/accounts/:account_id/outcome_groups/:id/outcomes`

`PUT /api/v1/accounts/:account_id/outcome_groups/:id/outcomes/:outcome_id`

**Scope:** `url:PUT|/api/v1/accounts/:account_id/outcome_groups/:id/outcomes/:outcome_id`

`POST /api/v1/courses/:course_id/outcome_groups/:id/outcomes`

**Scope:** `url:POST|/api/v1/courses/:course_id/outcome_groups/:id/outcomes`

`PUT /api/v1/courses/:course_id/outcome_groups/:id/outcomes/:outcome_id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/outcome_groups/:id/outcomes/:outcome_id`

Link an outcome into the outcome group. The outcome to link can either be specified by a PUT to the link URL for a specific outcome (the outcome\_id in the PUT URLs) or by supplying the information for a new outcome (title, description, ratings, mastery\_points) in a POST to the collection.

If linking an existing outcome, the outcome\_id must identify an outcome available to this context; i.e. an outcome owned by this group’s context, an outcome owned by an associated account, or a global outcome. With outcome\_id present, any other parameters (except move\_from) are ignored.

If defining a new outcome, the outcome is created in the outcome group’s context using the provided title, description, ratings, and mastery points; the title is required but all other fields are optional. The new outcome is then linked into the outcome group.

If ratings are provided when creating a new outcome, an embedded rubric criterion is included in the new outcome. This criterion’s mastery\_points default to the maximum points in the highest rating if not specified in the mastery\_points parameter. Any ratings lacking a description are given a default of “No description”. Any ratings lacking a point value are given a default of 0. If no ratings are provided, the mastery\_points parameter is ignored.

**Request Parameters:**

The ID of the existing outcome to link.

The ID of the old outcome group. Only used if outcome\_id is present.

The title of the new outcome. Required if outcome\_id is absent.

A friendly name shown in reports for outcomes with cryptic titles, such as common core standards names.

The description of the new outcome.

A custom GUID for the learning standard.

The mastery threshold for the embedded rubric criterion.

The description of a rating level for the embedded rubric criterion.

The points corresponding to a rating level for the embedded rubric criterion.

The new calculation method. Defaults to “decaying\_average” if the Outcomes New Decaying Average Calculation Method FF is ENABLED then Defaults to “weighted\_average”

Allowed values: `weighted_average`, `decaying_average`, `n_mastery`, `latest`, `highest`, `average`

The new calculation int. Only applies if the calculation\_method is “weighted\_average”, “decaying\_average” or “n\_mastery”. Defaults to 65

**Example Request:**

```
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/outcomes/1.json' \
     -X PUT \
     -H "Authorization: Bearer <token>"
```

```
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/outcomes.json' \
     -X POST \
     -F 'title=Outcome Title' \
     -F 'display_name=Title for reporting' \
     -F 'description=Outcome description' \
     -F 'vendor_guid=customid9000' \
     -F 'mastery_points=3' \
     -F 'calculation_method=decaying_average' \
     -F 'calculation_int=65' \
     -F 'ratings[][description]=Exceeds Expectations' \
     -F 'ratings[][points]=5' \
     -F 'ratings[][description]=Meets Expectations' \
     -F 'ratings[][points]=3' \
     -F 'ratings[][description]=Does Not Meet Expectations' \
     -F 'ratings[][points]=0' \
     -H "Authorization: Bearer <token>"
```

```
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/outcomes.json' \
     -X POST \
     --data-binary '{
           "title": "Outcome Title",
           "display_name": "Title for reporting",
           "description": "Outcome description",
           "vendor_guid": "customid9000",
           "mastery_points": 3,
           "ratings": [
             { "description": "Exceeds Expectations", "points": 5 },
             { "description": "Meets Expectations", "points": 3 },
             { "description": "Does Not Meet Expectations", "points": 0 }
           ]
         }' \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <token>"
```

Returns an [OutcomeLink](https://developerdocs.instructure.com/services/canvas/resources/outcome_groups#outcomelink) object.

[OutcomeGroupsApiController#unlinkarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

`DELETE /api/v1/global/outcome_groups/:id/outcomes/:outcome_id`

**Scope:** `url:DELETE|/api/v1/global/outcome_groups/:id/outcomes/:outcome_id`

`DELETE /api/v1/accounts/:account_id/outcome_groups/:id/outcomes/:outcome_id`

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/outcome_groups/:id/outcomes/:outcome_id`

`DELETE /api/v1/courses/:course_id/outcome_groups/:id/outcomes/:outcome_id`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/outcome_groups/:id/outcomes/:outcome_id`

Unlinking an outcome only deletes the outcome itself if this was the last link to the outcome in any group in any context. Aligned outcomes cannot be deleted; as such, if this is the last link to an aligned outcome, the unlinking will fail.

**Example Request:**

```
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/outcomes/1.json' \
     -X DELETE \
     -H "Authorization: Bearer <token>"
```

Returns an [OutcomeLink](https://developerdocs.instructure.com/services/canvas/resources/outcome_groups#outcomelink) object.

[OutcomeGroupsApiController#subgroupsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

`GET /api/v1/global/outcome_groups/:id/subgroups`

**Scope:** `url:GET|/api/v1/global/outcome_groups/:id/subgroups`

`GET /api/v1/accounts/:account_id/outcome_groups/:id/subgroups`

**Scope:** `url:GET|/api/v1/accounts/:account_id/outcome_groups/:id/subgroups`

`GET /api/v1/courses/:course_id/outcome_groups/:id/subgroups`

**Scope:** `url:GET|/api/v1/courses/:course_id/outcome_groups/:id/subgroups`

A paginated list of the immediate OutcomeGroup children of the outcome group.

Returns a list of [OutcomeGroup](https://developerdocs.instructure.com/services/canvas/resources/outcome_groups#outcomegroup) objects.

[OutcomeGroupsApiController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

`POST /api/v1/global/outcome_groups/:id/subgroups`

**Scope:** `url:POST|/api/v1/global/outcome_groups/:id/subgroups`

`POST /api/v1/accounts/:account_id/outcome_groups/:id/subgroups`

**Scope:** `url:POST|/api/v1/accounts/:account_id/outcome_groups/:id/subgroups`

`POST /api/v1/courses/:course_id/outcome_groups/:id/subgroups`

**Scope:** `url:POST|/api/v1/courses/:course_id/outcome_groups/:id/subgroups`

Creates a new empty subgroup under the outcome group with the given title and description.

**Request Parameters:**

The title of the new outcome group.

The description of the new outcome group.

A custom GUID for the learning standard

**Example Request:**

```
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/subgroups.json' \
     -X POST \
     -F 'title=Outcome Group Title' \
     -F 'description=Outcome group description' \
     -F 'vendor_guid=customid9000' \
     -H "Authorization: Bearer <token>"
```

```
curl 'https://<canvas>/api/v1/accounts/1/outcome_groups/1/subgroups.json' \
     -X POST \
     --data-binary '{
           "title": "Outcome Group Title",
           "description": "Outcome group description",
           "vendor_guid": "customid9000"
         }' \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <token>"
```

Returns an [OutcomeGroup](https://developerdocs.instructure.com/services/canvas/resources/outcome_groups#outcomegroup) object.

[OutcomeGroupsApiController#importarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/outcome_groups_api_controller.rb)

`POST /api/v1/global/outcome_groups/:id/import`

**Scope:** `url:POST|/api/v1/global/outcome_groups/:id/import`

`POST /api/v1/accounts/:account_id/outcome_groups/:id/import`

**Scope:** `url:POST|/api/v1/accounts/:account_id/outcome_groups/:id/import`

`POST /api/v1/courses/:course_id/outcome_groups/:id/import`

**Scope:** `url:POST|/api/v1/courses/:course_id/outcome_groups/:id/import`

Creates a new subgroup of the outcome group with the same title and description as the source group, then creates links in that new subgroup to the same outcomes that are linked in the source group. Recurses on the subgroups of the source group, importing them each in turn into the new subgroup.

Allows you to copy organizational structure, but does not create copies of the outcomes themselves, only new links.

The source group must be either global, from the same context as this outcome group, or from an associated account. The source group cannot be the root outcome group of its context.

**Request Parameters:**

The ID of the source outcome group.

If true, perform action asynchronously. In that case, this endpoint will return a Progress object instead of an OutcomeGroup. Use the [progress endpoint](https://developerdocs.instructure.com/services/canvas/resources/progress#method.progress.show) to query the status of the operation. The imported outcome group id and url will be returned in the results of the Progress object as “outcome\_group\_id” and “outcome\_group\_url”

**Example Request:**

```
curl'https://<canvas>/api/v1/accounts/2/outcome_groups/3/import.json'\
-XPOST\
-F'source_outcome_group_id=2'\
-H"Authorization: Bearer <token>"
```

Returns an [OutcomeGroup](https://developerdocs.instructure.com/services/canvas/resources/outcome_groups#outcomegroup) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).