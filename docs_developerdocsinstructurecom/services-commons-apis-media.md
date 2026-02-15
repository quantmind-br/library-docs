---
title: Media | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/commons/apis/media
source: sitemap
fetched_at: 2026-02-15T09:14:49.128349-03:00
rendered_js: false
word_count: 87
summary: Describes a deprecated API endpoint used for creating Docviewer or Notorious media objects for previewing, restricted specifically to the Common Cartridge Manager.
tags:
    - deprecated
    - media-creation
    - api-endpoint
    - docviewer
    - notorious
    - ccm
category: api
---

### Create a Docviewer or Notorious item (DEPRECATED)

**DEPRECATED**: This endpoint will be removed. Only to be invoked via CCM (Common Cartridge Manager) to create a media object for previewing. This endpoint will not be allowed for any other requestor.

**Example:**

```
  curl -X POST -H "Authorization: Basic dev" -H "Content-Type: application/json" --data @data.json "https://lor.instructure.com/api/media"
  data.json:
  {
    "callbackUrl": "wwww.callback-when-finished-url.com",
    "fileName": "name-of-file.pdf",
    "fileUrl": "www.path-to-file.com"
  }
```

callbackUrlstringRequired

URL for callback on media creation success

fileUrlstringRequired

Valid URL for resource to be processed

200

Media creation request accepted

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).