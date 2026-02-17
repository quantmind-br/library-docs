---
title: Bootstrap 5 migration | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/guides/bs5migration
source: sitemap
fetched_at: 2026-02-17T15:28:31.460131-03:00
rendered_js: false
word_count: 1726
summary: This document outlines the phased migration process from Bootstrap 4 to Bootstrap 5, detailing specific refactoring steps and class replacements for a smooth transition. It provides technical guidance on upgrading dependencies, using compatibility bridges, and updating deprecated utility classes and components.
tags:
    - bootstrap-migration
    - frontend-development
    - scss-refactoring
    - moodle-development
    - css-frameworks
    - bootstrap-5
    - web-design-standards
category: guide
---

Bootstrap 5 has evolved with new features, improvements, and changes in its latest version, and along with this some breaking changes also come, which need to be addressed in the migration process.

To achieve a smoother process and facilitate the moment of the update, the migration has been divided into different steps:

1. **PopperJS upgrade**: This is the first step in the migration process, as Bootstrap 5 requires PopperJS version 2. This step is about upgrading the current PopperJS version to version 2. Because we still need PopperJS version 1 for Bootstrap 4 both versions will co-exist until all usages are migrated to v2.
2. **SCSS Deprecation process**: A SCSS deprecation process will be needed for the cleanup after BS5 upgrade. More details about it in [SCSS deprecation](https://moodledev.io/general/development/policies/deprecation/scss-deprecation).
3. **Refactoring BS4 features dropped in BS5**: This step is about refactoring the current Bootstrap 4 features that will be deprecated or dropped in its version 5 and they can be replaced with current codebase.
4. **Create a BS5 "bridge"**: Some simple breaking changes could be also addressed in advance creating a BS5 "bridge". With small additions to this "bridge", we can refactor in advance the occurrences in the codebase for some dropped features in BS5.
5. **BS5 upgrade**: Upgrade the current Bootstrap 4 version to version 5.
6. **BS4 backwards-compatibility layer**: Alongside the update, a new backwards-compatibility layer will also be created, and some of the Bootstrap 4 syntax will still work until the final deprecation. This will help third-party plugins to be updated in a more gradual way.
7. **Final deprecation**

note

The migration process will be done in a gradual way, and the steps will be executed in different phases. The first phase with the PopperJS upgrade, the SCSS deprecation process and the refactoring will be included in Moodle 4.4. The other steps will be ready in following releases. This documentation page will be updated accordingly with the process.

## Refactoring BS4 features dropped in BS5[​](#refactoring-bs4-features-dropped-in-bs5 "Direct link to Refactoring BS4 features dropped in BS5")

Some of the Bootstrap 4 classes will be deprecated or dropped in its version 5. To prepare for this, some of the current Bootstrap 4 classes usages have been replaced with version 5 compatible classes. Doing these refactors in advance, will help us to upgrade to Bootstrap 5 in the future.

### Badges[​](#badges "Direct link to Badges")

- Badge colour class helpers `.badge-*` have been replaced with background utilities (use `.bg-primary` instead of `.badge-primary`) combined with the corresponding text colour classes (`.text-dark` or `.text-white`) to meet accessibility contrast. Or use the new `.text-bg-*` classes.
- The `.badge-pill` class has been replaced with `.rounded-pill`

Don't

```
<spanclass="badge badge-danger badge-pill">Error badge</span>
```

Do

```
<spanclass="badge text-bg-danger rounded-pill">Error badge</span>
```

### Media[​](#media "Direct link to Media")

The `.media` component has been replaced with utility classes.

Don't

```
<divclass="media">
<divclass="media-left">
        [...]
</div>
<divclass="media-body">
        [...]
</div>
</div>
```

Do

```
<divclass="d-flex">
<divclass="flex-shrink-0">
        [...]
</div>
<divclass="flex-grow-1 ms-3">
        [...]
</div>
</div>
```

### Mixins[​](#mixins "Direct link to Mixins")

The following previously deprecated mixins will be dropped in BS5, so they can be refactored:

- hover, hover-focus, plain-hover-focus and hover-focus-active
- float-left, float-right and float-none
- nav-divider
- img-retina
- text-hide
- invisible
- form-control-focus
- text-emphasis-variant
- size
- make-container-max-widths
- g-variant and bg-gradient-variant

Don't

```
.collapse-list-item{
padding: $collapse-list-item-padding-y $collapse-list-item-padding-x;
@includehover-focus(){
background-color: $collapse-list-item-hover-bg;
border-color: $collapse-list-item-hover-border;
}
}
```

Do

```
.collapse-list-item{
padding: $collapse-list-item-padding-y $collapse-list-item-padding-x;
&:hover,
    &:focus{
background-color: $collapse-list-item-hover-bg;
border-color: $collapse-list-item-hover-border;
}
}
```

### Forms[​](#forms "Direct link to Forms")

- The `.form-group` helper class has been replaced with margins.
- The `.form-inline` helper class has been replaced with utility classes.

Don't

```
<formclass="form-inline">
<divclass="form-group">
        [...]
</div>
</form>
```

Do

```
<formclass="d-flex flex-wrap align-items-center">
<divclass="mb-3">
        [...]
</div>
</form>
```

### Card decks[​](#card-decks "Direct link to Card decks")

The `.card-deck` helper class has been replaced with utility classes.

Don't

```
<divclass="card-deck">
<divclass="card">
        [...]
</div>
<divclass="card">
        [...]
</div>
</div>
```

Do

```
<divclass="row row-cols-1 row-cols-sm-2">
<divclass="col">
<divclass="card">
            [...]
</div>
</div>
<divclass="col">
<divclass="card">
            [...]
</div>
</div>
</div>
```

## Create a BS5 "bridge"[​](#create-a-bs5-bridge 'Direct link to Create a BS5 "bridge"')

Some simple breaking changes could be also addressed in advance creating a BS5 "bridge". With small additions to this "bridge", we can refactor in advance the occurrences in the codebase for some dropped or changed features in BS5.

A new SCSS file `bs5-bridge.scss` has been created in the `theme/boost/scss/moodle` folder. This file will contain the necessary changes to make the codebase compatible with Bootstrap 5.

Example of a bridge in `bs5-bridge.scss`

```
/* In Bootstrap 5 the .no-gutters class has been replaced with .g-0, so we can
add a new class in the bridge file to make the codebase compatible with BS5. */
.g-0{
@extend .no-gutters;
}
```

### No gutters[​](#no-gutters "Direct link to No gutters")

The `.no-gutters` grid class has been replaced with `.g-0`.

Don't

```
<divclass="row no-gutters">
<divclass="col-6">[...]</div>
<divclass="col-6">[...]</div>
</div>
```

Do

```
<divclass="row g-0">
<divclass="col-6">[...]</div>
<divclass="col-6">[...]</div>
</div>
```

### Close button[​](#close-button "Direct link to Close button")

The `.close` class has been replaced with `.btn-close`.

Don't

```
<divclass="alert alert-warning alert-dismissible"role="alert">
  I'm an alert.
<buttontype="button"class="close"data-dismiss="alert"aria-label="Close">
<spanaria-hidden="true">&times;</span>
</button>
</div>
```

Do

```
<divclass="alert alert-warning alert-dismissible"role="alert">
  I'm an alert.
<buttontype="button"class="btn-close"data-dismiss="alert"aria-label="Close">
<spanaria-hidden="true">&times;</span>
</button>
</div>
```

### Directional utilities[​](#directional-utilities "Direct link to Directional utilities")

Several utilities have been renamed to use logical property names instead of directional ones.

- Renamed .float-left and .float-right to .float-start and .float-end.
- Renamed .border-left and .border-right to .border-start and .border-end.
- Renamed .rounded-left and .rounded-right to .rounded-start and .rounded-end.
- Renamed .ml-* and .mr-* to .ms-* and .me-\*.
- Renamed .pl-* and .pr-* to .ps-* and .pe-\*.
- Renamed .text-left and .text-right to .text-start and .text-end.

Don't

```
<divclass="ml-3 pr-sm-3">
<divclass="border-left text-left">[...]</div>
<divclass="float-right mr-auto">[...]</div>
</div>
```

Do

```
<divclass="ms-3 pe-sm-3">
<divclass="border-start text-start">[...]</div>
<divclass="float-end me-auto">[...]</div>
</div>
```

### Theme color level[​](#theme-color-level "Direct link to Theme color level")

In Bootstrap 4.x we used a function called `theme-color-level()` which was removed in Bootstrap 5. The prototype of the function was:

Previous version using `theme-color-level()`

```
@functiontheme-color-level($colorname, $level){
    [...]
}
[...]
theme-color-level('primary',1);
```

The replacement is now `shift-color()`. This function is used to shift a color by a percentage (weight) of shades. So, two major difference in the new version:

- we use the color definition instead of the color name
- we use percentages instead of levels.

Current version using `shift-color()`

```
@functionshift-color($color, $weight){
   [...]
}
[...]
shift-color($primary,10%);
```

As we transitioned from using levels to percentages, the parameters have changed. So instead of working with numbers (1 to 11), we now use percentages. To simplify this transition, Bootstrap 5 has established a new equivalency: each level increment from 1 now corresponds to a 10% shift.

From absolute levels to percentages

For example, if a theme-color-level was previously set to a value of 1, it will now be set to 10%. A level of two will be adjusted by 20% and so on.

We can use the following formula to convert the level to percentage:

Don't

```
theme-color-level('primary',1)
theme-color-level('primary',-2)
```

Do

```
shift-color($primary,10%);
shift-color($primary,-20%);
```

note

The `theme-color-level()` has been changed to `color-level()` and then subsequently removed and replaced by scale-color(). In the stable 5.0 the final decision was to adopt `shift-color()` so we will use this function in the bridge file.

### Rounded classes[​](#rounded-classes "Direct link to Rounded classes")

The `.rounded-sm` and `.rounded-lg` classes have been replaced with `.rounded-1` and `.rounded-3`.

Don't

```
<divclass="rounded-lg"> Rounded content </div>
```

Do

```
<divclass="rounded-3"> Rounded content </div>
```

### Screen reader utilities[​](#screen-reader-utilities "Direct link to Screen reader utilities")

"Screen reader" classes are now "visually hidden" classes.

- Renamed `.sr-only` and `.sr-only-focusable` to `.visually-hidden` and `.visually-hidden-focusable`.
- Renamed `sr-only()` and `sr-only-focusable()` mixins to `visually-hidden()` and `visually-hidden-focusable()`.

Don't

```
<spanclass="sr-only sr-only-focusable">
    Visually hidden text
</span>
```

Do

```
<spanclass="visually-hidden visually-hidden-focusable">
    Visually hidden text
</span>
```

Don't

```
.my-hidden-text {
    @include sr-only();
    @include sr-only-focusable();
}
```

Do

```
.my-hidden-text {
    @include visually-hidden();
    @include visually-hidden-focusable();
}
```

### Font utility classes[​](#font-utility-classes "Direct link to Font utility classes")

The `.font-weight-*` class has been replaced with `.fw-*` for brevity and consistency. The `.font-italic` class has been replaced with `.fst-italic` for brevity and consistency.

Don't

```
<spanclass="font-weight-bold font-italic">I'm a bold italic text</span>
```

Do

```
<spanclass="fw-bold fst-italic">I'm a bold italic text</span>
```

## Bootstrap 5 upgrade[​](#bootstrap-5-upgrade "Direct link to Bootstrap 5 upgrade")

After **Refactoring BS4 features dropped in BS5** and **Create a BS5 "bridge"**, the remaining Bootstrap breaking changes will be addressed in the upgrade to Bootstrap 5.

The `bs5-bridge.scss` SCSS file will be removed as it will no longer be needed, and the Bootstrap library in theme\_boost will be upgraded to version 5.3. After that the codebase will be fully compatible with Bootstrap 5.

### Refactor dropdowns positioning classes[​](#refactor-dropdowns-positioning-classes "Direct link to Refactor dropdowns positioning classes")

Replace `.dropdown-menu-[left|right]` with `.dropdown-menu-[start|end]`.

Don't

```
<divclass="dropdown-menu dropdown-menu-right">
    [...]
</div>
```

Do

```
<divclass="dropdown-menu dropdown-menu-end">
    [...]
</div>
```

### Refactor custom form elements[​](#refactor-custom-form-elements "Direct link to Refactor custom form elements")

- `.custom-check` is now `.form-check`.
- `.custom-check.custom-switch` is now `.form-check.form-switch`.
- `.custom-select` is now `.form-select`.
- `.custom-file` and `.form-file` have been replaced by custom styles on top of `.form-control`.
- `.custom-range` is now `.form-range`.
- Dropped `.input-group-append` and `.input-group-prepend`. You can now just add buttons and `.input-group-text` as direct children of the input groups.

Don't

```
<selectname="outcome"class="custom-select"> [...] </select>

<divclass="input-group">
<inputtype="text"class="form-control"> [...] </input>
<divclass="input-group-append">
<buttontype="submit"class="btn btn-primary search-icon">
            {{#pix}} a/search, core {{/pix}}
<spanclass="visually-hidden">{{#str}} search, core {{/str}}</span>
</button>
</div>
</div>
```

Do

```
<selectname="outcome"class="form-select"> [...] </select>

<divclass="input-group">
<inputtype="text"class="form-control"> [...] </input>
<buttontype="submit"class="btn btn-primary search-icon">
        {{#pix}} a/search, core {{/pix}}
<spanclass="visually-hidden">{{#str}} search, core {{/str}}</span>
</button>
</div>
```

### Refactor media query mixins[​](#refactor-media-query-mixins "Direct link to Refactor media query mixins")

- `media-breakpoint-down()` uses the breakpoint itself instead of the next breakpoint (e.g., `media-breakpoint-down(lg)` instead of `media-breakpoint-down(md)` targets viewports smaller than lg).
- In `media-breakpoint-between()` the second parameter also uses the breakpoint itself instead of the next breakpoint (e.g., `media-breakpoint-between(sm, lg)` instead of `media-breakpoint-between(sm, md)` targets viewports between sm and lg).

Don't

```
// This will target viewports smaller than md.
@includemedia-breakpoint-down(sm){
    [...]
}
```

Do

```
// This will target viewports smaller than md.
@includemedia-breakpoint-down(md){
    [...]
}
```

### Refactor BS5 data attributes[​](#refactor-bs5-data-attributes "Direct link to Refactor BS5 data attributes")

Data attributes for all JavaScript plugins are now namespaced to help distinguish Bootstrap functionality from our own code.

Don't

```
// Tooltip.
<buttonclass="btn btn-outline-secondary"
type="button"
data-toggle="tooltip"
data-html="true"
title="{{#str}} string_with_html, block_my_block {{/str}}"
>
    {{#pix}} i/info, core {{/pix}}
</button>

// Collapse.
<buttonclass="btn btn-primary"type="button"data-toggle="collapse"data-target="#collapsableContent"aria-expanded="false"aria-controls="collapseExample">
    Open the collapsable content
</button>
<divclass="collapse"id="collapsableContent">
    [...]
</div>
```

Do

```
// Tooltip.
<buttonclass="btn btn-outline-secondary"
type="button"
data-bs-toggle="tooltip"
data-bs-html="true"
title="{{#str}} string_with_html, block_my_block {{/str}}"
>
    {{#pix}} i/info, core {{/pix}}
</button>

// Collapse.
<buttonclass="btn btn-primary"
type="button"
data-bs-toggle="collapse"
data-bs-target="#collapsableContent"
aria-expanded="false"
aria-controls="collapseExample"
>
    Open the collapsable content
</button>
<divclass="collapse"id="collapsableContent">
    [...]
</div>
```

### Bootstrap 5 and Jquery[​](#bootstrap-5-and-jquery "Direct link to Bootstrap 5 and Jquery")

Bootstrap dropped jQuery dependency and rewrote plugins to be in regular JavaScript. This means that all the jQuery Bootstrap-related code in the Moodle codebase has been rewritten in vanilla JavaScript.

Don't

```
import$from'jquery';

$(document).on('shown shown.bs.tab',function(e){
[...]
$('#my-dropdown').dropdown('toggle');
});
```

Do

```
importDropdownfrom'theme_boost/bootstrap/dropdown';
document.querySelectorAll('[data-bs-toggle="tab"]').forEach((tab)=>{
    tab.addEventListener('shown.bs.tab',(e)=>{
[...]
const bootstrapDropdown =newDropdown('#my-dropdown');
        bootstrapDropdown.toggle();
});
});
```

backwards compatibility

Although Bootstrap does not need jQuery anymore, it is still possible to use it in Moodle. See [MDL-84324](https://moodle.atlassian.net/browse/MDL-84324) for more information.

## BS4 backwards-compatibility layer[​](#bs4-backwards-compatibility-layer "Direct link to BS4 backwards-compatibility layer")

The migration from Bootstrap 4 to Bootstrap 5 involves a transition period to allow third-party plugins to update gradually. To facilitate this, a backwards-compatibility layer has been created, ensuring that some Bootstrap 4 syntax will continue to function until final deprecation in Moodle 6.0. This approach aims to provide developers with sufficient time to adapt their code to the new Bootstrap 5 framework.

The BS4 backwards-compatibility layer encompasses three crucial aspects to facilitate a smooth transition for third-party contributions:

1. **Bootstrap jQuery support**: This allows existing plugins and components that rely on jQuery to continue functioning while developers work on updating their code to the new vanilla JavaScript approach.
2. **SCSS helpers and utilities**: The compatibility layer includes some SCSS helpers and utilities from Bootstrap 4, enabling developers to gradually adapt their custom styles to the new Bootstrap 5.
3. **Bootstrap 4 old data attributes syntax silent replacement**: This feature quietly replaces the old Bootstrap 4 data attribute syntax with the new Bootstrap 5 syntax, ensuring that existing markup continues to work without immediate changes.

### Bootstrap jQuery support[​](#bootstrap-jquery-support "Direct link to Bootstrap jQuery support")

To ease the transition from Bootstrap 4 to Bootstrap 5, the backwards-compatibility layer maintains support for jQuery-dependent components. This allows developers to continue using existing jQuery-based plugins and custom code while gradually migrating to the new vanilla JavaScript approach introduced in Bootstrap 5.

The following examples illustrate how to use jQuery with Bootstrap 5 components:

```
$('[data-bs-toggle="tooltip"]').tooltip();
```

Or with event listeners:

```
$('#myTab a').on('shown.bs.tab',function(){
// do something...
});
```

### SCSS helpers and utilities[​](#scss-helpers-and-utilities "Direct link to SCSS helpers and utilities")

The compatibility layer includes a selection of SCSS helpers and utilities from Bootstrap 4. This provision enables developers to continue using familiar class names and mixins while they work on updating their custom styles to align with Bootstrap 5's new utility API system and class structure.

Some of the SCSS helpers and utilities available in the backwards-compatibility layer include:

- `.media` component
- Coloured badges using `.badge-success`, `badge-warning`, ... classes
- Inline forms using `.form-inline` class
- Spacing utilities like `.mr-1`, `.pl-2`, ...
- `.sr-only` and `.sr-only-focusable` classes
- Font utilities like `.font-weight-bold`, `.font-italic`, ...
- Custom controls in forms using `.custom-radio`, `.custom-switch`, ...

All these backwards-compatible SCSS helpers and utilities will be available until the final deprecation in Moodle 6.0. More details about the SCSS deprecation process can be found in [SCSS deprecation](https://moodledev.io/general/development/policies/deprecation/scss-deprecation).

### Bootstrap 4 old data attributes syntax silent replacement[​](#bootstrap-4-old-data-attributes-syntax-silent-replacement "Direct link to Bootstrap 4 old data attributes syntax silent replacement")

To minimize immediate breaking changes, the backwards-compatibility layer implements a silent replacement mechanism for Bootstrap 4's data attribute syntax.

As per Bootstrap's migration guide "*Data attributes for all JavaScript plugins are now namespaced to help distinguish Bootstrap functionality from third parties and your own code. For example, we use `data-bs-toggle` instead of `data-toggle`.*"

This feature can be used to translate old data attributes to their Bootstrap 5 equivalents, allowing existing markup to function without requiring immediate updates.

Example of bs4-compat silent replacement in amd module

```
import*asBS4compatfrom'theme_boost/bs4-compat';

[...]

// Init Bootstrap 4 compatibility giving an specific element to look into.
BS4compat.init(document.querySelector('[data-region="my-plugin-region"]'));

// Init Bootstrap 4 compatibility in the entire document.
BS4compat.init();
```

Example of bs4-compat silent replacement in a template

```
[...]

{{#js}}
// Init Bootstrap 4 compatibility in the entire document.
require(['theme_boost/bs4-compat'], function(BS4Compat) {
    BS4Compat.init();
});
{{/js}}
```

Example of bs4-compat silent replacement in a php file

```
$PAGE->requires->js_call_amd('theme_boost/bs4-compat','init');
```

This will replace for example `data-toggle="tooltip"` with `data-bs-toggle="tooltip"`, or `data-target="#collapsableContent"` with `data-bs-target="#collapsableContent"`.

warning

Dynamic generated content containing old data attributes syntax will not be replaced.