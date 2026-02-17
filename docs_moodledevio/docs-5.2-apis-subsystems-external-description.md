---
title: Function Declarations | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/apis/subsystems/external/description
source: sitemap
fetched_at: 2026-02-17T15:45:31.238245-03:00
rendered_js: false
word_count: 0
summary: This document outlines the configuration structure for registering a custom web service function in Moodle, defining properties such as the implementation class, access type, and service availability.
tags:
    - moodle-development
    - web-services
    - php-configuration
    - plugin-development
    - external-functions
    - ajax-support
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