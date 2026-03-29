---
title: Demystifying Mistral's Instruct Tokenization & Chat Templates - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-chat_templates
source: crawler
fetched_at: 2026-01-29T07:34:53.665282943-03:00
rendered_js: false
word_count: 2126
summary: This document explains the technical evolution and implementation details of Mistral AI's tokenizer versions, from V1 to Tekken, focusing on instruction following and chat templates.
tags:
    - mistral-ai
    - tokenization
    - chat-templates
    - instruction-tuning
    - llm-development
category: concept
---

> \[!IMPORTANT] This document is deprecated. Please take a look at the full, in-depth documentation [here](https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-readme).

From the original tokenizer V1 to the most recent V3 and Tekken tokenizers, Mistral's tokenizers have undergone subtle changes related to how to tokenize for the instruct models. We've come a long way in optimization and research to find the best approach. Today, we'll delve into these tokenizers, demystify any sources of debate, and explore how they work, the proper chat templates to use for each one, and their story within the community!

In this article, we will mostly delve into instruction tokenization and chat templates for simple instruction following. We won't dig into function calling or fill in the middle.

The ground truth for all the information available here can be found by exploring the repos on hugging face as well as on github, specifically [mistral\_common](https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-chat_templates).

### Tokenizer V1:

With mistral-common, the system prompt is prepended to the first user message by default (feel free to customise it)

### Tokenizer V2:

With mistral-common, the system prompt is prepended to the last user message by default (feel free to customise it)

**FIM**

### Tokenizer V3:

V3 is highly similar to V2, the only difference concerns function calling.

**FIM**

### Tokenizer V3 - Tekken (Nemo):

With mistral-common, the system prompt is prepended to the last user message by default (feel free to customise it)

EDIT: New document explaining can be found in our [cookbooks](https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-chat_templates)

## Tokenizer V1

The very first releases, Mistral 7B V1 and V2 as well as Mixtral 8x7B V1, were met with a lot of appreciation and love from the community. However, this did not prevent some disagreements and debates within the community regarding the correct chat templates for the instruct tokenizers. Today, you can reliably rely on `mistral_common` as the ground truth for the tokenization process, but back then, most of the community relied on the available Jinja chat templates!

The community was very quick to notice inconsistencies around the tokenizers and the chat templates, achieving better results with custom versions that adjusted the whitespaces surrounding special strings. It's amazing how the community is very fast and helpful in detecting any issues and bugs related to the models!

The tokenizer used for these first releases, based on `sentencepiece`, uses a similar template to the old Llama models. This tokenizer deals with instruct messages as follows:

### Instruct Chat Template

The chat template was, as previously mentioned, highly similar to the first Llama template, and would result in strings like the following.

Here, the only special strings were `[INST]` to start the user message and `[/INST]` to end the user message, making way for the assistant's response. The BOS (beginning of string) was and still is represented with `<s>`, and the EOS (end of string) is `</s>`, used at the end of each completion, terminating any assistant message.

**The whitespaces are of extreme importance.**

Note that `<s>` and `</s>` are more like strings representing the BOS and EOS than actual strings. Their corresponding IDs are `1` and `2`.

> ⚠️ This template will always cause the model to output a token that starts with a whitespace, always having a leading space. Depending on your inference engine, it may or may not strip that whitespace by default. Hence, it is essential to ensure that a whitespace (and a single one) is present after each assistant response when using the template.

The Jinja template for the HuggingFace `transformers` for this kind of string could look something like this:

You can see the current one being used by default by taking a look at the [tokenizer\_config.json](https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-chat_templates).

Here it is formatted to be easier to read, making it easier to understand how they work:

> ⚠️ As you can see, each `message['content']` is always preceded by a whitespace. This assumes that `message['content']` has the first whitespace manually removed by you or your inference library.

If you want to apply the template yourself manually, you can do it in Python:

### Instruct Tokenization Logic

Now let's dig into the original logic behind the tokenization process that you can see in `mistral_common`. You often would not simply provide the text to the tokenizer and encode the entire string as it is, `mistral-common` actually goes directly from `request` -&gt; `int`, while other approaches such as the one used by `transformers` is closer to `request` -&gt; `str` -&gt; `int`. The way it is actually done for the tokenization process is closer to the following logic:

