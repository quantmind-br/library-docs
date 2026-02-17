---
title: Service creation | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/apis/subsystems/external/advanced/custom-services
source: sitemap
fetched_at: 2026-02-17T15:45:26.962572-03:00
rendered_js: false
word_count: 126
summary: This document outlines the structure and available parameters for defining external web services in Moodle using a services configuration array.
tags:
    - moodle
    - external-services
    - api-definition
    - web-service-configuration
    - php-configuration
category: configuration
---

```
$services=[
// The name of the service.
// This does not need to include the component name.
'myintegration'=>[

// A list of external functions available in this service.
'functions'=>[
'local_groupmanager_create_groups',
],

// If set, the external service user will need this capability to access
// any function of this service.
// For example: 'local_groupmanager/integration:access'
'requiredcapability'=>'local_groupmanager/integration:access',

// If enabled, the Moodle administrator must link a user to this service from the Web UI.
'restrictedusers'=>0,

// Whether the service is enabled by default or not.
'enabled'=>1,

// This field os optional, but requried if the `restrictedusers` value is
// set, so as to allow configuration via the Web UI.
'shortname'=>'',

// Whether to allow file downloads.
'downloadfiles'=>0,

// Whether to allow file uploads.
'uploadfiles'=>0,
]
];
```