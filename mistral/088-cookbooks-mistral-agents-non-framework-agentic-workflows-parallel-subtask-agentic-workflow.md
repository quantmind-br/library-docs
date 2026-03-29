---
title: Parallel Subtask Agent Workflow - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-agents-non_framework-agentic_workflows-parallel_subtask_agentic_workflow
source: crawler
fetched_at: 2026-01-29T07:33:44.972329203-03:00
rendered_js: false
word_count: 514
summary: This document explains how to build an agentic workflow that uses an orchestrator LLM to decompose complex tasks into parallel subtasks executed by specialized workers with real-time search capabilities.
tags:
    - agentic-workflows
    - mistral-ai
    - tavily-api
    - parallel-processing
    - task-decomposition
    - llm-orchestration
    - pydantic
category: tutorial
---

## Introduction

This notebook demonstrates how to create a generic agent workflow that automatically breaks complex tasks into multiple subtasks.

These subtasks are completed using parallel MistralAI LLM calls, enhanced with real-time information from Tavily API.

The results are then synthesized into a comprehensive response.

## Workflow Overview

1. An orchestrator LLM analyzes the main task and breaks it into distinct, parallel subtasks
2. Each subtask is assigned to a worker LLM with specialized instructions
3. Workers execute in parallel, using Tavily API for up-to-date information as needed
4. Results are synthesized into a unified response

**NOTE**: We will use MistralAI’s LLM for subtask handling and response synthesis, and the Tavily API to retrieve up-to-date real.

## Solution Architecture

![solution architecture](https://docs.mistral.ai/cookbooks/mistral/agents/non_framework/agentic_workflows/images/parallel_subtask_agentic_workflow.png)

### Installation

### Imports

### Set your API keys

Here we set the API keys for `MistralAI` and `Tavily`. You can obtain the keys from the following links:

1. MistralAI: [https://console.mistral.ai/api-keys](https://console.mistral.ai/api-keys)
2. Tavily: [https://app.tavily.com/home](https://app.tavily.com/home)

### Initialize Mistral client

### Tavily API configuration

### Pydantic Models for Structured Data

Pydantic models provide data validation and serialization, ensuring the data we receive from LLMs matches our expected structure. This helps maintain consistency between the orchestrator and worker components.

**SubTask:** Individual subtask definition - defines a discrete unit of work with its type, description, and optional search query.

**TaskList:** Output structure from the orchestrator - contains analysis and a list of defined subtasks to be executed in parallel.

### API Utility Functions

API Utility functions handle communication with external APIs and process the responses, providing clean interfaces for the rest of the workflow.

**fetch\_information:** Retrieves relevant information from Tavily API based on a query and returns structured results.

**run\_mistral\_llm:** Executes a standard call to Mistral AI with given prompts, returning the generated content.

**parse\_structured\_output:** Uses Mistral's structured output capability to generate and parse responses according to Pydantic models.

### Async Worker Functions

These functions enable parallel execution of subtasks, allowing the workflow to process multiple components simultaneously for greater efficiency.

**run\_task\_async:** Executes a single subtask asynchronously, enhancing it with relevant information from Tavily when needed.

**execute\_tasks\_in\_parallel:** Manages the parallel execution of all subtasks, ensuring they run concurrently and their results are properly collected.

## Main Workflow Function

The primary orchestration function that coordinates the entire parallel subtask process from initial request to final synthesized response.

**parallel\_subtask\_workflow:** Manages the complete workflow by orchestrating task decomposition, parallel execution of subtasks, and final synthesis of results into a comprehensive response.

Steps:

1. **Task Analysis:** The orchestrator analyzes the user's query and breaks it into distinct subtasks
2. **Subtask Definition:** Each subtask is defined with a unique ID, type, description, and search query
3. **Parallel Execution:** Subtasks are executed concurrently by worker agents Information Enhancement: Workers retrieve relevant information from Tavily when needed
4. **Result Collection:** Outputs from all workers are gathered
5. **Synthesis:** Individual results are combined into a comprehensive final response
6. **Final Response:** Complete workflow results are returned, including both individual analyses and the synthesized answer

### Run workflow with an example task

Here we run the worklow with a sample example task comparing mobile phones recommendation

### Final Response

### Examining Orchestrator Analysis, Subtask information and responses

We can examine the Orchestrator Analysis, subtasks created, the corresponding search queries, and the individual responses.