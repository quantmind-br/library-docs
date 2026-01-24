---
title: Modify request property
url: https://developers.cloudflare.com/workers/examples/modify-request-property/index.md
source: llms
fetched_at: 2026-01-24T15:26:10.912694363-03:00
rendered_js: false
word_count: 67
summary: This document explains how to intercept and modify properties of an incoming HTTP request, such as the URL, method, and headers, before forwarding it to a different destination using Cloudflare Workers.
tags:
    - cloudflare-workers
    - request-handling
    - http-headers
    - javascript
    - typescript
    - python
    - middleware
category: guide
---

---
title: Modify request property · Cloudflare Workers docs
description: Create a modified request with edited properties based off of an
  incoming request.
lastUpdated: 2025-08-18T14:27:42.000Z
chatbotDeprioritize: false
tags: Middleware,Headers,JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/modify-request-property/
  md: https://developers.cloudflare.com/workers/examples/modify-request-property/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/modify-request-property)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

* JavaScript

  ```js
  export default {
    async fetch(request) {
      /**
       * Example someHost is set up to return raw JSON
       * @param {string} someUrl the URL to send the request to, since we are setting hostname too only path is applied
       * @param {string} someHost the host the request will resolve too
       */
      const someHost = "example.com";
      const someUrl = "https://foo.example.com/api.js";


      /**
       * The best practice is to only assign new RequestInit properties
       * on the request object using either a method or the constructor
       */
      const newRequestInit = {
        // Change method
        method: "POST",
        // Change body
        body: JSON.stringify({ bar: "foo" }),
        // Change the redirect mode.
        redirect: "follow",
        // Change headers, note this method will erase existing headers
        headers: {
          "Content-Type": "application/json",
        },
        // Change a Cloudflare feature on the outbound response
        cf: { apps: false },
      };


      // Change just the host
      const url = new URL(someUrl);


      url.hostname = someHost;


      // Best practice is to always use the original request to construct the new request
      // to clone all the attributes. Applying the URL also requires a constructor
      // since once a Request has been constructed, its URL is immutable.
      const newRequest = new Request(
        url.toString(),
        new Request(request, newRequestInit),
      );


      // Set headers using method
      newRequest.headers.set("X-Example", "bar");
      newRequest.headers.set("Content-Type", "application/json");
      try {
        return await fetch(newRequest);
      } catch (e) {
        return new Response(JSON.stringify({ error: e.message }), {
          status: 500,
        });
      }
    },
  };
  ```

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      /**
       * Example someHost is set up to return raw JSON
       * @param {string} someUrl the URL to send the request to, since we are setting hostname too only path is applied
       * @param {string} someHost the host the request will resolve too
       */
      const someHost = "example.com";
      const someUrl = "https://foo.example.com/api.js";


      /**
       * The best practice is to only assign new RequestInit properties
       * on the request object using either a method or the constructor
       */
      const newRequestInit = {
        // Change method
        method: "POST",
        // Change body
        body: JSON.stringify({ bar: "foo" }),
        // Change the redirect mode.
        redirect: "follow",
        // Change headers, note this method will erase existing headers
        headers: {
          "Content-Type": "application/json",
        },
        // Change a Cloudflare feature on the outbound response
        cf: { apps: false },
      };


      // Change just the host
      const url = new URL(someUrl);


      url.hostname = someHost;


      // Best practice is to always use the original request to construct the new request
      // to clone all the attributes. Applying the URL also requires a constructor
      // since once a Request has been constructed, its URL is immutable.
      const newRequest = new Request(
        url.toString(),
        new Request(request, newRequestInit),
      );


      // Set headers using method
      newRequest.headers.set("X-Example", "bar");
      newRequest.headers.set("Content-Type", "application/json");
      try {
        return await fetch(newRequest);
      } catch (e) {
        return new Response(JSON.stringify({ error: e.message }), {
          status: 500,
        });
      }
    },
  } satisfies ExportedHandler;
  ```

* Python

  ```py
  import json
  from workers import WorkerEntrypoint
  from pyodide.ffi import to_js as _to_js
  from js import Object, URL, Request, fetch, Response


  def to_js(obj):
      return _to_js(obj, dict_converter=Object.fromEntries)


  class Default(WorkerEntrypoint):
      async def fetch(self, request):
          some_host = "example.com"
          some_url = "https://foo.example.com/api.js"


          # The best practice is to only assign new_request_init properties
          # on the request object using either a method or the constructor
          new_request_init = {
            "method": "POST", # Change method
            "body": json.dumps({ "bar": "foo" }), # Change body
            "redirect": "follow", # Change the redirect mode
            # Change headers, note this method will erase existing headers
            "headers": {
              "Content-Type": "application/json",
            },
            #  Change a Cloudflare feature on the outbound response
            "cf": { "apps": False },
          }


          # Change just the host
          url = URL.new(some_url)
          url.hostname = some_host


          # Best practice is to always use the original request to construct the new request
          # to clone all the attributes. Applying the URL also requires a constructor
          # since once a Request has been constructed, its URL is immutable.
          org_request = Request.new(request, new_request_init)
          new_request = Request.new(url.toString(),org_request)


          new_request.headers["X-Example"] =  "bar"
          new_request.headers["Content-Type"] = "application/json"


          try:
              return await fetch(new_request)
          except Exception as e:
              return Response.new({"error": str(e)}, status=500)
  ```

* Hono

  ```ts
  import { Hono } from "hono";


  const app = new Hono();


  app.all("*", async (c) => {
    /**
     * Example someHost is set up to return raw JSON
     */
    const someHost = "example.com";
    const someUrl = "https://foo.example.com/api.js";


    // Create a URL object to modify the hostname
    const url = new URL(someUrl);
    url.hostname = someHost;


    // Create a new request
    // First create a clone of the original request with the new properties
    const requestClone = new Request(c.req.raw, {
      // Change method
      method: "POST",
      // Change body
      body: JSON.stringify({ bar: "foo" }),
      // Change the redirect mode
      redirect: "follow" as RequestRedirect,
      // Change headers, note this method will erase existing headers
      headers: {
        "Content-Type": "application/json",
        "X-Example": "bar",
      },
      // Change a Cloudflare feature on the outbound response
      cf: { apps: false },
    });


    // Then create a new request with the modified URL
    const newRequest = new Request(url.toString(), requestClone);


    // Send the modified request
    const response = await fetch(newRequest);


    // Return the response
    return response;
  });


  // Handle errors
  app.onError((err, c) => {
    return err.getResponse();
  });


  export default app;
  ```