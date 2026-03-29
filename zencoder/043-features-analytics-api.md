---
title: Analytics API - Zencoder Docs
url: https://docs.zencoder.ai/features/analytics-api
source: crawler
fetched_at: 2026-01-23T09:28:13.072845069-03:00
rendered_js: false
word_count: 455
summary: This document provides a technical guide to the Zencoder Analytics API, covering authentication via OAuth 2.0 and instructions for programmatically retrieving usage data.
tags:
    - zencoder-api
    - analytics-data
    - oauth-2-0
    - rest-api
    - usage-tracking
    - authentication
category: api
---

## Overview

The Zencoder Analytics API enables programmatic access to your organization’s usage data, allowing you to integrate Zencoder metrics into your existing business intelligence tools, custom dashboards, and reporting systems. This REST API provides the same data available in the [Analytics Dashboard](https://docs.zencoder.ai/features/analytics) in a machine-readable format.

## Getting Your API Credentials

Before making API requests, you’ll need to generate a personal access token to obtain your `client_id` and `client_secret`:

1. Navigate to [auth.zencoder.ai](https://auth.zencoder.ai) and sign in
2. Go to **Administration → Settings**
3. Select **Personal Tokens** from the settings menu
4. Click **Generate Token**
5. Configure your token:
   
   - **Description**: Enter a meaningful identifier (e.g., “Analytics API Integration” or “BI Dashboard”)
   - **Expiration**: Select an appropriate duration for your use case
6. Click **Generate**

## Authentication

To authenticate and obtain a JWT access token, make a POST request to the authentication endpoint. **Endpoint**

```
POST https://fe.zencoder.ai/oauth/token
```

**Headers**

- `Content-Type: application/json`

**Request Body Parameters**

ParameterTypeRequiredDescription`client_id`stringYesYour client identifier`client_secret`stringYesYour client secret key`grant_type`stringYesOAuth 2.0 grant type. Use `"client_credentials"`

**Using the Access Token** Include the obtained JWT token in the `Authorization` header of subsequent API requests:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Example Requests**

- cURL
- Node.js
- Python

```
# Get access token
curl -X POST https://fe.zencoder.ai/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "grant_type": "client_credentials"
  }'

# Use the token in subsequent requests
curl -X GET https://api.zencoder.ai/your-endpoint \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

```
// Get access token
const response = await fetch('https://fe.zencoder.ai/oauth/token', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    client_id: 'your_client_id',
    client_secret: 'your_client_secret',
    grant_type: 'client_credentials'
  })
});

const { access_token } = await response.json();

// Use the token in subsequent requests
const usageResponse = await fetch('https://api.zencoder.ai/your-endpoint', {
  headers: {
    'Authorization': `Bearer ${access_token}`
  }
});
```

```
import requests

# Get access token
response = requests.post(
    'https://fe.zencoder.ai/oauth/token',
    headers={'Content-Type': 'application/json'},
    json={
        'client_id': 'your_client_id',
        'client_secret': 'your_client_secret',
        'grant_type': 'client_credentials'
    }
)

access_token = response.json()['access_token']

# Use the token in subsequent requests
usage_response = requests.get(
    'https://api.zencoder.ai/your-endpoint',
    headers={'Authorization': f'Bearer {access_token}'}
)
```

**Response**

```
{
  "token_type": "Bearer",
  "access_token": "eyJhbGciOiJSU...",
  "id_token": "eyJhbGciOiJSU...",
  "refresh_token": "5bead02f-...",
  "expires_in": 86400
}
```

**Response Fields**

## Usage Data Endpoint

Retrieves usage analytics data for the authenticated tenant (account). **Endpoint**

**Headers**

- `Authorization: Bearer YOUR_ACCESS_TOKEN`

**Query String Parameters**

ParameterTypeRequiredDescription`period`stringNoTime period for usage data. Must be one of: `7d`, `30d`, `90d`. Defaults to `7d` if neither `period` nor `day` is provided`day`stringNoSpecific day for usage data in `YYYY-MM-DD` format. Cannot be used together with `period`

**Note**: You must provide either `period` OR `day`, but not both. If neither is provided, defaults to `period=7d`. **Example Requests** Get usage data for the last 30 days:

```
GET /api/v1/data/usage?period=30d HTTP/1.1
Host: api.zencoder.ai
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

Get usage data for a specific day:

```
GET /api/v1/data/usage?day=2025-10-15 HTTP/1.1
Host: api.zencoder.ai
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response** Success Response (200 OK):

```
{
  "status": "success",
  "data": {
    "period": {
      "start": "2025-09-24",
      "end": "2025-10-01",
      "days": 7
    },
    "summary": {
      "total_active_users": 48,
      "total_messages": 1372
    },
    "users": [
      {
        "email": "joe.doe@example.ai",
        "messages": 58,
        "last_active": "2025-10-01",
        "ides": [
          "VS Code"
        ],
        "languages": [
          "JavaScript",
          "TypeScript"
        ]
      }
    ],
    "daily": [
      {
        "day": "2025-09-24",
        "active_users": 21,
        "messages": 188,
        "ides": [
          {
            "ide_name": "VS Code",
            "engaged_users": 6
          },
          {
            "ide_name": "IntelliJ CE",
            "engaged_users": 1
          },
          {
            "ide_name": "WebStorm",
            "engaged_users": 1
          }
        ],
        "languages": [
          {
            "language_name": "JavaScript",
            "engaged_users": 1
          },
          {
            "language_name": "TypeScript",
            "engaged_users": 2
          }
        ]
      }
    ]
  }
}
```

Error Responses:

**Response Fields**

**Example Requests**

- Last 30 Days
- Specific Day
- Last 7 Days (Default)

<!--THE END-->

- cURL
- Node.js
- Python

```
curl -X GET "https://api.zencoder.ai/api/v1/data/usage?period=30d" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

```
const response = await fetch('https://api.zencoder.ai/api/v1/data/usage?period=30d', {
  headers: {
    'Authorization': `Bearer ${access_token}`
  }
});
const data = await response.json();
```

```
response = requests.get(
    'https://api.zencoder.ai/api/v1/data/usage?period=30d',
    headers={'Authorization': f'Bearer {access_token}'}
)
data = response.json()
```

- cURL
- Node.js
- Python

```
curl -X GET "https://api.zencoder.ai/api/v1/data/usage?day=2025-10-15" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

```
const response = await fetch('https://api.zencoder.ai/api/v1/data/usage?day=2025-10-15', {
  headers: {
    'Authorization': `Bearer ${access_token}`
  }
});
const data = await response.json();
```

```
response = requests.get(
    'https://api.zencoder.ai/api/v1/data/usage?day=2025-10-15',
    headers={'Authorization': f'Bearer {access_token}'}
)
data = response.json()
```

- cURL
- Node.js
- Python

```
curl -X GET "https://api.zencoder.ai/api/v1/data/usage" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

```
const response = await fetch('https://api.zencoder.ai/api/v1/data/usage', {
  headers: {
    'Authorization': `Bearer ${access_token}`
  }
});
const data = await response.json();
```

```
response = requests.get(
    'https://api.zencoder.ai/api/v1/data/usage',
    headers={'Authorization': f'Bearer {access_token}'}
)
data = response.json()
```

## Troubleshooting