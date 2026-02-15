---
title: Configuring | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.lti_dev_key_config
source: sitemap
fetched_at: 2026-02-15T08:57:45.090427-03:00
rendered_js: false
word_count: 2005
summary: This document outlines the necessary configuration steps for LTI Advantage Tools in Canvas, covering authentication endpoints, developer keys, and JSON configuration structures.
tags:
    - lti-advantage
    - canvas-lms
    - developer-keys
    - openid-connect
    - json-configuration
    - external-tools
category: configuration
---

For a successful launch to occur, LTI Advantage Tools require configuration on both Canvas and inside the tool:

## Overview of an LTI Launch

This section has moved to the [LTI Launch Overview page](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.lti_launch_overview).

Tools will need to be aware of some Canvas-specific settings in order to accept a launch from Canvas and use the LTI Advantage Services:

- **Canvas Public JWKs**: When the tool receives the authentication response ([Step 3](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.lti_launch_overview#step-3)), tools must [validate that the request is actually coming from Canvasarrow-up-right](http://www.imsglobal.org/spec/security/v1p0/#authentication-response-validation). Canvas' public keys are environment-specific, but not domain-specific (the same key set can be used across all client accounts):
  
  - Production: `https://sso.canvaslms.com/api/lti/security/jwks`
  - Beta: `https://sso.beta.canvaslms.com/api/lti/security/jwks`
  - Test: `https://sso.test.canvaslms.com/api/lti/security/jwks`
    
    **Note:** The domain for this endpoint used to be `https://canvas.instructure.com`. The impetus for this change and other exact details are described in [this Canvas Community articlearrow-up-right](https://community.canvaslms.com/t5/The-Product-Blog/Minor-LTI-1-3-Changes-New-OIDC-Auth-Endpoint-Support-for/ba-p/551677). Tools wishing to implement the Platform Storage spec are required to use the new domain for this endpoint, and all other tools should update this endpoint in their configuration store as soon as possible. This change will eventually be enforced, but for now is not a breaking change - the old domain will continue to work. Any questions or issues are either addressed in the linked article or can be filed as a standard support/partner support case, referencing the OIDC Auth endpoint change.
- **Authorization Redirect URL**: The values and use of this are described in [Step 2](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.lti_launch_overview#step-2). Since the URL is static, you will want to configure this in your tool. Tools that wish to utilize [Step 1.5](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.lti_launch_overview#login-redirect) need to include *all* possible redirect URLs here.
- **Deployment ID**: The `deployment_id` can be optionally configured in the tool. A single developer key may have many deployments, so the deployment ID can be used to identify which deployment is being launched. For more, refer to the LTI 1.3 core specification, [section 4.1.2arrow-up-right](https://www.imsglobal.org/spec/lti/v1p3/#lti_deployment_id-login-parameter). The `deployment_id` in Canvas is exposed after a tool has been [deployed using the `client_id`arrow-up-right](https://community.canvaslms.com/t5/Admin-Guide/How-do-I-configure-an-external-app-for-an-account-using-a-client/ta-p/202).

## Configuring the Tool in Canvas

With LTI Advantage, Canvas moved to using Developer Keys to store tool configuration information. After a developer key is [created and enabledarrow-up-right](https://community.canvaslms.com/t5/Admin-Guide/How-do-I-configure-an-LTI-key-for-an-account/ta-p/140), tools can be deployed to [accounts/sub-accountsarrow-up-right](https://community.canvaslms.com/t5/Admin-Guide/How-do-I-configure-an-external-app-for-an-account-using-a-client/ta-p/202) or [coursesarrow-up-right](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-configure-an-external-app-for-a-course-using-a-client/ta-p/1071).

Developer Keys allow tools to set the required parameters to complete the [OpenID Connect Launch Flowarrow-up-right](https://www.imsglobal.org/spec/security/v1p0#openid_connect_launch_flow), leverage [LTI Advantage Services](https://developerdocs.instructure.com/services/canvas/oauth2/file.oauth#accessing-lti-advantage-services), and configure other important settings.

With guidance from the tool developer, developer keys settings can be manually entered by Account Admins. Tools providers can also supply Account Admins with a JSON configuration or configuration URL containing the settings the tool provider has verified to work.

In the manual case, since many of the extensions listed here require more than a few lines of configuration, there is not currently an interface for *every* extension to be manually configured. Instead, we encourage tool providers to expose a set of URL endpoints that return working configuration options for their tool services.

If providing a URL configuration endpoint is not an option, you can also provide your users with raw JSON that they can paste in for configuration.

### Anatomy of a JSON configuration

In this section, an example JSON configuration is shown followed by a table describing the relevance of each field.

**NOTE**: Certain placement-specific settings may not be described here. Some examples of JSON configuration snippets and placement-specific settings are also found in the placements sub-menu in the left-navigation of this documentation.

```
{
  "title": "The Best Tool",
  "description": "1.3 Test Tool used for documentation purposes.",
  "oidc_initiation_url": "https://your.oidc_initiation_url",
  "oidc_initiation_urls": {
    "eu-west-1": "https://your.eu-specific1.oidc_initiation_url",
    "eu-central-1": "https://your.eu-specific2.oidc_initiation_url"
  },
  "target_link_uri": "https://your.target_link_uri",
  "scopes": [
    "https://purl.imsglobal.org/spec/lti-ags/scope/lineitem",
    "https://purl.imsglobal.org/spec/lti-ags/scope/result.readonly"
  ],
  "extensions": [
    {
      "domain": "thebesttool.com",
      "tool_id": "the-best-tool",
      "platform": "canvas.instructure.com",
      "privacy_level": "public",
      "settings": {
        "text": "Launch The Best Tool",
        "labels": {
          "en": "Launch The Best Tool",
          "en-AU": "G'day, Launch The Best Tool",
          "es": "Lanzar la mejor herramienta",
          "zh-Hans": "启动最佳工具"
        },
        "icon_url": "https://some.icon.url/tool-level.png",
        "selection_height": 800,
        "selection_width": 800,
        "placements": [
          {
            "text": "User Navigation Placement",
            "icon_url": "https://some.icon.url/my_dashboard.png",
            "placement": "user_navigation",
            "message_type": "LtiResourceLinkRequest",
            "target_link_uri": "https://your.target_link_uri/my_dashboard",
            "canvas_icon_class": "icon-lti",
            "custom_fields": {
              "foo": "$Canvas.user.id"
            }
          },
          {
            "text": "Editor Button Placement",
            "icon_url": "https://some.icon.url/editor_tool.png",
            "placement": "editor_button",
            "message_type": "LtiDeepLinkingRequest",
            "target_link_uri": "https://your.target_link_uri/content_selector",
            "selection_height": 500,
            "selection_width": 500
          },
          {
            "text": "Course Navigation Placement",
            "icon_url": "https://static.thenounproject.com/png/131630-200.png",
            "placement": "course_navigation",
            "message_type": "LtiResourceLinkRequest",
            "target_link_uri": "https://your.target_link_uri/launch?placement=course_navigation",
            "required_permissions": "manage_calendar",
            "selection_height": 500,
            "selection_width": 500
          }
        ]
      }
    }
  ],
  "public_jwk": {
    "kty": "RSA",
    "alg": "RS256",
    "e": "AQAB",
    "kid": "8f796169-0ac4-48a3-a202-fa4f3d814fcd",
    "n": "nZD7QWmIwj-3N_RZ1qJjX6CdibU87y2l02yMay4KunambalP9g0fU9yZLwLX9WYJINcXZDUf6QeZ-SSbblET-h8Q4OvfSQ7iuu0WqcvBGy8M0qoZ7I-NiChw8dyybMJHgpiP_AyxpCQnp3bQ6829kb3fopbb4cAkOilwVRBYPhRLboXma0cwcllJHPLvMp1oGa7Ad8osmmJhXhM9qdFFASg_OCQdPnYVzp8gOFeOGwlXfSFEgt5vgeU25E-ycUOREcnP7BnMUk7wpwYqlE537LWGOV5z_1Dqcqc9LmN-z4HmNV7b23QZW4_mzKIOY4IqjmnUGgLU9ycFj5YGDCts7Q",
    "use": "sig"
  },
  "custom_fields": {
    "bar": "$Canvas.user.sisid"
  }
}
```

```
<tr class="request-param">
  <td>environments</td>
  <td>
    <strong style="color: red;">Ignored</strong>
  </td>
  <td>JSON object</td>
  <td class="param-desc">
    <p>LTI 1.1 tools <a href="file.tools_xml.md">support environment-specific domains and launch urls</a>, used for launching
    from beta or test instances of Canvas. This config option is not supported for LTI 1.3. Tools instead should use the
    <code>canvas_environment</code> parameter of the OIDC Login request to redirect to environment-specific launch urls or
    instances of the tool, as specified in <a href="file.lti_dev_key_config.md#login-redirect">Step 1.5</a> above, and/or
    use the region-specific <a href="#param-oidc-initial-urls">oidc_initiation_urls</a>.
    </p>
  </td>
</tr>
```

```
<tr class="request-param">
  <td>public_jwk</td>
  <td>
      required, see notes
  </td>
  <td>JSON object</td>
  <td class="param-desc">
```

Required if public\_jwk\_url is omitted. The tools [public keyarrow-up-right](https://www.imsglobal.org/spec/lti/v1p3/impl/#tool-s-jwk-set) to be used during the client\_credentials grant for [accessing LTI Advantage services](https://developerdocs.instructure.com/services/canvas/oauth2/file.oauth#accessing-lti-advantage-services).

The default name of the tool in the app index. This value is also displayed if no "text" field is provided within extension settings or placements.

A description of the tool.

Optional region-specific [login initiation urlsarrow-up-right](https://www.imsglobal.org/spec/security/v1p0#step-1-third-party-initiated-login) that Canvas should redirect the User Agent to. Each institution's Canvas install lives in a particular AWS region, typically one close to the institution's physical region. If this AWS region is listed as a key in this object, the URL in the value will override the default \`oidc\_initiation\_url\`. As of 2023, the regions used by Canvas are: us-east-1, us-west-2, ca-central-1, eu-west-1, eu-central-1, ap-southeast-1, ap-southeast-2.

The [target\_link\_uriarrow-up-right](https://www.imsglobal.org/spec/security/v1p0#step-1-third-party-initiated-login) that Canvas should pass in the to the login initiation endpoint. This allows tools to determine which redirect\_uri to pass Canvas in the authorization redirect request and should be [verified during the final launcharrow-up-right](https://www.imsglobal.org/spec/lti/v1p3/impl#verify-the-target_link_uri). This can be set at the tool-level, or within the "placements" JSON object for placement-specific target\_link\_uri's.

The comma separated list of scopes to be allowed when using the [client\_credentials grant to access LTI services](https://developerdocs.instructure.com/services/canvas/oauth2/file.oauth#accessing-lti-advantage-services).

Allowed values: `"https://purl.imsglobal.org/spec/lti-ags/scope/lineitem"`, `"https://purl.imsglobal.org/spec/lti-ags/scope/result.readonly"`, `"https://purl.imsglobal.org/spec/lti-ags/scope/score"`, `"https://purl.imsglobal.org/spec/lti-nrps/scope/contextmembership.readonly"`, `"https://purl.imsglobal.org/spec/lti-ags/scope/lineitem.readonly"`, `"https://purl.imsglobal.org/spec/lti/scope/noticehandlers"`, `"https://canvas.instructure.com/lti/public_jwk/scope/update"`

The set of Canvas extensions, including placements, that the tool should use. \[See extensions parameters below.](#extension-params)

Custom fields that will be sent to the tool consumer; can be set at the tool-level or within the "placement" JSON object for placement-specific custom fields. When the tool is launched, all custom fields will be sent to the tool as strings. Read more about [variable substitutions in custom fields.](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.tools_variable_substitutions)

The following fields can be put under `extensions`:

The domain Canvas should use to match clicked LTI links against. This is recommended if [deep linking](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.content_item) is used.

Allows tools to set a unique identifier for the tool.

The LMS platform that the extensions belong to. This should always be set to "canvas.instructure.com" for cloud-hosted Canvas.

What level of user information to send to the external tool. Setting this to "name\_only" will include fields that contain the user's name and sourcedid in the launch claims. "email\_only" will include only the user's email. "public" includes all fields from "name\_only", "email\_only", and fields like the user's picture. "anonymous" will not include any of these fields. Note that the "sub" claim containing the user's ID is always included.

Allowed values: `anonymous`, `public` `name_only`, `email_only`

The following can be put under `extensions.settings`:

Custom fields that will be sent to the tool consumer; can be set at the tool-level or within the "placement" JSON object for placement-specific custom fields. When the tool is launched, all custom fields will be sent to the tool as strings. Read more about [variable substitutions in custom fields.](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.tools_variable_substitutions)

The url of the icon to show for this tool. Can be set within the "settings" object for tool-level icons, or in the "placement" object for placement-specific icons. NOTE: Not all placements display an icon.

An object for translations of the "text", used to support internationalization (i18n) / localization (l10n). If the user's Canvas interface is set to one of the languages listed, the tool will display the translated text in place of the value in the "text" field. This JSON object is in the format `{"en": "Name", "es": "Nombre"}`, where "en" and "es" are IETF language tags. More specific locales ("en-AU") are preferred over less specific ones ("en"). A partial list of language tags can be found [herearrow-up-right](https://en.wikipedia.org/wiki/IETF_language_tag#List_of_common_primary_language_subtags). Can be set within "settings" or individual placements.

Settings to be used for specific tool placements. Values given in this `settings.placements` array will override the value given in the \`settings\` object for that particular placement. [See placements parameters below.](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.lti_dev_key_config#placements-params)

Limits tool visibility to users with certain permissions, as defined on the user's built-in Canvas user roles AND the custom roles that you may have created in Canvas. This is a comma-separated string of one or more required permissions, such as `manage_groups_add,manage_groups_delete` or `read_outcomes`. The tool will be hidden for users without all specified permissions. If set in placement-specific settings, that placement will be hidden; if set at the tool-level (e.g. under `extensions[0]`), each of the tool's placements will be hidden. For true access control, please use (instead or in addition) the [Canvas.membership.permissions&lt;&gt;](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.tools_variable_substitutions#Canvas-membership-permissions) custom variable expansion, and check its value in your tool. To learn more about roles and permissions, and to see the permissions available for this parameter, visit the [Roles API docs](https://developerdocs.instructure.com/services/canvas/resources/roles).

The display height of the iframe. This may be ignored or overridden for some LTI placements due to other UI requirements set by Canvas. Tools are advised to experiment with this setting to see what makes the most sense for their application.

The display width of the iframe. This may be ignored or overridden for some LTI placements due to other UI requirements set by Canvas. Tools are advised to experiment with this setting to see what makes the most sense for their application.

The default text to show for this tool. Can be set within "settings" for the tool-level display text, or within "placements" object for placement-specific display text.

The following can be put under `extensions.settings.placements`. (Note: `extensions.settings.placements` is an array of JSON objects. This table shows the values that can be in those JSON objects.) Values given for a placement in this array will override the value given in `extensions.settings`.

Custom fields that will be sent to the tool consumer; can be set at the tool-level or within the "placement" JSON object for placement-specific custom fields. When the tool is launched, all custom fields will be sent to the tool as strings. Read more about [variable substitutions in custom fields.](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.tools_variable_substitutions)

Optional, defaults to \`true\`. Determines if the placement is enabled.

The url of the icon to show for this tool. Can be set within the "settings" object for tool-level icons, or in the "placement" object for placement-specific icons. NOTE: Not all placements display an icon.

An object for translations of the "text", used to support internationalization (i18n) / localization (l10n). If the user's Canvas interface is set to one of the languages listed, the tool will display the translated text in place of the value in the "text" field. This JSON object is in the format `{"en": "Name", "es": "Nombre"}`, where "en" and "es" are IETF language tags. More specific locales ("en-AU") are preferred over less specific ones ("en"). A partial list of language tags can be found [herearrow-up-right](https://en.wikipedia.org/wiki/IETF_language_tag#List_of_common_primary_language_subtags). Can be set within "settings" or individual placements.

The IMS message type to be sent in the launch. This is set at the placement level. Not all placements support both message\_types.

Allowed values: `"LtiResourceLinkRequest"`, `"LtiDeepLinkingRequest"`

Limits tool visibility to users with certain permissions, as defined on the user's built-in Canvas user roles AND the custom roles that you may have created in Canvas. This is a comma-separated string of one or more required permissions, such as `manage_groups_add,manage_groups_delete` or `read_outcomes`. The tool will be hidden for users without all specified permissions. If set in placement-specific settings, that placement will be hidden; if set at the tool-level (e.g. under `extensions[0]`), each of the tool's placements will be hidden. For true access control, please use (instead or in addition) the [Canvas.membership.permissions&lt;&gt;](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.tools_variable_substitutions#Canvas-membership-permissions) custom variable expansion, and check its value in your tool. To learn more about roles and permissions, and to see the permissions available for this parameter, visit the [Roles API docs](https://developerdocs.instructure.com/services/canvas/resources/roles).

The display height of the iframe. This may be ignored or overridden for some LTI placements due to other UI requirements set by Canvas. Tools are advised to experiment with this setting to see what makes the most sense for their application.

The display width of the iframe. This may be ignored or overridden for some LTI placements due to other UI requirements set by Canvas. Tools are advised to experiment with this setting to see what makes the most sense for their application.

The default text to show for this tool. Can be set within "settings" for the tool-level display text, or within "placements" object for placement-specific display text.

#### Placement-specific Settings

The following settings only apply to certain placements.

A comma-separated list of MIME types, e.g.: `"image/jpeg,image/png"`. The LTI tool will be shown in the file\_menu placement if the file's MIME type matches one of the MIME types in the list. [(Screenshot of the file\_menu placement.)](https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.placements_overview#file-menu)

account\_navigation, course\_navigation

Whether the tool should be shown in the sidebar.

Allowed values: `enabled`, `disabled`

An SVG path to be used for the tool's icon in the global\_navigation placement. Note: this should be the SVG path itself, not a URL to an SVG image. The value of this parameter will be used as the `d` attribute on the SVG's `path` element. [See MDN for more information.arrow-up-right](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d)

Whether the tool should open in the tray (a.k.a. sidebar) rather than a modal window. `True` means to use the tray, `false` means to use a modal window. The tray allows the user to still interact with the page while the tray is open; the modal window blocks the rest of the page while the modal window is open.

account\_navigation, course\_navigation, global\_navigation, user\_navigation

Whether the tool should be launched in a new tab.

Allowed values: `_blank`

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 2 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).