- **Tokenize each message:**  
  You would have user messages and assistant messages. You would take them separately as individual strings, with the user message encapsulated with the special strings, and encode them. In the previous example, this would be something like:  
  `encode("[INST] user message [/INST]")`, `encode("assistant message")`, and `encode("[INST] new user message [/INST]")`, and so on...
- **Concatenate:**  
  Once each message is tokenized and encoded, you would concatenate them all, prepending them with the BOS ID and separating them by pairs with the EOS ID:  
  `BOS_ID + encode("[INST] user message [/INST]") + encode("assistant message") + EOS_ID + encode("[INST] new user message [/INST]")`

You might notice that if followed step by step, this would actually match with a string and whitespaces added like so:

"\_" represents the added whitespaces when encapsulating with the special strings

If compared to the chat template mentioned above, this misses some whitespaces after the BOS and EOS. Where do they come from then? They come from `sentencepiece` when encoding. It will, by default, start with a leading whitespace. So every time we `encode`, we are adding a leading whitespace. Therefore:

- `encode("[INST] user message [/INST]")` is actually encoding `encode(" [INST] user message [/INST]")`

This adds the leading whitespaces, making the final string look more like:

"\_" represents the new added whitespaces by sentencepiece

Finally, token per token it will give the following:

"\_" represents any whitespace

### System Prompt

The first releases did not have a specific methodology for system prompts. By default, we usually prepend the system prompt to the first user message, followed by two new lines:

## Tokenizer V2

Following the previous tokenizer, and mostly used by the proprietary models, the second version of the tokenizer powered models such as the now old Mistral Small 2402 and Mistral Large 2402. This new tokenizer introduced control tokens, specifically for the previous special strings `[INST]` and `[/INST]`, which became control tokens with the corresponding IDs being `3` and `4`, but also new control tokens for function calling.

### Instruct Chat Template

Due to the introduction of the control tokens, the chat template changed slightly due to the absence of some whitespaces.

For comparison, here is a string with the previous chat template of the previous tokenizer:

> ⚠️ This template will always cause the model to output a token that starts with a whitespace, always having a leading space. Depending on your inference engine, it may or may not strip that whitespace by default. Hence, it is essential to ensure that a whitespace (and a single one) is present after each assistant response when using the template.

The Jinja Template for the HuggingFace `transformers` for this kind of string could look something like this:

After being formatted to be easier to read:

> ⚠️ As you can see, each `message['content']` is always preceded by a whitespace. This assumes that `message['content']` has the first whitespace manually removed by you or your inference library.

If you want to apply the template yourself manually, you can do it in Python:

**FIM**  
For FIM, the template would be as follows:

### Instruct Tokenization Logic

Now that we have control tokens, the process to tokenize has changed slightly. Here is the new logic behind the chat template:

- **Tokenize each message:**  
  You have user messages and assistant messages. You now take them separately as individual strings and encode them:  
  `encode(user_message)`, `encode(assistant_message)`, and `encode(new_user_message)`, and so on...
- **Concatenate:**  
  Once each message is tokenized and encoded, you would concatenate them all, prepending them with the BOS ID and separating them by pairs with the EOS ID while encapsulating the user messages with the control tokens, specifically `[INST]` ID and `[/INST]` ID:  
  `BOS_ID + INST_ID + encode("user message") + /INST_ID + encode("assistant message") + EOS_ID + INST_ID + encode("new user message") + /INST_ID`

Following this, the string would be something like so:

However, once more, this misses some whitespaces, this time after the control tokens. They come from the same place as before, from `sentencepiece`:

- `encode("user message")` is actually encoding `encode(" user message")`
- `encode("assistant message")` is actually encoding `encode(" assistant message")`
- `encode("new user message")` is actually encoding `encode(" new user message")`

This adds the missing whitespaces, making the final string look more like:

"\_" represents the new added whitespaces by sentencepiece

Finally, token per token it will give the following:

### System Prompt

The second version of the tokenizer implements a slightly different system prompt approach. By default, it prepends it to the last user message:

