---
title: PostMessage | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.lti_window_post_message
source: sitemap
fetched_at: 2026-02-15T08:57:33.399123-03:00
rendered_js: false
word_count: 1902
summary: This document explains how LTI tools integrated with Canvas use the window.postMessage API for inter-frame communication and platform storage. It outlines specific message subjects, security requirements, and implementation patterns for developers.
tags:
    - canvas-lms
    - lti-integration
    - postmessage-api
    - iframe-communication
    - platform-storage
    - javascript
    - inter-window-messaging
category: guide
---

## Using window.postMessage in LTI Tools

Canvas listens for events sent through the `window.postMessage` Javascript API (docs [herearrow-up-right](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)) from LTI tools and other children rendered in iframes or opened in new tabs/windows. Tools can send various types of events to resize windows, launch in new windows, or other functionality. Note that this is not part of the LTI specification, and is Canvas-specific. In addition, these messages are not currently supported by any of the Canvas mobile apps, only the web version of Canvas.

The data sent to `window.postMessage` can be of any type, and each message type looks for different data. Most data is sent as an object with a `subject` property.

Some of these message handlers require the presence of a `token`, which identifies the tool launch. This token is present in the launch as a custom variable, `$com.instructure.PostMessageToken`, and should be passed in postMessage calls if it's present.

**Note: Previous versions of this documentation recommended always sending messages to** `window.top`**.** **This is no longer recommended, as tools should target the parent window they are embedded in.**

If the LTI tool is launched in a iframe, as is most common, then postMessages should be sent to the window embedding the LTI tool (usually accessible by `window.parent`). However, if the tool is launched in a new tab, window, or popup, then postMessages should be directed to `window.opener`. The examples will use `window.parent`, but in practice, the target recipient can sometimes also be `window.opener`.

