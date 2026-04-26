---
title: Changelog | Mistral Docs
url: https://docs.mistral.ai/resources/changelogs
source: sitemap
fetched_at: 2026-04-26T04:11:20.889786411-03:00
rendered_js: false
word_count: 1382
summary: This document provides a comprehensive chronological record of platform updates, including new model releases, API enhancements, security patches, and SDK developments.
tags:
    - release-notes
    - model-updates
    - api-changes
    - platform-changelog
    - software-versioning
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Find out about all the latest changes to our tool. You may filter by date and type of release.

## March 22

- We released Voxtral TTS (`voxtral-tts-2603`), our state-of-the-art text-to-speech model with zero-shot voice cloning, multilingual support, and real-time streaming. MODEL RELEASED

## March 15

- We released Mistral Small 4 (`mistral-small-2603`), a hybrid model unifying instruct, reasoning, and coding in a single multimodal model with a 256k context window. MODEL RELEASED
- We released Leanstral (`labs-leanstral-2603`), our first open-source code agent designed for Lean 4 formal proof engineering. MODEL RELEASED

## March 11

- We released Mistral Moderation 2603 (`mistral-moderation-2603`). MODEL RELEASED
- We added [Custom Guardrails](https://docs.mistral.ai/studio-api/safety-moderation#custom-guardrails) support for Agents and Conversations. API UPDATED
  - Guardrails can now be configured directly on an Agent via the `guardrails` parameter.
  - Guardrails can be passed per-request on `POST /v1/conversations` using the `guardrails` field.
  - Guardrails can be passed per-request on `POST /v1/chat/completions` using the `guardrails` field.

## February 3

- We released Voxtral Mini Transcribe 2 (`voxtral-mini-2602`) and Voxtral Mini Transcribe Realtime (`voxtral-mini-transcribe-realtime-2602`). MODEL RELEASED
  - Introducing `context biasing` in our Audio Transcriptions API.
  - Introducing `diarize`in our Audio Transcriptions API.

## January 26

- We released Vibe 2.0. OTHER
  - Devstral 2.0 moves to paid API access. MODEL RELEASED
- Document Annotations update and improvements, 8 page limit removed. API UPDATED

## January 18

- We released inline batching allowing the creation of batch jobs without file uploading. API UPDATED

## December 17

- We released OCR 3 (`mistral-ocr-2512`). MODEL RELEASED
  - Introducing `table_format` in our OCR API, allowing you to choose between `markdown` and `html` for table formatting. API UPDATED
  - Introducing `extract_footer`, `extract_header` in our OCR API, as well as `hyperlinks` output. API UPDATED

## December 15

- We released Mistral Small Creative (`labs-mistral-small-creative`) as a Labs model. MODEL RELEASED

## December 8

- We released Devstral 2 (`devstral-2512`) and Devstral Small 2 (`labs-devstral-small-2512`). MODEL RELEASED
- We released Mistral Vibe. OTHER

## December 1

- We released Mistral Large 3 (`mistral-large-2512`) and Ministral 3 (`ministral-3b-2512`, `ministral-8b-2512` and `ministral-14b-2512`). MODEL RELEASED

## September 16

- We released Magistral Medium 1.2 (`magistral-medium-2509`) and Magistral Small 1.2 (`magistral-small-2509`). MODEL RELEASED

## August 26

- Added a new parameter `p` to the chunks streamed back by the Completion API. SECURITY API UPDATED
  - Implemented for security to prevent token-length side-channel attacks, as reported by Microsoft researchers.
  - Note that this change may break applications relying on strict parsing of the chunks. Applications using the official SDK are unaffected, but users relying on the `mistral-common` package may need to update to `1.8.4` or higher.

## August 11

- We released Mistral Medium 3.1 (mistral-medium-2508). MODEL RELEASED

## July 29

- We released Codestral 2508 (`codestral-2508`). MODEL RELEASED

## July 23

- We released Magistral Medium 1.1 (`magistral-medium-2507`) and Magistral Small 1.1 (`magistral-small-2507`). MODEL RELEASED
- We released a Document Library API to manage libraries. API UPDATED
- SDK support for Audio and Transcription available. OTHER

## July 14

- We released our first Audio models for chat and a Transcription API:
  - Voxtral Small (`voxtral-small-2507`) available for chat use cases MODEL RELEASED
  - Voxtral Mini (`voxtral-mini-2507`) available for chat use cases MODEL RELEASED
  - Voxtral Mini Transcribe (`voxtral-mini-2507` via `audio/transcriptions`) optimized for transcription MODEL RELEASED API UPDATED

## July 9

- We released Devstral Small 1.1 (`devstral-small-2507`) and Devstral Medium (`devstral-medium-2507`). MODEL RELEASED

## June 22

- Mistral Small 3.2 API available (`mistral-small-2506`). API UPDATED

## June 19

- We released Mistral Small 3.2. MODEL RELEASED

## June 9

- We released Magistral Medium (`magistral-medium-2506`) and Magistral Small (`magistral-small-2506`). MODEL RELEASED

## May 27

- We released Codestral Embed (`codestral-embed`). MODEL RELEASED

## May 26

- We released the new [Agents API](https://docs.mistral.ai/studio-api/agents/introduction). API UPDATED

## May 21

- We released Mistral OCR 2 (`mistral-ocr-2505`) and [annotations](https://docs.mistral.ai/studio-api/document-processing/annotations). MODEL RELEASED API UPDATED

## May 20

- We released Devstral Small (`devstral-small-2505`). MODEL RELEASED

## May 6

- We released Mistral Medium 3 (`mistral-medium-2505`). MODEL RELEASED

## March 16

- We released Mistral Small 3.1 (`mistral-small-2503`). MODEL RELEASED

## March 5

- We released Mistral OCR (`mistral-ocr-2503`) and [document understanding](https://docs.mistral.ai/studio-api/document-processing/basic_ocr). MODEL RELEASED API UPDATED

## February 16

- We released Mistral Saba (`mistral-saba-2502`). MODEL RELEASED

## January 29

- We released Mistral Small 3 (`mistral-small-2501`). MODEL RELEASED

## January 12

- We released Codestral 2501 (`codestral-2501`). MODEL RELEASED

## November 17

- We released Mistral Large 2.1 (`mistral-large-2411`) and Pixtral Large (`pixtral-large-2411`). MODEL RELEASED
- [Le Chat](https://chat.mistral.ai/): OTHER
  - Web search with citations
  - Canvas for ideation, in-line editing, and export
  - State of the art document and image understanding, powered by the new multimodal Pixtral Large
  - Image generation, powered by Black Forest Labs Flux Pro
  - Fully integrated offering, from models to outputs
  - Faster responses powered by speculative editing

## November 5

- We released moderation API and batch API. MODEL RELEASED API UPDATED
- We introduced three new parameters: API UPDATED
  - `presence_penalty`: penalizes the repetition of words or phrases
  - `frequency_penalty`: penalizes the repetition of words based on their frequency in the generated text
  - `n`: number of completions to return for each request, input tokens are only billed once.
- We downscaled the temperature parameter of `pixtral-12b`, `ministral-3b-2410`, and `ministral-8b-2410` by a multiplier of 0.43 to improve consistency, quality, and unify model behavior. API UPDATED

## October 8

- We released Ministral 3B (`ministral-3b-2410`) and Ministral 8B (`ministral-8b-2410`). MODEL RELEASED

## September 16

- We released Pixtral (`pixtral-12b-2409`) and Mistral Small v24.09 (`mistral-small-2409`). MODEL RELEASED
- We reduced price on our flagship model, Mistral Large 2. API UPDATED
- We introduced a free API tier on La Plateforme. API UPDATED

## September 12

- In le Chat, we added a mitigation against an obfuscated prompt method that could lead to data exfiltration, reported by researchers [Xiaohan Fu](https://xhfu.me/) and Earlence Fernandes. The attack required users to willingfully copy and paste adversarial prompts and provide personal data to the model. No user was impacted and no data was exfiltrated. SECURITY

## July 28

- We released version 1.0 of our Python and JS SDKs with major upgrades and syntax changes. Check out our [migration guide](https://github.com/mistralai/client-python/blob/main/MIGRATION.md) for details. OTHER
- We released Agents API. See details [here](https://docs.mistral.ai/studio-api/agents/introduction). API UPDATED

## July 23

- We released Mistral Large 2 (`mistral-large-2407`). MODEL RELEASED
- We added fine-tuning support for Codestral, Mistral Nemo and Mistral Large. Now the model choices for fine-tuning are `open-mistral-7b` (v0.3), `mistral-small-latest` (`mistral-small-2402`), `codestral-latest` (`codestral-2405`), `open-mistral-nemo` and , `mistral-large-latest` (`mistral-large-2407`) API UPDATED

## July 17

- We released Mistral Nemo (`open-mistral-nemo`). MODEL RELEASED

## July 15

- We released Codestral Mamba (`open-codestral-mamba`) and Mathstral. MODEL RELEASED

## June 4

- We released fine-tuning API. Check out the [capability docs](https://docs.mistral.ai/resources/deprecated/finetuning) and [guides](https://docs.mistral.ai/resources/deprecated/finetuning). API UPDATED

## May 28

- New model available: `codestral-latest` (aka `codestral-2405`). Check out the code generation [docs](https://docs.mistral.ai/mistral-vibe/using-fim-api). MODEL RELEASED API UPDATED

## May 22

- Function calling: `tool_call_id` is now mandatory in chat messages with the `tool` role. API UPDATED

## April 16

- New model available: `open-mixtral-8x22b` (aka `open-mixtral-8x22b-2404`). Check the release [blog](https://mistral.ai/news/mixtral-8x22b/) for details. MODEL RELEASED
  - For function calling, `tool_call_id` must not be null for `open-mixtral-8x22b`. OTHER
- We released three versions of tokenizers for commercial and open-weight models: check the related [guide](https://github.com/mistralai/mistral-common) and [repo](https://github.com/mistralai/mistral-common) for more details. OTHER

## March 27

- JSON mode now available for all models on La Plateforme. API UPDATED

## February 25

- API endpoints: We renamed 3 API endpoints and added 2 model endpoints. API UPDATED
  - `open-mistral-7b` (aka `mistral-tiny-2312`): renamed from `mistral-tiny`. The endpoint `mistral-tiny` will be deprecated in three months.
  - `open-mixtral-8x7B` (aka `mistral-small-2312`): renamed from `mistral-small`. The endpoint `mistral-small` will be deprecated in three months.
  - `mistral-small-latest` (aka `mistral-small-2402`): new model. MODEL RELEASED
  - `mistral-medium-latest` (aka `mistral-medium-2312`): old model. The previous `mistral-medium` has been dated and tagged as `mistral-medium-2312`. The endpoint `mistral-medium` will be deprecated in three months.
  - `mistral-large-latest` (aka `mistral-large-2402`): our new flagship model with leading performance. MODEL RELEASED
- New API capabilities: API UPDATED
  - [Function calling](https://docs.mistral.ai/studio-api/conversations/function-calling): available for Mistral Small and Mistral Large.
  - [JSON mode](https://docs.mistral.ai/studio-api/conversations/structured-output#json-mode): available for Mistral Small and Mistral Large
- [La Plateforme](https://console.mistral.ai/): OTHER
  - We added multiple currency support to the payment system, including the option to pay in US dollars.
  - We introduced enterprise platform features including admin management, which allows users to manage individuals from your organization.
- [Le Chat](https://chat.mistral.ai/): OTHER
  - We introduced the brand new chat interface Le Chat to easily interact with Mistral models.
  - You can currently interact with three models: Mistral Large, Mistral Next, and Mistral Small.

## January 15

- We added token usage information in streaming requests. You can find it in the last chunk returned. API UPDATED

## January 10

- We have enhanced the API's strictness. Previously the API would silently ignores unsupported parameters in the requests, but it now strictly enforces the validity of all parameters. If you have unsupported parameters in your request, you will see the error message "Extra inputs are not permitted". API UPDATED
- A previous version of the [guardrailing documentation](https://docs.mistral.ai/studio-api/safety-moderation) incorrectly referred to the API parameter as `safe_mode` instead of `safe_prompt`. We corrected this in the documentation. OTHER