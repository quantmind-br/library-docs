---
title: Question Types | Moodle Developer Resources
url: https://moodledev.io/general/app/development/plugins-development-guide/examples/question-types
source: sitemap
fetched_at: 2026-02-17T15:54:50.837254-03:00
rendered_js: false
word_count: 0
summary: This document defines the PHP configuration structure required to register a custom Moodle question type within the mobile application environment.
tags:
    - moodle
    - mobile-app
    - question-type
    - plugin-configuration
    - mobile-addon
category: configuration
---

```
$addons=[
"qtype_YOURQTYPENAME"=>[
"handlers"=>[
'YOURQTYPENAME'=>[
'displaydata'=>[
'title'=>'YOURQTYPENAME question',
'icon'=>'/question/type/YOURQTYPENAME/pix/icon.gif',
'class'=>'',
],
'delegate'=>'CoreQuestionDelegate',
'method'=>'mobile_get_YOURQTYPENAME',
'offlinefunctions'=>[
'mobile_get_YOURQTYPENAME'=>[],
],
'styles'=>[
'url'=>'/question/type/YOURQTYPENAME/mobile/styles_app.css',
'version'=>'1.00',
],
],
],
'lang'=>[
['pluginname','qtype_YOURQTYPENAME'],
],
],
];
```