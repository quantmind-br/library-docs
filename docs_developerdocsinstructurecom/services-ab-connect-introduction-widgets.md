---
title: Using AB Connect's Embeddable Widgets | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/introduction/widgets
source: sitemap
fetched_at: 2026-02-15T09:03:51.058935-03:00
rendered_js: false
word_count: 2199
summary: This document provides instructions for integrating and configuring the Instructure Academic Benchmarks Standards Browser widget into web applications. It details script inclusion, initialization via jQuery, and the various configuration properties available to control UI state and event handling.
tags:
    - academic-benchmarks
    - instructure
    - standards-browser
    - jquery-integration
    - widget-configuration
    - frontend-development
category: guide
---

In continuing efforts to make the process of working with academic Standards easy and efficient, we have begun to create plug-able widgets that can be used directly in apps created by our partners. The widgets are designed to enable our partners to offer capabilities within their apps with only a few lines of code. We will continue to expand the capabilities of the widgets as well as add to the list of supported widgets over time.

Our initial offering is a widget that enables the end user to browse for and select Standards. We will continue to expand the capabilities to support faceted and full text search as well as search-by-number.

## Supporting Infrastructure

Instructure's Academic Benchmarks widgets are hosted on Amazon's Content Delivery Network (CDN) to ensure high availability and responsiveness.

## Standards Browser Integration

The app is built on jQuery and completely embeds all requirements directly within the one package to ensure smooth integration. To plug the widget into your app, start by including the script into your HTML file:

`<script src="https://widgets.academicbenchmarks.com/ABConnect/v4/dist/widgets.js"></script>`

The required version of jQuery is encapsulated within the widget JavaScript to avoid version dependency issues but the order in which your app loads the various libraries matters. If you use jQuery, you should always load jQuery before the AB Connect widgets. We've bundled a version of jQuery in such a way as not to interfere with other versions that may be included on the page. To ensure the smoothest integration possible, the widget will handle the encapsulated jQuery in the following manor:

1. If jQuery was loaded into the page before the widgets, then the widgets will be installed into it but the widgets will use the encapsulated version of jQuery internally.
2. If jQuery is not loaded at all, then the encapsulated version of jQuery (and widgets) will be installed into the page. (version 2.2.4)
3. If jQuery is loaded **after** the widgets, then the version of jQuery (and widgets) installed by AB Connect will be rendered inaccessible.

### Adding the Widget to Your Page

Once the script is included, create a div to hold the widget. Note that the widget was designed for a minimum size of 800 x 600 px. If it is given more space than that, it will expand to take advantage of it. You can give the div any name/class/tag you like.

`<div class="standardsBrowser" style="width: 800px; height: 600px;"></div>`

Initializing the browser is as simple as:

`$('.standardsBrowser').standardsBrowser(config);`

The `config` object can be used to define the behavior of the widget as well as how it interacts with your app.

The configuration object you include in the widget initiation can help control the behavior of the widget. This section describes the properties of the configuration object and how they are used to control the widget.

- `uiEntityState` - This is an object property that defines the initial values of elements in the UI as well as their visibility. Each property of the uiEntityState object contains an optional flag (named "show") indicating whether that element is visible and a value property indicating the initial value(s) of the element. If the "show" property is left out, the default is true. If the value property is left out, no initial selection is made. If the element property is not included, the element is visible with no initial selection. Properties:
  
  - `authority` - Indicates the drop-down listing the authorities available for browsing. The value property is the GUID of the initial authority selection.
  - `publication` - Indicates the drop-down listing the publications available for browsing. The value property is the GUID of the initial publication selection.
  - `document` - Indicates the drop-down listing the documents available for browsing. The value property is the GUID of the initial document selection.

E.g.:

```
    uiEntityState: {
      authority: {
        show: false,
        value: "A83297F2-901A-11DF-A622-0C319DFF4B22"
      },
      publication: {
        show: false,
        value: "964E0FEE-AD71-11DE-9BF2-C9169DFF4B22"
      },
      document: {
        show: false,
        value: "6C2635F0-6EC0-11DF-AB2D-366B9DFF4B22"
      }
    }
```

would pre-select the Common Core Math Standards and hide the lists so the user couldn't change the selection.

