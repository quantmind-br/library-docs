---
title: Transform user-uploaded images before uploading to R2 · Cloudflare Images docs
url: https://developers.cloudflare.com/images/tutorials/optimize-user-uploaded-image/index.md
source: llms
fetched_at: 2026-01-24T15:15:49.801240601-03:00
rendered_js: false
word_count: 930
summary: This guide explains how to use Cloudflare Workers to handle image uploads, apply visual watermarks via the Images API, and store processed images in R2 storage.
tags:
    - cloudflare-workers
    - cloudflare-images
    - r2-storage
    - image-transformation
    - watermarking
    - file-upload
category: guide
---

In this guide, you will build an app that accepts image uploads, overlays the image with a visual watermark, then stores the transformed image in your R2 bucket.

***

With Images, you have the flexibility to choose where your original images are stored. You can transform images that are stored outside of the Images product, like in [R2](https://developers.cloudflare.com/r2/).

When you store user-uploaded media in R2, you may want to optimize or manipulate images before they are uploaded to your R2 bucket.

You will learn how to connect Developer Platform services to your Worker through bindings, as well as use various optimization features in the Images API.

## Prerequisites

Before you begin, you will need to do the following:

* Add an [Images Paid](https://developers.cloudflare.com/images/pricing/#images-paid) subscription to your account. This allows you to bind the Images API to your Worker.
* Create an [R2 bucket](https://developers.cloudflare.com/r2/get-started/#2-create-a-bucket), where the transformed images will be uploaded.
* Create a new Worker project.

If you are new, review how to [create your first Worker](https://developers.cloudflare.com/workers/get-started/guide/).

## 1: Set up your Worker project

To start, you will need to set up your project to use the following resources on the Developer Platform:

* [Images](https://developers.cloudflare.com/images/transform-images/bindings/) to transform, resize, and encode images directly from your Worker.
* [R2](https://developers.cloudflare.com/r2/api/workers/workers-api-usage/) to connect the bucket for storing transformed images.
* [Assets](https://developers.cloudflare.com/workers/static-assets/binding/) to access a static image that will be used as the visual watermark.

### Add the bindings to your Wrangler configuration

Configure your `wrangler.toml` file to add the Images, R2, and Assets bindings:

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "images": {
      "binding": "IMAGES"
    },
    "r2_buckets": [
      {
        "binding": "R2",
        "bucket_name": "<BUCKET>"
      }
    ],
    "assets": {
      "directory": "./<DIRECTORY>",
      "binding": "ASSETS"
    }
  }
  ```

* wrangler.toml

  ```toml
  [images]
  binding = "IMAGES"


  [[r2_buckets]]
  binding = "R2"
  bucket_name = "<BUCKET>"


  [assets]
  directory = "./<DIRECTORY>"
  binding = "ASSETS"
  ```

Replace `<BUCKET>` with the name of the R2 bucket where you will upload the images after they are transformed. In your Worker code, you will be able to refer to this bucket using `env.R2.`

Replace `./<DIRECTORY>` with the name of the project's directory where the overlay image will be stored. In your Worker code, you will be able to refer to these assets using `env.ASSETS`.

### Set up your assets directory

Because we want to apply a visual watermark to every uploaded image, you need a place to store the overlay image.

The assets directory of your project lets you upload static assets as part of your Worker. When you deploy your project, these uploaded files, along with your Worker code, are deployed to Cloudflare's infrastructure in a single operation.

After you configure your Wrangler file, upload the overlay image to the specified directory. In our example app, the directory `./assets` contains the overlay image.

## 2: Build your frontend

You will need to build the interface for the app that lets users upload images.

In this example, the frontend is rendered directly from the Worker script.

To do this, make a new `html` variable, which contains a `form` element for accepting uploads. In `fetch`, construct a new `Response` with a `Content-Type: text/html` header to serve your static HTML site to the client:

```js
const html = `
<!DOCTYPE html>
        <html>
          <head>
            <meta charset="UTF-8">
            <title>Upload Image</title>
          </head>
          <body>
            <h1>Upload an image</h1>
            <form method="POST" enctype="multipart/form-data">
              <input type="file" name="image" accept="image/*" required />
              <button type="submit">Upload</button>
            </form>
          </body>
        </html>
`;


export default {
  async fetch(request, env) {
    if (request.method === "GET") {
      return new Response(html, {headers:{'Content-Type':'text/html'},})
    }
    if (request.method ==="POST") {
      // This is called when the user submits the form
    }
  }
};
```

## 3: Read the uploaded image

After you have a `form`, you need to make sure you can transform the uploaded images.

Because the `form` lets users upload directly from their disk, you cannot use `fetch()` to get an image from a URL. Instead, you will operate on the body of the image as a stream of bytes.

To do this, parse the data from the `form` as an array buffer:

```js
export default {
  async fetch(request, env) {
    if (request.method === "GET") {
      return new Response(html, {headers:{'Content-Type':'text/html'},})
    }
    if (request.method === "POST") {
      try {
        // Parse form data
        const formData = await request.formData();
        const file = formData.get("image");
        if (!file || typeof file.arrayBuffer !== "function") {
          return new Response("No image file provided", { status: 400 });
        }


        // Read uploaded image as array buffer
        const fileBuffer = await file.arrayBuffer();
      } catch (err) {
        console.log(err.message)
      }
    }
  }
};
```

Prevent potential errors when accessing request.body

The body of a [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) can only be accessed once. If you previously used `request.formData()` in the same request, you may encounter a TypeError when attempting to access `request.body`.

To avoid errors, create a clone of the Request object with `request.clone()` for each subsequent attempt to access a Request's body. Keep in mind that Workers have a [memory limit of 128 MB per Worker](https://developers.cloudflare.com/workers/platform/limits#worker-limits) and loading particularly large files into a Worker's memory multiple times may reach this limit. To ensure memory usage does not reach this limit, consider using [Streams](https://developers.cloudflare.com/workers/runtime-apis/streams/).

## 4: Transform the image

For every uploaded image, you want to perform the following actions:

* Overlay the visual watermark that we added to our assets directory.
* Transcode the image — with its watermark — to `AVIF`. This compresses the image and reduces its file size.
* Upload the transformed image to R2.

### Set up the overlay image

To fetch the overlay image from the assets directory, create a function `assetUrl` then use `env.ASSETS` to retrieve the `watermark.png` image:

```js
var __defProp = Object.defineProperty;
var __name = (target, value) => __defProp(target, "name", { value, configurable: true });


function assetUrl(request, path) {
  const url = new URL(request.url);
  url.pathname = path;
  return url;
}
__name(assetUrl, "assetUrl");


export default {
  async fetch(request, env) {
    if (request.method === "GET") {
      return new Response(html, {headers:{'Content-Type':'text/html'},})
    }
    if (request.method === "POST") {
      try {
        // Parse form data
        const formData = await request.formData();
        const file = formData.get("image");
        if (!file || typeof file.arrayBuffer !== "function") {
          return new Response("No image file provided", { status: 400 });
        }


        // Read uploaded image as array buffer
        const fileBuffer = await file.arrayBuffer();


        // Fetch image as watermark
        let watermarkStream = (await env.ASSETS.fetch(assetUrl(request, "watermark.png"))).body;
      } catch (err) {
        console.log(err.message)
      }
    }
  }
};
```

### Watermark and transcode the image

You can interact with the Images binding through `env.IMAGES`.

This is where you will put all of the optimization operations you want to perform on the image. Here, you will use the `.draw()` function to apply a visual watermark over the uploaded image, then use `.output()` to encode the image as AVIF:

```js
var __defProp = Object.defineProperty;
var __name = (target, value) => __defProp(target, "name", { value, configurable: true });


function assetUrl(request, path) {
  const url = new URL(request.url);
  url.pathname = path;
  return url;
}
__name(assetUrl, "assetUrl");


export default {
  async fetch(request, env) {
    if (request.method === "GET") {
      return new Response(html, {headers:{'Content-Type':'text/html'},})
    }
    if (request.method === "POST") {
      try {
        // Parse form data
        const formData = await request.formData();
        const file = formData.get("image");
        if (!file || typeof file.arrayBuffer !== "function") {
          return new Response("No image file provided", { status: 400 });
        }


        // Read uploaded image as array buffer
        const fileBuffer = await file.arrayBuffer();


        // Fetch image as watermark
        let watermarkStream = (await env.ASSETS.fetch(assetUrl(request, "watermark.png"))).body;


        // Apply watermark and convert to AVIF
        const imageResponse = (
          await env.IMAGES.input(fileBuffer)
              // Draw the watermark on top of the image
              .draw(
                env.IMAGES.input(watermarkStream)
                  .transform({ width: 100, height: 100 }),
                { bottom: 10, right: 10, opacity: 0.75 }
              )
              // Output the final image as AVIF
              .output({ format: "image/avif" })
          ).response();
      } catch (err) {
        console.log(err.message)
      }
    }
  }
};
```

## 5: Upload to R2

Upload the transformed image to R2.

By creating a `fileName` variable, you can specify the name of the transformed image. In this example, you append the date to the name of the original image before uploading to R2.

Here is the full code for the example:

```js
var __defProp = Object.defineProperty;
var __name = (target, value) => __defProp(target, "name", { value, configurable: true });


function assetUrl(request, path) {
  const url = new URL(request.url);
  url.pathname = path;
  return url;
}
__name(assetUrl, "assetUrl");


export default {
  async fetch(request, env) {
    if (request.method === "GET") {
      return new Response(html, {headers:{'Content-Type':'text/html'},})
    }
    if (request.method === "POST") {
      try {
        // Parse form data
        const formData = await request.formData();
        const file = formData.get("image");
        if (!file || typeof file.arrayBuffer !== "function") {
          return new Response("No image file provided", { status: 400 });
        }


        // Read uploaded image as array buffer
        const fileBuffer = await file.arrayBuffer();


        // Fetch image as watermark
        let watermarkStream = (await env.ASSETS.fetch(assetUrl(request, "watermark.png"))).body;


        // Apply watermark and convert to AVIF
        const imageResponse = (
          await env.IMAGES.input(fileBuffer)
              // Draw the watermark on top of the image
              .draw(
                env.IMAGES.input(watermarkStream)
                  .transform({ width: 100, height: 100 }),
                { bottom: 10, right: 10, opacity: 0.75 }
              )
              // Output the final image as AVIF
              .output({ format: "image/avif" })
          ).response();


          // Add timestamp to file name
          const fileName = `image-${Date.now()}.avif`;


          // Upload to R2
          await env.R2.put(fileName, imageResponse.body)


          return new Response(`Image uploaded successfully as ${fileName}`, { status: 200 });
      } catch (err) {
        console.log(err.message)
      }
    }
  }
};
```

## Next steps

In this tutorial, you learned how to connect your Worker to various resources on the Developer Platform to build an app that accepts image uploads, transform images, and uploads the output to R2.

Next, you can [set up a transformation URL](https://developers.cloudflare.com/images/transform-images/transform-via-url/) to dynamically optimize images that are stored in R2.