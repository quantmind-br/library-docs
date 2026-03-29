---
title: Building Gradio app with Mistral OCR to extract text and images from PDFs - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-gradio-mistralocr
source: crawler
fetched_at: 2026-01-29T07:33:50.523969126-03:00
rendered_js: false
word_count: 380
summary: A guide on building a Gradio application that leverages Mistral OCR to extract both text and images from PDF documents.
tags:
    - Mistral AI
    - OCR
    - Gradio
    - PDF
    - Python
category: guide
---

This cookbook provides a step-by-step guide to setting up and using Mistral OCR with Gradio.  
The application allows you to extract text and images from PDFs and images using Mistral's OCR capabilities.

## Prerequisites

Before you begin, ensure you have the following:

- Python installed on your system.
- An API key from Mistral AI.
- Necessary Python packages installed.

## Step 1: Install Required Packages

First, install the required Python packages. You can do this using pip:

## Step 2: Set Up Environment Variables

You need to set up your Mistral API key as an environment variable.  
You can do this in your terminal or add it to your script.

You can create an API key on our [Platforme](https://docs.mistral.ai/cookbooks/third_party-gradio-mistralocr).

## Step 3: Import Libraries

Import the necessary libraries in your Python script.

## Step 4: Initialize Mistral Client

Initialize the Mistral client using your API key.

## Step 5: Define Helper Functions

### Encode Image to Base64

This function encodes an image to a base64 string.  
It will be required to provide local images to the service.

### Replace Images in Markdown

This function replaces image placeholders in markdown with base64-encoded images.  
Mistral OCR is capable of outputting interleaved text and images; this function will replace placeholders to render with Gradio.

### Get Combined Markdown

This function combines the markdown from all pages of the OCR response.  
It will output a ready-to-be-rendered version and a raw markdown output without the images.

### Fetch Content Type

This function fetches the content type of a URL.  
The objective is to detect if we are handling PDF files or image files.

## Step 6: Define OCR Functions

### Perform OCR on File

To perform OCR on local PDF files, it is required to upload them first to the Platforme and get a signed URL that will be used for OCR tasks.

### Perform OCR on URL

Next, we can define a function to perform OCR on URLs.  
We need different ones for images and for PDF documents.

## Step 7: Create Gradio Interface

Lastly, we can create the Gradio interface to interact with the OCR functions!

## Step 8: Run the Application

Run the script to launch the Gradio interface. You can interact with the interface to perform OCR on files or URLs.

A live demo can be found [here](https://docs.mistral.ai/cookbooks/third_party-gradio-mistralocr), and more information can be found on the [blog post](https://docs.mistral.ai/cookbooks/third_party-gradio-mistralocr).