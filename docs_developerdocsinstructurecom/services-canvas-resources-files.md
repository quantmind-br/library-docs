---
title: Files | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/files
source: sitemap
fetched_at: 2026-02-15T09:00:36.055445-03:00
rendered_js: false
word_count: 1906
summary: This document provides a technical specification for an API used to manage files, folders, and storage quotas, including detailed data models for objects and their associated endpoints.
tags:
    - file-management
    - api-specification
    - canvas-lms
    - storage-quota
    - rest-api
    - usage-rights
category: api
---

An API for managing files and folders See the File Upload Documentation for details on the file upload workflow.

**A File object looks like:**

```
{
"id": 569,
"folder_id": 4207,
"display_name": "file.txt",
"filename": "file.txt",
"content-type": "text/plain",
"url": "http://www.example.com/files/569/download?download_frd=1",
  // file size in bytes
"size": 43451,
"created_at": "2012-07-06T14:58:50Z",
"updated_at": "2012-07-06T14:58:50Z",
"unlock_at": "2012-07-07T14:58:50Z",
"locked": false,
"hidden": false,
"lock_at": "2012-07-20T14:58:50Z",
"hidden_for_user": false,
  // Changes who can access the file. Valid options are 'inherit' (the default),
  // 'course', 'institution', and 'public'. Only valid in course endpoints.
"visibility_level": "course",
"thumbnail_url": null,
"modified_at": "2012-07-06T14:58:50Z",
  // simplified content-type mapping
"mime_class": "html",
  // identifier for file in third-party transcoding service
"media_entry_id": "m-3z31gfpPf129dD3sSDF85SwSDFnwe",
"locked_for_user": false,
"lock_info": null,
"lock_explanation": "This assignment is locked until September 1 at 12:00am",
  // optional: url to the document preview. This url is specific to the user
  // making the api call. Only included in submission endpoints.
"preview_url": null
}
```

**A Folder object looks like:**

```
{
  "context_type": "Course",
  "context_id": 1401,
  "files_count": 0,
  "position": 3,
  "updated_at": "2012-07-06T14:58:50Z",
  "folders_url": "https://www.example.com/api/v1/folders/2937/folders",
  "files_url": "https://www.example.com/api/v1/folders/2937/files",
  "full_name": "course files/11folder",
  "lock_at": "2012-07-06T14:58:50Z",
  "id": 2937,
  "folders_count": 0,
  "name": "11folder",
  "parent_folder_id": 2934,
  "created_at": "2012-07-06T14:58:50Z",
  "unlock_at": null,
  "hidden": false,
  "hidden_for_user": false,
  "locked": true,
  "locked_for_user": false,
  // If true, indicates this is a read-only folder containing files submitted to
  // assignments
  "for_submissions": false
}
```

**An UsageRights object looks like:**

```
// Describes the copyright and license information for a File
{
  // Copyright line for the file
  "legal_copyright": "(C) 2014 Incom Corporation Ltd",
  // Justification for using the file in a Canvas course. Valid values are
  // 'own_copyright', 'public_domain', 'used_by_permission', 'fair_use',
  // 'creative_commons'
  "use_justification": "creative_commons",
  // License identifier for the file.
  "license": "cc_by_sa",
  // Readable license name
  "license_name": "CC Attribution Share-Alike",
  // Explanation of the action performed
  "message": "4 files updated",
  // List of ids of files that were updated
  "file_ids": [1, 2, 3]
}
```

**A License object looks like:**

```
{
  // a short string identifying the license
  "id": "cc_by_sa",
  // the name of the license
  "name": "CC Attribution ShareAlike",
  // a link to the license text
  "url": "http://creativecommons.org/licenses/by-sa/4.0"
}
```

