---
title: Valetudo AI | Trusted Medical Answer Assistant
url: https://docs.perplexity.ai/docs/cookbook/showcase/valetudo-ai.md
source: llms
fetched_at: 2026-02-04T07:22:52.060035896-03:00
rendered_js: false
word_count: 302
summary: Valetudo AI is a medical assistant application that leverages the Perplexity Sonar API to provide evidence-based health answers using curated domain filters, location-based searches, and image analysis.
tags:
    - medical-assistant
    - perplexity-api
    - sonar-pro
    - health-tech
    - image-analysis
    - search-filters
    - ai-implementation
category: other
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Valetudo AI | Trusted Medical Answer Assistant

> Sonar-powered medical assistant for fast, science-backed answers.

# Valetudo AI

**Valetudo AI** is a science-backed medical assistant powered by the Perplexity Sonar API. It provides fast, clear, and well-cited answers to health questions — helping users cut through misinformation with filters, image analysis, and ready-made prompt templates.

Designed for conscious users — like parents, patients, and medical students — seeking reliable information.

## Features

* **Cited Answers** — sourced from a curated list of 10 trusted medical domains
* **Smart Filters** — by date and country for localized, up-to-date insights
* **Image Upload** — analyze photos of medication, conditions, or packaging
* **Prompt Templates** — 7 categories for symptom checks, drug safety, research, and more
* **Simple UI** — built with React and Tailwind CSS

## How It Uses the Sonar API

Valetudo AI integrates with [Perplexity Sonar Pro](https://docs.perplexity.ai), leveraging advanced features for domain-specific search and rich responses:

| Feature          | API Field                         | Purpose                                           |
| ---------------- | --------------------------------- | ------------------------------------------------- |
| Context Control  | `search_context_size: medium`     | Balances speed and depth for focused medical Q\&A |
| Trusted Domains  | `search_domain_filter`            | Restricts results to vetted health sources        |
| Visual Input     | `image_url`                       | Enables image-based medical queries               |
| Freshness Filter | `search_after/before_date_filter` | Helps surface recent and relevant findings        |
| Local Relevance  | `user_location`                   | Tailors answers based on user’s region            |

## Links

* [GitHub Repository](https://github.com/vero-code/valetudo-ai)
* [Devpost Submission](https://devpost.com/software/valetudo-ai)
* [View All Screenshots](https://github.com/vero-code/valetudo-ai/tree/master/screenshots)

## Demo Video

See Valetudo AI in action:

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/AX3nOh9LbTc" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Screenshots

### Home Interface

![Home screen](https://raw.githubusercontent.com/vero-code/valetudo-ai/refs/heads/master/screenshots/1-home.png)

### Prompt Templates

![Prompt templates](https://raw.githubusercontent.com/vero-code/valetudo-ai/refs/heads/master/screenshots/10-prompts.png)

### Image Upload

![Image upload](https://raw.githubusercontent.com/vero-code/valetudo-ai/refs/heads/master/screenshots/8-image-upload.png)

### Date & Location Filters

![Date filter](https://raw.githubusercontent.com/vero-code/valetudo-ai/refs/heads/master/screenshots/7-date-filter.png)

![Location filter](https://raw.githubusercontent.com/vero-code/valetudo-ai/refs/heads/master/screenshots/9-location-filter.png)