---
title: API Roadmap
url: https://docs.perplexity.ai/docs/resources/feature-roadmap.md
source: llms
fetched_at: 2026-02-04T07:24:43.817540938-03:00
rendered_js: false
word_count: 252
summary: This document outlines the planned updates and upcoming features for the Perplexity API, highlighting improvements in performance, new endpoints, and expanded multimodal capabilities.
tags:
    - api-roadmap
    - product-updates
    - perplexity-api
    - embeddings-api
    - multimodal-features
    - performance-optimization
category: other
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# API Roadmap

> Upcoming features and improvements for the Perplexity API designed to enhance your development experience.

Our roadmap is shaped by our users - have a feature in mind? Submit your suggestion [here](https://community.perplexity.ai/) and help us build the future of AI together.

<AccordionGroup>
  <Accordion title="V2 Chat Completions Migration" description="An improvement to your existing API">
    We're migrating the Chat Completions API to a new v2 endpoint with significantly improved performance:

    * **Same Endpoint**: The `/v2/chat/completions` endpoint maintains full compatibility with the existing API contract
    * **Reduced Latency**: Approximately 40% lower latency compared to the current endpoint
    * **Automatic Migration**: Traffic from v1 will automatically be moved to v2 - this change is seamless and no action needs to be taken

    This migration will provide faster response times while maintaining full backward compatibility with your existing integrations.
  </Accordion>

  <Accordion title="Embeddings API" description="A new API for vector embeddings and semantic search">
    We're introducing an Embeddings API to enable semantic search and retrieval capabilities:

    * **Text Embeddings**: Generate high-quality vector embeddings from text input
    * **Semantic Search**: Build applications that can find and retrieve information based on meaning and context
    * **RAG Applications**: Power retrieval-augmented generation workflows with custom knowledge bases

    This API will enable you to build sophisticated search and retrieval applications that understand semantic relationships between content.
  </Accordion>

  <Accordion title="Video Upload Capabilities" description="Multimodal video processing">
    We're expanding our multimodal capabilities to include video uploads.

    This feature will enable:

    * **Video Content Analysis**: Upload and analyze video files directly through the API
    * **Frame-by-Frame Processing**: Extract insights from video content at multiple time points
    * **Visual Scene Understanding**: Analyze visual elements, objects, and activities in video content
    * **Multimodal Search**: Search for information based on both visual and audio elements from your uploaded videos

    Supported formats will include common video file types (MP4, MOV, AVI) with reasonable file size limits for API efficiency.

    This capability will unlock new use cases in content moderation, educational analysis, media research, and automated video summarization.
  </Accordion>

  <Accordion title="File Search & Connectors" description="Expanded data access">
    Expanding your ability to access and process information:

    * **File Repository Integration**: Query file repositories tied to your API organization
    * **Multi-format File Search**: Search across various file types (PDFs, documents, spreadsheets)
    * **External Data Source Integration**: Connect to external data stores and databases
    * **Enterprise Connector Parity**: Full feature parity with enterprise connector capabilities

    This feature will allow your applications to tap into a broader range of data sources for more comprehensive insights, enabling you to build applications that can search and analyze your organization's entire knowledge base.
  </Accordion>

  <Accordion title="Expanded Structured Outputs Support" description="Enhanced response formatting">
    We're expanding our structured outputs capabilities:

    * **Universal JSON Support**: JSON structured outputs are now available for all models across all tiers
    * **Advanced Schema Validation**: Enhanced validation options for more reliable structured data
    * **Output Templates**: Pre-defined templates for common use cases

    This expansion will make it easier to build applications that require consistent, structured data from our API responses.
  </Accordion>

  <Accordion title="Documentation Overhaul" description="More comprehensive resources">
    We're committed to making our documentation a truly exceptional resource:

    * **Improved Layout**: Optimized structure for better self-serve workflows
    * **Consistent Design**: Unified branding between our landing page and documentation
    * **Enhanced Content**: Revised explanations for better developer understanding
    * **Vertical-Specific Guides**: Specialized documentation for publishers, merchants, and other industry partners
    * **High-Fidelity Demos**: More comprehensive examples beyond our basic cookbook demos
    * **Comprehensive Prompt Guide**: In-depth resources to help you build effectively with our search + LLM API
    * **API Selection Guides**: Clear guidance on which API is best suited for specific scenarios

    These improvements will help you get up to speed faster and make the most of our API capabilities.
  </Accordion>

  <Accordion title="Increased Rate Limits" description="Support for high-volume applications">
    We're scaling our infrastructure to support significantly higher request volumes:

    * **Enterprise-Scale Rate Limits**: Supporting use cases up to 100K requests per minute
    * **High-Growth Startup Support**: Designed specifically for rapidly scaling applications
    * **Infrastructure Reliability**: Enhanced stability and reduced latency spikes under high load
    * **Regional Scaling**: Expanded infrastructure deployment for global applications

    This enhancement will ensure our API can grow alongside your application's user base and processing needs, supporting everything from high-growth startups to enterprise-scale deployments.
  </Accordion>

  <Accordion title="Better Error Handling" description="Clearer troubleshooting">
    Improving our error framework:

    * More descriptive error messages
    * Clearer guidance on resolving common issues

    This will reduce debugging time and help you understand and address issues more efficiently.
  </Accordion>

  <Accordion title="Multimedia Capabilities" description="Beyond text processing">
    Broadening the types of content you can work with:

    * **URL Content Integration**: Specify URLs within prompts to search for and analyze content from specific web pages directly
    * **Advanced URL Parsing**: Extract and analyze content from web pages with enhanced accuracy and context understanding
    * **Web Page Analysis**: Deep content extraction including text, images, and structured data from URLs
    * **Real-time Web Content**: Access to live web content for dynamic analysis and research

    These features will enable new use cases and richer interactions within your applications, allowing you to reference specific web content and build more comprehensive research workflows with real-time web data integration.
  </Accordion>

  <Accordion title="Context Management / Memory" description="Improved context handling">
    We're addressing the limitations of managing context in API calls by introducing new context management features.

    Key improvements include:

    * **Efficient Context Storage**: Avoid appending responses from previous API calls to new ones, reducing the risk of exceeding context windows.
    * **Session-Based Memory**: Enable session-based memory to maintain context across multiple API calls without manual intervention.

    These enhancements will make it easier to build applications that require persistent context without hitting technical limitations.
  </Accordion>

  <Accordion title="Pro Search Public Release" description="Advanced agentic capabilities for all">
    We're preparing to make Pro Search available to all API users:

    * **Multi-step Reasoning**: Access to the advanced agentic research capabilities currently in beta
    * **Dynamic Tool Execution**: Automated web searches, URL content fetching, and Python code execution
    * **Intelligent Classification**: Automatic determination of when to use pro search vs fast search based on query complexity
    * **Transparent Reasoning**: Real-time streaming of the model's thought process and tool usage

    This will unlock sophisticated research workflows and enable your applications to handle complex, multi-dimensional queries that require computational analysis and deep web research.
  </Accordion>

  <Accordion title="Voice-to-Voice API" description="Real-time audio interactions">
    Introducing voice-based interactions through our API:

    * **Real-time Voice Processing**: Direct voice input and audio response generation
    * **Natural Conversation Flow**: Maintain context across voice interactions
    * **Multi-language Support**: Voice capabilities across multiple languages
    * **Low-latency Streaming**: Optimized for real-time voice applications

    This capability will enable voice assistants, interactive applications, and hands-free interfaces that can search and reason about information through natural speech.
  </Accordion>

  <Accordion title="Finance Tools Integration" description="Financial data and analysis">
    Expanding our capabilities with specialized financial tools:

    * **Market Data Access**: Real-time and historical stock prices, market indicators
    * **Ticker Symbol Lookup**: Intelligent company and symbol resolution
    * **Financial Analysis Tools**: Price history, trend analysis, and market insights
    * **SEC Filing Integration**: Enhanced search and analysis of financial documents

    These tools will enable sophisticated financial applications, trading platforms, and investment research tools with access to comprehensive financial data and analysis capabilities.
  </Accordion>

  <Accordion title="Labs Features via API" description="Experimental capabilities">
    Bringing cutting-edge experimental features to the API:

    * **Early Access Features**: Test new capabilities before general release
    * **Advanced Model Variants**: Access to experimental model configurations
    * **Prototype Integrations**: Early versions of upcoming integrations and tools
    * **Developer Feedback Integration**: Direct influence on feature development through testing

    This will give developers early access to innovative features and the opportunity to shape the future direction of our API capabilities.
  </Accordion>

  <Accordion title="Enhanced Third-Party Integrations" description="Seamless ecosystem connectivity">
    Expanding our integration ecosystem:

    * **Agentic Framework Support**: Enhanced integrations with LangChain, LlamaIndex, and other AI frameworks
    * **Developer Platform Integration**: Native support for popular development environments
    * **Workflow Automation**: Integration with automation platforms and CI/CD pipelines
    * **Real-time Collaboration**: Enhanced tooling for team-based development

    These integrations will make it easier to incorporate our API into your existing development workflows and build more sophisticated AI applications.
  </Accordion>

  <Accordion title="Developer Analytics Dashboard" description="Comprehensive usage insights">
    Advanced analytics and monitoring for your API usage:

    * **Query Analysis**: Detailed insights into query patterns, types, and performance
    * **Usage Metrics**: Comprehensive tracking of API calls, response times, and success rates
    * **Error Monitoring**: Detailed error tracking and debugging information
    * **Performance Optimization**: Insights to help optimize your application's API usage
    * **Cost Management**: Detailed billing breakdowns and usage forecasting

    This dashboard will provide the visibility you need to optimize your applications, manage costs, and understand user behavior patterns.
  </Accordion>
</AccordionGroup>

## Timeline and Availability

This roadmap represents our current development priorities. Features will be released incrementally, with some becoming available in the coming months and others planned for later in the year.

We'll announce new feature availability through our [changelog](/docs/resources/changelog) and via email notifications to API users.