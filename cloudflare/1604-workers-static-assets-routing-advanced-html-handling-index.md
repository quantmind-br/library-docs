---
title: HTML handling · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/static-assets/routing/advanced/html-handling/index.md
source: llms
fetched_at: 2026-01-24T15:32:22.470269183-03:00
rendered_js: false
word_count: 659
summary: This document explains how to configure trailing slash behavior for HTML assets in Cloudflare Workers using the html_handling setting. It covers automatic, forced, and dropped trailing slash options to help manage SEO and canonical URL patterns.
tags:
    - cloudflare-workers
    - wrangler-config
    - html-handling
    - trailing-slashes
    - seo-optimization
    - static-assets
category: configuration
---

Forcing or dropping trailing slashes on request paths (for example, `example.com/page/` vs. `example.com/page`) is often something that developers wish to control for cosmetic reasons. Additionally, it can impact SEO because search engines often treat URLs with and without trailing slashes as different, separate pages. This distinction can lead to duplicate content issues, indexing problems, and overall confusion about the correct canonical version of a page.

The [`assets.html_handling` configuration](https://developers.cloudflare.com/workers/wrangler/configuration/#assets) determines the redirects and rewrites of requests for HTML content. It is used to specify the pattern for canonical URLs, thus where Cloudflare serves HTML content from, and additionally, where Cloudflare redirects non-canonical URLs to.

Take the following directory structure:

## Automatic trailing slashes (default)

This will usually give you the desired behavior automatically: individual files (e.g. `foo.html`) will be served *without* a trailing slash and folder index files (e.g. `foo/index.html`) will be served *with* a trailing slash.

* wrangler.jsonc

  ```jsonc
  {
    "name": "my-worker",
    "compatibility_date": "2026-01-24",
    "assets": {
      "directory": "./dist/",
      "html_handling": "auto-trailing-slash"
    }
  }
  ```

* wrangler.toml

  ```toml
  name = "my-worker"
  compatibility_date = "2026-01-24"


  [assets]
  directory = "./dist/"
  html_handling = "auto-trailing-slash"
  ```

Based on the incoming requests, the following assets would be served:

| Incoming Request | Response | Asset Served |
| - | - | - |
| /file | 200 | /dist/file.html |
| /file.html | 307 to /file | - |
| /file/ | 307 to /file | - |
| /file/index | 307 to /file | - |
| /file/index.html | 307 to /file | - |
| /folder | 307 to /folder/ | - |
| /folder.html | 307 to /folder | - |
| /folder/ | 200 | /dist/folder/index.html |
| /folder/index | 307 to /folder | - |
| /folder/index.html | 307 to /folder | - |

## Force trailing slashes

Alternatively, you can force trailing slashes (`force-trailing-slash`).

* wrangler.jsonc

  ```jsonc
  {
    "name": "my-worker",
    "compatibility_date": "2026-01-24",
    "assets": {
      "directory": "./dist/",
      "html_handling": "force-trailing-slash"
    }
  }
  ```

* wrangler.toml

  ```toml
  name = "my-worker"
  compatibility_date = "2026-01-24"


  [assets]
  directory = "./dist/"
  html_handling = "force-trailing-slash"
  ```

Based on the incoming requests, the following assets would be served:

| Incoming Request | Response | Asset Served |
| - | - | - |
| /file | 307 to /file/ | - |
| /file.html | 307 to /file/ | - |
| /file/ | 200 | /dist/file.html |
| /file/index | 307 to /file/ | - |
| /file/index.html | 307 to /file/ | - |
| /folder | 307 to /folder/ | - |
| /folder.html | 307 to /folder/ | - |
| /folder/ | 200 | /dist/folder/index.html |
| /folder/index | 307 to /folder/ | - |
| /folder/index.html | 307 to /folder/ | - |

## Drop trailing slashes

Or you can drop trailing slashes (`drop-trailing-slash`).

* wrangler.jsonc

  ```jsonc
  {
    "name": "my-worker",
    "compatibility_date": "2026-01-24",
    "assets": {
      "directory": "./dist/",
      "html_handling": "drop-trailing-slash"
    }
  }
  ```

* wrangler.toml

  ```toml
  name = "my-worker"
  compatibility_date = "2026-01-24"


  [assets]
  directory = "./dist/"
  html_handling = "drop-trailing-slash"
  ```

Based on the incoming requests, the following assets would be served:

| Incoming Request | Response | Asset Served |
| - | - | - |
| /file | 200 | /dist/file.html |
| /file.html | 307 to /file | - |
| /file/ | 307 to /file | - |
| /file/index | 307 to /file | - |
| /file/index.html | 307 to /file | - |
| /folder | 200 | /dist/folder/index.html |
| /folder.html | 307 to /folder | - |
| /folder/ | 307 to /folder | - |
| /folder/index | 307 to /folder | - |
| /folder/index.html | 307 to /folder | - |

## Disable HTML handling

Alternatively, if you have bespoke needs, you can disable the built-in HTML handling entirely (`none`).

* wrangler.jsonc

  ```jsonc
  {
    "name": "my-worker",
    "compatibility_date": "2026-01-24",
    "assets": {
      "directory": "./dist/",
      "html_handling": "none"
    }
  }
  ```

* wrangler.toml

  ```toml
  name = "my-worker"
  compatibility_date = "2026-01-24"


  [assets]
  directory = "./dist/"
  html_handling = "none"
  ```

Based on the incoming requests, the following assets would be served:

| Incoming Request | Response | Asset Served |
| - | - | - |
| /file | Depends on `not_found_handling` | Depends on `not_found_handling` |
| /file.html | 200 | /dist/file.html |
| /file/ | Depends on `not_found_handling` | Depends on `not_found_handling` |
| /file/index | Depends on `not_found_handling` | Depends on `not_found_handling` |
| /file/index.html | Depends on `not_found_handling` | Depends on `not_found_handling` |
| /folder | Depends on `not_found_handling` | Depends on `not_found_handling` |
| /folder.html | Depends on `not_found_handling` | Depends on `not_found_handling` |
| /folder/ | Depends on `not_found_handling` | Depends on `not_found_handling` |
| /folder/index | Depends on `not_found_handling` | Depends on `not_found_handling` |
| /folder/index.html | 200 | /dist/folder/index.html |