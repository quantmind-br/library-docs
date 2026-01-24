---
title: 'Geolocation: Weather application'
url: https://developers.cloudflare.com/workers/examples/geolocation-app-weather/index.md
source: llms
fetched_at: 2026-01-24T15:26:02.872597498-03:00
rendered_js: false
word_count: 122
summary: This document demonstrates how to use geolocation coordinates from incoming requests to fetch and display localized weather and air quality data using Cloudflare Workers and external APIs.
tags:
    - geolocation
    - cloudflare-workers
    - request-metadata
    - weather-api
    - serverless-functions
category: tutorial
---

---
title: "Geolocation: Weather application · Cloudflare Workers docs"
description: Fetch weather data from an API using the user's geolocation data.
lastUpdated: 2025-08-18T14:27:42.000Z
chatbotDeprioritize: false
tags: Geolocation,JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/geolocation-app-weather/
  md: https://developers.cloudflare.com/workers/examples/geolocation-app-weather/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/geolocation-app-weather)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

* JavaScript

  ```js
  export default {
    async fetch(request) {
      let endpoint = "https://api.waqi.info/feed/geo:";
      const token = ""; //Use a token from https://aqicn.org/api/
      let html_style = `body{padding:6em; font-family: sans-serif;} h1{color:#f6821f}`;


      let html_content = "<h1>Weather 🌦</h1>";


      const latitude = request.cf.latitude;
      const longitude = request.cf.longitude;
      endpoint += `${latitude};${longitude}/?token=${token}`;
      const init = {
        headers: {
          "content-type": "application/json;charset=UTF-8",
        },
      };


      const response = await fetch(endpoint, init);
      const content = await response.json();


      html_content += `<p>This is a demo using Workers geolocation data. </p>`;
      html_content += `You are located at: ${latitude},${longitude}.</p>`;
      html_content += `<p>Based off sensor data from <a href="${content.data.city.url}">${content.data.city.name}</a>:</p>`;
      html_content += `<p>The AQI level is: ${content.data.aqi}.</p>`;
      html_content += `<p>The N02 level is: ${content.data.iaqi.no2?.v}.</p>`;
      html_content += `<p>The O3 level is: ${content.data.iaqi.o3?.v}.</p>`;
      html_content += `<p>The temperature is: ${content.data.iaqi.t?.v}°C.</p>`;


      let html = `
        <!DOCTYPE html>
        <head>
          <title>Geolocation: Weather</title>
        </head>
        <body>
          <style>${html_style}</style>
          <div id="container">
          ${html_content}
          </div>
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
      let endpoint = "https://api.waqi.info/feed/geo:";
      const token = ""; //Use a token from https://aqicn.org/api/
      let html_style = `body{padding:6em; font-family: sans-serif;} h1{color:#f6821f}`;


      let html_content = "<h1>Weather 🌦</h1>";


      const latitude = request.cf.latitude;
      const longitude = request.cf.longitude;
      endpoint += `${latitude};${longitude}/?token=${token}`;
      const init = {
        headers: {
          "content-type": "application/json;charset=UTF-8",
        },
      };


      const response = await fetch(endpoint, init);
      const content = await response.json();


      html_content += `<p>This is a demo using Workers geolocation data. </p>`;
      html_content += `You are located at: ${latitude},${longitude}.</p>`;
      html_content += `<p>Based off sensor data from <a href="${content.data.city.url}">${content.data.city.name}</a>:</p>`;
      html_content += `<p>The AQI level is: ${content.data.aqi}.</p>`;
      html_content += `<p>The N02 level is: ${content.data.iaqi.no2?.v}.</p>`;
      html_content += `<p>The O3 level is: ${content.data.iaqi.o3?.v}.</p>`;
      html_content += `<p>The temperature is: ${content.data.iaqi.t?.v}°C.</p>`;


      let html = `
        <!DOCTYPE html>
        <head>
          <title>Geolocation: Weather</title>
        </head>
        <body>
          <style>${html_style}</style>
          <div id="container">
          ${html_content}
          </div>
        </body>`;


      return new Response(html, {
        headers: {
          "content-type": "text/html;charset=UTF-8",
        },
      });
    },
  } satisfies ExportedHandler;
  ```

* Hono

  ```ts
  import { Hono } from 'hono';
  import { html } from 'hono/html';


  type Bindings = {};


  interface WeatherApiResponse {
    data: {
      aqi: number;
      city: {
        name: string;
        url: string;
      };
      iaqi: {
        no2?: { v: number };
        o3?: { v: number };
        t?: { v: number };
      };
    };
  }


  const app = new Hono<{ Bindings: Bindings }>();


  app.get('*', async (c) => {
    // Get API endpoint
    let endpoint = "https://api.waqi.info/feed/geo:";
    const token = ""; // Use a token from https://aqicn.org/api/


    // Define styles
    const html_style = `body{padding:6em; font-family: sans-serif;} h1{color:#f6821f}`;


    // Get geolocation from Cloudflare request
    const req = c.req.raw;
    const latitude = req.cf?.latitude;
    const longitude = req.cf?.longitude;


    // Create complete API endpoint with coordinates
    endpoint += `${latitude};${longitude}/?token=${token}`;


    // Fetch weather data
    const init = {
      headers: {
        "content-type": "application/json;charset=UTF-8",
      },
    };
    const response = await fetch(endpoint, init);
    const content = await response.json() as WeatherApiResponse;


    // Build HTML content
    const weatherContent = html`
      <h1>Weather 🌦</h1>
      <p>This is a demo using Workers geolocation data.</p>
      <p>You are located at: ${latitude},${longitude}.</p>
      <p>Based off sensor data from <a href="${content.data.city.url}">${content.data.city.name}</a>:</p>
      <p>The AQI level is: ${content.data.aqi}.</p>
      <p>The N02 level is: ${content.data.iaqi.no2?.v}.</p>
      <p>The O3 level is: ${content.data.iaqi.o3?.v}.</p>
      <p>The temperature is: ${content.data.iaqi.t?.v}°C.</p>
    `;


    // Complete HTML document
    const htmlDocument = html`
      <!DOCTYPE html>
      <head>
        <title>Geolocation: Weather</title>
      </head>
      <body>
        <style>${html_style}</style>
        <div id="container">
          ${weatherContent}
        </div>
      </body>
    `;


    // Return HTML response
    return c.html(htmlDocument);
  });


  export default app;
  ```

* Python

  ```py
  from workers import WorkerEntrypoint, Response, fetch


  class Default(WorkerEntrypoint):
      async def fetch(self, request):
          endpoint = "https://api.waqi.info/feed/geo:"
          token = "" # Use a token from https://aqicn.org/api/
          html_style = "body{padding:6em; font-family: sans-serif;} h1{color:#f6821f}"
          html_content = "<h1>Weather 🌦</h1>"


          latitude = request.cf.latitude
          longitude = request.cf.longitude


          endpoint += f"{latitude};{longitude}/?token={token}"
          response = await fetch(endpoint)
          content = await response.json()


          html_content += "<p>This is a demo using Workers geolocation data. </p>"
          html_content += f"You are located at: {latitude},{longitude}.</p>"
          html_content += f"<p>Based off sensor data from <a href='{content['data']['city']['url']}'>{content['data']['city']['name']}</a>:</p>"
          html_content += f"<p>The AQI level is: {content['data']['aqi']}.</p>"
          html_content += f"<p>The N02 level is: {content['data']['iaqi']['no2']['v']}.</p>"
          html_content += f"<p>The O3 level is: {content['data']['iaqi']['o3']['v']}.</p>"
          html_content += f"<p>The temperature is: {content['data']['iaqi']['t']['v']}°C.</p>"


          html = f"""
          <!DOCTYPE html>
            <head>
              <title>Geolocation: Weather</title>
            </head>
            <body>
              <style>{html_style}</style>
              <div id="container">
              {html_content}
              </div>
            </body>
          """


          headers = {"content-type": "text/html;charset=UTF-8"}
          return Response(html, headers=headers)
  ```