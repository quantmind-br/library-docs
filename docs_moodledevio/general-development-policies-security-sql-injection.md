---
title: SQL injection | Moodle Developer Resources
url: https://moodledev.io/general/development/policies/security/sql-injection
source: sitemap
fetched_at: 2026-02-17T15:59:51.052604-03:00
rendered_js: false
word_count: 370
summary: This document explains the risks of SQL injection in Moodle and outlines the best practices for developers to prevent vulnerabilities using placeholders and parameter cleaning.
tags:
    - sql-injection
    - security
    - database-security
    - moodle-development
    - coding-standards
    - data-cleaning
category: guide
---

## What is the danger?[​](#what-is-the-danger "Direct link to What is the danger?")

Suppose your code in `/course/view.php?id=123` does something like:

```
SELECTFROM mdl_course WHERE id = $id;
```

where the `$id = 123` has come from the URL. Suppose that your code does not bother to clean that parameter properly.

Along comes Evil Hacker, and edits the URL to be `/course/view.php?id=123;DELETE+FROM+mdl_user` I will let you work out why that is a very, very bad thing.

Of course, depending on exactly what the database query is, the malicious input needs to be constructed appropriately, but that is just a matter of trial and error for Evil Hacker.

## How Moodle avoids this problem[​](#how-moodle-avoids-this-problem "Direct link to How Moodle avoids this problem")

Once again, it is a case of being very suspicious of any input that came from outside Moodle. In the example above, `$id` should clearly have been cleaned by passing `PARAM_INT` to `required_param`.

It is more tricky with a query like

```
UPDATE mdl_user SET lastname ='$lastname'WHERE id = $id;
```

What happens when `$lastname` is `O'Brian`? Well, you have to escape the ' like this: `O\\'Brian`.

- In Moodle 1.9, `addslashes` is applied automatically to all input you get via `required_param` or `optional_param`.
- Moodle 2.0 onwards, completely avoid the dangerous process of building SQL by concatenating strings. In Moodle 2.0 the SQL would look like

```
UPDATE mdl_user SET lastname = ? WHERE id = ?;
```

and then we would pass an array of values `[$lastname, $id]` to the database along with the SQL.

## What you need to do in your code[​](#what-you-need-to-do-in-your-code "Direct link to What you need to do in your code")

- Use higher level `dmllib` methods, like `get_record`, whenever possible, so you do not have to create SQL yourself.
- When you have to insert values into SQL statements, **use place-holders** to insert the values safely.
- Test your code by using a tool like [sqlmap](https://sqlmap.org/), or by manually trying tricky inputs like:  
  `< > & \&lt; \&gt; \&amp; ' \\' 碁 \ \\`

In Moodle 1.9 or earlier:

- Data from `required_param` and `optional_param` have already had `addslashes` applied, ready to be used in database queries, but make sure you put single quotes round each value.
- If you have loaded some data from the database, and then want to re-insert it, then apply `addslashes` or `addslashes_object` to it first.

## What you need to do as an administrator[​](#what-you-need-to-do-as-an-administrator "Direct link to What you need to do as an administrator")

- This is not something that administrators can do anything about (other than keeping your Moodle up-to-date).

## See also[​](#see-also "Direct link to See also")

- [Security](https://moodledev.io/general/development/policies/security)
- [Coding](https://moodledev.io/general/development/policies)
- [https://sqlmap.org](https://sqlmap.org) - A tool for automatically finding SQL injection vulnerabilities.