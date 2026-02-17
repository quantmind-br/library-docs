---
title: Editor API | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/apis/subsystems/editor
source: sitemap
fetched_at: 2026-02-17T15:45:22.121711-03:00
rendered_js: false
word_count: 188
summary: This document explains how to use the Moodle Editor API to programmatically set up and configure text editors, including general options and editor-specific settings.
tags:
    - moodle-development
    - editor-api
    - atto-editor
    - php-api
    - text-editor-setup
category: api
---

Version: main (5.2)

The editor API lets you control Moodle text editors. It can be found in `lib/editorlib.php`.

important

Normally you do not need to use this API directly because you can include editors as part of a Moodle form, which will automatically set up the editor for you.

## How to set up a text editor[​](#how-to-set-up-a-text-editor "Direct link to How to set up a text editor")

To set up a text editor on an existing HTML text area field:

- Call function `editors_get_preferred_editor()`, which will return an object of the texteditor class.
- Call function `use_editor()` to enable the editor for the text area.

For example, assuming there is an HTML text area with id `mytextareaid`:

```
$editor=editors_get_preferred_editor(FORMAT_HTML);
$editor->use_editor('mytextareaid');
```

## Editor options[​](#editor-options "Direct link to Editor options")

The use\_editor function allows an options array to be supplied.

### General options[​](#general-options "Direct link to General options")

- `context`: set to the current context object
- `enable_filemanagement`: set false to disable the file management plugin
- `autosave`: set false to disable autosave

### Atto-specific options[​](#atto-specific-options "Direct link to Atto-specific options")

- `toolbar`: set to override which icons appear on the toolbar (normally it uses the admin setting - this is for special cases for example if you want a minimal editor in a particular plugin).

The following example will cause atto to show the four buttons indicated.

```
$attobuttons='style1 = bold, italic'.PHP_EOL.'list = unorderedlist, orderedlist';
$editor->use_editor($id,[
'context'=>$context,
'autosave'=>false,
'atto:toolbar'=>$attobuttons
],[
'return_types'=>FILE_EXTERNAL,
]);
```