The LTI Platform Storage messages (`lti.get_data` and `lti.put_data`) should be sent to either the direct parent frame, or to a named frame that will be present in `window.parent.frames`. If this named frame is present, it will be returned in the `lti.capabilities.response` message and also present in the `lti_storage_target` body parameter in the LTI 1.3 Login and Launch requests. This is also defined in the [Platform Storage specarrow-up-right](https://www.imsglobal.org/spec/lti-cs-pm/v0p1#target-frame).

Most message handlers will respond with a postMessage with a subject that matches the intial subject, with `.response` appended. If an error occurs during message handling, the response postMessage will contain an `error` property with a `code` and a `message`.

Sample code for receiving the response messages:

```
window.addEventListener('message',function(event){
  // Process response
})
```

Messages sent by a tool that has been launched from a Canvas mobile app will not receive any response messages.

Responds with a list of subjects that Canvas will respond to, and if necessary the named frame to address each subject to. Part of the LTI Platform Storage spec, defined [herearrow-up-right](https://www.imsglobal.org/spec/lti-cs-pm/v0p1#capabilities-request-postmessage).

**Required properties:**

- subject: "lti.capabilities"

Returning postMessage includes the following properties:

- subject: "lti.capabilities"
- supported\_messages: array of supported message types with these properties:
  
  - subject: the string name of each message type
  - frame: (optional) the named frame on the parent window to which postMessages should be sent

```
window.parent.postMessage({subject: 'lti.capabilities'}, '*')
```

Responds with an html object containing page content. This will contain all markup and children elements of the main content area of the page. Some content may be filtered from this response. The scope `https://canvas.instructure.com/lti/page_content/show` is required to use this functionality. Currently, only `Assignments` and `Wiki Pages` are supported by getPageContent, but support for additional pages is planned.

**Required properties:**

- subject: "lti.getPageContent"

```
window.parent.postMessage({subject: 'lti.getPageContent'}, '*')
```

Returning postMessage includes the following properties:

- subject: "lti.getPageContent"
- pageContent: a string containing HTML

```
{
  subject: 'lti.getPageContent.response',
  content: '<div>...</div>'
}
```

Responds with an object containing page settings. This includes the current locale, time zome, contrast settings, url to the active branding configuration file, and the width of the parent (Canvas) window. This is the same json file url provided by the [Brand Configs API](https://developerdocs.instructure.com/services/canvas/resources/brand_configs).

**Required properties:**

- subject: "lti.getPageSettings"

```
window.parent.postMessage({subject: 'lti.getPageSettings'}, '*')
```

Returning postMessage includes the following properties:

- subject: "lti.getPageSettings"
- pageSettings: an object containing the following keys:
  
  - active\_brand\_config\_json\_url

```
{
  pageSettings: {
    locale: 'en',
    time_zone: 'Etc/UTC',
    use_high_contrast: false,
    active_brand_config_json_url: 'https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/default/variables-7dd4b80918af0e0218ec0229e4bd5873.json',
    window_width: 1024
  }
}
```

Stores the provided `value` at the provided `key` in Canvas's [localstoragearrow-up-right](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage), partitioned by tool. Data stored by one tool cannot be accessed by another, is only stored in the user's browser, and is short-lived. Part of the LTI Platform Storage spec, defined [herearrow-up-right](https://www.imsglobal.org/spec/lti-pm-s/v0p1).

The spec requires that this message's target origin be set to the platform's OIDC Authorization url as defined [here](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.lti_launch_overview#step-2), so that the tool can be certain that Canvas is the entity receiving the message. To enable this feature, Canvas also requires that messages with this target origin are sent to the `post_message_forwarding` frame, which is a sibling frame to the tool. For now, tools are also still allowed to send this message directly to the parent window and use the wildcard `*` origin, although this does not conform to the spec.

Support for this API is signalled using the `lti_storage_target` parameter, which is included in the LTI 1.3 login and launch requests. If this parameter absent, tools should use cookies instead of trying to use this postMessage. The default value for this parameter is `_parent`, which means messages should be sent to `window.parent`. When the value is something else (like `post_message_forwarding`), the tool should send message to the frame with that name present at `window.parent.frames[lti_storage_target]`.

**Note:** When a tool is launched from within an active RCE (Rich Content Editor) this sibling frame may not be available, since the RCE uses an iframe to represent the editor box. If the message sent to this frame using this origin doesn't receive a timely response, the tool should fall back to sending the message to the parent window using the wildcard `*` origin.

**Required properties:**

- key: the string key to store `value` at
- value: the string to store at `key`, or `null` to remove an existing value
- message\_id: any random string value. a UUID is easiest

Returned postMessage includes the following properties:

- subject: "lti.fetchWindowSize.response"
- key: the same key provided in the initial message
- value: the same value provided in the initial message
- message\_id: the same message\_id provided in the initial message

```
window.parent.frames['post_message_forwarding'].postMessage(
  {
    subject: 'lti.put_data',
    key: 'hello',
    value: 'world',
    message_id: '14556a4f-e9af-43f7-bd1f-d3e260d05a9f',
  },
  'http://sso.canvaslms.com'
)
window.parent.postMessage(
  {
    subject: 'lti.put_data',
    key: 'hello',
    value: 'world',
    message_id: '14556a4f-e9af-43f7-bd1f-d3e260d05a9f',
  },
  '*'
)
```

Fetches the value stored at the provided `key` in Canvas's [localstoragearrow-up-right](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage), partitioned by tool. Data stored by one tool cannot be accessed by another, is only stored in the user's browser, and is short-lived. Part of the LTI Platform Storage spec, defined [herearrow-up-right](https://www.imsglobal.org/spec/lti-pm-s/v0p1).

The spec requires that this message's target origin be set to the platform's OIDC Authorization url as defined [here](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.lti_launch_overview#step-2), so that the tool can be certain that Canvas is the entity receiving the message. To enable this feature, Canvas also requires that messages with this target origin are sent to the `post_message_forwarding` frame, which is a sibling frame to the tool. For now, tools are also still allowed to send this message directly to the parent window and use the wildcard `*` origin, although this does not conform to the spec.

Support for this API is signalled using the `lti_storage_target` parameter, which is included in the LTI 1.3 login and launch requests. If this parameter absent, tools should use cookies instead of trying to use this postMessage. The default value for this parameter is `_parent`, which means messages should be sent to `window.parent`. When the value is something else (like `post_message_forwarding`), the tool should send message to the frame with that name present at `window.parent.frames[lti_storage_target]`.

**Note:** When a tool is launched from within an active RCE (Rich Content Editor) this sibling frame may not be available, since the RCE uses an iframe to represent the editor box. If the message sent to this frame using this origin doesn't receive a timely response, the tool should fall back to sending the message to the parent window using the wildcard `*` origin.

**Required properties:**

- key: the string key for the retrieved value
- message\_id: any random string value. a UUID is easiest

Returning postMessage includes the following properties:

- key: the same key provided in the initial message
- value: the value, if any, stored at that key in Canvas's localstorage. `null` will be sent if the key/value pair doesn't exist.
- message\_id: the same message\_id provided in the initial message

```
window.parent.frames['post_message_forwarding'].postMessage(
  {
    subject: 'lti.get_data',
    key: 'hello',
    message_id: '14556a4f-e9af-43f7-bd1f-d3e260d05a9f',
  },
  'http://sso.canvaslms.com'
)
window.parent.postMessage(
  {
    subject: 'lti.get_data',
    key: 'hello',
    message_id: '14556a4f-e9af-43f7-bd1f-d3e260d05a9f',
  },
  '*'
)
```

Launches the tool that sent the event in a full-window context (ie not inside a Canvas iframe).

**Required properties:**

- subject: "requestFullWindowLaunch"
- data: either a string or an object
  
  - if a string, a url for relaunching the tool
  - if an object, has required sub-properties
- data.url: a url for relaunching the tool
- data.placement: the Canvas placement that the tool was launched in. Provided in the 1.3 id token under the custom claim section (`https://www.instructure.com/placement`).
- data.resource\_link\_id: the Canvas resource\_link\_id for the resource launched. Provided in the 1.3 id token under the `resource_link` claim (`https://purl.imsglobal.org/spec/lti/claim/resource_link#id`).

**Optional properties:**

- data.launchType: defaults to "same\_window"
  
  - "same\_window": launches the tool in the same window, replacing Canvas entirely
  - "new\_window": launches the tool in a new tab/window, which depends on user preference
  - "popup": launches the tool in a popup window
- data.launchOptions.width: for launchType: popup, defines the popup window's width. Defaults to 800.
- data.launchOptions.height: for launchType: popup, defines the popup window's height. Defaults to 600.

```
window.parent.postMessage(
  {
    subject: 'requestFullWindowLaunch',
    data: {
      url: 'https://example-tool.com/launch',
      placement: 'course_navigation',
      launchType: 'new_window',
      launchOptions: {
        width: 1000,
        height: 800,
      },
    },
  },
  '*'
)
```

Notifies the Canvas page holding the tool that a resource has finished importing. Canvas will respond by reloading the page, if the tool was present in the external apps tray. Used on wiki pages.

**Required properties:**

- subject: "lti.resourceImported"

```
window.parent.postMessage({subject: 'lti.resourceImported'}, '*')
```

Tells Canvas to remove the right side nav in the assignments view.

**Required properties:**

- subject: "lti.hideRightSideWrapper"

```
window.parent.postMessage(
  {
    subject: 'lti.hideRightSideWrapper',
  },
  '*'
)
```

Tells Canvas to change the height of the iframe containing the tool.

**Required properties:**

- subject: "lti.frameResize"

**Optional properties:**

- token: postMessage token, discussed above.

```
window.parent.postMessage(
  {
    subject: 'lti.frameResize',
    height: 400,
  },
  '*'
)
```

Sends a postMessage event back to the tool with details about the window size of the tool's containing iframe.

**Required properties:**

- subject: "lti.fetchWindowSize"

Returning postMessage includes the following properties:

- subject: "lti.fetchWindowSize.response"
- height: height of the iframe
- width: width of the iframe
- footer: height of the "#fixed\_bottom" HTML element or 0 if not found
- scrollY: the number of px that the iframe is scrolled vertically

```
window.parent.postMessage({subject: 'lti.fetchWindowSize'}, '*')
```

Toggles the module navigation footer based on the message's content.

**Required properties:**

- subject: "lti.showModuleNavigation"
- show: Boolean, whether to show or hide the footer

```
window.parent.postMessage(
  {
    subject: 'lti.showModuleNavigation',
    show: true,
  },
  '*'
)
```

Scrolls the iframe all the way to the top of its container.

**Required properties:**

- subject: "lti.scrollToTop"

```
window.parent.postMessage({subject: 'lti.scrollToTop'}, '*')
```

Sets a message to be shown in a browser dialog before page closes (ie "Do you really want to leave this page?")

**Required properties:**

- subject: "lti.setUnloadMessage"

**Optional properties:**

- message: The message to be shown in the dialog. Most browser no longer support a custom message here, so a generic (built-in to the browser) message will be shown.

```
window.parent.postMessage(
  {
    subject: 'lti.setUnloadMessage',
    message: 'Are you sure you want to leave this app?',
  },
  '*'
)
```

Clears any set message to be shown on page close.

Required properties

- subject: "lti.removeUnloadMessage"

```
window.parent.postMessage({subject: 'lti.removeUnloadMessage'}, '*')
```

Shows an alert for screen readers.

**Required properties:**

- subject: "lti.screenReaderAlert"
- body: The contents of the alert.

```
window.parent.postMessage(
  {
    subject: 'lti.screenReaderAlert',
    body: 'An alert just for screen readers',
  },
  '*'
)
```

Shows an alert using Canvas's alert system, and includes the name of the LTI tool that sent the message.

**Required properties:**

- body: The contents of the alert - can either be a string, or JSON string.

**Optional properties:**

- alertType: "success", "warning", or "error". Defaults to "success".
- title: A display name for the tool. If not provided, Canvas will attempt to supply the tool name or default to "External Tool".

```
window.parent.postMessage(
  {
    subject: 'lti.showAlert',
    alertType: 'warning',
    body: 'An warning to be shown',
    title: 'Tool Name',
  },
  '*'
)
```

Sends a debounced postMessage event to the tool every time its containing iframe is scrolled.

**Required properties:**

- subject: "lti.enableScrollEvents"

Returning postMessage includes the following properties:

- scrollY: the number of px that the iframe is scrolled vertically

```
window.parent.postMessage({subject: 'lti.enableScrollEvents'}, '*')
```

Opens the navigation sidebar, a replacement for toggleCourseNavigationMenu. Can be used on course, account or group page.

**Required properties:**

- subject: "showNavigationMenu"

```
window.parent.postMessage({subject:'showNavigationMenu'},'*')
```

Closes the navigation sidebar, a replacement for toggleCourseNavigationMenu. Can be used on course, account or group page.

**Required properties:**

- subject: "hideNavigationMenu"

```
window.parent.postMessage({subject:'hideNavigationMenu'},'*')
```

### toggleCourseNavigationMenu ⚠️

**Use show or hideNavigationMenu instead!**

Opens and closes the course navigation sidebar, giving more space for the tool to display.

**Required properties:**

- subject: "toggleCourseNavigationMenu"

```
window.parent.postMessage({subject:'toggleCourseNavigationMenu'},'*')
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 2 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).