---
title: /scrape - Scrape HTML elements · Cloudflare Browser Rendering docs
url: https://developers.cloudflare.com/browser-rendering/rest-api/scrape-endpoint/index.md
source: llms
fetched_at: 2026-01-24T14:04:39.992094703-03:00
rendered_js: false
word_count: 359
summary: This document explains how to use the /scrape endpoint to programmatically extract structured content, dimensions, and metadata from web pages using CSS selectors.
tags:
    - cloudflare-api
    - browser-rendering
    - web-scraping
    - css-selectors
    - data-extraction
category: api
---

The `/scrape` endpoint extracts structured data from specific elements on a webpage, returning details such as element dimensions and inner HTML.

## Endpoint

```txt
https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/scrape
```

## Required fields

You must provide either `url` or `elements`:

* `url` (string)
* `elements` (array of objects) — each object must include `selector` (string)

## Common use cases

* Extract headings, links, prices, or other repeated content with CSS selectors
* Collect metadata (for example, titles, descriptions, canonical links)

## Basic usage

### Extract headings and links from a URL

* curl

  Go to `https://example.com` and extract metadata from all `h1` and `a` elements in the DOM.

  ```bash
  curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/scrape' \
    -H 'Authorization: Bearer <apiToken>' \
    -H 'Content-Type: application/json' \
    -d '{
    "url": "https://example.com/",
    "elements": [{
      "selector": "h1"
    },
    {
      "selector": "a"
    }]
  }'
  ```

  ```json
  {
    "success": true,
    "result": [
      {
        "results": [
          {
            "attributes": [],
            "height": 39,
            "html": "Example Domain",
            "left": 100,
            "text": "Example Domain",
            "top": 133.4375,
            "width": 600
          }
        ],
        "selector": "h1"
      },
      {
        "results": [
          {
            "attributes": [
              { "name": "href", "value": "https://www.iana.org/domains/example" }
            ],
            "height": 20,
            "html": "More information...",
            "left": 100,
            "text": "More information...",
            "top": 249.875,
            "width": 142
          }
        ],
        "selector": "a"
      }
    ]
  }
  ```

* TypeScript SDK

  ```typescript
  import Cloudflare from "cloudflare";


  const client = new Cloudflare({
    apiToken: process.env["CLOUDFLARE_API_TOKEN"],
  });


  const scrapes = await client.browserRendering.scrape.create({
    account_id: process.env["CLOUDFLARE_ACCOUNT_ID"],
    elements: [
          { selector: "h1" },
          { selector: "a" }
      ]
  });


  console.log(scrapes);
  ```

Many more options exist, like setting HTTP credentials using `authenticate`, setting `cookies`, and using `gotoOptions` to control page load behaviour - check the endpoint [reference](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/scrape/methods/create/) for all available parameters.

### Response fields

* `results` *(array of objects)* - Contains extracted data for each selector.

  * `selector` *(string)* - The CSS selector used.

  * `results` *(array of objects)* - List of extracted elements matching the selector.

    * `text` *(string)* - Inner text of the element.
    * `html` *(string)* - Inner HTML of the element.
    * `attributes` *(array of objects)* - List of extracted attributes such as `href` for links.
    * `height`, `width`, `top`, `left` *(number)* - Position and dimensions of the element.

## Advanced Usage

Looking for more parameters?

Visit the [Browser Rendering API reference](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/scrape/methods/create/) for all available parameters, such as setting HTTP credentials using `authenticate`, setting `cookies`, and customizing load behavior using `gotoOptions`.

### Handling JavaScript-heavy pages

For JavaScript-heavy pages or Single Page Applications (SPAs), the default page load behavior may return empty or incomplete results. This happens because the browser considers the page loaded before JavaScript has finished rendering the content.

The simplest solution is to use the `gotoOptions.waitUntil` parameter set to `networkidle0` or `networkidle2`:

```json
{
  "url": "https://example.com",
  "gotoOptions": {
    "waitUntil": "networkidle0"
  }
}
```

For faster responses, advanced users can use `waitForSelector` to wait for a specific element instead of waiting for all network activity to stop. This requires knowing which CSS selector indicates the content you need has loaded. For more details, refer to [REST API timeouts](https://developers.cloudflare.com/browser-rendering/reference/timeouts/).

### Set a custom user agent

You can change the user agent at the page level by passing `userAgent` as a top-level parameter in the JSON body. This is useful if the target website serves different content based on the user agent.

Note

The `userAgent` parameter does not bypass bot protection. Requests from Browser Rendering will always be identified as a bot.

## Troubleshooting

If you have questions or encounter an error, see the [Browser Rendering FAQ and troubleshooting guide](https://developers.cloudflare.com/browser-rendering/faq/).