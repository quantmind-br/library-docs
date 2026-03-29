---
title: 'Prefix Use Cases: Language Adherence, Saving Tokens, Roleplay, Anti-Jailbreaking - Mistral AI Cookbook'
url: https://docs.mistral.ai/cookbooks/mistral-prompting-prefix_use_cases
source: crawler
fetched_at: 2026-01-29T07:34:01.434153498-03:00
rendered_js: false
word_count: 1380
summary: This guide from the Mistral AI Cookbook explores practical applications of prompt prefixes to improve language adherence, optimize token usage, enhance roleplay, and implement anti-jailbreaking measures.
tags:
    - Mistral AI
    - prompt engineering
    - prefix use cases
    - token optimization
    - AI safety
category: guide
---

In this notebook, we will talk about a specific feature of our API - the ability to add a **prefix** to the model's response.

### What is it?

A prefix is essentially a string that is prepended to a model's response, rather than to the user's query. This means that the model will not generate the string, but it will be included as part of the input.

For example, let's say we ask a model a question:

- Input: `User: Hi there! Assistant:`
- Output: `Hello! It's nice to meet you. Is there something you'd like to talk about or learn more about? I'm here to help.`

However, if we want the model to always start with "I'm kind" for a specific use case and continue from there as a completion model, it would look like this:

- Input: `User: Hi there! Assistant: I'm kind`
- Output: `and new here, so please bear with me if I make any mistakes. How can I assist you today?`

This way, we can force the model to begin a sentence or response with a desired string of our choice!

### Other Examples

For reference, here are some other examples of prefixes being used to better visualize:

Question:  
\- `"How are you?"`  
Prefix:  
\- `"Fine"`  
Assistant:  
\- `"Fine, thank you! How can I help you today?"`

Question:  
\- `"Who is Albert Einstein?"`  
Prefix:  
\- `"Well..."`  
Assistant:  
\- `"Well...you've asked about one of the most influential scientists in history! Albert Einstein (1879-1955) was a theoretical physicist, known best [...]"`

## Cool Examples

We will now dig into a few different cool examples and explore its hidden potential!

Essentially, prefixes enable a high level of instruction following and adherence or define the model's response more effectively with less effort.

For all of the following examples, we will need to set up our client. Let's import the required package and then create the client with your API key!

### Overview

**The topics we are going to delve into are:**

- **[Language Adherence](#language-adherence):** How to make a model always answer in a specific language regardless of input.
- **[Saving Tokens](#saving-tokens):** Leveraging the potential of prefixes to save as much input tokens as possible.
- **[Roleplay](#roleplay):** Make use of prefixes for various roleplay and creative writing tasks.
- **[Anti-Jailbreaking](#anti-jailbreaking):** Implementing extremely strong safeguarding mechanisms.

### Language Adherence

There are a few cases where we want our model to always answer in a specific language, regardless of the language used by the `user` or by any documents or retrieval systems quoted by the `user`.

Let's imagine the following scenario: we want our model to always answer in a specific writing style in French. In this case, we want it to respond as a pirate assistant that always answers in French.

For that, we will define a `system` prompt!

As you might have noticed, some models struggle to adhere to a specific language, even if we insist, unless we take the time to carefully engineer the prompts. And even then, there may still be consistency issues.

Another solution would be to use a few-shot learning approach, but this can quickly become expensive in terms of tokens and time-consuming.

So, for those scenarios, prefixes are a great solution! The idea is to **specify the language or prefix a sentence in the correct language beforehand**, so the model will more easily adhere to it.

Optionally, you can remove the prefix if you do not expect it to be part of the answer.

Perfect! We might even be able to remove part of the original system to save some tokens.

And there we have it! With the help of prefixes, we can achieve very high language adherence, making it easier to set different languages for any application.

### Saving Tokens

As mentioned previously, prefixes can allow us to save a lot of tokens, making system prompts sometimes obsolete!

Our next mission will be to completely replace a system prompt with a very specific and short prefix...

In the previous "Language Adherence" example, our goal was to create a pirate assistant that always answers in French. The system prompt we used looked like this:

In English, this translates to:

So, let's try to make use of the prefix feature and come up with something that will allow the model to understand that it should both answer as an assistant and a pirate... while also using French... like the start of a dialogue! Something like this:

Three words were all it took! This really shows off the hidden potential of prefixes!

*Note: While prefixes can be money-saving and very useful for language adherence, the best solution is to use both a system prompt or detailed instruction and a prefix. Using a prefix alone might sometimes result in noisy and unpredictable answers with undesirable and hallucinated comments from the model. The right balance between the two would be the recommended way to go.*

### Roleplay

Previously, we indirectly explored prefixes in the sections on [Language Adherence](#language-adherence) and [Saving Tokens](#saving-tokens). Prefixes can be extremely helpful and fun to play with, especially in the context of roleplaying and other creative writing tasks!

In this segment, we will explore how we can make use of different aspects of prefixes to write stories and chat with diverse characters from history!

**Pick a Character**  
I'm in the mood to talk to Shakespeare right now – after all, he must have a lot of insights about creative writing!  
For this, we will set a prefix in the same way we would start a dialogue.

Interesting, but it's still not very consistent – sometimes it will generate entire dialogues and conversations.  
Fear not, we can solve this by tweaking the prefix to be a bit more explicit.

There you go! This is similar to what we saw in the [Saving Tokens](#saving-tokens) section, but it's not exactly a roleplay, is it?  
Let's roll back and make it clearer what the objective is. We'll instruct and explain to the model what we expect from it.

We are getting there! Now let's have a full conversation with a character of your choice and chat!

We can go even further now! Let's keep all the previous logic and add a new step – let's add a second or more characters to our roleplaying conversation!  
To pick who speaks, we can randomize it by importing the `random` module.

*Note: We could also make an agent decide and pick which character should speak next. This would provide a more smooth and dynamic interaction!*

There you go! You can now freely speak and interact with any character you like or find interesting!

### Anti-Jailbreaking

There are many scenarios where we require a model to answer within a specific spectrum for various reasons, but most of them rely on very good system prompt adherence.

The idea we are going to explore here is similar to the "Language Adherence" example we previously discussed, but in a more sophisticated way for the purpose of safeguarding. This is because there are many individuals who try to bypass system prompts and security measures with specially crafted prompts.

To combat this, we can make use of prefixes, which are actually quite effective!

Let's imagine a specific use case that requires a system prompt within a very fixed spectrum. For this, we will use our own safe prompt:

Perfect, it's working as desired... but now it's time to ethically test the limits of the safe prompt for demonstration purposes. For this, we have designed a simple jailbreaking prompt.

As we can seen, it's possible to easily break free from the system prompt and other safe prompts with some prompt engineering. However, prefixes make it much harder, and sometimes almost impossible, to break. Let's see this in action with a rewritten safe prompt as a prefix:

While it may be possible to replace the system prompt entirely with a prefix, it's not advised. This is because hallucinations and other undesirable behavior may occur, and new methods of jailbreaking may start to develop. The best solution is to use both a system prompt and a prefix, sandwiching the user's questions between them. This allows for very strong control of the spectrum of possible answers from the model.

*Note: The same principle can be applied to make the model answer in scenarios it would normally refuse, making this feature very adaptable to different needs and use cases.*