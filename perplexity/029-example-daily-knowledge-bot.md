---
title: Daily Knowledge Bot
url: https://docs.perplexity.ai/docs/cookbook/examples/daily-knowledge-bot/README.md
source: llms
fetched_at: 2026-02-04T07:21:08.920817667-03:00
rendered_js: false
word_count: 421
summary: This document provides instructions for setting up and running a Python application that uses the Perplexity AI API to generate and store interesting daily facts based on rotating topics.
tags:
    - python
    - perplexity-api
    - automation
    - api-integration
    - knowledge-bot
    - educational-tool
category: tutorial
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Daily Knowledge Bot

> A Python application that delivers interesting facts about rotating topics using the Perplexity AI API

# Daily Knowledge Bot

A Python application that delivers interesting facts about rotating topics using the Perplexity AI API. Perfect for daily learning, newsletter content, or personal education.

## 🌟 Features

* **Daily Topic Rotation**: Automatically selects topics based on the day of the month
* **AI-Powered Facts**: Uses Perplexity's Sonar API to generate interesting and accurate facts
* **Customizable Topics**: Easily extend or modify the list of topics
* **Persistent Storage**: Saves facts to dated text files for future reference
* **Robust Error Handling**: Gracefully manages API failures and unexpected errors
* **Configurable**: Uses environment variables for secure API key management

## 📋 Requirements

* Python 3.6+
* Required packages:
  * requests
  * python-dotenv
  * (optional) logging

## 🚀 Installation

1. Clone this repository or download the script
2. Install the required packages:

```bash  theme={null}
# Install from requirements file (recommended)
pip install -r requirements.txt

# Or install manually
pip install requests python-dotenv
```

3. Set up your Perplexity API key:
   * Create a `.env` file in the same directory as the script
   * Add your API key: `PERPLEXITY_API_KEY=your_api_key_here`

## 🔧 Usage

### Running the Bot

Simply execute the script:

```bash  theme={null}
python daily_knowledge_bot.py
```

This will:

1. Select a topic based on the current day
2. Fetch an interesting fact from Perplexity AI
3. Save the fact to a dated text file in your current directory
4. Display the fact in the console

### Customizing Topics

Edit the `topics.txt` file (one topic per line) or modify the `topics` list directly in the script.

Example topics:

```
astronomy
history
biology
technology
psychology
ocean life
ancient civilizations
quantum physics
art history
culinary science
```

### Automated Scheduling

#### On Linux/macOS (using cron):

```bash  theme={null}
# Edit your crontab
crontab -e

# Add this line to run daily at 8:00 AM
0 8 * * * /path/to/python3 /path/to/daily_knowledge_bot.py
```

#### On Windows (using Task Scheduler):

1. Open Task Scheduler
2. Create a new Basic Task
3. Set it to run daily
4. Add the action: Start a program
5. Program/script: `C:\path\to\python.exe`
6. Arguments: `C:\path\to\daily_knowledge_bot.py`

## 🔍 Configuration Options

The following environment variables can be set in your `.env` file:

* `PERPLEXITY_API_KEY` (required): Your Perplexity API key
* `OUTPUT_DIR` (optional): Directory to save fact files (default: current directory)
* `TOPICS_FILE` (optional): Path to your custom topics file

## 📄 Output Example

```
DAILY FACT - 2025-04-02
Topic: astronomy

Saturn's iconic rings are relatively young, potentially forming only 100 million years ago. This means dinosaurs living on Earth likely never saw Saturn with its distinctive rings, as they may have formed long after the dinosaurs went extinct. The rings are made primarily of water ice particles ranging in size from tiny dust grains to boulder-sized chunks.
```

## 🛠️ Extending the Bot

Some ways to extend this bot:

* Add email or SMS delivery capabilities
* Create a web interface to view fact history
* Integrate with social media posting
* Add multimedia content based on the facts
* Implement advanced scheduling with specific topics on specific days

## ⚠️ Limitations

* API rate limits may apply based on your Perplexity account
* Quality of facts depends on the AI model
* The free version of the Sonar API has a token limit that may truncate longer responses

## 📜 License

[MIT License](https://github.com/ppl-ai/api-cookbook/blob/main/LICENSE)

## 🙏 Acknowledgements

* This project uses the Perplexity AI API ([https://docs.perplexity.ai/](https://docs.perplexity.ai/))
* Inspired by daily knowledge calendars and fact-of-the-day services