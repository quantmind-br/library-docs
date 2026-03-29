---
title: Multi-Agent Orchestration for Data Analysis & Simulation Scenarios - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-multi_agents_data_analysis-readme
source: crawler
fetched_at: 2026-01-29T07:33:44.806923502-03:00
rendered_js: false
word_count: 261
summary: This document provides instructions for setting up and using a multi-agent data analysis platform that uses Mistral AI and Chainlit to perform natural language queries and scenario simulations.
tags:
    - mistral-ai
    - multi-agent-systems
    - data-analysis
    - chainlit
    - sql-generation
    - simulation
    - python
category: guide
---

[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-multi_agents_data_analysis-readme)

A sophisticated data analysis and simulation platform using a multi-agent workflow powered by Chainlit and Mistral AI. This application enables users to perform complex data queries and run what-if scenario simulations through natural language interactions.

### Current Status

![Current Status](https://docs.mistral.ai/cookbooks/mistral/agents/agents_api/multi_agents_data_analysis/public/assets/current_status.jpg)

### Desired Status

![Desired Status](https://docs.mistral.ai/cookbooks/mistral/agents/agents_api/multi_agents_data_analysis/public/assets/desired_status.jpg)

## 🚀 Features

- **Natural Language Querying**: Ask data questions in plain English
- **Automatic SQL Generation**: AI converts questions to SQL queries
- **Scenario Simulation**: Run what-if analyses on your data
- **Visualization**: Automatic chart generation for results
- **Multi-Agent Architecture**: Specialized agents for different tasks
- **Interactive UI**: User-friendly Chainlit interface

## 📋 Table of Contents

- [Installation](https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-multi_agents_data_analysis-readme)
- [Usage](https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-multi_agents_data_analysis-readme)
- [Demos](https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-multi_agents_data_analysis-readme)
- [Architecture](https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-multi_agents_data_analysis-readme)
- [Roadmap](https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-multi_agents_data_analysis-readme)

## 🛠️ Installation

### Prerequisites

- Python 3.11+
- [UV](https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-multi_agents_data_analysis-readme) for package management (recommended)
- Mistral API key

### Steps

1. **Clone the repository**:
2. **Set up environment variables**:
   
   - Copy `.env.example` to `.env`
   - Add your Mistral API key to `.env`
3. **Create and activate virtual environment**:
   
   ```
   uv venv
   source .venv/bin/activate  # Linux/macOS# .\.venv\Scripts\activate  # Windows
   ```
   
   ```
   uv venv
   source .venv/bin/activate  # Linux/macOS# .\.venv\Scripts\activate  # Windows
   ```
4. **Install dependencies**:
5. **Run the application**:
   
   ```
   uv run -- chainlit run app.py
   ```
   
   ```
   uv run -- chainlit run app.py
   ```

## 🎛️ Usage

### Starting the Application

1. Run the Chainlit app as shown above
2. Open the provided URL in your browser
3. Use the starter questions or ask your own

### Example Queries

- "Show total estimated revenue across all accounts in January 2025"
- "List the top 5 account names by available balance"
- "What if we raise deposit rates by 0.5%?"

### Workflow Visualization

Type "Show workflow" to see the system architecture diagram.

## 📊 Demos

[Demo Script](https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-multi_agents_data_analysis-public-scripts-script)

### Data Analysis

![](https://docs.mistral.ai/cookbooks/mistral/agents/agents_api/multi_agents_data_analysis/public/assets/multi_agent_1.gif)

### Scenario Simulation

![](https://docs.mistral.ai/cookbooks/mistral/agents/agents_api/multi_agents_data_analysis/public/assets/multi_agent_2.png)

## 🏛️ Architecture

The system uses a multi-agent approach:

1. **Router Agent**: Determines query intent
2. **Analysis Agent**: Handles data queries
3. **Simulation Agent**: Runs what-if scenarios
4. **Report Agent**: Generates visualizations

```
graph TD;    A[User]--> B[Router Agent];    B -->|Data Query| C[Analysis Agent];    B -->|Simulation| D[Simulation Agent];    C --> E[Database];    D --> E;    C --> F[Report Agent];    D --> F;    F --> A;
```

```
graph TD;    A[User]--> B[Router Agent];    B -->|Data Query| C[Analysis Agent];    B -->|Simulation| D[Simulation Agent];    C --> E[Database];    D --> E;    C --> F[Report Agent];    D --> F;    F --> A;
```

## 🗺️ Roadmap

- Add voice input support
- Implement more advanced simulation models
- Add user authentication
- Support additional data sources