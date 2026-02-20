---
title: HTML Writer API | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/apis/core/htmlwriter
source: sitemap
fetched_at: 2026-02-17T15:11:21.555998-03:00
rendered_js: false
word_count: 56
summary: This document explains how to use the Moodle HTML writer class to programmatically generate HTML tags and attributes within PHP renderer functions.
tags:
    - moodle
    - html-writer
    - php
    - rendering
    - html-generation
category: reference
---

Version: 4.5

Moodle has a class called *HTML writer* which allows you to output basic HTML tags. This is typically used within renderer functions, for example `question/type/*pluginname*/renderer.php`.

tip

Please consider using [templates](https://moodledev.io/docs/4.5/guides/templates) as an alternative to the *HTML writer*.

## Methods[​](#methods "Direct link to Methods")

### div[​](#div "Direct link to div")

```
html_writer::div(content,class="", attributes="");
```

Example usage:

```
html_writer::div('anonymous');// <div>anonymous</div>
html_writer::div('kermit','frog');// <div class="frog">kermit</div>
```

Attributes can be set by an array with key-value pairs.

```
html_writer::div('Mr','toad',array('id'=>'tophat'));
// <div class="toad" id="tophat">Mr/div>
```

### span[​](#span "Direct link to span")

```
html_writer::start_span('zombie').'BRAINS'.html_writer::end_span();
// <span class="zombie">BRAINS</span>
```

### Generic tags[​](#generic-tags "Direct link to Generic tags")

```
html_writer::tag(tag_name, contents, attributes=null);
html_writer::start_tag(tag_name, attributes=null;);
html_writer::end_tag(tag_name);
html_writer::empty_tag(tag_name, attributes=null);
html_writer::nonempty_tag(tag_name, content, attributes=null);
html_writer::attribute(name, value);
html_writer::attributes(attributes_array);
```