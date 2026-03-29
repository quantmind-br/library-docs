---
title: Chat with Your PDF using Mistral and Streamlit - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-streamlit-readme
source: crawler
fetched_at: 2026-01-29T07:34:08.787309762-03:00
rendered_js: false
word_count: 466
---

In this guide, we will introduce the basics of building a chatbot with chat and PDF reading capabilities using `streamlit`!

**Watch our demo by clicking this image:**

[![Panel Demo](https://img.youtube.com/vi/VGSAA-d_Sqo/0.jpg)](https://docs.mistral.ai/cookbooks/third_party-streamlit-readme)

## Chat Interface

First, let's implement a simple chat interface. To do this, we will need to import the `streamlit` and `mistralai` libraries.

*This demo uses `streamlit===1.35.0` and `mistralai===0.4.0`*

Next, create your `MistralClient` instance using your Mistral API key.

Now, we will initialize a session variable where all messages will be stored and display them on the screen.

The following step is to retrieve the input from the user and store it in the list of messages. For this, we will use `chat_input` from `streamlit`!

All that's left is to query Mistral and retrieve the response. To make the interaction smooth, we will handle it by streaming the response. For this, `streamlit` has `write_stream`, which accepts a generator. Let's define a generator!

With everything set, all we need to do is retrieve the response from the model and save it in the session.

There you go! An interface where you can chat with Mistral's models.

To run this code, enter `streamlit run chat.py` in the console.

## Chatting with PDFs

To enable our model to read PDFs, we need to convert the content, extract the text, and then use Mistral's embedding model to retrieve chunks of our document(s) to feed to the model. We will need to implement some basic RAG (Retrieval-Augmented Generation)!

For this task, we will require `faiss`, `PyPDF2`, and other libraries. Let's import them:

**For CPU only please install faiss-cpu instead.**

*This demo uses `numpy===1.26.4`, `PyPDF2===0.4.0` and `faiss-cpu===1.8.0`*

Now, we need to add the possibility to upload PDF files. For this, let's use `file_uploader` from `streamlit`. The PDF will then be stored in a new session variable:

The PDFs are stored, but as they are, we just have a large amount of bytes. To be able to chat with the PDF, we will need to extract the text and use Mistral's embeddings to retrieve the relevant chunks.

First, let's define a function that converts text to embeddings with Mistral:

Next, we can declare a function that will handle all the retrieval part. This step will make use of `faiss` for the vector store and the previously created `get_text_embedding` function. This will cut the different files into chunks, create the embeddings, and retrieve the best 4 chunks among them, which will then be concatenated into a single string:

Finally, we edit `ask_mistral` to implement our new RAG with the files! This function, when there are PDFs, will extract the text with `PyPDF2` and make use of `rag_pdf` to retrieve the relevant data. It will only then send the request to the model:

And everything is done! Now we can run our new interface with `streamlit run chat_with_pdfs.py`.