---
title: hls.js
url: https://developers.cloudflare.com/stream/examples/hls-js/index.md
source: llms
fetched_at: 2026-01-24T15:23:28.980143626-03:00
rendered_js: false
word_count: 39
summary: This document provides a code example for integrating the hls.js library with Cloudflare Stream to enable HLS video playback in a web browser.
tags:
    - cloudflare-stream
    - hls-js
    - video-playback
    - hls
    - javascript
    - streaming-video
category: tutorial
---

---
title: hls.js · Cloudflare Stream docs
description: Example of video playback with Cloudflare Stream and the HLS
  reference player (hls.js)
lastUpdated: 2025-08-18T14:27:42.000Z
chatbotDeprioritize: false
tags: Playback
source_url:
  html: https://developers.cloudflare.com/stream/examples/hls-js/
  md: https://developers.cloudflare.com/stream/examples/hls-js/index.md
---

```html
<html>
  <head>
    <script src="//cdn.jsdelivr.net/npm/hls.js@latest"></script>
  </head>
  <body>
    <video id="video"></video>
    <script>
      if (Hls.isSupported()) {
        const video = document.getElementById('video');
        const hls = new Hls();
        hls.attachMedia(video);
        hls.on(Hls.Events.MEDIA_ATTACHED, () => {
          hls.loadSource(
            'https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.m3u8'
          );
        });
      }


      video.play();
    </script>
  </body>
</html>
```

Refer to the [hls.js documentation](https://github.com/video-dev/hls.js/blob/master/docs/API.md) for more information.