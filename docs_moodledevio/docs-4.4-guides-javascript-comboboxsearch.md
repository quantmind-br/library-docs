---
title: Combobox searching | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/guides/javascript/comboboxsearch
source: sitemap
fetched_at: 2026-02-17T15:05:19.917196-03:00
rendered_js: false
word_count: 1026
summary: This document explains how to integrate and customize the Moodle core combobox search component to create consistent search interfaces. It provides implementation steps for PHP and JavaScript along with a reference of available helper methods for extending the base class.
tags:
    - moodle-development
    - combobox-search
    - ui-component
    - javascript-amd
    - frontend-api
    - search-functionality
category: guide
---

A combobox search component has been added to the core Moodle system. This component provides an additional layer of search functionality, allowing users to easily navigate and filter search results. The combobox search component is designed to be reusable and can be integrated into various areas of the Moodle platform.

To implement the combobox search component, follow these steps:

1. Add the necessary HTML structure for the dropdown in your template file
2. Initialize the component via PHP
3. Initialize the component using JavaScript

## Benefits[​](#benefits "Direct link to Benefits")

By moving the tertiary search dropdown component to the core, the Moodle development team aimed to achieve the following benefits:

- Improved consistency: Using a single, core component for the search dropdown ensures that the look and feel of this UI element remains consistent across different parts of Moodle.
- Improved code maintainability: Having the component in the core makes it easier for the development team to manage the codebase and ensure that any updates to the component are applied consistently across the entire application.
- Reduced code duplication: By making the component available to all Moodle modules, there is no need to duplicate the code in different parts of the application.

## Structure of the component[​](#structure-of-the-component "Direct link to Structure of the component")

### Extending the search\_combobox[​](#extending-the-search_combobox "Direct link to Extending the search_combobox")

If you want to get started quickly, you can extend the `search_combobox` class. This class provides a lot of the boilerplate code that you would otherwise need to write yourself. You'll also need to implement the functions that throw errors if undefined however as we need some information from you about what and how you are searching.

View example

path/to/plugin/amd/src/yourcomponent.js

```
importsearch_comboboxfrom'core/comboboxsearch/search_combobox';

exportdefaultclassextends search_combobox {
(...)
}
```

### Instantiate a Component[​](#instantiate-a-component "Direct link to Instantiate a Component")

If you'll be using JS for other functionality, you can do the following:

- AMD module
- PHP code

path/to/plugin/amd/src/main.js

```
importYourComponentfrom 'YOUR_PLUGIN/yourcomponent;

(...)

exportconstinit=()=>{
returnnewYourComponent({});
};

```

### Initialize a component from a mustache template[​](#initialize-a-component-from-a-mustache-template "Direct link to Initialize a component from a mustache template")

Components are easy to embed in mustache files. To do so your class must have a static "init" method that could be called inside the `{{#js}}`.

- Component class
- Mustache file

path/to/plugin/amd/src/childcomponent.js

```
importYourComponentfrom 'YOUR_PLUGIN/yourcomponent;

exportdefaultclassextendsYourComponent{

constructor(){
super();
}

staticinit(){
returnnewthis();
}
}

```

### search\_combobox helpers[​](#search_combobox-helpers "Direct link to search_combobox helpers")

The search\_combobox class offers some helpers to standardize the components' code and make them more maintainable.

#### getDataset()[​](#getdataset "Direct link to getDataset()")

Calls the implemented `fetchDataset` method and returns the dataset.

#### getDatasetSize()[​](#getdatasetsize "Direct link to getDatasetSize()")

Returns the size of the dataset without having to call `getDataset` first.

#### getMatchedResults()[​](#getmatchedresults "Direct link to getMatchedResults()")

Once a result set has been filtered, this method returns the matched results based on the users search input.

#### setMatchedResults()[​](#setmatchedresults "Direct link to setMatchedResults()")

By default, returns the dataset but can be overridden to show how exactly a result set matched upon the data.

#### getSearchTerm()[​](#getsearchterm "Direct link to getSearchTerm()")

Provide the current search term that the user entered without manually accessing the DOM.

#### getPreppedSearchTerm()[​](#getpreppedsearchterm "Direct link to getPreppedSearchTerm()")

Return the parsed (lowercase) search term.

#### setSearchTerms()[​](#setsearchterms "Direct link to setSearchTerms()")

When a user changes the value of the input, after we debounce, we update the search term in memory.

#### getHTMLElements()[​](#gethtmlelements "Direct link to getHTMLElements()")

Update and return some of the typical HTML elements that are used in the component.

#### closeSearch()[​](#closesearch "Direct link to closeSearch()")

