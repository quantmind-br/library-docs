---
title: Navigation | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.navigation_tools
source: sitemap
fetched_at: 2026-02-15T09:01:09.61157-03:00
rendered_js: false
word_count: 2245
summary: This document explains how to configure and deploy External Tools using LTI within the Canvas course navigation menu, detailing specific parameters for visibility, display types, and technical implementation for different LTI versions.
tags:
    - canvas-lms
    - lti-integration
    - course-navigation
    - external-tools
    - lti-1-3
    - configuration-settings
    - lti-placement
category: configuration
---

Canvas allows External Tools to be surfaced in a variety of navigation menus. The primary use case for using a navigation placement is to permit SSO to display a dashboard of some type. The Top Navigation placement launches in a drawer which allows the tool to be displayed alongside Canvas content.

## Course Navigation Placement

External tools can be configured to appear as links in course-level navigation. If the tool is configured on an account, any course in that account or any of its sub-accounts will have the link added to the course navigation by default. If the tool is configured in a course, then the navigation will only appear in that course.

There are some additional parameters that can be set on course navigation tools to define default behavior. These settings allow the tool to be disabled by default or visible only to some types of users.

Configuration of the Course Navigation Placement depends on the LTI version.

*Via JSON (LTI 1.3)*

```
{
"title":"Cool Course Navigation Tool ",
"scopes":[],
"extensions":[
{
"domain":"coursenavexample.com",
"tool_id":"course-nav",
"platform":"canvas.instructure.com",
"settings":{
"text":"Cool Course Navigation Tool Text",
"icon_url":"https://some.icon.url",
"placements":[
{
"text":"Cool App Dashboard",
"enabled":true,
"icon_url":"https://some.icon.url",
"placement":"course_navigation",
"message_type":"LtiResourceLinkRequest",
"target_link_uri":"https://your.target_link_uri/your_dashboard"
}
]
}
}
],
"public_jwk":{
"kty":"RSA",
"alg":"RS256",
"e":"AQAB",
"kid":"8f796169-0ac4-48a3-a202-fa4f3d814fcd",
"n":"nZD7QWmIwj-3N_RZ1qJjX6CdibU87y2l02yMay4KunambalP9g0fU9yZLwLX9WYJINcXZDUf6QeZ-SSbblET-h8Q4OvfSQ7iuu0WqcvBGy8M0qoZ7I-NiChw8dyybMJHgpiP_AyxpCQnp3bQ6829kb3fopbb4cAkOilwVRBYPhRLboXma0cwcllJHPLvMp1oGa7Ad8osmmJhXhM9qdFFASg_OCQdPnYVzp8gOFeOGwlXfSFEgt5vgeU25E-ycUOREcnP7BnMUk7wpwYqlE537LWGOV5z_1Dqcqc9LmN-z4HmNV7b23QZW4_mzKIOY4IqjmnUGgLU9ycFj5YGDCts7Q",
"use":"sig"
},
"description":"1.3 Test Tool",
"target_link_uri":"https://your.target_link_uri",
"oidc_initiation_url":"https://your.oidc_initiation_url"
}
```

*Via XML (LTI 1.0-1.2)*

```
<?xml version="1.0" encoding="UTF-8"?>
<cartridge_basiclti_link xmlns="http://www.imsglobal.org/xsd/imslticc_v1p0"
    xmlns:blti = "http://www.imsglobal.org/xsd/imsbasiclti_v1p0"
    xmlns:lticm ="http://www.imsglobal.org/xsd/imslticm_v1p0"
    xmlns:lticp ="http://www.imsglobal.org/xsd/imslticp_v1p0"
    xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation = "http://www.imsglobal.org/xsd/imslticc_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticc_v1p0.xsd
    http://www.imsglobal.org/xsd/imsbasiclti_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imsbasiclti_v1p0.xsd
    http://www.imsglobal.org/xsd/imslticm_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticm_v1p0.xsd
    http://www.imsglobal.org/xsd/imslticp_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticp_v1p0.xsd">
    <blti:launch_url>https://example.com/attendance</blti:launch_url>
    <blti:title>Attendance</blti:title>
    <blti:description>Provides an interactive seating chart and attendance tool</blti:description>
    <blti:extensions platform="canvas.instructure.com">
      <lticm:property name="privacy_level">public</lticm:property>
      <lticm:options name="course_navigation">
        <lticm:property name="enabled">true</lticm:property>
      </lticm:options>
    </blti:extensions>
</cartridge_basiclti_link>
```

