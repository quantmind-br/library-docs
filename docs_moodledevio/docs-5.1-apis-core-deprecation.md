---
title: Deprecation API | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/apis/core/deprecation
source: sitemap
fetched_at: 2026-02-17T15:34:08.380316-03:00
rendered_js: false
word_count: 0
summary: This document provides examples of how to use the PHP deprecated attribute to mark functions, classes, methods, and enum cases as obsolete within a codebase.
tags:
    - php
    - deprecation
    - attributes
    - coding-standards
    - moodle
    - backend-development
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