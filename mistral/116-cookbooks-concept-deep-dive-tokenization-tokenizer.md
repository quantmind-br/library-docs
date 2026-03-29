---
title: Tokenizer - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-tokenizer
source: crawler
fetched_at: 2026-01-29T07:34:53.473654753-03:00
rendered_js: false
word_count: 815
summary: This document explains the fundamental role of tokenizers in language models, covering the processes of encoding and decoding, different tokenization methods, and the trade-offs involved in vocabulary size and efficiency.
tags:
    - tokenization
    - nlp
    - large-language-models
    - byte-pair-encoding
    - sentencepiece
    - text-encoding
category: concept
---

## Introduction

A tokenizer has the role of converting a request, often a string, into a sequence of token IDs that the model will receive as input. A token can be anything from a single character to a subword or a symbol. The model possesses a vocabulary of tokens with their corresponding IDs. The tokenizer's job is to break apart the string and convert it into a sequence of token IDs, a step called "encoding." It is also the tokenizer's job to convert a sequence of IDs back into a string, a step called "decoding." Once provided with a sequence of token IDs, the model tries to predict the next token.

For simplicity, let's describe tokens as full words.

Imagine a scenario where we have the following sentence: "Hello, how are"

### Encoding

1. The tokenizer will first break apart the sentence into different pieces, or tokens. For example:
   
   - `Hello,`
   - `how`
   - `are`
2. The tokenizer will then get the token ID corresponding to each token. For example:
   
   - `Hello,` -&gt; `432`
   - `how` -&gt; `523`
   - `are` -&gt; `87`
   
   This sequence of token IDs is then provided to the model.

### Decoding

1. The model will try to predict the next token. Let's say it predicts:
   
   - `75`
   
   We will then have a full sequence of token IDs:
   
   - `432` + `523` + `87` + `75`
2. This sequence can be decoded back into a full string:
   
   - `Hello,` + `how` + `are` + `you` -&gt; `Hello, how are you`

## Types of Tokenizers

There are multiple ways to make tokenizers with various approaches...

### ASCII/Character-Based Tokenizer

A simple tokenizer is the ASCII/Character-based tokenizer, where each character and ASCII symbol is treated as a token. This approach is straightforward but has several drawbacks:

- **Slow Prediction**: Predicting symbol after symbol is inefficient.
- **Statistical Errors**: Prone to errors due to the granularity of the tokens.
- **Information/Sequence Length Ratio**: Lower ratio of information per sequence length.

### Word-Based Tokenizer

Another type is the word-based tokenizer, where each word is considered a token. While this may seem intuitive, it is not optimized. For example, consider the following words:

- "fast"
- "fastest"
- "faster"
- "slow"
- "slowest"
- "slower"

A word-based tokenizer would translate these into 6 tokens. However, a more efficient approach would be to use subword tokens:

- "fast"
- "est"
- "er"
- "slow"

With only 4 tokens, we can reproduce the original 6 words by combining them.

### BPE and More

Byte Pair Encoding (BPE) is a simple form of data compression technique used in tokenization. It works by iteratively merging the most frequent bigram (pair of consecutive tokens) in the text. This process continues until the desired vocabulary size is reached. BPE is particularly useful for handling out-of-vocabulary words by breaking them down into subword units!

#### Example

Let's consider a simple example to understand BPE better. Suppose we have the following text:

We'll start with each character as a separate token:

The objective will be to train a tokenizer with, for this example, a vocabulary size of 5, meaning 5 unique tokens.

##### Step 1: Initial Tokens

-&gt; 8 tokens

##### Step 2: Merge the Most Frequent Bigram

The most frequent bigram is `l` and `o`. We merge them to form a new token `lo`.

##### Step 3: New tokens

-&gt; 7 tokens

##### Step 4: Merge again Most Frequent Bigram

The next most frequent bigram is `lo` and `w`. We merge them to form a new token `low`.

##### Step 5: New tokens

-&gt; 7 tokens

##### Repeat this process...

Repeat the procedure until reaching the vocab size desired, in the end will look like this:

##### Final Tokens

-&gt; 5 tokens

The process of building a tokenizer that is efficient and compresses the knowledge well for your model is a crucial step towards efficient language models, with a lot of trade-offs to consider.

## Trade-offs in Tokenization

The trade-offs between vocabulary size, length, and compression ratio are critical in the world of LLMs for several reasons:

- **Model Efficiency**: Smaller vocabulary sizes can lead to faster training and inference times.
- **Memory Usage**: Larger vocabularies require more memory.
- **Generalization**: Subword tokenization can help the model generalize better by capturing common subword patterns.

## Make your own Tokenizer

Let's make a tokenizer using the `sentencepiece` library and BPE.

### Step 1: Obtain Training Data

First, we need a large text dataset to train our tokenizer. For this example, we'll use a subset of Wikipedia.

### Step 2: Train the Tokenizer

We can train a tokenizer quickly using the `sentencepiece` library.

### Step 3: Encode Example

Let's encode a simple example to see how the tokenizer works.

Note: `sentencepiece` by default will prefix a dummy whitespace while encoding, so it's important to be aware of this.

We can quickly see the impact of the vocabulary size by training a new tokenizer with a larger vocabulary size, lets say `vocab_size = 8192`.

## That's not all

There is more to building a tokenizer, especially when considering [control tokens](https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-control_tokens). Building a proper tokenizer is an important step for good performance, efficiency, and compression ratio of your models!