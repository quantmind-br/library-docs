---
title: Examples Overview
url: https://docs.perplexity.ai/docs/cookbook/examples/README.md
source: llms
fetched_at: 2026-02-04T07:21:07.537747626-03:00
rendered_js: false
word_count: 478
summary: This document provides an overview of production-ready example applications demonstrating various use cases for the Perplexity Sonar API, including tools for fact-checking, financial tracking, and academic research.
tags:
    - perplexity-api
    - sonar-api
    - api-examples
    - llm-applications
    - python-scripts
    - fact-checking
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Examples Overview

> Ready-to-use applications demonstrating Perplexity Sonar API capabilities

# Examples Overview

Welcome to the **Perplexity Sonar API Examples** collection! These are production-ready applications that demonstrate real-world use cases of the Sonar API.

## 🚀 Quick Start

Navigate to any example directory and follow the instructions in the README.md file.

## 📋 Available Examples

### 🔍 [Fact Checker CLI](fact-checker-cli/)

**Purpose**: Verify claims and articles for factual accuracy\
**Type**: Command-line tool\
**Use Cases**: Journalism, research, content verification

**Key Features**:

* Structured claim analysis with ratings
* Source citation and evidence tracking
* JSON output for automation
* Professional fact-checking workflow

**Quick Start**:

```bash  theme={null}
cd fact-checker-cli/
python fact_checker.py --text "The Earth is flat"
```

***

### 🤖 [Daily Knowledge Bot](daily-knowledge-bot/)

**Purpose**: Automated daily fact delivery system\
**Type**: Scheduled Python application\
**Use Cases**: Education, newsletters, personal learning

**Key Features**:

* Topic rotation based on calendar
* Persistent storage of facts
* Configurable scheduling
* Educational content generation

**Quick Start**:

```bash  theme={null}
cd daily-knowledge-bot/
python daily_knowledge_bot.py
```

***

### 🏥 [Disease Information App](disease-qa/)

**Purpose**: Interactive medical information lookup\
**Type**: Web application (HTML/JavaScript)\
**Use Cases**: Health education, medical reference, patient information

**Key Features**:

* Interactive browser interface
* Structured medical knowledge cards
* Citation tracking for medical sources
* Standalone deployment ready

**Quick Start**:

```bash  theme={null}
cd disease-qa/
jupyter notebook disease_qa_tutorial.ipynb
```

***

### 📊 [Financial News Tracker](financial-news-tracker/)

**Purpose**: Real-time financial news monitoring and market analysis\
**Type**: Command-line tool\
**Use Cases**: Investment research, market monitoring, financial journalism

**Key Features**:

* Real-time financial news aggregation
* Market sentiment analysis (Bullish/Bearish/Neutral)
* Impact assessment and sector analysis
* Investment insights and recommendations

**Quick Start**:

```bash  theme={null}
cd financial-news-tracker/
python financial_news_tracker.py "tech stocks"
```

***

### 📚 [Academic Research Finder](research-finder/)

**Purpose**: Academic literature discovery and summarization\
**Type**: Command-line research tool\
**Use Cases**: Academic research, literature reviews, scholarly work

**Key Features**:

* Academic source prioritization
* Paper citation extraction with DOI links
* Research-focused prompting
* Scholarly workflow integration

**Quick Start**:

```bash  theme={null}
cd research-finder/
python research_finder.py "quantum computing advances"
```

## 🔑 API Key Setup

All examples require a Perplexity API key. You can set it up in several ways:

### Environment Variable (Recommended)

```bash  theme={null}
export PPLX_API_KEY="your-api-key-here"
```

### .env File

Create a `.env` file in the example directory:

```bash  theme={null}
PERPLEXITY_API_KEY=your-api-key-here
```

### Command Line Argument

```bash  theme={null}
python script.py --api-key your-api-key-here
```

## 🛠️ Common Requirements

All examples require:

* **Python 3.7+**
* **Perplexity API Key** ([Get one here](https://docs.perplexity.ai/guides/getting-started))
* **Internet connection** for API calls

Additional requirements vary by example and are listed in each `requirements.txt` file.

## 🎯 Choosing the Right Example

| **If you want to...**       | **Use this example**         |
| --------------------------- | ---------------------------- |
| Verify information accuracy | **Fact Checker CLI**         |
| Learn something new daily   | **Daily Knowledge Bot**      |
| Look up medical information | **Disease Information App**  |
| Track financial markets     | **Financial News Tracker**   |
| Research academic topics    | **Academic Research Finder** |

## 🤝 Contributing

Found a bug or want to improve an example? We welcome contributions!

1. **Report Issues**: Open an issue describing the problem
2. **Suggest Features**: Propose new functionality or improvements
3. **Submit Code**: Fork, implement, and submit a pull request

See our [Contributing Guidelines](https://github.com/ppl-ai/api-cookbook/blob/main/CONTRIBUTING.md) for details.

## 📄 License

All examples are licensed under the [MIT License](https://github.com/ppl-ai/api-cookbook/blob/main/LICENSE).

***

**Ready to explore?** Pick an example above and start building with Perplexity's Sonar API! 🚀