Close the associated dropdown manually since we control the dropdown rather than purely relying on Bootstrap. We can optionally clear the users' search term.

#### searchResultsVisible()[​](#searchresultsvisible "Direct link to searchResultsVisible()")

Shorthand for confirming if the search results are currently visible.

#### toggleDropdown()[​](#toggledropdown "Direct link to toggleDropdown()")

Manually open and close the dropdown rather than purely relying on Bootstrap.

#### updateNodes()[​](#updatenodes "Direct link to updateNodes()")

Ensure that nodes that are susceptible to change are up-to-date when we need them.

#### registerClickHandlers()[​](#registerClickHandlers "Direct link to registerClickHandlers()")

Handle our base case of click handlers i.e. opening and closing the dropdown. This can be further extended in callers for any special handling.

#### registerKeyHandlers()[​](#registerKeyHandlers "Direct link to registerKeyHandlers()")

Handle our base case of keyboard handlers i.e. opening and closing the dropdown, accessibility handling. This can be further extended in callers for any special handling.

#### registerInputHandlers()[​](#registerInputHandlers "Direct link to registerInputHandlers()")

Register the text input handlers for the search input and debounce the input so that we don't need to fire a bunch of calls as the user is still typing.

#### filterrenderpipe()[​](#filterrenderpipe "Direct link to filterrenderpipe()")

Combine the filter and render methods into a single method to be called by the input handlers as a QoL shorthand call.

#### renderAndShow()[​](#renderAndShow "Direct link to renderAndShow()")

Given we need to update the display, ensure we have the latest dataset and render it.

#### keyUpDown()[​](#keyUpDown "Direct link to keyUpDown()")

Given the user is navigating the dropdown with the keyboard, handle the common up and down arrow key cases.

#### clickHandler()[​](#clickHandler "Direct link to clickHandler()")

Used within [registerClickHandlers](#registerClickHandlers) to handle the common click cases like selecting results, closing the dropdown, etc.

#### keyHandler()[​](#keyHandler "Direct link to keyHandler()")

Used within [registerKeyHandlers](#registerKeyHandlers) to handle the common keyboard cases like navigating nodes, closing the dropdown, etc.

#### selectNode()[​](#selectnode "Direct link to selectNode()")

When used in conjunction with [keyUpDown](#keyUpDown) and other similar functions, this function will select the node that the user has navigated to.

#### moveToFirstNode()[​](#movetofirstnode "Direct link to moveToFirstNode()")

When used in conjunction with [keyUpDown](#keyUpDown) and other similar functions, this function will move the user to the first node in the dropdown.

#### moveToLastNode()[​](#movetolastnode "Direct link to moveToLastNode()")

When used in conjunction with [keyUpDown](#keyUpDown) and other similar functions, this function will move the user to the last node in the dropdown.

#### moveToNode()[​](#movetonode "Direct link to moveToNode()")

When used in conjunction with [keyUpDown](#keyUpDown) and other similar functions, this function will move the user to the node that is passed in.

### Required functions to implement[​](#required-functions-to-implement "Direct link to Required functions to implement")

We bootstrap a lot of the functionality within the component but there are some functions that you will need to implement yourself. This is because we don't know what your data looks like, how you want to filter it, etc.

#### fetchDataset()[​](#fetchdataset "Direct link to fetchDataset()")

Implementors should return a dataset that will be used to filter and render the results, this can be provided as a promise or a synchronous call.

#### filterDataset(dataset)[​](#filterdatasetdataset "Direct link to filterDataset(dataset)")

Implementors should return a filtered dataset based on the search term that the user has entered, this is entirely up to your as long as you set the results.

#### filterMatchDataset()[​](#filtermatchdataset "Direct link to filterMatchDataset()")

This can either just return the base dataset or you can use it to mutate the dataset to show how the results matched the search term i.e. adding links and whatnot.

#### renderDropdown()[​](#renderdropdown "Direct link to renderDropdown()")

Where and how do you want the data to be rendered? This is entirely up to you.

#### componentSelector()[​](#componentselector "Direct link to componentSelector()")

We need to know where to find the component in the DOM, this is the selector that will be used to find the component.

#### dropdownSelector()[​](#dropdownselector "Direct link to dropdownSelector()")

We need to know where to find the dropdown in the DOM, this is the selector that will be used to find the dropdown.

#### triggerSelector()[​](#triggerselector "Direct link to triggerSelector()")

We need to know where to find the trigger in the DOM, this is the selector that will be used to find the trigger.

For example usages view the [examples](https://moodledev.io/docs/4.4/guides/javascript/comboboxsearch/examples) page.