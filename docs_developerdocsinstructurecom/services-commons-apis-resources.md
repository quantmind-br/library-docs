---
title: Resources | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/commons/apis/resources
source: sitemap
fetched_at: 2026-02-15T09:14:59.531713-03:00
rendered_js: false
word_count: 1907
summary: This document provides technical specifications for the Canvas Commons API endpoints used to manage, search, and preview learning resources. It details methods for creating and updating resource metadata, performing filtered searches, and retrieving media preview sources.
tags:
    - canvas-commons
    - learning-object-repository
    - rest-api
    - resource-management
    - content-search
    - media-previews
category: api
---

/api/resources/{resourceId}/document-preview

Returns a redirect (303) to a document preview iframe URL for the specified resource.

`curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/resources/0123456789/document-preview?documentId=abcdefg"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

resourceIdstringRequired

The unique identifier for the resource

documentIdstringOptional

The document ID to preview (optional, defaults to the latest version's document)

303

Redirect to document preview iframe URL

/api/resources/{resourceId}/document-preview

### List Formats for a Media Preview

/api/resources/{resourceId}/media-preview-sources

Lists the sources to use in a video or audio tag for a given resource.

`curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/resources/0123456789/media-preview-sources"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

resourceIdstringRequired

The unique identifier for the resource

mediaObjectIdstringOptional

The specific media object Id requested for previewing (optional)

/api/resources/{resourceId}/media-preview-sources

Create a resource.

**Upload Example:**

```
# Create the resource record
curl -X POST -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data @data.json "https://lor.instructure.com/api/resources"
data.json:
{
  "title": "The War of the Worlds",
  "description": "Watch out for black smoke, and heat rays. The Martians are invading!",
  "licenseIds": ["attribution_noderivs"],
  "licenseSpecs": "You are free to: Share — copy and redistribute the material in any medium or format",
  "thumbnail": {
    "url": "http://lor-images.s3.amazonaws.com/subjects/english-language-arts/English-05-262x147.jpg",
    "description": "Close up of fountain pen on old letter"
  },
  "gradeIds": ["1", "2", "3"],
  "scopeIds": [ "PUBLIC" ],
  "subjectIds": ["math", "specialty"],
  "type": "discussion",
  "tags": ["Science Fiction", "Martian People"],
  "upload": {
    "contentType": "application/pdf",
    "checksum": "crU95OObMRyOS/XyvDD7Tw=="
  }
}

# Upload the actual file
curl -X PUT -H "Content-Type: application/pdf" -H "Content-MD5: <base64 encoded md5>" --data @war-of-the-worlds.pdf <response.meta.uploadUrl>

# Let Commons know the upload is complete
curl -H "X-Session-ID: 0123456789" <response.meta.uploadSuccessRedirectUrl>
```

**Export Example:**

```
# Create the resource record
curl -X POST -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data @data.json "https://lor.instructure.com/api/resources"
data.json:
{
  "title": "The War of the Worlds",
  "description": "Watch out for black smoke, and heat rays. The Martians are invading!",
  "licenseIds": ["attribution"],
  "licenseSpecs": "You are free to: Share — copy and redistribute the material in any medium or format",
  "thumbnail": {
    "url": "http://lor-images.s3.amazonaws.com/subjects/english-language-arts/English-05-262x147.jpg",
    "description": "Close up of fountain pen on old letter"
  },
  "gradeIds": ["1", "2", "3"],
  "scopeIds": [ "PUBLIC" ],
  "subjectIds": ["math", "specialty"],
  "type": "discussion",
  "tags": ["Science Fiction", "Martian People"],
  "export": {
    "contentType": "application/pdf",
    "url": "https://canvas.instructure.com/files/1337/download?download_frd=1&verifier=LIMRsQ4AbWNPgMSoQHkf5SsxULnn61mevsdpZY9X"
  }
}
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

titlestring · min: 1 · max: 250Required

The title of the resource.

descriptionstring · min: 1 · max: 2000Required

The description of the resource.

licenseSpecsstring · min: 1 · max: 400Optional

Details of the resource's licence terms.

scopeIdsstring\[]Optional

An array of scope ids the resource will be accessible to.

typestring · enumRequiredPossible values:

tagsstring\[] · min: 1 · max: 10Required

An array of tags to associate with the resource.

mediaObjectIdstringOptional

The ID of a media object in Canvas that is required when a media file (audio/video) is being exported from Canvas

Search through resources the current user has permission to view. The results are listed by relevance if a `q` parameter is present, otherwise the results are listed by update date, most recent first.

**Example:**

```
curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/resources?q=ratio&gradeIds=4,5,6&types=course,quiz"
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

