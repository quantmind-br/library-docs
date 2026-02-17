---
title: Hooks API | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/apis/core/hooks
source: sitemap
fetched_at: 2026-02-17T15:24:46.650652-03:00
rendered_js: false
word_count: 1665
summary: This document explains the Moodle Hooks API, a PSR-14 compliant system for customizing core functionality and plugins through hook emitters, instances, and callbacks.
tags:
    - moodle
    - hooks-api
    - psr-14
    - plugin-development
    - php
    - callbacks
category: api
---

This page describes the Hooks API which is a replacement for some of the lib.php based one-to-many [plugin callbacks](https://docs.moodle.org/dev/Callbacks) implementing on [PSR-14](https://www.php-fig.org/psr/psr-14/).

The most common use case for hooks is to allow customisation of standard plugins or core functionality through hook callbacks in local plugins. For example adding a custom institution password policy that applies to all enabled authentication plugins through a new local plugin.

## Hook Policies[​](#hook-policies "Direct link to Hook Policies")

New hooks added to Moodle from Moodle 4.4 onwards must meet the following rules:

- When describing a hook which happens before or after, the following modifiers are allowed:
  
  - `before`
  - `after`
- When a modifier is used, it should be used as a *prefix*
- Hooks belonging to a core subsystem should be located within that subsystem, and *not* in the `core` subsystem
- Hook descriptions **should** be in English, and **should not** use language strings or support translation

Examples of valid hook names

- `\core_course\hook\before_course_visibility_changed`
- `\core_form\hook\before_form_validation`
- `\core_form\hook\after_form_validation`
- `\core\hook\navigation\before_render`

## General concepts[​](#general-concepts "Direct link to General concepts")

### Mapping to PSR-14[​](#mapping-to-psr-14 "Direct link to Mapping to PSR-14")

Moodle does not allow camelCase for naming of classes and method and Moodle already has events, however the PSR-14 adherence has higher priority here.

PSR-14HooksEventHookListenerHook callbackEmitterHook emitterDispatcherHook dispatcher (implemented in Hook manager)Listener ProviderHook callback provider (implemented in Hook manager)

### Hook emitter[​](#hook-emitter "Direct link to Hook emitter")

A *Hook emitter* is a place in code where core or a plugin needs to send or receive information to/from any other plugins. The exact type of information flow facilitated by hooks is not defined.

### Hook instance[​](#hook-instance "Direct link to Hook instance")

Information passed between subsystem and plugins is encapsulated in arbitrary PHP class instances. These can be in any namespace, but generally speaking they should be placed in the `some_component\hook\*` namespace.

Hooks are encouraged to describe themselves and to provide relevant metadata to make them easier to use and discover. There are two ways to describe a hook:

- implement the `\core\hook\described_hook` interface, which has two methods:
  
  - `get_description(): string;`
  - `get_tags(): array;`
- add an instance of the following attributes to the class:
  
  - `\core\attribute\label(string $description)`
  - `\core\attribute\tags($a, $set, $of, $tags, ...)`
  - `\core\attribute\hook\replaces_callbacks('a_list_of_legacy_callbacks', 'that_this_hook_replaces')`

### Hook callback[​](#hook-callback "Direct link to Hook callback")

The code executing a hook does not know in advance which plugin is going to react to a hook.

Moodle maintains an ordered list of callbacks for each class of hook. Any plugin is free to register its own hook callbacks by creating a `db/hooks.php` file. The specified plugin callback method is called whenever a relevant hook is dispatched.

### Hooks overview page[​](#hooks-overview-page "Direct link to Hooks overview page")

The **Hooks overview page** lists all hooks that may be triggered in the system together with all registered callbacks. It can be accessed by developers and administrators from the Site administration menu.

This page is useful especially when adding custom local plugins with hook callbacks that modify standard Moodle behaviour.

In special cases administrators may override default hook callback priorities or disable some unwanted callbacks completely:

/config.php

```
$CFG->hooks_callback_overrides=[
\mod_activity\hook\installation_finished::class=>[
'test_otherplugin\\callbacks::activity_installation_finished'=>['disabled'=>true],
],
];
```

The hooks overview page will automatically list any hook which is placed inside any `*\hook\*` namespace within any Moodle component. If you define a hook which is *not* in this namespace then you **must** also define a new `\core\hook\discovery_agent` implementation in `[component]\hooks`.

## Adding new hooks[​](#adding-new-hooks "Direct link to Adding new hooks")

1. Developer first identifies a place where they need to ask or inform other plugins about something.
2. Depending on the location a new class implementing `core\hook\described_hook` is added to `core\hook\*` or `some_plugin\hook\*` namespace as appropriate.
3. Optionally the developer may wish to allow the callback to stop any subsequent callbacks from receiving the object. If so, then the object should implement the `Psr\EventDispatcher\StoppableEventInterface` interface.
4. Optionally if any data needs to be sent to hook callbacks, the developer may add internal hook constructor, some instance properties for data storage and public methods for data access from callbacks.

Hook classes may be any class you like. When designing a new Hook, you should think about how consumers may wish to change the data they are passed.

All hook classes should be defined as final, if needed traits can help with code reuse in similar hooks.

Hooks not located in standard locations

If you define a hook which is *not* in the `[component]\hook\*` namespace then you **must** also define a new `\core\hook\discovery_agent` implementation in `[component]\hooks`.

/mod/example/classes/hooks.php

```
<?php

namespacemod_example;

classhooksimplements\core\hook\discovery_agent{
publicstaticfunctiondiscover_hooks():array{
return[
[
'class'=>\mod_example\local\entitychanges\create_example::class,
'description'=>'A hook fired when an example was created',
],
];
}
}
```

### Example of hook creation[​](#example-of-hook-creation "Direct link to Example of hook creation")

Imagine mod\_activity plugin wants to notify other plugins that it finished installation, then mod\_activity plugin developer adds a new hook and calls it at the end of plugin installation process.

- Described by attribute
- Described using Interface

/mod/activity/classes/hook/installation\_finished.php

```
<?php
namespacemod_activity\hook;

#[\core\attribute\label('Hook dispatched at the very end of installation of mod_activity plugin.')]
#[\core\attribute\tags('installation')]
finalclassinstallation_finished{
publicfunction__construct(
publicreadonlystring$version,
){
}
}
```

/mod/activity/db/install.php

```
<?php
functionxmldb_activity_install(){
$hook=new\mod_activity\hook\installation_finished();
\core\di::get(\core\hook\manager::class)->dispatch($hook);
}

```

## Dispatching hooks[​](#dispatching-hooks "Direct link to Dispatching hooks")

Once a hook has been created, it needs to be *dispatched*. The dispatcher is responsible for ordering all listeners and calling them with the hook data.

The hook manager is responsible for dispatching hook instances using the `dispatch(object $hook)` method.

The `dispatch` method is an instance method and requires an instance of the hook manager.

From Moodle 4.4 you should make use of the [Dependency Injection](https://moodledev.io/docs/5.0/apis/core/di) system, for example:

Dispatching a hook with DI

```
\core\di::get(\core\hook\manager::class)->dispatch($hook);
```

Using DI for dependency injection has the benefit that the hook manager can use fixture callbacks to test a range of behaviours, for example:

Mocking a hook listener

```
// Unit test.
publicfunctiontest_before_standard_footer_html_hooked():void{
// Load the callback classes.
require_once(__DIR__.'/fixtures/core_renderer/before_standard_footer_html_callbacks.php');

// Replace the version of the manager in the DI container with a phpunit one.
\core\di::set(
\core\hook\manager::class,
\core\hook\manager::phpunit_get_instance([
// Load a list of hooks for `test_plugin1` from the fixture file.
'test_plugin1'=>__DIR__.
'/fixtures/core_renderer/before_standard_footer_html_hooks.php',
]),
);

$page=newmoodle_page();
$renderer=newcore_renderer($page,RENDERER_TARGET_GENERAL);

$html=$renderer->standard_footer_html();
$this->assertIsString($html);
$this->assertStringContainsString('A heading can be added',$html);
}

// fixtures/core_renderer/before_standard_footer_html_callbacks.php
finalclassbefore_standard_footer_html_callbacks{
publicstaticfunctionbefore_standard_footer_html(
\core\hook\output\before_standard_footer_html$hook,
):void{
$hook->add_html("<h1>A heading can be added</h1>");
}
}

// fixtures/core_renderer/before_standard_footer_html_hooks.php
$callbacks=[
[
'hook'=>\core\hook\output\before_standard_footer_html::class,
'callback'=>[
\test_fixtures\core_renderer\before_standard_footer_html_callbacks::class,
'before_standard_footer_html',
],
],
];
```

note

Prior to Moodle 4.3 the only way to dispatch a hook is by accessing the manager instance:

```
\core\hook\manager::get_instance()->dispatch($hook);
```

This approach is harder to test in situ.

## Registering of hook callbacks[​](#registering-of-hook-callbacks "Direct link to Registering of hook callbacks")

Any plugin is free to register callbacks for all core and plugin hooks. The registration is done by adding a `db/hooks.php` file to plugin. Callbacks may be provided as a PHP callable in either:

- string notation, in the form of `some\class\name::static_method`; or
- array notation, in the form of `[\some\class\name::class, 'static_method']`.

Use of array notation

Support for Array notated callbacks was introduced in Moodle 4.4. If you are writing a callback for a Moodle 4.3 site, you *must* use the string notation.

Hook callbacks are executed in the order of their priority from highest to lowest. Any guidelines for callback priority should be described in hook descriptions if necessary.

caution

Hooks may be dispatched at any time, *including during system installation and upgrade* (for example `before_http_headers`). Callback methods for such hooks must take extra care to ensure the plugin is properly initialised and that the database is available if database calls are made (as the database does not exist during site installation).

The `during_initial_install()` function can be used to check whether the the site is currently being installed, and `get_config('your_pluginname', 'version')` are two ways to conditionally make database queries or use API functions. `isset($CFG->upgraderunning)` can also be used to test if an upgrade is running. Failing to implement these checks may render the web install/upgrade page unusable.

Please note that the legacy component callback system did *not* call the `lib.php` callbacks during installation or upgrade. As such, when porting these callbacks to hooks, you may need to implement additional checks as described above.

### Example of hook callback registration[​](#example-of-hook-callback-registration "Direct link to Example of hook callback registration")

First developer needs to add a new static method to some class that accepts instance of a hook as parameter.

/local/stuff/classes/local/hook\_callbacks.php

```
<?php
namespacelocal_stuff\local;
use\mod_activity\hook\installation_finished;

classhook_callbacks{
publicstaticfunctionactivity_installation_finished(installation_finished$hook):void{
if(during_initial_install()){
return;
}
if(!get_config('local_stuff','version'){
return;
}
// Do something...
}
}
```

Then the developer has to register this new method as the hook callback by adding it to the `db/hooks.php` file.

/local/stuff/db/hooks.php

```
<?php
$callbacks=[
[
'hook'=>mod_activity\hook\installation_finished::class,
'callback'=>[\local_stuff\local\hook_callbacks::class,'activity_installation_finished'],
'priority'=>500,
],
];
```

Callback registrations are cached, so developers should to either increment the version number for the component they place the hook into. During development it is also possible to purge caches.

In this particular example, the developer would probably also add some code to `db/install.php` to perform the necessary action in case the hook gets called before the `local_stuff` plugin is installed.

## Deprecation of legacy lib.php callbacks[​](#deprecation-of-legacy-libphp-callbacks "Direct link to Deprecation of legacy lib.php callbacks")

Hooks are a direct replacement for one-to-many lib.php callback functions that were implemented using the `get_plugins_with_function()`, `plugin_callback()`, or `component_callback()` functions.

If a hook implements the `core\hook\deprecated_callback_replacement` interface, and if deprecated `lib.php` callbacks can be listed in `get_deprecated_plugin_callbacks()` hook method then developers needs to only add extra parameter to existing legacy callback functions and the hook manager will trigger appropriated deprecated debugging messages when it detects plugins that were not converted to new hooks yet.

Legacy fallback

Please note **it is** possible for plugin to contain both legacy `lib.php` callback and PSR-14 hook callbacks.

This allows community contributed plugins to be made compatible with multiple Moodle branches.

The legacy `lib.php` callbacks are automatically ignored if hook callback is present.

## Example how to migrate legacy callback[​](#example-how-to-migrate-legacy-callback "Direct link to Example how to migrate legacy callback")

This example describes migration of `after_config` callback from the very end of `lib/setup.php`.

First we need a new hook:

- Described by attribute
- Described using Interface

/lib/classes/hook/after\_config.php

```
<?php
namespacecore\hook;

usecore\attribute;

#[attribute\label('Hook dispatched at the very end of lib/setup.php')]
#[attribute\tags('config')]
#[attribute\hook\replaces_callbacks('after_config')]
finalclassafter_config{
}
```

The hook needs to be emitted immediately after the current callback execution code, and an extra parameter `$migratedtohook` must be set to true in the call to `get_plugins_with_function()`.

/lib/setup.php

```

// Allow plugins to callback as soon possible after setup.php is loaded.
$pluginswithfunction=get_plugins_with_function('after_config','lib.php',true,true);
foreach($pluginswithfunctionas$plugins){
foreach($pluginsas$function){
try{
$function();
}catch(Throwable$e){
debugging("Exception calling '$function'",DEBUG_DEVELOPER,$e->getTrace());
}
}
}
// Dispatch the new Hook implementation immediately after the legacy callback.
\core\di::get(\core\hook\manager::class())->dispatch(new\core\hook\after_config());
```

## Hooks which contain data[​](#hooks-which-contain-data "Direct link to Hooks which contain data")

It is often desirable to pass a data object when dispatching hooks.

This can be useful where you are passing code that consumers may wish to change.

Since the hook is an arbitrary PHP object, it is possible to create any range of public data and/or method you like and for the callbacks to use those methods and properties for later consumption.

/lib/classes/hook/block\_delete\_pre.php

```
<?php

namespacecore\hook;

usecore\attribute;

#[attribute\label('A hook dispatched just before a block instance is deleted')]
#[attribute\hook\replaces_callbacks('pre_block_delete')]
finalclassblock_delete_pre{
publicfunction__construct(
publicreadonly\stdClass$blockinstance,
){}
}
```

When dispatching the hook, it behaves as any other normal PHP Object:

/lib/blocklib.php

```
// Allow plugins to use this block before we completely delete it.
if($pluginsfunction=get_plugins_with_function('pre_block_delete','lib.php',true,true)){
foreach($pluginsfunctionas$plugintype=>$plugins){
foreach($pluginsas$pluginfunction){
$pluginfunction($instance);
}
}
}
}
$hook=new\core\hook\block_delete_pre($instance);
\core\di::get(\core\hook\manager::class())->dispatch($hook);
```

## Hooks which can be stopped[​](#hooks-which-can-be-stopped "Direct link to Hooks which can be stopped")

In some situations it is desirable to allow a callback to stop execution of a hook. This can happen in situations where the hook contains that should only be set once.

The Moodle hooks implementation has support for the full PSR-14 specification, including Stoppable Events.

To make use of Stoppable events, the hook simply needs to implement the `Psr\EventDispatcher\StoppableEventInterface` interface.

/lib/classes/hook/block\_delete\_pre.php

```
<?php

namespacecore\hook;

usecore\attribute;

#[attribute\label('A hook dispatched just before a block instance is deleted')]
#[attribute\hook\replaces_callbacks('pre_block_delete')]
finalclassblock_delete_preimplements
Psr\EventDispatcher\StoppableEventInterface
{
publicfunction__construct(
publicreadonly\stdClass$blockinstance,
){}

publicfunctionisPropagationStopped():bool{
return$this->stopped;
}

publicfunctionstop():void{
$this->stopped=true;
}
}
```

A callback will only be called if the hook was not stopped before-hand. Depending on the hook implementation, it can stop he

/local/myplugin/classes/callbacks.php

```
<?php

namespacelocal_myplugin;

classcallbacks{
publicstaticfunctionblock_pre_delete(\core\hook\block_delete_pre$hook):void{
// ...
$hook->stop();
}
}
```

## Tips and Tricks[​](#tips-and-tricks "Direct link to Tips and Tricks")

Whilst not being formal requirements, you are encouraged to:

- describe and tag your hook as appropriate using either:
  
  - the `\core\hook\described_hook` interface; or
  - the `\core\attribute\label` and `\core\attribute\tags` attributes
- make use of constructor property promotion combined with readonly properties to reduce unnecessary boilerplate.