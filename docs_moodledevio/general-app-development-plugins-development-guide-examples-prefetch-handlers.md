---
title: Prefetch Handlers | Moodle Developer Resources
url: https://moodledev.io/general/app/development/plugins-development-guide/examples/prefetch-handlers
source: sitemap
fetched_at: 2026-02-17T15:54:50.583597-03:00
rendered_js: false
word_count: 225
summary: This document explains how to implement custom prefetch handlers for Moodle app modules to support complex offline functionality, such as chaining web service calls and handling additional arguments.
tags:
    - moodle-development
    - mobile-app
    - prefetch-handler
    - offline-mode
    - web-services
    - plugin-api
category: guide
---

[CoreCourseModuleDelegate](https://moodledev.io/general/app/development/plugins-development-guide/api-reference#corecoursemoduledelegate) handlers allow you to define a list of offline functions to prefetch a module. However, you might want to create your own prefetch handler to determine what needs to be downloaded. For example, you might need to chain Web Service calls (passing the result of a Web Service request to another), and this cannot be done using offline functions.

```
classAddonModCertificateModulePrefetchHandlerextendsthis.CoreCourseActivityPrefetchHandlerBase{

constructor(){
super();

this.name='AddonModCertificateModulePrefetchHandler';
this.modName='certificate';

// This must match the plugin identifier from db/mobile.php,
// otherwise the download link in the context menu will not update correctly.
this.component='mod_certificate';
this.updatesNames=/^configuration$|^.*files$/;
}

// Override the prefetch call.
prefetch(module, courseId, single, dirPath){
returnthis.prefetchPackage(module, courseId, single, prefetchCertificate);
}

}

asyncfunctionprefetchCertificate(module, courseId, single, siteId){
// Perform all the WS calls.
// You can access most of the app providers using that.ClassName. E.g. that.CoreWSProvider.call().
}

this.CoreCourseModulePrefetchDelegate.registerHandler(newAddonModCertificateModulePrefetchHandler());
```

One relatively simple full example is where you have a function that needs to work offline, but it has an additional argument other than the standard ones. You can imagine for this an activity like the book module, where it has multiple pages for the same `cmid`. The app will not automatically work in this situation — it will call the offline function with the standard arguments only — so you won't be able to prefetch all the possible parameters.

To deal with this, you need to implement a Web Service in your Moodle component that returns the list of possible extra arguments, and then you can call this Web Service and loop around doing the same thing the app does when it prefetches the offline functions. Here is an example from a third-party module with multiple values for a custom `section` parameter in the mobile function `mobile_document_view`. We're only showing the actual prefetch function, the rest of the code is the same as above:

```
asyncfunctionprefetchOucontent(module, courseId, single, siteId){
const component ='mod_oucontent';

// Get the site, first.
const site =await that.CoreSitesProvider.getSite(siteId);

// Read the list of pages in this document using a web service.
const pages = site.read('mod_oucontent_get_page_list',{'cmid': module.id});

// For each page, read and process the page - this is a copy of logic in the app at
// siteplugins.ts (prefetchFunctions), but modified to add the custom argument.
awaitPromise.all(pages.map(async(page)=>{
const args ={
courseid: courseId,
cmid: module.id,
userid: site.getUserId()
};

if(page !==''){
            args.section= page;
}

const result =await that.CoreSitePluginsProvider.getContent(component,'mobile_document_view', args);

if(result.files?.length){
await that.CoreFilepoolProvider.downloadOrPrefetchFiles(
                site.id,
                result.files,
true,
false,
                component,
                module.id,
);
}
}));
}
```