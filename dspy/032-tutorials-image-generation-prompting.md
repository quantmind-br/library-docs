---
title: Image Generation Prompt iteration - DSPy
url: https://dspy.ai/tutorials/image_generation_prompting/
source: sitemap
fetched_at: 2026-01-23T08:04:03.723283128-03:00
rendered_js: false
word_count: 1316
summary: This document outlines a structured workflow for evaluating image generation results against desired prompts, featuring iterative feedback and prompt refinement.
tags:
    - prompt-engineering
    - image-evaluation
    - feedback-loop
    - structured-data
    - iterative-refinement
    - ai-vision
category: guide
---

```


[2025-01-17T11:36:55.947579]

System message:

Your input fields are:
1. `desired_prompt` (str)
2. `current_image` (Image)
3. `current_prompt` (str)

Your output fields are:
1. `feedback` (str)
2. `revised_prompt` (str)
3. `image_strictly_matches_desired_prompt` (bool)

All interactions will be structured in the following way, with the appropriate values filled in.

[[ ## desired_prompt ## ]]
{desired_prompt}

[[ ## current_image ## ]]
{current_image}

[[ ## current_prompt ## ]]
{current_prompt}

[[ ## feedback ## ]]
{feedback}

[[ ## revised_prompt ## ]]
{revised_prompt}

[[ ## image_strictly_matches_desired_prompt ## ]]
{image_strictly_matches_desired_prompt}        # note: the value you produce must be True or False

[[ ## completed ## ]]

In adhering to this structure, your objective is: 
        Given the fields `desired_prompt`, `current_image`, `current_prompt`, produce the fields `feedback`, `revised_prompt`, `image_strictly_matches_desired_prompt`.


User message:

[[ ## desired_prompt ## ]]
A scene that's both peaceful and tense

[[ ## current_image ## ]]
<image_url: https://fal.media/files/panda/HLKaiKFc_sN_fwBBN1C_2_1d1a72732e294452afb056a26d6b6c96.jpg>

[[ ## current_prompt ## ]]
A scene that's both peaceful and tense

Respond with the corresponding output fields, starting with the field `[[ ## feedback ## ]]`, then `[[ ## revised_prompt ## ]]`, then `[[ ## image_strictly_matches_desired_prompt ## ]]` (must be formatted as a valid Python bool), and then ending with the marker for `[[ ## completed ## ]]`.


Response:

[[ ## feedback ## ]]
The image depicts a calm café scene with two individuals engaged in conversation, which conveys a sense of peace. However, the woman's posture and expression suggest an underlying tension, as she appears to be contemplative or distressed. This duality aligns well with the desired prompt of being both peaceful and tense.

[[ ## revised_prompt ## ]]
A scene that captures the duality of peace and tension in a café setting.

[[ ## image_strictly_matches_desired_prompt ## ]]
True

[[ ## completed ## ]]


[2025-01-17T11:37:55.458433]

System message:

Your input fields are:
1. `desired_prompt` (str)
2. `current_image` (Image)
3. `current_prompt` (str)

Your output fields are:
1. `feedback` (str)
2. `image_strictly_matches_desired_prompt` (bool)
3. `revised_prompt` (str)

All interactions will be structured in the following way, with the appropriate values filled in.

[[ ## desired_prompt ## ]]
{desired_prompt}

[[ ## current_image ## ]]
{current_image}

[[ ## current_prompt ## ]]
{current_prompt}

[[ ## feedback ## ]]
{feedback}

[[ ## image_strictly_matches_desired_prompt ## ]]
{image_strictly_matches_desired_prompt}        # note: the value you produce must be True or False

[[ ## revised_prompt ## ]]
{revised_prompt}

[[ ## completed ## ]]

In adhering to this structure, your objective is: 
        Given the fields `desired_prompt`, `current_image`, `current_prompt`, produce the fields `feedback`, `image_strictly_matches_desired_prompt`, `revised_prompt`.


User message:

[[ ## desired_prompt ## ]]
A scene that's both peaceful and tense

[[ ## current_image ## ]]
<image_url: https://fal.media/files/elephant/p3M00ca786Ov5ITX8nXUs_7b815b2087e54c1fbd798b9b9e0c5f5e.jpg>

[[ ## current_prompt ## ]]
A scene that's both peaceful and tense

Respond with the corresponding output fields, starting with the field `[[ ## feedback ## ]]`, then `[[ ## image_strictly_matches_desired_prompt ## ]]` (must be formatted as a valid Python bool), then `[[ ## revised_prompt ## ]]`, and then ending with the marker for `[[ ## completed ## ]]`.


Response:

[[ ## feedback ## ]]
The image depicts a peaceful autumn scene with people walking among colorful leaves, which aligns with the peaceful aspect of the prompt. However, it lacks any elements that convey tension, making it not fully representative of the desired prompt.

[[ ## image_strictly_matches_desired_prompt ## ]]
False

[[ ## revised_prompt ## ]]
A serene autumn scene with elements that suggest underlying tension

[[ ## completed ## ]]


[2025-01-17T11:38:24.032318]

System message:

Your input fields are:
1. `desired_prompt` (str)
2. `current_image` (Image)
3. `current_prompt` (str)

Your output fields are:
1. `feedback` (str)
2. `image_strictly_matches_desired_prompt` (bool)
3. `revised_prompt` (str)

All interactions will be structured in the following way, with the appropriate values filled in.

[[ ## desired_prompt ## ]]
{desired_prompt}

[[ ## current_image ## ]]
{current_image}

[[ ## current_prompt ## ]]
{current_prompt}

[[ ## feedback ## ]]
{feedback}

[[ ## image_strictly_matches_desired_prompt ## ]]
{image_strictly_matches_desired_prompt}        # note: the value you produce must be True or False

[[ ## revised_prompt ## ]]
{revised_prompt}

[[ ## completed ## ]]

In adhering to this structure, your objective is: 
        Given the fields `desired_prompt`, `current_image`, `current_prompt`, produce the fields `feedback`, `image_strictly_matches_desired_prompt`, `revised_prompt`.


User message:

[[ ## desired_prompt ## ]]
A scene that's both peaceful and tense

[[ ## current_image ## ]]
<image_url: https://fal.media/files/monkey/QhPlYYa5tob38190Gtn0t_17e963cacc1542d5977031aff954c718.jpg>

[[ ## current_prompt ## ]]
A serene autumn scene with elements that suggest underlying tension

Respond with the corresponding output fields, starting with the field `[[ ## feedback ## ]]`, then `[[ ## image_strictly_matches_desired_prompt ## ]]` (must be formatted as a valid Python bool), then `[[ ## revised_prompt ## ]]`, and then ending with the marker for `[[ ## completed ## ]]`.


Response:

[[ ## feedback ## ]]
The image depicts a serene autumn scene with vibrant foliage and a calm river, which aligns well with the idea of peace. However, it lacks explicit elements that suggest underlying tension, making it less effective in conveying both aspects of the desired prompt.

[[ ## image_strictly_matches_desired_prompt ## ]]
False

[[ ## revised_prompt ## ]]
A serene autumn scene with elements that evoke a sense of unease or foreboding

[[ ## completed ## ]]


[2025-01-17T11:38:46.424883]

System message:

Your input fields are:
1. `desired_prompt` (str)
2. `current_image` (Image)
3. `current_prompt` (str)

Your output fields are:
1. `feedback` (str)
2. `image_strictly_matches_desired_prompt` (bool)
3. `revised_prompt` (str)

All interactions will be structured in the following way, with the appropriate values filled in.

[[ ## desired_prompt ## ]]
{desired_prompt}

[[ ## current_image ## ]]
{current_image}

[[ ## current_prompt ## ]]
{current_prompt}

[[ ## feedback ## ]]
{feedback}

[[ ## image_strictly_matches_desired_prompt ## ]]
{image_strictly_matches_desired_prompt}        # note: the value you produce must be True or False

[[ ## revised_prompt ## ]]
{revised_prompt}

[[ ## completed ## ]]

In adhering to this structure, your objective is: 
        Given the fields `desired_prompt`, `current_image`, `current_prompt`, produce the fields `feedback`, `image_strictly_matches_desired_prompt`, `revised_prompt`.


User message:

[[ ## desired_prompt ## ]]
A scene that's both peaceful and tense

[[ ## current_image ## ]]
<image_url: https://fal.media/files/panda/kNBH7FF1uLk06nXonN0Zr_256e1bf2f71c4dcc8eb94027f09f3452.jpg>

[[ ## current_prompt ## ]]
A serene autumn scene with elements that evoke a sense of unease or foreboding

Respond with the corresponding output fields, starting with the field `[[ ## feedback ## ]]`, then `[[ ## image_strictly_matches_desired_prompt ## ]]` (must be formatted as a valid Python bool), then `[[ ## revised_prompt ## ]]`, and then ending with the marker for `[[ ## completed ## ]]`.


Response:

[[ ## feedback ## ]]
The image depicts a serene autumn scene with warm colors and soft lighting, which aligns with the peaceful aspect of the desired prompt. However, it lacks elements that evoke tension or unease, making it not fully meet the requirement for a scene that is both peaceful and tense.

[[ ## image_strictly_matches_desired_prompt ## ]]
False

[[ ## revised_prompt ## ]]
A serene autumn scene that includes subtle elements of tension or foreboding, such as dark shadows or an unsettling atmosphere.

[[ ## completed ## ]]


[2025-01-17T11:39:03.586839]

System message:

Your input fields are:
1. `desired_prompt` (str)
2. `current_image` (Image)
3. `current_prompt` (str)

Your output fields are:
1. `feedback` (str)
2. `image_strictly_matches_desired_prompt` (bool)
3. `revised_prompt` (str)

All interactions will be structured in the following way, with the appropriate values filled in.

[[ ## desired_prompt ## ]]
{desired_prompt}

[[ ## current_image ## ]]
{current_image}

[[ ## current_prompt ## ]]
{current_prompt}

[[ ## feedback ## ]]
{feedback}

[[ ## image_strictly_matches_desired_prompt ## ]]
{image_strictly_matches_desired_prompt}        # note: the value you produce must be True or False

[[ ## revised_prompt ## ]]
{revised_prompt}

[[ ## completed ## ]]

In adhering to this structure, your objective is: 
        Given the fields `desired_prompt`, `current_image`, `current_prompt`, produce the fields `feedback`, `image_strictly_matches_desired_prompt`, `revised_prompt`.


User message:

[[ ## desired_prompt ## ]]
A scene that's both peaceful and tense

[[ ## current_image ## ]]
<image_url: https://fal.media/files/penguin/AXRlgHfIxbZ26Ipgd64Rn_d012474791904e70bd419945f7179980.jpg>

[[ ## current_prompt ## ]]
A serene autumn scene that includes subtle elements of tension or foreboding, such as dark shadows or an unsettling atmosphere.

Respond with the corresponding output fields, starting with the field `[[ ## feedback ## ]]`, then `[[ ## image_strictly_matches_desired_prompt ## ]]` (must be formatted as a valid Python bool), then `[[ ## revised_prompt ## ]]`, and then ending with the marker for `[[ ## completed ## ]]`.


Response:

[[ ## feedback ## ]]
The image depicts a foggy forest scene with autumn leaves, creating a peaceful atmosphere. However, the overall mood is somewhat tense due to the fog and shadows, aligning well with the desired prompt of being both peaceful and tense. 

[[ ## image_strictly_matches_desired_prompt ## ]]
True

[[ ## revised_prompt ## ]]
A serene autumn scene with fog and shadows, capturing both peace and tension.

[[ ## completed ## ]]


```