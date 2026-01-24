# Z.AI Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://docs.z.ai/llms.txt |
| **Generated** | 2026-01-24 |
| **Total Documents** | 88 |
| **Strategy** | llms |

---

## Document Index

### 1. Overview & Introduction (001-005)
*Platform overview, quick start guides, and core concepts for getting started with Z.AI.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-guides-overview-overview.md` | Overview | Comprehensive overview of Z.AI model ecosystem with text, vision, image, and video generation models | z-ai-models, large-language-models, vision-language-models, model-capabilities |
| 002 | `002-guides-overview-quick-start.md` | Quick Start | Step-by-step introduction to Z.AI Open Platform covering API key, model selection, and SDKs | quick-start, api-integration, z-ai-platform, python-sdk, java-sdk |
| 003 | `003-guides-overview-concept-param.md` | Core Parameters | Detailed overview of core LLM configuration parameters including sampling, token limits, reasoning | llm-parameters, temperature, nucleus-sampling, max-tokens |
| 004 | `004-guides-overview-pricing.md` | Pricing | Pricing structure for Z.AI's suite of AI models including text, image, video, audio | pricing, z-ai, token-costs, glm-models, billing |
| 005 | `005-guides-overview-migrate-to-glm-new.md` | Migrate to GLM-4.7 | Migration guide from legacy models to GLM-4.7 with code examples | glm-4-7, model-migration, api-integration, streaming-tool-calls |

### 2. API Reference - Introduction & Core (011-013)
*API fundamentals, authentication, error codes, and rate limiting.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 011 | `011-api-reference-introduction.md` | Introduction | Introduction to Z.AI RESTful API with endpoint configurations and authentication | z-ai-api, rest-api, authentication, sdk-integration, http-bearer |
| 012 | `012-api-reference-api-code.md` | Errors | HTTP status codes and internal business error codes for troubleshooting | error-codes, http-status-codes, api-errors, troubleshooting |
| 013 | `013-api-reference-rate-limit.md` | Rate Limits | Rate limiting documentation | rate-limits, api-limits |

### 3. API Reference - LLM (021)
*Chat completion API for text generation.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 021 | `021-api-reference-llm-chat-completion.md` | Chat Completion | OpenAPI spec for Chat Completion API with multimodal inputs and streaming | chat-completion, multimodal-ai, text-generation, vision-model, function-calling |

### 4. API Reference - Agents (026-029)
*Agent chat, conversation history, file upload, and async result retrieval.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 026 | `026-api-reference-agents-agent.md` | Agent Chat | OpenAPI definition for Z.AI chat agents including translation, video, slides | openapi-spec, agent-chat, translation-api, video-generation |
| 027 | `027-api-reference-agents-agent-conversation.md` | Conversation History | API spec for conversation history endpoint for slides_glm_agent | api-specification, conversation-history, slides-glm-agent |
| 028 | `028-api-reference-agents-file-upload.md` | File Upload | File Upload API for glossaries and terminology lists | file-upload, api-reference, translation-support |
| 029 | `029-api-reference-agents-get-async-result.md` | Retrieve Result | API spec for querying async agent request status and outcomes | api-reference, asynchronous-processing, task-retrieval |

### 5. API Reference - Audio (036)
*Audio transcription API.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 036 | `036-api-reference-audio-audio-transcriptions.md` | Audio Transcriptions | API spec for transcribing audio using GLM-ASR-2512 with sync and streaming | audio-transcription, speech-to-text, glm-asr, streaming-data |

### 6. API Reference - Image (041-043)
*Image generation APIs (sync and async).*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 041 | `041-api-reference-image-generate-image.md` | Generate Image | API spec for image generation from text prompts using GLM-Image | image-generation, text-to-image, glm-image, api-reference |
| 042 | `042-api-reference-image-generate-image-async.md` | Generate Image(Async) | API spec for async image generation using GLM-Image | image-generation, async-api, glm-image, text-to-image |
| 043 | `043-api-reference-image-get-image-status.md` | Retrieve Result | API for querying async task status for video and image generation | z-ai-api, async-result, video-generation, image-generation |

### 7. API Reference - Video (051-052)
*Video generation APIs.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 051 | `051-api-reference-video-generate-video.md` | Generate Video(Async) | OpenAPI for async video generation using CogVideoX and Vidu | video-generation, async-api, cogvideox, vidu, text-to-video |
| 052 | `052-api-reference-video-get-video-status.md` | Retrieve Result | API for retrieving async task status and results for image/video | api-reference, async-processing, video-generation, task-status |

### 8. API Reference - Tools (061-063)
*Tokenizer, web search, and web reader APIs.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 061 | `061-api-reference-tools-tokenizer.md` | Tokenizer | API for calculating token counts for text, images, video | tokenizer-api, token-count, llm-infrastructure, usage-tracking |
| 062 | `062-api-reference-tools-web-search.md` | Web Search | OpenAPI spec for Web Search optimized for LLM processing | web-search, openapi-spec, llm-tools, search-engine |
| 063 | `063-api-reference-tools-web-reader.md` | Web Reader | API for parsing and extracting URL content to markdown/text | web-reader, content-parsing, web-scraping, markdown-conversion |

### 9. LLM Model Guides (071-074)
*Detailed guides for GLM language model series.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 071 | `071-guides-llm-glm-4.7.md` | GLM-4.7 | Overview of GLM-4.7 with specs, function calling, context caching | glm-4-7, llm-specifications, ai-coding, multimodal-interaction |
| 072 | `072-guides-llm-glm-4.6.md` | GLM-4.6 | GLM-4.6 enhancements in coding, reasoning, long-context | glm-4-6, large-language-model, api-integration, coding-performance |
| 073 | `073-guides-llm-glm-4.5.md` | GLM-4.5 | GLM-4.5 series with MoE architecture and reasoning capabilities | glm-4-5, mixture-of-experts, large-language-models, agent-applications |
| 074 | `074-guides-llm-glm-4-32b-0414-128k.md` | GLM-4-32B-0414-128K | Technical specs and quick-start for GLM-4-32B-0414-128K | glm-4, large-language-model, llm-api, function-calling |

### 10. Vision Language Model Guides (086-088)
*Multimodal vision-language models.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 086 | `086-guides-vlm-glm-4.6v.md` | GLM-4.6V | GLM-4.6V multimodal with 128k context and tool-calling | multimodal-llm, glm-4-6v, visual-understanding, function-calling |
| 087 | `087-guides-vlm-glm-4.5v.md` | GLM-4.5V | GLM-4.5V multimodal visual reasoning model overview | glm-4-5v, multimodal-llm, visual-reasoning, computer-vision |
| 088 | `088-guides-vlm-autoglm-phone-multilingual.md` | AutoGLM-Phone-Multilingual | Vision-language framework for Android automation | autoglm, multimodal-llm, android-automation, adb-control |

### 11. Audio Guides (096)
*Speech recognition model guide.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 096 | `096-guides-audio-glm-asr-2512.md` | GLM-ASR-2512 | Speech recognition model with basic and streaming API calls | speech-recognition, asr, audio-transcription, glm-asr-2512 |

### 12. Image Generation Guides (101-102)
*Image generation model guides.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 101 | `101-guides-image-glm-image.md` | GLM-Image | GLM-Image generation with Python and Java SDK integration | image-generation, glm-image, ai-sdk, python, java |
| 102 | `102-guides-image-cogview-4.md` | CogView-4 | Open-source bilingual text-to-image model with variable resolutions | cogview-4, text-to-image, image-generation, bilingual-model |

### 13. Video Generation Guides (111-113)
*Video generation model guides.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 111 | `111-guides-video-cogvideox-3.md` | CogVideoX-3 | HD video generation from text, images, or frames | cogvideox-3, video-generation, text-to-video, image-to-video |
| 112 | `112-guides-video-vidu-q1.md` | Vidu Q1 | Multi-modal video generation for film and advertising | vidu-q1, video-generation, text-to-video, image-to-video |
| 113 | `113-guides-video-vidu2.md` | Vidu 2 | High-speed image-to-video and keyframe-based generation | vidu-2, video-generation, image-to-video, keyframe-animation |

### 14. Capabilities & Features (121-127)
*Core capabilities like streaming, function calling, structured output, and thinking modes.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 121 | `121-guides-capabilities-streaming.md` | Streaming Messages | Real-time response generation with SSE | streaming-messages, real-time-response, server-sent-events |
| 122 | `122-guides-capabilities-function-calling.md` | Function Calling | Implement function calling with external systems | function-calling, ai-agents, python-sdk, api-integration |
| 123 | `123-guides-capabilities-struct-output.md` | Structured Output | JSON mode for structured AI responses | structured-output, json-mode, json-schema, data-extraction |
| 124 | `124-guides-capabilities-thinking.md` | Deep Thinking | Chain-of-thought reasoning in GLM models | deep-thinking, chain-of-thought, glm-models, reasoning |
| 125 | `125-guides-capabilities-thinking-mode.md` | Thinking Mode | GLM-4.7 thinking modes for tool-calling and conversation | glm-4-7, thinking-mode, reasoning-content, tool-calling |
| 126 | `126-guides-capabilities-cache.md` | Context Caching | Automatic context caching for cost reduction | context-caching, token-optimization, cost-reduction |
| 127 | `127-guides-capabilities-stream-tool.md` | Tool Streaming Output | Streaming for tool calls and reasoning | tool-calling, streaming-output, glm-4-6, real-time-feedback |

### 15. Tools Guides (136-137)
*Web search and streaming tool guides.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 136 | `136-guides-tools-web-search.md` | Web Search | Web search tool overview | web-search, financial-calendar, market-analysis |
| 137 | `137-guides-tools-stream-tool.md` | Stream Tool Call | Stream Tool Call in GLM-4.6 for real-time feedback | zai-platform, glm-4-6, streaming-output, tool-calling |

### 16. Agent Guides (146-148)
*Specialized AI agents for slides, translation, and video.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 146 | `146-guides-agents-slide.md` | GLM Slide/Poster Agent(beta) | AI tool for converting natural language to slides/posters | glm-agent, slide-generation, poster-creation, visual-design |
| 147 | `147-guides-agents-translation.md` | Translation Agent | AI translation with 6 strategies and 40+ languages | translation-agent, multilingual-support, language-localization |
| 148 | `148-guides-agents-video-template.md` | Video Effect Template Agent | AI video templates for special effects from images | video-generation, ai-agent, image-to-video, special-effects |

### 17. SDK & Development (156-160)
*SDK guides for HTTP, Python, Java, OpenAI compatibility, and LangChain.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 156 | `156-guides-develop-http-introduction.md` | HTTP API Calls | Technical overview for Z.AI RESTful HTTP API | http-api, restful, authentication, jwt, api-key |
| 157 | `157-guides-develop-python-introduction.md` | Official Python SDK | Z.AI Python SDK installation and core features | python-sdk, zai-platform, llm-integration, developer-tools |
| 158 | `158-guides-develop-java-introduction.md` | Official Java SDK | Z.AI Java SDK guide with Maven/Gradle setup | java-sdk, zai-api, maven-dependency, gradle-setup |
| 159 | `159-guides-develop-openai-python.md` | OpenAI Python SDK | Integrate OpenAI Python SDK with Z.AI services | openai-sdk, python, z-ai, api-compatibility, llm-integration |
| 160 | `160-guides-develop-langchain-introduction.md` | LangChain Integration | Integrate Z.AI with LangChain framework | langchain, z-ai-integration, python-sdk, llm-orchestration |

### 18. DevPack Overview (171-174)
*GLM Coding Plan overview, quick start, FAQs, and referral program.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 171 | `171-devpack-overview.md` | Overview | GLM Coding Plan for integrating GLM-4.7 into coding tools | glm-coding-plan, ai-powered-coding, glm-4-7, subscription-plans |
| 172 | `172-devpack-quick-start.md` | Quick Start | Setup GLM Coding Plan with API key and model configuration | glm-coding-plan, api-setup, coding-tools, quick-start |
| 173 | `173-devpack-faq.md` | FAQs | GLM Coding Plan FAQs on subscriptions, quotas, billing | glm-coding-plan, subscription-management, usage-quotas |
| 174 | `174-devpack-credit-campaign-rules.md` | Invite Friends, Get Credits | Z.ai referral program rules and incentives | referral-program, platform-credits, user-rewards |

### 19. DevPack Extensions (181-182)
*CLI helper and usage query plugins.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 181 | `181-devpack-extension-coding-tool-helper.md` | Coding Tool Helper | CLI for managing AI coding tools with GLM plans | cli-assistant, tool-management, mcp-server, coding-tools |
| 182 | `182-devpack-extension-usage-query-plugin.md` | Usage Query Plugin | Plugin for monitoring GLM Coding Plan quota | claude-code, glm-coding-plan, usage-monitoring |

### 20. DevPack MCP Servers (186-189)
*Model Context Protocol servers for web reading, search, vision, and GitHub.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 186 | `186-devpack-mcp-reader-mcp-server.md` | Web Reader MCP Server | MCP server for web content extraction | mcp-server, web-content-extraction, model-context-protocol |
| 187 | `187-devpack-mcp-search-mcp-server.md` | Web Search MCP Server | MCP server for real-time web search | mcp-server, web-search, z-ai, model-context-protocol |
| 188 | `188-devpack-mcp-vision-mcp-server.md` | Vision MCP Server | MCP server for GLM-4.6V vision capabilities | vision-mcp-server, model-context-protocol, image-analysis |
| 189 | `189-devpack-mcp-zread-mcp-server.md` | Zread MCP Server | MCP server for GitHub repository data access | mcp-server, github-integration, code-analysis, zread-ai |

### 21. DevPack Tool Integrations (196-208)
*Integration guides for various AI coding tools.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 196 | `196-devpack-tool-claude.md` | Claude Code | Install Claude Code with GLM Coding Plan via Z.AI | claude-code, glm-4, z-ai-integration, cli-setup |
| 197 | `197-devpack-tool-claude-for-ide.md` | Claude Code IDE Plugin | Claude Code plugin for VS Code and JetBrains | claude-code, ide-plugin, vs-code, jetbrains |
| 198 | `198-devpack-tool-cline.md` | Cline | Cline VS Code extension with GLM Coding Plan | cline, vs-code, glm-coding-plan, ai-integration |
| 199 | `199-devpack-tool-cursor.md` | Cursor | GLM-4.7 integration in Cursor IDE | cursor-ide, glm-4-7, openai-api-protocol |
| 200 | `200-devpack-tool-crush.md` | Crush | Crush AI coding agent with Z.AI API | crush-ai, terminal-agent, glm-coding-plan |
| 201 | `201-devpack-tool-droid.md` | Factory Droid | Factory Droid with Z.AI GLM models | factory-droid, z-ai-glm, ai-coding-agent, byok |
| 202 | `202-devpack-tool-eigent.md` | Eigent | Eigent desktop agent with Z.ai GLM models | eigent, glm-coding-plan, desktop-agent |
| 203 | `203-devpack-tool-goose.md` | Goose | Goose AI agent with GLM via Anthropic-compatible provider | goose-desktop, glm-models, z-ai-api, mcp-protocol |
| 204 | `204-devpack-tool-kilo.md` | Kilo Code | Kilo Code VS Code extension with GLM | vs-code-extension, kilo-code, glm-coding-plan |
| 205 | `205-devpack-tool-opencode.md` | Open Code | OpenCode CLI with Z.AI GLM models | opencode-cli, z-ai-glm, ai-coding-assistant |
| 206 | `206-devpack-tool-roo.md` | Roo Code | Roo Code VS Code plugin with GLM | roo-code, vs-code-extension, glm-coding-plan |
| 207 | `207-devpack-tool-trae.md` | TRAE | GLM-4.7 integration in TRAE IDE | trae-ide, glm-4, z-ai-api, coding-assistant |
| 208 | `208-devpack-tool-others.md` | Other Tools | GLM-4.7 integration via OpenAI-compatible API | glm-4-7, openai-protocol, api-configuration |

### 22. Scenario Examples (216-223)
*Step-by-step integration examples for various tools.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 216 | `216-scenario-example-develop-tools-claude.md` | Claude Code | GLM-4.7 integration in Claude Code via Anthropic endpoint | claude-code, glm-4-7, z-ai, api-integration |
| 217 | `217-scenario-example-develop-tools-cline.md` | Cline | Cline VS Code with Z.AI GLM via OpenAI API | cline, vs-code-extension, glm-4, api-configuration |
| 218 | `218-scenario-example-develop-tools-gemini.md` | Gemini CLI | Customized Gemini CLI for Z.AI GLM | gemini-cli, z-ai, glm-models, cli-configuration |
| 219 | `219-scenario-example-develop-tools-gork.md` | Grok CLI | Grok CLI with Z.AI GLM models | grok-cli, z-ai, glm-models, cli-installation |
| 220 | `220-scenario-example-develop-tools-kilo.md` | Kilo Code | Kilo Code VS Code with Z.AI GLM | vs-code, kilo-code, z-ai, mcp-protocol |
| 221 | `221-scenario-example-develop-tools-n8n.md` | n8n Workflow | Z.AI GLM in n8n workflows via OpenAI node | n8n-integration, z-ai-glm, workflow-automation |
| 222 | `222-scenario-example-develop-tools-opencode.md` | OpenCode | OpenCode AI agent with Z.AI GLM | opencode, z-ai-glm, ai-coding-agent, cli-integration |
| 223 | `223-scenario-example-develop-tools-roo.md` | Roo Code | Roo Code VS Code with Z.AI GLM | roo-code, vs-code, z-ai, glm-model |

### 23. Help & FAQ (231)
*Frequently asked questions and troubleshooting.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 231 | `231-help-faq.md` | FAQ | GLM-4.5 FAQs on caching, billing, rate limits, payments | faq, glm-4-5, caching, billing, rate-limits |

### 24. Legal & Terms (236-238)
*Terms of use, privacy policy, and subscription terms.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 236 | `236-legal-agreement-terms-of-use.md` | Terms of Use | Legal terms and prohibited activities for Z.ai services | terms-of-use, legal-agreement, user-conduct |
| 237 | `237-legal-agreement-privacy-policy.md` | Privacy Policy | How Z.ai collects and protects personal data | privacy-policy, data-protection, personal-data |
| 238 | `238-legal-agreement-subscription-terms.md` | Subscriptions, Fees, and Payment | Billing, subscriptions, and payment terms | billing-terms, subscription-policy, payment-processing |

### 25. Release Notes (241)
*Changelog and release history.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 241 | `241-release-notes-new-released.md` | New Released | Chronological log of Z.AI model updates and releases | z-ai, model-updates, release-notes, glm-series, changelog |

---

## Quick Reference

### By Topic

| Topic | File Range |
|-------|------------|
| **Getting Started** | 001-005 |
| **API Reference** | 011-063 |
| **LLM Models** | 071-074 |
| **Vision Models** | 086-088 |
| **Audio** | 096 |
| **Image Generation** | 101-102 |
| **Video Generation** | 111-113 |
| **Capabilities** | 121-127 |
| **Tools** | 136-137 |
| **Agents** | 146-148 |
| **SDKs** | 156-160 |
| **DevPack & Coding Plan** | 171-208 |
| **Integration Examples** | 216-223 |
| **Help** | 231 |
| **Legal** | 236-238 |
| **Release Notes** | 241 |

### By Concept

| Concept | Files |
|---------|-------|
| **GLM-4.7 (Latest)** | 005, 071, 125, 171, 199, 207 |
| **Function Calling** | 021, 074, 122, 127 |
| **Streaming** | 021, 036, 121, 127, 137 |
| **Vision/Multimodal** | 086, 087, 088, 188 |
| **Image Generation** | 041-043, 101-102 |
| **Video Generation** | 051-052, 111-113, 148 |
| **MCP Servers** | 186-189 |
| **Claude Code** | 196-197, 216 |
| **VS Code Extensions** | 198, 204, 206, 217, 220, 223 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read files **001-002** for platform overview and quick start
- Review **003-004** for core parameters and pricing

### Level 2: API Understanding
- Study **011-013** for API introduction and error handling
- Explore **021** for chat completion fundamentals

### Level 3: Model Selection
- Compare LLM models in **071-074**
- Explore vision models in **086-088** if needed
- Review image/video models in **101-113**

### Level 4: Advanced Capabilities
- Learn capabilities in **121-127** (streaming, function calling, thinking modes)
- Understand agents in **146-148**

### Level 5: SDK Integration
- Choose your SDK path: HTTP (156), Python (157), Java (158), OpenAI (159), LangChain (160)
- Set up DevPack with **171-172**

### Level 6: Tool Integration
- Configure your preferred coding tool from **196-208**
- Use MCP servers from **186-189** for enhanced capabilities

### Level 7: Reference
- Consult **231** for FAQs
- Review **241** for latest releases

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression adapted to the Z.AI documentation structure.*
