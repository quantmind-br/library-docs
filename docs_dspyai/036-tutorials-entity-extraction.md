---
title: Entity Extraction - DSPy
url: https://dspy.ai/tutorials/entity_extraction/
source: sitemap
fetched_at: 2026-01-23T08:03:52.841439236-03:00
rendered_js: false
word_count: 667
summary: This document defines a structured prompt and few-shot examples for performing named entity recognition to extract specific individuals from tokenized text strings.
tags:
    - named-entity-recognition
    - ner
    - few-shot-prompting
    - nlp
    - token-extraction
    - prompt-engineering
category: reference
---

```


[2024-11-18T21:15:00.584497]

System message:

Your input fields are:
1. `tokens` (list[str]): tokenized text

Your output fields are:
1. `rationale` (str): ${produce the extracted_people}. We ...
2. `extracted_people` (list[str]): all tokens referring to specific people extracted from the tokenized text

All interactions will be structured in the following way, with the appropriate values filled in.

[[ ## tokens ## ]]
{tokens}

[[ ## rationale ## ]]
{rationale}

[[ ## extracted_people ## ]]
{extracted_people}        # note: the value you produce must be pareseable according to the following JSON schema: {"type": "array", "items": {"type": "string"}}

[[ ## completed ## ]]

In adhering to this structure, your objective is: 
        In a high-stakes situation where accurate identification of individuals is critical for regulatory compliance and public health communication, extract contiguous tokens referring to specific people from the provided list of string tokens. Ensure that you output each identified individual as separate tokens without combining multiple tokens into a single value. This task is essential for ensuring clarity and accountability in communications pertaining to EU regulations and health matters.


User message:

[[ ## tokens ## ]]
["He", "said", "further", "scientific", "study", "was", "required", "and", "if", "it", "was", "found", "that", "action", "was", "needed", "it", "should", "be", "taken", "by", "the", "European", "Union", "."]

Respond with the corresponding output fields, starting with the field `[[ ## rationale ## ]]`, then `[[ ## extracted_people ## ]]` (must be formatted as a valid Python list[str]), and then ending with the marker for `[[ ## completed ## ]]`.


Assistant message:

[[ ## rationale ## ]]
There are no specific people mentioned in the provided tokens. The only reference is to the "European Union," which is an organization rather than a specific person. We therefore conclude that there are no extracted people.

[[ ## extracted_people ## ]]
[]

[[ ## completed ## ]]


User message:

[[ ## tokens ## ]]
["BRUSSELS", "1996-08-22"]

Respond with the corresponding output fields, starting with the field `[[ ## rationale ## ]]`, then `[[ ## extracted_people ## ]]` (must be formatted as a valid Python list[str]), and then ending with the marker for `[[ ## completed ## ]]`.


Assistant message:

[[ ## rationale ## ]]
There are no tokens referring to specific people in the provided list. We only have a location and a date.

[[ ## extracted_people ## ]]
[]

[[ ## completed ## ]]


User message:

[[ ## tokens ## ]]
["Fischler", "proposed", "EU-wide", "measures", "after", "reports", "from", "Britain", "and", "France", "that", "under", "laboratory", "conditions", "sheep", "could", "contract", "Bovine", "Spongiform", "Encephalopathy", "(", "BSE", ")", "--", "mad", "cow", "disease", "."]

Respond with the corresponding output fields, starting with the field `[[ ## rationale ## ]]`, then `[[ ## extracted_people ## ]]` (must be formatted as a valid Python list[str]), and then ending with the marker for `[[ ## completed ## ]]`.


Assistant message:

[[ ## rationale ## ]]
The extracted tokens refer to specific people mentioned in the text. In this case, "Fischler" is the only token that refers to a specific person. We extract this token as it is contiguous and represents an individual involved in the proposed measures.

[[ ## extracted_people ## ]]
["Fischler"]

[[ ## completed ## ]]


User message:

[[ ## tokens ## ]]
["Germany", "'s", "representative", "to", "the", "European", "Union", "'s", "veterinary", "committee", "Werner", "Zwingmann", "said", "on", "Wednesday", "consumers", "should", "buy", "sheepmeat", "from", "countries", "other", "than", "Britain", "until", "the", "scientific", "advice", "was", "clearer", "."]

Respond with the corresponding output fields, starting with the field `[[ ## rationale ## ]]`, then `[[ ## extracted_people ## ]]` (must be formatted as a valid Python list[str]), and then ending with the marker for `[[ ## completed ## ]]`.


Assistant message:

[[ ## rationale ## ]]
We extracted the name "Werner Zwingmann" from the tokenized text as it refers to a specific person mentioned in the context of a statement regarding sheepmeat consumption.

[[ ## extracted_people ## ]]
["Werner", "Zwingmann"]

[[ ## completed ## ]]


User message:

[[ ## tokens ## ]]
["LONDON", "1996-12-06"]

Respond with the corresponding output fields, starting with the field `[[ ## rationale ## ]]`, then `[[ ## extracted_people ## ]]` (must be formatted as a valid Python list[str]), and then ending with the marker for `[[ ## completed ## ]]`.


Response:

[[ ## rationale ## ]]
There are no tokens referring to specific people in the provided list. The tokens only include a location and a date.

[[ ## extracted_people ## ]]
[]

[[ ## completed ## ]]


```