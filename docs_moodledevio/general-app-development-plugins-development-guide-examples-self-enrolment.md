---
title: Self Enrolment | Moodle Developer Resources
url: https://moodledev.io/general/app/development/plugins-development-guide/examples/self-enrolment
source: sitemap
fetched_at: 2026-02-17T15:54:53.394303-03:00
rendered_js: false
word_count: 41
summary: This document explains how to support enrolment plugins in the Moodle app by registering handlers in CoreEnrolDelegate and implementing specific JavaScript methods.
tags:
    - moodle-app
    - coreenroldelegate
    - enrolment-plugins
    - mobile-development
    - plugin-integration
category: guide
---

Using [CoreEnrolDelegate](https://moodledev.io/general/app/development/plugins-development-guide/api-reference#coreenroldelegate-43) handlers you can support enrolment plugins in the app. In this example, we can see how to support a self enrol plugin. You'll need to register a handler in `db/mobile.php` and return the following JavaScript from the `method` implementation:

```
constgetEnrolmentInfo=(id)=>{
// Get enrolment info for the enrol instance.
// Used internally, you can use any name, parameters and return data in here.
};

constselfEnrol=(method, info)=>{
// Self enrol the user in the course.
// Used internally, you can use any name, parameters and return data in here.
};

var result ={
getInfoIcons:(courseId)=>{
returnthis.CoreEnrolService.getSupportedCourseEnrolmentMethods(courseId,'selftest').then(enrolments=>{
if(!enrolments.length){
return[];
}

// Since this code is for testing purposes just use the first one.
returngetEnrolmentInfo(enrolments[0].id).then(info=>{
if(!info.enrolpassword){
return[{
label:'plugin.enrol_selftest.pluginname',
icon:'fas-right-to-bracket',
}];
}else{
return[{
label:'plugin.enrol_selftest.pluginname',
icon:'fas-key',
}];
}
});
});
},
enrol:(method)=>{
returngetEnrolmentInfo(method.id).then(info=>{
returnselfEnrol(method, info);
});
},
invalidate:(method)=>{
// Invalidate WS data.
},
};

result;
```