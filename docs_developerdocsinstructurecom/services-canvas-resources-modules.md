---
title: Modules | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/modules
source: sitemap
fetched_at: 2026-02-15T08:58:16.449066-03:00
rendered_js: false
word_count: 1635
summary: This document defines the data structures and API endpoints for managing learning modules, their constituent items, and completion requirements within a course.
tags:
    - canvas-lms
    - api-reference
    - learning-modules
    - course-content
    - module-items
    - data-models
category: api
---

Modules are collections of learning materials useful for organizing courses and optionally providing a linear flow through them. Module items can be accessed linearly or sequentially depending on module configuration. Items can be unlocked by various criteria such as reading a page or achieving a minimum score on a quiz. Modules themselves can be unlocked by the completion of other Modules.

If any active AssignmentOverrides exist on a ContextModule, then only students who have an applicable override can access the module and are assigned its items. AssignmentOverrides can be created for a (group of) student(s) or a section.

**A Module object looks like:**

```
{
  // the unique identifier for the module
"id": 123,
  // the state of the module: 'active', 'deleted'
"workflow_state": "active",
  // the position of this module in the course (1-based)
"position": 2,
  // the name of this module
"name": "Imaginary Numbers and You",
  // (Optional) the date this module will unlock
"unlock_at": "2012-12-31T06:00:00-06:00",
  // Whether module items must be unlocked in order
"require_sequential_progress": true,
  // Whether module requires all required items or one required item to be
  // considered complete (one of 'all' or 'one')
"requirement_type": "all",
  // IDs of Modules that must be completed before this one is unlocked
"prerequisite_module_ids": [121,122],
  // The number of items in the module
"items_count": 10,
  // The API URL to retrive this module's items
"items_url": "https://canvas.example.com/api/v1/modules/123/items",
  // The contents of this module, as an array of Module Items. (Present only if
  // requested via include[]=items AND the module is not deemed too large by
  // Canvas.)
"items": null,
  // The state of this Module for the calling user one of 'locked', 'unlocked',
  // 'started', 'completed' (Optional; present only if the caller is a student or
  // if the optional parameter 'student_id' is included)
"state": "started",
  // the date the calling user completed the module (Optional; present only if the
  // caller is a student or if the optional parameter 'student_id' is included)
"completed_at": null,
  // if the student's final grade for the course should be published to the SIS
  // upon completion of this module
"publish_final_grade": null,
  // (Optional) Whether this module is published. This field is present only if
  // the caller has permission to view unpublished modules.
"published": true
}
```

**A CompletionRequirement object looks like:**

```
{
  // one of 'must_view', 'must_submit', 'must_contribute', 'min_score',
  // 'min_percentage', 'must_mark_done'
  "type": "min_score",
  // minimum score required to complete (only present when type == 'min_score')
  "min_score": 10,
  // minimum percentage required to complete (only present when type ==
  // 'min_percentage')
  "min_percentage": 70,
  // whether the calling user has met this requirement (Optional; present only if
  // the caller is a student or if the optional parameter 'student_id' is
  // included)
  "completed": true
}
```

**A ContentDetails object looks like:**

```
{
  "points_possible": 20,
  "due_at": "2012-12-31T06:00:00-06:00",
  "unlock_at": "2012-12-31T06:00:00-06:00",
  "lock_at": "2012-12-31T06:00:00-06:00",
  "locked_for_user": true,
  "lock_explanation": "This quiz is part of an unpublished module and is not available yet.",
  "lock_info": {"asset_string":"assignment_4","unlock_at":"2012-12-31T06:00:00-06:00","lock_at":"2012-12-31T06:00:00-06:00","context_module":{}}
}
```

**A ModuleItem object looks like:**

