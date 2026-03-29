---
title: LiteLLM Prompt Management (GitOps) | liteLLM
url: https://docs.litellm.ai/docs/proxy/native_litellm_prompt
source: sitemap
fetched_at: 2026-01-21T19:53:06.770721869-03:00
rendered_js: false
word_count: 18
summary: This document explains how to use LiteLLM to load and execute prompts stored as .prompt files from local directories, BitBucket, or GitLab repositories.
tags:
    - litellm
    - prompt-management
    - dotprompt
    - version-control-integration
    - gitlab-integration
    - bitbucket-integration
category: guide
---

Store prompts as `.prompt` files in your repository and use them directly with LiteLLM. No external services required.

```
model: dotprompt/<base_model>     # required (e.g., dotprompt/gpt-4)
prompt_id: str                    # required - the .prompt filename without extension
prompt_variables: Optional[dict]  # optional - variables for template rendering
```

```
model: bitbucket/<base_model>     # required (e.g., bitbucket/gpt-4)
prompt_id: str                    # required - the .prompt filename without extension
prompt_variables: Optional[dict]  # optional - variables for template rendering
bitbucket_config: Optional[dict]  # optional - BitBucket configuration (if not set globally)
```

```
model: gitlab/<base_model>        # required (e.g., gitlab/gpt-4)
prompt_id: str                    # required - the .prompt filename without extension
prompt_variables: Optional[dict]  # optional - variables for template rendering
gitlab_config: Optional[dict]     # optional - Gitlab configuration (if not set globally)
```

```
# File system integration
response = litellm.completion(
    model="dotprompt/gpt-4",
    prompt_id="hello",
    prompt_variables={"user_message":"Hello world"},
    messages=[{"role":"user","content":"This will be ignored"}]
)

# BitBucket integration
response = litellm.completion(
    model="bitbucket/gpt-4",
    prompt_id="hello",
    prompt_variables={"user_message":"Hello world"},
    bitbucket_config={
"workspace":"your-workspace",
"repository":"your-repo",
"access_token":"your-token"
}
)

# Gitlab integration
response = litellm.completion(
    model="gitlab/gpt-4",
    prompt_id="hello",
    prompt_variables={"user_message":"Hello world"},
    gitlab_config={
"project":"a/b/<repo_name>",
"access_token":"your-access-token",
"base_url":"gitlab url",
"prompts_path":"src/prompts",# folder to point to, defaults to root
"branch":"main"# optional, defaults to main
}
)
```