qstringOptional

The text to search for in the title, description, tags, author name, and account name

accountIdstringOptional

If specified, public resources shared by that account are shown unless the user searching is an admin

scopeIdsstringOptional

Comma separated account, consortium(prefixed with 'consortium-'), group(prefixed with 'group-'), or user ids to filter resources by. 'PUBLIC' is also a valid value for finding public resources

sortBystring · enumOptional

The order search results are returned in. All results are returned in descending order.

Default: `relevance`Possible values:

sortOrderstring · enumOptional

Sort results asc or desc (default=desc).

Default: `desc`Possible values:

authorIdsstringOptional

Comma separated ids for authors that created or shared resources to find

sizeintegerOptional

The number of results to return

Default: `24`

exportStatusstring · enumOptional

The readiness of the resource for use.

Possible values:

cursorstringOptional

An identifier from a prior query to continue retrieving results for

scrollstringOptional

If present, the search will use the Scroll API. Check the meta object for the scroll ID

scrollIdstringOptional

When doing a Scroll API search, only this param is needed in order to continue the search

gradeIdsstring · enumOptional

An array of grade ids to associate with the resource

Possible values:

subjectIdsstring · enumOptional

An array of subject ids to associate with the resource

Possible values:

typestring · enumOptional

Deprecated. The type of resource

Possible values:

typesstring · enumOptional

Comma separated resource types to find

Possible values:

### Update Meta Data for a Resource

Update the title, description, tags, and other meta data associated with a resource. Resource creators or administrators are allowed to update the meta data of a resource. If the resource is shared to a group then the group manager can also update the meta data of the resource.

**Example:**

```
curl -X PUT -H "X-Session-ID: 0123456789" -H "Content-Type:application/json" --data @data.json "https://lor.instructure.com/api/resources/abcdef"
data.json:
{
  "title": "The Invisible Man",
  "description": "Be careful when messing around with the refractive index",
  "export": {
    "url": "http://www.hogwartsishere.com/about/",
    "contentType": "application/pdf"
  },
  "licenseIds": ["attribution_noncommercial_sharealike"],
  "licenseSpecs": "You are free to: Share — copy and redistribute the material in any medium or format Adapt — remix, transform, and build upon the material",
  "thumbnail": {
    "url": "http://lor-images.s3.amazonaws.com/subjects/english-language-arts/English-05-262x147.jpg",
    "description": "Close up of fountain pen on old letter"
  },
  "gradeIds": ["1", "2", "3"],
  "scopeIds": ["PUBLIC"],
  "subjectIds": ["math", "specialty"],
  "tags": ["Science Fiction", "Invisible People"],
  "versionNotes": "This corrects the typo on page 220."
}
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

idstringRequired

The unique id of the resource

titlestring · min: 1 · max: 250Optional

The title of the resource.

descriptionstring · min: 1 · max: 2000Optional

The description of the resource.

licenseSpecsstring · min: 1 · max: 400Optional

Details of the resource's licence terms.

scopeIdsstring\[]Optional

An array of scope ids the resource will be accessible to.

tagsstring\[] · min: 1 · max: 10Optional

An array of tags to associate with the resource.

versionNotesstring · min: 1 · max: 350Optional

Any changes that you made to the resource should be described here

### Remove a Single Resource from Commons

Resource creators or administrators are allowed to remove a resource from Commons. If the resource was shared to a group then the group manager can also remove the resource from Commons.

**Example:**

```
curl -X DELETE -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/resources/abcdef"
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

