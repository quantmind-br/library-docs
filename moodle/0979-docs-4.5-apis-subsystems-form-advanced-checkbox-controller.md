---
title: Checkbox controller | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/apis/subsystems/form/advanced/checkbox-controller
source: sitemap
fetched_at: 2026-02-17T15:14:20.590351-03:00
rendered_js: false
word_count: 75
summary: This document demonstrates how to implement checkbox controllers in Moodle forms to manage group selection and deselection for advanced checkboxes.
tags:
    - moodle-forms
    - php-api
    - checkbox-controller
    - form-elements
    - bulk-actions
category: guide
---

```
publicfunctiondefinition():void{
// These two elements are part of group 1.
$mform->addElement('advcheckbox','test1','Test 1',null,['group'=>1]);
$mform->addElement('advcheckbox','test2','Test 2',null,['group'=>1]);

// Add a checkbox controller for all checkboxes in `group => 1`:
$this->add_checkbox_controller(1);

// These two elements are part of group 3.
$mform->addElement('advcheckbox','test3','Test 3',null,['group'=>3]);
$mform->addElement('advcheckbox','test4','Test 4',null,['group'=>3]);

// Add a checkbox controller for all checkboxes in `group => 3`.
// This example uses a different wording isntead of Select all/none by passing the second parameter:
$this->add_checkbox_controller(
3,
get_string("checkall","plugintype_pluginname")
);
}
```