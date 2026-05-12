---
title: Agent | Firecrawl
url: https://docs.firecrawl.dev/features/agent
source: sitemap
fetched_at: 2026-03-23T07:24:49.487937-03:00
rendered_js: false
word_count: 1021
summary: This document explains the functionality and usage of the Firecrawl /agent API, a tool designed to autonomously search, navigate, and extract structured data from websites using natural language prompts.
tags:
    - web-scraping
    - data-extraction
    - ai-agent
    - api-documentation
    - automated-research
    - structured-data
category: api
---

Firecrawl `/agent` is a magic API that searches, navigates, and gathers data from the widest range of websites, finding data in hard-to-reach places and uncovering data in ways no other API can. It accomplishes in a few minutes what would take a human many hours — end-to-end data collection, without scripts or manual work. Whether you need one data point or entire datasets at scale, Firecrawl `/agent` works to get your data. **Think of `/agent` as deep research for data, wherever it is!**

Agent builds on everything great about `/extract` and takes it further:

- **No URLs Required**: Just describe what you need via `prompt` parameter. URLs are optional
- **Deep Web Search**: Autonomously searches and navigates deep into sites to find your data
- **Reliable and Accurate**: Works with a wide variety of queries and use cases
- **Faster**: Processes multiple sources in parallel for quicker results

## Using `/agent`

The only required parameter is `prompt`. Simply describe what data you want to extract. For structured output, provide a JSON schema. The SDKs support Pydantic (Python) and Zod (Node) for type-safe schema definitions:

### Response

```
{
  "success": true,
  "status": "completed",
  "data": {
    "founders": [
      {
        "name": "Eric Ciarla",
        "role": "Co-founder",
        "background": "Previously at Mendable"
      },
      {
        "name": "Nicolas Camara",
        "role": "Co-founder",
        "background": "Previously at Mendable"
      },
      {
        "name": "Caleb Peffer",
        "role": "Co-founder",
        "background": "Previously at Mendable"
      }
    ]
  },
  "expiresAt": "2024-12-15T00:00:00.000Z",
  "creditsUsed": 15
}
```

## Providing URLs (Optional)

You can optionally provide URLs to focus the agent on specific pages:

## Job Status and Completion

Agent jobs run asynchronously. When you submit a job, you’ll receive a Job ID that you can use to check status:

- **Default method**: `agent()` waits and returns final results
- **Start then poll**: Use `start_agent` (Python) or `startAgent` (Node) to get a Job ID immediately, then poll with `get_agent_status` / `getAgentStatus`

### Possible States

StatusDescription`processing`The agent is still working on your request`completed`Extraction finished successfully`failed`An error occurred during extraction`cancelled`The job was cancelled by the user

#### Pending Example

```
{
  "success": true,
  "status": "processing",
  "expiresAt": "2024-12-15T00:00:00.000Z"
}
```

#### Completed Example

```
{
  "success": true,
  "status": "completed",
  "data": {
    "founders": [
      {
        "name": "Eric Ciarla",
        "role": "Co-founder"
      },
      {
        "name": "Nicolas Camara",
        "role": "Co-founder"
      },
      {
        "name": "Caleb Peffer",
        "role": "Co-founder"
      }
    ]
  },
  "expiresAt": "2024-12-15T00:00:00.000Z",
  "creditsUsed": 15
}
```

You can share agent runs directly from the Agent playground. Shared links are public — anyone with the link can view the run output and activity — and you can revoke access at any time to disable the link. Shared pages are not indexed by search engines.

## Model Selection

Firecrawl Agent offers two models. **Spark 1 Mini is 60% cheaper** and is the default — perfect for most use cases. Upgrade to Spark 1 Pro when you need maximum accuracy on complex tasks.

ModelCostAccuracyBest For`spark-1-mini`**60% cheaper**StandardMost tasks (default)`spark-1-pro`StandardHigherComplex research, critical extraction

### Spark 1 Mini (Default)

`spark-1-mini` is our efficient model, ideal for straightforward data extraction tasks. **Use Mini when:**

