---
title: Serve private images · Cloudflare Images docs
url: https://developers.cloudflare.com/images/manage-images/serve-images/serve-private-images/index.md
source: llms
fetched_at: 2026-01-24T15:16:00.336575833-03:00
rendered_js: false
word_count: 180
summary: This document explains how to secure and serve private images using signed URL tokens and Cloudflare Workers. It details the process of obtaining security keys and programmatically generating expiring URLs to control image access.
tags:
    - cloudflare-images
    - signed-urls
    - security
    - cloudflare-workers
    - image-delivery
    - authentication
category: guide
---

You can serve private images by using signed URL tokens. When an image requires a signed URL, the image cannot be accessed without a token unless it is being requested for a variant set to always allow public access.

1. In the Cloudflare dashboard, go to the **Hosted Images** page.

   [Go to **Hosted images**](https://dash.cloudflare.com/?to=/:account/images/hosted)

2. Select **Keys**.

3. Copy your key and use it to generate an expiring tokenized URL.

Note

Private images do not currently support custom paths.

The example below uses a Worker that takes in a regular URL without a signed token and returns a tokenized URL that expires after one day. You can, however, set this expiration period to whatever you need, by changing the const `EXPIRATION` value.

* JavaScript

  ```js
  const KEY = "YOUR_KEY_FROM_IMAGES_DASHBOARD";
  const EXPIRATION = 60 * 60 * 24; // 1 day


  const bufferToHex = (buffer) =>
    [...new Uint8Array(buffer)]
      .map((x) => x.toString(16).padStart(2, "0"))
      .join("");


  async function generateSignedUrl(url) {
    // `url` is a full imagedelivery.net URL
    // e.g. https://imagedelivery.net/cheeW4oKsx5ljh8e8BoL2A/bc27a117-9509-446b-8c69-c81bfeac0a01/mobile


    const encoder = new TextEncoder();
    const secretKeyData = encoder.encode(KEY);
    const key = await crypto.subtle.importKey(
      "raw",
      secretKeyData,
      { name: "HMAC", hash: "SHA-256" },
      false,
      ["sign"],
    );


    // Attach the expiration value to the `url`
    const expiry = Math.floor(Date.now() / 1000) + EXPIRATION;
    url.searchParams.set("exp", expiry);
    // `url` now looks like
    // https://imagedelivery.net/cheeW4oKsx5ljh8e8BoL2A/bc27a117-9509-446b-8c69-c81bfeac0a01/mobile?exp=1631289275


    const stringToSign = url.pathname + "?" + url.searchParams.toString();
    // for example, /cheeW4oKsx5ljh8e8BoL2A/bc27a117-9509-446b-8c69-c81bfeac0a01/mobile?exp=1631289275


    // Generate the signature
    const mac = await crypto.subtle.sign(
      "HMAC",
      key,
      encoder.encode(stringToSign),
    );
    const sig = bufferToHex(new Uint8Array(mac).buffer);


    // And attach it to the `url`
    url.searchParams.set("sig", sig);


    return new Response(url);
  }


  export default {
    async fetch(request, env, ctx) {
      const url = new URL(event.request.url);
      const imageDeliveryURL = new URL(
        url.pathname
          .slice(1)
          .replace("https:/imagedelivery.net", "https://imagedelivery.net"),
      );
      return generateSignedUrl(imageDeliveryURL);
    },
  };
  ```

* TypeScript

  ```ts
  const KEY = "YOUR_KEY_FROM_IMAGES_DASHBOARD";
  const EXPIRATION = 60 * 60 * 24; // 1 day


  const bufferToHex = (buffer) =>
    [...new Uint8Array(buffer)]
      .map((x) => x.toString(16).padStart(2, "0"))
      .join("");


  async function generateSignedUrl(url) {
    // `url` is a full imagedelivery.net URL
    // e.g. https://imagedelivery.net/cheeW4oKsx5ljh8e8BoL2A/bc27a117-9509-446b-8c69-c81bfeac0a01/mobile


    const encoder = new TextEncoder();
    const secretKeyData = encoder.encode(KEY);
    const key = await crypto.subtle.importKey(
      "raw",
      secretKeyData,
      { name: "HMAC", hash: "SHA-256" },
      false,
      ["sign"],
    );


    // Attach the expiration value to the `url`
    const expiry = Math.floor(Date.now() / 1000) + EXPIRATION;
    url.searchParams.set("exp", expiry);
    // `url` now looks like
    // https://imagedelivery.net/cheeW4oKsx5ljh8e8BoL2A/bc27a117-9509-446b-8c69-c81bfeac0a01/mobile?exp=1631289275


    const stringToSign = url.pathname + "?" + url.searchParams.toString();
    // for example, /cheeW4oKsx5ljh8e8BoL2A/bc27a117-9509-446b-8c69-c81bfeac0a01/mobile?exp=1631289275


    // Generate the signature
    const mac = await crypto.subtle.sign(
      "HMAC",
      key,
      encoder.encode(stringToSign),
    );
    const sig = bufferToHex(new Uint8Array(mac).buffer);


    // And attach it to the `url`
    url.searchParams.set("sig", sig);


    return new Response(url);
  }


  export default {
    async fetch(request, env, ctx): Promise<Response> {
      const url = new URL(event.request.url);
      const imageDeliveryURL = new URL(
        url.pathname
          .slice(1)
          .replace("https:/imagedelivery.net", "https://imagedelivery.net"),
      );
      return generateSignedUrl(imageDeliveryURL);
    },
  } satisfies ExportedHandler<Env>;
  ```