For more examples, refer to the [Configuring](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.lti_dev_key_config) documentation.

The Course Navigation Placement is well suited for external apps that wish to be surfaced in Canvas without having to implement an LTI deep linking workflow. Once the tool is configured, no additional steps are required for users to see the launch point (unless the tool is disabled by default). It is well suited for tools that want to provide a simple SSO connection from Canvas to the external application. A dashboard type experience can be provided by apps offering services like:

- Course-level Analytics or tool settings
- Management of external course resources
- Allowing users to select multiple resources and generate line items for them (LTI Advantage tools only)
- Allowing teachers or students to complete an [OAuth2 flow](https://developerdocs.instructure.com/services/canvas/oauth2/file.oauth#accessing-canvas-api) so a tool can run API requests on their behalf.

<!--THE END-->

- Canvas does not support Deep Linking from this placement, however, Assignment and Grading Services could be used to generate many line items in Canvas.
- There is no 'resource' context, only course context.

<!--THE END-->

1. After configuring a course navigation tool, the instructor or student navigates to their course in Canvas.
2. Then, they click a link in the course navigation menu.
3. The tool consumes the LTI launch and renders the application.

If the tool is disabled by default, the instructor must first [organize the navigation tabsarrow-up-right](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-manage-Course-Navigation-links/ta-p/1020) to surface the LTI launch point.

All of these settings are contained under "course\_navigation"

- url: &lt;url&gt; (optional)
  
  This is the URL that will be POSTed to when users click the left tab. It can be the same as the tool's URL, or something different. Domain and URL matching are not enforced for course navigation links. In order to prevent security warnings for users, it is recommended that this URL be over SSL (https). This is required if a url is not set on the main tool configuration.
- default: 'enabled', 'disabled' (optional, 'enabled' by default)
  
  This specifies whether the link is turned on or off by default for courses. Course administrators will see the link appear in Settings just like any other link, and can explicitly order, enable and disable the link from there.
- visibility: 'public', 'members', 'admins' (optional, 'public' by default)
  
  This specifies what types of users will see the link in the course navigation. "public" means anyone accessing the course, "members" means only users enrolled in the course, and "admins" means only Teachers, TAs, Designers and account admins will see the link.
- text: &lt;text&gt; (optional)
  
  This is the default text that will be shown in the left hand navigation as the text of the link. This can be overridden by language-specific settings if desired by using the labels setting. This is required if a text value is not set on the main tool configuration.
- labels: &lt;set of locale-label pairs&gt; (optional)
  
  This can be used to specify different label names for different locales. For example, if an institution supports both English and Spanish interfaces, the text in the link should change depending on the language being displayed. This option lets you support multiple languages for a single tool.
- enabled: &lt;boolean&gt; (required)
  
  Whether to enable this selection feature.
- display\_type &lt;text&gt; (optional)
  
  The layout type to use when launching the tool. Must be one of the following:
  
  - default
    
    Includes Canvas global navigation, breadcrumb, and course navigation.
  - full\_width
    
    Includes Canvas global navigation but does not include breadcrumb or course navigation.
  - full\_width\_in\_context
    
    Includes Canvas global\_navigation, breadcrumb, and course navigation, and gives the tool access to the rest of the horizontal screen width.
  - full\_width\_with\_nav
    
    Includes Canvas global\_navigation, breadcrumb, and course navigation, and gives the tool access to the rest of the horizontal screen width.
  - in\_nav\_context
    
    Includes Canvas global\_navigation, breadcrumbs, and course navigation.
  - borderless
    
    Does not include Canvas global\_navigation, course navigation, or breadcrumbs.
- windowTarget: \_blank (optional)
  
  When set to \_blank, the windowTarget property allows you to configure a launch to happen in a new tab instead of in an iframe. Omit this if you want to launch in frame.

External tools can also be configured to appear as links in account-level navigation. If the tool is configured on an account, administrators in that account and any of its sub-accounts will see the link in their account navigation.

Refer to the [Course Navigation Placement's](https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.navigation_tools#course_navigation) configuring section and simply replace **course\_navigation** with **account\_navigation**.

Once configured, the account\_navigation placement surfaces the LTI launch point in the account/sub-account navigation menu. This placement works well for:

- Account-level reporting and analytics tools
- Management of account-level tool resources or settings
- Allowing admins to complete an [OAuth2 flow](https://developerdocs.instructure.com/services/canvas/oauth2/file.oauth#accessing-canvas-api) so a tool can run API requests on their behalf.

<!--THE END-->

- This placement does not provide any course or resource level context in the Launch.
- This is primarily a one-way launch; returning data to Canvas requires using Canvas API.

<!--THE END-->

1. After configuring an account navigation tool, the admin navigates to the account.
2. Then, they click the LTI link in the account navigation menu.
3. The tool consumes the LTI launch and renders the application.

All of these settings are contained under "account\_navigation"

- url: &lt;url&gt; (optional)
  
  This is the URL that will be POSTed to when users click the left tab. It can be the same as the tool's URL, or something different. Domain and URL matching are not enforced for account navigation links. In order to prevent security warnings for users, it is recommended that this URL be over SSL (https). This is required if a url is not set on the main tool configuration.
- text: &lt;text&gt; (optional)
  
  This is the default text that will be shown in the left-hand navigation as the text of the link. This can be overridden by language-specific settings if desired by using the labels setting. This is required if a text value is not set on the main tool configuration.
- labels: &lt;set of locale-label pairs&gt; (optional)
  
  This can be used to specify different label names for different locales. For example, if an institution supports both English and Spanish interfaces, the text in the link should change depending on the language being displayed. This option lets you support multiple languages for a single tool.
- enabled: &lt;boolean&gt; (required)
  
  Whether to enable this selection feature.
- display\_type &lt;text&gt; (optional)
  
  The layout type to use when launching the tool. Must be one of the following:
  
  - default
    
    Includes Canvas global navigation, breadcrumb, and account navigation.
  - full\_width
    
    Includes Canvas global navigation but does not include breadcrumb or account navigation. This is the default and recommended display type for global navigation.
  - full\_width\_in\_context
    
    Includes Canvas global navigation, breadcrumb, and account navigation, and gives the tool access to the rest of the horizontal screen width.
  - full\_width\_with\_nav
    
    Includes Canvas global navigation, breadcrumb, and account navigation, and gives the tool access to the rest of the horizontal screen width.
  - in\_nav\_context
    
    Includes Canvas global navigation, breadcrumbs, and course navigation.
  - borderless
    
    Does not include Canvas global navigation, account navigation, or breadcrumbs.
- windowTarget: \_blank (optional)
  
  When set to \_blank, the windowTarget property allows you to configure a launch to happen in a new tab instead of in an iframe. Omit this if you want to launch in frame.
- root\_account\_only: &lt;boolean&gt; (optional)
  
  If set to true, the tool will not be shown in the account navigation for subaccounts. Defaults to false (show in root account and all subaccounts).

External tools can also be configured to appear as links in user-level navigation. If the tool is configured on a root account, all users logged in to that account will see the link in their profile navigation by default.

Refer to the [Course Navigation Placement's](https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.navigation_tools#course_navigation) configuring section and simply replace **course\_navigation** with **user\_navigation**.

User navigation links will only work if they are configured at the **root account level**.

Once configured, the user\_navigation placement surfaces the LTI launch point in the users "Account" slide-out tray. This placement works well for:

- Management of user-level resources in an external application
- User-level analytics or tool settings
- Allowing users to complete an [OAuth2 flow](https://developerdocs.instructure.com/services/canvas/oauth2/file.oauth#accessing-canvas-api) so a tool can run API requests on their behalf.

<!--THE END-->

- This placement does not provide any course or resource level context in the Launch.
- This is primarily a one-way launch. Returning data to Canvas requires using Canvas API.

<!--THE END-->

1. After configuring, the user clicks on the "Account" icon from the global navigation side-bar.
2. Then, they click the LTI link in the tray that slides out.
3. The tool consumes the LTI launch and renders their application.

All of these settings are contained under "user\_navigation"

- url: &lt;url&gt; (optional)
  
  This is the URL that will be POSTed to when users click the left tab. It can be the same as the tool's URL, or something different. Domain and URL matching are not enforced for user navigation links. In order to prevent security warnings for users, it is recommended that this URL be over SSL (https). This is required if a url is not set on the main tool configuration.
- text: &lt;text&gt; (optional)
  
  This is the default text that will be shown in the left hand navigation as the text of the link. This can be overridden by language-specific settings if desired by using the labels setting. This is required if a text value is not set on the main tool configuration.
- labels: &lt;set of locale-label pairs&gt; (optional)
  
  This can be used to specify different label names for different locales. For example, if an institution supports both English and Spanish interfaces, the text in the link should change depending on the language being displayed. This option lets you support multiple languages for a single tool.
- enabled: &lt;boolean&gt; (required)
  
  Whether to enable this selection feature.
- visibility: 'public', 'members', 'admins' (optional, 'public' by default)
  
  This specifies what types of users will see the link in the user navigation. "public" and "members" means anyone will see it, and "admins" means only account admins will see the link.
- windowTarget: \_blank (optional)
  
  When set to \_blank, the windowTarget property allows you to configure a launch to happen in a new tab instead of in an iframe. Omit this if you want to launch in frame.

External tools can be configured to appear in the Top Navigation menu and will launch in a drawer alongside the Canvas content. A preview of this can be seen in [Placements Overview](https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.placements_overview).

To use the top navigation placement, the following requirements must be met:

- The feature flag top\_navigation\_placement needs to be enabled.
- The tool is configured with a placement entry for top\_navigation.

The tool will then show up in the Top Navigation tool menu with both the icon\_url and text properties. If no icon\_url is provided, a default icon generated from the first letter of the tool title will be used instead. Up to two tools can also be "pinned" which promotes them from the Tool Menu to a dedicated button (icon only) alongside the menu. This pinning is done per Account and can be managed by a user with manage tools permission in the Apps tab of the account settings.

All of these settings are present for the **top\_navigation** placement:

- url: &lt;url&gt; (required if not set on main tool configuration)
  
  This is the URL that will be POSTed to when users click the launch button. It can be the same as the tool's URL, or something different. Domain and URL matching are not enforced for top\_navigation launches. In order to prevent security warnings for users, it is recommended that URLs be over SSL (https). This setting is required if a url is not set on the main tool configuration.
- text: &lt;text&gt; (required if not set on main tool configuration)
  
  This is the default text that will be shown on the hover-over tip and menu entry.
- icon\_url &lt;url&gt; (optional)
  
  The URL for an icon that identifies your tool in the toolbar. The icon will be shown at 16x16 pixels. It is recommended that this icon be in PNG or SVG format. The url must be an https (SSL) URL.
  
  If a tool does not provide an icon\_url on the, a default icon based on the first letter of the tool's name will be used.
- selection\_width: &lt;pixels&gt; (optional)
  
  This currently has no effect as the Drawer size is a fixed width of 320px.
- selection\_height: &lt;pixels&gt; (optional)
  
  This currently has no effect as the Drawer height is fixed to the available space of the browser viewport minus the tool title header and close button.
- allow\_fullscreen: &lt;boolean&gt; (optional)
  
  This setting controls whether the tool is allowed to enter fullscreen mode. If not set, the tool will not be able to enter fullscreen.

We have also introduced two new postMessage functions to enhance the Top Navigation placement. The first, **lti.getPageContent**, allows an LTI tool to request the content of the current page, providing valuable context data directly from the front end without the need for a REST API call. The second, **lti.getPageSettings**, returns an object containing locale, timezone, and theme information, enabling tools to match Canvas's appearance for improved accessibility and cohesion.

Currently, only `Assignments` and `Wiki Pages` are supported by getPageContent, but support for additional pages is planned. Further documentation for making use of Canvas Post Message functions is located in the Using window.postMessage in LTI Tools section of the Canvas REST API and Extensions Documentation.

**Security**

To control access to the **lti.getPageContent** postMessage function, we have introduced a new LTI scope `https://canvas.instructure.com/lti/page_content/show`, tools without this scope will not be able to invoke the postMessage function.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).