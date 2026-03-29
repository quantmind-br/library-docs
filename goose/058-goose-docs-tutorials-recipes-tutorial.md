---
title: Recipes | goose
url: https://block.github.io/goose/docs/tutorials/recipes-tutorial
source: github_pages
fetched_at: 2026-01-22T22:16:24.688539411-03:00
rendered_js: true
word_count: 616
summary: This document explains how to create, configure, and use Goose recipes to automate tasks, covering extensions, parameters, and AI model settings.
tags:
    - goose-ai
    - goose-recipes
    - prompt-engineering
    - mcp-extensions
    - automation
    - yaml-configuration
category: guide
---

goose recipes are files that contain all the details to allow goose to do one specific task. Since they are contained in just one file, they are easy to share through all the normal ways we share files, including version management systems like git. Let's get started with the simplest recipe possible.

## The Simplest Recipe[​](#the-simplest-recipe "Direct link to The Simplest Recipe")

The simplest recipe is basically just a prompt. This might seem not all that useful—after all I can just share my prompt on Slack or email—but it turns out that the most important reason users can't get agents to do what they want is that their prompts are too short and that they don't iterate enough on those prompts. Keeping prompts in a text file helps with both these things.

Here's a recipe that will plan a trip to Europe:

```
title: Trip planner
description: Plan your next trip
prompt:|
 Help the user plan a trip to Europe for 14 days.
 Create a detailed itinerary that includes:
  - places to visit
  - activities to do
  - local cuisine to try
  - a rough budget estimate
```

You can run it from the command line using:

```
goose run --recipe trip.yaml
```

## Extensions[​](#extensions "Direct link to Extensions")

goose recipes have a section where you can specify which [extensions](https://block.github.io/goose/docs/guides/recipes/recipe-reference#extensions) goose can use during execution. goose will only use the ones you specify.

Let's say we want to make sure we have good weather during our Europe trip. We can just add a weather extension (this example uses the [weather-mcp-server](https://github.com/TuanKiri/weather-mcp-server) by TuanKiri under the MIT License) to our recipe, modify the prompt a bit and now goose will check the weather before adding a city to our trip.

```
title: Trip planner
description: Plan your next trip
prompt:|
 Help the user plan a trip to Europe for 14 days. Create a detailed itinerary that includes:
  - places to visit
  - activities to do
  - local cuisine to try
  - a rough budget estimate
 Ensure that the user has good weather throughout their trip. Optimize their trip based on the forecast in potential locations.
extensions:
-type: stdio
name: weathermcpserver
cmd: /Users/svega/Development/weather-mcp-server/weather-mcp-server
args:[]
timeout:300
description:"Weather data for trip planning"
env_keys:
- WEATHER_API_KEY
```

## Parameters[​](#parameters "Direct link to Parameters")

We can make our recipes dynamic by adding parameters. Parameters are variables that are provided by the user of our recipes. They each have a data type and a requirement field that defines if they are required, optional or provided by the user. We can generalize our trip recipe by adding a parameter for the destination and the length of the trip:

```
parameters:
-key: destination
input_type: string
requirement: required
description: Destination for the trip. Should be a large region with multiple climates.
-key: duration
input_type: number
requirement: required
description: Number of days for the trip.
```

Recipes use a template system that lets you insert variables like `{{ destination }}` which get filled in with the actual values you provide. Once you've updated the prompt with the right details, you can run your new recipe like this to get a plan for a 14 day trip to Africa:

```
goose run --recipe trip.yaml --params destination=Africa --params duration=14
```

## Settings[​](#settings "Direct link to Settings")

By default, goose uses the `temperature` and `model` you've already chosen, which usually works just fine. But sometimes you might want more control. For example, when performing a subjective task like planning a trip, it can help to turn up the `temperature` setting. Think of temperature like a creativity dial - the higher it is, the more varied and unexpected the results. If the first suggestion isn't quite right, the user can just run the recipe again to get a new one.

You can also specify which AI provider and model to use for a specific recipe:

```
settings:
goose_provider:"anthropic"
goose_model:"claude-sonnet-4-20250514"
temperature:0.8
```

The available settings are:

- `goose_provider`: The AI provider (e.g., "anthropic", "openai")
- `goose_model`: The specific model name
- `temperature`: Controls creativity/randomness (0.0-1.0, higher = more creative)

These settings will override your default goose configuration when this recipe runs.

## External Files[​](#external-files "Direct link to External Files")

Sometimes, you'll want to give the agent access to extra information without cramming all that data into the prompt. Instead of pasting everything in, you can keep the data in a separate file and point the recipe to it.

To help with this, recipes include a built-in variable called `{{ recipe_dir }}`, which lets you reference files stored alongside your recipe. For example, you could download the UNESCO list from [Kaggle](https://www.kaggle.com/datasets/ramjasmaurya/unesco-heritage-sites2021?resource=download) and use it in your travel planning recipe.

Then we reference the file in our prompt like:

```
prompt:|
 You can use the \{\{ recipe_dir \}\}/unesco.csv file to 
 check information on UNESCO world heritage sites to
 include in your travel plan.
```

We also need to specify an extension to read files:

```
extensions:
-type: builtin
name: developer
display_name: Developer
timeout:300
bundled:true
```

Here we add the [Developer extension](https://block.github.io/goose/docs/mcp/developer-mcp) which provides the ability to read files for relevant information.

Example Recipe Output

View detailed 10-day European itinerary

## Learn More[​](#learn-more "Direct link to Learn More")

Check out the [Recipes](https://block.github.io/goose/docs/guides/recipes) guide for more docs, tools, and resources to help you master goose recipes.