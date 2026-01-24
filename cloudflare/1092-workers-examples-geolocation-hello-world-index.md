---
title: 'Geolocation: Hello World'
url: https://developers.cloudflare.com/workers/examples/geolocation-hello-world/index.md
source: llms
fetched_at: 2026-01-24T15:26:03.211527198-03:00
rendered_js: false
word_count: 123
summary: This document demonstrates how to access and display visitor geolocation data, such as country, city, and coordinates, using the Cloudflare-specific properties on the request object.
tags:
    - cloudflare-workers
    - geolocation
    - javascript
    - typescript
    - python
    - request-cf
    - hono
category: tutorial
---

---
title: "Geolocation: Hello World · Cloudflare Workers docs"
description: Get all geolocation data fields and display them in HTML.
lastUpdated: 2025-08-18T14:27:42.000Z
chatbotDeprioritize: false
tags: Geolocation,JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/geolocation-hello-world/
  md: https://developers.cloudflare.com/workers/examples/geolocation-hello-world/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/geolocation-hello-world)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

* JavaScript

  ```js
  export default {
    async fetch(request) {
      let html_content = "";
      let html_style =
        "body{padding:6em; font-family: sans-serif;} h1{color:#f6821f;}";


      html_content += "<p> Colo: " + request.cf.colo + "</p>";
      html_content += "<p> Country: " + request.cf.country + "</p>";
      html_content += "<p> City: " + request.cf.city + "</p>";
      html_content += "<p> Continent: " + request.cf.continent + "</p>";
      html_content += "<p> Latitude: " + request.cf.latitude + "</p>";
      html_content += "<p> Longitude: " + request.cf.longitude + "</p>";
      html_content += "<p> PostalCode: " + request.cf.postalCode + "</p>";
      html_content += "<p> MetroCode: " + request.cf.metroCode + "</p>";
      html_content += "<p> Region: " + request.cf.region + "</p>";
      html_content += "<p> RegionCode: " + request.cf.regionCode + "</p>";
      html_content += "<p> Timezone: " + request.cf.timezone + "</p>";


      let html = `<!DOCTYPE html>
        <head>
          <title> Geolocation: Hello World </title>
          <style> ${html_style} </style>
        </head>
        <body>
          <h1>Geolocation: Hello World!</h1>
          <p>You now have access to geolocation data about where your user is visiting from.</p>
          ${html_content}
        </body>`;


      return new Response(html, {
        headers: {
          "content-type": "text/html;charset=UTF-8",
        },
      });
    },
  };
  ```

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      let html_content = "";
      let html_style =
        "body{padding:6em; font-family: sans-serif;} h1{color:#f6821f;}";


      html_content += "<p> Colo: " + request.cf.colo + "</p>";
      html_content += "<p> Country: " + request.cf.country + "</p>";
      html_content += "<p> City: " + request.cf.city + "</p>";
      html_content += "<p> Continent: " + request.cf.continent + "</p>";
      html_content += "<p> Latitude: " + request.cf.latitude + "</p>";
      html_content += "<p> Longitude: " + request.cf.longitude + "</p>";
      html_content += "<p> PostalCode: " + request.cf.postalCode + "</p>";
      html_content += "<p> MetroCode: " + request.cf.metroCode + "</p>";
      html_content += "<p> Region: " + request.cf.region + "</p>";
      html_content += "<p> RegionCode: " + request.cf.regionCode + "</p>";
      html_content += "<p> Timezone: " + request.cf.timezone + "</p>";


      let html = `<!DOCTYPE html>
        <head>
          <title> Geolocation: Hello World </title>
          <style> ${html_style} </style>
        </head>
        <body>
          <h1>Geolocation: Hello World!</h1>
          <p>You now have access to geolocation data about where your user is visiting from.</p>
          ${html_content}
        </body>`;


      return new Response(html, {
        headers: {
          "content-type": "text/html;charset=UTF-8",
        },
      });
    },
  } satisfies ExportedHandler;
  ```

* Python

  ```py
  from workers import WorkerEntrypoint, Response


  class Default(WorkerEntrypoint):
      async def fetch(self, request):
          html_content = ""
          html_style = "body{padding:6em font-family: sans-serif;} h1{color:#f6821f;}"


          html_content += "<p> Colo: " + request.cf.colo + "</p>"
          html_content += "<p> Country: " + request.cf.country + "</p>"
          html_content += "<p> City: " + request.cf.city + "</p>"
          html_content += "<p> Continent: " + request.cf.continent + "</p>"
          html_content += "<p> Latitude: " + request.cf.latitude + "</p>"
          html_content += "<p> Longitude: " + request.cf.longitude + "</p>"
          html_content += "<p> PostalCode: " + request.cf.postalCode + "</p>"
          html_content += "<p> Region: " + request.cf.region + "</p>"
          html_content += "<p> RegionCode: " + request.cf.regionCode + "</p>"
          html_content += "<p> Timezone: " + request.cf.timezone + "</p>"


          html = f"""
          <!DOCTYPE html>
            <head>
              <title> Geolocation: Hello World </title>
              <style> {html_style} </style>
            </head>
            <body>
              <h1>Geolocation: Hello World!</h1>
              <p>You now have access to geolocation data about where your user is visiting from.</p>
              {html_content}
            </body>
          """


          headers = {"content-type": "text/html;charset=UTF-8"}
          return Response(html, headers=headers)
  ```

* Hono

  ```ts
  import { Hono } from "hono";
  import { html } from "hono/html";


  // Define the RequestWithCf interface to add Cloudflare-specific properties
  interface RequestWithCf extends Request {
    cf: {
      // Cloudflare-specific properties for geolocation
      colo: string;
      country: string;
      city: string;
      continent: string;
      latitude: string;
      longitude: string;
      postalCode: string;
      metroCode: string;
      region: string;
      regionCode: string;
      timezone: string;
      // Add other CF properties as needed
    };
  }


  const app = new Hono();


  app.get("*", (c) => {
    // Cast the raw request to include Cloudflare-specific properties
    const request = c.req.raw;


    // Define styles
    const html_style =
      "body{padding:6em; font-family: sans-serif;} h1{color:#f6821f;}";


    // Create content with geolocation data
    let html_content = html` <p>Colo: ${request.cf.colo}</p>
      <p>Country: ${request.cf.country}</p>
      <p>City: ${request.cf.city}</p>
      <p>Continent: ${request.cf.continent}</p>
      <p>Latitude: ${request.cf.latitude}</p>
      <p>Longitude: ${request.cf.longitude}</p>
      <p>PostalCode: ${request.cf.postalCode}</p>
      <p>MetroCode: ${request.cf.metroCode}</p>
      <p>Region: ${request.cf.region}</p>
      <p>RegionCode: ${request.cf.regionCode}</p>
      <p>Timezone: ${request.cf.timezone}</p>`;


    // Compose the full HTML
    const htmlContent = html`<!DOCTYPE html>
      <head>
        <title>Geolocation: Hello World</title>
        <style>
          ${html_style}
        </style>
      </head>
      <body>
        <h1>Geolocation: Hello World!</h1>
        <p>
          You now have access to geolocation data about where your user is
          visiting from.
        </p>
        ${html_content}
      </body> `;


    // Return the HTML response
    return c.html(htmlContent);
  });


  export default app;
  ```