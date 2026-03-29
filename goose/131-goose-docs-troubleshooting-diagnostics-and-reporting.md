---
title: Diagnostics and Reporting | goose
url: https://block.github.io/goose/docs/troubleshooting/diagnostics-and-reporting
source: github_pages
fetched_at: 2026-01-22T22:16:06.296640755-03:00
rendered_js: true
word_count: 510
summary: This guide explains how to use goose's support features, including generating diagnostic bundles, reporting bugs, and requesting new features.
tags:
    - troubleshooting
    - diagnostics
    - bug-reporting
    - feature-requests
    - support-tools
    - error-recovery
category: guide
---

goose provides several built-in features to help you get support, report issues, and request new functionality. This guide covers the diagnostics system, bug reporting, and feature request tools.

FeaturePurposeLocationOutput**Diagnostics**Generate troubleshooting dataChat input toolbarZIP file with system info, logs, and session data**Report a Bug**Submit bug reportsSettings → Help & feedbackOpens GitHub issue template**Request a Feature**Suggest new featuresSettings → Help & feedbackOpens GitHub issue template

## Diagnostics System[​](#diagnostics-system "Direct link to Diagnostics System")

The diagnostics feature creates a comprehensive troubleshooting bundle that includes system information, session data, configuration files, and recent logs. This is invaluable for debugging issues or getting technical support.

### Generating Diagnostics[​](#generating-diagnostics "Direct link to Generating Diagnostics")

- goose Desktop
- goose CLI

<!--THE END-->

1. In an active chat session, look for the icon in the bottom toolbar
2. Click the diagnostics button
3. Review the information in the modal about what data will be collected
4. Click `Download` to generate and save the diagnostics bundle
5. The ZIP file will be saved as `diagnostics_{session_id}.zip`

tip

The diagnostics button is only available when you have an active session, as it needs a session ID to generate the bundle.

### Using Diagnostics Data[​](#using-diagnostics-data "Direct link to Using Diagnostics Data")

The diagnostics ZIP file contains several folders:

```
diagnostics_abc123def.zip
├── logs/
│   ├── goose-2024-01-15.jsonl
│   ├── goose-2024-01-14.jsonl
│   └── ...
├── session.json          # Your session messages
├── config.yaml          # Configuration files (if they exist)
└── system.txt           # System information
```

**When to generate diagnostics:**

- Experiencing crashes or unexpected behavior
- Getting error messages you don't understand
- Performance issues or slow responses
- Before reporting bugs to include technical details

**What's included in diagnostics:**

- **System Information**: App version, operating system, architecture, and timestamp
- **Session Data**: Your current conversation messages and history
- **Configuration Files**: Your [configuration files](https://block.github.io/goose/docs/guides/config-files) (if they exist)
- **Log Files**: Recent application logs for debugging

Privacy Notice

Diagnostics bundles contain your session messages and system information. If your session includes sensitive data (API keys, personal information, proprietary code), review the contents before sharing publicly.

## Bug Reports[​](#bug-reports "Direct link to Bug Reports")

The bug report feature opens a structured GitHub issue template to help you provide all necessary information for effective bug reporting.

### Creating Bug Reports[​](#creating-bug-reports "Direct link to Creating Bug Reports")

- goose Desktop
- goose CLI

<!--THE END-->

1. Click the button in the top-left to open the sidebar
2. Click `Settings` in the sidebar
3. Scroll down to the `Help & feedback` section
4. Click `Report a Bug`
5. This opens GitHub in your browser with a pre-filled bug report template

## Feature Requests[​](#feature-requests "Direct link to Feature Requests")

The feature request system helps you suggest improvements and new functionality for goose.

### Submitting Feature Requests[​](#submitting-feature-requests "Direct link to Submitting Feature Requests")

- goose Desktop
- goose CLI

<!--THE END-->

1. Click the button in the top-left to open the sidebar
2. Click `Settings` in the sidebar
3. Scroll down to the `Help & feedback` section
4. Click `Request a Feature`
5. This opens GitHub in your browser with a feature request template

## Error Recovery with "Ask goose"[​](#error-recovery-with-ask-goose 'Direct link to Error Recovery with "Ask goose"')

When certain types of error occur in goose Desktop (such as failures to activate extensions), you'll see an `Ask goose` button in the error notification. This feature lets you quickly troubleshoot the issue with goose's help:

1. When the error occurs, an `Ask goose` button appears in the error notification
2. Click the button to send the error details to goose in a chat prompt
3. goose provides diagnostic suggestions and potential solutions

## Additional Debugging[​](#additional-debugging "Direct link to Additional Debugging")

For issues not resolved by diagnostics:

- [**Session and System Logs**](https://block.github.io/goose/docs/guides/logs): View detailed logs for debugging individual sessions
- [**Telemetry Export**](https://block.github.io/goose/docs/guides/environment-variables#observability): Configure telemetry for performance analysis and production monitoring