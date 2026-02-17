---
title: Files in Forms | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/apis/subsystems/form/usage/files
source: sitemap
fetched_at: 2026-02-17T15:27:49.125593-03:00
rendered_js: false
word_count: 1528
summary: This document explains how to integrate file upload and management capabilities into Moodle forms using the File API and specific form elements like filepicker, filemanager, and editor.
tags:
    - moodle-development
    - file-api
    - moodle-forms
    - file-upload
    - php-development
    - file-management
category: guide
---

Files and their metadata are stored within the [File API](https://moodledev.io/docs/5.0/apis/subsystems/files). Each file within the API is associated with:

- a context id;
- a component;
- a *file area*; and
- an optional item id.

This combination acts as a virtual bucket, within which any desired file structure may be used.

A common use case is to allow users to upload file content within a standard Moodle form.

Normally this works as follows:

1. User starts to create, or re-edit an existing item - this may be a forum post, resource, glossary entry, and so on.
2. User presses some sort of button to browse for new files to attach or embed
3. User sees our "Choose file..." dialog, which contains one or more repository instances.
4. User chooses a file, the corresponding [Repository plugin](https://moodledev.io/docs/5.0/apis/plugintypes/repository) takes care of copying the file into a "draft file area" within Moodle
5. File appears in the text or as an attachment in the form.
6. When the user hits save, the [File API](https://moodledev.io/docs/5.0/apis/subsystems/files) is invoked to move the file from the draft file area into a permanent file area associated with that data

This document shows you how to use Moodle forms to interact with users in a standard and secure way.

If you just want to write code to manipulate Moodle files internally (without user input) you can use the [File API](https://moodledev.io/docs/5.0/apis/subsystems/files) without involving form elements.

## Form elements[​](#form-elements "Direct link to Form elements")

There are three file-related form elements for interacting with users:

1. `filepicker` - a way to specify one file for the case when you want to process the file and throw it away
2. `filemanager` - a way to attach one or more files as a collection, using the file picker interface
3. `editor` - a way to specify a textarea with a HTML editor, and all the handling of images and movies within that HTML

### File picker[​](#file-picker "Direct link to File picker")

The *File picker* may be used directly to allow a user to upload *one* file so that it can be processed, and then removed.

Example use-cases include allowing a single file to be uploaded for a purpose such as CSV import, or restoration of a backup.

note

A filepicker element does not typically support storing data within the File API.

If you want a file that remains part of the Moodle storage and will reappear when you reopen the form, then you should use a filemanager instead (and restrict it to a single file, if necessary).

#### Using the filepicker element[​](#using-the-filepicker-element "Direct link to Using the filepicker element")

```
$mform->addElement(
'filepicker',
'userfile',
get_string('file'),
null,
[
'maxbytes'=>$maxbytes,
'accepted_types'=>'*',
]
);
```

#### Working with an uploaded file[​](#working-with-an-uploaded-file "Direct link to Working with an uploaded file")

To get the contents of the uploaded file:

```
$content=$mform->get_file_content('userfile');
```

To get the name of the uploaded file:

```
$name=$mform->get_new_filename('userfile');
```

To save the uploaded file to the server filesystem:

```
$success=$mform->save_file('userfile',$fullpath,$override);
```

note

Be wary of this approach if you need to use the file in multiple page requests.

A clustered server installation will need the file to be accessible on any server node.

To store the chosen file in the Moodle file API:

```
$storedfile=$mform->save_stored_file('userfile',...);
```

### File manager[​](#file-manager "Direct link to File manager")

The File Manager element improves on file picker by allowing you to manage more than one file. It is expected that the files will be stored permanently for future use.

Examples of the File manager can be found all over Moodle and include the Forum, and Glossary attachments, Course files, and more.

#### Add a file manager element[​](#add-a-file-manager-element "Direct link to Add a file manager element")

Example:

```
$mform->addElement(
'filemanager',
'attachments',
get_string('attachment','moodle'),
null,
[
'subdirs'=>0,
'maxbytes'=>$maxbytes,
'areamaxbytes'=>10485760,
'maxfiles'=>50,
'accepted_types'=>['document'],
'return_types'=>FILE_INTERNAL|FILE_EXTERNAL,
]
);
```

When a user uploads files, these are stored into a *draft* file area for that user. It is the developers responsibility to then move those files within the File API.

#### Loading existing files into draft area[​](#loading-existing-files-into-draft-area "Direct link to Loading existing files into draft area")

If you are presenting a form which has previously had data saved to it, for example when editing an existing piece of content, you will need to copy all of the existing files into the draft file area used in the form. This can be achieved using the `file_prepare_draft_area` function, for example:

```
// Fetch the entry being edited, or create a placeholder.
if(empty($id)){
$entry=(object)[
'id'=>null,
];
}else{
$entry=$DB->get_records('glossary_entries',['id'=>$id]);
}

// Get an unused draft itemid which will be used for this form.
$draftitemid=file_get_submitted_draft_itemid('attachments');

// Copy the existing files which were previously uploaded
// into the draft area used by this form.
file_prepare_draft_area(
// The $draftitemid is the target location.
$draftitemid,

// The combination of contextid / component / filearea / itemid
// form the virtual bucket that files are currently stored in
// and will be copied from.
$context->id,
'mod_glossary',
'attachment',
$entry->id,
[
'subdirs'=>0,
'maxbytes'=>$maxbytes,
'maxfiles'=>50,
]
);

// Set the itemid of draft area that the files have been moved to.
$entry->attachments=$draftitemid;
$mform->set_data($entry);
```

#### Store updated set of files[​](#store-updated-set-of-files "Direct link to Store updated set of files")

During the processing of the submitted data, the developer handling the form will need to handle storing the files in an appropriate part of the File API.

This can be accomplished using the `file_save_draft_area_files()` function, for example:

```
if($data=$mform->get_data()){
// ... store or update $entry.

// Now save the files in correct part of the File API.
file_save_draft_area_files(
// The $data->attachments property contains the itemid of the draft file area.
$data->attachments,

// The combination of contextid / component / filearea / itemid
// form the virtual bucket that file are stored in.
$context->id,
'mod_glossary',
'attachment',
$entry->id,

[
'subdirs'=>0,
'maxbytes'=>$maxbytes,
'maxfiles'=>50,
]
);
}
```

### Editors[​](#editors "Direct link to Editors")

Another common place to handle files is within an HTML editor, such as TinyMCE.

There are two ways of using the editor element in code, the first one is easier but expects some standardised fields. The second method is more low level.

All of the methods share key behaviours:

- When preparing the editor:
  
  - You must create a draft file area to store the files while the user is making changes.
- When using the editor:
  
  - Any files referenced use a full URL, for example `https://example.com/pluginfile.php/123/user/icon/456/filedir/filename.png`.
  - These files are stored in the draft file area.
- When processing the form submission:
  
  - You must process the content so that part of the URL is replaced with a placeholder - usually `@@PLUGINFILE@@`. For example the URL may become `@@PLUGINFILE@@/filedir/filename.png`.
  - You must pass it through a function to move the files from the draft file area into the correct file area for your code.
- When displaying the editor content:
  
  - You must pass it through `file_rewrite_pluginfile_urls()` to rewrite it back to a servable URL.
  - You must provide a `pluginfile` function to perform access control checks and serve the file.
- When fetching existing content for editing:
  
  - You must copy it into a new draft file area so that changes can be made.
  - You must rewrite the `@@PLUGINFILE@@` URL with the new draft file area.

#### Simple use[​](#simple-use "Direct link to Simple use")

By creating a series of fields in the database, it is very easy to have standard functions fetch and store the data for this editor. For example, if you wanted to store data in a field called `textfield`, you would need to create fields in the database for:

- `textfield` - where the content is actually stored
- `textfieldformat` - to store the *format* of the field
- `textfieldtrust` (optional) - to store whether the text is trusted

This is then paired with a set of options which are used when adding the Editor for the form, and processing the file content before displaying, and after saving the form, for example:

```
$textfieldoptions=[
'trusttext'=>true,
'subdirs'=>true,
'maxfiles'=>$maxfiles,
'maxbytes'=>$maxbytes,
'context'=>$context,
];
```

To add the editor to the form, and process the form data:

1. Add editor `textfield_editor` to moodle form, pass options through custom data in form constructor. You should set `$data->id` to null if data not exist yet.

```
$mform->addElement(
'editor',
'textfield_editor',
get_string('fieldname','somemodule'),
null,
$textfieldoptions
);
```

1. Prepare the data - this will ensure that any existing files will be copied to the draft file area, and any existing placeholder is replaced for use in the form.

```
$data=file_prepare_standard_editor(
// The existing data.
$data,

// The field name in the database.
'textfield',

// The options.
$textfieldoptions,

// The combination of contextid, component, filearea, and itemid.
$context,
'mod_somemodule',
'somearea',
$data->id
);
```

1. After the form is submitted, process the editor - this will move the files from the draft file area into the persistent storage, and rewrite the URLs to use the placeholder.

```
$data=file_postupdate_standard_editor(
// The submitted data.
$data,

// The field name in the database.
'textfield',

// The options.
$textfieldoptions,

// The combination of contextid, component, filearea, and itemid.
$context,
'mod_somemodule',
'somearea',
$data->id
);
```

Real world examples can be found in `mod/glossary/edit.php` and `mod/glossary/comment.php`.

#### Low-level use[​](#low-level-use "Direct link to Low-level use")

If you prefer, you can call the various underlying functions yourself. This is not typically required.

Important

You must call both the pre-processing, and post-processing, functions to ensure the correct behaviour.

1. detect if the form was already submitted (this usually means that the draft area already exists) - `file_get_submitted_draft_itemid()`
2. prepare a draft file area for temporary storage of all files attached to the text - `file_prepare_draft_area()`
3. convert encoded relative links to absolute links - `file_prepare_draft_area()`
4. create the form and set current data
5. after submission the changed files must be merged back into original area - `file_save_draft_area_files()`
6. absolute links have to be replaced by relative links - `file_save_draft_area_files()`

##### Prepare current data - text and files[​](#prepare-current-data---text-and-files "Direct link to Prepare current data - text and files")

```
if(empty($entry->id)){
$entry=(object)[
'id'=>null,
'definition'=>'',
'format'=>FORMAT_HTML,
];
}

$draftid_editor=file_get_submitted_draft_itemid('entry');
$currenttext=file_prepare_draft_area(
$draftid_editor,
$context->id,
'mod_glossary',
'entry',
$entry->id,
[
'subdirs'=>true),
$entry->definition,
]
);
$entry->entry=[
'text'=>$currenttext,
'format'=>$entry->format,
'itemid'=>$draftid_editor,
];

$mform->set_data($entry);
```

note

Multiple files can be stored in the same virtual bucket. They will have different file names and/or file paths within the same item id.

##### Obtain text, format and save draft files[​](#obtain-text-format-and-save-draft-files "Direct link to Obtain text, format and save draft files")

To retrieve editor content, you need to use following code:

```
if($fromform=$mform->get_data()){
// Content of the editor field.
$messagetext=$fromform->entry['text'];
// Format of the content.
$messageformat=$fromform->entry['format'];
}
```

When a user selects a file using the file picker, the file is initially stored in a draft file area, and a URL is inserted into the HTML in the editor that lets the person editing the content (but no one else) see the file.

When the user submits the form, we then need to save the draft files to the correct place in permanent storage. (Just like you have to call `$DB->update_record('tablename', $data);` to have the other parts of the form submission stored correctly.)

The `save_files_from_draft_area` function and replace absolute links with internal relative links do:

```
$messagetext=file_save_draft_area_files(
// The id of the draft file area.
$draftideditor,

// The combination of contextid / component / filearea / itemid
// form the virtual bucket that file are stored in.
$context->id,
'mod_glossary',
'entry',
$entry->id,

// The options to pass.
[
'subdirs'=>true,
],

// The text received from the form.
$messagetext
);
```

All URLs in content that point to files managed to the File API are converted to a form that starts `@@PLUGINFILE@@/` before the content is stored in the database. That is what we mean by rewriting.

## File serving[​](#file-serving "Direct link to File serving")

### Convert internal relative links to absolute links[​](#convert-internal-relative-links-to-absolute-links "Direct link to Convert internal relative links to absolute links")

Before text content is displayed to the user, any URLs in the `@@PLUGINFILE@@/` form in the content need to be rewritten to the real URL where the user can access the files.

```
$messagetext=file_rewrite_pluginfile_urls(
// The content of the text stored in the database.
$messagetext,
// The pluginfile URL which will serve the request.
'pluginfile.php',

// The combination of contextid / component / filearea / itemid
// form the virtual bucket that file are stored in.
$context->id,
'frankenstyle_component',
'filearea',
$itemid
);
```

### Implement file serving access control[​](#implement-file-serving-access-control "Direct link to Implement file serving access control")

Attachments and embedded images should have the same access control as the text itself. In a majority of cases these files are served using `pluginfile.php`. Access control is defined in the `[componentpath]/lib.php` file, using a function named `[componentname]_pluginfile()`.

## File browsing support[​](#file-browsing-support "Direct link to File browsing support")

Only owner of each file area is allowed to use low level File API function to access files, other parts of Moodle should use file browsing API.

Activities may specify browsing support in own `module/lib.php` file by implementing functions `module_get_file_areas()` and `module_get_file_info()`.

## See also[​](#see-also "Direct link to See also")

- [File API](https://moodledev.io/docs/5.0/apis/subsystems/files)
- [Using the file API](https://moodledev.io/docs/5.0/apis/subsystems/files)
- [Repository plugins](https://moodledev.io/docs/5.0/apis/plugintypes/repository)