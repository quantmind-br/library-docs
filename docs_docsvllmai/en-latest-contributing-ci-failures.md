---
title: CI Failures - vLLM
url: https://docs.vllm.ai/en/latest/contributing/ci/failures/
source: sitemap
fetched_at: 2026-05-07T21:11:23.334195534-03:00
rendered_js: false
word_count: 290
summary: This document provides instructions for troubleshooting, reporting, and reproducing continuous integration (CI) failures within the vLLM project repository.
tags:
    - ci-testing
    - debug-workflow
    - github-actions
    - buildkite
    - issue-tracking
    - developer-guidelines
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/contributing/ci/failures.md "Edit this page")

What should I do when a CI job fails on my PR, but I don't think my PR caused the failure?

- Check the dashboard of current CI test failures:  
  👉 [CI Failures Dashboard](https://github.com/orgs/vllm-project/projects/20)
- If your failure **is already listed**, it's likely unrelated to your PR. Help fixing it is always welcome!
  
  - Leave comments with links to additional instances of the failure.
  - React with a 👍 to signal how many are affected.
- If your failure **is not listed**, you should **file an issue**.

## Filing a CI Test Failure Issue[¶](#filing-a-ci-test-failure-issue "Permanent link")

- **File a bug report:**  
  👉 [New CI Failure Report](https://github.com/vllm-project/vllm/issues/new?template=450-ci-failure.yml)
- **Use this title format:**
  
  ```
  [CI Failure]: failing-test-job - regex/matching/failing:test
  ```
- **For the environment field:**
  
  ```
  Still failing on main as of commit abcdef123
  ```
- **In the description, include failing tests:**
  
  ```
  FAILED failing/test.py:failing_test1 - Failure description
  FAILED failing/test.py:failing_test2 - Failure description
  https://github.com/orgs/vllm-project/projects/20
  https://github.com/vllm-project/vllm/issues/new?template=400-bug-report.yml
  FAILED failing/test.py:failing_test3 - Failure description
  ```
- **Attach logs** (collapsible section example):
  
  Logs:
  
  ```
  ERROR 05-20 03:26:38 [dump_input.py:68] Dumping input data
  --- Logging error ---  
  Traceback (most recent call last):  
    File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 203, in execute_model  
      return self.model_executor.execute_model(scheduler_output)
  ...
  FAILED failing/test.py:failing_test1 - Failure description
  FAILED failing/test.py:failing_test2 - Failure description
  FAILED failing/test.py:failing_test3 - Failure description
  ```

## Logs Wrangling[¶](#logs-wrangling "Permanent link")

Download a job's log (no Buildkite login required):

[.buildkite/scripts/ci-fetch-log.sh](https://github.com/vllm-project/vllm/blob/main/.buildkite/scripts/ci-fetch-log.sh)

```
# Find the failing job. Each row's URL is .../builds/<N>#<job_uuid>:
ghprchecks<PR>--repovllm-project/vllm

# Download + strip timestamps/ANSI in one step:
.buildkite/scripts/ci-fetch-log.sh"https://buildkite.com/vllm/ci/builds/<N>#<job_uuid>"
```

To clean an already-downloaded log:

[.buildkite/scripts/ci-clean-log.sh](https://github.com/vllm-project/vllm/blob/main/.buildkite/scripts/ci-clean-log.sh)

Use a tool [wl-clipboard](https://github.com/bugaevc/wl-clipboard) for quick copy-pasting:

```
tail-525ci_build.log|wl-copy
```

## Investigating a CI Test Failure[¶](#investigating-a-ci-test-failure "Permanent link")

1. Go to 👉 [Buildkite main branch](https://buildkite.com/vllm/ci/builds?branch=main)
2. Bisect to find the first build that shows the issue.
3. Add your findings to the GitHub issue.
4. If you find a strong candidate PR, mention it in the issue and ping contributors.

## Reproducing a Failure[¶](#reproducing-a-failure "Permanent link")

CI test failures may be flaky. Use a bash loop to run repeatedly:

[.buildkite/scripts/rerun-test.sh](https://github.com/vllm-project/vllm/blob/main/.buildkite/scripts/rerun-test.sh)

```
./rerun-test.shtests/v1/engine/test_engine_core_client.py::test_kv_cache_events[True-tcp]
```

## Submitting a PR[¶](#submitting-a-pr "Permanent link")

If you submit a PR to fix a CI failure:

- Link the PR to the issue: Add `Closes #12345` to the PR description.
- Add the `ci-failure` label: This helps track it in the [CI Failures GitHub Project](https://github.com/orgs/vllm-project/projects/20).

## Other Resources[¶](#other-resources "Permanent link")

- 🔍 [Test Reliability on `main`](https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests?branch=main&order=ASC&sort_by=reliability)
- 🧪 [Latest Buildkite CI Runs](https://buildkite.com/vllm/ci/builds?branch=main)

## Daily Triage[¶](#daily-triage "Permanent link")

Use [Buildkite analytics (2-day view)](https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests?branch=main&period=2days) to:

- Identify recent test failures **on `main`** .
- Exclude legitimate test failures on PRs.
- (Optional) Ignore tests with 0% reliability.

Compare to the [CI Failures Dashboard](https://github.com/orgs/vllm-project/projects/20).