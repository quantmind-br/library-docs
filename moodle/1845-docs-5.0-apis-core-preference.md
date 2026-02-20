---
title: Preference API | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/apis/core/preference
source: sitemap
fetched_at: 2026-02-17T15:24:55.744489-03:00
rendered_js: false
word_count: 306
summary: This document explains the Preference API used for managing user-specific settings and data storage in both the database and session. It details core functions for setting, retrieving, and deleting preferences while outlining best practices for handling default values.
tags:
    - preference-api
    - user-settings
    - data-storage
    - php-api
    - session-management
    - moodle-development
category: api
---

The Preference API is used for the storage and retrieval of user preferences. These preferences are stored in the database for users with an account, however for guests or users who are not currently logged in the preferences are stored in the Session.

All of these functions operate on the current user by default, however you can specify the user you wish to operate on by passing a user ID or a moodle user object to the $user parameter. Normally this is used for state indicators, where it can be as simple as a yes or no, however you can also use it to store more complex user data, such as a serialized PHP object.

It is considered good practice to abstain from storing default values as a user preference as this creates a lot of redundancy. Instead you should apply the default value at the code level if there is no stored value for a given preference.

## Primary functions[​](#primary-functions "Direct link to Primary functions")

### get\_user\_preferences()[​](#get_user_preferences "Direct link to get_user_preferences()")

This function can be used to fetch the value of a requested (via $name) preference, or if it doesn't exist the value given in the $default parameter will be returned. If you do not specify a $name then all preferences will be returned.

```
get_user_preferences(
string$name=null,
mixed$default=null,
stdClass|int|null$user=null
):mixed;
```

### set\_user\_preference()[​](#set_user_preference "Direct link to set_user_preference()")

This function can be used to set the value of a preference named $name.

```
set_user_preference(
string$name,
mixed$value,
stdClass|int|null$user=null
):bool;
```

### set\_user\_preferences()[​](#set_user_preferences "Direct link to set_user_preferences()")

This function takes an array or preferences containing the name and value for each preference. For each element in the array this function passes the keys and values of each element as the $name and $value parameters (respectively) in calls to `set_user_preferences()`.

```
set_user_preferences(
array$preferences,
stdClass|int|null$user=null
):bool;
```

### unset\_user\_preference()[​](#unset_user_preference "Direct link to unset_user_preference()")

This deletes the requested preference, specified by the $name parameter.

```
unset_user_preference(
string$name,
stdClass|int|null$user=null
):bool;
```

## Example usage of the API[​](#example-usage-of-the-api "Direct link to Example usage of the API")

Set a preference and then retrieve it

```
set_user_preference('foo_nameformat','long');

// Returns the string - "long"
get_user_preferences('foo_nameformat');
```

Set another preference and then retrieve all preferences

```
set_user_preference('foo_showavatars','no');

// returns [
//     foo_nameformat  => "long",
//     foo_showavatars => "no",
// ];
get_user_preferences();
```

Add an array of preferences and change foo\_nameformat to short

```
$preferences=[
'foo_displaynum'=>'100',
'foo_nameformat'=>'short',
];

set_user_preferences($preferences);

// returns [
//     foo_nameformat  => "short",
//     foo_showavatars => "no",
//     foo_displaynum  => "100",
// ];
get_user_preferences();
```

Delete a preference

```
unset_user_preference('foo_showavatars');

// returns [
//     foo_nameformat  => "short",
//     foo_displaynum  => "yes",
// ];
get_user_preferences();
```