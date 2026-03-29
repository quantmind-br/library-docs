---
title: Analytics Dashboard - Zencoder Docs
url: https://docs.zencoder.ai/features/analytics
source: crawler
fetched_at: 2026-01-23T09:28:14.05580779-03:00
rendered_js: false
word_count: 498
summary: This document explains how organizational administrators can use the Zencoder Analytics dashboard to monitor team engagement, track usage trends, and analyze developer activity metrics. It provides instructions for interpreting dashboard components, exporting data for custom reporting, and implementing best practices for resource optimization.
tags:
    - zencoder-analytics
    - usage-metrics
    - admin-dashboard
    - developer-productivity
    - data-export
    - user-engagement
category: guide
---

## Overview

Zencoder Analytics provides organizational administrators with daily insights into how their teams are using Zencoder. The dashboard delivers actionable metrics that help engineering managers make informed decisions about resource allocation, identify adoption patterns, and optimize their team’s development workflow.

## Accessing Analytics

Navigate to your [Analytics dashboard](https://auth.zencoder.ai/analytics) directly, or go to [auth.zencoder.ai](https://auth.zencoder.ai) and select `Analytics` from the sidebar navigation. ![Zencoder Analytics dashboard showing active users graph and member activity table with IDE and language usage data](https://mintcdn.com/forgoodaiinc/NXH8pGxYpJ6zaJow/images/analytics.png?fit=max&auto=format&n=NXH8pGxYpJ6zaJow&q=85&s=170ac8911b7e8e043d5c6cc79fa3f95e)

## Dashboard Components

### Active Users Metric

The prominent metric card displays the total number of unique users who have actively engaged with Zencoder agents during the selected time period. This provides a quick snapshot of overall adoption across your organization.

### Usage Trends Graph

The interactive line chart visualizes daily active user patterns over time, helping you:

- Identify usage trends and patterns (weekday vs. weekend activity)
- Track adoption growth following team onboarding
- Spot anomalies that may require investigation
- Understand seasonal or project-based usage fluctuations

Hover over any data point to see precise user counts for that specific day.

### Time Period Filters

Select from three predefined time ranges to analyze your data:

- `7 days`: Focus on recent activity and immediate trends
- `30 days`: Understand monthly patterns and team rhythms
- `90 days`: Analyze quarterly trends and long-term adoption

### Member Activity Table

The detailed member table provides granular insights into individual usage:

ColumnDescription`Email`User identification for tracking individual adoption`Agent Messages`Total number of interactions with Zencoder agents, indicating engagement level`IDEs`Development environments used by each member (VS Code, IDEA, PyCharm, etc.)`Languages`Programming languages the user has been utilizing Zencoder for`Last Active`Most recent activity timestamp to identify active vs. dormant users

### Data Export

Download your analytics data as a CSV file for:

- Integration with existing business intelligence tools
- Custom analysis and reporting (including IDE and language distribution)
- Compliance and audit requirements
- Historical record keeping

## Best Practices

1. Regularly review analytics data by scheduling weekly or monthly check-ins to maintain visibility into team usage patterns and trends
2. Set baselines by establishing what normal usage patterns look like for your team so you can quickly identify anomalies or changes in behavior
3. Share insights from the exported data to create reports for stakeholders and demonstrate the value of Zencoder across your organization
4. Track onboarding success by monitoring new user adoption rates after training sessions to ensure your rollouts are effective
5. Optimize license allocation by analyzing actual usage patterns and reallocating seats to teams that will benefit most from Zencoder
6. Leverage IDE and language insights to identify technology patterns across your organization—use this data to prioritize training resources, share best practices between teams using similar stacks, and ensure your tooling investments align with actual developer needs

## Troubleshooting

- Verify you have Owner or Manager permissions
- Ensure your subscription is Core or higher

### Missing Users

- Confirm users are part of your organization
- Verify users have authenticated at least once
- Check if filters are excluding certain time periods

### Export Issues

- Ensure your browser allows file downloads
- Check available disk space for CSV downloads
- Try a different browser if issues persist