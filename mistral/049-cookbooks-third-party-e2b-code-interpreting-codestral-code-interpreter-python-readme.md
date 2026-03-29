---
title: E2B Python AI Code Execution with Mistral's Codestral - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-e2b_code_interpreting-codestral-code-interpreter-python-readme
source: crawler
fetched_at: 2026-01-29T07:34:02.815549157-03:00
rendered_js: false
word_count: 280
---

This AI data analyst can plot a linear regression chart based on CSV data. It uses Mistral's Codestral as the LLM, and the [Code Interpreter SDK](https://docs.mistral.ai/cookbooks/third_party-e2b_code_interpreting-codestral-code-interpreter-python-readme) by E2B for the code interpreting capabilities. The SDK quickly creates a secure cloud sandbox powered by [Firecracker](https://docs.mistral.ai/cookbooks/third_party-e2b_code_interpreting-codestral-code-interpreter-python-readme). Inside this sandbox is a running Jupyter server that the LLM can use.

Read more about Mistral's new Codestral model [here](https://docs.mistral.ai/cookbooks/third_party-e2b_code_interpreting-codestral-code-interpreter-python-readme).

The AI agent performs a data analysis task on an uploaded CSV file, executes the AI-generated code in the sandboxed environment by E2B, and returns a chart, saving it as a PNG file.

## Installation

## 1. Load API keys

Add your API keys to the corresponding part of the program.

## 2. Run the program

To work with Python Jupyter Notebooks in VSCode, activate an Anaconda environment or another Python environment in which you've installed the Jupyter package. You can run an individual cell using the Run icon and the output will be displayed below the code cell.

The script performs the following steps:

- Loads the API keys from the environment variables.
- Uploads the CSV dataset to the E2B sandboxed cloud environment.
- Sends a prompt to the Codestal model to generate Python code for analyzing the dataset.
- Executes the generated Python code using the E2B Code Interpreter SDK.
- Saves any generated visualization as a PNG file.

After running the program, you should get the result of the data analysis task saved in an `image_1.png` file. You should see a plot like this:

![Example of the output](https://docs.mistral.ai/cookbooks/third_party/E2B_Code_Interpreting/codestral-code-interpreter-python/image_1.png)

## Connect with E2B & learn more

If you encounter any problems, please let us know at our [Discord](https://docs.mistral.ai/cookbooks/third_party-e2b_code_interpreting-codestral-code-interpreter-python-readme).

Check the [E2B documentation](https://docs.mistral.ai/cookbooks/third_party-e2b_code_interpreting-codestral-code-interpreter-python-readme) to learn more about how to use the Code Interpreter SDK.