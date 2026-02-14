---
title: Monitoring | Dokploy
url: https://docs.dokploy.com/docs/core/monitoring
source: crawler
fetched_at: 2026-02-14T14:18:05.138121-03:00
rendered_js: true
word_count: 427
summary: This document explains how to set up and configure server and application monitoring in Dokploy Cloud, covering settings for refresh rates, data retention, and alert thresholds.
tags:
    - dokploy
    - server-monitoring
    - metrics-collection
    - performance-monitoring
    - alert-thresholds
    - infrastructure-management
category: configuration
---

Monitor your applications and servers with Dokploy

### [Prerequisites](#prerequisites)

Before setting up monitoring for your applications and servers, ensure you have completed the server deployment setup. You can verify this by:

1. Navigate to Remote Servers → Select your server → Setup Server
2. Validate that you see a green checkmark in every section

### [Configuration Options](#configuration-options)

Once the prerequisites are met, you can access the Monitoring Section where you'll find the following configuration options:

#### [Refresh Rates](#refresh-rates)

- **Server Refresh Rate**: Determines how frequently the server metrics are collected (default: 20 seconds). Lower values provide more accurate metrics but increase server load.
- **Container Refresh Rate**: Sets the frequency for container metric collection (default: 20 seconds). Similar to server refresh rate, lower values mean more precise data but higher resource usage.

#### [Data Management](#data-management)

- **Cron Job**: Automated task that cleans old metrics based on the retention period settings.
- **Server Retention Days**: Specifies how long metrics data is stored (default: 2 days).
- **Port**: The designated port for the metrics server (default: 4500).

#### [Service Selection](#service-selection)

- **Include Services**: Choose which services to monitor. Options include:
  
  - All services
  - Specific compose services
  - Specific applications
  - Both compose and applications
- **Exclude Services**: Specify services to exclude from monitoring using the same options as above.

#### [Alert Thresholds](#alert-thresholds)

- **CPU Threshold (%)**: Set the CPU usage percentage that triggers an alert. Set to 0 to disable alerts.
- **Memory Threshold (%)**: Set the memory usage percentage that triggers an alert. Set to 0 to disable alerts.

#### [Security and Integration](#security-and-integration)

- **Metrics Token**: Authentication token for metrics requests. You can:
  
  - Use the automatically generated token
  - Generate a new token in the server section
- **Metrics Callback URL**: The endpoint that receives metrics data. Default URL is:
  
  ```
  https://app.dokploy.com/api/trpc/notification.receiveNotification
  ```
  
  You can use this default or configure your own callback URL.

In order to enable just click on `Save Changes` button.

### [Notifications](#notifications)

If you have configured notifications with Server Threshold properties, metric alerts will be sent to your enabled notification providers, the notifications will sent only if the threshold is exceeded based on the Server itself not individual services.

### [Important Security Note](#important-security-note)

**Make sure port 4500 is open on your server** to allow proper communication of monitoring metrics. This is essential for the monitoring system to function correctly.

If you have errors like failed to fetch metrics, or no data available, just give it a few minutes and check again, this is normal, the server needs to collect data first.

You should see something like this for your server:

![Architecture Diagram](https://docs.dokploy.com/_next/image?url=%2Fmonitoring.png&w=3840&q=75)

For your services you should see something like this:

![Architecture Diagram](https://docs.dokploy.com/_next/image?url=%2Fmonitoring-services.png&w=3840&q=75)

This is feature only available on Cloud Version of Dokploy.