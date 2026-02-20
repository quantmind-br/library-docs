---
title: Function Declarations | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/apis/subsystems/external/description
source: sitemap
fetched_at: 2026-02-17T15:13:27.996397-03:00
rendered_js: false
word_count: 0
summary: This document provides a PHP code snippet for defining a web service function in a Moodle plugin, detailing parameters such as class names, access types, and service integration.
tags:
    - moodle-development
    - web-services
    - external-functions
    - php-configuration
    - plugin-development
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