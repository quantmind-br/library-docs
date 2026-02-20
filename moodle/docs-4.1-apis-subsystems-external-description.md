---
title: Function Declarations | Moodle Developer Resources
url: https://moodledev.io/docs/4.1/apis/subsystems/external/description
source: sitemap
fetched_at: 2026-02-17T14:56:08.162279-03:00
rendered_js: false
word_count: 0
summary: This document outlines the configuration structure for defining a web service function within a Moodle plugin, detailing properties like class location, access type, and service integration.
tags:
    - moodle-development
    - web-services
    - php-configuration
    - external-functions
    - plugin-api
category: configuration
---

```
$functions=[
// The name of your web service function, as discussed above.
'local_myplugin_create_groups'=>[
// The name of the namespaced class that the function is located in.
'classname'=>'local_groupmanager\external\create_groups',

// A brief, human-readable, description of the web service function.
'description'=>'Creates new groups.',

// Options include read, and write.
'type'=>'write',

// Whether the service is available for use in AJAX calls from the web.
'ajax'=>true,

// An optional list of services where the function will be included.
'services'=>[
// A standard Moodle install includes one default service:
// - MOODLE_OFFICIAL_MOBILE_SERVICE.
// Specifying this service means that your function will be available for
// use in the Moodle Mobile App.
MOODLE_OFFICIAL_MOBILE_SERVICE,
],
],
];
```