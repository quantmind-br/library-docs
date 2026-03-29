---
title: KNN - DSPy
url: https://dspy.ai/api/optimizers/KNN/
source: sitemap
fetched_at: 2026-01-23T08:02:20.01859344-03:00
rendered_js: false
word_count: 81
summary: This document provides a technical specification for the dspy.KNN class, which retrieves the most similar training examples using vector embeddings and k-nearest neighbors logic.
tags:
    - dspy
    - knn-retriever
    - vector-embeddings
    - similarity-search
    - nearest-neighbor
    - data-retrieval
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/optimizers/KNN.md "Edit this page")

## `dspy.KNN(k: int, trainset: list[Example], vectorizer: Embedder)` [¶](#dspy.KNN "Permanent link")

A k-nearest neighbors retriever that finds similar examples from a training set.

Parameters:

Name Type Description Default `k` `int`

Number of nearest neighbors to retrieve

*required* `trainset` `list[Example]`

List of training examples to search through

*required* `vectorizer` `Embedder`

The `Embedder` to use for vectorization

*required*

Example

```
importdspy
fromsentence_transformersimport SentenceTransformer

# Create a training dataset with examples
trainset = [
    dspy.Example(input="hello", output="world"),
    # ... more examples ...
]

# Initialize KNN with a sentence transformer model
knn = KNN(
    k=3,
    trainset=trainset,
    vectorizer=dspy.Embedder(SentenceTransformer("all-MiniLM-L6-v2").encode)
)

# Find similar examples
similar_examples = knn(input="hello")
```

Source code in `dspy/predict/knn.py`

````
def__init__(self, k: int, trainset: list[Example], vectorizer: Embedder):
"""
    A k-nearest neighbors retriever that finds similar examples from a training set.

    Args:
        k: Number of nearest neighbors to retrieve
        trainset: List of training examples to search through
        vectorizer: The `Embedder` to use for vectorization

    Example:
        ```python
        import dspy
        from sentence_transformers import SentenceTransformer

        # Create a training dataset with examples
        trainset = [
            dspy.Example(input="hello", output="world"),
            # ... more examples ...
        ]

        # Initialize KNN with a sentence transformer model
        knn = KNN(
            k=3,
            trainset=trainset,
            vectorizer=dspy.Embedder(SentenceTransformer("all-MiniLM-L6-v2").encode)
        )

        # Find similar examples
        similar_examples = knn(input="hello")
        ```
    """
    self.k = k
    self.trainset = trainset
    self.embedding = vectorizer
    trainset_casted_to_vectorize = [
        " | ".join([f"{key}: {value}" for key, value in example.items() if key in example._input_keys])
        for example in self.trainset
    ]
    self.trainset_vectors = self.embedding(trainset_casted_to_vectorize).astype(np.float32)
````

### Functions[¶](#dspy.KNN-functions "Permanent link")

#### `__call__(**kwargs) -> list` [¶](#dspy.KNN.__call__ "Permanent link")

Source code in `dspy/predict/knn.py`

```
def__call__(self, **kwargs) -> list:
    input_example_vector = self.embedding([" | ".join([f"{key}: {val}" for key, val in kwargs.items()])])
    scores = np.dot(self.trainset_vectors, input_example_vector.T).squeeze()
    nearest_samples_idxs = scores.argsort()[-self.k :][::-1]
    return [self.trainset[cur_idx] for cur_idx in nearest_samples_idxs]
```

:::