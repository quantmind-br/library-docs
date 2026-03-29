---
title: ForgeCode
url: https://forgecode.dev/docs/logging/
source: sitemap
fetched_at: 2026-03-29T14:52:00.249578755-03:00
rendered_js: false
word_count: 409
summary: This document explains how to work with ForgeCode's JSON-formatted logging system, including how to locate, view, filter, and analyze logs for troubleshooting and system monitoring purposes.
tags:
    - json-logs
    - troubleshooting
    - log-analysis
    - error-handling
    - api-interactions
    - log-filtering
    - jq-parsing
    - log-rotation
category: guide
---

ForgeCode generates detailed JSON-formatted logs that help with troubleshooting and understanding the application's behavior. These logs provide valuable insights into system operations and API interactions.

Logs are stored in your application support directory with date-based filenames. The typical path looks like:

You can easily locate log files using the built-in command `/info`, which displays system information including the exact path to your log files.

ForgeCode logs are structured in JSON format, making them easy to parse and analyze. Each log entry contains fields such as:

- **timestamp**: When the event occurred
- **level**: Log level (info, warn, error, debug)
- **message**: Description of the event
- **context**: Additional contextual information
- **requestId**: Identifier for API requests (when applicable)
- **duration**: Time taken for operations (when applicable)

Example log entry:

### Basic Log Viewing[​](#basic-log-viewing "Direct link to Basic Log Viewing")

To view logs in real-time with automatic updates, use the `tail` command:

### Formatted Log Viewing with jq[​](#formatted-log-viewing-with-jq "Direct link to Formatted Log Viewing with jq")

Since ForgeCode logs are in JSON format, you can pipe them through `jq` for better readability:

This displays the logs in a nicely color-coded structure that's much easier to analyze.

### Filtering Logs[​](#filtering-logs "Direct link to Filtering Logs")

You can use `jq` to filter logs for specific information:

ForgeCode uses different log levels to categorize information:

- **debug**: Detailed debugging information
- **info**: General information about system operation
- **warn**: Warning conditions that don't cause errors
- **error**: Error conditions that affect operation

You can configure the log level in your environment variables:

### API Interactions[​](#api-interactions "Direct link to API Interactions")

Look for logs containing API request and response information to understand model interactions:

### File Operations[​](#file-operations "Direct link to File Operations")

File operations are logged with details about paths and actions:

### Shell Commands[​](#shell-commands "Direct link to Shell Commands")

Shell command execution is logged with command details and results:

### API Issues[​](#api-issues "Direct link to API Issues")

If you're experiencing problems with AI responses:

1. Look for logs with level "error" and context related to API calls
2. Check for rate limiting or token quota issues
3. Verify API key validity in error messages

Example search:

### Performance Analysis[​](#performance-analysis "Direct link to Performance Analysis")

To analyze performance:

1. Look for logs with duration information
2. Identify operations that take longer than expected
3. Check for patterns in slow operations

Example search:

### File Operation Errors[​](#file-operation-errors "Direct link to File Operation Errors")

For file operation issues:

1. Search for file-related error logs
2. Check for permission issues or missing paths
3. Verify file content details

Example search:

### Log Rotation[​](#log-rotation "Direct link to Log Rotation")

ForgeCode automatically rotates logs daily, creating new files with the current date. Old logs are retained but not actively written to.

### Storage Considerations[​](#storage-considerations "Direct link to Storage Considerations")

Log files can grow large with heavy usage. Consider periodically archiving or removing old logs to conserve disk space:

### Log Archiving[​](#log-archiving "Direct link to Log Archiving")

For important sessions, you might want to archive logs: