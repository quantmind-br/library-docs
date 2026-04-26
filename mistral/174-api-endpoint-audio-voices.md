---
title: Audio Voices
url: https://docs.mistral.ai/api/endpoint/audio/voices
source: sitemap
fetched_at: 2026-04-26T04:01:20.999687076-03:00
rendered_js: false
word_count: 164
summary: API reference for managing custom voice profiles, including endpoints for listing, creating, retrieving, updating, and deleting audio voices.
tags:
    - audio-api
    - voice-management
    - rest-api
    - media-processing
    - api-reference
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Audio Voices

API for managing custom voice profiles.

---

## List Voices

`GET /v1/audio/voices`

List all voices (excluding sample data).

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `page_size` | integer | - | Maximum voices to return |

### Code Example

```bash
curl https://api.mistral.ai/v1/audio/voices \
  -X GET \
  -H 'Authorization: Bearer YOUR_APIKEY_HERE'
```

### Response

```json
{
  "items": [{"created_at": "2025-10-07T20:56:01.974Z", "id": "ipsum eiusmod", "name": "consequat do", "user_id": null}],
  "page": 87,
  "page_size": 14,
  "total": 56,
  "total_pages": 91
}
```

---

## Create Voice

`POST /v1/audio/voices`

Create a new voice with base64-encoded audio sample.

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `name` | string | - | Voice name |
| `sample_audio` | string (base64) | - | Base64-encoded audio file |
| `sample_filename` | string\|null | - | Original filename for extension detection |
| `retention_notice` | integer | `30` | Retention period |

### Code Example

```bash
curl https://api.mistral.ai/v1/audio/voices \
  -X POST \
  -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
  -H 'Content-Type: application/json' \
  -d '{"name": "ipsum eiusmod", "sample_audio": "consequat do"}'
```

---

## Get Voice

`GET /v1/audio/voices/{voice_id}`

Get voice details (excluding sample).

---

## Delete Voice

`DELETE /v1/audio/voices/{voice_id}`

Delete a custom voice.

---

## Update Voice

`PATCH /v1/audio/voices/{voice_id}`

Update voice metadata (name, gender, languages, age, tags).

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `languages` | array\<string\>\|null | - | Supported languages |

---

## Get Voice Sample

`GET /v1/audio/voices/{voice_id}/sample`

Get the audio sample for a voice.

#voice-management #audio-api #rest-api
