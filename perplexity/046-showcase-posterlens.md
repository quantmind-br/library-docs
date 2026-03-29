---
title: PosterLens | Scientific Poster Scanner & Research Assistant
url: https://docs.perplexity.ai/docs/cookbook/showcase/posterlens.md
source: llms
fetched_at: 2026-02-04T07:22:36.422422218-03:00
rendered_js: false
word_count: 331
summary: This document introduces PosterLens, an iOS application that uses OCR and AI integration to enable interactive exploration and semantic search of scientific posters.
tags:
    - ios-app
    - ocr-processing
    - perplexity-api
    - scientific-research
    - semantic-search
    - swiftui
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# PosterLens | Scientific Poster Scanner & Research Assistant

> An iOS app that transforms static scientific posters into interactive insights using OCR and Perplexity's Sonar Pro API for semantic search and context

**PosterLens** is an iOS app that transforms static scientific posters into interactive, explorable insights using OCR and AI. Created for the Perplexity Hackathon 2025, it allows researchers, MSLs, and medical writers to scan posters and explore them interactively using natural language, extracting meaning and surfacing related studies instantly.

![PosterLens Screenshot](https://cdn.prod.website-files.com/66d49e8555a289120a81ec3e/68930ad938e072c05d1be0b9_PosterLens.png)

## Features

* **Scientific Poster Scanning** using device camera and Apple Vision OCR
* **Natural Language Q\&A** about poster content with AI-powered responses
* **Semantic Search Integration** using Perplexity Sonar Pro for related studies
* **Citation Validation** with PubMed E-utilities for academic accuracy
* **Auto-Generated Research Questions** and future research directions
* **On-Device Processing** for privacy and performance
* **Interactive Research Experience** transforming static content into dynamic insights

## Prerequisites

* iOS 17+ device with camera
* Xcode 15+ for development
* Apple Developer account for App Store distribution
* Perplexity API key (Sonar Pro)
* OpenAI API key (GPT-3.5)
* PubMed E-utilities access

## Installation

```bash  theme={null}
# Clone the repository
git clone https://github.com/nickjlamb/PosterLens.git
cd PosterLens

# Open in Xcode
open PosterLens.xcodeproj
```

## Configuration

Add your API keys to the project configuration:

```swift  theme={null}
// API Configuration
PERPLEXITY_API_KEY=your_sonar_pro_api_key
OPENAI_API_KEY=your_gpt_api_key
PUBMED_API_KEY=your_pubmed_api_key
```

## Usage

1. **Install from App Store**: Download PosterLens from the iOS App Store
2. **Scan Poster**: Point your camera at a scientific poster
3. **OCR Processing**: Apple Vision automatically extracts text content
4. **Ask Questions**: Use natural language to query the poster content
5. **Explore Related Research**: Discover semantically related studies via Sonar Pro
6. **Validate Citations**: Check academic references with PubMed integration

## Code Explanation

* **Frontend**: Native iOS app built with SwiftUI for modern UI/UX
* **OCR Processing**: Apple Vision framework for text extraction from images
* **AI Integration**: Perplexity Sonar Pro API for semantic search and context understanding
* **Natural Language**: GPT-3.5 for Q\&A and content interpretation
* **Academic Validation**: PubMed E-utilities for citation verification
* **On-Device Processing**: Local OCR and processing for privacy and performance
* **Research Enhancement**: Auto-generation of research questions and future directions

## Links

* [GitHub Repository](https://github.com/nickjlamb/PosterLens)
* [App Store](https://apps.apple.com/us/app/posterlens-research-scanner/id6745453368)