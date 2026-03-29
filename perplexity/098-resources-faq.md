---
title: Frequently Asked Questions
url: https://docs.perplexity.ai/docs/resources/faq.md
source: llms
fetched_at: 2026-02-04T07:24:41.046561966-03:00
rendered_js: false
word_count: 274
summary: This document provides answers to frequently asked questions regarding the Perplexity API, covering technical specifications, billing tiers, data privacy, and compatibility with OpenAI's interface.
tags:
    - faq
    - perplexity-api
    - billing-tiers
    - openai-compatibility
    - data-privacy
    - rate-limits
    - error-handling
    - reasoning-models
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Why isn't the `response_format` parameter working for reasoning models?">
    The `sonar-reasoning-pro` model is designed to output a `<think>` section containing reasoning tokens, immediately followed by a valid JSON object. As a result, the `response_format` parameter does not remove these reasoning tokens from the output.

    We recommend using a custom parser to extract the valid JSON portion. An example implementation can be found [here](https://github.com/ppl-ai/api-discussion/blob/main/utils/extract_json_reasoning_models.py).
  </Accordion>

  <Accordion title="Does the API use content filtering or SafeSearch?">
    Yes, for the API, content filtering in the form of SafeSearch is turned on by default. This helps filter out potentially offensive and inappropriate content, including pornography, from search results. SafeSearch is an automated filter that works across search results to provide a safer experience. You can learn more about SafeSearch on the [official Wikipedia page](https://en.wikipedia.org/wiki/SafeSearch).
  </Accordion>

  <Accordion title="How do I file a bug report and what happens afterward?">
    To file a bug report, please use our GitHub repository and file the bug in [issues](https://github.com/ppl-ai/api-discussion/issues). Once you've submitted your report, we kindly ask that you share the link to the issue with us via email at [api@perplexity.ai](mailto:api@perplexity.ai) so we can track it on our end.

    We truly appreciate your patience, and we'll get back to you as soon as possible. Due to the current volume of reports, it may take a little time for us to respond—but rest assured, we're on it.
  </Accordion>

  <Accordion title="Where are Perplexity's language models hosted?">
    Our compute is hosted via Amazon Web Services in North America. By default, the API has zero day retention of user prompt data, which is never used for AI training.
  </Accordion>

  <Accordion title="How can I upgrade to the next usage tier?">
    The only way for an account to be upgraded to the next usage tier is through all-time credit purchase.

    Here are the spending criteria associated with each tier:

    | Tier   | Credit Purchase (all time) |
    | ------ | -------------------------- |
    | Tier 0 | -                          |
    | Tier 1 | \$50                       |
    | Tier 2 | \$250                      |
    | Tier 3 | \$500                      |
    | Tier 4 | \$1000                     |
    | Tier 5 | \$5000                     |
  </Accordion>

  <Accordion title="How can I track my spend/usage per API key?">
    We offer a way to track your billing per API key. You can do this by navigating to the following location:

    **Settings > View Dashboard > Invoice history > Invoices**

    Then click on any invoice and each item from the total bill will have a code at the end of it (e.g., pro (743S)). Those 4 characters are the last 4 of your API key.
  </Accordion>

  <Accordion title="How do I request a new feature?">
    A Feature Request is a suggestion to improve or add new functionality to the Perplexity Sonar API, such as:

    * Requesting support for a new model or capability (e.g., image processing, fine-tuning options)
    * Asking for new API parameters (e.g., additional filters, search options)
    * Suggesting performance improvements (e.g., faster response times, better citation handling)
    * Enhancing existing API features (e.g., improving streaming reliability, adding new output formats)

    If your request aligns with these, please submit a feature request here: [Github Feature requests](https://github.com/ppl-ai/api-discussion/issues)
  </Accordion>

  <Accordion title="Why are the results from the API different from the UI? ">
    1. The API uses the same search system as the UI with differences in configuration—so their outputs may differ.
    2. The underlying AI model might differ between the API and the UI for a given query.
  </Accordion>

  <Accordion title="Will user data submitted through the API be used for model training or other purposes?">
    We collect the following types of information:

    **API Usage Data:** We collect billable usage metadata such as the number of requests and tokens. You can view your own usage in the [Perplexity API dashboard](https://perplexity.ai/settings/api).

    **User Account Information:** When you create an account with us, we collect your name, email address, and other relevant contact information.

    We do not retain any query data sent through the API and do not train on any of your data.
  </Accordion>

  <Accordion title="Does the API currently support web browsing?">
    Yes, the [Sonar Models](https://docs.perplexity.ai/guides/model-cards) leverage information from Perplexity's search index and the public internet.
  </Accordion>

  <Accordion title="What are the limitations to the number of API calls?">
    You can find our [rate limits here](https://docs.perplexity.ai/guides/usage-tiers).
  </Accordion>

  <Accordion title="What's the best way to stay up to date with API updates?">
    We email users about new developments and also post in the [changelog](changelog/changelog).
  </Accordion>

  <Accordion title="How should I respond to 401: Authorization errors?">
    401 error codes indicate that the provided API key is invalid, deleted, or belongs to an account which ran out of credits. You likely need to purchase more credits in the [Perplexity API dashboard](https://perplexity.ai/settings/api). You can avoid this issue by configuring auto-top-up.
  </Accordion>

  <Accordion title="Do you support fine-tuning?">
    Currently, we do not support fine-tuning.
  </Accordion>

  <Accordion title="I have another question or an issue">
    Please reach out to [api@perplexity.ai](mailto:api@perplexity.ai) or [support@perplexity.ai](mailto:support@perplexity.ai) for other API inquiries. You can also post on our [discussion forum](https://github.com/ppl-ai/api-discussion/discussions) and we will get back to you.
  </Accordion>

  <Accordion title="Does Perplexity provide service quality assurances such as service uptime, frequency of failures, and target recovery time in the event of a failure?">
    We do not guarantee this at the moment.
  </Accordion>

  <Accordion title="Do you expose CoTs if I use your reasoning APIs or Deep Research API?">
    We expose the CoTs for Sonar Reasoning Pro. We don't currently expose the CoTs for Deep Research.
  </Accordion>

  <Accordion title="Are the reasoning tokens in Deep Research same as CoTs in the answer?">
    Reasoning tokens in Deep Research are a bit different than the CoTs in the answer—these tokens are used to reason through the research material before generating the final output via the CoTs.
  </Accordion>

  <Accordion title="Is the internet data access provided by the API identical to that of Perplexity's web interface?">
    Yes, the API offers exactly the same internet data access as Perplexity's web platform.
  </Accordion>

  <Accordion title="To what extent is the API OpenAI compatible?">
    The Perplexity API is designed to be broadly compatible with OpenAI's chat completions endpoint. It adopts a similar structure—including fields such as `id`, `model`, and `usage`—and supports analogous parameters like `model`, `messages`, and `stream`.

    **Key Differences from the standard OpenAI response include:**

    * **Response Object Structure:**
      * OpenAI responses typically have an `object` value of `"chat.completion"` and a `created` timestamp, whereas our response uses `object: "response"` and a `created_at` field.
      * Instead of a `choices` array, our response content is provided under an `output` array that contains detailed message objects.

    * **Message Details:**
      * Each message in our output includes a `type` (usually `"message"`), a unique `id`, and a `status`.
      * The actual text is nested within a `content` array that contains objects with `type`, `text`, and an `annotations` array for additional context.

    * **Additional Fields:**
      * Our API response provides extra meta-information (such as `status`, `error`, `instructions`, and `max_output_tokens`) that are not present in standard OpenAI responses.
      * The `usage` field also differs, offering detailed breakdowns of input and output tokens (including fields like `input_tokens_details` and `output_tokens_details`).

    These differences are intended to provide enhanced functionality and additional context while maintaining broad compatibility with OpenAI's API design.
  </Accordion>
</AccordionGroup>