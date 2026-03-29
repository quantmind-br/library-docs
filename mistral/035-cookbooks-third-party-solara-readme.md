---
title: Chat with Your PDF using Mistral and Solara - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-solara-readme
source: crawler
fetched_at: 2026-01-29T07:34:03.634137782-03:00
rendered_js: false
word_count: 495
---

*Author: Alonso Silva Allende (Nokia Bell Labs), GitHub handle: [alonsosilvaallende](https://docs.mistral.ai/cookbooks/third_party-solara-readme)*

In this guide, we introduce the basics of building a chatbot with chat and PDF reading capabilities using `solara`

## Chat Interface

Let's implement a simple chat interface. To do this, we need to import `solara` and `mistralai` libraries.

*This demo uses `solara===1.41.0` and `mistralai===1.2.3`*

Create your `client` using your Mistral API key.

Let's initialize a reactive variable where all messages will be stored.

Given a list of messages (for the moment empty but not for long), we query Mistral and retrieve the response. To make the interaction smooth, we handle it by streaming the response. For this, we define a generator.

We stream the response by displaying each chunk as it is received.

Given a list of messages, we display them on the screen:

The following step is to retrieve the input from the user and store it in the list of messages. For this, we will use `ChatInput` from `solara`

We need to handle a streamed response. Therefore we create a task which will be activated by a change on the number of user messages.

That's it! An interface where you can chat with Mistral's models. I added some optional styling below.

To run this code, enter `solara run chat.py` in the console. Alternatively, you can modify it directly in [PyCafe](https://docs.mistral.ai/cookbooks/third_party-solara-readme).

## Chatting with PDFs

To enable our model to read PDFs, we need to convert the content, extract the text, and then use Mistral's embedding model to retrieve chunks of our document(s) to feed to the model. We need to implement some basic RAG (Retrieval-Augmented Generation)!

For this task, we require `faiss` and `PyPDF2`. Let's import them:

**For CPU only please install faiss-cpu instead.**

This demo uses `PyPDF2===3.0.1` and `faiss-cpu===1.8.0`

Now, we need to add the possibility to upload PDF files. For this, let's use `FileDropMultiple` from `solara`. The PDFs will then be stored in a new reactive variable:

The PDFs are stored, but as they are, we just have a large amount of bytes. To be able to chat with the PDF, we will need to extract the text:

Now that we have the texts, let's use Mistral's embeddings to retrieve the relevant chunks. First, let's define a function that converts text to embeddings with Mistral:

Next, we can declare a function that will handle all the retrieval part. This step will make use of `faiss` for the vector store and the previously created `get_text_embedding function`. This will cut the different files into chunks, create the embeddings, and retrieve the best 4 chunks among them, which will then be concatenated into a single string:

Finally, we edit `response_generator` to implement our new RAG with the files! This function, when there are PDFs, will extract the text with PyPDF2 and make use of `rag_pdf` to retrieve the relevant data. It will only then send the request to the model:

And everything is done! Now we can run our new interface with `solara run chat_with_pdfs.py`