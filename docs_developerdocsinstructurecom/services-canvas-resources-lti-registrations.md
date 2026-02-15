---
title: LTI Registrations | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/lti_registrations
source: sitemap
fetched_at: 2026-02-15T08:57:10.474172-03:00
rendered_js: false
word_count: 1435
summary: This document defines the API resources and data structures used for managing LTI tool registrations and configurations within Canvas root accounts.
tags:
    - lti-registration
    - canvas-api
    - lti-1-3
    - lti-1-1
    - tool-configuration
    - account-binding
category: api
---

BETA: This API resource is not finalized, and there could be breaking changes before its final release.

API for accessing and configuring LTI registrations in a root account. LTI Registrations can be any of:

- 1.3 manual installation (via JSON, URL, or UI)
- 1.1 manual installation (via XML, URL, or UI)

The Dynamic Registration process uses a different API endpoint to finalize the process and create the registration. The [Registration guide](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.registration) has more details on that process.

**A Lti::Registration object looks like:**

```
// A registration of an LTI tool in Canvas
{
  // the Canvas ID of the Lti::Registration object
"id": 2,
  // Tool-provided registration name
"name": "My LTI Tool",
  // Admin-configured friendly display name
"admin_nickname": "My LTI Tool (Campus A)",
  // Tool-provided URL to the tool's icon
"icon_url": "https://mytool.com/icon.png",
  // Tool-provided name of the tool vendor
"vendor": "My Tool LLC",
  // The Canvas id of the account that owns this registration
"account_id": 1,
  // Flag indicating if registration is internally-owned
"internal_service": false,
  // Flag indicating if registration is owned by this account, or inherited from
  // Site Admin
"inherited": false,
  // LTI version of the registration, either 1.1 or 1.3
"lti_version": "1.3",
  // Flag indicating if registration was created using LTI Dynamic Registration.
  // Only present if lti_version is 1.3
"dynamic_registration": false,
  // The state of the registration
"workflow_state": "active",
  // Timestamp of the registration's creation
"created_at": "2024-01-01T00:00:00Z",
  // Timestamp of the registration's last update
"updated_at": "2024-01-01T00:00:00Z",
  // The user that created this registration. Not always present. If a string,
  // this registration was created by Instructure.
"created_by": {"type":"User"},
  // The user that last updated this registration. Not always present. If a
  // string, this registration was last updated by Instructure.
"updated_by": {"type":"User"},
  // The Canvas id of the root account
"root_account_id": 1,
  // The binding for this registration and this account
"account_binding": {"type":"Lti::RegistrationAccountBinding"},
  // The Canvas-style tool configuration for this registration
"configuration": {"type":"Lti::ToolConfiguration"}
}
```

**A Lti::RegistrationAccountBinding object looks like:**

```
// A binding between an LTI registration and an account, defining the
// registration's availability in that account
{
  // the Canvas ID of the Lti::RegistrationAccountBinding object
  "id": 10,
  // The Canvas id of the account
  "account_id": 1,
  // The Canvas id of the root account
  "root_account_id": 1,
  // The Canvas id of the Lti::Registration
  "registration_id": 2,
  // The state of the binding (on, off, allow, deleted)
  "workflow_state": "on",
  // Timestamp of the binding's creation
  "created_at": "2024-01-01T00:00:00Z",
  // Timestamp of the binding's last update
  "updated_at": "2024-01-01T00:00:00Z",
  // The user that created this binding
  "created_by": {"type":"User"},
  // The user that last updated this binding
  "updated_by": {"type":"User"}
}
```

**A Lti::LegacyConfiguration object looks like:**

```
// A legacy configuration format for LTI 1.3 tools.
{
  // The display name of the tool
  "title": "My Tool",
  // The description of the tool
  "description": "My Tool is built by me, for me.",
  // A key-value listing of all custom fields the tool has requested
  "custom_fields": {"context_title":"$Context.title","special_tool_thing":"foo1234"},
  // The default launch URL for the tool. Overridable by placements.
  "target_link_uri": "https://mytool.com/launch",
  // 1.3 specific. URL used for initial login request
  "oidc_initiation_url": "https://mytool.com/1_3/login",
  // 1.3 specific. Region-specific login URLs for data protection compliance
  "oidc_initiation_urls": {"eu-west-1":"https:\/\/dub.mytool.com\/1_3\/login"},
  // 1.3 specific. The tool's public JWK in JSON format. Discouraged in favor of a
  // url hosting a JWK set.
  "public_jwk": {"e":"AQAB","etc":"etc"},
  // 1.3 specific. The tool-hosted URL containing its public JWK keyset. Canvas
  // may cache JWKs up to 5 minutes.
  "public_jwk_url": "https://mytool.com/1_3/jwks",
  // 1.3 specific. List of LTI scopes requested by the tool
  "scopes": ["https://purl.imsglobal.org/spec/lti-ags/scope/lineitem"],
  // Array of extensions for the tool
  "extensions": null
}
```

