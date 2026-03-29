---
title: Multi-Agent Earnings Call Analysis System (MAECAS) - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-agents-non_framework-earnings_calls-multi_agent_earnings_call_analysis_system_(maecas)
source: crawler
fetched_at: 2026-01-29T07:33:48.373085428-03:00
rendered_js: false
word_count: 1299
---

Companies earnings calls provide critical insights into a company's performance, strategy, and future outlook. However, these transcripts are lengthy, dense, and cover diverse topics - making it challenging to extract targeted insights efficiently.

## The Problem

Quarterly earnings calls provide critical insights into company performance, strategies, and outlook, but extracting meaningful analysis presents significant challenges:

- Earnings call transcripts are lengthy and dense, often spanning 20+ pages of complex financial discussions Key insights are scattered throughout the text without clear organization.
- Different stakeholders need different types of information (financial metrics, strategic initiatives, risk factors).
- Cross-quarter analysis requires manually tracking evolving narratives across multiple calls.
- Traditional manual analysis is time-consuming, inconsistent, and prone to missing important details.

## Why This Matters

For investors, analysts, and business leaders, comprehensive earnings call analysis delivers significant value:

- Time Efficiency: Reduce analysis time from days to minutes
- Decision Support: Provide structured insights for investment and strategic decisions
- Comprehensive Coverage: Ensure no important insights are missed
- Consistent Analysis: Apply the same analytical rigor to every transcript
- Trend Detection: Identify patterns across quarters that might otherwise go unnoticed

## Our Solution

The Earnings Call Analysis Orchestrator transforms how earnings calls are processed through a multi-agent workflow that:

1. Extracts insights from quarterly transcripts using specialized analysis agents
2. Delivers both comprehensive reports and targeted query responses
3. Identifies trends and patterns across quarters
4. Maintains a structured knowledge base of earnings insights

## Specialized Analysis Agents

Our system employs specialized agents working in coordination to deliver comprehensive analysis:

**Financial Agent:** Extracts revenue figures, profit margins, growth metrics, and other quantifiable performance indicators.

**Strategic Agent:** Identifies product roadmaps, market expansions, partnerships, and long-term vision initiatives.

**Sentiment Agent:** Evaluates management's confidence, tone, and enthusiasm across different business segments.

**Risk Agent:** Detects supply chain, market, regulatory challenges, and assesses their severity and mitigation plans.

**Competitor Agent:** Tracks competitive positioning, market share discussions, and differentiation strategies.

**Temporal Agent:** Analyzes trends across quarters to identify business trajectory and evolving priorities.

## Workflow Orchestration

The orchestrator serves as the central coordinator that:

- Efficiently processes and caches transcript text using advanced OCR
- Activates specialized agents based on analysis needs Stores structured insights in a centralized knowledge base
- Generates comprehensive reports with executive summaries, sectional analyses, and outlook
- Answers specific queries by leveraging relevant insights across quarters

## Dataset

For demonstration purposes, we use NVIDIA's quarterly earnings call transcripts from 2025:

- Q1 2025 Earnings Call Transcript
- Q2 2025 Earnings Call Transcript
- Q3 2025 Earnings Call Transcript
- Q4 2025 Earnings Call Transcript

These transcripts contain discussions of financial results, strategic initiatives, market conditions, and forward-looking statements by NVIDIA's management team and their interactions with financial analysts.

## Mistral AI Models

For our implementation, we use Mistral AI's LLMs:

`mistral-small-latest`: Used for general analysis and response generation.

`mistral-large-latest`: Used for structured output generation.

`mistral-ocr-latest`: Used for PDF transcript extraction and processing.

This modular approach enables both in-depth report generation and targeted question answering while maintaining efficiency through selective agent activation and insights reuse.

## Solution Architecture

