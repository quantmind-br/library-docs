---
title: Editor Button | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.editor_button_placement
source: sitemap
fetched_at: 2026-02-15T09:13:30.082357-03:00
rendered_js: false
word_count: 878
summary: This document explains how to configure and use the editor_button placement for LTI external tools to enable deep linking and content embedding within the Canvas Rich Content Editor.
tags:
    - canvas-lms
    - lti-integration
    - rich-content-editor
    - deep-linking
    - external-tools
    - editor-button
category: configuration
---

External tools can be configured to appear as buttons in the rich content editor. The **editor\_button** placement allows many users to use the [LTI Deep Linking](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.content_item) flow to select resources from an external tool and embed them in the [Canvas Rich Content Editorarrow-up-right](https://community.canvaslms.com/t5/Canvas-Basics-Guide/What-is-the-New-Rich-Content-Editor/ta-p/12) (RCE).

For configuration examples and links to the specification, please refer to the [LTI Deep Linking documentation](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.content_item). Simply replace the **assignment\_selection** text with **editor\_button** in the XML (LTI 1.0, 1.1, and 1.2) or JSON (LTI 1.3) examples.

- Tools can embed different content types (images, text/html, LTI Launch URLs, basic URLs).
- Tools can determine the presentation style and size of the content.
- Tools can return an array of different content types in a single message.
- Many different types of users can access the RCE from many different locations such as assignment descriptions, discussions posts, and wiki pages.

<!--THE END-->

- Requires UI interactions to generate content. To generate content server-to-server, use of [Canvas API](https://developerdocs.instructure.com/services/canvas/oauth2/file.oauth#accessing-canvas-api) is required.

<!--THE END-->

1. A user loads a page that has the RCE available (discussion posts, quiz questions, etc.).
2. Once loaded, tools that use the **editor\_button** placement will appear in the tool bar of the RCE.
3. When the tool bar button is clicked, Canvas initiates an LTI launch to the tool and indicates that a deep linking selection request is happening.
4. The tool can then present the user with a UI to select and/or create content and return items of different types to Canvas.
5. Canvas then consumes the request and converts the payload to HTML in the RCE.
6. Once published, the audience can then view the content returned by the tool.

The end result is users can search for embeddable content from a tool provider and submit it back to the RCE without having to leave Canvas or paste embed code!

**Pro-tip:** Use the com.instructure.Editor.contents and/or com.instructure.Editor.selection [variable substitutions](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.tools_variable_substitutions) to include the full RCE contents and/or highlighted selection, respectively, in the launch request.

All of these settings are contained for the **editor\_button** placement:

- url: &lt;url&gt; (required if not set on main tool configuration)
  
  This is the URL that will be POSTed to when users click the left tab. It can be the same as the tool's URL, or something different. Domain and URL matching are not enforced for editor\_button launches; however, if LTI links are returned, Domain and URL matching is enforced. In order to prevent security warnings for users, it is recommended that URLs be over SSL (https). This setting is required if a url is not set on the main tool configuration.
- text: &lt;text&gt; (required if not set on main tool configuration)
  
  This is the default text that will be shown on the hover-over tip for the RCE button. This can be overridden by language-specific settings if desired by using the labels setting. This is required if a text value is not set on the main tool configuration.
- icon\_url &lt;url&gt; (optional)
  
  The URL for an icon that identifies your tool in the RCE toolbar. The icon will be shown at 16x16 pixels in the editor toolbar, and at 28x28 pixels in the editor's listing of all tools. It is recommended that this icon be in PNG or SVG format. The url must be an https (SSL) URL.
  
  After April 2024, if a tool does not provide an icon\_url on the editor\_button placement or the main tool configuration, a default icon based on the first letter of the tool's name will be used. Before this change, if a tool does not provide an icon\_url, the editor\_button placement will be removed from the tool's install configuration, and the tool will not be shown in the editor\_button placement.
- labels: &lt;set of locale-label pairs&gt; (optional)
  
  This can be used to specify different label names for different locales. For example, if an institution supports both English and Spanish interfaces, the text for the hover-over tip should change depending on the language being displayed. This option lets you support multiple languages for a single tool.
- enabled: &lt;boolean&gt; (optional)
  
  Whether to enable this selection feature; this setting defaults to enabled if omitted.
- message\_type: &lt;an IMS LTI message type&gt; (optional)
  
  Sets the message\_type to be sent during the LTI launch. It is expected that the tool use this to determine if a Deep Linking flow is being requested by Canvas and present an appropriate UI. A Deep Linking flow is highly recommended for this placement, but is not required. See the [Deep Linking documentation](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.content_item) for more information, including accepted values.
- selection\_width: &lt;pixels&gt; (optional)
  
  This sets the width (px) of the selection launch modal. Canvas may set a maximum or minimum width that overrides this option.
- selection\_height: &lt;pixels&gt; (optional)
  
  This sets the height (px) of the selection launch modal. Canvas may set a maximum or minimum height that overrides this option.
- visibility: 'public', 'members', 'admins' (optional, 'public' by default)
  
  This specifies what types of users will see the link in the editor. "public" means anyone accessing the course, "members" means only users enrolled in the course, and "admins" means only Teachers, TAs, Designers and account admins will see the link.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).