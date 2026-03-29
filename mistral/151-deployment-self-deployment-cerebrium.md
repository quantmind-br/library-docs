---
title: Cerebrium | Mistral Docs
url: https://docs.mistral.ai/deployment/self-deployment/cerebrium
source: crawler
fetched_at: 2026-01-29T07:34:17.796619119-03:00
rendered_js: false
word_count: 291
summary: A technical guide on deploying and running Mistral AI models using the Cerebrium serverless infrastructure platform.
tags:
    - Mistral AI
    - Cerebrium
    - Deployment
    - LLM
    - Serverless
category: guide
---

## Deploy with Cerebrium

[Cerebrium](https://www.cerebrium.ai/) is a serverless AI infrastructure platform that makes it easier for companies to build and deploy AI based applications. They offer Serverless GPU's with low cold start times with over 12 varieties of GPU chips that auto scale and you only pay for the compute you use.

First, we install Cerebrium and login to get authenticated.

Then let us create our first project

You set up your environment and hardware in the **cerebrium.toml** file that was created using the init function above. Here we are using a Ampere A10 GPU etc. You can read more [here](https://docs.cerebrium.ai/cerebrium/environments/custom-images)

Running code in Cerebrium is like writing normal python with no special syntax. In your **main.py** specify the following:

We need to add our Hugging Face token to our [Cerebrium Secrets](https://docs.cerebrium.ai/cerebrium/environments/using-secrets) since using the Mistral model requires authentication. Please make sure the Huggingface token you added, has **WRITE** permissions. On first deploy, it will download the model and store it on disk therefore for subsequent calls it will load the model from disk.

Add the following to your main.py:

Every function in Cerebrium is callable through and API endpoint. Code at the top most layer (ie: not in a function) is instantiated only when the container is spun up the first time so for subsequent calls, it will simply run the code defined in the function you call.

Our final main.py should look like this:

You will see your application deploy, install pip packages and download the model. Once completed it will output a CURL request you can use to call your endpoint. Just remember to end the url with the function you would like to call - in this case /run.

You should then get a message looking like this: