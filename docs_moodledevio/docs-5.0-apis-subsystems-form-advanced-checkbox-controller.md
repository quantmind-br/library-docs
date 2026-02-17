---
title: Checkbox controller | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/apis/subsystems/form/advanced/checkbox-controller
source: sitemap
fetched_at: 2026-02-17T15:27:39.753075-03:00
rendered_js: false
word_count: 75
summary: This document demonstrates how to implement a checkbox controller to provide 'Select all/none' functionality for grouped form elements.
tags:
    - moodle-forms
    - php-development
    - checkbox-controller
    - form-elements
    - ui-interaction
category: tutorial
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