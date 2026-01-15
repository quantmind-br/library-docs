---
title: Google Gemini - Factory Documentation
url: https://docs.factory.ai/cli/byok/google-gemini
source: sitemap
fetched_at: 2026-01-13T19:03:27.357015529-03:00
rendered_js: false
word_count: 50
summary: Instructions for configuring and connecting to Google's Gemini AI models within the Factory application by adding specific model definitions to the settings file.
tags:
    - google-gemini
    - ai-models
    - factory-config
    - api-setup
    - multimodal-ai
    - settings-json
category: configuration
---

Connect to Google’s Gemini models for advanced AI capabilities with multimodal support.

## Configuration

Add to `~/.factory/settings.json`:

```
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
2. Click “Create API Key”
3. Copy your API key
4. Add it to your Factory configuration

## Notes

- Base URL uses the `v1beta` API version
- Gemini models use the `generic-chat-completion-api` provider type