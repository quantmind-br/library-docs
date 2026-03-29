---
title: PRD Generator & Linear Ticket Creator with MistralAI Agents API and MCP - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-prd_linear_ticket-readme
source: crawler
fetched_at: 2026-01-29T07:33:46.801844408-03:00
rendered_js: false
word_count: 165
summary: A technical tutorial demonstrating how to build an automated PRD generator and Linear ticket creator using the Mistral AI Agents API and Model Context Protocol (MCP).
tags:
    - Mistral AI
    - Agents API
    - MCP
    - Linear
    - AI Agents
    - Automation
category: guide
---

Application that generates Product Requirements Documents (PDF) from transcript PDFs and creates Linear tickets using MistralAI Agents API with MCP servers.

[![Linear Ticket](https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/gif/Linear_tickets.gif)](https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-prd_linear_ticket-readme)

## Use Case

- Extract text from PDF transcripts using OCR
- Generate comprehensive PRDs from meeting transcripts
- Parse PRDs into structured features
- Create Linear tickets automatically for each feature

## Architecture

### Main Application

- **app.py**: Chainlit interface with MistralAI agent integration

### MCP Servers

- **stdio\_prd\_generator\_server.py**: PDF OCR processing and PRD generation using MistralAI LLMs
- **stdio\_linear\_ticket\_gen\_server.py**: PRD parsing and Linear ticket creation via GraphQL API

## Installation

## Environment Setup

Set your MistralAI API key:

Set your Mistral API key in both the servers:

- `mcp_servers/stdio_linear_ticket_gen_server.py`
- `mcp_servers/stdio_prd_generator_server`

Configure Linear API credentials in `mcp_servers/stdio_linear_ticket_gen_server.py`:

- Update `linear_api_key` with your Linear API key
- Update `team_id` with your Linear team ID

## Usage

Run the application:

Ask questions like:

- "Generate a PRD from transcript.pdf"
- "Generate a PRD outlining LeChat improvements based on the transcript in transcript.pdf, and create corresponding Linear tickets."

The app will automatically extract text from PDFs, generate PRDs, and create corresponding Linear tickets.