> ⚠️ This is how `mistral_common` and the templates implement system prompts, but this can easily be customized. Feel free to use system prompts in different places, such as the second from the last or simply as the first user message, as before.

## Tokenizer V3

This tokenizer powers models such as Mixtral 8x22B, Codestral 22B, Mathstral 7B, Mamba Codestral 7B, Small 2409 and Large 2 (Large 2407). It is highly similar to the second version, with only tool use being slightly different.

The chat template, tokenization, and system prompt for basic instruct are the same as the previous one.

### Tekken

Tekken is a different version of the V3 tokenizer and powers Mistral Nemo 12B and Pixtral 12B. While the original one and previous tokenizers were based on `sentencepiece`, Tekken is based on `tiktoken`. With a considerably larger vocabulary size, it also deals with encoding differently. The main difference for the chat template is that it does not prepend a whitespace like `sentencepiece`.

This results in a simpler chat template and more intuitive tokenization.

### Tekken Instruct Chat Template

With even fewer intrusive whitespaces, the new template is as simple as the following:

For comparison, here is the chat template of the previous tokenizer:

The Jinja template for the HuggingFace `transformers` for this kind of string could look something like this:

Formatted to be easier to read:

If you want to apply the template yourself manually, you can do it in Python:

### Tekken Instruct Tokenization Logic

The logic for the tokenization is still the same as the previous one, which is:

- **Tokenize each message:**  
  You have user messages and assistant messages. You now take them separately as individual strings and encode them:  
  `encode(user_message)`, `encode(assistant_message)`, and `encode(new_user_message)`, and so on...
- **Concatenate:**  
  Once each message is tokenized and encoded, you would concatenate them all, prepending them with the BOS ID and separating them by pairs with the EOS ID while encapsulating the user messages with the control tokens, specifically `[INST]` ID and `[/INST]` ID:  
  `BOS_ID + INST_ID + encode("user message") + /INST_ID + encode("assistant message") + EOS_ID + INST_ID + encode("new user message") + /INST_ID`

And that is all. The resulting string is more intuitive, with no whitespaces added since it has a different behavior from `sentencepiece`, making the final string the following:

Token per token::

### System Prompt

By default, the system prompt is handled similarly to the previous versions:

## Conclusion

The tokenizers have evolved significantly from V1 to V3 and the Tekken variant, each iteration bringing improvements and changes that have sometimes led to debates and issues within the community. Understanding the nuances of these tokenizers is crucial for optimizing the performance of Mistral models in various applications and properly fine-tuning.

### Key Takeaways:

1. **Tokenizer V1**:
   
   - Used `sentencepiece` and a template similar to Llama models.
   - Special strings `[INST]` and `[/INST]` with whitespace handling.
   - System prompt prepended to the first user message with two new lines.
2. **Tokenizer V2**:
   
   - Introduced control tokens for `[INST]` and `[/INST]` as well as other control tokens.
   - Slightly adjusted chat template due to the absence of some whitespaces.
   - System prompt prepended to the last user message.
3. **Tokenizer V3**:
   
   - Similar to V2 but improved tool use.
   - Same chat template, tokenization, and system prompt approach as V2.
4. **Tokenizer V3 - Tekken**:
   
   - Based on `tiktoken` with a larger vocabulary.
   - Simpler chat template with no leading whitespaces.

### Best Practices:

- **Whitespace Handling**: Pay close attention to whitespace handling, especially with the `sentencepiece`-based tokenizers, as they prepend leading whitespaces.
- **Control Tokens**: Use control tokens correctly in V2 and V3 tokenizers to ensure proper encapsulation of user messages.
- **System Prompts**: Customize system prompts as needed, but be aware of the default placements in different tokenizer versions.

### Community and Resources:

- **Community Contributions**: The community has been instrumental in identifying and resolving inconsistencies and bugs, showcasing the collaborative nature of open-source development. Join Mistral's [discord server](https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-chat_templates) and exchange with community members!
- **Ground Truth**: For the most accurate and up-to-date information, refer to the [mistral\_common](https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-chat_templates) repository on GitHub and the [documentation](https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-chat_templates).