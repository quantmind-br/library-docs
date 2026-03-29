---
title: Stream Player
url: https://developers.cloudflare.com/stream/examples/stream-player/index.md
source: llms
fetched_at: 2026-01-24T15:23:34.928341334-03:00
rendered_js: false
word_count: 38
summary: This document provides a code example for embedding a video using the Cloudflare Stream Player within an HTML iframe.
tags:
    - cloudflare-stream
    - video-playback
    - iframe-embed
    - html5-video
    - web-development
category: tutorial
---

---
title: Stream Player · Cloudflare Stream docs
description: Example of video playback with the Cloudflare Stream Player
lastUpdated: 2025-08-18T14:27:42.000Z
chatbotDeprioritize: false
tags: Playback
source_url:
  html: https://developers.cloudflare.com/stream/examples/stream-player/
  md: https://developers.cloudflare.com/stream/examples/stream-player/index.md
---

```html
<html>
  <head> </head>
  <body>
    <div style="position: relative; padding-top: 56.25%;">
    <iframe
      src="https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/iframe?poster=https%3A%2F%2Fcustomer-f33zs165nr7gyfy4.cloudflarestream.com%2F6b9e68b07dfee8cc2d116e4c51d6a957%2Fthumbnails%2Fthumbnail.jpg%3Ftime%3D%26height%3D600"
      style="border: none; position: absolute; top: 0; left: 0; height: 100%; width: 100%;"
      allow="accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;"
      allowfullscreen="true"
    ></iframe>
    </div>
  </body>
</html>
```

Refer to the [Using the Stream Player](https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/) for more information.