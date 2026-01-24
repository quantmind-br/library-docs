---
title: REST API · Cloudflare AI Search docs
url: https://developers.cloudflare.com/ai-search/usage/rest-api/index.md
source: llms
fetched_at: 2026-01-24T14:00:52.863730299-03:00
rendered_js: false
word_count: 635
summary: This guide provides instructions and reference information for using the AI Search REST API to perform data retrieval and generate AI-powered responses.
tags:
    - ai-search
    - rest-api
    - cloudflare-ai
    - autorag
    - vector-search
    - retrieval-augmented-generation
    - api-authentication
category: api
---

This guide will instruct you through how to use the AI Search REST API to make a query to your AI Search.

AI Search is the new name for AutoRAG

API endpoints may still reference `autorag` for the time being. Functionality remains the same, and support for the new naming will be introduced gradually.

## Prerequisite: Get AI Search API token

You need an API token with the `AI Search - Read` and `AI Search Edit` permissions to use the REST API. To create a new token:

1. In the Cloudflare dashboard, go to the **AI Search** page.

[Go to **AI Search**](https://dash.cloudflare.com/?to=/:account/ai/ai-search)

1. Select your AI Search.
2. Select **Use AI Search** and then select **API**.
3. Select **Create an API Token**.
4. Review the prefilled information then select **Create API Token**.
5. Select **Copy API Token** and save that value for future use.

## AI Search

This REST API searches for relevant results from your data source and generates a response using the model and the retrieved relevant context:

```bash
curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/autorag/rags/{AUTORAG_NAME}/ai-search \
-H 'Content-Type: application/json' \
-H "Authorization: Bearer {API_TOKEN}" \
-d '{
  "query": "How do I train a llama to deliver coffee?",
  "model": @cf/meta/llama-3.3-70b-instruct-fp8-fast,
  "rewrite_query": false,
  "max_num_results": 10,
  "ranking_options": {
    "score_threshold": 0.3,
  },
  "reranking": {
    "enabled": true,
      "model": "@cf/baai/bge-reranker-base"
  },
  "stream": true,
}'
```

Note

You can get your `ACCOUNT_ID` by navigating to [Workers & Pages on the dashboard](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/#find-account-id-workers-and-pages).

### Parameters

`query` string required

The input query.

`model` string optional

The text-generation model that is used to generate the response for the query. For a list of valid options, check the AI Search Generation model Settings. Defaults to the generation model selected in the AI Search Settings.

`system_prompt` string optional

The system prompt for generating the answer.

`rewrite_query` boolean optional

Rewrites the original query into a search optimized query to improve retrieval accuracy. Defaults to `false`.

`max_num_results` number optional

The maximum number of results that can be returned from the Vectorize database. Defaults to `10`. Must be between `1` and `50`.

`ranking_options` object optional

Configurations for customizing result ranking. Defaults to `{}`.

* `score_threshold` number optional
  * The minimum match score required for a result to be considered a match. Defaults to `0`. Must be between `0` and `1`.

`reranking` object optional

Configurations for customizing reranking. Defaults to `{}`.

* `enabled` boolean optional

  * Enables or disables reranking, which reorders retrieved results based on semantic relevance using a reranking model. Defaults to `false`.

* `model` string optional

  * The reranking model to use when reranking is enabled.

`stream` boolean optional

Returns a stream of results as they are available. Defaults to `false`.

`filters` object optional

Narrow down search results based on metadata, like folder and date, so only relevant content is retrieved. For more details, refer to [Metadata filtering](https://developers.cloudflare.com/ai-search/configuration/metadata/).

### Response

This is the response structure without `stream` enabled.

```sh
{
  "success": true,
  "result": {
    "object": "vector_store.search_results.page",
    "search_query": "How do I train a llama to deliver coffee?",
    "response": "To train a llama to deliver coffee:\n\n1. **Build trust** — Llamas appreciate patience (and decaf).\n2. **Know limits** — Max 3 cups per llama, per `llama-logistics.md`.\n3. **Use voice commands** — Start with \"Espresso Express!\"\n4.",
    "data": [
      {
        "file_id": "llama001",
        "filename": "llama/logistics/llama-logistics.md",
        "score": 0.45,
        "attributes": {
          "modified_date": 1735689600000,   // unix timestamp for 2025-01-01
          "folder": "llama/logistics/",
        },
        "content": [
          {
            "id": "llama001",
            "type": "text",
            "text": "Llamas can carry 3 drinks max."
          }
        ]
      },
      {
        "file_id": "llama042",
        "filename": "llama/llama-commands.md",
        "score": 0.4,
        "attributes": {
          "modified_date": 1735689600000,   // unix timestamp for 2025-01-01
          "folder": "llama/",
        },
        "content": [
          {
            "id": "llama042",
            "type": "text",
            "text": "Start with basic commands like 'Espresso Express!' Llamas love alliteration."
          }
        ]
      },
    ],
    "has_more": false,
    "next_page": null
  }
}
```

## Search

This REST API searches for results from your data source and returns the relevant results:

```bash
curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/autorag/rags/{AUTORAG_NAME}/search \
-H 'Content-Type: application/json' \
-H "Authorization: Bearer {API_TOKEN}" \
-d '{
  "query": "How do I train a llama to deliver coffee?",
  "rewrite_query": true,
  "max_num_results": 10,
  "ranking_options": {
    "score_threshold": 0.3,
  },
  "reranking": {
    "enabled": true,
      "model": "@cf/baai/bge-reranker-base"
  }'
```

Note

You can get your `ACCOUNT_ID` by navigating to Workers & Pages on the dashboard, and copying the Account ID under Account Details.

### Parameters

`query` string required

The input query.

`rewrite_query` boolean optional

Rewrites the original query into a search optimized query to improve retrieval accuracy. Defaults to `false`.

`max_num_results` number optional

The maximum number of results that can be returned from the Vectorize database. Defaults to `10`. Must be between `1` and `50`.

`ranking_options` object optional

Configurations for customizing result ranking. Defaults to `{}`.

* `score_threshold` number optional
  * The minimum match score required for a result to be considered a match. Defaults to `0`. Must be between `0` and `1`.

`reranking` object optional

Configurations for customizing reranking. Defaults to `{}`.

* `enabled` boolean optional

  * Enables or disables reranking, which reorders retrieved results based on semantic relevance using a reranking model. Defaults to `false`.

* `model` string optional

  * The reranking model to use when reranking is enabled.

`filters` object optional

Narrow down search results based on metadata, like folder and date, so only relevant content is retrieved. For more details, refer to [Metadata filtering](https://developers.cloudflare.com/ai-search/configuration/metadata).

### Response

```sh
{
  "success": true,
  "result": {
    "object": "vector_store.search_results.page",
    "search_query": "How do I train a llama to deliver coffee?",
    "data": [
      {
        "file_id": "llama001",
        "filename": "llama/logistics/llama-logistics.md",
        "score": 0.45,
        "attributes": {
          "modified_date": 1735689600000,   // unix timestamp for 2025-01-01
          "folder": "llama/logistics/",
        },
        "content": [
          {
            "id": "llama001",
            "type": "text",
            "text": "Llamas can carry 3 drinks max."
          }
        ]
      },
      {
        "file_id": "llama042",
        "filename": "llama/llama-commands.md",
        "score": 0.4,
        "attributes": {
          "modified_date": 1735689600000,   // unix timestamp for 2025-01-01
          "folder": "llama/",
        },
        "content": [
          {
            "id": "llama042",
            "type": "text",
            "text": "Start with basic commands like 'Espresso Express!' Llamas love alliteration."
          }
        ]
      },
    ],
    "has_more": false,
    "next_page": null
  }
}
```