![Solution Architecture](https://docs.mistral.ai/cookbooks/mistral/agents/non_framework/earnings_calls/solution_architecture.png)

### Installation

We need `mistralai` for LLM usage.

## Imports

### Setup API Keys

Here we setup MistralAI API key.

### Initialize Mistral client

Here we initialise Mistral client.

### Download Data

We will use NVIDIA's quarterly earnings call transcripts from 2025:

- Q1 2025 Earnings Call Transcript
- Q2 2025 Earnings Call Transcript
- Q3 2025 Earnings Call Transcript
- Q4 2025 Earnings Call Transcript

These transcripts contain discussions of financial results, strategic initiatives, market conditions, and forward-looking statements by NVIDIA's management team and their interactions with financial analysts.

### Initiate Models

1. DEFAULT\_MODEL - For General Analysis
2. STRUCTURED\_MODEL - For Structured Outputs
3. OCR\_MODEL - For parsing the earnings call document.

### Data Models

The solution uses specialized Pydantic models to structure and extract insights:

#### Core Analysis Models

- **FinancialInsight**: Captures metrics, values, and confidence scores for financial performance
- **StrategicInsight**: Represents initiatives, descriptions, timeframes, and importance ratings
- **SentimentInsight**: Tracks topic sentiment, evidence, and speaker attributions
- **RiskInsight**: Documents risks, impacts, mitigations, and severity scores
- **CompetitorInsight**: Records market segments, positioning, and competitive dynamics
- **TemporalInsight**: Identifies trends, patterns, and supporting evidence across quarters

#### Workflow Models

- **QueryAnalysis**: Determines required quarters, agent types, and analysis dimensions from user queries
- **ReportSection**: Structures report content with title, body, and optional subsections

#### Response Wrappers

- Each analysis model has a corresponding response wrapper (e.g., FinancialInsightsResponse) that packages insights into structured formats compatible with the Mistral API parsing capabilities

The models use Python's Literal types for categorized fields (such as sentiment levels or trend types) to enforce strict validation and ensure consistent terminology, enabling reliable cross-quarter comparisons while providing consistent knowledge extraction, storage, and retrieval across multiple analysis dimensions for both comprehensive reports and targeted queries.

#### Financial Insight

#### Strategic Insight

#### Sentiment Insight

#### Risk Insight

#### Competitor Insight

#### Temporal Insight

#### Query Analysis

#### Report Section

### PDF Parser

Our PDF parser uses Mistral's OCR capabilities to extract high-quality text from earnings call transcripts while implementing a file-based caching system to improve performance. This approach enables accurate text extraction with minimal processing overhead for repeated analyses.

### Insights Storage

The system includes a centralized InsightsStore component that:

- Maintains a persistent JSON database of all extracted insights
- Organizes insights by type (financial, strategic, etc.) and quarter
- Provides efficient retrieval for both report generation and query answering
- Eliminates redundant processing by caching analysis results

### Specialised Agents

Our analysis relies on five domain-focused agents, each extracting specific insights:

**Financial Agent** - Analyzes metrics, revenue figures, margins, and growth rates.

**Strategic Agent** - Identifies product roadmaps, market expansions, and R&D investments.

**Sentiment Agent** - Evaluates management tone, confidence levels, and enthusiasm across topics.

**Risk Agent** - Detects challenges, uncertainties, and potential threats with severity ratings.

**Competitor Agent** - Tracks competitive positioning, market share discussions, and differentiation strategies.

Each agent processes transcripts through specialized prompts, producing structured insights that feed into the overall analysis.

#### `Agent` base class for specialised agents

#### Financial Agent

#### Strategic Agent.

#### Sentiment Agent

#### Risk Agent

#### Competitor Agent

#### Temporal Analysis Agent

### Query Processor

The Query Processor analyzes user questions to determine the specific components needed:

- Interprets the queries about NVIDIA's earnings calls
- Identifies which quarters (Q1-Q4) are relevant to the question
- Determines which agent types should be activated based on query content
- Decides whether temporal analysis across quarters is required
- Provides a clear interpretation of the user's intent

This component ensures the workflow activates only the necessary analysis paths, improving efficiency while maintaining comprehensive answers.

### Orchestration Layer

The **EarningsCallAnalysisOrchestrator** coordinates the entire analysis workflow with key functions:

- **process\_transcript()**: Analyzes a quarterly transcript with all specialized agents
- **generate\_comprehensive\_report()**: Creates detailed reports across selected quarters
- **answer\_query()**: Provides targeted responses to specific earnings call questions
- **\_generate\_report\_sections()**: Produces structured sections (financial, strategic, etc.)
- **\_generate\_query\_response()**: Crafts focused answers from relevant insights
- **\_compile\_report()**: Assembles all sections into a cohesive markdown document

This orchestration ensures efficient resource utilization while delivering both in-depth analysis reports and precise query responses.

### Initialize the system for NVIDIA 2025 earnings calls

### Process All Quarterly Transcripts

We process all quarterly transcripts and generate different insights at once, making both report generation and query answering more efficient.

### Report Generation

We generate comprehensive report by organizing insights across quarters into structured sections including executive summary, financial analysis, strategic initiatives, market positioning, risk assessment, and future outlook.

### Query Answering

Our system analyzes user questions to determine relevant quarters, agent types, and analysis dimensions, then provides targeted responses using only the most applicable insights.

#### Query-1

Query - What were NVIDIA's key financial metrics in Q1 and Q2 2025?

Agents Used - Financial Agent

Quarters - Q1, Q2

Temporal Analysis Required - False

Financial Year - 2025

#### Query-2

Query - Identify strategic shifts in NVIDIA's automotive business across 2025

Agents Used - Strategic Agent

Quarters - Q1, Q2, Q3, Q4

Temporal Analysis Required - True

Financial Year - 2025

#### Query-3

Query - What risks did NVIDIA highlight in their Q4 earnings call, and how do they compare to those mentioned in Q3?

Agents Used - Risk Agent

Quarters - Q3, Q4

Temporal Analysis Required - True

Financial Year - 2025