- Extracting simple data points (contact info, pricing, etc.)
- Working with well-structured websites
- Cost efficiency is a priority
- Running high-volume extraction jobs

### Spark 1 Pro

`spark-1-pro` is our flagship model, designed for maximum accuracy on complex extraction tasks. **Use Pro when:**

- Performing complex competitive analysis
- Extracting data that requires deep reasoning
- Accuracy is critical for your use case
- Dealing with ambiguous or hard-to-find data

### Specifying a Model

Pass the `model` parameter to select which model to use:

## Parameters

ParameterTypeRequiredDescription`prompt`string**Yes**Natural language description of the data you want to extract (max 10,000 characters)`model`stringNoModel to use: `spark-1-mini` (default) or `spark-1-pro``urls`arrayNoOptional list of URLs to focus the extraction`schema`objectNoOptional JSON schema for structured output`maxCredits`numberNoMaximum number of credits to spend on this agent task. Defaults to **2,500** if not set. The dashboard supports values up to **2,500**; for higher limits, set `maxCredits` via the API (values above 2,500 are always treated as paid requests). If the limit is reached, the job fails and **no data is returned**, though credits consumed for work performed are still charged.

FeatureAgent (New)ExtractURLs RequiredNoYesSpeedFasterStandardCostLowerStandardReliabilityHigherStandardQuery FlexibilityHighModerate

## Example Use Cases

- **Research**: “Find the top 5 AI startups and their funding amounts”
- **Competitive Analysis**: “Compare pricing plans between Slack and Microsoft Teams”
- **Data Gathering**: “Extract contact information from company websites”
- **Content Summarization**: “Summarize the latest blog posts about web scraping”

## CSV Upload in Agent Playground

The [Agent Playground](https://www.firecrawl.dev/app/agent) supports CSV upload for batch processing. Your CSV can contain one or more columns of input data. For example, a single column of company names, or multiple columns such as company name, product, and website URL. Each row represents one item for the agent to process. Upload your CSV, write a prompt describing what data you want the agent to find for each row, define your output fields, and run. The agent processes each row in parallel and fills in the results.

## API Reference

Check out the [Agent API Reference](https://docs.firecrawl.dev/api-reference/endpoint/agent) for more details. Have feedback or need help? Email [help@firecrawl.com](mailto:help@firecrawl.com).

## Pricing

Firecrawl Agent uses **dynamic billing** that scales with the complexity of your data extraction request. You pay based on the actual work Agent performs, ensuring fair pricing whether you’re extracting simple data points or complex structured information from multiple sources.

### How Agent pricing works

Agent pricing is **dynamic and credit-based** during Research Preview:

- **Simple extractions** (like contact info from a single page) typically use fewer credits and cost less
- **Complex research tasks** (like competitive analysis across multiple domains) use more credits but reflect the total effort involved
- **Transparent usage** shows you exactly how many credits each request consumed
- **Credit conversion** automatically converts agent credit usage to credits for easy billing

### Parallel Agents Pricing

If you are running multiple agents in parallel with Spark-1 Fast, pricing is a lot more predictable at 10 credits per cell.

### Getting started

**All users** receive **5 free daily runs**, which can be used from either the playground or the API, to explore Agent’s capabilities without any cost. Additional usage is billed based on credit consumption and converted to credits.

### Managing costs

Agent can be expensive, but there are some ways to decrease the cost:

- **Start with free runs**: Use your 5 daily free requests to understand pricing
- **Set a `maxCredits` parameter**: Limit your spending by setting a maximum number of credits you’re willing to spend. The dashboard caps this at 2,500 credits; to set a higher limit, use the `maxCredits` parameter directly via the API (note: values above 2,500 are always billed as paid requests)
- **Optimize prompts**: More specific prompts often use fewer credits
- **Monitor usage**: Track your consumption through the dashboard
- **Set expectations**: Complex multi-domain research will use more credits than simple single-page extractions

Try Agent now at [firecrawl.dev/app/agent](https://www.firecrawl.dev/app/agent) to see how credit usage scales with your specific use cases.

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.