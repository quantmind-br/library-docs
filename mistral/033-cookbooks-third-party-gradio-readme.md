---
title: Chat with Your PDF using Mistral and Gradio - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-gradio-readme
source: crawler
fetched_at: 2026-01-29T07:34:09.851088757-03:00
rendered_js: false
word_count: 372
---

In this guide, we will introduce the basics of building a chatbot with chat and PDF reading capabilities using `gradio`!

**Watch our demo by clicking this image:**

[![Gradio Demo](https://img.youtube.com/vi/mrHgm7MOipw/0.jpg)](https://docs.mistral.ai/cookbooks/third_party-gradio-readme)

## Chat Interface

First, let's implement a simple chat interface. To do this, we will need to import the `gradio`, `mistralai` libraries, and `ChatMessage` from `mistralai.models.chat_completion`.

*This demo uses `gradio===4.32.2` and `mistralai===0.4.0`*

Next, create your `MistralClient` instance using your Mistral API key.

To create our interface with `gradio`, we can make use of their `ChatInterface`. It will look something like this:

Now, all we have to do is edit `ask_mistral` so it parses our message and history, calls Mistral's API, and streams the response.

Done! Once ready, you can run the script (`chat.py`)!

## Chatting with PDFs

To enable our model to read PDFs, we need to convert the content, extract the text, and then use Mistral's embedding model to retrieve chunks of our document(s) to feed to the model. We will need to implement some basic RAG (Retrieval-Augmented Generation)!

For this task, we will require `faiss`, `PyPDF2`, and other libraries. Let's import them:

**For CPU only please install faiss-cpu instead.**

*This demo uses `numpy===1.26.4`, `PyPDF2===0.4.0` and `faiss-cpu===1.8.0`*

For our interface to allow the uploading of files, we need to toggle multimodality on our `ChatInterface`.

Now, our interface will also accept files. The next step is to handle them and filter out the PDF files from the messages.

We are ready to read the PDF files and implement some RAG. For this, we will need to make a function that retrieves the relevant chunks of text from the PDFs concatenated as a single string. For that, we will make use of Mistral's embeddings. Let's quickly design a function that will convert text to the embeddings:

And now, we can make `rag_pdf` that will handle all the RAG and retrieve the proper chunks:

In this function, we cut the PDF files into chunks of equal sizes, get their embeddings, and apply some vector search with `faiss` to retrieve the best 4 chunks. The next and last step will be to read the PDF files themselves with `PyPDF2` and integrate them with the model:

With this, we are ready to go! We can run our script `chat_with_pdfs.py`.