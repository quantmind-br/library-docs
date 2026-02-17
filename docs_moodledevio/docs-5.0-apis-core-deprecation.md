---
title: Deprecation API | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/apis/core/deprecation
source: sitemap
fetched_at: 2026-02-17T15:24:27.351833-03:00
rendered_js: false
word_count: 0
summary: This document provides examples of how to use the Moodle core deprecated attribute to mark functions, classes, methods, and enum cases for future removal. It illustrates the use of various attribute parameters such as replacement, version, reason, and issue tracker ID.
tags:
    - php
    - moodle
    - deprecation-attribute
    - api-lifecycle
    - coding-standards
category: reference
---

```
// On a global function:
#[\core\attribute\deprecated('random_bytes',since:'4.3')]
functionrandom_bytes_emulate($length){
// Replaced by random_bytes since Moodle 4.3.
}

// On a class:
#[\core\attribute\deprecated(replacement:null,since:'4.4',reason:'This functionality has been removed.')]
classexample{
#[\core\attribute\deprecated(
replacement:'\core\example::do_something',
since:'4.3',
reason:'No longer required',
mdl:'MDL-12345',
)]
publicfunctiondo_something():void{}
}

// On an enum case:
enumexample{
#[\core\attribute\deprecated('example::OPTION',since:'4.4',final:true)]
caseOPTION;
}
```