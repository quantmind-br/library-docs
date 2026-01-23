---
title: Guardrail Testing Playground | liteLLM
url: https://docs.litellm.ai/docs/proxy/guardrails/test_playground
source: sitemap
fetched_at: 2026-01-21T19:52:38.633177745-03:00
rendered_js: false
word_count: 221
summary: This document provides instructions on how to use the LiteLLM Guardrail Testing Playground to compare multiple guardrail responses and validate security configurations in real-time.
tags:
    - litellm
    - guardrails
    - security-testing
    - playground
    - llm-security
    - configuration-validation
category: guide
---

Test and compare multiple guardrails in real-time with an interactive playground interface.

## How to Use the Guardrail Testing Playground[​](#how-to-use-the-guardrail-testing-playground "Direct link to How to Use the Guardrail Testing Playground")

The Guardrail Testing Playground allows you to quickly test and compare the behavior of different guardrails with sample inputs.

### Steps to Test Guardrails[​](#steps-to-test-guardrails "Direct link to Steps to Test Guardrails")

1. **Navigate to the Guardrails Section**
   
   - Open the LiteLLM Admin UI
   - Go to the **Guardrails** section
2. **Open Test Playground**
   
   - Click on the **Test Playground** tab at the top of the page
3. **Select Guardrails to Test**
   
   - Check the guardrails you want to compare
   - You can select multiple guardrails to see how they each respond to the same input
4. **Enter Your Input**
   
   - Type or paste your test input in the text area
   - This could be a prompt, message, or any text you want to validate against the guardrails
5. **Run the Test**
   
   - Click the **Test guardrails** button (or press Enter)
6. **View Results**
   
   - See the output from each selected guardrail
   - Compare how different guardrails handle the same input
   - Results will show whether the input passed or was blocked by each guardrail

## Use Cases[​](#use-cases "Direct link to Use Cases")

This is ideal for **Security Teams** & **LiteLLM Admins** evaluating guardrail solutions.

This brings the following benefits for LiteLLM users:

- **Compare guardrail responses**: test the same prompt across multiple providers (Lakera, Noma AI, Bedrock Guardrails, etc.) simultaneously.
- **Validate configurations**: verify your guardrails catch the threats you care about before production deployment.