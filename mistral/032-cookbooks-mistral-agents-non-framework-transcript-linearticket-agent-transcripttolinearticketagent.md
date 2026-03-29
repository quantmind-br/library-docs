---
title: 'Call Transcript-to-PRD-to-Ticket Agent: Converting Meeting Transcripts to Linear Tickets using Mistral AI LLMs - Mistral AI Cookbook'
url: https://docs.mistral.ai/cookbooks/mistral-agents-non_framework-transcript_linearticket_agent-transcripttolinearticketagent
source: crawler
fetched_at: 2026-01-29T07:33:45.62539742-03:00
rendered_js: false
word_count: 530
summary: This document outlines an automated pipeline that leverages Mistral AI and OCR to transform meeting transcripts into structured Product Requirements Documents (PRDs) and actionable Linear development tickets.
tags:
    - mistral-ai
    - ocr
    - workflow-automation
    - linear-api
    - llm-agents
    - prd-generation
category: tutorial
---

## Problem Statement

In modern software development, a significant challenge is efficiently converting customer calls and meetings into actionable development tickets. This process typically involves:

- Manual note-taking during calls
- Converting notes into Product Requirements Documents (PRDs)
- Breaking down PRDs into actionable tickets
- Creating and managing tickets in project management tools (ex:- Linear)

This manual process is:

- Time-consuming
- Prone to information loss
- Subject to inconsistencies
- Difficult to scale

## Our Solution

We've created an automated pipeline that leverages Mistral's LLM and OCR models to streamline this process:

### Stage 1: PRD Generation

- Takes raw call transcripts as input (parsed using Mistral OCR)
- Uses Mistral AI LLM to generate structured PRD
- Implements iterative refinement for accuracy
- Ensures alignment with original discussion (from transcript)

<!--THE END-->

- Analyzes PRD to identify distinct features
- Extracts technical requirements
- Captures constraints and success metrics
- Maintains traceability to original content(call/ transcript)

## Mistral LLM Integration

The solution uses several Mistral AI LLM capabilities:

1. **Chat Completion API**
   
   - Used for PRD generation
   - Handles iterative refinement
   - Processes feedback and improvements
2. **Structured Output**
   
   - Formats PRD content
   - Extracts feature lists
   - Generates ticket descriptions
3. **Context Management**
   
   - Maintains consistency across iterations
   - Preserves original transcript context
   - Ensures accurate information flow

This notebook walks through the implementation of this pipeline, demonstrating how to automate the journey from call transcripts to PRD creation to actionable development tickets on Linear.

![Solution Architecture](https://raw.githubusercontent.com/mistralai/cookbook/main/mistral/agents/non_framework/transcript_linearticket_agent/solution_architecture.png)

### Installation

### Imports

### Download Call Transcript

For this demonstration we will use a product call regarding LeChat.

*Note*: The trascript is synthetically generated just for the demonstration purposes.

### Configuration and Setup

Our pipeline integrates Mistral AI LLM for PRD generation and Linear for ticket management. Let's set up the required configurations:

## API Setup

1. **Linear Configuration**
   
   - Get API key from Linear (Settings → API)
   - Get your Team ID
   - GraphQL endpoint: [https://api.linear.app/graphql](https://api.linear.app/graphql)
2. **Mistral AI Configuration**
   
   - Get API key from Mistral AI
   - We use "mistral-large-latest" model

### Data Models

We also define our data structures for Features and descriptions that we create on Linear based on PRD.

### PRD Generation Agent

The PRD Generation Agent (`PRDAgent`) is responsible for converting call transcripts into accurate PRDs through an iterative process:

1. First creates initial PRD (`generate_initial_prd`)
2. Then gets feedback (`get_feedback`)
3. Refines based on feedback (`refine_prd`)
4. Repeats until quality is satisfactory (max 3 times) (`run`)

### Ticket Creation Agent

The Ticket Creation Agent converts PRDs into actionable tickets on Linear through three main steps:

1. Parses PRD into structured features and descriptions (`parse_prd`)
2. Converts each feature into a ticket format (`create_ticket`)
3. Creates tickets in Linear via GraphQL API (`create_tickets_from_prd`)

### Workflow Orchestrator

The Workflow Orchestrator:

- Coordinates the entire process
- Manages communication between agents
- Handles the overall workflow

### Parse The Call Transcript

We will use Mistral OCR model to parse the downloaded call transcript file.

### Running the Pipeline

Let's test the pipeline with a sample transcript that discusses about LeChat product call.

### Understanding the Output

The pipeline produces:

1. A structured PRD
2. List of features and descriptions
3. Linear tickets with URLs

#### PRD

#### Features

#### Linear Tickets Created

#### Here is a sample image showing how the tickets will be created in the Linear UI. (The tickets will vary based on the transcript.)

![LinearTicket](https://raw.githubusercontent.com/mistralai/cookbook/main/mistral/agents/non_framework/transcript_linearticket_agent/linear_tickets.png)

### Next Steps

You can extend this pipeline by:

1. Adding priority levels to tickets.
2. Including custom fields in Linear tickets.
3. Incorporate similar pipeline with Jira.