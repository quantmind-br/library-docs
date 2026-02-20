---
title: Bootstrap 5 migration | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/guides/bs5migration
source: sitemap
fetched_at: 2026-02-17T15:15:38.773311-03:00
rendered_js: false
word_count: 873
summary: This document outlines the multi-step process for migrating from Bootstrap 4 to Bootstrap 5, detailing specific CSS class changes, component refactors, and the implementation of a compatibility bridge. It provides developers with guidance on replacing deprecated features with version 5-compatible alternatives.
tags:
    - bootstrap-5
    - migration-guide
    - css-framework
    - moodle-development
    - scss-refactoring
    - frontend-development
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

- Badge colour class helpers `.badge-*` have been replaced with background utilities (use `.bg-primary` instead of `.badge-primary`) combined with the corresponding text colour classes (`.text-dark` or `.text-white`) to meet accessibility contrast.
- The `.badge-pill` class has been replaced with `.rounded-pill`

Don't

```
<spanclass="badge badge-danger badge-pill">Error badge</span>
```

Do

```
<spanclass="badge bg-danger text-white rounded-pill">Error badge</span>
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
<divclass="flex-grow-1 ml-3">
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