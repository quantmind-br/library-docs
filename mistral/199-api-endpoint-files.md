---
title: Files
url: https://docs.mistral.ai/api/endpoint/files
source: sitemap
fetched_at: 2026-04-26T04:02:13.182101585-03:00
rendered_js: false
word_count: 75
summary: REST API endpoints for managing, uploading, retrieving, and deleting organization files.
tags:
    - file-management
    - api-endpoints
    - data-upload
    - rest-api
    - file-storage
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Files

File management API for organization resources.

---

## Endpoints

| Method | Path | Description |
|-------|------|-------------|
| `GET` | `/v1/files` | List files belonging to organization |
| `POST` | `/v1/files` | Upload file (max 512 MB per file; Fine-tuning only supports .jsonl) |
| `GET` | `/v1/files/{file_id}` | Get file information |
| `DELETE` | `/v1/files/{file_id}` | Delete a file |
| `GET` | `/v1/files/{file_id}/content` | Download file |
| `GET` | `/v1/files/{file_id}/url` | Get file URL |

> [!info]
> Contact support to increase storage limits.

#file-management #file-storage #data-upload
