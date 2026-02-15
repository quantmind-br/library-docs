---
title: Migration Selection | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.migration_selection_placement
source: sitemap
fetched_at: 2026-02-15T09:13:32.95027-03:00
rendered_js: false
word_count: 666
summary: This document explains how to configure the migration selection placement for external tools to facilitate course content imports using LTI Deep Linking and Common Cartridge files.
tags:
    - canvas-lms
    - lti-deep-linking
    - migration-selection
    - course-import
    - common-cartridge
    - external-tools
category: configuration
---

## Migration Selection Placement

External tools can be configured to appear in the "Course Imports" menu of a course. The **migration\_selection** placement allows course designers (Admins/Instructors) to use the [LTI Deep Linking](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.content_item) flow to select a Common Cartridge file from an external tool and import it into a course.

For configuration examples and links to the specification, please refer to the [LTI Deep Linking documentation](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.content_item). Simply replace the **assignment\_selection** text with **migration\_selection** in the XML (LTI 1.0, 1.1, and 1.2) or JSON (LTI 1.3) examples.

- Tools can import large quantities and types of content into the Canvas.
- Tools, particularly content publishers, can provide a custom UI that allows course designers to currate content on the tool side before importing.

<!--THE END-->

- Tools must create a UI allowing the designer to either select existing cartridges or select content and generate common cartridge files on-the-fly.
- Tools must provide a download URL that is reachable by Canvas.

A user must have the **Course Content - add / edit / delete** permission. From the course settings page, the user can click on the **Import Course Content** button on the right sidebar. In the **Content Type** dropdown, any tool with the **migration\_selection** placement will appear. After selecting the tool, the user can click the **Find Course** button. When clicked, Canvas initiates an LTI launch to the tool and indicates that a deep linking selection request is happening. The tool can then present the user with a UI (specifcally an iframe in a modal) to select and/or create common cartridge files and return a file download url to Canvas. The user then has the option to select all of the content or select just some. When the **Import** button is clicked, Canvas downloads the file from the url, and initiates a course import process using the file provided by the tool.

All of these settings are contained for the **migration\_selection** placement:

- url: &lt;url&gt; (optional)
  
  This is the URL that will be POSTed to when users click the **Find Course** button. It can be the same as the tool's URL, or something different. Domain and URL matching are not enforced for migration\_selection launches; however, if LTI links are returned, Domain and URL matching is enforced. In order to prevent security warnings for users, it is recommended that URLs be over SSL (https). This setting is required if a url is not set on the main tool configuration.
- text: &lt;text&gt; (optional)
  
  This is the default text that will be shown on in the **Content Type** menu. This can be overridden by language-specific settings if desired by using the labels setting. This is required if a text value is not set on the main tool configuration.
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