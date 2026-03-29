---
title: Mistral Embeddings API - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-embeddings-embeddings
source: crawler
fetched_at: 2026-01-29T07:34:00.69444505-03:00
rendered_js: false
word_count: 1135
summary: A technical guide providing instructions and examples for using the Mistral Embeddings API to represent text as numerical vectors for tasks like semantic search and clustering.
tags:
    - mistral
    - embeddings
    - api
    - vectors
    - nlp
category: guide
---

Embeddings are vectorial representations of text that capture the semantic meaning of paragraphs through their position in a high dimensional vector space. Mistral Embeddings API offers cutting-edge, state-of-the-art embeddings for text, which can be used for many NLP tasks. In this guide, we will cover the fundamentals of the Mistral embeddings API, including how to measure the distance between text embeddings, and explore its main use cases: clustering and classification.

## Mistral Embeddings API

To generate text embeddings using Mistral’s embeddings API, we can make a request to the API endpoint and specify the embedding model `mistral-embed`, along with providing a list of input text. The API will then return the corresponding embeddings as numerical vectors, which can be used for further analysis or processing in NLP applications.

The output is a EmbeddingResponse object with the embeddings and the token usage information.

Let’s take a look of the length of the first embedding:

It returns 1024, which means that our embedding dimension is 1024. The `mistral-embed` model generates embedding vectors of dimension 1024 for each text string, regardless of the text length. It’s worth noting that while higher dimensional embeddings can better capture text information and improve the performance of NLP tasks, they may require more computational resources for hosting and inference, and may result in increased latency and memory usage for storing and processing these embeddings. This trade-off between performance and computational resources should be considered when designing NLP systems that rely on text embeddings.

### Distance measures

In the realm of text embeddings, texts with similar meanings or context tend to be located in closer proximity to each other within this space, as measured by the distance between their vectors. This is due to the fact that the model has learned to group semantically related texts together during the training process.

Let’s take a look at a simple example. To simplify working with text embeddings, we can wrap the embedding API in this function:

Suppose we have two sentences: one about cats and the other about books. We want to find how similar each sentence is to the reference sentence "Books are mirrors: You only see in them what you already have inside you". We can see that the distance between the reference sentence embeddings and the book sentence embeddings is smaller than the distance between the reference sentence embeddings and the cat sentence embeddings.

In our example above, we used the Euclidean distance to measure the distance between embedding vectors (note that since Mistral embeddings are norm 1, cosine similarity, dot product or Euclidean distance are all equivalent).

### Paraphrase detection

Another potential use case is paraphrase detection. In this simple example, we have a list of three sentences, and we would like to find out if any of the two sentences are paraphrases of each other. If the distance between two sentence embeddings is small, it suggests that the two sentences are semantically similar and could be potential paraphrases.

Result suggests that the first two sentences are semantically similar and could be potential paraphrases, whereas the third sentence is more different. This is just a super simple example. But this approach can be extended to more complex situations in real-world applications, such as detecting paraphrases in social media posts, news articles, or customer reviews.

### Batch processing

The Mistral Embeddings API is designed to process text in batches for improved efficiency and speed. In this example, we will demonstrate this by loading the Symptom2Disease dataset from [Kaggle](https://www.kaggle.com/datasets/niyarrbarman/symptom2disease), which contains 1200 rows with two columns: "label" and "text". The "label" column indicates the disease category, while the "text" column describes the symptoms associated with that disease.

We wrote a function `get_embeddings_by_chunks` that splits data into chunks and then sends each chunk to the Mistral embedding API to get the embeddings. Then we saved the embeddings as a new column in the dataframe. Note that the Mistral Embeddings API will provide auto-chunking in the future, so that users don’t need to manually split the data into chunks before sending it to the API.

## t-SNE embeddings visualization

We mentioned previously that our embeddings have 1024 dimensions, which makes them impossible to visualize directly. Thus, in order to visualize our embeddings, we can use a dimensionality reduction technique such as t-SNE to project our embeddings into a lower-dimensional space that is easier to visualize.

In this example, we transform our embeddings to 2 dimensions and create a 2D scatter plot showing the relationships among embeddings of different diseases.

#### Comparison with fasttext

We can compare it with fastText, a popular open-source embeddings model. However, when examining the t-SNE embeddings plot, we notice that fastText embeddings fail to create clear separations between data points with matching labels.

## Classification

Text embeddings can be used as input features in machine learning models, such as classification and clustering. In this example, we use a classification model to predict the disease labels from the embeddings of disease description text.

#### Comparison with fasttext

Additionally, let’s take a look at the performance using fastText embeddings in this classification task. It appears that the classification model achieves better performance with Mistral embedding models as compared to using fastText embeddings.

## Clustering

What if we don’t have disease labels? One approach to gain insights from the data is through clustering. Clustering is an unsupervised machine learning technique that groups similar data points together based on their similarity with respect to certain features. In the context of text embeddings, we can use the distance between each embedding as a measure of similarity, and group together data points with embeddings that are close to each other in the high-dimensional space.

Since we already know there are 24 clusters, let’s use the K-means clustering with 24 clusters. Then we can inspect a few examples and verify whether the examples in a single cluster are similar to one another. For example, take a look at the first three rows of cluster 23. We can see that they look very similar in terms of symptoms.

## Retrieval

Our embedding model excels in retrieval tasks, as it is trained with retrieval in mind. Embeddings are also incredibly helpful in implementing retrieval-augmented generation (RAG) systems, which use retrieved relevant information from a knowledge base to generate responses. At a high-level, we embed a knowledge base, whether it is a local directory, text files, or internal wikis, into text embeddings and store them in a vector database. Then, based on the user's query, we retrieve the most similar embeddings, which represent the relevant information from the knowledge base. Finally, we feed these relevant embeddings to a large language model to generate a response that is tailored to the user's query and context. If you are interested in learning more about how RAG systems work and how to implement a basic RAG, check out our [previous guide](https://github.com/mistralai/cookbook/blob/main/mistral/rag/basic_RAG.ipynb) on this topic.