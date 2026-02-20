---
title: Shortlinks | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/apis/subsystems/routing/shortlinks
source: sitemap
fetched_at: 2026-02-17T15:37:15.662243-03:00
rendered_js: false
word_count: 272
summary: This document explains the implementation and generation of shortlinks in Moodle, covering URL structures, requirements, and the creation of custom handlers for public and private links.
tags:
    - moodle
    - shortlinks
    - routing
    - url-generation
    - api-development
category: api
---

Version: 5.1

Shortlinks are concise URLs that route to a fully-qualified URL in Moodle. Comprising of a smaller set of characters, their use is suitable for SMS, convenience, or where a longer URL would not be suitable.

## Requirements[​](#requirements "Direct link to Requirements")

Shortlinks require Moodle's routing system to be enabled and fully functioning as they have been fully integrated into the existing routing subsystem. Ensure routing is configured by following this [routing guide](https://docs.moodle.org/500/en/Configuring_the_Router).

## URL structure[​](#url-structure "Direct link to URL structure")

A shortlink URL will be comprised of the following:

- Base domain
- Route group of `s` or `p`
- Shortcode (e.g. `X8fG56aa`)

A complete shortlink will look something like this: `http://yourmoodle.com/s/X8fG56aa`.

## Short codes[​](#short-codes "Direct link to Short codes")

Short codes are unique identifiers at the end of a shortlink. The characters available for building short codes is limited to the extended alpha-numeric set (ALPHANUMEXT) with the the omission of ambiguous characters (i.e. upper case 'i' and lower case 'L').

## Generating shortlinks[​](#generating-shortlinks "Direct link to Generating shortlinks")

Before a shortlink can be used, a shortlink will need to be generated. Shortlink generation is random and length can be specified when calling the relevant method.

There are two types of shortlinks:

- Public shortlinks
- Private shortlinks

### Public[​](#public "Direct link to Public")

Public shortlinks can be accessed by anyone. Their use will be designated with a `/p/` in the URL.

```
$public=\core\di::get(\core\shortlink::class)->create_shortlink(
component:$component,
linktype:$linktype,
identifier:$identifier,
userid:0,
minlength:4,
maxlength:4,
);
```

### Private[​](#private "Direct link to Private")

Private shortlinks are tied to a specific user or set of users. Their use will be designated with a `/s/` in the URL.

```
$private=\core\di::get(\core\shortlink::class)->create_shortlink_for_users(
component:$component,
linktype:$linktype,
identifier:$identifier,
userids:$userids,
minlength:4,
maxlength:4,
);
```

## Using shortlinks[​](#using-shortlinks "Direct link to Using shortlinks")

Each component using shortlinks will need to have a `shortlink_handler` class. There are two methods that the implemented interface requires:

- `get_valid_linktypes()`
- `process_shortlink()`

```
classshortlink_handlerimplementsshortlink_handler_interface{
#[\Override]
publicfunctionget_valid_linktypes():array{
return[
'view',
];
}

#[\Override]
publicfunctionprocess_shortlink(
string$type,
string$identifier,
):?\core\url{
returnmatch($type){
'view'=>new\core\url('/mod/assign/view.php',[
'id'=>$identifier,
]),
default=>null,
};
}
}
```

Assuming the shortlink has been generated, the above example would allow a shortlink URL of `http://yourmoodle.com/s/SHORTCODE` to map to `http://yourmoodle.com/mod/assign/view.php?id=IDENTIFIER`

## See also[​](#see-also "Direct link to See also")

- [Routing](https://moodledev.io/docs/5.1/apis/subsystems/routing)