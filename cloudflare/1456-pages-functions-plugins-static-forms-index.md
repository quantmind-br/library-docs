---
title: Static Forms · Cloudflare Pages docs
url: https://developers.cloudflare.com/pages/functions/plugins/static-forms/index.md
source: llms
fetched_at: 2026-01-24T15:18:56.76973906-03:00
rendered_js: false
word_count: 163
summary: This document explains how to install and configure the Static Forms Pages Plugin to intercept and handle HTML form submissions within a Cloudflare Pages application.
tags:
    - cloudflare-pages
    - static-forms
    - form-handling
    - pages-plugins
    - serverless-functions
category: guide
---

The Static Forms Pages Plugin intercepts all form submissions made which have the `data-static-form-name` attribute set. This allows you to take action on these form submissions by, for example, saving the submission to KV.

## Installation

* npm

  ```sh
  npm i @cloudflare/pages-plugin-static-forms
  ```

* yarn

  ```sh
  yarn add @cloudflare/pages-plugin-static-forms
  ```

* pnpm

  ```sh
  pnpm add @cloudflare/pages-plugin-static-forms
  ```

## Usage

```typescript
import staticFormsPlugin from "@cloudflare/pages-plugin-static-forms";


export const onRequest: PagesFunction = staticFormsPlugin({
  respondWith: ({ formData, name }) => {
    const email = formData.get("email");
    return new Response(
      `Hello, ${email}! Thank you for submitting the ${name} form.`,
    );
  },
});
```

```html
<body>
  <h1>Sales enquiry</h1>
  <form data-static-form-name="sales">
    <label>Email address <input type="email" name="email" /></label>
    <label>Message <textarea name="message"></textarea></label>
    <button type="submit">Submit</button>
  </form>
</body>
```

The Plugin takes a single argument, an object with a `respondWith` property. This function takes an object with a `formData` property (the [`FormData`](https://developer.mozilla.org/en-US/docs/Web/API/FormData) instance) and `name` property (the name value of your `data-static-form-name` attribute). It should return a `Response` or `Promise` of a `Response`. It is in this `respondWith` function that you can take action such as serializing the `formData` and saving it to a KV namespace.

The `method` and `action` attributes of the HTML form do not need to be set. The Plugin will automatically override them to allow it to intercept the submission.