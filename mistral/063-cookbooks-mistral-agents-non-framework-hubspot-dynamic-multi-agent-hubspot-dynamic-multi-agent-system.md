---
title: HubSpot Dynamic Multi-Agent System with Magistral Reasoning - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-agents-non_framework-hubspot_dynamic_multi_agent-hubspot_dynamic_multi_agent_system
source: crawler
fetched_at: 2026-01-29T07:33:43.526397665-03:00
rendered_js: false
word_count: 739
summary: This document demonstrates how to build an intelligent multi-agent system using Mistral reasoning models to automate complex HubSpot CRM operations and data analysis via natural language. It explains the architecture of specialized agents that process business queries, perform data operations, and synthesize actionable insights.
tags:
    - mistral-ai
    - hubspot-api
    - multi-agent-systems
    - crm-automation
    - magistral-reasoning
    - llm-orchestration
category: tutorial
---

This cookbook demonstrates the power of Magistral reasoning model combined with HubSpot CRM integration to create an intelligent, multi-agent system that can understand complex business queries and execute sophisticated CRM operations automatically.  
The system transforms natural language business questions into actionable insights and automated CRM updates, showcasing how advanced AI reasoning can streamline sales operations and strategic decision-making.

![Sample Demo](https://docs.mistral.ai/cookbooks/mistral/agents/non_framework/hubspot_dynamic_multi_agent/assets/demo.gif)

## Problem Statement

### Traditional CRM Challenges

Modern sales and marketing teams face several critical challenges when working with CRM systems like HubSpot:

**Manual Data Analysis:** Teams spend hours manually analyzing deals, contacts, and companies to extract insights **Complex Query Processing:** Business stakeholders struggle to get answers to multi-faceted questions that require data from multiple CRM objects **Strategic Planning:** Market analysis and expansion planning requires combining CRM data with business intelligence in ways that aren't natively supported

### Sample Query

"Assign priorities to all deals based on deal value"

These queries require:

- Understanding business context
- Analyzing multiple data sources
- Applying business logic
- Generating actionable recommendations
- Sometimes updating CRM records automatically

## Solution Architecture

**Core Innovation:** Magistral Reasoning + HubSpot Integration + Multi-Agent Orchestration

Our solution combines **Mistral's Magistral reasoning model** with **HubSpot's comprehensive CRM API** through a sophisticated multi-agent system that can:

- **Understand** complex business queries using Magistral's advanced reasoning capabilities
- **Plan** multi-step execution strategies with dynamically created specialized agents
- **Execute** both data analysis and CRM updates through coordinated agent workflows
- **Synthesize** results into actionable business insights with strategic recommendations

### AgentOrchestrator

**Master coordinator** that manages the entire multi-agent workflow and HubSpot integration. Orchestrates the complete flow from query analysis through sub-agent execution to final synthesis, while managing agent lifecycle and data connectivity.

### LeadAgent

Powered by **Magistral reasoning model** with `<think>` pattern processing, the Lead Agent performs sophisticated query analysis to understand business intent, determine data requirements, and create detailed execution plans specifying which sub-agents to create dynamically.

### Dynamic Sub-Agents

Sub-agents are **created on-the-fly** based on specific query requirements - not pre-defined templates. Each agent is dynamically generated with specialized roles (e.g., priority\_calculator, market\_analyzer, deals\_updater), specific tasks, and targeted data access patterns using **Mistral Small** for fast execution.

### HubSpot API Connector

Dedicated connector providing comprehensive access to CRM data and operations:

- **Property Discovery:** Automatically maps all available HubSpot fields and valid values
- **Data Fetching:** Retrieves deals, contacts, and companies with full property sets
- **Batch Updates:** Efficiently updates multiple records in batches of 100

### SynthesisAgent

**Final orchestrator** that combines all sub-agent results into coherent, actionable business insights using **Mistral Small**. Transforms technical agent outputs into user-friendly responses with strategic recommendations and next steps.

![Solution Architecture](https://docs.mistral.ai/cookbooks/mistral/agents/non_framework/hubspot_dynamic_multi_agent/assets/solution_architecture.png)

#### Installation

We need `hubspot-api-client` and `mistralai` packages for the demonstration.

#### Imports

#### Setup API Keys

#### Setup MistralAI Client

#### HubSpot API connector

- `get_data`: Fetches CRM data from HubSpot API, Retrieves deals, contacts, and companies data for the analysis.
- `batch_update`: Performs batch updates to HubSpot records, the updates and writes them back to HubSpot in efficient batches of 100 records.
- `get_properties`: Automatically fetches and formats all HubSpot deal, contact, and company properties, including valid values and dropdown options, so agents can update data reliably without errors.

#### Magistral (reasoning) and Mistral small LLM functions

- `magistral_reasoning`: Uses Magistral reasoning model for complex query analysis and execution planning with thinking process.
- `mistral_small_execution`: Uses Mistral Small model for sub-agent task execution.

#### LeadAgent

**Powered by Magistral reasoning model** for sophisticated query analysis and execution planning

- `analyze_query`: Uses Magistral's `<think>` pattern to understand business intent, determine data requirements, and create detailed execution plans with dynamic sub-agent specifications
- Determines whether queries require read-only analysis or write-back operations to HubSpot

#### SubAgent

**Dynamic agents created on-the-fly** based on query complexity and requirements

- `execute`: Uses Mistral Small for fast task execution including data analysis, business logic application, and CRM updates
- Specialized roles generated automatically (e.g., priority\_calculator, market\_analyzer, deals\_updater)
- Handles both read-only operations and write-back operations with proper HubSpot property validation

#### SynthesisAgent

**Final orchestrator** that combines all sub-agent results into coherent business insights

- `synthesize`: Uses Mistral Small to create user-friendly responses with actionable recommendations and next steps
- Transforms technical agent outputs into executive-ready summaries and strategic guidance

#### AgentOrchestrator

**Master coordinator** that manages the entire multi-agent workflow and HubSpot integration

- `process_query`: Orchestrates the complete flow from query analysis through sub-agent execution to final synthesis
- Manages agent lifecycle, data flow between agents, and HubSpot connectivity
- Provides rich logging and monitoring of the multi-agent process

#### Initialize the multi-agent system

#### Test Queries

##### Query-1

##### HubSpot status before updation

![HubSpot Status Before Updation](https://docs.mistral.ai/cookbooks/mistral/agents/non_framework/hubspot_dynamic_multi_agent/assets/hubspot_status_before_updation.png)

##### HubSpot status after updation

![HubSpot Status After Updation](https://docs.mistral.ai/cookbooks/mistral/agents/non_framework/hubspot_dynamic_multi_agent/assets/hubspot_status_after_updation.png)

##### Dynamically Created Agents

##### Answer

##### Query-2

##### Dynamically Created Agents

##### Answer