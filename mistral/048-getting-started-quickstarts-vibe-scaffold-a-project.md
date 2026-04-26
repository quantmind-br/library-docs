---
title: Scaffold a project with Mistral Vibe | Mistral Docs
url: https://docs.mistral.ai/getting-started/quickstarts/vibe/scaffold-a-project
source: sitemap
fetched_at: 2026-04-26T04:07:33.619084343-03:00
rendered_js: false
word_count: 332
summary: This document provides a walkthrough on how to use Mistral Vibe to scaffold a complete software project from a natural-language description while maintaining control through step-by-step change confirmation.
tags:
    - mistral-vibe
    - project-scaffolding
    - natural-language-processing
    - code-generation
    - development-workflow
category: tutorial
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Use [Mistral Vibe](https://docs.mistral.ai/mistral-vibe/overview) to generate a full project structure from a natural-language description, review every change before Mistral Vibe applies it, and run the result.

**What you get:**
- **Natural-language scaffolding**: describe what you want and Mistral Vibe creates the files
- **Step-by-step confirmation**: Mistral Vibe splits large tasks into steps and asks for approval
- **Full preview**: see every file change before it is written to disk

**Time to complete:** ~10 minutes

**Prerequisites:** Mistral Vibe installed and configured. Complete [[047-getting-started-quickstarts-vibe-install-and-first-prompt]] first if needed.

## Steps

Start in a fresh directory so Mistral Vibe generates the project from scratch. Mistral Vibe starts with an empty context.

### Describe Your Project

Give Mistral Vibe a clear description of what you want to build. Be specific about language, framework, and key features:

> Create a Python Flask API with two endpoints: a /health endpoint that returns `{"status": "ok"}` and a /predict endpoint that accepts a JSON body with a "text" field and returns `{"label": "positive", "score": 0.95}`. Include a requirements.txt and a README.

### Review and Approve

Mistral Vibe breaks the request into steps and begins generating files. Before creating or editing any file, Mistral Vibe shows a preview of the changes.

![Mistral Vibe showing a preview of changes and asking for confirmation](https://docs.mistral.ai/assets/quickstarts/vibe/demo.png)

For each step, Mistral Vibe displays:
1. The files it plans to create or modify
2. The content of each file
3. A confirmation prompt

Review the changes and type `y` to approve, or provide feedback to adjust the output. After each approved step, Mistral Vibe shows the result.

![Mistral Vibe displaying generated output and completed steps](https://docs.mistral.ai/assets/quickstarts/vibe/results.png)

Continue approving steps until the project is complete.

## Verify the Project

Check that the project was created:

```bash
ls
```

You should see the files Mistral Vibe generated (e.g., `app.py`, `requirements.txt`, `README.md`).

Run the project to confirm it works:

```bash
python app.py
```

Test the endpoints:

```bash
curl http://localhost:5000/health
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"text": "great product"}'
```

Both endpoints should return valid JSON responses.

#mistral-vibe #project-scaffolding #code-generation