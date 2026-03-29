---
title: Shaka Player
url: https://developers.cloudflare.com/stream/examples/shaka-player/index.md
source: llms
fetched_at: 2026-01-24T15:23:32.122772605-03:00
rendered_js: false
word_count: 86
summary: This document provides instructions and code examples for integrating Shaka Player with Cloudflare Stream to play DASH and HLS video manifests.
tags:
    - cloudflare-stream
    - shaka-player
    - video-playback
    - dash
    - hls
    - javascript
category: tutorial
---

---
title: Shaka Player · Cloudflare Stream docs
description: Example of video playback with Cloudflare Stream and Shaka Player
lastUpdated: 2025-08-18T14:27:42.000Z
chatbotDeprioritize: false
tags: Playback
source_url:
  html: https://developers.cloudflare.com/stream/examples/shaka-player/
  md: https://developers.cloudflare.com/stream/examples/shaka-player/index.md
---

First, create a video element, using the poster attribute to set a preview thumbnail image. Refer to [Display thumbnails](https://developers.cloudflare.com/stream/viewing-videos/displaying-thumbnails/) for instructions on how to generate a thumbnail image using Cloudflare Stream.

```html
<video
  id="video"
  width="640"
  poster="https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/thumbnails/thumbnail.jpg"
  controls
  autoplay
></video>
```

Then listen for `DOMContentLoaded` event, create a new instance of Shaka Player, and load the manifest URI.

```javascript
// Replace the manifest URI with an HLS or DASH manifest from Cloudflare Stream
const manifestUri =
  'https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.mpd';


document.addEventListener('DOMContentLoaded', () => {
  const video = document.getElementById('video');
  const player = new shaka.Player(video);
  await player.load(manifestUri);
});
```

Refer to the [Shaka Player documentation](https://github.com/shaka-project/shaka-player) for more information.