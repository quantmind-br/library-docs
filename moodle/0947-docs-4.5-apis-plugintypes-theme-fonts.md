---
title: Fonts | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/apis/plugintypes/theme/fonts
source: sitemap
fetched_at: 2026-02-17T15:12:52.946007-03:00
rendered_js: false
word_count: 247
summary: This document provides technical instructions on implementing custom fonts in Moodle, covering file location conventions, supported formats, and CSS placeholder syntax for themes and plugins.
tags:
    - moodle-development
    - custom-fonts
    - web-fonts
    - theme-customization
    - plugin-development
    - css-placeholders
category: guide
---

Version: 4.5

CSS3 standard introduced the possibility to specify custom fonts, see [CSS web fonts tutorial](http://www.w3schools.com/css/css3_fonts.asp).

Moodle includes support for plugin or theme fonts. It is very similar to theme images and pix subdirectories.

## Font file locations[​](#font-file-locations "Direct link to Font file locations")

Depending on where you intend to use the font put it into one of the following locations:

- `/lib/fonts/` Fonts used in core.
- `/plugindir/fonts/` Fonts used by plugin.
- `/theme/sometheme/fonts/` Theme specific fonts.

You can also override core and plugin fonts in theme:

- `/theme/sometheme/fonts_core/` Overridden core fonts.
- `/theme/sometheme/fonts_plugins/plugintype_pluginname/` Overridden fonts of some plugin.

important

- Subdirectories are not allowed.
- Use only lowercase alphanumeric characters and underscore in font file names.
- WOFF (Web Open Font Format), TTF (True Type Fonts), OTF (OpenType Fonts), SVG (Scalable Vector Graphic) and EOT (Embedded OpenType) fonts are supported, but it's recommended to use WOFF fonts.

### CSS placeholders[​](#css-placeholders "Direct link to CSS placeholders")

Use a font in a plugin

```
@font-face{
font-family: ThreeDumb;
src:url([[font:mod_book|3dumb.woff]]);
}
```

The placeholder references file `/mod/book/fonts/3dumb.woff`, the new font face could be for example used for book headings:

```
.path-mod-book.book_chapter_title{
font-family: ThreeDumb;
}
```

If you want to use some font in theme only, you can for example:

Use a font in theme only

```
@font-face{
font-family: goodDogFont;
src:url([[font:theme|good_dog.woff]]);
}

a{font-family:goodDogFont;}
```

The font would be stored in `/theme/yourtheme/fonts/good_dog.woff` file.

Based on previous example, if you want to use some font stored in `/lib/fonts/` directory, you have to replace `font:theme` by `font:core`.

### More free fonts[​](#more-free-fonts "Direct link to More free fonts")

Please respect all licenses for font redistribution, you can get some nice free fonts from [http://www.fontsquirrel.com](http://www.fontsquirrel.com) for example.

warning

This is not intended for forcing of something like Comic Sans on all your visitors ;-)