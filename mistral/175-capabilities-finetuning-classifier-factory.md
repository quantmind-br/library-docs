---
title: Classifier Factory | Mistral Docs
url: https://docs.mistral.ai/capabilities/finetuning/classifier_factory
source: crawler
fetched_at: 2026-01-29T07:33:36.113303261-03:00
rendered_js: false
word_count: 821
---

In various domains and enterprises, classification models play a crucial role in enhancing efficiency, improving user experience, and ensuring compliance. These models serve diverse purposes, including but not limited to:

- Moderation: Classification models are essential for moderating services and classifying unwanted content. For instance, our [moderation service](https://docs.mistral.ai/capabilities/guardrailing/#moderation-api) helps in identifying and filtering inappropriate or harmful content in real-time, ensuring a safe and respectful environment for users.
- **Intent Detection**: These models help in understanding user intent and behavior. By analyzing user interactions, they can predict the user's next actions or needs, enabling personalized recommendations and improved customer support.
- **Sentiment Analysis**: Emotion and sentiment detection models analyze text data to determine the emotional tone behind words. This is particularly useful in social media monitoring, customer feedback analysis, and market research, where understanding public sentiment can drive strategic decisions.
- **Data Clustering**: Classification models can group similar data points together, aiding in data organization and pattern recognition. This is beneficial in market segmentation, where businesses can identify distinct customer groups for targeted marketing campaigns.
- **Fraud Detection**: In the financial sector, classification models help in identifying fraudulent transactions by analyzing patterns and anomalies in transaction data. This ensures the security and integrity of financial systems.
- **Spam Filtering**: Email services use classification models to filter out spam emails, ensuring that users receive only relevant and safe communications.
- **Recommendation Systems**: Classification models power recommendation engines by categorizing user preferences and suggesting relevant products, movies, or content based on past behavior and preferences.

By leveraging classification models, organizations can make data-driven decisions, improve operational efficiency, and deliver better products and services to their customers.

For this reason, we designed a friendly and easy way to make your own classifiers. Leveraging our small but highly efficient models and training methods, the Classifier Factory is both available directly in the [AI Studio](https://console.mistral.ai/build/finetuned-models) and our API.

### Dataset

To fine-tune a model, you need to provide a dataset that contains the data you want to train on, it is also recommended to have a validation dataset and a test dataset.

The dataset must be in a specific format, and you can upload it to the Mistral Cloud before launching the fine-tuning job.

Data must be stored in JSON Lines (`.jsonl`) files, which allow storing multiple JSON objects, each on a new line.

We provide two endpoints:

- `v1/classifications`: To classify raw text.
- `v1/chat/classifications`: To classify chats and multi-turn interactions.

There are 2 main kinds of classification models\***\*:\*\***

- Single Target
- Multi-Target

For single label classification, data must have the label name and the value for that corresponding label. Example:

For multiple labels, you can provide a list:

When using the result model, you will be able to retrieve the scores for the corresponding label and value.

Note that the files must be in JSONL format, meaning every JSON object must be flattened into a single line, and each JSON object is on a new line.

Raw `.jsonl` file example.

- Label data must be a dictionary with the label name as the key and the label value as the value.

### Create and Manage Fine-tuning Jobs

To create your custom model, you need to create a fine-tuning job. You can fully manage jobs via our API, from creation, to starting, monitoring and cancellation.

A fine-tuning job corresponds to a single training run. You can create a fine-tuning job with the following parameters:

- model: the specific model you would like to fine-tune. The choice is `ministral-3b-latest`.
- training\_files: a collection of training file IDs, which can consist of a single file or multiple files.
- validation\_files: a collection of validation file IDs, which can consist of a single file or multiple files.
- hyperparameters: two adjustable hyperparameters, "training\_steps" and "learning\_rate", that users can modify.
- auto\_start:
  
  - `auto_start=True`: Your job will be launched immediately after validation.
  - `auto_start=False` (default): You can manually start the training after validation by sending a POST request to `/fine_tuning/jobs/<uuid>/start`.
- integrations: external integrations we support such as Weights and Biases for metrics tracking during training.

After creating a fine-tuning job, you can check the job status using:

Initially, the job status will be `"QUEUED"`. After a brief period, the status will update to `"VALIDATED"`. At this point, you can proceed to start the fine-tuning job:

### Use and Delete Fine-tuned Models

Once your fine-tuning job is done, you can use your fine-tuned custom model to classify your data and use it in your applications.

Below is an example of how to use a fine-tuned model to classify your data.

You can delete a fine-tuned model if you no longer need it.

Explore our guides and [cookbooks](https://github.com/mistralai/cookbook) leveraging the Classifier Factory:

- [Intent Classification](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/classifier_factory/intent_classification.ipynb): Creating a single-target, single-label, intent classification model to predict user actions and improve customer interactions.
- [Moderation Classifier](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/classifier_factory/moderation_classifier.ipynb): Build a single-target, multi-label, simple moderation model to label public comments.
- [Product Classification](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/classifier_factory/product_classification.ipynb): Create a multi-target, single-label and multi-label, food classification model to categorize dishes and their country of origin and compare to classic LLM solutions, enhancing recipe recommendations and dietary planning.