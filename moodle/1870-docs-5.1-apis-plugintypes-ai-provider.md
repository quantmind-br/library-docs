---
title: Providers | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/apis/plugintypes/ai/provider
source: sitemap
fetched_at: 2026-02-17T15:34:41.971796-03:00
rendered_js: false
word_count: 1045
summary: This document explains how to develop and implement AI Provider plugins for Moodle, detailing the architecture, class requirements, and processing methods needed to interface with external AI services.
tags:
    - moodle-development
    - ai-subsystem
    - plugin-development
    - php-api
    - ai-provider
    - backend-architecture
category: guide
---

Providers are the interface between the [AI subsystem](https://moodledev.io/docs/5.1/apis/subsystems/ai) and external AI. Their focus should be on converting the data requested into the format needed by the external AI, and then correctly providing the response back.

Incoming data to the Provider plugin arrives via the Manager `core_ai\manager`. The Manager is the connective tissue between the Provider and the [Placement](https://moodledev.io/docs/5.1/apis/plugintypes/ai/placement) plugins. Likewise, all responses from the Provider plugin are handed back to the Manager before being passed to the Placement plugin.

A Provider plugin allows many "provider instances" to be defined, each of which can support a different set of configurations. This facilitates having providers for specific tasks. So, you can use a more efficient model for lightweight tasks like summarisation, and a more fully featured model for text generation. Another example is defaulting to using a cheaper model with a lower token limit, and then falling back to a more expensive model if a request is too large for the default model.

The Golden Rule:

Placements **do not** know about Providers, and Providers **do not** know about Placements. Everything should go via the Manager.

## Class implementation[​](#class-implementation "Direct link to Class implementation")

Providers are defined as classes in their own namespace according to their plugin name. The naming convention for a Provider class is `aiprovider_<plugin name>`. For example: `aiprovider_openai`, or `aiprovider_azureai` (with a corresponding namespace).

Each Provider **must** inherit from the `\core_ai\provider` abstract class.

### Required Methods[​](#required-methods "Direct link to Required Methods")

They must also implement the following methods:

**`get_action_list(): array`**

This is the list of Actions that are supported by this Provider, for example the `aiprovider_openai` plugin defines this as:

```
publicstaticfunctionget_action_list():array{
return[
\core_ai\aiactions\generate_text::class,
\core_ai\aiactions\generate_image::class,
\core_ai\aiactions\summarise_text::class,
];
}
```

**`is_provider_configured(): bool`**

Each provider will need to specify what it takes to be considered as configured. It is likely that each provider will have a set of keys necessary to access the external AI API.

The `is_provider_configured()` must return `true` for UI component visibility and functionality. If not overridden, it will return `false` by default.

For example, the `aiprovider_azureai` provider checks values are set for `$this->apikey` and `$this->apiendpoint` and returns the result.

```
publicfunctionis_provider_configured():bool{
return!empty($this->config['apikey'])&&!empty($this->config['endpoint']);
}
```

## Process classes[​](#process-classes "Direct link to Process classes")

For each action supported by the provider, the provider plugin **must** implement a `process_<action>` class, where `<action>` is the name of the action. For example: `process_generate_image`.

Every process action class **must** inherit from the `\core_ai\process_base` abstract class.

The process action class **must** implement a `process()` method. This method is responsible for converting the data requested by an Action into the format needed by the external AI services API, and then correctly providing the response back from the AI in an Action Response object.

The process action classes and process method are expected by the manager to exist and be callable.

As most provider plugins will support more than one action, it is recommended to create an `abstract_processor` class that inherits from the `\core_ai\process_base` class and then have each process action class inherit from this abstract class.

For example, the `aiprovider_openai` plugin defines an `abstract_processor` class that inherits from the `\core_ai\process_base` class and then the `process_generate_image`, `process_generate_text` and `process_summarise_text` classes inherit from this abstract class.

This can be visualised as follows:

Apart from this, Providers are free to define their own structure. It should be kept in mind that Providers are designed to be a 'thin wrapper' around the external AI systems API. They shouldn't store data, or have their own UI elements (beyond what is required for configuration).

## Plugin structure[​](#plugin-structure "Direct link to Plugin structure")

Provider plugins reside in the `ai/provider` directory.

Each Provider is in a separate subdirectory and consists of a number of mandatory files and any other files the developer is going to use.

The typical directory layout for the Provider plugin, using OpenAI Provider as an example:

```
.
├── amd
│   ├── build
│   │   ├── modelchooser.min.js
│   │   └── modelchooser.min.js.map
│   └── src
│       └── modelchooser.js
├── classes
│   ├── abstract_processor.php
│   ├── aimodel
│   │   ├── gpt4o.php
│   │   └── o1.php
│   ├── form
│   │   ├── action_form.php
│   │   ├── action_generate_image_form.php
│   │   └── action_generate_text_form.php
│   ├── helper.php
│   ├── hook_listener.php
│   ├── privacy
│   │   └── provider.php
│   ├── process_generate_image.php
│   ├── process_generate_text.php
│   ├── process_summarise_text.php
│   └── provider.php
├── db
│   └── hooks.php
├── lang
│   └── en
│       └── aiprovider_openai.php
├── tests
│   ├── fixtures
│   │   ├── image_request_success.json
│   │   ├── test.jpg
│   │   └── text_request_success.json
│   ├── process_generate_image_test.php
│   ├── process_generate_text_test.php
│   ├── process_summarise_text_test.php
│   └── provider_test.php
└── version.php

```

## Provider Settings[​](#provider-settings "Direct link to Provider Settings")

Settings for the Provider are defined as a [Hook](https://moodledev.io/docs/5.1/apis/core/hooks). Each Provider plugin should create a new `classes/hook_listener.php` file. This file should contain a class with a static method that defines the hook callback. create a new admin settings page using `core_ai\admin\admin_settingspage_provider` class. This class should implement a `set_form_definition_for_aiprovider_<plugin name>` method.

This method should define the settings form for the provider plugin, using the provided `mform` object.

For example, the `aiprovider_openai` plugin defines this:

```
namespaceaiprovider_openai;
usecore_ai\hook\after_ai_provider_form_hook;

classhook_listener{

/**
     * Hook listener for the Open AI instance setup form.
     *
     * @param after_ai_provider_form_hook $hook The hook to add to the AI instance setup.
     */
publicstaticfunctionset_form_definition_for_aiprovider_openai(after_ai_provider_form_hook$hook):void{
if($hook->plugin!=='aiprovider_openai'){
return;
}

$mform=$hook->mform;

// Required setting to store OpenAI API key.
$mform->addElement(
'passwordunmask',
'apikey',
get_string('apikey','aiprovider_openai'),
['size'=>75],
);
$mform->addHelpButton('apikey','apikey','aiprovider_openai');
$mform->addRule('apikey',get_string('required'),'required',null,'client');

// Setting to store OpenAI organization ID.
$mform->addElement(
'text',
'orgid',
get_string('orgid','aiprovider_openai'),
['size'=>25],
);
$mform->setType('orgid',PARAM_TEXT);
$mform->addHelpButton('orgid','orgid','aiprovider_openai');

}

}
```

Because a hook is used to define the settings, Provider plugins also need to have a `db/hooks.php` file to register its hook callback. The specified plugin callback method is called whenever the provider instance is chosen in the provider administration settings.

For example, the `aiprovider_openai` plugin defines this:

```
defined('MOODLE_INTERNAL')||die();

$callbacks=[
[
'hook'=>\core_ai\hook\after_ai_provider_form_hook::class,
'callback'=>\aiprovider_openai\hook_listener::class.'::set_form_definition_for_aiprovider_openai',
],
];
```

## Action Settings[​](#action-settings "Direct link to Action Settings")

Each of the actions that a provider plugin supports can have its own settings. If an action requires additional settings, the provider class for the plugin should override the `get_action_settings()` method. The method must return an instance of `core_ai\form\action_settings_form`.

For example, the `aiprovider_openai` plugin defines this:

```
#[\Override]
publicstaticfunctionget_action_settings(
string$action,
array$customdata=[],
):action_settings_form|bool{
$actionname=substr($action,(strrpos($action,'\\')+1));
$customdata['actionname']=$actionname;
$customdata['action']=$action;
if($actionname==='generate_text'||$actionname==='summarise_text'){
returnnewform\action_generate_text_form(customdata:$customdata);
}elseif($actionname==='generate_image'){
returnnewform\action_generate_image_form(customdata:$customdata);
}

returnfalse;
}
```

The actual settings form for the actions should be defined in the `classes/form` directory. For example, the `aiprovider_openai` plugin defines `action_generate_text_form` and `action_generate_image_form` classes. These classes should extend the `core_ai\form\action_settings_form` class, and must implement the `definition()` method.

For example, the `aiprovider_openai` plugin defines this:

```
classaction_generate_text_formextendsaction_settings_form{
#[\Override]
protectedfunctiondefinition(){
$mform=$this->_form;
$actionconfig=$this->_customdata['actionconfig']['settings']??[];
$returnurl=$this->_customdata['returnurl']??null;
$actionname=$this->_customdata['actionname'];
$action=$this->_customdata['action'];
$providerid=$this->_customdata['providerid']??0;

// Action model to use.
$mform->addElement(
'text',
'model',
get_string("action:{$actionname}:model",'aiprovider_openai'),
'maxlength="255" size="20"',
);
$mform->setType('model',PARAM_TEXT);
$mform->addRule('model',null,'required',null,'client');
$mform->setDefault('model',$actionconfig['model']??'gpt-4o');
$mform->addHelpButton('model',"action:{$actionname}:model",'aiprovider_openai');

...
```

## Predefined models[​](#predefined-models "Direct link to Predefined models")

Pre-defined models allow AI providers to define specific model configurations that can be selected by users. This provides a better user experience by offering known model options with appropriate default parameters rather than requiring manual configuration.

### Creating Model Classes[​](#creating-model-classes "Direct link to Creating Model Classes")

To implement pre-defined models, you will need to create model classes in the `[your_plugin]/classes/aimodel` directory and extend the `core_ai\aimodel\base` class.

For example, `aiprovider_openai` plugin defines this:

```
namespaceaiprovider_openai\aimodel;

usecore_ai\aimodel\base;
useMoodleQuickForm;

classgpt4oextendsbaseimplementsopenai_base{
#[\Override]
publicfunctionget_model_name():string{
return'gpt-4o';
}

#[\Override]
publicfunctionget_model_display_name():string{
return'GPT-4o';
}

// Add other model-specific methods or properties
}
```

### Implementing Per-Model Settings[​](#implementing-per-model-settings "Direct link to Implementing Per-Model Settings")

To add configurable settings for individual models:

1. Override the `has_model_settings()` and `add_model_settings()` methods:
   
   ```
   #[\Override]
   publicfunctionhas_model_settings():bool{
   returntrue;
   }
   
   #[\Override]
   publicfunctionadd_model_settings(MoodleQuickForm$mform):void{
   $mform->addElement(
   'text',
   'top_p',
   get_string('settings_top_p','aiprovider_openai'),
   );
   $mform->setType('top_p',PARAM_FLOAT);
   $mform->addHelpButton('top_p','settings_top_p','aiprovider_openai');
   
   // Add more model settings as needed
   $mform->addElement(
   'text',
   'max_tokens',
   get_string('settings_max_tokens','aiprovider_openai'),
   );
   $mform->setType('max_tokens',PARAM_INT);
   }
   ```
2. Create a helper class to manage models. For example, the `aiprovider_openai` plugin defines this:
   
   ```
   namespaceaiprovider_openai;
   
   classhelper{
   /**
        * Get all model classes.
        *
        * @return array Array of model classes
        */
   publicstaticfunctionget_model_classes():array{
   $models=[];
   $modelclasses=\core_component::get_component_classes_in_namespace('aiprovider_openai','aimodel');
   foreach($modelclassesas$class=>$path){
   if(!class_exists($class)||!is_a($class,\core_ai\aimodel\base::class,true)){
   thrownew\coding_exception("Model class not valid: {$class}");
   }
   $models[]=$class;
   }
   return$models;
   }
   
   /**
        * Get a specific model class instance.
        *
        * @param string $modelname The model name
        * @return \core_ai\aimodel\base|null The model class or null if not found
        */
   publicstaticfunctionget_model_class(string$modelname):?\core_ai\aimodel\base{
   foreach(self::get_model_classes()as$modelclass){
   $model=new$modelclass();
   if($model->get_model_name()===$modelname){
   return$model;
   }
   }
   returnnull;
   }
   }
   ```

### Integrating with Action Settings Forms[​](#integrating-with-action-settings-forms "Direct link to Integrating with Action Settings Forms")

To add model settings to action forms, you will need to create a hook listener that adds the model settings to the action form.

For example, the `aiprovider_openai` plugin does these:

1. Create a hook listener that adds model settings to the action form:
   
   ```
   publicstaticfunctionset_model_form_definition_for_aiprovider_openai(after_ai_action_settings_form_hook$hook):void{
   if($hook->plugin!=='aiprovider_openai'){
   return;
   }
   
   $mform=$hook->mform;
   if(isset($mform->_elementIndex['modeltemplate'])){
   $model=$mform->getElementValue('modeltemplate');
   if(is_array($model)){
   $model=$model[0];
   }
   
   // Handle custom model option.
   if($model=='custom'){
   $mform->addElement('header','modelsettingsheader',get_string('settings','aiprovider_openai'));
   $mform->addElement(
   'textarea',
   'modelextraparams',
   get_string('extraparams','aiprovider_openai'),
   ['rows'=>5,'cols'=>20],
   );
   $mform->setType('modelextraparams',PARAM_TEXT);
   }else{
   // Handle pre-defined model settings.
   $targetmodel=helper::get_model_class($model);
   if($targetmodel&&$targetmodel->has_model_settings()){
   $mform->addElement('header','modelsettingsheader',get_string('settings','aiprovider_openai'));
   $targetmodel->add_model_settings($mform);
   }
   }
   }
   }
   ```
2. Register the hook callback in `db/hooks.php`:
   
   ```
   $callbacks=[
   [
   'hook'=>\core_ai\hook\after_ai_action_settings_form_hook::class,
   'callback'=>\aiprovider_openai\hook_listener::class.'::set_model_form_definition_for_aiprovider_openai',
   ],
   ];
   ```

### Model Selection UI[​](#model-selection-ui "Direct link to Model Selection UI")

To create a model selector UI for your action settings form, you will need to add the model selector element to your action settings form.

For example, `aiprovider_openai` plugin defines this:

```
// Create model selector options
$models=[];
foreach(helper::get_model_classes()as$modelclass){
$model=new$modelclass();
$models[$model->get_model_name()]=$model->get_model_display_name();
}
$models['custom']=get_string('custom_model','aiprovider_openai');

$mform->addElement(
'select',
'modeltemplate',
get_string('model_template','aiprovider_openai'),
$models
);
$mform->setDefault('modeltemplate','gpt-4o');
```

## Rate limiting[​](#rate-limiting "Direct link to Rate limiting")

Provider plugins by default implement rate limiting to prevent abuse of the external AI services. This is inherited from the `core_ai\provider` class. Developers don't need to implement rate limiting themselves.

This default rate limiting behaviour can be changed by overriding the `is_request_allowed()` method `core_ai\provider` class.