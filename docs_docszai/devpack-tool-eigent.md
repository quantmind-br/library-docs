---
title: Eigent
url: https://docs.z.ai/devpack/tool/eigent.md
source: llms
fetched_at: 2026-01-24T11:21:26.275889976-03:00
rendered_js: false
word_count: 350
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.z.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Eigent

> Methods for Using the GLM Coding Plan in Eigent

Eigent is an open-source cowork  agent that runs on your desktop. It is built with a multi-agent workforce architecture, supported by general abilities such as browser automation, terminal automation and MCPs. This design enables agents in Eigent to perform tasks much like human workers operating in real desktop environments, without the need for deep API integrations or constant workflow reconfiguration.

Eigent works seamlessly with the [GLM Coding Plan](https://z.ai/subscribe), delivering high-performance AI capabilities at exceptional value.

<Tip>
  **Christmas Deal:** Enjoy 50% off your first GLM Coding Plan purchase, **plus an extra 10%/20% off**! [Subscribe](https://z.ai/subscribe?utm_source=z.ai\&utm_medium=link\&utm_term=glm-devpack\&utm_campaign=Platform_Ops&_channel_track_key=jFgqJREK) now.
</Tip>

<Warning>
  Using the GLM Coding Plan, you need to configure the dedicated Coding API [https://api.z.ai/api/coding/paas/v4](https://api.z.ai/api/coding/paas/v4) instead of the General API [https://api.z.ai/api/paas/v4](https://api.z.ai/api/paas/v4)
</Warning>

## Step 1: Installing Eigent

Choose the installation method that best suits your needs:

<Tabs>
  <Tab title="Official Download (Recommended)">
    ### 1. Download Eigent

    Visit [eigent.ai](https://eigent.ai/) and download the latest version for your platform (macOS 11+ or Windows).

    ### 2. Install the Application

    * **macOS**: Open the downloaded `.dmg` file and drag Eigent into your Applications folder
    * **Windows**: Run the downloaded `.exe` installer and follow the on-screen instructions

    ### 3. Launch Eigent

    Open the application and log in to get started.
  </Tab>

  <Tab title="Run from Source">
    For developers who want to run Eigent locally from source code.

    **Prerequisites:**

    * Node.js >= 18.0.0, \< 23.0.0
    * Python >= 3.12, \< 3.13
    * Docker (recommended) or PostgreSQL 15

    ### 1. Clone the Repository

    ```bash  theme={null}
    git clone https://github.com/eigent-ai/eigent.git
    cd eigent
    ```

    ### 2. Start Backend Services

    ```bash  theme={null}
    cd server
    cp .env.example .env
    docker compose up -d
    ```

    ### 3. Configure Frontend Environment

    In the project root directory, modify `.env.development`:

    ```bash  theme={null}
    VITE_BASE_URL=/api
    VITE_USE_LOCAL_PROXY=true
    VITE_PROXY_URL=http://localhost:3001
    ```

    ### 4. Start Frontend Service

    ```bash  theme={null}
    npm install
    npm run dev
    ```
  </Tab>
</Tabs>

## Step 2: Configuring the GLM Model

### 1. Access Application Settings

Launch Eigent and navigate to the **Home Page**, then click on the **Settings** tab.

![Description](https://cdn.bigmodel.cn/markdown/1768546337853image.png)

### 2. Locate Model Configuration

In the Settings menu, find and select the **Models** section, then scroll down to the **Custom Model** area and look for the **Z.ai Config** card.

![Description](https://cdn.bigmodel.cn/markdown/176861556077320260117.jpg)

### 3. Enter Configuration Details

Click on the Z.ai Config card and fill in the following information:

* **API Key**: Enter your Z.AI API Key (obtain from [Z.AI API Console](https://z.ai/manage-apikey/apikey-list))
* **API Host**: Enter `https://api.z.ai/api/coding/paas/v4/`
* **Model Type**: Enter the model name (e.g., `glm-4.7`, `glm-4.7`, or `glm-4.5-air`)

Click **Save** to apply your changes.

### 4. Set as Default

Once saved, click the **"Set as Default"** button on the Z.ai Config card to make GLM your default model.

## Step 3: Getting Started

With the configuration complete, you can now use Eigent with GLM models for:

* Autonomous code generation and refactoring
* Complex debugging and problem-solving
* Multi-file project management
* Technical documentation generation
* Code review and optimization

Your Eigent agents are now powered by Z.AI's GLM models and ready to assist with your development tasks.