---
title: Line Items | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/line_items
source: sitemap
fetched_at: 2026-02-15T09:10:25.433857-03:00
rendered_js: false
word_count: 691
summary: This document defines the LTI Assignment and Grade Services Line Item API, explaining how to create, list, and manage gradebook columns within Canvas. It covers the LineItem object model, required scopes, and specific request parameters for CRUD operations.
tags:
    - lti-advantage
    - assignment-and-grade-services
    - canvas-lms
    - api-documentation
    - line-item-api
    - ims-global
category: api
---

Line Item API for 1EdTech (IMS) [Assignment and Grade Services](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.assignment_tools).

**A LineItem object looks like:**

```
{
  // The fully qualified URL for showing, updating, and deleting the Line Item
"id": "http://institution.canvas.com/api/lti/courses/5/line_items/2",
  // The maximum score of the Line Item
"scoreMaximum": 50,
  // The label of the Line Item.
"label": "50",
  // Tag used to qualify a line Item beyond its ids
"tag": "50",
  // A Tool Provider specified id for the Line Item. Multiple line items can share
  // the same resourceId within a given context
"resourceId": "50",
  // The resource link id the Line Item is attached to
"resourceLinkId": "50",
  // The extension that defines the submission_type of the line_item. Only returns
  // if set through the line_item create endpoint.
"https://canvas.instructure.com/lti/submission_type": "{
"type":"external_tool",
"external_tool_url":"https://my.launch.url",
}",
  // The launch url of the Line Item. Only returned if `include=launch_url` query
  // parameter is passed, and only for Show and List actions.
"https://canvas.instructure.com/lti/launch_url": "https://my.tool.url/launch"
}
```

[Lti::Ims::LineItemsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/line_items_controller.rb)

`POST /api/lti/courses/:course_id/line_items`

**Scope:** `url:POST|/api/lti/courses/:course_id/line_items`

Create a new Line Item

**Request Parameters:**

The maximum score for the line item. Scores created for the Line Item may exceed this value.

The label for the Line Item. If no resourceLinkId is specified this value will also be used as the name of the placeholder assignment.

A Tool Provider specified id for the Line Item. Multiple line items may share the same resourceId within a given context.

A value used to qualify a line Item beyond its ids. Line Items may be queried by this value in the List endpoint. Multiple line items can share the same tag within a given context.

The resource link id the Line Item should be attached to. This value should match the LTI id of the Canvas assignment associated with the tool.

The ISO8601 date and time when the line item is made available. Corresponds to the assignment’s unlock\_at date.

The ISO8601 date and time when the line item stops receiving submissions. Corresponds to the assignment’s due\_at date.

`https://canvas.instructure.com/lti/submission_type`

(EXTENSION) - Optional block to set Assignment Submission Type when creating a new assignment is created.

- type - ‘none’ or ‘external\_tool’
- external\_tool\_url - Submission URL only used when type: ‘external\_tool’

**Example Request:**

```
{
  "scoreMaximum": 100.0,
  "label": "LineItemLabel1",
  "resourceId": 1,
  "tag": "MyTag",
  "resourceLinkId": "1",
  "startDateTime": "2022-01-31T22:23:11+0000",
  "endDateTime": "2022-02-07T22:23:11+0000",
  "https://canvas.instructure.com/lti/submission_type": {
    "type": "external_tool",
    "external_tool_url": "https://my.launch.url"
  }
}
```

Returns a [LineItem](https://developerdocs.instructure.com/services/canvas/resources/line_items#lineitem) object.

[Lti::Ims::LineItemsController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/line_items_controller.rb)

`PUT /api/lti/courses/:course_id/line_items/:id`

**Scope:** `url:PUT|/api/lti/courses/:course_id/line_items/:id`

Update new Line Item

**Request Parameters:**

The maximum score for the line item. Scores created for the Line Item may exceed this value.

The label for the Line Item. If no resourceLinkId is specified this value will also be used as the name of the placeholder assignment.

A Tool Provider specified id for the Line Item. Multiple line items may share the same resourceId within a given context.

A value used to qualify a line Item beyond its ids. Line Items may be queried by this value in the List endpoint. Multiple line items can share the same tag within a given context.

The ISO8601 date and time when the line item is made available. Corresponds to the assignment’s unlock\_at date.

The ISO8601 date and time when the line item stops receiving submissions. Corresponds to the assignment’s due\_at date.

Returns a [LineItem](https://developerdocs.instructure.com/services/canvas/resources/line_items#lineitem) object.

[Lti::Ims::LineItemsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/line_items_controller.rb)

`GET /api/lti/courses/:course_id/line_items/:id`

**Scope:** `url:GET|/api/lti/courses/:course_id/line_items/:id`

Show existing Line Item

**Request Parameters:**

Array of additional information to include.

- “launch\_url”
  
  includes the launch URL for this line item using the “https://canvas.instructure.com/lti/launch\_url” extension

Allowed values: `launch_url`

Returns a [LineItem](https://developerdocs.instructure.com/services/canvas/resources/line_items#lineitem) object.

[Lti::Ims::LineItemsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/line_items_controller.rb)

`GET /api/lti/courses/:course_id/line_items`

**Scope:** `url:GET|/api/lti/courses/:course_id/line_items`

List all Line Items for a course

**Request Parameters:**

If specified only Line Items with this tag will be included.

If specified only Line Items with this resource\_id will be included.

If specified only Line Items attached to the specified resource\_link\_id will be included.

May be used to limit the number of Line Items returned in a page

Array of additional information to include.

- “launch\_url”
  
  includes the launch URL for each line item using the “https://canvas.instructure.com/lti/launch\_url” extension

Allowed values: `launch_url`

Returns a [LineItem](https://developerdocs.instructure.com/services/canvas/resources/line_items#lineitem) object.

[Lti::Ims::LineItemsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/line_items_controller.rb)

`DELETE /api/lti/courses/:course_id/line_items/:id`

**Scope:** `url:DELETE|/api/lti/courses/:course_id/line_items/:id`

Delete an existing Line Item

Returns a [LineItem](https://developerdocs.instructure.com/services/canvas/resources/line_items#lineitem) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).