idstringRequired

The unique id of the resource

204

Resource deleted successfully

/api/resources/{resourceId}/report

Report a resource as spam, infringing, or inappropriate.

**Example:**

```
curl -X POST -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data @data.json "https://lor.instructure.com/api/resources/1231231/report"
data.json:
{
  "reportType": "spam"
}
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

resourceIdstringRequired

The resourceId to mark as reported

reportTypestring · enumRequiredPossible values:

201

Resource reported successfully

/api/resources/{resourceId}/report

### Update a Resource with a New Version

/api/resources/{id}/new-version

Create an update for a resource by uploading a new version of the file.

**Upload Example:**

```
# Update the resource record
curl -X PUT -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data @data.json "https://lor.instructure.com/api/resources/abcdef/new-version"
data.json:
{
  "title": "The Time Traveler",
  "description": "An Adventure through time",
  "licenseIds": ["attribution_sharealike"],
  "licenseSpecs": "You are free to: Share — copy and redistribute the material in any medium or format",
  "thumbnail": {
    "url": "http://lor-images.s3.amazonaws.com/subjects/english-language-arts/English-05-262x147.jpg",
    "description": "Close up of fountain pen on old letter"
  },
  "gradeIds": ["1", "2", "3"],
  "scopeIds": ["PUBLIC"],
  "subjectIds": ["math", "specialty"],
  "tags": ["Science Fiction", "Time Travel"],
  "upload": {
    "contentType": "application/pdf",
    "checksum": "crU95OObMRyOS/XyvDD7Tw=="
  },
  "versionNotes": "This corrects the typo on page 284."
}

# Upload the actual file for the new version
curl -X PUT -H "Content-Type: application/pdf" -H "Content-MD5: <base64 encoded md5>" --data @war-of-the-worlds.pdf <response.meta.uploadUrl>

# Let Commons know the upload is complete
curl -H "X-Session-ID: 0123456789" <response.meta.uploadSuccessRedirectUrl>
```

**Export Example:**

```
# Update the resource record
curl -X PUT -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data @data.json "https://lor.instructure.com/api/resources/abcdef/new-version"
data.json:
{
  "title": "The Time Traveler",
  "description": "An Adventure through time!",
  "licenseIds": ["attribution_sharealike"],
  "licenseSpecs": "You are free to: Share — copy and redistribute the material in any medium or format",
  "thumbnail": {
    "url": "http://lor-images.s3.amazonaws.com/subjects/english-language-arts/English-05-262x147.jpg",
    "description": "Close up of fountain pen on old letter"
  },
  "gradeIds": ["1", "2", "3"],
  "scopeIds": ["PUBLIC"],
  "subjectIds": ["math", "specialty"],
  "tags": ["Science Fiction", "Time Travel"],
  "export": {
    "contentType": "application/pdf",
    "url": "https://canvas.instructure.com/files/1337/download?download_frd=1&verifier=LIMRsQ4AbWNPgMSoQHkf5SsxULnn61mevsdpZY9X"
  },
  "versionNotes": "This corrects the typo on page 284."
}
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

idstringRequired

The unique id of the resource

titlestring · min: 1 · max: 250Optional

The title of the resource.

descriptionstring · min: 1 · max: 2000Optional

The description of the resource.

licenseSpecsstring · min: 1 · max: 400Optional

Details of the resource's licence terms.

scopeIdsstring\[]Optional

An array of scope ids the resource will be accessible to.

tagsstring\[] · min: 1 · max: 10Required

An array of tags to associate with the resource.

versionNotesstring · min: 1 · max: 350Required

Any changes that you made to the resource should be described here

/api/resources/{id}/new-version

/api/resources/{id}/download

Get a redirect to a url that will download the resource.

**Example:**

