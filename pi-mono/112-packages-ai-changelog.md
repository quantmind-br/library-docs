---
title: CHANGELOG
url: https://github.com/badlogic/pi-mono/blob/main/packages/ai/CHANGELOG.md
source: git
fetched_at: 2026-05-03T09:30:59.547460391-03:00
rendered_js: false
word_count: 4080
summary: This document provides a detailed changelog of software releases, outlining breaking changes, new provider integrations, and bug fixes for AI model handling and API compatibility.
tags:
    - changelog
    - api-integration
    - breaking-changes
    - ai-models
    - software-updates
    - provider-configuration
category: reference
optimized: true
optimized_at: 2026-05-03T12:31:00Z
---
# Changelog

## [Unreleased]

### Breaking Changes

> [!warning]
> Switched `xiaomi` provider from Token Plan AMS (`https://token-plan-ams.xiaomimimo.com/anthropic`) to API billing (`https://api.xiaomimimo.com/anthropic`). `XIAOMI_API_KEY` now refers to API billing key from [platform.xiaomimimo.com](https://platform.xiaomimimo.com). Token Plan users must switch to `xiaomi-token-plan-*` providers.

### Added

- Xiaomi MiMo Token Plan regional providers:
  - `xiaomi-token-plan-cn` — `XIAOMI_TOKEN_PLAN_CN_API_KEY`
  - `xiaomi-token-plan-ams` — `XIAOMI_TOKEN_PLAN_AMS_API_KEY`
  - `xiaomi-token-plan-sgp` — `XIAOMI_TOKEN_PLAN_SGP_API_KEY`

## [0.72.1] - 2026-05-02

No changes.

## [0.72.0] - 2026-05-01

### Breaking Changes

> [!warning]
> Replaced `OpenAICompletionsCompat.reasoningEffortMap` with top-level `Model.thinkingLevelMap` for model-specific thinking controls ([#3208](https://github.com/badlogic/pi-mono/issues/3208)).

**Migration:**
```ts
// Before
compat: { reasoningEffortMap: { high: "high", xhigh: "max" } }

// After
thinkingLevelMap: { minimal: null, low: null, medium: null, high: "high", xhigh: "max" }
```

> [!warning]
> Removed `supportsXhigh()`. Use `getSupportedThinkingLevels(model).includes("xhigh")` or `clampThinkingLevel(model, requestedLevel)` instead.

### Added

- Xiaomi MiMo Token Plan provider (Anthropic-compatible), `XIAOMI_API_KEY` auth ([#4005](https://github.com/badlogic/pi-mono/pull/4005) by [@Phoen1xCode](https://github.com/Phoen1xCode)).
- `Model.thinkingLevelMap`, `getSupportedThinkingLevels()`, `clampThinkingLevel()` for model-specific thinking metadata ([#3208](https://github.com/badlogic/pi-mono/issues/3208)).

### Fixed

- OpenAI Codex Responses `streamSimple()` now honors configured transport (not always SSE); `auto` defaults to cached WebSocket ([#4083](https://github.com/badlogic/pi-mono/issues/4083)).
- Xiaomi MiMo model catalog uses Token Plan Anthropic endpoint, not direct API ([#3912](https://github.com/badlogic/pi-mono/issues/3912)).

## [0.71.1] - 2026-05-01

### Added

- `websocket-cached` transport for OpenAI Codex Responses with ChatGPT subscription auth. Keeps WebSocket open per session, sends only new conversation items after first request.

## [0.71.0] - 2026-04-30

### Breaking Changes

> [!warning]
> Removed built-in Google Gemini CLI and Google Antigravity support (provider registration, model metadata, OAuth, package exports). Switch to another supported provider.

### Added

- Cloudflare AI Gateway as built-in provider with OpenAI, Anthropic, Workers AI routing. Auth: `CLOUDFLARE_API_KEY`/`CLOUDFLARE_ACCOUNT_ID`/`CLOUDFLARE_GATEWAY_ID` ([#3856](https://github.com/badlogic/pi-mono/pull/3856) by [@mchenco](https://github.com/mchenco)).
- Moonshot AI as built-in OpenAI-compatible provider. Auth: `MOONSHOT_API_KEY`.
- Mistral Medium 3.5 model metadata and reasoning-mode handling ([#4009](https://github.com/badlogic/pi-mono/pull/4009) by [@technocidal](https://github.com/technocidal)).
- `AssistantMessage.responseModel` on openai-completions path: surfaces concrete `chunk.model` when it differs from requested id (e.g. OpenRouter `auto` -> `anthropic/...`) ([#3968](https://github.com/badlogic/pi-mono/pull/3968) by [@purrgrammer](https://github.com/purrgrammer)).

### Fixed

- Google Vertex Gemini 3 tool call replay: no longer sends `skip_thought_signature_validator` sentinel for unsigned tool calls ([#4032](https://github.com/badlogic/pi-mono/issues/4032)).
- Updated `@anthropic-ai/sdk` to `^0.91.1` (clears GHSA-p7fg-763f-g4gf) ([#3992](https://github.com/badlogic/pi-mono/issues/3992)).
- DeepSeek V4 Flash `xhigh` thinking: preserves `xhigh` and maps to DeepSeek's `max` reasoning effort ([#3944](https://github.com/badlogic/pi-mono/issues/3944)).
- Anthropic streams ending before `message_stop` treated as errors, not successful partial responses ([#3936](https://github.com/badlogic/pi-mono/issues/3936)).
- Generated OpenAI-compatible DeepSeek V4 models carry provider-specific reasoning effort mapping outside direct DeepSeek provider ([#3940](https://github.com/badlogic/pi-mono/issues/3940)).
- DeepSeek V4 Flash and V4 Pro pricing metadata updated to current official rates ([#3910](https://github.com/badlogic/pi-mono/issues/3910)).
- DeepSeek prompt cache hits tracked from `prompt_cache_hit_tokens` in OpenAI-compatible usage responses ([#3880](https://github.com/badlogic/pi-mono/issues/3880)).

### Removed

- Built-in Google Gemini CLI and Google Antigravity provider, model, OAuth, and export support.

## [0.70.6] - 2026-04-28

### Added

- Cloudflare Workers AI as built-in provider. Auth: `CLOUDFLARE_API_KEY`/`CLOUDFLARE_ACCOUNT_ID`. OpenAI-compatible streaming, model catalog generation ([#3851](https://github.com/badlogic/pi-mono/pull/3851) by [@mchenco](https://github.com/mchenco)).

### Fixed

- Removed generated Cloudflare Workers AI `User-Agent` model headers.
- Bedrock inference profile capability checks: normalize profile ARNs to underlying model name.

## [0.70.5] - 2026-04-27

No changes.

## [0.70.4] - 2026-04-27

No changes.

## [0.70.3] - 2026-04-27

### Added

- Azure Cognitive Services endpoint support for Azure OpenAI Responses base URLs ([#3799](https://github.com/badlogic/pi-mono/pull/3799) by [@marcbloech](https://github.com/marcbloech)).

### Changed

- OpenAI Codex Responses default text verbosity set to `low` when no verbosity specified.

### Fixed

- API-key environment discovery falls back to `/proc/self/environ` when Bun's sandbox leaves `process.env` empty ([#3801](https://github.com/badlogic/pi-mono/pull/3801) by [@mdsjip](https://github.com/mdsjip)).
- Bedrock prompt-caching and adaptive-thinking capability checks use model name when model id is an inference profile ARN ([#3527](https://github.com/badlogic/pi-mono/pull/3527) by [@anirudhmarc](https://github.com/anirudhmarc)).
- Anthropic SSE parsing ignores unknown proxy events (e.g. OpenAI-style `done` terminators) ([#3708](https://github.com/badlogic/pi-mono/issues/3708)).
- OpenAI-compatible prompt cache tests cover proxies that explicitly disable long cache retention.
- `tools: []` no longer sent on OpenAI-compatible, Anthropic, OpenAI Responses, OpenAI Codex Responses, and Azure OpenAI Responses requests when no tools active. DashScope/Aliyun Qwen rejects `"[]"` with `"[] is too short - 'tools'"` (HTTP 400) ([#3650](https://github.com/badlogic/pi-mono/pull/3650) by [@HQidea](https://github.com/HQidea)).
- `supportsXhigh()` recognizes DeepSeek V4 Pro, preserving `xhigh` reasoning ([#3662](https://github.com/badlogic/pi-mono/issues/3662)).
- OpenAI-compatible DeepSeek V4 model replay includes empty `reasoning_content` on assistant messages when needed ([#3668](https://github.com/badlogic/pi-mono/issues/3668)).

## [0.70.2] - 2026-04-24

### Fixed

- OpenAI/Azure/Anthropic provider request option forwarding omits undefined `timeout`/`maxRetries`, avoiding SDK validation errors like `timeout must be an integer` ([#3627](https://github.com/badlogic/pi-mono/issues/3627)).

## [0.70.1] - 2026-04-24

### Added

- DeepSeek as built-in OpenAI-compatible provider with V4 Flash and V4 Pro models. Auth: `DEEPSEEK_API_KEY`.

### Fixed

- DeepSeek V4 session replay 400 errors fixed by adding `thinkingFormat: "deepseek"`, `reasoningEffortMap`, `requiresReasoningContentOnAssistantMessages` compat ([#3636](https://github.com/badlogic/pi-mono/issues/3636)).
- GPT-5.5 generated context window metadata uses observed 272k limit.
- Provider request controls expose `timeoutMs` and `maxRetries` in stream options and forward them through OpenAI/Azure/Anthropic request options ([#3627](https://github.com/badlogic/pi-mono/issues/3627)).

## [0.70.0] - 2026-04-23

### Added

- GPT-5.5 added to OpenAI Codex model generation.
- `findEnvKeys()` for callers to identify configured provider API-key environment variables without exposing credential values.

### Fixed

- `google-vertex` forwards custom `model.baseUrl` values to `@google/genai`, enabling Vertex proxy/gateway endpoints ([#3619](https://github.com/badlogic/pi-mono/issues/3619)).
- OpenAI-compatible completion usage parsing stops double-counting reasoning tokens already in `completion_tokens` ([#3581](https://github.com/badlogic/pi-mono/issues/3581)).
- Long cache retention compatibility via `compat.supportsLongCacheRetention` ([#3543](https://github.com/badlogic/pi-mono/issues/3543)).
- `openai-responses` compatibility via `compat.sendSessionIdHeader: false` ([#3579](https://github.com/badlogic/pi-mono/issues/3579)).
- `anthropic-messages` tool streaming compatibility via `compat.supportsEagerToolInputStreaming` ([#3575](https://github.com/badlogic/pi-mono/issues/3575)).
- `supportsXhigh()` recognizes `openai-codex` `gpt-5.5`, preserving `xhigh` instead of clamping to `high`.
- `openai-completions` streamed tool-call assembly coalesces deltas by stable tool index when gateways mutate tool call IDs mid-stream ([#3576](https://github.com/badlogic/pi-mono/issues/3576)).
- `packages/ai` E2E coverage updated to use currently supported OpenAI Responses and OpenAI Codex models; Bedrock adaptive-thinking payload updated to `display: "summarized"` shape.
- Built-in `kimi-coding` model generation attaches `User-Agent: KimiCLI/1.5` to all requests ([#3586](https://github.com/badlogic/pi-mono/issues/3586)).
- GPT-5.5 Codex capability handling: clamp unsupported minimal reasoning to `low`, apply 2.5x priority service-tier pricing multiplier ([#3618](https://github.com/badlogic/pi-mono/pull/3618) by [@markusylisiurunen](https://github.com/markusylisiurunen)).

## [0.69.0] - 2026-04-22

### Breaking Changes

> [!warning]
> Migrated TypeBox from `@sinclair/typebox` 0.34.x + AJV to `typebox` 1.x + TypeBox's built-in validator. Tool argument validation now runs in eval-restricted runtimes (Cloudflare Workers). Install and import from `typebox` instead of `@sinclair/typebox`. ([#3112](https://github.com/badlogic/pi-mono/issues/3112))

### Fixed

- `google-gemini-cli` built-in model discovery includes `gemini-3.1-flash-lite-preview` ([#3545](https://github.com/badlogic/pi-mono/issues/3545)).
- `transformMessages()` synthesizes missing trailing tool results for transcripts ending with unresolved assistant tool calls ([#3555](https://github.com/badlogic/pi-mono/issues/3555)).

## [0.68.1] - 2026-04-22

### Added

- Fireworks provider support via Fireworks' Anthropic-compatible Messages API, built-in models from models.dev. Auth: `FIREWORKS_API_KEY` ([#3519](https://github.com/badlogic/pi-mono/issues/3519)).

### Fixed

- Anthropic streaming hardened against malformed tool-call JSON: owns SSE parsing with defensive JSON repair, replaced deprecated `fine-grained-tool-streaming` beta header with per-tool `eager_input_streaming` ([#3175](https://github.com/badlogic/pi-mono/issues/3175)).
- Bedrock runtime endpoint resolution stops pinning built-in regional endpoints over `AWS_REGION`/`AWS_PROFILE`, restoring `us.*`/`eu.*` inference profile support ([#3481](https://github.com/badlogic/pi-mono/issues/3481), [#3485](https://github.com/badlogic/pi-mono/issues/3485), [#3486](https://github.com/badlogic/pi-mono/issues/3486), [#3487](https://github.com/badlogic/pi-mono/issues/3487), [#3488](https://github.com/badlogic/pi-mono/issues/3488)).

## [0.68.0] - 2026-04-20

### Added

- `PI_OAUTH_CALLBACK_HOST` support for built-in Anthropic, Gemini CLI, Google Antigravity, and OpenAI Codex OAuth flows ([#3409](https://github.com/badlogic/pi-mono/pull/3409) by [@Michaelliv](https://github.com/Michaelliv)).

### Changed

- Bedrock Converse requests omit `inferenceConfig.maxTokens` when model token limits unknown; omit `temperature` when unset ([#3400](https://github.com/badlogic/pi-mono/pull/3400) by [@wirjo](https://github.com/wirjo)).

### Fixed

- `openai-completions` `compat.requiresThinkingAsText` assistant replay preserves text-part serialization ([#3387](https://github.com/badlogic/pi-mono/issues/3387)).
- Cloud Code Assist tool schemas strip JSON Schema meta-declaration keys (`$schema`, `$defs`, `definitions`) before sending OpenAPI `parameters` ([#3412](https://github.com/badlogic/pi-mono/pull/3412) by [@vladlearns](https://github.com/vladlearns)).
- Non-vision model requests replace user and tool-result image blocks with text placeholders instead of silently dropping ([#3429](https://github.com/badlogic/pi-mono/issues/3429)).
- Direct OpenAI Chat Completions requests map `sessionId` and `cacheRetention` to OpenAI prompt caching fields ([#3426](https://github.com/badlogic/pi-mono/issues/3426)).
- OpenAI-compatible Chat Completions requests optionally send aligned session-affinity headers via `compat.sendSessionAffinityHeaders` ([#3430](https://github.com/badlogic/pi-mono/issues/3430)).
- Direct Bedrock runtime client construction passes `model.baseUrl` through as SDK `endpoint` ([#3402](https://github.com/badlogic/pi-mono/pull/3402) by [@wirjo](https://github.com/wirjo)).
- OpenAI-compatible Chat Completions Anthropic-style prompt caching applies `cache_control` breakpoint on last tool definition via `compat.cacheControlFormat` ([#3392](https://github.com/badlogic/pi-mono/issues/3392)).

## [0.67.68] - 2026-04-17

### Fixed

- Bedrock bearer-token authentication uses SDK's native token auth path, omits Claude `thinking.display` for GovCloud targets ([#3359](https://github.com/badlogic/pi-mono/issues/3359)).
- Direct Mistral tool definitions strip TypeBox symbol metadata before passing schemas to SDK ([#3361](https://github.com/badlogic/pi-mono/issues/3361)).

## [0.67.67] - 2026-04-17

### Added

- Bedrock Converse bearer-token authentication via `AWS_BEARER_TOKEN_BEDROCK` ([#3125](https://github.com/badlogic/pi-mono/pull/3125) by [@wirjo](https://github.com/wirjo)).

### Fixed

- Anthropic and Bedrock adaptive-thinking payload tests expect default `display: "summarized"` field.
- Mistral Small 4 reasoning requests use `reasoning_effort` instead of `prompt_mode` ([#3338](https://github.com/badlogic/pi-mono/issues/3338)).
- `qwen-chat-template` OpenAI-compatible requests set `chat_template_kwargs.preserve_thinking: true` ([#3325](https://github.com/badlogic/pi-mono/issues/3325)).
- OpenAI Codex service-tier accounting trusts explicitly requested tier when API echoes default tier ([#3307](https://github.com/badlogic/pi-mono/pull/3307) by [@markusylisiurunen](https://github.com/markusylisiurunen)).

## [0.67.6] - 2026-04-16

### Added

- `onResponse` in `StreamOptions` for inspecting provider HTTP status and headers after response arrives ([#3128](https://github.com/badlogic/pi-mono/issues/3128)).
- `thinkingDisplay` (`"summarized" | "omitted"`) in `AnthropicOptions` and `BedrockOptions`, wired to Anthropic/Bedrock `thinking` config. Defaults to `"summarized"`.

### Fixed

- OpenAI Responses prompt caching for non-`api.openai.com` base URLs sends `session_id` and `x-client-request-id` headers unconditionally when `sessionId` provided ([#3264](https://github.com/badlogic/pi-mono/pull/3264) by [@vegarsti](https://github.com/vegarsti)).

## [0.67.5] - 2026-04-16

### Fixed

- Opus 4.7 adaptive thinking configuration across Anthropic and Bedrock providers: recognizes Opus 4.7 adaptive-thinking support, maps `xhigh` to provider-supported effort values ([#3286](https://github.com/badlogic/pi-mono/pull/3286) by [@markusylisiurunen](https://github.com/markusylisiurunen)).

## [0.67.4] - 2026-04-16

### Changed

- Added `claude-opus-4-7` model for Anthropic, OpenRouter.
- Anthropic prompt caching adds `cache_control` breakpoint on last tool definition ([#3260](https://github.com/badlogic/pi-mono/issues/3260)).
- Kimi Coding model generation normalizes deprecated `k2p5` to `kimi-for-coding` from models.dev data ([#3242](https://github.com/badlogic/pi-mono/issues/3242)).

## [0.67.3] - 2026-04-15

### Fixed

- `google-vertex` API key resolution treats `gcp-vertex-credentials` as Application Default Credentials marker, not literal API key ([#3221](https://github.com/badlogic/pi-mono/pull/3221) by [@deepkilo](https://github.com/deepkilo)).

## [0.67.2] - 2026-04-14

### Fixed

- Direct OpenAI Responses requests send aligned `prompt_cache_key`, `session_id`, `x-client-request-id` when `sessionId` provided ([#3018](https://github.com/badlogic/pi-mono/pull/3018) by [@steipete](https://github.com/steipete)).
- Fixed streaming-only `partialJson` scratch buffers leaking into persisted OpenAI Responses tool calls.

## [0.67.1] - 2026-04-13

No changes.

## [0.67.0] - 2026-04-13

### Added

- Full `OpenRouterRouting` field support: fallbacks, parameter requirements, data collection, ZDR, ignore lists, quantizations, provider sorting, max price, preferred throughput/latency constraints ([#2904](https://github.com/badlogic/pi-mono/pull/2904) by [@zmberber](https://github.com/zmberber)).

### Fixed

- Bumped default Antigravity User-Agent version to `1.21.9` ([#2901](https://github.com/badlogic/pi-mono/pull/2901) by [@aadishv](https://github.com/aadishv)).
- Thinking levels for Gemma 4 models use `thinkingLevel` and map Pi reasoning levels to model's supported thinking levels ([#2903](https://github.com/badlogic/pi-mono/pull/2903) by [@aadishv](https://github.com/aadishv)).
- Gemini 2.5 Flash Lite minimal thinking budget uses model's supported 512-token minimum ([#2861](https://github.com/badlogic/pi-mono/pull/2861) by [@JasonOA888](https://github.com/JasonOA888)).
- OpenAI Codex Responses requests forward configured `serviceTier` values ([#2996](https://github.com/badlogic/pi-mono/pull/2996) by [@markusylisiurunen](https://github.com/markusylisiurunen)).

## [0.66.1] - 2026-04-08

No changes.

## [0.66.0] - 2026-04-08

### Fixed

- Fixed bare `readline` import to use `node:readline` prefix for Deno compatibility ([#2885](https://github.com/badlogic/pi-mono/issues/2885) by [@milosv-vtool](https://github.com/milosv-vtool)).

## [0.65.2] - 2026-04-06

No changes.

## [0.65.1] - 2026-04-05

### Fixed

- OpenAI-compatible completions streaming usage preserves `prompt_tokens_details.cache_write_tokens`, normalizes OpenRouter `cached_tokens` to previous-request cache hits only ([#2802](https://github.com/badlogic/pi-mono/issues/2802)).

## [0.65.0] - 2026-04-03

### Added

- Tool streaming support for newer Z.ai models ([#2732](https://github.com/badlogic/pi-mono/pull/2732) by [@kaofelix](https://github.com/kaofelix)).

### Fixed

- Anthropic context overflow detection recognizes HTTP 413 `request_too_large` errors ([#2734](https://github.com/badlogic/pi-mono/issues/2734)).
- OpenAI Responses tool-call streaming emits `toolcall_delta` when function call arguments arrive only in `response.function_call_arguments.done` ([#2745](https://github.com/badlogic/pi-mono/issues/2745)).
- Bedrock throttling errors no longer misidentified as context overflow ([#2699](https://github.com/badlogic/pi-mono/pull/2699) by [@xu0o0](https://github.com/xu0o0)).

## [0.64.0] - 2026-03-29

### Added

- Opt-in faux provider helpers for deterministic tests and scripted demos: `registerFauxProvider()`, `fauxAssistantMessage()`, `fauxText()`, `fauxThinking()`, `fauxToolCall()`.

## [0.63.2] - 2026-03-29

No changes.

## [0.63.1] - 2026-03-27

### Added

- `gemini-3.1-pro-preview-customtools` model support for `google-vertex` provider ([#2610](https://github.com/badlogic/pi-mono/pull/2610) by [@gordonhwc](https://github.com/gordonhwc)).

### Fixed

- Context overflow detection recognizes Ollama error responses like `prompt too long; exceeded max context length...` ([#2626](https://github.com/badlogic/pi-mono/issues/2626)).

## [0.63.0] - 2026-03-27

### Breaking Changes

> [!warning]
> Removed deprecated direct `minimax` and `minimax-cn` model IDs. Use `MiniMax-M2.7` or `MiniMax-M2.7-highspeed`. ([#2596](https://github.com/badlogic/pi-mono/pull/2596) by [@liyuan97](https://github.com/liyuan97))

### Fixed

- GitHub Copilot OpenAI Responses requests omit `reasoning` field when no reasoning effort requested ([#2567](https://github.com/badlogic/pi-mono/issues/2567)).
- Google and Vertex cost calculation subtract cached prompt tokens from billable input tokens when providers report `cachedContentTokenCount` ([#2588](https://github.com/badlogic/pi-mono/pull/2588) by [@sparkleMing](https://github.com/sparkleMing)).

## [0.62.0] - 2026-03-23

### Added

- `requestMetadata` option in `BedrockOptions` for AWS cost allocation tagging ([#2511](https://github.com/badlogic/pi-mono/pull/2511) by [@wjonaskr](https://github.com/wjonaskr)).
- `BedrockOptions` type exported from package root entry point.

### Fixed

- OpenAI Responses replay normalizes oversized resumed tool call IDs before sending to Codex and other Responses-compatible targets.
- Anthropic thinking disable sends `thinking: { type: "disabled" }` for reasoning-capable models when thinking is explicitly off ([#2022](https://github.com/badlogic/pi-mono/issues/2022)).
- Explicit thinking disable handling across Google, Google Vertex, Gemini CLI, OpenAI Responses, Azure OpenAI Responses, OpenRouter-backed OpenAI-compatible completions ([#2490](https://github.com/badlogic/pi-mono/issues/2490)).
- OpenAI-compatible completions streams ignore null chunks instead of crashing ([#2466](https://github.com/badlogic/pi-mono/pull/2466) by [@Cheng-Zi-Qing](https://github.com/Cheng-Zi-Qing)).

## [0.61.1] - 2026-03-20

### Changed

- MiniMax model metadata added missing `MiniMax-M2.1-highspeed` entries for `minimax` and `minimax-cn` providers ([#2445](https://github.com/badlogic/pi-mono/pull/2445) by [@1500256797](https://github.com/1500256797)).

## [0.61.0] - 2026-03-20

### Added

- `gpt-5.4-mini` model support for `openai-codex` provider with Codex pricing metadata ([#2334](https://github.com/badlogic/pi-mono/pull/2334) by [@justram](https://github.com/justram)).

### Fixed

- `validateToolArguments()` falls back gracefully when AJV schema compilation blocked in restricted runtimes ([#2395](https://github.com/badlogic/pi-mono/issues/2395)).
- `google-vertex` API key resolution ignores placeholder auth markers like `<authenticated>` ([#2335](https://github.com/badlogic/pi-mono/issues/2335)).
- OpenRouter reasoning requests use provider's nested `reasoning.effort` payload instead of OpenAI's `reasoning_effort` ([#2298](https://github.com/badlogic/pi-mono/pull/2298) by [@PriNova](https://github.com/PriNova)).
- Bedrock prompt caching for application inference profiles allows cache points forced with `AWS_BEDROCK_FORCE_CACHE=1` ([#2346](https://github.com/badlogic/pi-mono/pull/2346) by [@haoqixu](https://github.com/haoqixu)).

## [0.60.0] - 2026-03-18

### Fixed

- Gemini 3 and Antigravity image tool results stay inline as multimodal tool responses ([#2052](https://github.com/badlogic/pi-mono/issues/2052)).
- Bedrock Claude 4.6 model metadata uses correct 200K context window ([#2305](https://github.com/badlogic/pi-mono/issues/2305)).
- Lazy built-in provider registration allows compiled Bun binaries to load providers on first use ([#2314](https://github.com/badlogic/pi-mono/issues/2314)).
- Built-in OAuth callback flows share aligned callback handling across Anthropic, Gemini CLI, Antigravity, OpenAI Codex ([#2316](https://github.com/badlogic/pi-mono/issues/2316)).
- OpenAI-compatible z.ai `network_error` responses surface as errors for caller retry ([#2313](https://github.com/badlogic/pi-mono/issues/2313)).
- OpenAI Responses replay normalizes oversized resumed tool call IDs ([#2328](https://github.com/badlogic/pi-mono/issues/2328)).

## [0.59.0] - 2026-03-17

### Added

- `client` injection support in `AnthropicOptions` for providing pre-built Anthropic-compatible client.

### Changed

- Lazy-load built-in provider modules and root provider wrappers. Importing `@mariozechner/pi-ai` no longer eagerly loads provider SDKs ([#2297](https://github.com/badlogic/pi-mono/issues/2297)).

### Fixed

- Provider-specific `responseId` support on `AssistantMessage` for Anthropic, OpenAI, Google, Gemini CLI, Mistral ([#2245](https://github.com/badlogic/pi-mono/issues/2245)).
- Claude 4.6 context window overrides in generated model metadata reflect intended values ([#2286](https://github.com/badlogic/pi-mono/issues/2286)).

## [0.58.4] - 2026-03-16

No changes.

## [0.58.3] - 2026-03-15

No changes.

## [0.58.2] - 2026-03-15

### Fixed

- Anthropic OAuth manual login and token refresh: localhost callback URI for pasted redirect/code flows, omit `scope` from refresh-token requests ([#2169](https://github.com/badlogic/pi-mono/issues/2169)).

## [0.58.1] - 2026-03-14

### Fixed

- OpenAI Codex websocket protocol includes required headers, properly terminates SSE streams on connection close ([#1961](https://github.com/badlogic/pi-mono/issues/1961)).
- Bedrock prompt caching enabled only for Claude models ([#2053](https://github.com/badlogic/pi-mono/issues/2053)).
- Qwen models via OpenAI-compatible providers use `qwen-chat-template` compat mode ([#2020](https://github.com/badlogic/pi-mono/issues/2020)).
- Bedrock unsigned thinking replay handles edge cases with empty/malformed thinking blocks ([#2063](https://github.com/badlogic/pi-mono/issues/2063)).
- `xhigh` reasoning effort detection for Claude Opus 4.6 matches by model ID ([#2040](https://github.com/badlogic/pi-mono/issues/2040)).
- Handle `finish_reason: "end"` from Ollama/LM Studio by mapping to `"stop"` ([#2142](https://github.com/badlogic/pi-mono/issues/2142)).

## [0.58.0] - 2026-03-14

### Added

- `GOOGLE_CLOUD_API_KEY` environment variable support for `google-vertex` provider as alternative to ADC ([#1976](https://github.com/badlogic/pi-mono/pull/1976) by [@gordonhwc](https://github.com/gordonhwc)).

### Changed

- Raised Claude Opus 4.6, Sonnet 4.6, and related Bedrock model context windows from 200K to 1M tokens ([#2135](https://github.com/badlogic/pi-mono/pull/2135) by [@mitsuhiko](https://github.com/mitsuhiko)).

### Fixed

- GitHub Copilot device-code login polling respects OAuth slow-down intervals, waits before first token poll ([#1956](https://github.com/badlogic/pi-mono/pull/1956) by [@drewburr](https://github.com/drewburr)).
- Usage statistics captured for OpenAI-compatible providers returning usage in `choice.usage` ([#2017](https://github.com/badlogic/pi-mono/issues/2017)).
- Tool result images sent in `function_call_output` items for OpenAI Responses API providers ([#2104](https://github.com/badlogic/pi-mono/issues/2104)).
- `openai-completions` provider sends assistant content as plain strings, not structured content blocks ([#2008](https://github.com/badlogic/pi-mono/pull/2008) by [@geraldoaax](https://github.com/geraldoaax)).
- Error details in OpenAI Responses `response.failed` handler include status code, error code, message ([#1956](https://github.com/badlogic/pi-mono/pull/1956) by [@drewburr](https://github.com/drewburr)).

## [0.57.1] - 2026-03-07

### Fixed

- Context overflow detection recognizes z.ai `model_context_window_exceeded` errors ([#1937](https://github.com/badlogic/pi-mono/issues/1937)).

## [0.57.0] - 2026-03-07

### Added

- Per-request payload inspection and replacement hook via `beforeProviderRequest`.

## [0.56.3] - 2026-03-06

### Added

- `claude-sonnet-4-6` model for `google-antigravity` provider ([#1859](https://github.com/badlogic/pi-mono/issues/1859)).
- Bumped default Antigravity User-Agent version to `1.18.4` ([#1859](https://github.com/badlogic/pi-mono/issues/1859)).

### Fixed

- Antigravity Claude thinking beta header detection uses provider and model capability instead of `-thinking` suffix ([#1859](https://github.com/badlogic/pi-mono/issues/1859)).
- OpenAI Responses reasoning replay regression fixed: reasoning blocks preserved on follow-up turns ([#1878](https://github.com/badlogic/pi-mono/issues/1878)).

## [0.56.2] - 2026-03-05

### Added

- `gpt-5.4` model support for `openai`, `openai-codex`, `azure-openai-responses`, `opencode` providers. Treated as xhigh-capable, capped to 272000 context window.
- `gpt-5.3-codex` fallback model availability for `github-copilot` ([#1853](https://github.com/badlogic/pi-mono/issues/1853)).

### Fixed

- OpenAI Responses assistant `phase` metadata (`commentary`, `final_answer`) preserved across turns by encoding `id` and `phase` in `textSignature` ([#1819](https://github.com/badlogic/pi-mono/issues/1819)).
- OpenAI Responses replay omits empty thinking blocks.
- Mistral provider switched from OpenAI-compatible completions path to Mistral's native SDK and conversations API ([#1716](https://github.com/badlogic/pi-mono/issues/1716)).
- Antigravity endpoint fallback: 403/404 responses cascade to next endpoint, added `autopush-cloudcode-pa.sandbox` endpoint, removed extra fingerprint headers ([#1830](https://github.com/badlogic/pi-mono/issues/1830)).
- `@mariozechner/pi-ai/oauth` package exports point directly at built `dist` files ([#1856](https://github.com/badlogic/pi-mono/issues/1856)).
- Gemini 3 unsigned tool call replay uses `skip_thought_signature_validator` sentinel ([#1829](https://github.com/badlogic/pi-mono/issues/1829)).

## [0.56.1] - 2026-03-05

No changes.

## [0.56.0] - 2026-03-04

### Breaking Changes

> [!warning]
> Moved Node OAuth runtime exports off top-level package entry. Import OAuth functions from `@mariozechner/pi-ai/oauth` instead of `@mariozechner/pi-ai`. ([#1814](https://github.com/badlogic/pi-mono/issues/1814))

### Added

- `gemini-3.1-flash-lite-preview` fallback model entry for `google` provider ([#1785](https://github.com/badlogic/pi-mono/issues/1785) by [@n-WN](https://github.com/n-WN)).
- OpenCode Go provider support with `opencode-go` model catalog, `OPENCODE_API_KEY` auth ([#1757](https://github.com/badlogic/pi-mono/issues/1757)).

### Changed

- Updated Antigravity Gemini 3.1 model metadata and request headers to match upstream.

### Fixed

- Gemini 3.1 thinking-level detection in `google` and `google-vertex` providers uses level-based thinking config ([#1785](https://github.com/badlogic/pi-mono/issues/1785)).
- Browser bundling failures fixed by lazy-loading Bedrock provider ([#1814](https://github.com/badlogic/pi-mono/issues/1814)).
- `ERR_VM_DYNAMIC_IMPORT_CALLBACK_MISSING` failures fixed by replacing `Function`-based dynamic imports with module dynamic imports ([#1814](https://github.com/badlogic/pi-mono/issues/1814)).
- Bedrock region resolution for `AWS_PROFILE` honors `region` from selected profile ([#1800](https://github.com/badlogic/pi-mono/issues/1800)).
- Groq Qwen3 reasoning effort mapping translates unsupported effort values ([#1745](https://github.com/badlogic/pi-mono/issues/1745)).

## [0.55.4] - 2026-03-02

No changes.

## [0.55.3] - 2026-02-27

No changes.

## [0.55.2] - 2026-02-27

### Fixed

- Restored built-in OAuth providers when unregistering dynamically registered provider IDs. Added `resetOAuthProviders()`.
- Z.ai thinking control uses `enable_thinking` parameter name correctly ([#1674](https://github.com/badlogic/pi-mono/pull/1674) by [@okuyam2y](https://github.com/okuyam2y)).
- `redacted_thinking` blocks captured as `ThinkingContent` with `redacted: true` ([#1665](https://github.com/badlogic/pi-mono/pull/1665) by [@tctev](https://github.com/tctev)).
- `interleaved-thinking-2025-05-14` beta header not sent for adaptive thinking models (Opus 4.6, Sonnet 4.6) ([#1665](https://github.com/badlogic/pi-mono/pull/1665) by [@tctev](https://github.com/tctev)).
- Temperature not sent alongside extended thinking ([#1665](https://github.com/badlogic/pi-mono/pull/1665) by [@tctev](https://github.com/tctev)).
- `(external, cli)` user-agent flag no longer causes 401 errors on Anthropic setup-token endpoint ([#1677](https://github.com/badlogic/pi-mono/pull/1677) by [@LazerLance777](https://github.com/LazerLance777)).
- Crash fixed when OpenAI-compatible provider returns chunk with no `choices` array ([#1671](https://github.com/badlogic/pi-mono/issues/1671)).

## [0.55.1] - 2026-02-26

### Added

- `gemini-3.1-pro-preview` model support for `google-gemini-cli` provider ([#1599](https://github.com/badlogic/pi-mono/pull/1599) by [@audichuang](https://github.com/audichuang)).

### Fixed

- Adaptive thinking for Claude Sonnet 4.6 in Anthropic and Bedrock providers; `xhigh` effort values clamped to supported levels ([#1548](https://github.com/badlogic/pi-mono/pull/1548) by [@tctev](https://github.com/tctev)).
- Vertex ADC credential detection race avoided by not caching false negative during async import initialization ([#1550](https://github.com/badlogic/pi-mono/pull/1550) by [@jeremiahgaylord-web](https://github.com/jeremiahgaylord-web)).

## [0.55.0] - 2026-02-24

No changes.

## [0.54.2] - 2026-02-23

No changes.

## [0.54.1] - 2026-02-22

No changes.

## [0.54.0] - 2026-02-19

No changes.

## [0.53.1] - 2026-02-19

No changes.

## [0.53.0] - 2026-02-17

### Added

- Anthropic `claude-sonnet-4-6` fallback model entry to generated model definitions.

## [0.52.12] - 2026-02-13

### Added

- `transport` in `StreamOptions` with values `"sse"`, `"websocket"`, `"auto"` (supported by `openai-codex-responses`).
- WebSocket transport support for OpenAI Codex Responses (`openai-codex-responses`).

### Changed

- OpenAI Codex Responses defaults to SSE transport unless `transport` explicitly set.
- OpenAI Codex Responses WebSocket connections cached per `sessionId`, expire after 5 minutes idle.

## [0.52.11] - 2026-02-13

### Added

- MiniMax M2.5 model entries for `minimax`, `minimax-cn`, `openrouter`, `vercel-ai-gateway` providers; `minimax-m2.5-free` for `opencode`.

## [0.52.10] - 2026-02-12

### Added

- Optional `metadata` field in `StreamOptions` for provider-specific metadata ([#1384](https://github.com/badlogic/pi-mono/pull/1384) by [@7Sageer](https://github.com/7Sageer)).
- `gpt-5.3-codex-spark` model definition (128k context, text-only, research preview).

### Changed

- GitHub Copilot Claude 4.x models routed through Anthropic Messages API; centralized Copilot dynamic header handling ([#1353](https://github.com/badlogic/pi-mono/pull/1353) by [@NateSmyth](https://github.com/NateSmyth)).

### Fixed

- OpenAI completions and responses streams tolerate malformed trailing tool-call JSON ([#1424](https://github.com/badlogic/pi-mono/issues/1424)).

## [0.52.9] - 2026-02-08

### Changed

- Updated Antigravity system instruction to more compact version.

### Fixed

- `parametersJsonSchema` for Google provider tool declarations supports full JSON Schema ([#1398](https://github.com/badlogic/pi-mono/issues/1398) by [@jarib](https://github.com/jarib)).
- Reverted incorrect Antigravity model change: `claude-opus-4-6-thinking` back to `claude-opus-4-5-thinking`.
- Corrected opencode context windows for Claude Sonnet 4 and 4.5 ([#1383](https://github.com/badlogic/pi-mono/issues/1383)).

## [0.52.8] - 2026-02-07

### Added

- OpenRouter `auto` model alias for automatic model routing ([#1361](https://github.com/badlogic/pi-mono/pull/1361) by [@yogasanas](https://github.com/yogasanas)).

### Changed

- Replaced Claude Opus 4.5 with Opus 4.6 in model definitions ([#1345](https://github.com/badlogic/pi-mono/pull/1345) by [@calvin-hpnet](https://github.com/calvin-hpnet)).

## [0.52.7] - 2026-02-06

### Added

- `AWS_BEDROCK_SKIP_AUTH` and `AWS_BEDROCK_FORCE_HTTP1` environment variables for unauthenticated Bedrock proxies ([#1320](https://github.com/badlogic/pi-mono/pull/1320) by [@virtuald](https://github.com/virtuald)).

### Fixed

- Set OpenAI Responses API requests to `store: false` by default ([#1308](https://github.com/badlogic/pi-mono/issues/1308)).
- Re-exported TypeBox `Type`, `Static`, `TSchema` from `@mariozechner/pi-ai` ([#1338](https://github.com/badlogic/pi-mono/issues/1338)).
- Bedrock adaptive thinking handling for Claude Opus 4.6 with interleaved thinking beta responses ([#1323](https://github.com/badlogic/pi-mono/pull/1323) by [@markusylisiurunen](https://github.com/markusylisiurunen)).
- `AWS_BEDROCK_SKIP_AUTH` environment detection avoids `process` access in non-Node.js environments.

## [0.52.6] - 2026-02-05

No changes.

## [0.52.5] - 2026-02-05

### Fixed

- `supportsXhigh()` treats Anthropic Messages Opus 4.6 models as xhigh-capable for `streamSimple` mapping.

## [0.52.4] - 2026-02-05

No changes.

## [0.52.3] - 2026-02-05

### Fixed

- Bedrock Opus 4.6 model IDs: removed `:0` suffix; fixed cache pricing for `us.*`/`eu.*` variants.
- Added missing `eu.anthropic.claude-opus-4-6-v1` inference profile to model catalog.
- Claude Opus 4.6 context window metadata set to 200000 for Anthropic and OpenCode providers.

## [0.52.2] - 2026-02-05

No changes.

## [0.52.1] - 2026-02-05

### Added

- Adaptive thinking support for Claude Opus 4.6 with effort levels (`low`, `medium`, `high`, `max`).
- `effort` option in `AnthropicOptions` for controlling adaptive thinking depth.
- `thinkingEnabled` automatically uses adaptive thinking for Opus 4.6+ models.
- `streamSimple`/`completeSimple` map `ThinkingLevel` to effort levels for Opus 4.6.

### Changed

- Updated `@anthropic-ai/sdk` to 0.73.0.
- Updated `@aws-sdk/client-bedrock-runtime` to 3.983.0.
- Updated `@google/genai` to 1.40.0.
- Removed `fast-xml-parser` override.

## [0.52.0] - 2026-02-05

### Added

- Claude Opus 4.6 model to generated model catalog.
- GPT-5.3 Codex model to generated model catalog (OpenAI Codex provider only).

## [0.51.6] - 2026-02-04

### Fixed

- OpenAI Codex Responses provider respects configured baseUrl ([#1244](https://github.com/badlogic/pi-mono/issues/1244)).

## [0.51.5] - 2026-02-04

### Changed

- Bedrock model generation drops legacy workarounds now handled upstream ([#1239](https://github.com/badlogic/pi-mono/pull/1239) by [@unexge](https://github.com/unexge)).

## [0.51.4] - 2026-02-03

No changes.

## [0.51.3] - 2026-02-03

### Fixed

- `xhigh` thinking level support check accepts gpt-5.2 model IDs ([#1209](https://github.com/badlogic/pi-mono/issues/1209)).

## [0.51.2] - 2026-02-03

No changes.

## [0.51.1] - 2026-02-02

### Fixed

- `cache_control` applied to string-format user messages in Anthropic provider.

## [0.51.0] - 2026-02-01

### Fixed

- `cacheRetention` option passed through in `buildBaseOptions` ([#1154](https://github.com/badlogic/pi-mono/issues/1154)).
- OAuth login/refresh uses HTTP proxy settings (`HTTP_PROXY`, `HTTPS_PROXY` env vars) ([#1132](https://github.com/badlogic/pi-mono/issues/1132)).
- OpenAI-compatible completions omit unsupported `strict` tool fields ([#1172](https://github.com/badlogic/pi-mono/issues/1172)).

## [0.50.9] - 2026-02-01

### Added

- `PI_AI_ANTIGRAVITY_VERSION` environment variable to override Antigravity User-Agent version ([#1129](https://github.com/badlogic/pi-mono/issues/1129)).
- `cacheRetention` stream option with provider-specific mappings for prompt cache controls ([#1134](https://github.com/badlogic/pi-mono/issues/1134)).

## [0.50.8] - 2026-02-01

### Added

- `google-antigravity` provider: Gemini CLI integration with OAuth and API key auth.
- `openai-codex-responses` provider: OpenAI Codex Responses API integration.
- `github-copilot` provider: GitHub Copilot integration via OAuth.

### Fixed

- `openai-responses` provider respects configured baseUrl for non-`api.openai.com` endpoints.
- Google provider uses `parametersJsonSchema` for tool declarations to support full JSON Schema.

## [0.50.7] - 2026-01-31

### Added

- Anthropic `claude-opus-4-5-thinking` model support for reasoning workloads.
- `openai-responses` transport option with values `"sse"` and `"auto"` (WebSocket with cached context).

### Changed

- OpenAI Codex Responses defaults to `auto` transport with cached WebSocket context.
- Anthropic SSE parsing ignores unknown proxy events (e.g. OpenAI-style `done` terminators).

### Fixed

- `supportsXhigh()` recognizes DeepSeek V4 Pro, preserving `xhigh` reasoning.
- OpenAI-compatible DeepSeek V4 model replay includes empty `reasoning_content` on assistant messages.
- `tools: []` no longer sent when no tools active (DashScope rejects with HTTP 400).
- Bedrock prompt-caching and adaptive-thinking checks normalize profile ARNs to model names.

## [0.50.6] - 2026-01-30

### Fixed

- API-key environment discovery falls back to `/proc/self/environ` when Bun's sandbox empties `process.env`.
- Anthropic OAuth manual login uses localhost callback URI for pasted redirect/code flows.

## [0.50.5] - 2026-01-29

### Added

- Cloudflare AI Gateway provider with OpenAI, Anthropic, Workers AI routing.
- Cloudflare Workers AI provider with OpenAI-compatible streaming.

### Fixed

- `transformMessages()` synthesizes missing trailing tool results for unresolved assistant tool calls.
- Google Vertex Gemini 3 tool call replay stops sending `skip_thought_signature_validator` sentinel.

## [0.50.4] - 2026-01-28

### Added

- DeepSeek as built-in OpenAI-compatible provider (V4 Flash, V4 Pro).
- `thinkingFormat: "deepseek"` and `requiresReasoningContentOnAssistantMessages` compat for DeepSeek V4.

### Fixed

- DeepSeek V4 session replay 400 errors fixed with proper reasoning effort mapping.
- OpenAI Codex service-tier accounting trusts explicitly requested tier.

## [0.50.3] - 2026-01-27

### Added

- `AWS_BEARER_TOKEN_BEDROCK` for Bedrock Converse bearer-token authentication.
- Fireworks provider via Anthropic-compatible Messages API.

### Fixed

- `cache_control` breakpoint added on last tool definition for Anthropic prompt caching.
- Mistral Small 4 reasoning uses `reasoning_effort` instead of `prompt_mode`.

## [0.50.2] - 2026-01-26

### Fixed

- Non-vision model requests replace image blocks with text placeholders.
- OpenAI-compatible Chat Completions Anthropic-style prompt caching via `compat.cacheControlFormat`.

## [0.50.1] - 2026-01-25

### Added

- `thinkingDisplay` (`"summarized" | "omitted"`) in `AnthropicOptions`/`BedrockOptions`.
- `onResponse` callback in `StreamOptions` for inspecting provider HTTP status/headers.

### Fixed

- OpenAI Responses prompt caching sends session headers for non-`api.openai.com` base URLs.
- Bedrock bearer-token auth uses SDK's native token auth path.

## [0.50.0] - 2026-01-24

### Breaking Changes

> [!warning]
> TypeBox migration: `@sinclair/typebox` + AJV → `typebox` 1.x + TypeBox validator. Install and import from `typebox`. ([#3112](https://github.com/badlogic/pi-mono/issues/3112))

### Added

- Claude Opus 4.6 adaptive thinking with effort levels.
- `thinkingLevelMap`, `getSupportedThinkingLevels()`, `clampThinkingLevel()`.

### Fixed

- Gemini 3.1 thinking-level detection uses level-based thinking config.
- `google-vertex` API key resolution treats `gcp-vertex-credentials` as ADC marker.

## [0.49.x] - 2026-01

*(Earlier releases: see git history for detailed changelog)*

# Tags

#changelog #api-integration #breaking-changes #ai-models #software-updates #provider-configuration
