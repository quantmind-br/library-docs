---
title: Canvas — Canvas LMS integration — fetch enrolled courses and assignments using API token authentication | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/productivity/productivity-canvas
source: crawler
fetched_at: 2026-04-24T17:01:30.1132067-03:00
rendered_js: false
word_count: 286
summary: This document provides a comprehensive guide and reference for integrating with Canvas LMS, enabling users to fetch course and assignment data using an API token authentication method via a Hermes skill.
tags:
    - canvas-lms
    - api-integration
    - education
    - course-listing
    - assignment-management
    - token-authentication
category: guide
---

Canvas LMS integration — fetch enrolled courses and assignments using API token authentication.

SourceOptional — install with `hermes skills install official/productivity/canvas`Path`optional-skills/productivity/canvas`Version`1.0.0`AuthorcommunityLicenseMITTags`Canvas`, `LMS`, `Education`, `Courses`, `Assignments`

## Reference: full SKILL.md[​](#reference-full-skillmd "Direct link to Reference: full SKILL.md")

info

The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.

## Canvas LMS — Course & Assignment Access

Read-only access to Canvas LMS for listing courses and assignments.

## Scripts[​](#scripts "Direct link to Scripts")

- `scripts/canvas_api.py` — Python CLI for Canvas API calls

## Setup[​](#setup "Direct link to Setup")

1. Log in to your Canvas instance in a browser
2. Go to **Account → Settings** (click your profile icon, then Settings)
3. Scroll to **Approved Integrations** and click **+ New Access Token**
4. Name the token (e.g., "Hermes Agent"), set an optional expiry, and click **Generate Token**
5. Copy the token and add to `~/.hermes/.env`:

```text
CANVAS_API_TOKEN=your_token_here
CANVAS_BASE_URL=https://yourschool.instructure.com
```

The base URL is whatever appears in your browser when you're logged into Canvas (no trailing slash).

## Usage[​](#usage "Direct link to Usage")

```bash
CANVAS="python $HERMES_HOME/skills/productivity/canvas/scripts/canvas_api.py"

# List all active courses
$CANVAS list_courses --enrollment-state active

# List all courses (any state)
$CANVAS list_courses

# List assignments for a specific course
$CANVAS list_assignments 12345

# List assignments ordered by due date
$CANVAS list_assignments 12345 --order-by due_at
```

## Output Format[​](#output-format "Direct link to Output Format")

**list\_courses** returns:

```json
[{"id":12345,"name":"Intro to CS","course_code":"CS101","workflow_state":"available","start_at":"...","end_at":"..."}]
```

**list\_assignments** returns:

```json
[{"id":67890,"name":"Homework 1","due_at":"2025-02-15T23:59:00Z","points_possible":100,"submission_types":["online_upload"],"html_url":"...","description":"...","course_id":12345}]
```

Note: Assignment descriptions are truncated to 500 characters. The `html_url` field links to the full assignment page in Canvas.

## API Reference (curl)[​](#api-reference-curl "Direct link to API Reference (curl)")

```bash
# List courses
curl-s-H"Authorization: Bearer $CANVAS_API_TOKEN"\
"$CANVAS_BASE_URL/api/v1/courses?enrollment_state=active&per_page=10"

# List assignments for a course
curl-s-H"Authorization: Bearer $CANVAS_API_TOKEN"\
"$CANVAS_BASE_URL/api/v1/courses/COURSE_ID/assignments?per_page=10&order_by=due_at"
```

Canvas uses `Link` headers for pagination. The Python script handles pagination automatically.

## Rules[​](#rules "Direct link to Rules")

- This skill is **read-only** — it only fetches data, never modifies courses or assignments
- On first use, verify auth by running `$CANVAS list_courses` — if it fails with 401, guide the user through setup
- Canvas rate-limits to ~700 requests per 10 minutes; check `X-Rate-Limit-Remaining` header if hitting limits

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

ProblemFix401 UnauthorizedToken invalid or expired — regenerate in Canvas Settings403 ForbiddenToken lacks permission for this courseEmpty course listTry `--enrollment-state active` or omit the flag to see all statesWrong institutionVerify `CANVAS_BASE_URL` matches the URL in your browserTimeout errorsCheck network connectivity to your Canvas instance