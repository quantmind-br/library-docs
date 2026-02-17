---
title: Forms API | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/apis/subsystems/form
source: sitemap
fetched_at: 2026-02-17T15:04:25.607347-03:00
rendered_js: false
word_count: 1054
summary: This document explains how to use the Moodle Form API to create, process, and render secure, accessible forms by extending the moodleform class.
tags:
    - moodle
    - form-api
    - moodleform
    - php
    - web-forms
    - form-validation
    - ui-elements
category: api
---

Form are created using the Form API. The Form API supports most standard HTML elements, including checkboxes, radio buttons, text boxes, and so on, adding additional accessibility and security features to them.

## Highlights[​](#highlights "Direct link to Highlights")

- Tested and optimised for use on major screen-readers like Dragon and JAWS.
- Table-less layout.
- Processes form data securely, with `required_param`, `optional_param`, and session key.
- Supports client-side validation.
- Facility to add Moodle help buttons to forms.
- Support for file repository using the [File API](https://moodledev.io/docs/4.4/apis/subsystems/files) .
- Support for many custom Moodle specific and non-specific form elements.
- Facility for [repeated elements](https://moodledev.io/docs/4.4/apis/subsystems/form/advanced/repeat-elements).
- Facility for form elements in advanced groups

## Usage[​](#usage "Direct link to Usage")

The Moodle forms API separates forms into different areas:

1. a form definition, which extends the `moodleform` class; and
2. uses of that form.

To create a form in Moodle, you create a class that defines the form, including every form element. Your class must extend the `moodleform` class and overrides the [definition](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#definition.28.29) member function to describe the form elements.

An example of a form definition

\[path/to/plugin]/classes/form/myform.php

```
<?php

namespace[plugintype]_[pluginname]\form;

// moodleform is defined in formslib.php
require_once("$CFG->libdir/formslib.php");

classsimplehtml_formextends\moodleform{
// Add elements to form.
publicfunctiondefinition(){
// A reference to the form is stored in $this->form.
// A common convention is to store it in a variable, such as `$mform`.
$mform=$this->_form;// Don't forget the underscore!

// Add elements to your form.
$mform->addElement('text','email',get_string('email'));

// Set type of element.
$mform->setType('email',PARAM_NOTAGS);

// Default value.
$mform->setDefault('email','Please enter email');
}

// Custom validation should be added here.
functionvalidation($data,$files){
return[];
}
}
```

Once the form has been defined it can be instantiated elsewhere in Moodle, for example:

```

// Instantiate the myform form from within the plugin.
$mform=new\plugintype_pluginname\form\myform();

// Form processing and displaying is done here.
if($mform->is_cancelled()){
// If there is a cancel element on the form, and it was pressed,
// then the `is_cancelled()` function will return true.
// You can handle the cancel operation here.
}elseif($fromform=$mform->get_data()){
// When the form is submitted, and the data is successfully validated,
// the `get_data()` function will return the data posted in the form.
}else{
// This branch is executed if the form is submitted but the data doesn't
// validate and the form should be redisplayed or on the first display of the form.

// Set anydefault data (if any).
$mform->set_data($toform);

// Display the form.
$mform->display();
}
```

If you wish to use the form within a block then you should consider using the render method, as demonstrated below:

Note that the render method does the same as the display method, except returning the HTML rather than outputting it to the browser, as with above make sure you've included the file which contains the class for your Moodle form.

```
classblock_yourblockextendsblock_base{
publicfunctioninit(){
$this->title='Your Block';
}

publicfunctionget_content(){
$this->content=(object)[
'text'=>'',
];

$mform=new\plugintype_pluginname\form\myform();

if($mform->is_cancelled()){
// If there is a cancel element on the form, and it was pressed,
// then the `is_cancelled()` function will return true.
// You can handle the cancel operation here.
}elseif($fromform=$mform->get_data()){
// When the form is submitted, and the data is successfully validated,
// the `get_data()` function will return the data posted in the form.
}else{
// This branch is executed if the form is submitted but the data doesn't
// validate and the form should be redisplayed or on the first display of the form.

// Set anydefault data (if any).
$mform->set_data($toform);

// Display the form.
$this->content->text=$mform->render();
}

return$this->content;
}
}
```

## Form elements[​](#form-elements "Direct link to Form elements")

Moodle provides a number of basic, and advanced, form elements. These are described in more detail below.

### Basic form elements[​](#basic-form-elements "Direct link to Basic form elements")

01. [button](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#button)
02. [checkbox](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#checkbox)
03. [radio](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#radio)
04. [select](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#select)
05. [multi-select](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#multi-select)
06. [password](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#password)
07. [hidden](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#hidden)
08. [html](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#html) - div element
09. [static](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#static) - Display a static text.
10. [text](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#text)
11. [textarea](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#textarea)
12. [header](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#Use_Fieldsets_to_group_Form_Elements)

### Advanced form elements[​](#advanced-form-elements "Direct link to Advanced form elements")

01. [Autocomplete](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#autocomplete) - A select box that allows you to start typing to narrow the list of options, or search for results.
02. [advcheckbox](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#advcheckbox) - Advance checkbox
03. [choicedropdown](https://moodledev.io/docs/4.4/apis/subsystems/form/fields/choicedropdown) - A dropdown menu where custom information is displayed on each option.
04. [float](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#float)
05. [passwordunmask](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#passwordunmask) - A password element with option to show the password in plaintext.
06. [recaptcha](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#recaptcha)
07. [selectyesno](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#selectyesno)
08. [selectwithlink](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#selectwithlink)
09. [date\_selector](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#date_selector)
10. [date\_time\_selector](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#date_time_selector)
11. [duration](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#duration)
12. [editor](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#editor)
13. [filepicker](https://moodledev.io/docs/4.4/apis/subsystems/form/usage/files#file-picker) - upload single file
14. [filemanager](https://moodledev.io/docs/4.4/apis/subsystems/form/usage/files#file-manager) - upload multiple files
15. [tags](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#tags)
16. [addGroup](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#addGroup)
17. [modgrade](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#modgrade)
18. [modvisible](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#modvisible)
19. [choosecoursefile](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#choosecoursefile)
20. [grading](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#grading)
21. [questioncategory](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#questioncategory)

### Custom form elements[​](#custom-form-elements "Direct link to Custom form elements")

In addition to the standard form elements, you can register your own custom form elements, for example:

```
// Register a custom form element.
MoodleQuickForm::registerElementType(
// The custom element is named `course_competency_rule`.
// This is the element name used in the `addElement()` function.
'course_competency_rule',

// This is where it's definition is defined.
// This does not currently support class auto-loading.
"$CFG->dirroot/$CFG->admin/tool/lp/classes/course_competency_rule_form_element.php",

// The class name of the element.
'tool_lp_course_competency_rule_form_element'
);

// Add an instance of the custom form element to your form.
$mform->addElement(
// The name of the custome lement.
'course_competency_rule',
'competency_rule',
get_string('uponcoursemodulecompletion','tool_lp'),
$options
);
```

For a real-life example, see:

- [Custom element definition](https://github.com/moodle/moodle/blob/main/admin/tool/lp/classes/course_competency_rule_form_element.php)
- [Custom element usage](https://github.com/moodle/moodle/blob/main/admin/tool/lp/lib.php#L157-L161)

## Commonly used functions[​](#commonly-used-functions "Direct link to Commonly used functions")

### add\_action\_buttons()[​](#add_action_buttons "Direct link to add_action_buttons()")

Add the standard 'action' buttons to the form - these are the standard Submit, and Cancel buttons on the form.

```
publicfunctionadd_action_buttons(
bool$cancel=true,
?string$submitlabel=null
);
```

- The `$cancel` parameter can be used to control whether a cancel button is shown.
- The `$submitlabel` parameter can be used to set the label for the submit button. The default value comes from the `savechanges` string.

important

The `add_action_buttons` function is defined on the `moodleform` class, and not a part of `$this->_form`, for example:

```
publicfunctiondefinition(){
// Add your form elements here.
$this->_form->addElement(...);

// When ready, add your action buttons.
$this->add_action_buttons();
}
```

### add\_sticky\_action\_buttons()[​](#add_sticky_action_buttons "Direct link to add_sticky_action_buttons()")

This method calls `add_action_buttons()` internally and makes 'action' buttons sticky.

```
publicfunctionadd_sticky_action_buttons(
bool$cancel=true,
?string$submitlabel=null
);
```

### setDefault()[​](#setdefault "Direct link to setDefault()")

The [setDefault()](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#setDefault_2) function can be used to set the default value for an element.

### disabledIf()[​](#disabledif "Direct link to disabledIf()")

The [disabledIf()](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#disabledIf) function can be used to conditionally *disable* a group of elements, or and individual element depending on the state of other form elements.

### hideIf()[​](#hideif "Direct link to hideIf()")

The [hideif()](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#hideIf) function can be used to conditionally *hide* a group of elements, or and individual element depending on the state of other form elements.

### addRule()[​](#addrule "Direct link to addRule()")

The [addRule()](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#addRule) function can be used to define both client-side, and server-side validation rules. For example, this can be used to validate that a text-field is required, and has a type of email.

### addHelpButton()[​](#addhelpbutton "Direct link to addHelpButton()")

The [addHelpButton()](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#addHelpButton) function can be used to add a pop-up help button to a form element.

### setType()[​](#settype "Direct link to setType()")

The [setType()](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#setType) function can be used to specify how submitted values are cleaned. The `PARAM_*` constants are used to specify the type of data that will be submitted.

### disable\_form\_change\_checker()[​](#disable_form_change_checker "Direct link to disable_form_change_checker()")

Normally, if a user navigate away from any form and changes have been made, a popup will be shown to the user asking them to confirm that they wish to leave the page and that they may lose data.

In some cases this is not the desired behaviour, in which case the [disable\_form\_change\_checker()](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#disable_form_change_checker) function can be used to disable the form change checker.

For example:

```
publicfunctiondefinition(){
// Your definition goes here.

// Disable the form change checker for this form.
$this->_form->disable_form_change_checker();
}
```

This method adds values to `_shownonlyelements` array to decide whether a header should be shown or hidden. Only header names would be accepted and added to `_shownonlyelements` array. Headers included in `_shownonlyelements` will be shown expanded in the form. The rest of the headers will be hidden.

```
publicfunctionfilter_shown_headers(array$shownonly):void{
$this->_shownonlyelements=[];
if(empty($shownonly)){
return;
}
foreach($shownonlyas$headername){
$element=$this->getElement($headername);
if($element->getType()=='header'){
$this->_shownonlyelements[]=$headername;
$this->setExpanded($headername);
}
}
}
```

Empty `_shownonlyelements` array doesn't affect header's status or visibility.

/course/editsection.php

```
$showonly=optional_param('showonly',0,PARAM_TAGLIST);

[...]

$mform=$courseformat->editsection_form($PAGE->url,$customdata);

$initialdata=convert_to_array($sectioninfo);
if(!empty($CFG->enableavailability)){
$initialdata['availabilityconditionsjson']=$sectioninfo->availability;
}
$mform->set_data($initialdata);
if(!empty($showonly)){
$mform->filter_shown_headers(explode(',',$showonly));
}
```

### Other features[​](#other-features "Direct link to Other features")

In some cases you may want to [group elements](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition#Use_Fieldsets_to_group_Form_Elements) into collections.

## Unit testing[​](#unit-testing "Direct link to Unit testing")

In order to test the processing of submitted form contents in unit tests, the Forms API has a `mock_submit()` function.

This method makes the form behave as if the data supplied to it was submitted by the user via the web interface. The data still passes through all form validation, which means that \`get\_data() will return all of the parsed values, along with any defaults.

Example usage

```
// Instantiate a form to submit.
$form=newqtype_multichoice_edit_form(...);

// Fetch the data and then mock the submission of that data.
$questiondata=test_question_maker::get_question_data('multichoice','single');
$form->mock_submit($questiondata);

// The `get_data()` function will return the validated data, plus any defaults.
$actualfromform=$form->get_data();

// The resultant data can now be tested against the expected values.
$expectedfromform=test_question_maker::get_question_form_data('multichoice','single');
$this->assertEquals($expectedfromform,$actualfromform);

// The data can also be saved and tested in the context of the API.
save_question($actualfromform);
$actualquestiondata=question_load_questions(array($actualfromform->id));
$this->assertEquals($questiondata,$actualquestiondata);
```

## See also[​](#see-also "Direct link to See also")

- [Core APIs](https://moodledev.io/docs/4.4/apis)
- [lib/formslib.php Usage](https://moodledev.io/docs/4.4/apis/subsystems/form/usage)
- [lib/formslib.php Form Definition](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition)
- [Designing usable forms](https://moodledev.io/general/development/policies/designing-usable-forms)
- [Fragment](https://docs.moodle.org/dev/Fragment)
- [MForm Modal](https://docs.moodle.org/dev/MForm_Modal)