**A Lti::ToolConfiguration object looks like:**

```
// A Registration's Canvas-specific tool configuration.
{
  // The display name of the tool
  "title": "My Tool",
  // The description of the tool
  "description": "My Tool is built by me, for me.",
  // A key-value listing of all custom fields the tool has requested
  "custom_fields": {"context_title":"$Context.title","special_tool_thing":"foo1234"},
  // The default launch URL for the tool. Overridable by placements.
  "target_link_uri": "https://mytool.com/launch",
  // The tool's main domain. Highly recommended for deep linking, used to match
  // links to the tool.
  "domain": "mytool.com",
  // Tool-provided identifier, can be anything
  "tool_id": "MyTool",
  // Canvas-defined privacy level for the tool
  "privacy_level": "public",
  // 1.3 specific. URL used for initial login request
  "oidc_initiation_url": "https://mytool.com/1_3/login",
  // 1.3 specific. Region-specific login URLs for data protection compliance
  "oidc_initiation_urls": {"eu-west-1":"https:\/\/dub.mytool.com\/1_3\/login"},
  // 1.3 specific. The tool's public JWK in JSON format. Discouraged in favor of a
  // url hosting a JWK set.
  "public_jwk": {"e":"AQAB","etc":"etc"},
  // 1.3 specific. The tool-hosted URL containing its public JWK keyset. Canvas
  // may cache JWKs up to 5 minutes.
  "public_jwk_url": "https://mytool.com/1_3/jwks",
  // 1.3 specific. List of LTI scopes requested by the tool
  "scopes": ["https://purl.imsglobal.org/spec/lti-ags/scope/lineitem"],
  // 1.3 specific. List of possible launch URLs for after the Canvas authorize
  // redirect step
  "redirect_uris": ["https://mytool.com/launch", "https://mytool.com/1_3/launch"],
  // Default launch settings for all placements
  "launch_settings": {"message_type":"LtiResourceLinkRequest"},
  // List of placements configured by the tool
  "placements": [{"type":"Lti::Placement"}]
}
```

**A Lti::LaunchSettings object looks like:**

```
// Default launch settings for all placements
{
  // Default message type for all placements
  "message_type": "LtiResourceLinkRequest",
  // The text of the link to the tool (if applicable).
  "text": "Hello World",
  // Canvas-specific i18n for placement text. See the Navigation Placement docs.
  "labels": {"en":"Hello World","es":"Hola Mundo"},
  // Placement-specific custom fields to send in the launch. Merged with
  // tool-level custom fields.
  "custom_fields": {"special_placement_thing":"foo1234"},
  // Default iframe height. Not valid for all placements. Overrides tool-level
  // launch_height.
  "selection_height": 800,
  // Default iframe width. Not valid for all placements. Overrides tool-level
  // launch_width.
  "selection_width": 1000,
  // Default iframe height. Not valid for all placements. Overrides tool-level
  // launch_height.
  "launch_height": 800,
  // Default iframe width. Not valid for all placements. Overrides tool-level
  // launch_width.
  "launch_width": 1000,
  // Default icon URL. Not valid for all placements. Overrides tool-level
  // icon_url.
  "icon_url": "https://mytool.com/icon.png",
  // The HTML class name of an InstUI Icon. Used instead of an icon_url in select
  // placements.
  "canvas_icon_class": "icon-lti",
  // Comma-separated list of Canvas permission short names required for a user to
  // launch from this placement.
  "required_permissions": "manage_course_content_edit,manage_course_content_read",
  // When set to '_blank', opens placement in a new tab.
  "windowTarget": "_blank",
  // The Canvas layout to use when launching the tool. See the Navigation
  // Placement docs.
  "display_type": "full_width_in_context",
  // The 1.1 launch URL for this placement. Overrides tool-level url.
  "url": "https://mytool.com/launch?placement=course_navigation",
  // The 1.3 launch URL for this placement. Overrides tool-level target_link_uri.
  "target_link_uri": "https://mytool.com/launch?placement=course_navigation",
  // Specifies types of users that can see this placement. Only valid for some
  // placements like course_navigation.
  "visibility": "admins",
  // 1.1 specific. If true, the tool will send the SIS email in the
  // lis_person_contact_email_primary launch property
  "prefer_sis_email": false,
  // 1.1 specific. If true, query parameters from the launch URL will not be
  // copied to the POST body.
  "oauth_compliant": true,
  // An SVG to use instead of an icon_url. Only valid for global_navigation.
  "icon_svg_path_64": "M100,37L70.1,10.5v176H37...",
  // Default display state for course_navigation. If 'enabled', will show in
  // course sidebar. If 'disabled', will be hidden.
  "default": "disabled",
  // Comma-separated list of media types that the tool can accept. Only valid for
  // file_item.
  "accept_media_types": "image/*,video/*",
  // If true, the tool will be launched in the tray. Only used by the
  // editor_button placement.
  "use_tray": true
}
```

