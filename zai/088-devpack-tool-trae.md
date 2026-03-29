---
title: TRAE
url: https://docs.z.ai/devpack/tool/trae.md
source: llms
fetched_at: 2026-01-24T11:22:54.721122492-03:00
rendered_js: false
word_count: 272
summary: This document provides a step-by-step guide for integrating GLM-4.7 and the GLM Coding Plan into the TRAE IDE. It explains how to install the software, configure the Z.AI API provider, and troubleshoot common connection issues.
tags:
    - trae-ide
    - glm-4
    - z-ai-api
    - ai-integration
    - coding-assistant
    - ide-setup
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.z.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# TRAE

> Methods for using the GLM Coding Plan in TRAE

Trae (/treɪ/) is a developer-friendly IDE that offers AI Q\&A, inline code completion, and agentic programming workflows. With GLM models, TRAE can help you code faster, debug smarter, and automate routine tasks.

<Tip>
  **Christmas Deal:** Enjoy 50% off your first GLM Coding Plan purchase, **plus an extra 10%/20% off**! [Subscribe](https://z.ai/subscribe?utm_source=z.ai\&utm_medium=link\&utm_term=glm-devpack\&utm_campaign=Platform_Ops&_channel_track_key=jFgqJREK) now.
</Tip>

## Step 1: Install and Launch TRAE

<Steps>
  <Step title="Download and Install">
    * Go to the [TRAE website](https://www.trae.ai/?utm_source=content\&utm_medium=doc_zai\&utm_campaign=GLM) and install TRAE.
  </Step>

  <Step title="First Launch">
    * On first launch, you will see the setup screen.

    ![Description](https://cdn.bigmodel.cn/markdown/17624995101951.PNG?attname=1.PNG)

    * Click **Get Started** to begin the setup.
  </Step>
</Steps>

## Step 2: Configure GLM-4.7 in TRAE

Use your Z.AI API Key to add the GLM Coding Plan model in TRAE.

<Steps>
  <Step title="Open Models">
    * In the chat sidebar, click the **Settings** icon at top-right, then go to **Models**.
  </Step>

  <Step title="Add Custom Model">
    * Click **+ Add Model** to open the model creation dialog.

    ![Description](https://cdn.bigmodel.cn/markdown/17625008588212.PNG?attname=2.PNG)
  </Step>

  <Step title="Enter Configuration Details">
    * **Provider**: Select **Z.ai-plan**
    * **Model**: `GLM-4.7-plan`
    * **API Key**: Enter your **Z.AI API Key**

    <Warning>
      You may see both **Z.ai** and **Z.ai-plan** providers.\
      If you subscribed to the **GLM Coding Plan**, select **Z.ai-plan** to use the Coding Plan quota.\
      Selecting **Z.ai** will route to the general API and charges standard pricing from your balance.
    </Warning>

    <Tip>
      Click **Get API Key** to open the Z.AI API Key management page in your browser.
    </Tip>

    ![Description](https://cdn.bigmodel.cn/markdown/17625008731353.png?attname=3.png)
  </Step>

  <Step title="Validate and Save">
    * Click **Add Model**. TRAE will validate the API key and configuration.
    * On success, your custom model will be added and available for selection.
    * On failure, TRAE shows the error returned by Z.AI for troubleshooting.
  </Step>
</Steps>

## Step 3: Get Started with TRAE + GLM

* Select your **GLM-4.7-plan** model in TRAE.
* Ask for help with tasks such as feature implementation, code generation, refactoring, and debugging.
* Use inline suggestions and agentic actions to accelerate your workflow.

## FAQ

### Using Z.ai vs Z.ai-plan

* **Z.ai-plan**: For GLM Coding Plan subscribers. Routes via Coding API with plan quota. Use model `GLM-4.7`.
* **Z.ai**: For general API usage with standard pricing and balance deduction. Use models like `GLM-4.7`.

### Connection Fails When Adding Model

* Verify your **Z.AI API Key** is correct and active.
* Confirm your subscription status for the **GLM Coding Plan** if using **Z.ai-plan**.
* Check network connectivity and try again. If errors persist, review the error message shown in the **Add Model** dialog.

## Resources

* **TRAE Website**: [trae.ai](https://www.trae.ai/?utm_source=content\&utm_medium=doc_zai\&utm_campaign=GLM)
* **Z.AI API Keys**: [z.ai/manage-apikey/apikey-list](https://z.ai/manage-apikey/apikey-list)
* **GLM Coding Plan**: [z.ai/subscribe](https://z.ai/subscribe?utm_source=zai\&utm_medium=link\&utm_term=devpack-integration\&utm_campaign=Platform_Ops&_channel_track_key=w3mNdY8g)