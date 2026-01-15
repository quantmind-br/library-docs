---
title: Readiness Reports API - Factory Documentation
url: https://docs.factory.ai/reference/readiness-reports-api
source: sitemap
fetched_at: 2026-01-13T19:04:32.823817172-03:00
rendered_js: false
word_count: 305
summary: This document outlines the Readiness Reports API, which enables developers to programmatically access organization-wide agent readiness evaluation data. It covers authentication procedures, endpoint details for retrieving reports, schema definitions for data objects, and pagination logic.
tags:
    - api
    - readiness-reports
    - factory-api
    - agent-evaluation
    - authentication
    - pagination
    - api-reference
category: api
---

The Readiness Reports API provides programmatic access to your organization’s agent readiness evaluation data.

* * *

## Authentication

All requests require a Factory API key in the `Authorization` header:

```
Authorization: Bearer fk-your-api-key
```

Generate API keys at [app.factory.ai/settings/api-keys](https://app.factory.ai/settings/api-keys).

* * *

## Base URL

* * *

## Endpoints

### List Readiness Reports

Retrieves readiness reports for your organization.

```
GET /api/organization/maturity-level-reports
```

#### Query Parameters

ParameterTypeRequiredDescription`repoId`stringNoFilter reports by repository ID`limit`integerNoMaximum number of reports to return (must be positive)`startAfter`stringNoReport ID for pagination cursor

#### Response

```
{
  "reports": [
    {
      "reportId": "550e8400-e29b-41d4-a716-446655440000",
      "createdAt": 1701792000000,
      "repoUrl": "https://github.com/org/repo",
      "apps": {
        "apps/web": {
          "description": "Main Next.js application"
        },
        "apps/api": {
          "description": "Backend API service"
        }
      },
      "report": {
        "lint_config": {
          "numerator": 2,
          "denominator": 2,
          "rationale": "ESLint configured in both applications"
        },
        "type_check": {
          "numerator": 2,
          "denominator": 2,
          "rationale": "TypeScript strict mode enabled"
        }
      },
      "commitHash": "abc123def456",
      "branch": "main",
      "hasLocalChanges": false,
      "hasNonRemoteCommits": false,
      "modelUsed": {
        "id": "claude-sonnet-4-5",
        "reasoningEffort": "high"
      },
      "droidVersion": "0.30.0"
    }
  ]
}
```

#### Example Request

```
curl -X GET "https://app.factory.ai/api/organization/maturity-level-reports?limit=10" \
  -H "Authorization: Bearer fk-your-api-key"
```

* * *

## Readiness Report Schema

### Report Object

FieldTypeDescription`reportId`stringUnique identifier for the report (UUID)`createdAt`numberUnix timestamp in milliseconds when the report was created`repoUrl`stringRepository URL that was evaluated`apps`objectMap of application paths to description objects`report`objectMap of criterion IDs to evaluation results`commitHash`string?Git commit hash at time of evaluation`branch`string?Git branch name at time of evaluation`hasLocalChanges`boolean?Whether uncommitted changes existed`hasNonRemoteCommits`boolean?Whether unpushed commits existed`modelUsed`object?Model configuration used for evaluation`droidVersion`string?CLI version that generated the report

### App Description Object

FieldTypeDescription`description`stringBrief description of what the application does

### Criterion Evaluation Object

FieldTypeDescription`numerator`numberNumber of sub-applications passing the criterion (0 to denominator)`denominator`numberNumber of sub-applications on which the criterion was evaluated (minimum 1)`rationale`stringExplanation of the evaluation result

### Model Used Object

FieldTypeDescription`id`stringModel identifier`reasoningEffort`stringReasoning effort level (`low`, `medium`, `high`, `off`)

* * *

For large result sets, use cursor-based pagination:

1. Make initial request with desired `limit`
2. Get the `reportId` of the last item in the response
3. Pass that ID as `startAfter` in the next request

```
# First page
curl "https://app.factory.ai/api/organization/maturity-level-reports?limit=10"

# Next page (using last reportId from previous response)
curl "https://app.factory.ai/api/organization/maturity-level-reports?limit=10&startAfter=550e8400-e29b-41d4-a716-446655440000"
```

* * *

## Use Cases

### CI/CD Integration

Track readiness scores over time by fetching reports after each evaluation:

```
# Get latest report for a specific repository
curl "https://app.factory.ai/api/organization/maturity-level-reports?repoId=123&limit=1" \
  -H "Authorization: Bearer $FACTORY_API_KEY"
```

### Custom Dashboards

Build internal dashboards by fetching all reports and calculating aggregate metrics:

```
const response = await fetch(
  "https://app.factory.ai/api/organization/maturity-level-reports",
  { headers: { Authorization: `Bearer ${apiKey}` } }
);
const { reports } = await response.json();

// Calculate average level
const avgLevel =
  reports.reduce((sum, r) => sum + calculateLevel(r), 0) / reports.length;
```

### Automated Alerting

Set up alerts when readiness scores drop below thresholds:

```
# Fetch recent reports and check for regressions
reports=$(curl -s "https://app.factory.ai/api/organization/maturity-level-reports?limit=50" \
  -H "Authorization: Bearer $FACTORY_API_KEY")

# Process and alert on regressions...
```

* * *

## Error Responses

StatusDescription`400`Invalid request parameters`401`Missing or invalid API key`500`Internal server error