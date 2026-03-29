---
title: Automated Prompt Optimization - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-metagpt-prompt_optimization
source: crawler
fetched_at: 2026-01-29T07:33:47.702483552-03:00
rendered_js: false
word_count: 630
summary: This guide explains how to automate the prompt engineering process using Self-Supervised Prompt Optimization (SPO) with Mistral models and the MetaGPT framework. It provides a workflow for configuring tasks, selecting models, and iteratively refining prompts to improve output quality.
tags:
    - prompt-optimization
    - mistral-ai
    - metagpt
    - prompt-engineering
    - self-supervised-prompt-optimization
category: guide
---

- ❌ Prompt engineering... sucks. It's a non-standard process, heavily relying on trial and error and difficult to standardize
- 🤩 Luckily, we can automate it using ✨prompt optimization✨, investigated in recent works such as [*Self-Supervised Prompt Optimization*](https://arxiv.org/pdf/2502.06855)
- 🎯 In its essence, Prompt Optimization (PO) consists in the process of taking a prompt aiming at performing a certain task and iteratively refining it to make it better for the specific problem tackled.
- ✅ This notebook gives an overview of how to use PO with Mistral models

## Problem setting

- You have put up a form, and collected many more answers than the ones you can read.
- Your survey got popular---very popular, 😅---and need to sift through the answers. To keep things accessibly, we allowed (and will continue to!) responses using plain text.
- Filtering is therefore *impossible*. Still, you need some strategies to sift through the applications received to identify the most promising profiles.
- Let's define a few prompts to process answers and output answers we can filter on effectively.

### Task prompts

- Let's define a few prompts to process answers
- These prompts are purposely not optimized, and rather serve as an example of something quick and dirty we wish to work with.
- For this example, we will consider answers collected as part of the applications for our [Ambassadorship Program](https://docs.mistral.ai/guides/contribute/ambassador/)

### Installing dependancies

To use SPO via MetaGPT you need to clone the repository, and move this notebook inside of it. Dependancies are not easily usable, but hacking around it is fairly straightforward 😉

Just run:

## Create instruction files

After having installed `metagpt`, we can perform prompt optimization creating a yaml file specifying the task tackled.

From `metagpt` [documentation](https://github.com/geekan/MetaGPT/tree/main/examples/spo), this yaml file needs the following structure:

We will need to generate one of these template files **for each** of the prompts we are seeking to optimize. Luckily, we can do so automatically.

Also, as the tasks we're dealing with are fairly straightforward we can spare us providing few shot examples in the form Q&As 🤩

Still, these template files offer a very straightforward way to provide real-world few-shot examples so definitely worth looking into those.

## Creating model files

Once you created template files for the different prompts, you need to specify which models you need to use as (1) executors (2) evaluators and (3) optimizers for the different prompts.

metagpt's SPO requires you to provide these models within a specific `.yaml` file---you can use the following snippet to create these files using your own Mistral API key ([get one!](https://console.mistral.ai/api-keys)).

**We're good! 🎉**

Once you have (1) template files for your candidate prompts and (2) a `models.yaml` file to identify the different models you wish to use, we can get start running rounds and optimizing the prompts 😊

### A little hack: jupyter notebooks don't really work with `asyncio` 🫠

...if only jupyter notebooks worked well with `asyncio` 😂 The little hack here is to export the code you need to run prompt optimization to a `.py` file and then run that one using CLI-like instructions.

Here we are only creating one file for the job title extraction prompt. Exporting these prompt optimization processes to different files also allows for parallel execution (💨, right?). For the sake of demonstration, we are only showing how to optimize one prompt (job extraction), but you can easily switch this to other prompts yourself.

Now, let's run prompt optimization ☀️

## Asessing the results

Results indicate the original prompt is modified according to typical best-practices, such as providing examples to guide the LLM (**few-shot prompting**), or by providing tag-like elements to direct the model's attention towards particular parts of the input prompt.

This revised prompt has been obtained using only 5 optimization "rounds", and can further be optimized (although finally satisfactory performance is of course a heuristic in the context of black-box optimization)