**A Lti::Placement object looks like:**

```
// The tool's configuration for a specific placement
{
  // The name of the placement.
  "placement": "course_navigation",
  // If true, the tool will show in this placement. If false, it will not.
  "enabled": true,
  // Default message type for all placements
  "message_type": "LtiResourceLinkRequest",
  // The text of the link to the tool (if applicable).
  "text": "Hello World",
  // Canvas-specific i18n for placement text. See the Navigation Placement docs.
  "labels": {"en":"Hello World","es":"Hola Mundo"},
  // Placement-specific custom fields to send in the launch. Merged with
  // tool-level custom fields.
  "custom_fields": {"special_placement_thing":"foo1234"},
  // Default iframe height. Not valid for all placements. Overrides tool-level
  // launch_height.
  "selection_height": 800,
  // Default iframe width. Not valid for all placements. Overrides tool-level
  // launch_width.
  "selection_width": 1000,
  // Default iframe height. Not valid for all placements. Overrides tool-level
  // launch_height.
  "launch_height": 800,
  // Default iframe width. Not valid for all placements. Overrides tool-level
  // launch_width.
  "launch_width": 1000,
  // Default icon URL. Not valid for all placements. Overrides tool-level
  // icon_url.
  "icon_url": "https://mytool.com/icon.png",
  // The HTML class name of an InstUI Icon. Used instead of an icon_url in select
  // placements.
  "canvas_icon_class": "icon-lti",
  // Comma-separated list of Canvas permission short names required for a user to
  // launch from this placement.
  "required_permissions": "manage_course_content_edit,manage_course_content_read",
  // When set to '_blank', opens placement in a new tab.
  "windowTarget": "_blank",
  // The Canvas layout to use when launching the tool. See the Navigation
  // Placement docs.
  "display_type": "full_width_in_context",
  // The 1.1 launch URL for this placement. Overrides tool-level url.
  "url": "https://mytool.com/launch?placement=course_navigation",
  // The 1.3 launch URL for this placement. Overrides tool-level target_link_uri.
  "target_link_uri": "https://mytool.com/launch?placement=course_navigation",
  // Specifies types of users that can see this placement. Only valid for some
  // placements like course_navigation.
  "visibility": "admins",
  // 1.1 specific. If true, the tool will send the SIS email in the
  // lis_person_contact_email_primary launch property
  "prefer_sis_email": false,
  // 1.1 specific. If true, query parameters from the launch URL will not be
  // copied to the POST body.
  "oauth_compliant": true,
  // An SVG to use instead of an icon_url. Only valid for global_navigation.
  "icon_svg_path_64": "M100,37L70.1,10.5v176H37...",
  // Default display state for course_navigation. If 'enabled', will show in
  // course sidebar. If 'disabled', will be hidden.
  "default": "disabled",
  // Comma-separated list of media types that the tool can accept. Only valid for
  // file_item.
  "accept_media_types": "image/*,video/*",
  // If true, the tool will be launched in the tray. Only used by the
  // editor_button placement.
  "use_tray": true
}
```

**A Lti::Overlay object looks like:**

