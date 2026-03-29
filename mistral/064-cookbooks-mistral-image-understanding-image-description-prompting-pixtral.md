---
title: Image Description Extraction using Mistral's Pixtral API - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-image_understanding-image_description_prompting_pixtral
source: crawler
fetched_at: 2026-01-29T07:33:53.611085097-03:00
rendered_js: false
word_count: 180
---

In this notebook, we'll use the `Mistral` API to extract structured image descriptions in JSON format using the `Pixtral-12b-2409` model. We'll send an image URL and prompt the model to return key elements with descriptions.

## Prerequisites

Make sure you have an API key for the Mistral AI platform. We'll also show you how to load it from environment variables.

## Setup

We'll load the Mistral API key from environment variables and initialize the client. Make sure your API key is saved in your environment variables as `MISTRAL_API_KEY`.

## Sending Image URL for Description

We'll prompt the model to describe the image by providing an image URL. The response will be returned in a structured JSON format with the key elements described.

## Parsing the JSON Response

We'll now parse the JSON response from the API and print the elements and their corresponding descriptions.

## Conclusion

In this notebook, we used the Mistral Pixtral model to describe an image by sending an image URL and receiving a structured JSON response. The descriptions provided by the model offer insights into the key elements of the image.