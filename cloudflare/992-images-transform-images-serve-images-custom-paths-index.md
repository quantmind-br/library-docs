---
title: Serve images from custom paths · Cloudflare Images docs
url: https://developers.cloudflare.com/images/transform-images/serve-images-custom-paths/index.md
source: llms
fetched_at: 2026-01-24T15:15:45.134252155-03:00
rendered_js: false
word_count: 352
summary: This document explains how to use Cloudflare Transform Rules to rewrite URLs for image transformation services, covering custom paths, parameter mapping, and automated formatting.
tags:
    - cloudflare-images
    - transform-rules
    - url-rewrite
    - image-transformation
    - regex-matching
category: guide
---

You can use Transform Rules to rewrite URLs for every image that you transform through Images.

This page covers examples for the following scenarios:

* Serve images from custom paths
* Modify existing URLs to be compatible with transformations in Images
* Transform every image requested on your zone with Images

To create a rule:

1. In the Cloudflare dashboard, go to the **Rules Overview** page.

   [Go to **Overview**](https://dash.cloudflare.com/?to=/:account/:zone/rules/overview)

2. Select **Create rule** next to **URL Rewrite Rules**.

## Before you start

Every rule runs before and after the transformation request.

If the path for the request matches the path where the original images are stored on your server, this may cause the request to fetch the original image to loop.

To direct the request to the origin server, you can check for the string `image-resizing` in the `Via` header:

`...and (not (any(http.request.headers["via"][*] contains "image-resizing")))`

## Serve images from custom paths

By default, requests to transform images through Images are served from the `/cdn-cgi/image/` path. You can use Transform Rules to rewrite URLs.

### Basic version

Free and Pro plans support string matching rules (including wildcard operations) that do not require regular expressions.

This example lets you rewrite a request from `example.com/images` to `example.com/cdn-cgi/image/`:

```txt
(starts_with(http.request.uri.path, "/images")) and (not (any(http.request.headers["via"][*] contains "image-resizing")))
```

```txt
concat("/cdn-cgi/image", substring(http.request.uri.path, 7))
```

### Advanced version

Note

This feature requires a Business or Enterprise plan to enable regex in Transform Rules. Refer to [Cloudflare Transform Rules Availability](https://developers.cloudflare.com/rules/transform/#availability) for more information.

There is an advanced version of Transform Rules supporting regular expressions.

This example lets you rewrite a request from `example.com/images` to `example.com/cdn-cgi/image/`:

```txt
(http.request.uri.path matches "^/images/.*$") and (not (any(http.request.headers["via"][*] contains "image-resizing")))
```

```txt
regex_replace(http.request.uri.path, "^/images/", "/cdn-cgi/image/")
```

## Modify existing URLs to be compatible with transformations in Images

Note

This feature requires a Business or Enterprise plan to enable regex in Transform Rules. Refer to [Cloudflare Transform Rules Availability](https://developers.cloudflare.com/rules/transform/#availability) for more information.

This example lets you rewrite your URL parameters to be compatible with Images:

```txt
(http.request.uri matches "^/(.*)\\?width=([0-9]+)&height=([0-9]+)$")
```

```txt
regex_replace(
  http.request.uri,
  "^/(.*)\\?width=([0-9]+)&height=([0-9]+)$",
  "/cdn-cgi/image/width=${2},height=${3}/${1}"
)
```

Leave the **Query** > **Rewrite to** > *Static* field empty.

## Pass every image requested on your zone through Images

Note

This feature requires a Business or Enterprise plan to enable regular expressions in Transform Rules. Refer to [Cloudflare Transform Rules Availability](https://developers.cloudflare.com/rules/transform/#availability) for more information.

This example lets you transform every image that is requested on your zone with the `format=auto` option:

```txt
(http.request.uri.path.extension matches "(jpg)|(jpeg)|(png)|(gif)") and (not (any(http.request.headers["via"][*] contains "image-resizing")))
```

```txt
regex_replace(http.request.uri.path, "/(.*)", "/cdn-cgi/image/format=auto/${1}")
```