```
// Changes made by a Canvas admin to a tool's configuration.
{
  // The display name of the tool
  "title": "My Tool",
  // The description of the tool
  "description": "My Tool is built by me, for me.",
  // A key-value listing of all custom fields the tool has requested
  "custom_fields": {"context_title":"$Context.title","special_tool_thing":"foo1234"},
  // The default launch URL for the tool. Overridable by placements.
  "target_link_uri": "https://mytool.com/launch",
  // The tool's main domain. Highly recommended for deep linking, used to match
  // links to the tool.
  "domain": "mytool.com",
  // Canvas-defined privacy level for the tool
  "privacy_level": "public",
  // 1.3 specific. URL used for initial login request
  "oidc_initiation_url": "https://mytool.com/1_3/login",
  // 1.3 specific. List of LTI scopes that the tool has requested but an admin has
  // disabled
  "disabled_scopes": ["https://purl.imsglobal.org/spec/lti-ags/scope/lineitem"],
  // List of placements that the tool has requested but an admin has disabled
  "disabled_placements": ["course_navigation"],
  // Placement-specific settings changed by an admin
  "placements": {"course_navigation":{"$ref":"Lti::Placement"}}
}
```

**A Lti::OverlayVersion object looks like:**

```
// A single version of a tool's configuration overlay
{
  // The Canvas id of the root account
  "root_account_id": 1,
  // Timestamp of the version's creation
  "created_at": "2024-01-01T00:00:00Z",
  // Timestamp of the version's last update
  "updated_at": "2024-01-01T00:00:00Z",
  // Whether or not this change was caused by a reset of the tool's configuration
  "caused_by_reset": false,
  // The user that created this version. If a string, this registration was
  // created by Instructure.
  "created_by": {"type":"User"},
  // A list of changes made in this version compared to the previous version
  "diff": [["+", "disabled_placements[0]", "top_navigation"]],
  // The id of the overlay this version is for
  "lti_overlay_id": 1,
  // The id of the account this version is for
  "account_id": 1
}
```

**A Lti::PlacementOverlay object looks like:**

```
// Changes made by a Canvas admin to a tool's configuration for a specific
// placement.
{
  // The text of the link to the tool (if applicable).
  "text": "Hello World",
  // The default launch URL for the tool. Overridable by placements.
  "target_link_uri": "https://mytool.com/launch",
  // Default message type for all placements
  "message_type": "LtiResourceLinkRequest",
  // Default iframe height. Not valid for all placements. Overrides tool-level
  // launch_height.
  "launch_height": 800,
  // Default iframe width. Not valid for all placements. Overrides tool-level
  // launch_width.
  "launch_width": 1000,
  // Default icon URL. Not valid for all placements. Overrides tool-level
  // icon_url.
  "icon_url": "https://mytool.com/icon.png",
  // Default display state for course_navigation. If 'enabled', will show in
  // course sidebar. If 'disabled', will be hidden.
  "default": "disabled"
}
```

**A ListLtiRegistrationsResponse object looks like:**

```
// The response for the List LTI Registrations API endpoint
{
  // The total number of LTI registrations across all pages
  "total": 1,
  // The paginated list of LTI::Registrations
  "data": [{"$ref":"Lti::Registration"}]
}
```

**A ContextSearchResponse object looks like:**

```
// The response for the Search Accounts and Courses API endpoint
{
  // Accounts that match the search query. Limited to 100.
  "accounts": [{"$ref":"Account"}],
  // Courses that match the search query. Limited to 100.
  "courses": [{"$ref":"Course"}]
}
```

**A SearchableAccount object looks like:**

```
// A minimal representation of an Account for Canvas Apps search purposes
{
  // The Canvas DB ID
  "id": "1",
  // The account name
  "name": "An Account",
  // The SIS ID of the account, if any. Only present if user can read or manage
  // SIS.
  "sis_id": "sis-account-1",
  // Names of the accounts in this account's hierarchy, excluding the root and
  // this account.
  "display_path": ["Sub Account"]
}
```

**A SearchableCourse object looks like:**

```
// A minimal representation of a Course for Canvas Apps search purposes
{
  // The Canvas DB ID
  "id": "1",
  // The course name
  "name": "A Course",
  // The SIS ID of the course, if any. Only present if user can read or manage
  // SIS.
  "sis_id": "sis-course-1",
  // Names of the accounts in this course's account hierarchy, excluding the root.
  "display_path": ["Sub Account"],
  // The course code
  "course_code": "COURSE-101"
}
```

