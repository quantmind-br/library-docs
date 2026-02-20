---
title: Modal Dialogues | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/guides/javascript/modal
source: sitemap
fetched_at: 2026-02-17T15:15:52.131313-03:00
rendered_js: false
word_count: 609
summary: This document provides instructions on creating and managing accessible modal dialogues in Moodle using JavaScript modules, including standard modal types and custom implementations.
tags:
    - moodle-development
    - javascript-modals
    - user-interface
    - web-accessibility
    - moodle-js-api
    - modal-factory
    - mustache-templates
category: guide
---

The use of modal modules provides a simplified developer experience for creating modal dialogues within Moodle.

The module attempts to ensure that all accessibility requirements are met, including applying the correct aria roles, focus control, aria hiding background elements, and locking keyboard navigation.

Modals will fire events for common actions that occur within the modal for other code to listen to and react accordingly.

Moodle ships with several standard modal types for you to re-use including a simple cancel modal, and a save/cancel modal.

## Creating a basic modal[​](#creating-a-basic-modal "Direct link to Creating a basic modal")

Modals can be created by calling the static `create` method on the modal type you wish to create, for example:

Creating a stadard modal

```
importModalfrom'core/modal';

exportconstinit=async()=>{
const modal =awaitModal.create({
title:'Test title',
body:'<p>Example body content</p>',
footer:'An example footer content',
show:true,
removeOnClose:true,
});
}
```

