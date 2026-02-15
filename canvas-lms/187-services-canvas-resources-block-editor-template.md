---
title: BlockEditorTemplate | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/block_editor_template
source: sitemap
fetched_at: 2026-02-15T09:05:11.086784-03:00
rendered_js: false
word_count: 149
summary: This document defines the BlockEditorTemplate object structure and details the API endpoint for retrieving a list of block editor templates available within a specific course.
tags:
    - block-editor
    - api-documentation
    - canvas-lms
    - templates
    - content-management
    - rest-api
category: api
---

Block Editor Templates are pre-build templates that can be used to create pages. The BlockEditorTemplate API allows you to create, retrieve, update, and delete templates.

**A BlockEditorTemplate object looks like:**

```
{
  // the ID of the page
"id": 1,
  // name of the template
"name": "Navigation Bar",
  // description of the template
"description": "A bar of links to other content",
  // the creation date for the template
"created_at": "2012-08-06T16:46:33-06:00",
  // the date the template was last updated
"updated_at": "2012-08-08T14:25:20-06:00",
  // The JSON data that is the template
"node_tree": null,
  // The version of the editor that created the template
"editor_version": "1.0",
  // The type of template. One of 'block', 'section', or 'page'
"template_type": "page",
  // String indicating what state this assignment is in.
"workflow_state": "unpublished"
}
```

[BlockEditorTemplatesApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/block_editor_templates_api_controller.rb)

`GET /api/v1/courses/:course_id/block_editor_templates`

**Scope:** `url:GET|/api/v1/courses/:course_id/block_editor_templates`

A list of the block templates available to the current user.

**Request Parameters:**

Sort results by this field.

Allowed values: `name`, `created_at`, `updated_at`

The sorting order. Defaults to ‘asc’.

Allowed values: `asc`, `desc`

If true, include draft templates. If false or omitted only published templates will be returned.

What type of templates should be returned.

Allowed values: `page`, `section`, `block`

no description

Allowed values: `node_tree`, `thumbnail`

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/courses/123/block_editor_templates?sort=name&order=asc&drafts=true
```

Returns a list of [BlockEditorTemplate](https://developerdocs.instructure.com/services/canvas/resources/block_editor_template#blockeditortemplate) objects.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).