---
title: Choice Dropdown | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/apis/subsystems/form/fields/choicedropdown
source: sitemap
fetched_at: 2026-02-17T15:14:28.421778-03:00
rendered_js: false
word_count: 121
summary: This document explains how to implement the choicedropdown form field and the choicelist data definition to create enhanced selection menus with icons and descriptions.
tags:
    - form-api
    - choicedropdown
    - choicelist
    - ui-components
    - dropdown-menu
category: api
---

The `choicedropdown` form field creates a dropdown list with multiple options. It is different from a standard select dropdown in that each option can have extra icons and descriptions. This field is often used in forms to facilitate the selection of a non-trivial option that demands additional information.

While most form API fields use primitive data types, the `choicedropdown` form field uses a particular data definition called `choicelist`. This data definition is an abstraction that represents a user choice list and is used in other UI components like `core\output\local\dropdown\status` or `core\output\local\action_menu\subpanel`.

The `choicelist` class provides a way to define a list of options with additional information such as icons, descriptions, the currently selected option, or the ability to disable specific options.

```
// Define the options for the dropdown list.
$options=newcore\output\choicelist();
$options->add_option(
'option1',
"Text option 1",
[
'description'=>'Option 1 description',
'icon'=>newpix_icon('t/hide','Eye icon 1'),
]
);
$options->add_option(
'option2',
"Text option 2",
[
'description'=>'Option 2 description',
'icon'=>newpix_icon('t/stealth','Eye icon 2'),
]
);
$options->add_option(
'option3',
"Text option 3",
[
'description'=>'Option 3 description',
'icon'=>newpix_icon('t/show','Eye icon 3'),
]
);

// Add the choicedropdown field to the form.
$mform->addElement(
'choicedropdown',
'FIELDNAME',
get_string('FIELDNAME','PLUGINNAME'),
$options,
);
$mform->setDefault('FIELDNAME',$defaultvalue);
```