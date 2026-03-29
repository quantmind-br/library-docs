---
title: TruthTracer | AI-Powered Misinformation Detection Platform
url: https://docs.perplexity.ai/docs/cookbook/showcase/truth-tracer.md
source: llms
fetched_at: 2026-02-04T07:22:44.514976948-03:00
rendered_js: false
word_count: 369
summary: This guide explains how to set up and use TruthTracer, a misinformation detection platform that leverages various Perplexity Sonar models for claim verification and logical analysis.
tags:
    - misinformation-detection
    - perplexity-api
    - sonar-models
    - fact-checking
    - nestjs
    - react-app
    - ai-platform
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# TruthTracer | AI-Powered Misinformation Detection Platform

> A comprehensive misinformation detection platform that uses Perplexity's Sonar API to analyze claims, trace trust chains, and provide Socratic reasoning for fact verification

**TruthTracer** is a comprehensive misinformation detection platform that leverages Perplexity's Sonar API to provide multi-layered claim analysis. The platform combines fact-checking, trust chain tracing, and Socratic reasoning to deliver accurate, evidence-based verification results with confidence scores and detailed sourcing.

### Demo

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/twXeyK5ajyE" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Features

* **Multi-method Analysis** combining fact-checking, trust chain analysis, and Socratic reasoning
* **AI-Powered Verification** using Perplexity's Sonar, Sonar Deep Research, and Sonar Reasoning Pro  models
* **Real-time Processing** with parallel execution of multiple analysis methods
* **Evidence-based Results** providing sources, confidence scores, and detailed reasoning
* **Clean Architecture** with NestJS backend and React frontend
* **Production-Ready** with Docker deployment, comprehensive testing, and API documentation
* **Configurable Confidence Scoring** with customizable weights and thresholds

## Prerequisites

* Node.js 18+ and npm
* Perplexity API key (Sonar models access)
* Docker (optional for deployment)
* Git for repository cloning

## Installation

```bash  theme={null}
# Clone the backend repository
git clone https://github.com/anthony-okoye/truth-tracer-backend.git
cd truth-tracer-backend

# Install dependencies
npm install

# Clone the frontend repository
git clone https://github.com/anthony-okoye/truth-tracer-front.git
cd truth-tracer-front

# Install frontend dependencies
npm install
```

## Configuration

Create `.env` file in the backend directory:

```ini  theme={null}
# Required
SONAR_API_KEY=your_perplexity_api_key
SONAR_API_URL=https://api.perplexity.ai

# Optional configuration
SONAR_TIMEOUT=30000
SONAR_MAX_RETRIES=3
CONFIDENCE_WEIGHT_FACT_CHECK=0.35
CONFIDENCE_WEIGHT_TRUST_CHAIN=0.25
CONFIDENCE_WEIGHT_SOCRATIC=0.20
```

## Usage

1. **Start Backend**:

```bash  theme={null}
   cd truth-tracer-backend
   npm run start:dev
```

2. **Start Frontend**:

```bash  theme={null}
   cd truth-tracer-front
   npm start
```

3. **Access Application**: Open [http://localhost:3000](http://localhost:3000) in your browser

4. **Analyze Claims**:
   * Enter a claim in the text area
   * Click "Analyze Claim" to run fact-checking, trust chain analysis, and Socratic reasoning
   * View results with confidence scores, sources, and detailed explanations

## Code Explanation

* **Backend**: NestJS application with clean architecture following TypeScript best practices
* **AI Integration**: Perplexity Sonar API with three specialized models - Sonar for fact-checking, Sonar Deep Research for trust chain analysis, and Sonar Reasoning Pro for logical evaluation
* **Parallel Processing**: Simultaneous execution of all three analysis methods for efficient claim verification
* **Response Sanitization**: Custom JSON parsing and validation to handle various API response formats
* **Confidence Scoring**: Weighted scoring system combining results from all three analysis methods
* **Frontend**: React application with intuitive claim submission interface and detailed results visualization
* **Testing**: Comprehensive test suite including unit tests, end-to-end tests, and claim analysis testing

## How the Sonar API is Used

TruthTracer leverages Perplexity's Sonar API through three distinct analysis approaches:

```typescript  theme={null}
// Parallel execution of multiple Sonar models
const [factCheckResult, trustChainResult, socraticResult] = await Promise.all([
  sonarClient.chat.completions.create({
    model: "sonar",
    messages: [{ role: "user", content: factCheckPrompt }],
    max_tokens: 500
  }),
  sonarClient.chat.completions.create({
    model: "sonar-deep-research", 
    messages: [{ role: "user", content: trustChainPrompt }],
    max_tokens: 2500
  }),
  sonarClient.chat.completions.create({
    model: "sonar-reasoning",
    messages: [{ role: "user", content: socraticPrompt }],
    max_tokens: 4000
  })
]);
```

## Links

* [Live Demo](https://truthtracer.netlify.app/)
* [Backend Repository](https://github.com/anthony-okoye/truth-tracer-backend)
* [Frontend Repository](https://github.com/anthony-okoye/truth-tracer-front)