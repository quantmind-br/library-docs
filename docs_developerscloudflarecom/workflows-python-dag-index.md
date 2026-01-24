---
title: DAG Workflows · Cloudflare Workflows docs
url: https://developers.cloudflare.com/workflows/python/dag/index.md
source: llms
fetched_at: 2026-01-24T15:34:13.642169546-03:00
rendered_js: false
word_count: 104
summary: This document explains how to define directed acyclic graph dependencies in the Python Workflows SDK using the step.do decorator and depends parameter. It demonstrates how to orchestrate concurrent step execution and manage step-level dependencies for complex workflow patterns.
tags:
    - python-workflows-sdk
    - dag-workflows
    - step-dependencies
    - concurrent-execution
    - workflow-orchestration
category: guide
---

The Python Workflows SDK supports DAG workflows in a declarative way, using the `step.do` decorator with the `depends` parameter to define dependencies (other steps that must complete before this step can run).

```python
from workers import Response, WorkflowEntrypoint


class PythonWorkflowStarter(WorkflowEntrypoint):
    async def run(self, event, step):
        async def await_step(fn):
            try:
                return await fn()
            except TypeError as e:
                print(f"Successfully caught {type(e).__name__}: {e}")


        step.sleep('demo sleep', '10 seconds')


        @step.do('dependency1')
        async def dep_1():
            # does stuff
            print('executing dep1')


        @step.do('dependency2')
        async def dep_2():
            # does stuff
            print('executing dep2')


        @step.do('demo do', depends=[dep_1, dep_2], concurrent=True)
        async def final_step(res1, res2):
            # does stuff
            print('something')


        await await_step(final_step)


async def on_fetch(request, env):
    await env.MY_WORKFLOW.create()
    return Response("Hello world!")
```

On this example, `dep_1` and `dep_2` are run concurrently before execution of `final_step`, which depends on both of them.

Having `concurrent=True` allows the dependencies to be resolved concurrently. If one of the callables passed to `depends` has already completed, it will be skipped and its return value will be reused.

This pattern is useful for diamond shaped workflows, where a step depends on two or more other steps that can run concurrently.