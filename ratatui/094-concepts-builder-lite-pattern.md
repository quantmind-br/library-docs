---
title: Builder Lite Pattern
url: https://ratatui.rs/concepts/builder-lite-pattern/
source: crawler
fetched_at: 2026-02-01T21:12:59.012281279-03:00
rendered_js: false
word_count: 165
summary: This document explains the 'Builder Lite' pattern used in Ratatui for configuring widgets through method chaining and provides guidance on avoiding common pitfalls when using setter methods.
tags:
    - ratatui
    - rust
    - builder-lite
    - widget-configuration
    - method-chaining
category: concept
---

In Ratatui, most widgets (and some other objects) use the [Builder Lite](https://matklad.github.io/2022/05/29/builder-lite.html) pattern to set fields. This allows the object to be created in a single shot with methods that setup how the widget will be displayed, without having to store the widget in a variable and mutate it.

The builder lite pattern consumes the `self` parameter of each method and returns a value with the updated field. An example of this from Paragraph (and any other widget that supports being automatically wrapped in a block):

```

#[must_use]
pubfnblock(mutself, block: Block<'a>) ->Self {
self.block = Some(block);
self
}
```

Which you might call like:

```

letparagraph= Paragraph::new("foobar").block(Block::bordered())
```

If you’ve reached this page after seeing an error or warning in your app’s compilation, then it’s likely that you are calling the setter methods against an object, but not storing or using the result. This will have no effect on the actual display of the widget and is usually a mistake.

E.g. the following code:

```

lettext= Text::raw("wrong");
text.centered();
```

Should be replaced with:

```

lettext= Text::raw("right").centered();
```

Or in situations where you want to reuse a widget’s setup more than once:

```

lettext= Text::raw("right");
letcentered_text=text.clone().centered();
letbold_text=text.bold();
```