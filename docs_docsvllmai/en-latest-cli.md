---
title: vLLM CLI Guide - vLLM
url: https://docs.vllm.ai/en/latest/cli/
source: sitemap
fetched_at: 2026-05-07T21:10:56.295062924-03:00
rendered_js: false
word_count: 237
summary: This document provides an overview of the vLLM command-line interface, detailing commands for serving models, performing inference, running benchmarks, and processing batch jobs.
tags:
    - vllm
    - command-line-interface
    - model-serving
    - benchmarking
    - inference
    - cli-tools
category: reference
---

[](https://github.com/vllm-project/vllm/edit/main/docs/cli/README.md "Edit this page")

The vllm command-line tool is used to run and manage vLLM models. You can start by viewing the help message with:

Available Commands:

```
vllm{chat,complete,serve,bench,collect-env,run-batch}
```

## serve[¶](#serve "Permanent link")

Starts the vLLM OpenAI Compatible API server.

Start with a model:

```
vllmservemeta-llama/Llama-2-7b-hf
```

Specify the port:

```
vllmservemeta-llama/Llama-2-7b-hf--port8100
```

Serve over a Unix domain socket:

```
vllmservemeta-llama/Llama-2-7b-hf--uds/tmp/vllm.sock
```

Check with --help for more options:

```
# To list all groups
vllmserve--help=listgroup

# To view a argument group
vllmserve--help=ModelConfig

# To view a single argument
vllmserve--help=max-num-seqs

# To search by keyword
vllmserve--help=max

# To view full help with pager (less/more)
vllmserve--help=page
```

See [vllm serve](https://docs.vllm.ai/en/latest/cli/serve/) for the full reference of all available arguments.

## chat[¶](#chat "Permanent link")

Generate chat completions via the running API server.

```
# Directly connect to localhost API without arguments
vllmchat

# Specify API url
vllmchat--urlhttp://{vllm-serve-host}:{vllm-serve-port}/v1

# Quick chat with a single prompt
vllmchat--quick"hi"
```

See [vllm chat](https://docs.vllm.ai/en/latest/cli/chat/) for the full reference of all available arguments.

## complete[¶](#complete "Permanent link")

Generate text completions based on the given prompt via the running API server.

```
# Directly connect to localhost API without arguments
vllmcomplete

# Specify API url
vllmcomplete--urlhttp://{vllm-serve-host}:{vllm-serve-port}/v1

# Quick complete with a single prompt
vllmcomplete--quick"The future of AI is"
```

See [vllm complete](https://docs.vllm.ai/en/latest/cli/complete/) for the full reference of all available arguments.

## bench[¶](#bench "Permanent link")

Run benchmark tests for latency online serving throughput and offline inference throughput.

To use benchmark commands, please install with extra dependencies using `pip install vllm[bench]`.

Available Commands:

```
vllmbench{latency,serve,throughput}
```

### latency[¶](#latency "Permanent link")

Benchmark the latency of a single batch of requests.

```
vllmbenchlatency\
--modelmeta-llama/Llama-3.2-1B-Instruct\
--input-len32\
--output-len1\
--enforce-eager\
--load-formatdummy
```

See [vllm bench latency](https://docs.vllm.ai/en/latest/cli/bench/latency/) for the full reference of all available arguments.

### serve[¶](#serve_1 "Permanent link")

Benchmark the online serving throughput.

```
vllmbenchserve\
--modelmeta-llama/Llama-3.2-1B-Instruct\
--hostserver-host\
--portserver-port\
--random-input-len32\
--random-output-len4\
--num-prompts5
```

See [vllm bench serve](https://docs.vllm.ai/en/latest/cli/bench/serve/) for the full reference of all available arguments.

### throughput[¶](#throughput "Permanent link")

Benchmark offline inference throughput.

```
vllmbenchthroughput\
--modelmeta-llama/Llama-3.2-1B-Instruct\
--input-len32\
--output-len1\
--enforce-eager\
--load-formatdummy
```

See [vllm bench throughput](https://docs.vllm.ai/en/latest/cli/bench/throughput/) for the full reference of all available arguments.

## collect-env[¶](#collect-env "Permanent link")

Start collecting environment information.

## run-batch[¶](#run-batch "Permanent link")

Run batch prompts and write results to file.

Running with a local file:

```
vllmrun-batch\
-ifeatures/openai_batch/openai_example_batch.jsonl\
-oresults.jsonl\
--modelmeta-llama/Meta-Llama-3-8B-Instruct
```

Using remote file:

```
vllmrun-batch\
-ihttps://raw.githubusercontent.com/vllm-project/vllm/main/examples/features/openai_batch/openai_example_batch.jsonl\
-oresults.jsonl\
--modelmeta-llama/Meta-Llama-3-8B-Instruct
```

See [vllm run-batch](https://docs.vllm.ai/en/latest/cli/run-batch/) for the full reference of all available arguments.

## More Help[¶](#more-help "Permanent link")

For detailed options of any subcommand, use: