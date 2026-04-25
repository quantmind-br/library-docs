---
title: Google Gemini - Factory Documentation
url: https://docs.factory.ai/cli/byok/google-gemini
source: sitemap
fetched_at: 2026-04-15T09:01:35.628921537-03:00
rendered_js: false
word_count: 56
summary: This document provides instructions on how to configure and integrate Google Gemini AI models into the Factory CLI environment.
tags:
    - gemini-api
    - model-configuration
    - ai-integration
    - factory-cli
    - api-key-setup
category: configuration
---

- [Configuration](#configuration)
- [Getting Started](#getting-started)
- [Notes](#notes)

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

[Fireworks AI](https://docs.factory.ai/cli/byok/fireworks)[Groq](https://docs.factory.ai/cli/byok/groq)