---
title: Chunking - Crawl4AI Documentation (v0.8.x)
url: https://docs.crawl4ai.com/extraction/chunking/
source: sitemap
fetched_at: 2026-04-26T07:47:32.343322569-03:00
rendered_js: false
word_count: 199
summary: This document explores various text chunking strategies used to segment large documents into manageable units for enhanced processing, semantic analysis, and retrieval-augmented generation systems.
tags:
    - chunking-strategies
    - text-processing
    - natural-language-processing
    - rag
    - cosine-similarity
    - data-segmentation
category: guide
---

## Chunking Strategies

Chunking strategies are critical for dividing large texts into manageable parts, enabling effective content processing and extraction. These strategies are foundational in cosine similarity-based extraction techniques, which allow users to retrieve only the most relevant chunks of content for a given query. Additionally, they facilitate direct integration into RAG (Retrieval-Augmented Generation) systems for structured and scalable workflows.

### Why Use Chunking?

1. **Cosine Similarity and Query Relevance**: Prepares chunks for semantic similarity analysis. 2. **RAG System Integration**: Seamlessly processes and stores chunks for retrieval. 3. **Structured Processing**: Allows for diverse segmentation methods, such as sentence-based, topic-based, or windowed approaches.

### Methods of Chunking

#### 1. Regex-Based Chunking

Splits text based on regular expression patterns, useful for coarse segmentation.

**Code Example**:

```
classRegexChunking:
    def__init__(self, patterns=None):
        self.patterns = patterns or [r'\n\n']  # Default pattern for paragraphs

    defchunk(self, text):
        paragraphs = [text]
        for pattern in self.patterns:
            paragraphs = [seg for p in paragraphs for seg in re.split(pattern, p)]
        return paragraphs

# Example Usage
text = """This is the first paragraph.

This is the second paragraph."""
chunker = RegexChunking()
print(chunker.chunk(text))
```

#### 2. Sentence-Based Chunking

Divides text into sentences using NLP tools, ideal for extracting meaningful statements.

**Code Example**:

```
fromnltk.tokenizeimport sent_tokenize

classNlpSentenceChunking:
    defchunk(self, text):
        sentences = sent_tokenize(text)
        return [sentence.strip() for sentence in sentences]

# Example Usage
text = "This is sentence one. This is sentence two."
chunker = NlpSentenceChunking()
print(chunker.chunk(text))
```

#### 3. Topic-Based Segmentation

Uses algorithms like TextTiling to create topic-coherent chunks.

**Code Example**:

```
fromnltk.tokenizeimport TextTilingTokenizer

classTopicSegmentationChunking:
    def__init__(self):
        self.tokenizer = TextTilingTokenizer()

    defchunk(self, text):
        return self.tokenizer.tokenize(text)

# Example Usage
text = """This is an introduction.
This is a detailed discussion on the topic."""
chunker = TopicSegmentationChunking()
print(chunker.chunk(text))
```

#### 4. Fixed-Length Word Chunking

Segments text into chunks of a fixed word count.

**Code Example**:

```
classFixedLengthWordChunking:
    def__init__(self, chunk_size=100):
        self.chunk_size = chunk_size

    defchunk(self, text):
        words = text.split()
        return [' '.join(words[i:i + self.chunk_size]) for i in range(0, len(words), self.chunk_size)]

# Example Usage
text = "This is a long text with many words to be chunked into fixed sizes."
chunker = FixedLengthWordChunking(chunk_size=5)
print(chunker.chunk(text))
```

#### 5. Sliding Window Chunking

Generates overlapping chunks for better contextual coherence.

**Code Example**:

```
classSlidingWindowChunking:
    def__init__(self, window_size=100, step=50):
        self.window_size = window_size
        self.step = step

    defchunk(self, text):
        words = text.split()
        chunks = []
        for i in range(0, len(words) - self.window_size + 1, self.step):
            chunks.append(' '.join(words[i:i + self.window_size]))
        return chunks

# Example Usage
text = "This is a long text to demonstrate sliding window chunking."
chunker = SlidingWindowChunking(window_size=5, step=2)
print(chunker.chunk(text))
```

### Combining Chunking with Cosine Similarity

To enhance the relevance of extracted content, chunking strategies can be paired with cosine similarity techniques. Here’s an example workflow:

**Code Example**:

```
fromsklearn.feature_extraction.textimport TfidfVectorizer
fromsklearn.metrics.pairwiseimport cosine_similarity

classCosineSimilarityExtractor:
    def__init__(self, query):
        self.query = query
        self.vectorizer = TfidfVectorizer()

    deffind_relevant_chunks(self, chunks):
        vectors = self.vectorizer.fit_transform([self.query] + chunks)
        similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
        return [(chunks[i], similarities[i]) for i in range(len(chunks))]

# Example Workflow
text = """This is a sample document. It has multiple sentences. 
We are testing chunking and similarity."""

chunker = SlidingWindowChunking(window_size=5, step=3)
chunks = chunker.chunk(text)
query = "testing chunking"
extractor = CosineSimilarityExtractor(query)
relevant_chunks = extractor.find_relevant_chunks(chunks)

print(relevant_chunks)
```