- `selectMode` - This is a property indicating whether the browser is in single select mode (single - the default) or multiple select mode (multiple). If false, the user can select multiple Standards at a time. Note that the selection is cleared when the user changes facet filtering, does a search or changes document. It is the responsibility of the parent app to offer a mechanism to build and manage a persistent list of Standards if appropriate for the app.
- `enableDoubleClick` - This is a Boolean property indicating whether the browser supports double clicks (true). Default: false.
- `showAssetCount` - This is a Boolean property indicating whether the browser should show a badge indicating the number of Assets that are related to the Standard. This can be used in situations where the parent app is using the Standards Browser as a first step in helping the user search for related Assets. Note that this capability requires that your organization stores your content metadata profile as Assets in AB Connect. The default is false.
- `assetCountFilter` - This is a string property that is added to the AB Connect query that is used to retrieve the Asset count when the showAssetCount is true. By default, the widget counts any Assets that are owned by your account and are related to the Standard in question. However, you can pass a query string that is then appended to the query with an AND operator to further limit the query. E.g. you may want to further limit the results to a particular type of Asset or Assets of a particular media type. This property is optional and only used if showAssetCount is true.
- `authCredentials` - This is an object property containing the authorization credentials. See the AB Connect [documentation on authentication](https://developerdocs.instructure.com/services/ab-connect/introduction/authentication) for details.
  
  - `signature` -signature generated from your partner key and the expires value
  - `expires` -expiration date of the signature
  - `user` - optional parameter for an ID specific to this user
- `onStandardSelect` - An event handler defined by your app to handle selection events for Standards. The signature of the function must be function (event, GUID). The GUID of the Standard that was selected is the second parameter. This property is optional. Alternatively, you can register your event handlers directly via jQuery.
- `onStandardDoubleClick` - An event handler defined by your app to handle double-click events for Standards. The signature of the function must be function (event, GUID). The GUID of the Standard that was clicked is the second parameter. This property is optional.
- `onStandardDeselect` - An event handler defined by your app to handle deselection events for Standards. The signature of the function must be function (event, GUID). The GUID of the Standard that was deselected is the second parameter. Note that this event will fire multiple times in the event of multiple deselects (e.g. when multiple Standards are selected and the document or filter criteria changes). This property is optional.
- `onError` - An event handler defined by your app to handle error events. In the event of warnings or soft error situations, the widget will do it's best to recover and restore normal working behavior while logging the issue in the console. However, error conditions that are unrecoverable (e.g. authentication errors) will be surfaced to the parent app. The signature of the function must be function (event, message). Message is a human readable message describing the error that occurred. While this parameter is technically optional so the developer can alternatively choose to register this handler directly with jQuery, the developer MUST create a handler using one method or another or there will be no user feedback on error conditions.

Here is an example configuration object for an app that uses the browser for the selection of a single Standard.

```
var config = {
      selectMode: 'single',
      enableDoubleClick: false,
      authCredentials: {
        ID: gPartnerID,
        signature: gSignature,
        expires: gAuthExpires
      },
      onStandardSelect: function(event, GUID){
        standardSelected(GUID);
      },
      onStandardDeselect: function(event, GUID){
        noStandardSelected();
      },
      onError: function(event, message){
        alert(message);
      }
    };
```

The Standards Browser fires or forwards events to the parent app. Registering for most of the events is optional but the app **must** register for error events because the widget does not handle errors itself. Instead, it forwards them to the parent app so it can display the error using the same approach it displays errors from other elements of the UI.

The following events may be fired during the operation of the widget:

- `standardSelect` - A Standard has been selected. The GUID of the Standard is forwarded with the event. The parent app may choose to ignore such events or it may take some action like enable buttons that allow the user to take action (like add the Standard to a list or close the selection card or dialog).
- `standardDoubleClick` - A Standard has been double clicked. The GUID of the Standard is forwarded with the event. The parent app may choose to ignore such events or it may take some action like add the Standard to a list or close the selection card or dialog. Note that due to the way double clicks are handled in browsers, a double click action will actually create a select event for the Standard being clicked, followed by deselect events for ALL selected Standards followed by a double click event for the Standard being clicked.
- `standardDeselect` - A Standard has been deselected. The GUID of the Standard is forwarded with the event. The parent app may choose to ignore such events or it may take some action like disable buttons. Note that if the user has multiple Standards selected and does something like change the search criteria or publication, the parent app will receive multiple "standardDeselect" events rapidly - one for each selected Standard.
- `error` - An error has occurred and the widget is unable to self recover in a meaningful way.

The Standards Browser supports the following methods to help the parent app interact with it.

- `getConfiguration` - Returns the uiEntityState object containing the current configuration. This will help the parent app re-launch the widget in the same state as it was when the user closed it. E.g. `var state = $('.standardsBrowser').standardsBrowser('getConfiguration');`
- `getSelection` - Returns an array of GUIDs listing every Standard that is currently selected in the UI. E.g. `var listGuids = $('.standardsBrowser').standardsBrowser('getSelection');`

See the [Instructure Github repositoryarrow-up-right](https://github.com/instructure/abconnect-samples) for examples illustrating how to embed the Standards Browser into your app.

- **Minimum Standards Browser** - This is a minimum app that hosts the Standards Browser. Beyond illustrating the basics of using embeddable widgets in an app, this example shows the basic JSON body of the currently selected Standard. You can see the [browser in action herearrow-up-right](https://widgets.academicbenchmarks.com/ABConnect/v4/standards-browser-min/StandardsBrowser.html).
- **Integrated Relationship Browser** - This is a version of the Relationship Browser app that uses the Standards Browser rather in place of the home-grown browser from the original Relationship Browser app. You can [see it in action herearrow-up-right](https://widgets.academicbenchmarks.com/ABConnect/v4/relationships-browser/RelationshipBrowser.html).

### Common Integration Scenarios

#### Simple Single Selector Pop-Up

One common situation is having the user select a single Standard. You may want to do this when prompting a teacher to select a Standard related to a test item or starting the process of searching for items by alignment. The integration may look something like this:

1. Create a pop-up window (or div) that contains the Standards Browser widget in single select mode and buttons for "OK" and "Close".
2. Disable the "OK" button by default.
3. Listen for onStandardSelect events. When you receive one, enable the OK button.
4. Listen for onStandardDeselect events. When you receive one, disable the OK button.
5. Listen for onStandardDoubleClick events. When you receive one, record the GUID, close the dialog and return control to the parent app.
6. If the user selects OK:
   
   1. Call getSelection to retrieve the selected Standard, record the GUID
   2. Optionally call getConfiguration on the StandardsBrowser to grab the user selections for restoration later
   3. Close the dialog and return control to the parent app

#### Multiple Selector with a Managed List of Standards

Another common situation is having the user manage a list of Standards. This may come up when you want to allow a teacher to search for materials related to curriculum for the next quarter. The integration may look something like this:

01. Create an area on the page that contains the Standards Browser widget in multiselect mode as well as a separate list (we'll call this standardsList) and arrow buttons to allow user to add Standards to the standardsList and remove Standards from the list (perhaps "&gt;&gt;" and "&lt;&lt;" or "Add" and "Remove" buttons). You may also want some sort of Action button.
02. Disable the "Add" button by default.
03. Listen for onStandardSelect events. When you receive one, enable the "Add" button.
04. Listen for onStandardDeselect events. When you receive one, check getSelection to see if there are any Standards still selected. If not, disable the "Add" button.
05. Listen for onStandardDoubleClick events. When you receive one, add the Standard related to the GUID to the list.
06. Listen for click events on the "Add" button. When you receive one, add the Standard related to the GUID to the list.
07. Listen for selection events on the standardsList. When you receive one, enable the "Remove" button.
08. Listen for deselection events on the standardsList. When you receive one, check to see if there are any Standards selected in the standardsList. If not, disable the "Remove" button.
09. Listen for click events on the "Remove" button. When you receive one, remove the selected Standard from the standardsList.
10. Listen for click events on the "Action" button. When you receive one:
    
    1. Gather the list of Standards from standardsList
    2. Optionally call getConfiguration on the StandardsBrowser to grab the user selections for restoration later
    3. Pass control to the parent app. You may want to remove or hide the StandardsBrowser at this point depending on the needs of your app.

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).