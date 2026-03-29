---
title: Ellipsis | One-Click Podcast Generation Agent
url: https://docs.perplexity.ai/docs/cookbook/showcase/Ellipsis.md
source: llms
fetched_at: 2026-02-04T07:21:34.467651899-03:00
rendered_js: false
word_count: 307
summary: This document provides an overview and setup instructions for Ellipsis, an AI-powered agent designed for automated multi-speaker podcast generation. It includes details on installation, environment configuration, and running the system's backend and frontend components.
tags:
    - podcast-generation
    - ai-agent
    - text-to-speech
    - python
    - react
    - content-automation
    - perplexity-api
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Ellipsis | One-Click Podcast Generation Agent

> A next-gen podcast generation agent that brings human-like, high-quality audio content to life on any topic with just one click

**Ellipsis** is a next-generation podcast generation agent that brings human-like, high-quality audio content to life on any topic with just one click. Whether it's breaking news, deep-dive tech explainers, movie reviews, or post-match sports breakdowns, Ellipsis crafts intelligent podcast episodes that sound like they were created by seasoned hosts in a professional studio.

## Features

* **Intelligent Multi-Speaker Dialogue** with multiple distinct voices and personalities
* **Comprehensive Topic Coverage** from LLM architectures to lunar eclipses
* **Custom Evaluation Engine** ensuring factual accuracy, legal compliance, and conversational quality
* **Fully Automated Podcast Generation** with human-like, podcast-ready audio output
* **Real-time Streaming Updates** via Server-Sent Events (SSE)
* **Podbean Integration** for direct podcast publishing
* **Trending Topics Detection** using Perplexity API

## Prerequisites

* Node.js v16+ and npm/yarn
* Python 3.10+ and pip
* Redis server running (default on port 6380)
* Perplexity API key, Podbean credentials

## Installation

```bash  theme={null}
# Clone the repository
git clone https://github.com/dineshkannan010/Ellipsis.git
cd Ellipsis

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate    # macOS/Linux
pip install -r requirements.txt

# Install native packages
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
pip install git+https://github.com/freddyaboulton/orpheus-cpp.git
pip install huggingface_hub[hf_xet] hf_xet

# Frontend setup
cd ../frontend
npm install
```

## Configuration

Create `backend/.env`:

```ini  theme={null}
REDIS_URL=redis://your-redis-host:6379
PERPLEXITY_API_KEY=your_key_here
PODBEAN_CLIENT_ID=...
PODBEAN_CLIENT_SECRET=...
```

Create `frontend/.env`:

```ini  theme={null}
REACT_APP_API_URL=http://your-backend-host:5000
```

## Usage

1. **Start Redis Server**:
   ```bash  theme={null}
   redis-server --port 6380
   ```

2. **Launch Backend**:
   ```bash  theme={null}
   cd backend
   python app.py
   ```

3. **Launch Frontend**:
   ```bash  theme={null}
   cd frontend
   npm run dev
   ```

4. **Optional: Podbean Integration**:
   ```bash  theme={null}
   cd backend/integrations/podbean_mcp
   pip install -e .
   python server.py
   python client.py server.py
   ```

5. **Generate Content**: Enter a topic in the homepage textbox and hit Enter. Switch to `ContentGenerationView` to see live script & audio progress.

## Code Explanation

* **Backend**: Python Flask with Redis pub/sub, llama.cpp, and Orpheus TTS for audio generation
* **Frontend**: React with Vite, Tailwind CSS, and Server-Sent Events for real-time updates
* **AI Integration**: Perplexity API for content generation and trending topics detection
* **Audio Processing**: Multi-speaker TTS with distinct voice personalities
* **Content Evaluation**: Built-in pipelines for factual accuracy and legal compliance
* **Podcast Publishing**: Direct integration with Podbean via MCP server

## Demo Video

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/XUPsSuCBTFw" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Links

* [GitHub Repository](https://github.com/dineshkannan010/Ellipsis)
* [Devpost Submission](https://devpost.com/software/ellipsis)