```
curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/resources/abcdef/download"
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

idstringRequired

The unique id of the resource

303

Url where the resource can be downloaded

/api/resources/{id}/download

### Preview an Image Resource

/api/resources/{id}/image-preview

Get a redirect to a resized version of the original image resource.

**Example:**

```
curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/resources/abcdef/image-preview"
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

idstringRequired

The unique id of the resource

303

Location Url of the preview image

/api/resources/{id}/image-preview

### Inform of Upload Being Complete

/api/resources/versions/{versionId}/upload-complete

**This is not implemented!** This will start processing an upload. Remember, depending on the file size of the resource, the import process may take as long as 30 minutes.

**Example:**

```
curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/resources/versions/012344564789/upload-complete"
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

versionIdstringRequired

The unique id of the resource version

/api/resources/versions/{versionId}/upload-complete

### Import Latest Version of Resource into Canvas Course

/api/resources/{id}/import

Import the latest version of a resource from Commons into a single or multiple Canvas courses. A successful import will partly rely on the user having the proper permissions in Canvas to import resources into the Canvas course.

**Example:**

```
curl -X POST -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data @data.json "https://lor.instructure.com/api/resources/abcdef/import"
data.json:
{
  "courses":[
      {
        "id": 220,
        "name": "Algebra 1"
      },
      {
        "id": 284,
        "name": "Partial Differential Equations"
      }
  ]
}
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

idstringRequired

The unique id of the resource

/api/resources/{id}/import

### Create a new module in a Canvas Course

/api/resources/modules/new

Create a new module in a Canvas Course. Success will depend on the user having the proper permissions in Canvas to create new modules in the given course.

**Example:**

```
curl -X POST -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" "https://lor.instructure.com/api/resources/abcdef/modules/new"
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

/api/resources/modules/new

### Create a new assignment group in a Canvas Course

/api/resources/assignment-group/new

Create a new assignment group in a Canvas Course. Success will depend on the user having the proper permissions in Canvas to create new assignment groups in the given course.

**Example:**

```
curl -X POST -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" "https://lor.instructure.com/api/resources/abcdef/assignment-group/new"
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

/api/resources/assignment-group/new

### Get placeholder thumbnail

/api/resources/placeholder-thumbnail

Gets the placeholder thumbnail for a resource.

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

/api/resources/placeholder-thumbnail

/api/resources/thumbnails

List all of the possible thumbnails that Commons provides that can be used for a resource.

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

/api/resources/thumbnails

/api/resources/{id}/thumbnails

List all of the possible thumbnails that can be used for that resource. Note: For video type resources, the only thumbnail that will be listed is the one that was automatically generated from that video when it was uploaded.

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

idstringRequired

The unique id of the resource

/api/resources/{id}/thumbnails

Post a thumbnail image. The image needs to be a PNG, GIF, or JPEG. Animated GIFs will be decomposed and only the first frame will be kept. Animated GIFs must be well-formed. This endpoint does not accept files greater than 1 MB in size. The image will be automatically resized and cropped to 262x147 pixels (16:9 aspect ratio) in a jpg format. The image must be at least 262x147 pixels to be accepted. Thumbnails must be uploaded as multipart/form-data.

**Example:**

```
curl -X POST -H "X-Session-ID: 0123456789" -F "thumbnail=@example.png" "https://lor.instructure.com/api/resources/thumbnail"
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

thumbnailstring · binaryOptional

The image file to upload (PNG, GIF, or JPEG)

200

The url for the thumbnail

/api/resources/{resourceId}

Get a single resource by its ID.

**Example:**

```
curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/resources/abcdef"
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

resourceIdstringRequired

The id of the resource to retrieve

/api/resources/{resourceId}

### Redirects from commons to canvas resource page

/api/resources/{resourceId}/source

Redirects from commons to the Canvas resource page.

**Example:**

```
curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/resources/abcdef/source"
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

resourceIdstringRequired

The id of the resource to redirect to

302

Redirect to Canvas resource page

/api/resources/{resourceId}/source

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).