---
title: Form Usage | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/apis/subsystems/form/usage
source: sitemap
fetched_at: 2026-02-17T15:36:50.867573-03:00
rendered_js: false
word_count: 488
summary: This document explains the usage and structure of Moodle's Form API, detailing how to define form classes, handle data submission, and implement forms within activity modules.
tags:
    - moodle
    - form-api
    - php
    - moodleform
    - formslib
    - web-development
    - plugin-development
category: api
---

Moodle's Form API is an extension of the Pear HTML\_QuickForm API, which is no longer supported. Some documentation for the upstream library is [available in the PEAR package page](http://pear.php.net/package/HTML_QuickForm), including a [short tutorial](http://pear.php.net/manual/en/package.html.html-quickform.tutorial.php). A [longer tutorial is also available](http://web.archive.org/web/20130630141100/http://www.midnighthax.com/quickform.php), courtesy of the Internet Archive.

Moodle will attempt to provide a more complete tutorial in this documentation where possible.

Whilst much of the API originates in the PEAR package, all interaction with the library should be via the `moodleform` class, which acts as a controlling wrapper to HTML\_QuickForm.

## Basic Usage in A Normal Page[​](#basic-usage-in-a-normal-page "Direct link to Basic Usage in A Normal Page")

Generally the structure of a page with a form on it looks like this:

```
// You will process some page parameters at the top here and get the info about
// what instance of your module and what course you're in etc. Make sure you
// include hidden variable in your forms which have their defaults set in set_data
// which pass these variables from page to page.

// Setup $PAGE here.

// Instantiate the form that you defined.
$mform=new\plugintype_pluginname\form\myform();
// Default 'action' for form is strip_querystring(qualified_me()).

// Set the initial values, for example the existing data loaded from the database.
// This is typically an array of name/value pairs that match the
// names of data elements in the form.
// You can also use an object.
$mform->set_data($toform);

if($mform->is_cancelled()){
// You need this section if you have a cancel button on your form.
// You use this section to handle what to do if your user presses the cancel button.
// This is often a redirect back to an older page.
// NOTE: is_cancelled() should be called before get_data().
redirect($returnurl);

}elseif($fromform=$mform->get_data()){
// This branch is where you process validated data.

// Typically you finish up by redirecting to somewhere where the user
// can see what they did.
redirect($nexturl);
}

// If the form was not cancelled, and data was not submitted, then display the form.
echo$OUTPUT->header();
$mform->display();
echo$OUTPUT->footer();
```

You are encouraged to look at `lib/formslib.php` to see what additional functions and parameters are available. Available functions are well commented.

## Defining Your Form Class[​](#defining-your-form-class "Direct link to Defining Your Form Class")

The form class tells us about the structure of the form.

In most cases you can place this in an auto-loadable class, in which case it should be placed in a folder named `form`, for example:

```
<?php

namespacemod_forum\form;

classmyformextends\moodleform{
// ...
}
```

info

Historically it was not possible to auto-load classes. As a result, there are many parts of the core codebase which will manually require a file and expect a non-namespaced class name.

One example of this is in the activity edit form, which must be named `mod_[modname]_mod_form` and can either be located in `mod/[modname]/classes/mod_form.php` or in `mod/[modname]/mod_form.php`.

The name you give the class is used as the `id` attribute of your form in html. Any trailing '\_form' is removed. Your form class name should be unique in order for it to be selectable in CSS by theme designers who may want to adjust the css just for that form.

### definition()[​](#definition "Direct link to definition()")

Form definition is defined in further detail in the [Form definition](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition) documentation.

## Use in Activity Modules Add / Update Forms[​](#use-in-activity-modules-add--update-forms "Direct link to Use in Activity Modules Add / Update Forms")

The same form is used to create or edit an activity, but some legacy constraints still apply:

- The form *must* be named `mod_[modname]_mod_form`
- The class *must* be located in either:
  
  - `mod/[modname]/mod_form.php`; or
  - `mod/[modname]/classes/mod_form.php`
- The form *must* extend the `moodleform_mod` class.

### defaults\_preprocessing[​](#defaults_preprocessing "Direct link to defaults_preprocessing")

Since the data for the activity editing form is automatically filled from the database, you may need to pre-process this data to set values for some form fields. For example, in the Forum activity, in some situations a Unix Time Stamp is used to set a boolean checkbox.

This can be achieved using the `defaults_preprocessing` method.

### Post Processing[​](#post-processing "Direct link to Post Processing")

Whilst the pre-processing stage is performed in the `defaults_preprocessing` function, all post-processing is perform in the `[modname]_add_instance` and `[modname]_update_instance` functions in the activities `lib.php`.

These are called *after* data bas been validated by the Forms API.

### Standard activity form elements[​](#standard-activity-form-elements "Direct link to Standard activity form elements")

Moodle has a set of standard form elements used by all Activity modules. These allow for consistent control over activity visibility, group modes, and other common APIs.

The `standard_coursemodule_elements()` function is used to add these common elements, and it should be called *before* the standard action elements are added, for example:

```
classmod_example_mod_formextends\moodleform_mod{
publicfunctiondefinition(){
// Add the various form elements.
$this->_form->addElement(...);

// Add the standard elements.
$this->standard_coursemodule_elements();

// Add the form actions.
$this->add_action_buttons();
}
}
```