---
title: Atto | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/apis/plugintypes/atto
source: sitemap
fetched_at: 2026-02-17T15:25:21.396347-03:00
rendered_js: false
word_count: 0
summary: This document provides a template and example for implementing a custom button within the Moodle Atto text editor using the YUI framework.
tags:
    - moodle
    - atto-editor
    - javascript
    - plugin-development
    - yui-library
    - ui-component
category: reference
---

```
// This file is part of Moodle - http://moodle.org/
//
// Moodle is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Moodle is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Moodle.  If not, see <http://www.gnu.org/licenses/>.

/**
 * Example Button JavaScript for the atto_media plugin.
 *
 * @module   atto_media/button
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

Y.namespace('M.atto_media').Button=Y.Base.create(
'button',
Y.M.editor_atto.EditorPlugin,
[],
{
initializer:function(){
this.addButton({
callback:this._toggleMedia,
icon:'e/media',
inlineFormat:true,

// Key code for the keyboard shortcut which triggers this button:
keys:'66',

// Watch the following tags and add/remove highlighting as appropriate:
tags:'media'
});
},

_toggleMedia:function(){
// Handle the button click here.
// You can fetch any passed in parameters here as follows:
var langs =this.get('langs');
}
},{
ATTRS:{
// If any parameters were defined in the 'params_for_js' function,
// they should be defined here for proper access.
langs:{
value:['Default','Value']
}
}
}
);
```