---
title: FirstPrinciples | AI Learning Roadmap Generator
url: https://docs.perplexity.ai/docs/cookbook/showcase/first-principle.md
source: llms
fetched_at: 2026-02-04T07:21:55.111532476-03:00
rendered_js: false
word_count: 314
summary: This document introduces FirstPrinciples, an AI-powered application that uses conversational agents to generate personalized, structured learning roadmaps. It provides comprehensive instructions for installation, configuration, and usage across its React frontend and Flask backend.
tags:
    - ai-learning
    - roadmap-generator
    - openai-api
    - perplexity-api
    - flask
    - react
    - conversational-ai
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# FirstPrinciples | AI Learning Roadmap Generator

> An AI-powered learning roadmap generator that uses conversational AI to help users identify specific learning topics and provides personalized step-by-step learning plans

**FirstPrinciples App** is an AI-powered tool that transforms your broad learning goals into structured, personalized roadmaps. Through an interactive chat, the AI engages you in a conversation, asking targeted questions to refine your learning needs before generating a detailed plan. The application is built to help you learn more efficiently by providing a clear path forward.

<video controls className="w-full aspect-video rounded-xl" src="https://github.com/user-attachments/assets/6016c5dd-6c18-415e-b982-fafb56170b87" />

## Features

* **Interactive Chat Interface** for defining and refining learning goals through conversation
* **AI-Powered Topic Narrowing** with smart, targeted questions to specify learning objectives
* **Session Management** allowing multiple roadmap discussions and progress tracking
* **Visual Progress Indicators** showing when sufficient information has been gathered
* **Personalized Learning Plans** with structured, step-by-step roadmaps
* **Conversational AI Flow** combining OpenAI and Perplexity APIs for intelligent interactions

## Prerequisites

* Python 3.8+ and pip
* Node.js 16+ and npm
* OpenAI API key
* Perplexity API key

## Installation

```bash  theme={null}
# Clone the repository
git clone https://github.com/william-Dic/First-Principle.git
cd First-Principle

# Backend setup
cd flask-server
pip install -r requirements.txt

# Frontend setup
cd ../client
npm install
```

## Configuration

Create `.env` file in the `flask-server` directory:

```ini  theme={null}
OPENAI_API_KEY=your_openai_api_key
PPLX_API_KEY=your_perplexity_api_key
PERPLEXITY_API_KEY=your_perplexity_api_key
```

## Usage

1. **Start Backend**:
   ```bash  theme={null}
   cd flask-server
   python server.py
   ```
   Server runs on [http://localhost:5000](http://localhost:5000)

2. **Start Frontend**:
   ```bash  theme={null}
   cd client
   npm start
   ```
   Client runs on [http://localhost:3000](http://localhost:3000)

3. **Generate Roadmap**:
   * Open [http://localhost:3000](http://localhost:3000) in your browser
   * Describe what you want to learn in the chat interface
   * Answer AI follow-up questions to refine your learning goals
   * Receive a personalized, structured learning roadmap

## Code Explanation

* **Frontend**: React application with conversational chat interface and progress indicators
* **Backend**: Flask server managing API calls, session state, and conversation flow
* **AI Integration**: Combines OpenAI API for conversational flow and Perplexity API for intelligent topic analysis
* **Session Management**: Tracks conversation state and learning goal refinement
* **Roadmap Generation**: Creates structured, actionable learning plans based on user input
* **Conversational Flow**: Implements goal-oriented dialogue to narrow down learning objectives

## Links

* [GitHub Repository](https://github.com/william-Dic/First-Principle.git)
* [Demo Video](https://github.com/user-attachments/assets/6016c5dd-6c18-415e-b982-fafb56170b87)