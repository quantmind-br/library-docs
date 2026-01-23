---
title: Saving Recipes | goose
url: https://block.github.io/goose/docs/guides/recipes/storing-recipes
source: github_pages
fetched_at: 2026-01-22T22:14:16.972215306-03:00
rendered_js: true
word_count: 539
summary: This guide explains how to manage, store, and access recipes within goose using both the Desktop UI and CLI. It covers storage locations, file formats, and procedures for importing and using saved recipes.
tags:
    - goose-recipes
    - recipe-management
    - desktop-ui
    - cli
    - configuration
    - data-storage
category: guide
---

This guide covers storing, organizing, and finding goose recipes when you need to access them again later.

Desktop UI vs CLI

- **goose Desktop** has a visual Recipe Library for browsing and managing saved recipes
- **goose CLI** stores recipes as files that you find using file paths or environment variables

## Understanding Recipe Storage[​](#understanding-recipe-storage "Direct link to Understanding Recipe Storage")

Before saving recipes, it's important to understand where they can be stored and how this affects their availability.

### Recipe Storage Locations[​](#recipe-storage-locations "Direct link to Recipe Storage Locations")

TypeLocationAvailabilityBest For**Global**`~/.config/goose/recipes/`All projects and sessionsPersonal workflows, general-purpose recipes**Local**`YOUR_WORKING_DIRECTORY/.goose/recipes/`Only when working in that projectProject-specific workflows, team recipes

**Choose Global Storage When:**

- You want the recipe available across all projects
- It's a personal workflow or general-purpose recipe
- You're the primary user of the recipe

**Choose Local Storage When:**

- The recipe is specific to a particular project
- You're working with a team and want to share the recipe
- The recipe depends on project-specific files or configurations

## Storing Recipes[​](#storing-recipes "Direct link to Storing Recipes")

- goose Desktop
- goose CLI

**Save New Recipe:**

1. To create a recipe from your chat session, see [Create Recipe](https://block.github.io/goose/docs/guides/recipes/session-recipes#create-recipe)
2. Once in the Recipe Editor, click `Save Recipe` to save it to your Recipe Library

**Save Modified Recipe:**

If you're already using a recipe and want to save a modified version:

1. Click the button at the bottom of the app, which appears after sending your first message
2. Make any desired edits to the instructions, prompt, or other fields
3. Click `Save Recipe`

info

When you modify and save a recipe with a new name, a new recipe and new link are generated. You can still run the original recipe from the recipe library, or using the original link. If you edit a recipe without changing its name, the version in the recipe library is updated, but you can still run the original recipe via link.

### Importing Recipes[​](#importing-recipes "Direct link to Importing Recipes")

- goose Desktop
- goose CLI

Import a recipe using its deeplink or recipe file:

1. Click the button in the top-left to open the sidebar
2. Click `Recipes` in the sidebar
3. Click `Import Recipe`
4. Choose your import method:
   
   - To import via a link: Under `Recipe Deeplink`, paste in the [recipe link](https://block.github.io/goose/docs/guides/recipes/session-recipes#share-via-recipe-link)
   - To import via a file: Under `Recipe File`, click `Choose File`, select a recipe file, and click `Open`
5. Click `Import Recipe` to save a copy of the recipe to your Recipe Library

Recipe File Format

goose Desktop accepts `.yaml`, `.yml`, and `.json` files, but **the CLI only supports `.yaml` and `.json`** . For full compatibility across both interfaces, avoid `.yml` extensions.

All recipe formats follow the same [schema structure](https://block.github.io/goose/docs/guides/recipes/recipe-reference#core-recipe-schema).

## Finding Available Recipes[​](#finding-available-recipes "Direct link to Finding Available Recipes")

- goose Desktop
- goose CLI

**Access Recipe Library:**

1. Click the button in the top-left to open the sidebar
2. Click `Recipes` to view your Recipe Library
3. Browse your available recipes, which show:
   
   - Recipe title and description
   - Last modified date
   - Whether they're stored globally or locally

Desktop vs CLI Recipe Discovery

The Desktop Recipe Library displays all recipes you've explicitly saved or imported. It doesn't automatically discover recipe files from your filesystem like the CLI does.

## Using Saved Recipes[​](#using-saved-recipes "Direct link to Using Saved Recipes")

- goose Desktop
- goose CLI

<!--THE END-->

1. Click the button in the top-left to open the sidebar
2. Click `Recipes`
3. Find your recipe in the Recipe Library
4. Choose one of the following:
   
   - Click `Use` to run it immediately
   - Click `Preview` to see the recipe details first, then click **Load Recipe** to run it