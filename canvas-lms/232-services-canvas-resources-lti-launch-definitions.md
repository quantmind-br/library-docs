---
title: LTI Launch Definitions | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/lti_launch_definitions
source: sitemap
fetched_at: 2026-02-15T09:10:19.913333-03:00
rendered_js: false
word_count: 137
summary: This document defines the LTI Launch Definitions API, providing technical specifications for retrieving tool launch configurations and placement details within Canvas LMS.
tags:
    - canvas-lms
    - lti-integration
    - launch-definitions
    - external-tools
    - api-endpoints
category: api
---

## LTI Launch Definitions API

**A Lti::LaunchDefinition object looks like:**

```
// A bare-bones representation of an LTI tool used by Canvas to launch the tool
{
  // The type of the launch definition. Always 'ContextExternalTool'
"definition_type": "ContextExternalTool",
  // The Canvas ID of the tool
"definition_id": "123",
  // The display name of the tool for the given placement
"name": "My Tool",
  // The description of the tool for the given placement.
"description": "This is a tool that does things.",
  // The launch URL for the tool
"url": "https://www.example.com/launch",
  // The domain of the tool
"domain": "example.com",
  // Placement-specific config for given placements
"placements": {"assignment_selection":{"type":"Lti::PlacementLaunchDefinition"}}
}
```

**A Lti::PlacementLaunchDefinition object looks like:**

```
// A bare-bones LTI configuration for a specific placement
{
  // The LTI launch message type
  "message_type": "LtiResourceLinkRequest",
  // The launch URL for this placement
  "url": "https://www.example.com/launch?placement=assignment_selection",
  // The title of the tool for this placement
  "title": "My Tool (Assignment Selection)"
}
```

[Lti::LtiAppsController#launch\_definitionsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/lti_apps_controller.rb)

`GET /api/v1/courses/:course_id/lti_apps/launch_definitions`

**Scope:** `url:GET|/api/v1/courses/:course_id/lti_apps/launch_definitions`

`GET /api/v1/accounts/:account_id/lti_apps/launch_definitions`

**Scope:** `url:GET|/api/v1/accounts/:account_id/lti_apps/launch_definitions`

List all tools available in this context for the given placements, in the form of Launch Definitions. Used primarily by the Canvas frontend. API users should consider using the External Tools API instead. This endpoint is cached for 10 minutes!

**Request Parameters:**

The placements to return launch definitions for. If not provided, an empty list will be returned.

If true, only return launch definitions that are visible to the current user. Defaults to true.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).