---
title: Custom Status Report
url: https://lmstudio.ai/docs/typescript/plugins/prompt-preprocessor/custom-status-report
source: sitemap
fetched_at: 2026-04-07T21:32:22.06030964-03:00
rendered_js: false
word_count: 66
summary: This document demonstrates how to manage and report the processing status of a prompt preprocessor using `ctl.setStatus` and updating it with different states, including sub-statuses.
tags:
    - status-management
    - prompt-preprocessing
    - api-calls
    - state-updates
category: tutorial
---

Depending on the task, the prompt preprocessor may take some time to complete, for example, it may need to fetch some data from the internet or perform some heavy computation. In such cases, you can report the status of the preprocessing using `ctl.setStatus`.

src/promptPreprocessor.ts

```
const status = ctl.createStatus({
  status: "loading",
  text: "Preprocessing.",
});
```

You can update the status at any time by calling `status.setState`.

src/promptPreprocessor.ts

```
status.setState({
  status: "done",
  text: "Preprocessing done.",
})
```

You can even add sub status to the status:

src/promptPreprocessor.ts

```
const subStatus = status.addSubStatus({
  status: "loading",
  text: "I am a sub status."
});
```