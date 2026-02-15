---
title: dap env vars | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/dap-cli-readme/dap-cli-reference/dap-cli-reference-env-vars
source: sitemap
fetched_at: 2026-02-15T09:11:35.432142-03:00
rendered_js: false
word_count: 124
summary: This document explains how to configure the DAP CLI using environment variables for authentication, database connection settings, and usage tracking to simplify automation and improve security.
tags:
    - dap-cli
    - environment-variables
    - configuration
    - automation
    - authentication
category: configuration
---

To simplify configuration and improve security, the DAP CLI supports reading authentication and connection settings from environment variables. This is optional but highly recommended for automation and scripting on macOS, Linux, and Windows.

## Available Environment Variables

```
exportDAP_API_URL='https://api-gateway.instructure.com'
exportDAP_CLIENT_ID='your_canvas_data_client_id'
exportDAP_CLIENT_SECRET='your_canvas_data_secret'
exportDAP_CONNECTION_STRING='your_database_connection_string'
exportDAP_TRACKING='your_tracking_preference'
```

- `DAP_API_URL` *(optional)* Specifies the API endpoint. If omitted, the CLI uses the default production URL. Useful when working in beta or staging environments.
- `DAP_CONNECTION_STRING` *(optional)* The connection string to your target database. Supported formats:
  
  ```
  postgresql://user:password@host:5432/database
  mysql://user:password@host:3306/database
  mssql://user:password@host:1433/database
  ```
- `DAP_TRACKING` Controls whether CLI usage tracking is enabled. Tracking is enabled by default. To opt out, use one of the values listed below.
  
  Valid values for enabling/disabling tracking:

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).