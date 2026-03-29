---
title: FlameGuardAI | AI-powered wildfire prevention
url: https://docs.perplexity.ai/docs/cookbook/showcase/flameguardai.md
source: llms
fetched_at: 2026-02-04T07:22:00.717095777-03:00
rendered_js: false
word_count: 634
summary: This document introduces FlameGuardAI, an AI-powered tool that analyzes property photos using OpenAI Vision and Perplexity Sonar API to detect wildfire risks and provide detailed mitigation reports. It details the system's architecture, process for deep research, and technical stack used to convert visual data into actionable safety plans.
tags:
    - wildfire-prevention
    - perplexity-sonar-api
    - openai-vision
    - risk-assessment
    - home-safety
    - ai-integration
    - multimodal-ai
category: other
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# FlameGuardAI | AI-powered wildfire prevention

> AI-powered wildfire prevention using OpenAI Vision + Perplexity Sonar API

## 🧠 What it does

**FlameGuard AI™** helps homeowners, buyers, and property professionals detect and act on **external fire vulnerabilities** like wildfires or neighboring structure fires. It's more than a scan — it's a personalized research assistant for your home.

### Demo

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/EI5yT7_aD6U" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

### Try it out

* [FlameGuard AI](https://flameguardai.dlyog.com)
* [FlameGuard AI MCP](https://flameguardai-mcp.dlyog.com)
* [GitHub Repo](https://github.com/dlyog/fire-risk-assessor-drone-ai)

### Key Features:

* 📸 Upload a home photo
* 👁️ Analyze visible fire risks via **OpenAI Vision API**
* 📚 Trigger deep research using the **Perplexity Sonar API**
* 📄 Get a detailed, AI-generated report with:
  * Risk summary
  * Prevention strategies
  * Regional best practices
* 🛠️ Optional contractor referrals for mitigation
* 💬 Claude (MCP) chatbot integration for conversational analysis
* 🧾 GDPR-compliant data controls

Whether you're protecting your home, buying a new one, or just want peace of mind — **FlameGuard AI™ turns a photo into a plan**.

## ⚙️ How it works

### The FlameGuard AI™ Process

1. **📸 Upload**: User uploads a photo of their property
2. **👁️ AI Vision Analysis**: OpenAI Vision API identifies specific vulnerabilities (e.g., flammable roof, dry brush nearby)
3. **🔍 Deep Research**: For each risk, we generate a **custom research plan** and run **iterative agentic-style calls** to Perplexity Sonar
4. **📄 Report Generation**: Research is **aggregated, organized, and formatted** into an actionable HTML report — complete with citations, links, and visual guidance
5. **📧 Delivery**: Detailed report sent via email with DIY solutions and professional recommendations

### 🔍 Deep Research with Perplexity Sonar API

The real innovation is how we use the **Perplexity Sonar API**:

* We treat it like a research assistant gathering the best available information
* Each vulnerability triggers multiple queries covering severity, mitigation strategies, and localized insights
* Results include regional fire codes, weather patterns, and local contractor availability

This kind of **structured, trustworthy, AI-powered research would not be possible without Perplexity**.

### Technical Stack

FlameGuard AI™ is powered by a modern GenAI stack and built to scale:

* **Frontend**: Lightweight HTML dashboard with user account control, photo upload, and report access
* **Backend**: Python (Flask) with RESTful APIs
* **Database**: PostgreSQL (local) with **Azure SQL-ready** schema
* **AI Integration**: OpenAI Vision API + Perplexity Sonar API
* **Cloud-ready**: Built for **Azure App Service** with Dockerized deployment

## 🏆 Accomplishments that we're proud of

* Successfully used **OpenAI Vision + Perplexity Sonar API** together in a meaningful, real-world workflow
* Built a functioning **MCP server** that integrates seamlessly with Claude for desktop users
* Created a product that is **genuinely useful for homeowners today** — not just a demo
* Kept the experience simple, affordable, and scalable from the ground up
* Made structured deep research feel accessible and trustworthy

## 📚 What we learned

* The **Perplexity Sonar API** is incredibly powerful when used agentically — not just for answers, but for reasoning.
* Combining **multimodal AI (image + research)** opens up powerful decision-support tools.
* Users want **actionable insights**, not just data — pairing research with guidance makes all the difference.
* Trust and clarity are key: our design had to communicate complex information simply and helpfully.

## 🚀 What's next for FlameGuard AI™ - Prevention is Better Than Cure

We're just getting started.

### Next Steps:

* 🌐 Deploy to **Azure App Services** with production-ready database
* 📱 Launch mobile version with location-based scanning
* 🏡 Partner with **home inspection services** and **homeowners associations**
* 💬 Enhance Claude/MCP integration with voice-activated AI reporting
* 💸 Introduce B2B plans for real estate firms and home safety consultants
* 🛡️ Expand database of **local contractor networks** and regional fire codes

We're proud to stand with homeowners — not just to raise awareness, but to enable action.

**FlameGuard AI™ – Because some homes survive when others don't.**

***

**Contact us to know more: [info@dlyog.com](mailto:info@dlyog.com)**