[Lti::RegistrationsController#listarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`GET /api/v1/accounts/:account_id/lti_registrations`

**Scope:** `url:GET|/api/v1/accounts/:account_id/lti_registrations`

Returns all LTI registrations in the specified account. Includes registrations created in this account, those set to ‘allow’ from a parent root account (like Site Admin) and ‘on’ for this account, and those enabled ‘on’ at the parent root account level.

**Request Parameters:**

The number of registrations to return per page. Defaults to 15.

The page number to return. Defaults to 1.

The field to sort by. Choices are: name, nickname, lti\_version, installed, installed\_by, updated\_by, updated, and on. Defaults to installed.

The order to sort the given column by. Defaults to desc.

Allowed values: `asc`, `desc`

Array of additional data to include. Always includes \[account\_binding].

- “account\_binding”
  
  the registration’s binding to the given account
- “configuration”
  
  the registration’s Canvas-style tool configuration, without any overlays applied.
- “overlaid\_configuration”
  
  the registration’s Canvas-style tool configuration, with all overlays applied.
- “overlay”
  
  the registration’s admin-defined configuration overlay

**Example Request:**

```
This would return the specified LTI registration
curl -X GET 'https://<canvas>/api/v1/accounts/<account_id>/registrations' \
     -H "Authorization: Bearer <token>"
```

Returns a [ListLtiRegistrationsResponse](https://developerdocs.instructure.com/services/canvas/resources/lti_registrations#listltiregistrationsresponse) object.

[Lti::RegistrationsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`GET /api/v1/accounts/:account_id/lti_registrations/:id`

**Scope:** `url:GET|/api/v1/accounts/:account_id/lti_registrations/:id`

Return details about the specified LTI registration, including the configuration and account binding.

**Request Parameters:**

Array of additional data to include. Always includes \[account\_binding configuration].

- “account\_binding”
  
  the registration’s binding to the given account
- “configuration”
  
  the registration’s Canvas-style tool configuration, without any overlays applied.
- “overlaid\_configuration”
  
  the registration’s Canvas-style tool configuration, with all overlays applied.
- “overlaid\_legacy\_configuration”
  
  the registration’s legacy-style configuration, with all overlays applied.
- “overlay”
  
  the registration’s admin-defined configuration overlay
- “overlay\_versions”
  
  the registration’s overlay’s edit history

**Example Request:**

```
This would return the specified LTI registration
curl -X GET 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>' \
     -H "Authorization: Bearer <token>"
```

Returns a [Lti::Registration](https://developerdocs.instructure.com/services/canvas/resources/lti_registrations#lti::registration) object.

[Lti::RegistrationsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`POST /api/v1/accounts/:account_id/lti_registrations`

**Scope:** `url:POST|/api/v1/accounts/:account_id/lti_registrations`

Create a new LTI Registration, as well as an associated Tool Configuration, Developer Key, and Registration Account binding. To install/create using Dynamic Registration, please use the [Dynamic Registration API](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.registration).

**Request Parameters:**

The name of the tool. If one isn’t provided, it will be inferred from the configuration’s title.

A friendly nickname set by admins to override the tool name

A description of the tool. Cannot exceed 2048 bytes.

- Required, Lti::ToolConfiguration

<!--THE END-->

- Lti::Overlay
  
  The overlay configuration for the tool. Overrides values in the base configuration.

The unique identifier for the tool, used for analytics. If not provided, one will be generated.

The desired state for this registration/account binding. “allow” is only valid for Site Admin registrations. Defaults to “off”.

Allowed values: `on`, `off`, `allow`

**Example Request:**

```
This would create a new LTI Registration, as well as an associated Developer Key
and LTI Tool Configuration.
curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations' \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json" \
    -d '{
          "vendor": "Example",
          "name": "An Example Tool",
          "admin_nickname": "A Great LTI Tool",
          "configuration": {
            "title": "Sample Tool",
            "description": "A sample LTI tool",
            "target_link_uri": "https://example.com/launch",
            "oidc_initiation_url": "https://example.com/oidc",
            "redirect_uris": ["https://example.com/redirect"],
            "scopes": ["https://purl.imsglobal.org/spec/lti-ags/scope/lineitem"],
            "placements": [
              {
                "placement": "course_navigation",
                "enabled": true
              }
            ],
            "launch_settings": {}
          }
        }'
```

Returns a [Lti::Registration](https://developerdocs.instructure.com/services/canvas/resources/lti_registrations#lti::registration) object.

[Lti::RegistrationsController#show\_by\_client\_idarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`GET /api/v1/accounts/:account_id/lti_registration_by_client_id/:client_id`

**Scope:** `url:GET|/api/v1/accounts/:account_id/lti_registration_by_client_id/:client_id`

Returns details about the specified LTI registration, including the configuration and account binding.

**Example Request:**

```
This would return the specified LTI registration
curl -X GET 'https://<canvas>/api/v1/accounts/<account_id>/lti_registration_by_client_id/<client_id>' \
     -H "Authorization: Bearer <token>"
```

Returns a [Lti::Registration](https://developerdocs.instructure.com/services/canvas/resources/lti_registrations#lti::registration) object.

[Lti::RegistrationsController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`PUT /api/v1/accounts/:account_id/lti_registrations/:id`

**Scope:** `url:PUT|/api/v1/accounts/:account_id/lti_registrations/:id`

Update the specified LTI registration with the provided parameters. Note that updating the base tool configuration of a registration that is associated with a Dynamic Registration will return a 422. All other fields can be updated freely.

**Request Parameters:**

The admin-configured friendly display name for the registration

A description of the tool. Cannot exceed 2048 bytes.

- Lti::Overlay
  
  The overlay configuration for the tool. Overrides values in the base configuration. Note that updating the overlay of a registration associated with a Dynamic Registration IS allowed.

The desired state for this registration/account binding. “allow” is only valid for Site Admin registrations.

Allowed values: `on`, `off`, `allow`

A comment explaining why this change was made. Cannot exceed 2000 characters.

**Example Request:**

```
This would update the specified LTI Registration, as well as its associated Developer Key
and LTI Tool Configuration.
curl -X PUT 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>' \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json" \
    -d '{
          "vendor": "Example",
          "name": "An Example Tool",
          "admin_nickname": "A Great LTI Tool",
          "configuration": {
            "title": "Sample Tool",
            "description": "A sample LTI tool",
            "target_link_uri": "https://example.com/launch",
            "oidc_initiation_url": "https://example.com/oidc",
            "redirect_uris": ["https://example.com/redirect"],
            "scopes": ["https://purl.imsglobal.org/spec/lti-ags/scope/lineitem"],
            "placements": [
              {
                "placement": "course_navigation",
                "enabled": true
              }
            ],
            "launch_settings": {}
          }
        }'
```

Returns a [Lti::Registration](https://developerdocs.instructure.com/services/canvas/resources/lti_registrations#lti::registration) object.

[Lti::RegistrationsController#resetarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`PUT /api/v1/accounts/:account_id/lti_registrations/:id/reset`

**Scope:** `url:PUT|/api/v1/accounts/:account_id/lti_registrations/:id/reset`

Reset the specified LTI registration to its default settings in this context. This removes all customizations that were present in the overlay associated with this context.

**Example Request:**

```
This would reset the specified LTI registration to its default settings
curl -X PUT 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>/reset' \
     -H "Authorization: Bearer <token>"
```

Returns a [Lti::Registration](https://developerdocs.instructure.com/services/canvas/resources/lti_registrations#lti::registration) object.

[Lti::RegistrationsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`DELETE /api/v1/accounts/:account_id/lti_registrations/:id`

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/lti_registrations/:id`

Remove the specified LTI registration

**Example Request:**

```
This would delete the specified LTI registration
curl -X DELETE 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>' \
     -H "Authorization: Bearer <token>"
```

Returns a [Lti::Registration](https://developerdocs.instructure.com/services/canvas/resources/lti_registrations#lti::registration) object.

[Lti::RegistrationsController#bindarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`POST /api/v1/accounts/:account_id/lti_registrations/:id/bind`

**Scope:** `url:POST|/api/v1/accounts/:account_id/lti_registrations/:id/bind`

Enable or disable the specified LTI registration for the specified account. To enable an inherited registration (eg from Site Admin), pass the registration’s global ID.

Only allowed for root accounts.

**Specifics for Site Admin:** “on” enables and locks the registration on for all root accounts. “off” disables and hides the registration for all root accounts. “allow” makes the registration visible to all root accounts, but accounts must bind it to use it.

**Specifics for centrally-managed/federated consortia:** Child root accounts may only bind registrations created in the same account. For parent root account, binding also applies to all child root accounts.

**Request Parameters:**

The desired state for this registration/account binding. “allow” is only valid for Site Admin registrations.

Allowed values: `on`, `off`, `allow`

**Example Request:**

```
This would enable the specified LTI registration for the specified account
curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>/bind' \
     -H "Authorization: Bearer <token>" \
     -H "Content-Type: application/json" \
     -d '{"workflow_state": "on"}'
```

Returns a [Lti::RegistrationAccountBinding](https://developerdocs.instructure.com/services/canvas/resources/lti_registrations#lti::registrationaccountbinding) object.

[Lti::RegistrationsController#context\_searcharrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`GET /api/v1/accounts/:account_id/lti_registrations/:registration_id/deployments/:deployment_id/context_search`

**Scope:** `url:GET|/api/v1/accounts/:account_id/lti_registrations/:registration_id/deployments/:deployment_id/context_search`

This is a utility endpoint used by the Canvas Apps UI and may not serve general use cases.

Search for accounts and courses that match the search term on name, SIS id, or course code. Returns all matching accounts and courses, including those nested in sub-accounts. Returns bare-bones data about each account and course, and only up to 20 of each. Used to populate the search dropdowns when managing LTI registration availability.

**Request Parameters:**

Account ID. If provided, only searches within this account and only returns direct children of this account.

String to search for in account names, SIS ids, or course codes.

**Example Request:**

```
This would search for accounts and courses matching the search term "example"
curl -X GET 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>/deployments/<deployment_id>/context_search?search_term=example' \
     -H "Authorization: Bearer <token>"
```

Returns a [ContextSearchResponse](https://developerdocs.instructure.com/services/canvas/resources/lti_registrations#contextsearchresponse) object.

[Lti::RegistrationsController#overlay\_historyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`GET /api/v1/accounts/:account_id/lti_registrations/:id/overlay_history`

**Scope:** `url:GET|/api/v1/accounts/:account_id/lti_registrations/:id/overlay_history`

Returns the overlay history items for the specified LTI registration.

**Request Parameters:**

The maximum number of history items to return. Defaults to 10. Maximum allowed is 100.

**Example Request:**

```
This would return the overlay history for the specified LTI registration
curl -X GET 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>/overlay_history?limit=50' \
     -H "Authorization: Bearer <token>"
```

Returns a list of [Lti::OverlayVersion](https://developerdocs.instructure.com/services/canvas/resources/lti_registrations#lti::overlayversion) objects.

[Lti::RegistrationsController#historyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`GET /api/v1/accounts/:account_id/lti_registrations/:id/history`

**Scope:** `url:GET|/api/v1/accounts/:account_id/lti_registrations/:id/history`

Returns the history entries for the specified LTI registration. This endpoint provides comprehensive change tracking for all fields associated with the registration, including registration fields, developer key changes, internal configuration changes, and overlay changes. Supports pagination using the ‘page\` and \`per\_page\` parameters. The default page size is 10.

**Example Request:**

```
This would return the history for the specified LTI registration
curl -X GET 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<registration_id>/history' \
     -H "Authorization: Bearer <token>"
```

[Lti::RegistrationsController#show\_registration\_update\_requestarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`GET /api/v1/accounts/:account_id/lti_registrations/:id/update_requests/:update_request_id`

**Scope:** `url:GET|/api/v1/accounts/:account_id/lti_registrations/:id/update_requests/:update_request_id`

Retrieves details about a specific registration update request.

**Request Parameters:**

The id of the registration.

The id of the registration update request to retrieve.

**Example Request:**

```
curl 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/<id>/update_requests/<update_request_id>' \
     -H "Authorization: Bearer <token>"
```

[Lti::RegistrationsController#apply\_registration\_update\_requestarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/registrations_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`PUT /api/v1/accounts/:account_id/lti_registrations/:id/update_requests/:update_request_id/apply`

**Scope:** `url:PUT|/api/v1/accounts/:account_id/lti_registrations/:id/update_requests/:update_request_id/apply`

Applies a registration update request to an existing registration, replacing the existing configuration and overlay with the new values. If the request is rejected, marks it as rejected without applying changes.

**Request Parameters:**

The id of the registration to update.

The id of the registration update request to apply.

Whether to accept (true) or reject (false) the registration update request.

Optional overlay data to apply on top of the new configuration.

Optional comment explaining the reason for applying this update.

**Example Request:**

```
curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/lti_registrations/configuration/validate' \
     -d '{"overlay": <LtiConfigurationOverlay>, "accepted": boolean}' \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <token>"
```

Returns a [Lti::Registration](https://developerdocs.instructure.com/services/canvas/resources/lti_registrations#lti::registration) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).