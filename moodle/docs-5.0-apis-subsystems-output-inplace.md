---
title: Inplace editable | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/apis/subsystems/output/inplace
source: sitemap
fetched_at: 2026-02-17T15:27:55.827117-03:00
rendered_js: false
word_count: 535
summary: This document explains how to implement the inplace_editable API in Moodle plugins to enable direct editing of values on a page. It covers defining callbacks, implementing the templatable class, and configuring various UI types like text, toggles, and dropdowns.
tags:
    - moodle-development
    - inplace-editable
    - plugin-development
    - ui-component
    - php
    - frontend
category: tutorial
---

The `inplace_editable` element is a mini-API which allows developers to easily support editing of a value on any page. The interface is used in places such as the course section and activity name editing.

![inplace editable example.png](https://moodledev.io/assets/images/inplace_editable_example-4c04e1dc88f0488bb8798b34e131b69b.png)

## Implementing inplace\_editable in a plugin[​](#implementing-inplace_editable-in-a-plugin "Direct link to Implementing inplace_editable in a plugin")

The best way is to explain the usage on a simple example. Imagine we have plugin `tool_mytest` that needs to implement in-place editing of a field 'name' from db table `tool_mytest_mytable`. We are going to call this itemtype `mytestname`. Each plugin (or core component) may use as many item types as it needs.

Define a callback in `/admin/tool/mytest/lib.php` that starts with the plugin name and ends with `_inplace_editable`:

admin/tool/mytest/lib.php

```
functiontool_mytest_inplace_editable($itemtype,$itemid,$newvalue){
global$DB;

if($itemtype==='mytestname'){
$record=$DB->get_record('tool_mytest_mytable',['id'=>$itemid],'*',MUST_EXIST);

// Must call validate_context for either system, or course or course module context.
// This will both check access and set current context.
\external_api::validate_context(context_system::instance());

// Check permission of the user to update this item.
require_capability('tool/mytest:update',context_system::instance());

// Clean input and update the record.
$newvalue=clean_param($newvalue,PARAM_NOTAGS);

$DB->update_record('tool_mytest_mytable',['id'=>$itemid,'name'=>$newvalue));

// Prepare the element for the output:
$record->name=$newvalue;

returnnew\core\output\inplace_editable(
'tool_mytest',
'mytestname',
$record->id,
true,
format_string($record->name),
$record->name,
get_string('editmytestnamefield','tool_mytest'),
get_string('newvaluestring','tool_mytest',format_string($record->name))
);
}
}
```

In your renderer or wherever you actually display the name, use the same `inplace_editable` template:

```
$tmpl=new\core\output\inplace_editable(
'tool_mytest',
'mytestname',
$record->id,
has_capability('tool/mytest:update',context_system::instance()),
format_string($record->name),
$record->name,
newlang_string('editmytestnamefield','tool_mytest'),
newlang_string('newvaluestring','tool_mytest',format_string($record->name))
);
echo$OUTPUT->render($tmpl);
```

This was a very simplified example, in the real life you will probably want to:

- Create a function (or class extending `core\output\inplace_editable`) to form the instance of templatable object so you don't need to duplicate code;
- Use an existing function to update a record (which hopefully also validates input value and triggers events)
- Add unit tests and behat tests

View example

admin/tool/mytest/classes/local/inplace\_edit\_text.php

```

classinplace_edit_textextends\core\output\inplace_editable{
/**
     * Constructor.
     *
     * @param object $record
     */
publicfunction__construct($record){
parent::__construct(
component:'tool_mytest',
// The item type as managed your plugin.
            itemtype:'mytesttext',
// An ID that relates to this instance of this item type.
            itemid:$record->id,
// Whether this user can makes changes.
// Perhaps based upon a capability check.
            editable:has_capability(
'capname',
\context_system::instance(),
),
// The display value of this item.
            displayvalue:format_string($record->name),
// The machine-readable value.
            value:$record->name,
// Hints and labels.
            edithint:get_string('edithint','tool_mytest'),
editlabel:get_string('editlabel','tool_mytest'),
);
$this->set_type_select($answeroptionstemp);
}

/**
     * Updates the value in database and returns itself.
     *
     * Called from inplace_editable callback
     *
     * @param int $itemid
     * @param mixed $newvalue
     * @return \self
     */
publicstaticfunctionupdate($itemid,$newvalue){
// Clean the new value.
$newvalue=clean_param($newvalue,PARAM_INT);

// {{ Do some mighty things here}}

$record=$DB->get_record('xxx',['id'=>'xxx']);

// Finally return itself.
returnnewself($record);
}
}
```

## Toggles and dropdowns[​](#toggles-and-dropdowns "Direct link to Toggles and dropdowns")

You may choose to set the UI for your inplace editable element to be a string value (default), toggle or dropdown.

Examples of dropdown setup (see also [example by overriding class](https://github.com/moodle/moodle/blob/main/tag/classes/output/tagareacollection.php)):

```
$tagcollections=\core_tag_collection::get_collections_menu(true);
$tmpl=new\core\output\inplace_editable(
'core_tag',
'tagareacollection',
$tagarea->id,
$editable,

// Note that $displayvalue is not needed (null was passed in the example above).
// It will be automatically taken from options.
null,

// $value must be an existing index from the $tagcollections array,
// otherwise exception will be thrown.
$value,
$edithint,
$editlabel
);
$tmpl->set_type_select($tagcollections);
```

Example of toggle setup (see also [example by overriding class](https://github.com/moodle/moodle/blob/main/tag/classes/output/tagareaenabled.php)):

```
$tmpl=new\core\output\inplace_editable(
'core_tag',

'tagflag',

$tag->id,

$editable,

// $displayvalue usually toggles an image, for example closed/open eye.
// It is easier to implement by overriding the class.
// In this case $displayvalue can be generated from $value during exporting.
$displayvalue,

// $value must be an existing element of the array
// passed to set_type_toggle(), otherwise exception will be thrown.
$value,

$hint,
);
$tmpl->set_type_toggle([0,1]);
```

View example

admin/tool/mytest/classes/local/inplace\_edit\_select.php

```
classinplace_edit_selectextends\core\output\inplace_editable{
/**
     * Constructor.
     *
     * @param \stdClass $record
     */
publicfunction__construct($record){
// Get the options for inplace_edit select box.
// The array needs the format:
//     $options = [
//         'value1' => 'text1',
//         'value2' => 'text2',
//     ];
$options=\tool_mytest\classes\helper::get_options();

parent::__construct(
component:'tool_mytest',
// The item type as managed your plugin.
            itemtype:'mytestselect',
// An ID that relates to this instance of this item type.
            itemid:$record->id,
// Whether this user can makes changes.
// Perhaps based upon a capability check.
            editable:has_capability(
'capname',
\context_system::instance(),
),
// The display value of this item.
            displayvalue:$options[$optionkey],
// The machine-readable value.
            value:$optionkey,
// Hints and labels.
            edithint:get_string('edithint','tool_mytest'),
editlabel:get_string('editlabel','tool_mytest'),
);
$this->set_type_select($options);
}

/**
     * Updates the value in database and returns itself.
     *
     * Called from inplace_editable callback
     *
     * @param int $itemid
     * @param mixed $newvalue
     * @return \self
     */
publicstaticfunctionupdate($itemid,$newvalue){
// Clean the new value.
$newvalue=clean_param($newvalue,PARAM_INT);

// {{ Do some mighty things here}}

$record=$DB->get_record('xxx',['id'=>'xxx']);

// Finally return itself.
returnnewself($record);
}
}
```

View example rendering with PHP

```
$renderer=$PAGE->get_renderer('core');
$inplaceedit=newtool_mytest\local\inplace_edit_text($record);
$params=$inplaceedit->export_for_template($renderer);
echo$OUTPUT->render_from_template('core/inplace_editable',$params);
```

View example rendering with JavaScript

Render inplace\_edit with JavaScript

```
$itemid=153// Id of the element to be modified inplace.
$renderer=$PAGE->get_renderer('core');
$inplaceedit=newtool_mytest\local\inplace_edit_text($record);
$params=$inplaceedit->export_for_template($renderer);
```

The params are transferred via webservice and are then processed by JavaScript

```
Templates.renderForPromise('core/inplace_editable', params)
.then(({html, js})=>{
Templates.replaceNodeContents('nodeid', html, js);
returntrue;
})
.catch((error)=>displayException(error));
```

note

In the examples above, `core/inplace_edit` can also be used as a partial in another template.

## How does it work[​](#how-does-it-work "Direct link to How does it work")

`inplace_editable` consists of

- Templatable/renderable **class core\\output\\inplace\_editable**
- Template **core/inplace\_editable**
- JavaScript module **core/inplace\_editable**
- Web service **core\_update\_inplace\_editable** available from AJAX

All four call each other so it's hard to decide where we start explaining this circle of friends but let's start with web service.

1. **Web service** receives arguments (`$component`, `$itemtype`, `$itemid`, `$newvalue`) - it searches for the inplace\_editable callback in the component. Then web service calls this callback as `{component}_inplace_editable($itemtype, $itemid, $newvalue)`, this must return templatable element which is sent back to the web service caller. Web service requires user to be logged in. **Any other `capability/access` checks must be performed inside the callback.**
2. **Templatable element** contains such properties as component, `itemtype`, `itemid`, `displayvalue`, `value`, `editlabel` and `edithint`. When used in a **template** It only renders the display value and the edit link (with `title=edithint`). All other properties are rendered as `data-xxx` attributes. Template also ensures that JavaScript module is loaded.
3. **JavaScript module** registers a listener to when the edit link is clicked and then it replaces the display value with the text input box that allows to edit value. When user presses "Enter" the AJAX request is called to the web service and code from the component is executed. If web service throws an exception it is displayed for user as a popup.

## Events[​](#events "Direct link to Events")

Plugin page can listen to JQuery events that are triggered on successful update or when update failed. Example of the listeners (as inline JS code):

```
$PAGE->requires->js_amd_inline("
require(['jquery', 'core/local/inplace_editable/events'], function(\$, Events) {
    $('body').on(Events.eventTypes.elementUpdateFailed, '[data-inplaceeditable]', (e) => {
        // The exception object returned by the callback.
        const exception = e.exception;

        // The value that user tried to udpated the element to.
        const newvalue = e.newvalue;

        // This will prevent default error dialogue.
        e.preventDefault();

        // Do your own error processing here.
    });
    $('body').on(Events.eventTypes.elementUpdated, '[data-inplaceeditable]', (e) => {
        // Everything that web service returned.
        const ajaxreturn = e.ajaxreturn;

        // Element value before editing (note, this is raw value and not display value).
        const oldvalue = e.oldvalue;

        // Do your own stuff, for example update all other occurences of this element on the page.
    });
});
");
```

note

The above examples are not recommended and just give an example of how these APIs work.