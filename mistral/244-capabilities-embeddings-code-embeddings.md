---
title: Code Embeddings | Mistral Docs
url: https://docs.mistral.ai/capabilities/embeddings/code_embeddings
source: crawler
fetched_at: 2026-01-29T07:34:12.974020431-03:00
rendered_js: false
word_count: 494
---

Embeddings are at the core of multiple enterprise use cases, such as **retrieval systems**, **clustering**, **code analytics**, **classification**, and a variety of search applications. With code embedings, you can embed **code databases** and **repositories**, and power **coding assistants** with state-of-the-art retrieval capabilities.

[Open in Colab ↗](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/embeddings/code_embedding.ipynb)

### How to Generate Embeddings

To generate code embeddings using Mistral AI's embeddings API, we can make a request to the API endpoint and specify the embedding model `codestral-embed`, along with providing a list of input texts. The API will then return the corresponding embeddings as numerical vectors, which can be used for further analysis or processing in NLP applications.

We also provide `output_dtype` and `output_dimension` parameters that allow you to control the type and dimensional size of your embeddings.

`output_dtype` allows you to select the precision and format of the embeddings, enabling you to obtain embeddings with your desired level of numerical accuracy and representation.

The accepted dtypes are:

- **float** (default): A list of 32-bit (4-byte) single-precision floating-point numbers. Provides the highest precision and retrieval accuracy.
- **int8**: A list of 8-bit (1-byte) integers ranging from -128 to 127.
- **uint8**: A list of 8-bit (1-byte) integers ranging from 0 to 255.
- **binary**: A list of 8-bit integers that represent bit-packed, quantized single-bit embedding values using the `int8` type. The length of the returned list of integers is 1/8 of `output_dimension`. This type uses the offset binary method.
- **ubinary**: Similar to `binary`, but uses the `uint8` type for bit-packed, quantized single-bit embedding values.

`output_dimension` allows you to select a specific size for the embedding, enabling you to obtain an embedding of your chosen dimension, **defaults to 1536** and has a **maximum value of 3072**.

For any integer target dimension n, you can choose to retain the first n dimensions. These dimensions are ordered by relevance, and the first n are selected for a smooth trade-off between quality and cost.

Below is an example of how to use the embeddings API to generate embeddings for a list of input texts code related.

Let's take a look at the length of the first embedding:

It returns 1553, which means that our embedding dimension is 1553. The `codestral-embed` model generates embedding vectors up to dimensions of 3072 for each text string, regardless of the text length, you can reduce the dimension using `output_dimension` if needed. It's worth nothing that while higher dimensional embeddings can better capture text information and improve the performance of NLP tasks, they may require more resources and may result in increased latency and memory usage for storing and processing these embeddings. This trade-off between performance and computational resources should be considered when designing NLP systems that rely on text embeddings.

Below you will find some examples of how to use the Codestral Embeddings API and different use cases.

![Cat head](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fcat_head.png&w=48&q=75)

¡Meow! Click one of the tabs above to learn more.

For more information and guides on how to make use of our embedding sdk, we have the following cookbooks: