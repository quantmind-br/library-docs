---
title: AgentQL Extension | goose
url: https://block.github.io/goose/docs/mcp/agentql-mcp
source: github_pages
fetched_at: 2026-01-22T22:14:37.545304819-03:00
rendered_js: true
word_count: 41
summary: This tutorial demonstrates how to integrate the AgentQL MCP Server as a goose extension to extract and transform unstructured web content into structured JSON data.
tags:
    - agentql
    - mcp-server
    - goose-extension
    - web-extraction
    - data-transformation
    - structured-data
category: tutorial
---

This tutorial covers how to add the [AgentQL MCP Server](https://github.com/tinyfish-io/agentql-mcp) as a goose extension to extract and transform unstructured web content into structured data.

Let's use the AgentQL extension to gather and structure tech conference data to help plan speaking engagements.

```
I'm a tech conference speaker planning my 2025-2026 submissions. 

Extract for developer conferences (attendance > 500) occurring between 2022-2024:
- Conference name
- Conference dates
- CFP timeline 

To identify:
- Consistent monthly patterns
- Whether conferences stick to same months yearly
- If CFP windows are consistent year-to-year
- Any shifts in traditional timing

Structure results as JSON
```

```
I'll help you analyze conference patterns using the web data extraction tool. Let me break this down into a few queries to get comprehensive data.

─── extract-web-data | agentql ──────────────────────────
prompt: ...
url: ...

Let me get some historical data to compare patterns:

─── extract-web-data | agentql ──────────────────────────
prompt: ....
url: ....

Based on my research and the available data, I'll provide an analysis of major tech conference patterns. Here's the structured JSON with my findings:

{
  "analysis": {
    "major_conference_patterns": {
      "timing_consistency": {
        "spring_events": {
          "typical_months": ["March", "April", "May"],
          "notable_conferences": [
            "Google I/O",
            "Microsoft Build",
            "DevOpsDays (various locations)"
          ],
          "cfp_patterns": "Usually opens 4-6 months before event, closes 2-3 months before"
        },
        "fall_events": {
          "typical_months": ["September", "October", "November"],
          "notable_conferences": [
            "AWS re:Invent",
            "KubeCon + CloudNativeCon"
          ],
          "cfp_patterns": "Usually opens 6-8 months before event, closes 4-5 months before"
        }
      },
      "observed_trends": {
        "timing_consistency": "High - Most major conferences maintain consistent months year-over-year",
        "cfp_windows": {
          "typical_duration": "6-12 weeks",
          "advance_notice": "4-8 months before event",
          "variation": "Regional events tend to have shorter CFP windows (4-6 weeks)"
        },
        "recent_shifts": [
          "Increased hybrid/virtual options post-2022",
          "More regional editions of major conferences",
          "Earlier CFP deadlines for larger events"
        ]
      }
    },
    "recommendations_for_2025_2026": {
      "spring_submissions": {
        "prepare_by": "September-October of previous year",
        "submit_during": "November-December of previous year"
      },
      "fall_submissions": {
        "prepare_by": "February-March",
        "submit_during": "March-April"
      }
    }
  }
}


Key Insights for Your Planning:

1. **Monthly Patterns**:
   - Spring conference season: March-May
   - Fall conference season: September-November
   - Summer tends to be lighter for major tech conferences
   - December-January typically quiet except for regional events

2. **Year-to-Year Consistency**:
   - Major conferences (AWS re:Invent, KubeCon, Google I/O) are very consistent with their timing
   - Regional versions of major conferences (like DevOpsDays) show more date flexibility
   - Most maintain the same quarter/season year over year

3. **CFP Windows**:
   - Larger conferences: 6-8 months before event
   - Regional conferences: 3-4 months before event
   - Trend toward longer review periods for major conferences
   - Many now have rolling or multi-phase CFP processes

4. **Recent Shifts**:
   - Earlier CFP deadlines compared to pre-2022
   - More hybrid/virtual components
   - Increased number of regional editions of major conferences
   - Longer review periods for submissions

For 2025-2026 planning, I recommend:
- Start preparing fall 2025 submissions by February-March 2025
- Start preparing spring 2026 submissions by September-October 2025
- Consider regional versions of major conferences as they often have later deadlines
- Keep track of multi-track conferences as they might have different CFP deadlines for different tracks

Would you like me to focus on any specific aspect of these patterns or provide more detailed information about particular conferences?
```