```
{
  // the unique identifier for the module item
  "id": 768,
  // the id of the Module this item appears in
  "module_id": 123,
  // the position of this item in the module (1-based)
  "position": 1,
  // the title of this item
  "title": "Square Roots: Irrational numbers or boxy vegetables?",
  // 0-based indent level; module items may be indented to show a hierarchy
  "indent": 0,
  // the type of object referred to one of 'File', 'Page', 'Discussion',
  // 'Assignment', 'Quiz', 'SubHeader', 'ExternalUrl', 'ExternalTool'
  "type": "Assignment",
  // the id of the object referred to applies to 'File', 'Discussion',
  // 'Assignment', 'Quiz', 'ExternalTool' types
  "content_id": 1337,
  // link to the item in Canvas
  "html_url": "https://canvas.example.edu/courses/222/modules/items/768",
  // (Optional) link to the Canvas API object, if applicable
  "url": "https://canvas.example.edu/api/v1/courses/222/assignments/987",
  // (only for 'Page' type) unique locator for the linked wiki page
  "page_url": "my-page-title",
  // (only for 'ExternalUrl' and 'ExternalTool' types) external url that the item
  // points to
  "external_url": "https://www.example.com/externalurl",
  // (only for 'ExternalTool' type) whether the external tool opens in a new tab
  "new_tab": false,
  // Completion requirement for this module item
  "completion_requirement": {"type":"min_score","min_score":10,"completed":true},
  // (Present only if requested through include[]=content_details) If applicable,
  // returns additional details specific to the associated object
  "content_details": {"points_possible":20,"due_at":"2012-12-31T06:00:00-06:00","unlock_at":"2012-12-31T06:00:00-06:00","lock_at":"2012-12-31T06:00:00-06:00"},
  // (Optional) Whether this module item is published. This field is present only
  // if the caller has permission to view unpublished items.
  "published": true
}
```

**A ModuleItemSequenceNode object looks like:**

```
{
  // The previous ModuleItem in the sequence
  "prev": null,
  // The ModuleItem being queried
  "current": {"id":768,"module_id":123,"title":"A lonely page","type":"Page"},
  // The next ModuleItem in the sequence
  "next": {"id":769,"module_id":127,"title":"Project 1","type":"Assignment"},
  // The conditional release rule for the module item, if applicable
  "mastery_path": {"locked":true,"assignment_sets":[],"selected_set_id":null,"awaiting_choice":false,"still_processing":false,"modules_url":"\/courses\/11\/modules","choose_url":"\/courses\/11\/modules\/items\/9\/choose","modules_tab_disabled":false}
}
```

**A ModuleItemSequence object looks like:**

```
{
  // an array containing one ModuleItemSequenceNode for each appearence of the
  // asset in the module sequence (up to 10 total)
  "items": [{"prev":null,"current":{"id":768,"module_id":123,"title":"A lonely page","type":"Page"},"next":{"id":769,"module_id":127,"title":"Project 1","type":"Assignment"},"mastery_path":{"locked":true,"assignment_sets":[],"selected_set_id":null,"awaiting_choice":false,"still_processing":false,"modules_url":"\/courses\/11\/modules","choose_url":"\/courses\/11\/modules\/items\/9\/choose","modules_tab_disabled":false}}],
  // an array containing each Module referenced above
  "modules": [{"id":123,"name":"Overview"}, {"id":127,"name":"Imaginary Numbers"}]
}
```

**A ModuleAssignmentOverride object looks like:**

```
{
  // the ID of the assignment override
  "id": 4355,
  // the ID of the module the override applies to
  "context_module_id": 567,
  // the title of the override
  "title": "Section 6",
  // an array of the override's target students (present only if the override
  // targets an adhoc set of students)
  "students": null,
  // the override's target section (present only if the override targets a
  // section)
  "course_section": null
}
```

**An OverrideTarget object looks like:**

```
{
  // the ID of the user or section that the override is targeting
  "id": 7,
  // the name of the user or section that the override is targeting
  "name": "Section 6"
}
```

[ContextModulesApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/context_modules_api_controller.rb)

`GET /api/v1/courses/:course_id/modules`

**Scope:** `url:GET|/api/v1/courses/:course_id/modules`