[FilesController#api\_quotaarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

`GET /api/v1/courses/:course_id/files/quota`

**Scope:** `url:GET|/api/v1/courses/:course_id/files/quota`

`GET /api/v1/groups/:group_id/files/quota`

**Scope:** `url:GET|/api/v1/groups/:group_id/files/quota`

`GET /api/v1/users/:user_id/files/quota`

**Scope:** `url:GET|/api/v1/users/:user_id/files/quota`

Returns the total and used storage quota for the course, group, or user.

**Example Request:**

```
curl 'https://<canvas>/api/v1/courses/1/files/quota' \
      -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
{ "quota": 524288000, "quota_used": 402653184 }
```

[FilesController#api\_indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

`GET /api/v1/courses/:course_id/files`

**Scope:** `url:GET|/api/v1/courses/:course_id/files`

`GET /api/v1/users/:user_id/files`

**Scope:** `url:GET|/api/v1/users/:user_id/files`

`GET /api/v1/groups/:group_id/files`

**Scope:** `url:GET|/api/v1/groups/:group_id/files`

`GET /api/v1/folders/:id/files`

**Scope:** `url:GET|/api/v1/folders/:id/files`

Returns the paginated list of files for the folder or course.

**Request Parameters:**

Filter results by content-type. You can specify type/subtype pairs (e.g., ‘image/jpeg’), or simply types (e.g., ‘image’, which will match ‘image/gif’, ‘image/jpeg’, etc.).

Exclude given content-types from your results. You can specify type/subtype pairs (e.g., ‘image/jpeg’), or simply types (e.g., ‘image’, which will match ‘image/gif’, ‘image/jpeg’, etc.).

The partial name of the files to match and return.

Array of additional information to include.

- “user”
  
  the user who uploaded the file or last edited its content
- “usage\_rights”
  
  copyright and license information for the file (see UsageRights)

Allowed values: `user`

Array of information to restrict to. Overrides include\[]

- “names”
  
  only returns file name information

Sort results by this field. Defaults to ‘name’. Note that ‘sort=user`implies`include\[]=user`.</p> Allowed values:`name`,`size`,`created\_at`,`updated\_at`,`content\_type`,`user\`

The sorting order. Defaults to ‘asc’.

Allowed values: `asc`, `desc`

**Example Request:**

```
curl 'https://<canvas>/api/v1/folders/<folder_id>/files?content_types[]=image&content_types[]=text/plain \
      -H 'Authorization: Bearer <token>'
```

Returns a list of [File](https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/plagiarism_detection_submissions#file) objects.

[FilesController#public\_urlarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

`GET /api/v1/files/:id/public_url`

**Scope:** `url:GET|/api/v1/files/:id/public_url`

Determine the URL that should be used for inline preview of the file.

**Request Parameters:**

The id of the submission the file is associated with. Provide this argument to gain access to a file that has been submitted to an assignment (Canvas will verify that the file belongs to the submission and the calling user has rights to view the submission).

**Example Request:**

```
curl 'https://<canvas>/api/v1/files/1/public_url' \
      -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
{ "public_url": "https://example-bucket.s3.amazonaws.com/example-namespace/attachments/1/example-filename?AWSAccessKeyId=example-key&Expires=1400000000&Signature=example-signature" }
```

[FilesController#api\_showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

`GET /api/v1/files/:id`

**Scope:** `url:GET|/api/v1/files/:id`

`POST /api/v1/files/:id`

**Scope:** `url:POST|/api/v1/files/:id`

`GET /api/v1/courses/:course_id/files/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/files/:id`

`GET /api/v1/groups/:group_id/files/:id`

**Scope:** `url:GET|/api/v1/groups/:group_id/files/:id`

`GET /api/v1/users/:user_id/files/:id`

**Scope:** `url:GET|/api/v1/users/:user_id/files/:id`

Returns the standard attachment json object

**Request Parameters:**

Array of additional information to include.

- “user”
  
  the user who uploaded the file or last edited its content
- “usage\_rights”
  
  copyright and license information for the file (see UsageRights)

Allowed values: `user`

`replacement_chain_context_type`

When a user replaces a file during upload, Canvas keeps track of the “replacement chain.”

Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.

Must be set to ‘course’ or ‘account’. The “replacement\_chain\_context\_id” parameter must also be included.

`replacement_chain_context_id`

When a user replaces a file during upload, Canvas keeps track of the “replacement chain.”

Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.

Indicates the context ID Canvas should use when following the “replacement chain.” The “replacement\_chain\_context\_type” parameter must also be included.

**Example Request:**

```
curl 'https://<canvas>/api/v1/files/<file_id>' \
      -H 'Authorization: Bearer <token>'
curl 'https://<canvas>/api/v1/courses/<course_id>/files/<file_id>' \
      -H 'Authorization: Bearer <token>'
```

Returns a [File](https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/plagiarism_detection_submissions#file) object.

[FilesController#file\_refarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

`GET /api/v1/courses/:course_id/files/file_ref/:migration_id`

**Scope:** `url:GET|/api/v1/courses/:course_id/files/file_ref/:migration_id`

Get information about a file from a course copy file reference

**Example Request:**

```
curl https://<canvas>/api/v1/courses/1/files/file_ref/i567b573b77fab13a1a39937c24ae88f2 \
     -H 'Authorization: Bearer <token>'
```

Returns a [File](https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/plagiarism_detection_submissions#file) object.

[FilesController#api\_updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

`PUT /api/v1/files/:id`

**Scope:** `url:PUT|/api/v1/files/:id`

Update some settings on the specified file

**Request Parameters:**

The new display name of the file, with a limit of 255 characters.

The id of the folder to move this file into. The new folder must be in the same context as the original parent folder. If the file is in a context without folders this does not apply.

If the file is moved to a folder containing a file with the same name, or renamed to a name matching an existing file, the API call will fail unless this parameter is supplied.

- “overwrite”
  
  Replace the existing file with the same name
- “rename”
  
  Add a qualifier to make the new filename unique

Allowed values: `overwrite`, `rename`

The datetime to lock the file at

The datetime to unlock the file at

Configure which roles can access this file

**Example Request:**

```
curl -X PUT 'https://<canvas>/api/v1/files/<file_id>' \
     -F 'name=<new_name>' \
     -F 'locked=true' \
     -H 'Authorization: Bearer <token>'
```

Returns a [File](https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/plagiarism_detection_submissions#file) object.

[FilesController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

`DELETE /api/v1/files/:id`

**Scope:** `url:DELETE|/api/v1/files/:id`

Remove the specified file. Unlike most other DELETE endpoints, using this endpoint will result in comprehensive, irretrievable destruction of the file. It should be used with the ‘replace\` parameter set to true in cases where the file preview also needs to be destroyed (such as to remove files that violate privacy laws).

**Request Parameters:**

This action is irreversible. If replace is set to true the file contents will be replaced with a generic “file has been removed” file. This also destroys any previews that have been generated for the file. Must have manage files and become other users permissions

**Example Request:**

```
curl -X DELETE 'https://<canvas>/api/v1/files/<file_id>' \
     -H 'Authorization: Bearer <token>'
```

Returns a [File](https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/plagiarism_detection_submissions#file) object.

[FilesController#icon\_metadataarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

`GET /api/v1/files/:id/icon_metadata`

**Scope:** `url:GET|/api/v1/files/:id/icon_metadata`

Returns the icon maker file attachment metadata

**Example Request:**

```
curl 'https://<canvas>/api/v1/courses/1/files/1/metadata' \
      -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
{
  "type":"image/svg+xml-icon-maker-icons",
  "alt":"",
  "shape":"square",
  "size":"small",
  "color":"#FFFFFF",
  "outlineColor":"#65499D",
  "outlineSize":"large",
  "text":"Hello",
  "textSize":"x-large",
  "textColor":"#65499D",
  "textBackgroundColor":"#FFFFFF",
  "textPosition":"bottom-third",
  "encodedImage":"data:image/svg+xml;base64,PH==",
  "encodedImageType":"SingleColor",
  "encodedImageName":"Health Icon",
  "x":"50%",
  "y":"50%",
  "translateX":-54,
  "translateY":-54,
  "width":108,
  "height":108,
  "transform":"translate(-54,-54)"
}
```

[FilesController#reset\_verifierarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/files_controller.rb)

`POST /api/v1/files/:id/reset_verifier`

**Scope:** `url:POST|/api/v1/files/:id/reset_verifier`

Resets the link verifier. Any existing links to the file using the previous hard-coded “verifier” parameter will no longer automatically grant access.

Must have manage files and become other users permissions

**Example Request:**

```
curl -X POST 'https://<canvas>/api/v1/files/<file_id>/reset_verifier' \
     -H 'Authorization: Bearer <token>'
```

Returns a [File](https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/plagiarism_detection_submissions#file) object.

[FoldersController#api\_indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

`GET /api/v1/folders/:id/folders`

**Scope:** `url:GET|/api/v1/folders/:id/folders`

Returns the paginated list of folders in the folder.

**Example Request:**

```
curl 'https://<canvas>/api/v1/folders/<folder_id>/folders' \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [Folder](https://developerdocs.instructure.com/services/canvas/resources/files#folder) objects.

[FoldersController#list\_all\_foldersarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

`GET /api/v1/courses/:course_id/folders`

**Scope:** `url:GET|/api/v1/courses/:course_id/folders`

`GET /api/v1/users/:user_id/folders`

**Scope:** `url:GET|/api/v1/users/:user_id/folders`

`GET /api/v1/groups/:group_id/folders`

**Scope:** `url:GET|/api/v1/groups/:group_id/folders`

Returns the paginated list of all folders for the given context. This will be returned as a flat list containing all subfolders as well.

**Example Request:**

```
curl 'https://<canvas>/api/v1/courses/<course_id>/folders' \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [Folder](https://developerdocs.instructure.com/services/canvas/resources/files#folder) objects.

[FoldersController#resolve\_patharrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

`GET /api/v1/courses/:course_id/folders/by_path/*full_path`

**Scope:** `url:GET|/api/v1/courses/:course_id/folders/by_path/*full_path`

`GET /api/v1/courses/:course_id/folders/by_path`

**Scope:** `url:GET|/api/v1/courses/:course_id/folders/by_path`

`GET /api/v1/users/:user_id/folders/by_path/*full_path`

**Scope:** `url:GET|/api/v1/users/:user_id/folders/by_path/*full_path`

`GET /api/v1/users/:user_id/folders/by_path`

**Scope:** `url:GET|/api/v1/users/:user_id/folders/by_path`

`GET /api/v1/groups/:group_id/folders/by_path/*full_path`

**Scope:** `url:GET|/api/v1/groups/:group_id/folders/by_path/*full_path`

`GET /api/v1/groups/:group_id/folders/by_path`

**Scope:** `url:GET|/api/v1/groups/:group_id/folders/by_path`

Given the full path to a folder, returns a list of all Folders in the path hierarchy, starting at the root folder, and ending at the requested folder. The given path is relative to the context’s root folder and does not include the root folder’s name (e.g., “course files”). If an empty path is given, the context’s root folder alone is returned. Otherwise, if no folder exists with the given full path, a Not Found error is returned.

**Example Request:**

```
curl 'https://<canvas>/api/v1/courses/<course_id>/folders/by_path/foo/bar/baz' \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [Folder](https://developerdocs.instructure.com/services/canvas/resources/files#folder) objects.

[FoldersController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

`GET /api/v1/courses/:course_id/folders/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/folders/:id`

`GET /api/v1/users/:user_id/folders/:id`

**Scope:** `url:GET|/api/v1/users/:user_id/folders/:id`

`GET /api/v1/groups/:group_id/folders/:id`

**Scope:** `url:GET|/api/v1/groups/:group_id/folders/:id`

`GET /api/v1/folders/:id`

**Scope:** `url:GET|/api/v1/folders/:id`

Returns the details for a folder

You can get the root folder from a context by using ‘root’ as the :id. For example, you could get the root folder for a course like:

**Example Request:**

```
curl 'https://<canvas>/api/v1/courses/1337/folders/root' \
     -H 'Authorization: Bearer <token>'
```

```
curl 'https://<canvas>/api/v1/folders/<folder_id>' \
     -H 'Authorization: Bearer <token>'
```

Returns a [Folder](https://developerdocs.instructure.com/services/canvas/resources/files#folder) object.

[FoldersController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

`PUT /api/v1/folders/:id`

**Scope:** `url:PUT|/api/v1/folders/:id`

Updates a folder

**Request Parameters:**

The new name of the folder

The id of the folder to move this folder into. The new folder must be in the same context as the original parent folder.

The datetime to lock the folder at

The datetime to unlock the folder at

Flag the folder as locked

Flag the folder as hidden

Set an explicit sort position for the folder

**Example Request:**

```
curl -XPUT 'https://<canvas>/api/v1/folders/<folder_id>' \
     -F 'name=<new_name>' \
     -F 'locked=true' \
     -H 'Authorization: Bearer <token>'
```

Returns a [Folder](https://developerdocs.instructure.com/services/canvas/resources/files#folder) object.

[FoldersController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

`POST /api/v1/courses/:course_id/folders`

**Scope:** `url:POST|/api/v1/courses/:course_id/folders`

`POST /api/v1/users/:user_id/folders`

**Scope:** `url:POST|/api/v1/users/:user_id/folders`

`POST /api/v1/groups/:group_id/folders`

**Scope:** `url:POST|/api/v1/groups/:group_id/folders`

`POST /api/v1/folders/:folder_id/folders`

**Scope:** `url:POST|/api/v1/folders/:folder_id/folders`

`POST /api/v1/accounts/:account_id/folders`

**Scope:** `url:POST|/api/v1/accounts/:account_id/folders`

Creates a folder in the specified context

**Request Parameters:**

The id of the folder to store the new folder in. An error will be returned if this does not correspond to an existing folder. If this and parent\_folder\_path are sent an error will be returned. If neither is given, a default folder will be used.

The path of the folder to store the new folder in. The path separator is the forward slash ‘/\`, never a back slash. The parent folder will be created if it does not already exist. This parameter only applies to new folders in a context that has folders, such as a user, a course, or a group. If this and parent\_folder\_id are sent an error will be returned. If neither is given, a default folder will be used.

The datetime to lock the folder at

The datetime to unlock the folder at

Flag the folder as locked

Flag the folder as hidden

Set an explicit sort position for the folder

**Example Request:**

```
curl 'https://<canvas>/api/v1/folders/<folder_id>/folders' \
     -F 'name=<new_name>' \
     -F 'locked=true' \
     -H 'Authorization: Bearer <token>'
```

```
curl 'https://<canvas>/api/v1/courses/<course_id>/folders' \
     -F 'name=<new_name>' \
     -F 'locked=true' \
     -H 'Authorization: Bearer <token>'
```

Returns a [Folder](https://developerdocs.instructure.com/services/canvas/resources/files#folder) object.

[FoldersController#api\_destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

`DELETE /api/v1/folders/:id`

**Scope:** `url:DELETE|/api/v1/folders/:id`

Remove the specified folder. You can only delete empty folders unless you set the ‘force’ flag

**Request Parameters:**

Set to ‘true’ to allow deleting a non-empty folder

**Example Request:**

```
curl -X DELETE 'https://<canvas>/api/v1/folders/<folder_id>' \
     -H 'Authorization: Bearer <token>'
```

[FoldersController#create\_filearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

`POST /api/v1/folders/:folder_id/files`

**Scope:** `url:POST|/api/v1/folders/:folder_id/files`

Upload a file to a folder.

This API endpoint is the first step in uploading a file. See the [File Upload Documentation](https://developerdocs.instructure.com/services/canvas/basics/file.file_uploads) for details on the file upload workflow.

Only those with the “Manage Files” permission on a course or group can upload files to a folder in that course or group.

[FoldersController#copy\_filearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

`POST /api/v1/folders/:dest_folder_id/copy_file`

**Scope:** `url:POST|/api/v1/folders/:dest_folder_id/copy_file`

Copy a file from elsewhere in Canvas into a folder.

Copying a file across contexts (between courses and users) is permitted, but the source and destination must belong to the same institution.

**Request Parameters:**

The id of the source file

What to do if a file with the same name already exists at the destination. If such a file exists and this parameter is not given, the call will fail.

- “overwrite”
  
  Replace an existing file with the same name
- “rename”
  
  Add a qualifier to make the new filename unique

Allowed values: `overwrite`, `rename`

**Example Request:**

```
curl 'https://<canvas>/api/v1/folders/123/copy_file' \
     -H 'Authorization: Bearer <token>'
     -F 'source_file_id=456'
```

Returns a [File](https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/plagiarism_detection_submissions#file) object.

[FoldersController#copy\_folderarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

`POST /api/v1/folders/:dest_folder_id/copy_folder`

**Scope:** `url:POST|/api/v1/folders/:dest_folder_id/copy_folder`

Copy a folder (and its contents) from elsewhere in Canvas into a folder.

Copying a folder across contexts (between courses and users) is permitted, but the source and destination must belong to the same institution. If the source and destination folders are in the same context, the source folder may not contain the destination folder. A folder will be renamed at its destination if another folder with the same name already exists.

**Request Parameters:**

The id of the source folder

**Example Request:**

```
curl 'https://<canvas>/api/v1/folders/123/copy_folder' \
     -H 'Authorization: Bearer <token>'
     -F 'source_file_id=789'
```

Returns a [Folder](https://developerdocs.instructure.com/services/canvas/resources/files#folder) object.

[FoldersController#media\_folderarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/folders_controller.rb)

`GET /api/v1/courses/:course_id/folders/media`

**Scope:** `url:GET|/api/v1/courses/:course_id/folders/media`

`GET /api/v1/groups/:group_id/folders/media`

**Scope:** `url:GET|/api/v1/groups/:group_id/folders/media`

Returns the details for a designated upload folder that the user has rights to upload to, and creates it if it doesn’t exist.

If the current user does not have the permissions to manage files in the course or group, the folder will belong to the current user directly.

**Example Request:**

```
curl 'https://<canvas>/api/v1/courses/1337/folders/media' \
     -H 'Authorization: Bearer <token>'
```

Returns a [Folder](https://developerdocs.instructure.com/services/canvas/resources/files#folder) object.

[UsageRightsController#set\_usage\_rightsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/usage_rights_controller.rb)

`PUT /api/v1/courses/:course_id/usage_rights`

**Scope:** `url:PUT|/api/v1/courses/:course_id/usage_rights`

`PUT /api/v1/groups/:group_id/usage_rights`

**Scope:** `url:PUT|/api/v1/groups/:group_id/usage_rights`

`PUT /api/v1/users/:user_id/usage_rights`

**Scope:** `url:PUT|/api/v1/users/:user_id/usage_rights`

Sets copyright and license information for one or more files

**Request Parameters:**

List of ids of files to set usage rights for.

List of ids of folders to search for files to set usage rights for. Note that new files uploaded to these folders do not automatically inherit these rights.

Whether the file(s) or folder(s) should be published on save, provided that usage rights have been specified (set to ‘true\` to publish on save).

`usage_rights[use_justification]`

The intellectual property justification for using the files in Canvas

Allowed values: `own_copyright`, `used_by_permission`, `fair_use`, `public_domain`, `creative_commons`

`usage_rights[legal_copyright]`

The legal copyright line for the files

Returns an [UsageRights](https://developerdocs.instructure.com/services/canvas/resources/files#usagerights) object.

[UsageRightsController#remove\_usage\_rightsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/usage_rights_controller.rb)

`DELETE /api/v1/courses/:course_id/usage_rights`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/usage_rights`

`DELETE /api/v1/groups/:group_id/usage_rights`

**Scope:** `url:DELETE|/api/v1/groups/:group_id/usage_rights`

`DELETE /api/v1/users/:user_id/usage_rights`

**Scope:** `url:DELETE|/api/v1/users/:user_id/usage_rights`

Removes copyright and license information associated with one or more files

**Request Parameters:**

List of ids of files to remove associated usage rights from.

List of ids of folders. Usage rights will be removed from all files in these folders.

[UsageRightsController#licensesarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/usage_rights_controller.rb)

`GET /api/v1/courses/:course_id/content_licenses`

**Scope:** `url:GET|/api/v1/courses/:course_id/content_licenses`

`GET /api/v1/groups/:group_id/content_licenses`

**Scope:** `url:GET|/api/v1/groups/:group_id/content_licenses`

`GET /api/v1/users/:user_id/content_licenses`

**Scope:** `url:GET|/api/v1/users/:user_id/content_licenses`

A paginated list of licenses that can be applied

Returns a list of [License](https://developerdocs.instructure.com/services/canvas/resources/files#license) objects.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).