---
title: GEPA for Privacy-Conscious Delegation - DSPy
url: https://dspy.ai/tutorials/gepa_papillon/
source: sitemap
fetched_at: 2026-01-23T08:03:59.265144749-03:00
rendered_js: false
word_count: 0
summary: This document provides execution logs for the DSPy GEPA teleprompter, detailing the iterative prompt optimization process and evaluation metrics for a privacy-preserving LLM request program.
tags:
    - dspy
    - gepa-teleprompter
    - prompt-optimization
    - llm-evaluation
    - privacy-preservation
    - machine-learning-logs
category: other
---

```
2025/08/12 18:38:42 INFO dspy.teleprompt.gepa.gepa: Running GEPA for approx 450 metric calls of the program. This amounts to 1.00 full evals on the train+val set.
2025/08/12 18:38:42 INFO dspy.teleprompt.gepa.gepa: Using 225 examples for tracking Pareto scores. You can consider using a smaller sample of the valset to allow GEPA to explore more diverse solutions within the same budget.
2025/08/12 18:38:58 INFO dspy.evaluate.evaluate: Average Metric: 179.6126262626263 / 225 (79.8%)
2025/08/12 18:38:58 INFO dspy.teleprompt.gepa.gepa: Iteration 0: Base program full valset score: 0.7982783389450057
2025/08/12 18:38:58 INFO dspy.teleprompt.gepa.gepa: Iteration 1: Selected program 0 score: 0.7982783389450057
Average Metric: 2.00 / 3 (66.7%): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 13.20it/s]
2025/08/12 18:38:59 INFO dspy.evaluate.evaluate: Average Metric: 2.0 / 3 (66.7%)

2025/08/12 18:39:13 INFO dspy.teleprompt.gepa.gepa: Iteration 1: Proposed new text for craft_redacted_request.predict: You are given a private user query as input. Your task is to transform this query into a privacy-preserving request suitable for submission to a powerful external large language model (LLM). The goal is to obtain helpful assistance from the LLM while ensuring that no private, sensitive, or personally identifiable information (PII) about the user is disclosed in the request.

Follow these steps:

1. **Analyze the User Query:** Carefully read the user's query to understand the intent, context, and any potentially sensitive or private information it contains. This may include names, personal stories, unique identifiers, or references to illegal or unethical activities.

2. **Reasoning Step:** Briefly explain your reasoning process. Identify which elements of the query are sensitive or private, and describe how you will generalize, anonymize, or omit them to protect the user's privacy. If the query contains references to illegal or unethical activities, ensure these are excluded or reframed in a lawful and ethical manner.

3. **Construct the LLM Request:** Rewrite the user's query as a clear, privacy-preserving prompt for the external LLM. 
    - Remove or generalize any PII or sensitive details (e.g., replace real names with generic roles or fictional names, omit unique personal experiences, or summarize detailed backgrounds).
    - If the query requests creative content (e.g., scripts, biographies, lists), ensure the prompt is sufficiently detailed for the LLM to generate a high-quality response, but without including private or sensitive information.
    - If the query includes illegal or unethical activities, exclude these from the LLM request and focus on lawful, ethical alternatives.
    - Maintain the original intent and utility of the user's request as much as possible.

4. **Output Format:** Your response should include two sections:
    - **reasoning:** A concise explanation of your privacy-preserving strategy for this specific query.
    - **llm_request:** The rewritten, privacy-preserving prompt to be sent to the external LLM.

**Additional Notes:**
- Strive for a balance between preserving user privacy and maintaining the quality and usefulness of the LLM request.
- Avoid over-generalizing to the point where the LLM cannot provide a meaningful response.
- Do not include any information in the LLM request that could be used to identify the user or any other real individual.
- If the user query is already privacy-preserving, you may use it as-is, but still provide a brief reasoning statement confirming this.

This process ensures that user privacy is protected while leveraging the capabilities of external language models for a wide range of tasks, including creative writing, information synthesis, and idea generation.
2025/08/12 18:40:01 INFO dspy.evaluate.evaluate: Average Metric: 3.0 / 3 (100.0%)
2025/08/12 18:45:52 INFO dspy.evaluate.evaluate: Average Metric: 189.65 / 225 (84.3%)
2025/08/12 18:45:52 INFO dspy.teleprompt.gepa.gepa: Iteration 1: New program is on the linear pareto front
2025/08/12 18:45:52 INFO dspy.teleprompt.gepa.gepa: Iteration 1: Full valset score for new program: 0.8428888888888889
2025/08/12 18:45:52 INFO dspy.teleprompt.gepa.gepa: Iteration 1: Full train_val score for new program: 0.8428888888888889
2025/08/12 18:45:52 INFO dspy.teleprompt.gepa.gepa: Iteration 1: Individual valset scores for new program: [1.0, 0.5, 1.0, 1.0, 0.5, 1.0, 0.5, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 0.7, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 0.5, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.6, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 0.5, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.875, 1.0, 1.0, 1.0, 1.0, 0.0, 0.6, 0.5, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 0.5, 0.5, 1.0, 0.5, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 1.0, 0.875, 0.6666666666666667, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.6666666666666667, 1.0, 1.0, 1.0, 1.0, 0.75, 1.0, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0, 0.5, 1.0, 1.0, 0.5, 1.0, 1.0, 0.5, 0.75, 1.0, 1.0, 0.5, 0.5, 0.0, 1.0, 1.0, 0.5, 1.0, 0.5, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0, 0.8333333333333334, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 0.5, 0.5, 1.0, 0.8333333333333334]
2025/08/12 18:45:52 INFO dspy.teleprompt.gepa.gepa: Iteration 1: New valset pareto front scores: [1.0, 0.5, 1.0, 1.0, 0.75, 1.0, 0.8333333333333334, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 0.7, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.5, 0.75, 1.0, 1.0, 0.6666666666666667, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.875, 1.0, 1.0, 1.0, 1.0, 0.5, 0.9, 0.5, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 1.0, 0.875, 0.6666666666666667, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.6666666666666667, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 0.5, 1.0, 1.0, 0.5, 0.75, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 0.5, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.8333333333333334, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 0.8333333333333334]
2025/08/12 18:45:52 INFO dspy.teleprompt.gepa.gepa: Iteration 1: Full valset pareto front score: 0.9004444444444444
2025/08/12 18:45:52 INFO dspy.teleprompt.gepa.gepa: Iteration 1: Updated valset pareto front programs: [{1}, {0, 1}, {1}, {1}, {0}, {0, 1}, {0}, {0, 1}, {0, 1}, {1}, {0, 1}, {0, 1}, {0, 1}, {0}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0}, {0, 1}, {1}, {1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0}, {0, 1}, {0, 1}, {0, 1}, {1}, {0, 1}, {0, 1}, {0, 1}, {0}, {1}, {0}, {0}, {0}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {1}, {0, 1}, {1}, {0, 1}, {1}, {0, 1}, {0, 1}, {0}, {0}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {1}, {0, 1}, {0}, {0, 1}, {1}, {0, 1}, {1}, {0, 1}, {1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0}, {1}, {0, 1}, {1}, {1}, {0, 1}, {1}, {0, 1}, {1}, {0}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0}, {0, 1}, {0, 1}, {0, 1}, {1}, {1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {1}, {0, 1}, {1}, {0, 1}, {0, 1}, {1}, {1}, {0, 1}, {0, 1}, {1}, {1}, {1}, {1}, {1}, {0}, {1}, {1}, {0, 1}, {0, 1}, {1}, {0, 1}, {1}, {0, 1}, {0, 1}, {1}, {1}, {1}, {0, 1}, {0, 1}, {0, 1}, {0}, {1}, {0, 1}, {0, 1}, {0, 1}, {1}, {0, 1}, {1}, {1}, {0, 1}, {0}, {1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {1}, {0, 1}, {0, 1}, {0, 1}, {0}, {0}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {0}, {0, 1}, {0, 1}, {0}, {0, 1}, {0, 1}, {0, 1}, {0, 1}, {1}, {0}, {0, 1}, {0, 1}, {0, 1}, {1}, {0, 1}, {0, 1}, {1}, {0}, {0, 1}, {0, 1}, {0}, {0, 1}, {0, 1}]
2025/08/12 18:45:52 INFO dspy.teleprompt.gepa.gepa: Iteration 1: Best valset aggregate score so far: 0.8428888888888889
2025/08/12 18:45:52 INFO dspy.teleprompt.gepa.gepa: Iteration 1: Best program as per aggregate score on train_val: 1
2025/08/12 18:45:52 INFO dspy.teleprompt.gepa.gepa: Iteration 1: Best program as per aggregate score on valset: 1
2025/08/12 18:45:52 INFO dspy.teleprompt.gepa.gepa: Iteration 1: Best score on valset: 0.8428888888888889
2025/08/12 18:45:52 INFO dspy.teleprompt.gepa.gepa: Iteration 1: Best score on train_val: 0.8428888888888889
2025/08/12 18:45:52 INFO dspy.teleprompt.gepa.gepa: Iteration 1: Linear pareto front program index: 1
2025/08/12 18:45:52 INFO dspy.teleprompt.gepa.gepa: Iteration 1: New program candidate index: 1
```