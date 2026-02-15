---
title: Link Selection (Modules) | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.link_selection_placement
source: sitemap
fetched_at: 2026-02-15T09:13:43.052761-03:00
rendered_js: false
word_count: 776
summary: This document explains how to configure the link_selection placement for LTI tools in Canvas, enabling course designers to add non-graded external resources to modules via deep linking.
tags:
    - lti
    - canvas-lms
    - link-selection
    - external-tools
    - deep-linking
    - module-items
    - lti-configuration
category: configuration
---

External tools can be configured to be selectable as an LTI resource link during **module item** creation. The **link\_selection** placement allows course designers (Admins/Instructors) to use the [LTI Deep Linking](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.content_item) flow to select an LTI resource from an external tool and associate it with a Canvas module item.

Note: This placement is enabled by default in Canvas for LTI 1.1. It can be removed by using the `not_selectable` configuration option (see [External Tools API](https://developerdocs.instructure.com/services/canvas/resources/external_tools)). For LTI 1.3, the placement will only be enabled if listed in the `placements` in the JSON configuration.

For configuration examples and links to the specification, please refer to the [LTI Deep Linking documentation](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.content_item). Simply replace the **assignment\_selection** text with **link\_selection** in the XML (LTI 1.0, 1.1, and 1.2) or JSON (LTI 1.3) examples.

- Course designers can create non-graded LTI resources as organized links in Canvas modules.
- Students can view non-graded LTI resources without leaving Canvas.

<!--THE END-->

- Tools must create a UI allowing the course designer to either select existing LTI resources or create them on-the-fly.
- Only one LTI resource can be returned at a time.
- Tools **cannot synchronize grades and submissions** back to the course gradebook by leveraging [LTI grading services](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.assignment_tools). Tools that want this capability should use the

[assignment\_selection placement](https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.assignment_selection_placement) instead.

A user must be allowed to create Canvas module items and the tool must be configured to use the link\_selection placement. While tools *can* be configured to use link\_selection without deep linking, the workflow described here applies to tools that leverage deep linking *with* the link\_selection placement. If a tool does not leverage deep linking, Canvas uses the URL configured at the tool-level or placement-level every time the tool is selected in step 2 below.

During [module item creationarrow-up-right](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-add-an-external-URL-as-a-module-item/ta-p/967):

1. the user can select "External Tool" from the **Add** dropdown.
2. They then choose the tool they want to select content from.
3. Canvas then performs a Deep Linking launch request (if configured) to the tool and the user is presented with a tool-side UI to select or create a single LTI resource.
4. The tool then returns the LTI deep linking message back to Canvas with a URL for the LTI resource. Usually this message contains a URL with resource identifiers in the url.
5. When students view the module item, Canvas launches to the URL returned by the tool.
6. If a resource identifier was provided in Step 4, then the tool will receive this in the launch and be able to render the correct resource.

All of these settings are contained for the **link\_selection** placement:

- url: &lt;url&gt; (optional)
  
  This is the URL that will be POSTed to when users click selects the tool from the module item creation view. It can be the same as the tool's URL, something different. Domain and URL matching are not enforced for link\_selection launches; however, if LTI links are returned, Domain and URL matching is enforced. In order to prevent security warnings for users, it is recommended that URLs be over SSL (https). This setting is required if a url is not set on the main tool configuration.
- text: &lt;text&gt; (optional)
  
  This is the default text that will be shown on in the tool selection menu. This can be overridden by language-specific settings if desired by using the labels setting. This is required if a text value is not set on the main tool configuration.
- labels: &lt;set of locale-label pairs&gt; (optional)
  
  This can be used to specify different label names for different locales. For example, if an institution supports both English and Spanish interfaces, the text for the hover-over tip should change depending on the language being displayed. This option lets you support multiple languages for a single tool.
- enabled: &lt;boolean&gt; (required)
  
  Whether to enable this selection feature.
- message\_type: &lt;an IMS LTI message type&gt; (optional)
  
  Sets the message\_type to be sent during the LTI launch. It is expected that the tool use this to determine if a Deep Linking flow is being requested by Canvas and present an appropriate UI. A Deep Linking flow is highly recommended for this placement, but is not required. See the [Deep Linking documentation](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.content_item) for more information, including accepted values.
- selection\_width: &lt;pixels&gt; (optional)
  
  This sets the width (px) of the selection launch modal. Canvas may set a maximum or minimum width that overrides this option.
- selection\_height: &lt;pixels&gt; (optional)
  
  This sets the height (px) of the selection launch modal. Canvas may set a maximum or minimum height that overrides this option.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).