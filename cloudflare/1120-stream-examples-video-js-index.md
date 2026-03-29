---
title: Video.js
url: https://developers.cloudflare.com/stream/examples/video-js/index.md
source: llms
fetched_at: 2026-01-24T15:23:36.211207228-03:00
rendered_js: false
word_count: 35
summary: This document provides a code example for implementing video playback in web applications using the Video.js player and Cloudflare Stream.
tags:
    - cloudflare-stream
    - video-js
    - playback
    - hls
    - frontend
category: tutorial
---

---
title: Video.js · Cloudflare Stream docs
description: Example of video playback with Cloudflare Stream and Video.js
lastUpdated: 2025-08-18T14:27:42.000Z
chatbotDeprioritize: false
tags: Playback
source_url:
  html: https://developers.cloudflare.com/stream/examples/video-js/
  md: https://developers.cloudflare.com/stream/examples/video-js/index.md
---

```html
<html>
  <head>
    <link
      href="https://cdnjs.cloudflare.com/ajax/libs/video.js/7.10.2/video-js.min.css"
      rel="stylesheet"
    />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/video.js/7.10.2/video.min.js"></script>
  </head>
  <body>
    <video-js id="vid1" controls preload="auto">
      <source
        src="https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.m3u8"
        type="application/x-mpegURL"
      />
    </video-js>


    <script>
      const vid = document.getElementById('vid1');
      const player = videojs(vid);
    </script>
  </body>
</html>
```

Refer to the [Video.js documentation](https://docs.videojs.com/) for more information.