Other standard options are described in the JS Documentation for [the MoodleConfig type](https://jsdoc.moodledev.io/master/module-core_modal.html#~MoodleConfig).

Support for earlier versions

If you are supporting an earlier version of Moodle, then you must use the Modal Factory and register your modal.

### Modal Factory[​](#modal-factory "Direct link to Modal Factory")

The Modal Factory can be used to instantiate a new Modal. The factory provides a `create` function, accepting some configuration which is used to create the modal instance, and an optional *trigger element*. The `create` function returns a Promise that is resolved with the created modal.

The configuration is provided as an object with key/value pairs. The options are:

**key****description**titlethe title to display in the modal header - note: this will render HTMLbodythe main content to be rendered in the modal bodyfooterthe content to be rendered in the modal footertypeone of the modal types registered with the factorylargea boolean to indicate if the modal should be wider than the default size

Basic instantiation of a modal

```
importModalFactoryfrom'core/modal_factory';

exportconstinit=async()=>{
const modal =awaitModalFactory.create({
title:'test title',
body:'<p>Example body content</p>',
footer:'An example footer content',
});
    modal.show();

// ...
};
```

Where text, language strings, or HTML is accepted, a Promise can also be provided.

Using a template to render the body

```
importModalFactoryfrom'core/modal_factory';
importTemplatesfrom'core/templates';

exportconstinit=async()=>{
const modal =awaitModalFactory.create({
title:'test title',
body:Templates.render('mod_example/example_modal_content',{id:42}),
footer:'An example footer content',
});
    modal.show();

// ...
};
```

#### Using the 'trigger'[​](#using-the-trigger "Direct link to Using the 'trigger'")

Moodle Modals created using the Modal Factory support an optional *trigger* element. Whilst this is available, it is no longer recommended and support for it will likely be removed in Moodle 4.3.

Providing a trigger

```
importModalFactoryfrom'core/modal_factory';
importTemplatesfrom'core/templates';
import$from'jquery';

exportconstinit=async()=>{
const modal =awaitModalFactory.create({
title:'test title',
body:Templates.render('mod_example/example_modal_content',{id:42}),
footer:'An example footer content',
},$('a.item-delete'));

// ...
};
```

## Instantiating modal types[​](#instantiating-modal-types "Direct link to Instantiating modal types")

A number of commonly used modals are available as standard, these include:

- a Delete / Cancel modal
- a Save / Cancel modal
- a Cancel modal

<!--THE END-->

- Moodle 4.3
- Moodle 4.2 and earlier

note

If you are developing code for use in Moodle 4.2, or earlier, then you must continue to follow the 4.2 guidelines.

To use these modals you can call the `create` method on the relevant Modal Class.

Creating a save/cancel modal

```
importModalSaveCancelfrom'core/modal_save_cancel';
import{get_string as getString}from'core/str';

exportconstinit=async()=>{
const modal =awaitModalSaveCancel.create({
title:'test title',
body:getString('confirmchange','mod_example'),
});

// ...
};
```

Each type of modal may fire additional events to allow your code to handle the new functionality being offered -- for example, if you wanted to have a save/cancel modal that you did some form validation on before saving you could do something like the example below.

Listening to a Save event

```
importModalSaveCancelfrom'core/modal_save_cancel';
importModalEventsfrom'core/modal_events';
import{get_string as getString}from'core/str';

exportconstinit=async()=>{
const modal =awaitModalSaveCancel.create({
title:'test title',
body:getString('confirmchange','mod_example'),
});

    modal.getRoot().on(ModalEvents.save,(e)=>{
// ...
})

// ...
};
```

## Creating a custom modal type[​](#creating-a-custom-modal-type "Direct link to Creating a custom modal type")

In some situations it is desirable to write a brand new modal.

There are two parts to this:

- a new Modal class which extends the `core/modal` class; and
- a template

Custom modals in Moodle 4.2 and earlier

Since Moodle 4.3, creating the Modal class is as simple as extending the `core/modal` class, and providing a `TYPE` property, and `TEMPLATE` property.

For older versions of Moodle, refer to the [Moodle 4.2 documentation](https://672834180938720008adb671--moodledevdocs.netlify.app/docs/4.2/guides/javascript/modal/#creating-a-custom-modal-type).

mod/example/amd/src/my\_modal.js

```
importModalfrom'core/modal';

exportdefaultclassMyModalextendsModal{
staticTYPE="mod_example/my_modal";
staticTEMPLATE="mod_example/my_modal";
}
```

The template should extend the `core/modal` core template and can override any of the title, body, or footer regions, for example:

mod/example/templates/my\_modal.mustache

```
{{< core/modal }}
    {{$title}}{{#str}} login {{/str}}{{/title}}
    {{$body}}
        <div class="container">
            <form>
                <div class="form-group row">
                    <label for="inputEmail" class="col-sm-2 col-form-label">{{#str}} email {{/str}}</label>
                    <div class="col-sm-10">
                        <input type="email" class="form-control" id="inputEmail" placeholder="{{#str}} email {{/str}}">
                    </div>
                </div>
                <div class="form-group row">
                    <label for="inputPassword" class="col-sm-2 col-form-label">{{#str}} password {{/str}}</label>
                    <div class="col-sm-10">
                        <input type="password" class="form-control" id="inputPassword" placeholder="{{#str}} password {{/str}}">
                    </div>
                </div>
            </form>
        </div>
    {{/body}}
    {{$footer}}
        <button type="button" class="btn btn-primary" data-action="login">{{#str}} login {{/str}}</button>
        <button type="button" class="btn btn-secondary" data-action="cancel">{{#str}} cancel {{/str}}</button>
    {{/footer}}
{{/ core/modal }}
```

Once defined, the new modal can be instantiated using the standard `create` method, for example:

Instantiating a custom modal

```
importMyModalfrom'mod_example/my_modal';

exportdefaultconstinit=async()=>{
// ...
const modal =awaitMyModal.create({});

    modal.show();
}
```

### Overriding default configuration[​](#overriding-default-configuration "Direct link to Overriding default configuration")

When creating your own modal type, you may wish to override the standard configuration. This can be achieved by overriding the `configure` class and providing your own options, for example:

Overriding standard options

```
importModalfrom'core/modal';

exportdefaultclassMyModalextendsModal{
staticTYPE="mod_example/my_modal";
staticTEMPLATE="mod_example/my_modal";

configure(modalConfig){
// Show this modal on instantiation.
        modalConfig.show=true;

// Remove from the DOM on close.
        modalConfig.removeOnClose=true;

super.configure(modalConfig);

// Accept our own custom arguments too.
if(modalConfig.someValue){
this.setSomeValue(someValue);
}
}

setSomeValue(value){
this.someValue= value;
}
}
```