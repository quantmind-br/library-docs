---
title: Google Gemini
url: https://docs.factory.ai/cli/byok/google-gemini.md
source: llms
fetched_at: 2026-02-05T21:40:56.840129844-03:00
rendered_js: false
word_count: 83
summary: This document provides instructions for configuring and connecting Google Gemini AI models to the Factory platform using custom settings and API keys.
tags:
    - google-gemini
    - api-configuration
    - ai-models
    - factory-settings
    - gemini-api
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Gemini

> Access Google's Gemini models using your Gemini AI API key

Connect to Google's Gemini models for advanced AI capabilities with multimodal support.

## Configuration

Add to `~/.factory/settings.json`:

```json  theme={null}
{
  "customModels": [
    {
      "model": "gemini-2.5-pro",
      "displayName": "Gemini 2.5 Pro [Google]",
      "baseUrl": "https://generativelanguage.googleapis.com/v1beta/",
      "apiKey": "YOUR_GEMINI_API_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 32000
    },
    {
      "model": "gemini-1.5-pro",
      "displayName": "Gemini 1.5 Pro [Google]",
      "baseUrl": "https://generativelanguage.googleapis.com/v1beta/",
      "apiKey": "YOUR_GEMINI_API_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 1048576
    },
    {
      "model": "gemini-1.5-flash",
      "displayName": "Gemini 1.5 Flash [Google]",
      "baseUrl": "https://generativelanguage.googleapis.com/v1beta/",
      "apiKey": "YOUR_GEMINI_API_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 1048576
    }
  ]
}
```

## Getting Started

1. Go to [makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy your API key
4. Add it to your Factory configuration

## Notes

* Base URL uses the `v1beta` API version
* Gemini models use the `generic-chat-completion-api` provider type