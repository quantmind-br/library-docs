---
title: Audio - DSPy
url: https://dspy.ai/tutorials/audio/
source: sitemap
fetched_at: 2026-01-23T08:03:38.748700622-03:00
rendered_js: false
word_count: 259
summary: This document defines a structured system message template for generating detailed text-to-speech instructions that specify vocal tone and emotional style for AI synthesis models.
tags:
    - text-to-speech
    - openai-tts
    - prompt-engineering
    - voice-synthesis
    - emotional-modeling
category: configuration
---

```


[2025-05-15T22:09:40.088592]

System message:

Your input fields are:
1. `raw_line` (str)
2. `target_style` (str)
Your output fields are:
1. `reasoning` (str)
2. `openai_instruction` (str)
All interactions will be structured in the following way, with the appropriate values filled in.

[[ ## raw_line ## ]]
{raw_line}

[[ ## target_style ## ]]
{target_style}

[[ ## reasoning ## ]]
{reasoning}

[[ ## openai_instruction ## ]]
{openai_instruction}

[[ ## completed ## ]]
In adhering to this structure, your objective is: 
        Generate an OpenAI TTS instruction that makes the TTS model speak the given line with the target emotion or style, as if the speaker is a [insert persona relevant to the task, e.g. "irate customer", "angry boss", etc.]. The instruction should specify the tone, pitch, and other characteristics of the speaker's voice to convey the target emotion.


User message:

[[ ## raw_line ## ]]
It's eleven o'clock

[[ ## target_style ## ]]
disgust

Respond with the corresponding output fields, starting with the field `[[ ## reasoning ## ]]`, then `[[ ## openai_instruction ## ]]`, and then ending with the marker for `[[ ## completed ## ]]`.


Response:

[[ ## reasoning ## ]]
To convey disgust, the speaker's voice should be characterized by a high-pitched tone, a slightly nasal quality, and a sense of revulsion. The speaker's words should be delivered with a sense of distaste and aversion, as if the speaker is trying to convey their strong negative emotions.

[[ ## openai_instruction ## ]]
Generate a text-to-speech synthesis of the input text "It's eleven o'clock" with the following characteristics: 
- Tone: Disgusted
- Pitch: High-pitched, slightly nasal
- Emphasis: Emphasize the words to convey a sense of distaste and aversion
- Volume: Moderate to loud, with a sense of rising inflection at the end to convey the speaker's strong negative emotions
- Speaker: A person who is visibly and audibly disgusted, such as a character who has just been served a spoiled meal.

[[ ## completed ## ]]


```