A paginated list of the modules in a course

**Request Parameters:**

- “items”: Return module items inline if possible. This parameter suggests that Canvas return module items directly in the Module object JSON, to avoid having to make separate API requests for each module when enumerating modules and items. Canvas is free to omit ‘items’ for any particular module if it deems them too numerous to return inline. Callers must be prepared to use the [List Module Items API](https://developerdocs.instructure.com/services/canvas/resources/modules#method.context_module_items_api.index) if items are not returned.
- “content\_details”: Requires ‘items’. Returns additional details with module items specific to their associated content items. Includes standard lock information for each item.

Allowed values: `items`, `content_details`

The partial name of the modules (and module items, if ‘items’ is specified with include\[]) to match and return.

Returns module completion information for the student with this id.

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/courses/222/modules
```

Returns a list of [Module](https://developerdocs.instructure.com/services/canvas/resources/modules#module) objects.

[ContextModulesApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/context_modules_api_controller.rb)

`GET /api/v1/courses/:course_id/modules/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/modules/:id`

Get information about a single module

**Request Parameters:**

- “items”: Return module items inline if possible. This parameter suggests that Canvas return module items directly in the Module object JSON, to avoid having to make separate API requests for each module when enumerating modules and items. Canvas is free to omit ‘items’ for any particular module if it deems them too numerous to return inline. Callers must be prepared to use the [List Module Items API](https://developerdocs.instructure.com/services/canvas/resources/modules#method.context_module_items_api.index) if items are not returned.
- “content\_details”: Requires ‘items’. Returns additional details with module items specific to their associated content items. Includes standard lock information for each item.

Allowed values: `items`, `content_details`

Returns module completion information for the student with this id.

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/courses/222/modules/123
```

Returns a [Module](https://developerdocs.instructure.com/services/canvas/resources/modules#module) object.

[ContextModulesApiController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/context_modules_api_controller.rb)

`POST /api/v1/courses/:course_id/modules`

**Scope:** `url:POST|/api/v1/courses/:course_id/modules`

Create and return a new module

**Request Parameters:**

The date the module will unlock

The position of this module in the course (1-based)

`module[require_sequential_progress]`

Whether module items must be unlocked in order

`module[prerequisite_module_ids][]`

IDs of Modules that must be completed before this one is unlocked. Prerequisite modules must precede this module (i.e. have a lower position value), otherwise they will be ignored

`module[publish_final_grade]`

Whether to publish the student’s final grade for the course upon completion of this module.

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/modules \
  -X POST \
  -H 'Authorization: Bearer <token>' \
  -d 'module[name]=module' \
  -d 'module[position]=2' \
  -d 'module[prerequisite_module_ids][]=121' \
  -d 'module[prerequisite_module_ids][]=122'
```

Returns a [Module](https://developerdocs.instructure.com/services/canvas/resources/modules#module) object.

[ContextModulesApiController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/context_modules_api_controller.rb)

`PUT /api/v1/courses/:course_id/modules/:id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/modules/:id`

Update and return an existing module

**Request Parameters:**

The date the module will unlock

The position of the module in the course (1-based)

`module[require_sequential_progress]`

Whether module items must be unlocked in order

`module[prerequisite_module_ids][]`

IDs of Modules that must be completed before this one is unlocked Prerequisite modules must precede this module (i.e. have a lower position value), otherwise they will be ignored

`module[publish_final_grade]`

Whether to publish the student’s final grade for the course upon completion of this module.

Whether the module is published and visible to students

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/modules/<module_id> \
  -X PUT \
  -H 'Authorization: Bearer <token>' \
  -d 'module[name]=module' \
  -d 'module[position]=2' \
  -d 'module[prerequisite_module_ids][]=121' \
  -d 'module[prerequisite_module_ids][]=122'
```

Returns a [Module](https://developerdocs.instructure.com/services/canvas/resources/modules#module) object.

[ContextModulesApiController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/context_modules_api_controller.rb)

`DELETE /api/v1/courses/:course_id/modules/:id`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/modules/:id`

Delete a module

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/modules/<module_id> \
  -X Delete \
  -H 'Authorization: Bearer <token>'
```

Returns a [Module](https://developerdocs.instructure.com/services/canvas/resources/modules#module) object.

[ContextModulesApiController#relockarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/context_modules_api_controller.rb)

`PUT /api/v1/courses/:course_id/modules/:id/relock`

**Scope:** `url:PUT|/api/v1/courses/:course_id/modules/:id/relock`

Resets module progressions to their default locked state and recalculates them based on the current requirements.

Adding progression requirements to an active course will not lock students out of modules they have already unlocked unless this action is called.

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/modules/<module_id>/relock \
  -X PUT \
  -H 'Authorization: Bearer <token>'
```

Returns a [Module](https://developerdocs.instructure.com/services/canvas/resources/modules#module) object.

[ContextModuleItemsApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/context_module_items_api_controller.rb)

`GET /api/v1/courses/:course_id/modules/:module_id/items`

**Scope:** `url:GET|/api/v1/courses/:course_id/modules/:module_id/items`

A paginated list of the items in a module

**Request Parameters:**

If included, will return additional details specific to the content associated with each item. Refer to the [Module Item specification](https://developerdocs.instructure.com/services/canvas/resources/modules#Module%20Item) for more details. Includes standard lock information for each item.

Allowed values: `content_details`

The partial title of the items to match and return.

Returns module completion information for the student with this id.

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/courses/222/modules/123/items
```

Returns a list of [ModuleItem](https://developerdocs.instructure.com/services/canvas/resources/modules#moduleitem) objects.

[ContextModuleItemsApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/context_module_items_api_controller.rb)

`GET /api/v1/courses/:course_id/modules/:module_id/items/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/modules/:module_id/items/:id`

Get information about a single module item

**Request Parameters:**

If included, will return additional details specific to the content associated with this item. Refer to the [Module Item specification](https://developerdocs.instructure.com/services/canvas/resources/modules#Module%20Item) for more details. Includes standard lock information for each item.

Allowed values: `content_details`

Returns module completion information for the student with this id.

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/courses/222/modules/123/items/768
```

Returns a [ModuleItem](https://developerdocs.instructure.com/services/canvas/resources/modules#moduleitem) object.

[ContextModuleItemsApiController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/context_module_items_api_controller.rb)

`POST /api/v1/courses/:course_id/modules/:module_id/items`

**Scope:** `url:POST|/api/v1/courses/:course_id/modules/:module_id/items`

Create and return a new module item

**Request Parameters:**

The name of the module item and associated content

The type of content linked to the item

Allowed values: `File`, `Page`, `Discussion`, `Assignment`, `Quiz`, `SubHeader`, `ExternalUrl`, `ExternalTool`

The id of the content to link to the module item. Required, except for ‘ExternalUrl’, ‘Page’, and ‘SubHeader’ types.

The position of this item in the module (1-based).

0-based indent level; module items may be indented to show a hierarchy

Suffix for the linked wiki page (e.g. ‘front-page’). Required for ‘Page’ type.

`module_item[external_url]`

External url that the item points to. [Required for ‘ExternalUrl’ and ‘ExternalTool’ types.

Whether the external tool opens in a new tab. Only applies to ‘ExternalTool’ type.

`module_item[completion_requirement][type]`

Completion requirement for this module item. “must\_view”: Applies to all item types “must\_contribute”: Only applies to “Assignment”, “Discussion”, and “Page” types “must\_submit”, “min\_score”: Only apply to “Assignment” and “Quiz” types “must\_mark\_done”: Only applies to “Assignment” and “Page” types Inapplicable types will be ignored

Allowed values: `must_view`, `must_contribute`, `must_submit`, `must_mark_done`

`module_item[completion_requirement][min_score]`

Minimum score required to complete. Required for completion\_requirement type ‘min\_score’.

`module_item[iframe][width]`

Width of the ExternalTool on launch

`module_item[iframe][height]`

Height of the ExternalTool on launch

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/modules/<module_id>/items \
  -X POST \
  -H 'Authorization: Bearer <token>' \
  -d 'module_item[title]=module item' \
  -d 'module_item[type]=ExternalTool' \
  -d 'module_item[content_id]=10' \
  -d 'module_item[position]=2' \
  -d 'module_item[indent]=1' \
  -d 'module_item[new_tab]=true' \
  -d 'module_item[iframe][width]=300' \
  -d 'module_item[iframe][height]=200'
```

Returns a [ModuleItem](https://developerdocs.instructure.com/services/canvas/resources/modules#moduleitem) object.

[ContextModuleItemsApiController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/context_module_items_api_controller.rb)

`PUT /api/v1/courses/:course_id/modules/:module_id/items/:id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/modules/:module_id/items/:id`

Update and return an existing module item

**Request Parameters:**

The name of the module item

The position of this item in the module (1-based)

0-based indent level; module items may be indented to show a hierarchy

`module_item[external_url]`

External url that the item points to. Only applies to ‘ExternalUrl’ type.

Whether the external tool opens in a new tab. Only applies to ‘ExternalTool’ type.

`module_item[completion_requirement][type]`

Completion requirement for this module item. “must\_view”: Applies to all item types “must\_contribute”: Only applies to “Assignment”, “Discussion”, and “Page” types “must\_submit”, “min\_score”: Only apply to “Assignment” and “Quiz” types “must\_mark\_done”: Only applies to “Assignment” and “Page” types Inapplicable types will be ignored

Allowed values: `must_view`, `must_contribute`, `must_submit`, `must_mark_done`

`module_item[completion_requirement][min_score]`

Minimum score required to complete, Required for completion\_requirement type ‘min\_score’.

Whether the module item is published and visible to students.

Move this item to another module by specifying the target module id here. The target module must be in the same course.

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/modules/<module_id>/items/<item_id> \
  -X PUT \
  -H 'Authorization: Bearer <token>' \
  -d 'module_item[position]=2' \
  -d 'module_item[indent]=1' \
  -d 'module_item[new_tab]=true'
```

Returns a [ModuleItem](https://developerdocs.instructure.com/services/canvas/resources/modules#moduleitem) object.

[ContextModuleItemsApiController#select\_mastery\_patharrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/context_module_items_api_controller.rb)

`POST /api/v1/courses/:course_id/modules/:module_id/items/:id/select_mastery_path`

**Scope:** `url:POST|/api/v1/courses/:course_id/modules/:module_id/items/:id/select_mastery_path`

Select a mastery path when module item includes several possible paths. Requires Mastery Paths feature to be enabled. Returns a compound document with the assignments included in the given path and any module items related to those assignments

**Request Parameters:**

Assignment set chosen, as specified in the mastery\_paths portion of the context module item response

Which student the selection applies to. If not specified, current user is implied.

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/modules/<module_id>/items/<item_id>/select_master_path \
  -X POST \
  -H 'Authorization: Bearer <token>' \
  -d 'assignment_set_id=2992'
```

[ContextModuleItemsApiController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/context_module_items_api_controller.rb)

`DELETE /api/v1/courses/:course_id/modules/:module_id/items/:id`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/modules/:module_id/items/:id`

Delete a module item

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/modules/<module_id>/items/<item_id> \
  -X Delete \
  -H 'Authorization: Bearer <token>'
```

Returns a [ModuleItem](https://developerdocs.instructure.com/services/canvas/resources/modules#moduleitem) object.

[ContextModuleItemsApiController#mark\_as\_donearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/context_module_items_api_controller.rb)

`PUT /api/v1/courses/:course_id/modules/:module_id/items/:id/done`

**Scope:** `url:PUT|/api/v1/courses/:course_id/modules/:module_id/items/:id/done`

Mark a module item as done/not done. Use HTTP method PUT to mark as done, and DELETE to mark as not done.

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/modules/<module_id>/items/<item_id>/done \
  -X Put \
  -H 'Authorization: Bearer <token>'
```

[ContextModuleItemsApiController#item\_sequencearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/context_module_items_api_controller.rb)

`GET /api/v1/courses/:course_id/module_item_sequence`

**Scope:** `url:GET|/api/v1/courses/:course_id/module_item_sequence`

Given an asset in a course, find the ModuleItem it belongs to, the previous and next Module Items in the course sequence, and also any applicable mastery path rules

**Request Parameters:**

The type of asset to find module sequence information for. Use the ModuleItem if it is known (e.g., the user navigated from a module item), since this will avoid ambiguity if the asset appears more than once in the module sequence.

Allowed values: `ModuleItem`, `File`, `Page`, `Discussion`, `Assignment`, `Quiz`, `ExternalTool`

The id of the asset (or the url in the case of a Page)

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/module_item_sequence?asset_type=Assignment&asset_id=123 \
  -H 'Authorization: Bearer <token>'
```

Returns a [ModuleItemSequence](https://developerdocs.instructure.com/services/canvas/resources/modules#moduleitemsequence) object.

[ContextModuleItemsApiController#mark\_item\_readarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/context_module_items_api_controller.rb)

`POST /api/v1/courses/:course_id/modules/:module_id/items/:id/mark_read`

**Scope:** `url:POST|/api/v1/courses/:course_id/modules/:module_id/items/:id/mark_read`

Fulfills “must view” requirement for a module item. It is generally not necessary to do this explicitly, but it is provided for applications that need to access external content directly (bypassing the html\_url redirect that normally allows Canvas to fulfill “must view” requirements).

This endpoint cannot be used to complete requirements on locked or unpublished module items.

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/modules/<module_id>/items/<item_id>/mark_read \
  -X POST \
  -H 'Authorization: Bearer <token>'
```

[ModuleAssignmentOverridesController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/module_assignment_overrides_controller.rb)

`GET /api/v1/courses/:course_id/modules/:context_module_id/assignment_overrides`

**Scope:** `url:GET|/api/v1/courses/:course_id/modules/:context_module_id/assignment_overrides`

Returns a paginated list of AssignmentOverrides that apply to the ContextModule.

**Example Request:**

```
curl https://<canvas>/api/v1/courses/:course_id/modules/:context_module_id/assignment_overrides \
  -H 'Authorization: Bearer <token>'
```

Returns a list of [ModuleAssignmentOverride](https://developerdocs.instructure.com/services/canvas/resources/modules#moduleassignmentoverride) objects.

[ModuleAssignmentOverridesController#bulk\_updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/module_assignment_overrides_controller.rb)

`PUT /api/v1/courses/:course_id/modules/:context_module_id/assignment_overrides`

**Scope:** `url:PUT|/api/v1/courses/:course_id/modules/:context_module_id/assignment_overrides`

Accepts a list of overrides and applies them to the ContextModule. Returns 204 No Content response code if successful.

**Request Parameters:**

List of overrides to apply to the module. Overrides that already exist should include an ID and will be updated if needed. New overrides will be created for overrides in the list without an ID. Overrides not included in the list will be deleted. Providing an empty list will delete all of the module’s overrides. Keys for each override object can include: ‘id’, ‘title’, ‘student\_ids’, and ‘course\_section\_id’. ‘group\_id’ is accepted if the Differentiation Tags account setting is enabled.

**Example Request:**

```
curl https://<canvas>/api/v1/courses/:course_id/modules/:context_module_id/assignment_overrides \
  -X PUT \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{
        "overrides": [
          {
            "id": 212,
            "course_section_id": 3564
          },
          {
            "id": 56,
            "group_id": 7809
          },
          {
            "title": "an assignment override",
            "student_ids": [1, 2, 3]
          }
        ]
      }'
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 2 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).