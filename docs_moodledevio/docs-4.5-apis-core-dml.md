---
title: Data manipulation API | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/apis/core/dml
source: sitemap
fetched_at: 2026-02-17T15:11:08.090458-03:00
rendered_js: false
word_count: 2451
summary: This document outlines the Moodle Data Manipulation API, explaining how to use the global $DB object to interact with the database in a secure and cross-platform compatible manner.
tags:
    - moodle-development
    - database-api
    - dml
    - sql-placeholders
    - php
    - data-retrieval
category: api
---

This page describes the functions available to access data in the Moodle database. You should **exclusively** use these functions in order to retrieve or modify database content because these functions provide a high level of abstraction and guarantee that your database manipulation will work against different RDBMSes.

Where possible, tricks and examples will be documented here in order to make developers' lives a bit easier. Of course, feel free to clarify, complete and add more information to this documentation. It will be welcome, absolutely!

## General concepts[​](#general-concepts "Direct link to General concepts")

### DB object[​](#db-object "Direct link to DB object")

- The data manipulation API is exposed via public methods of the `$DB` object.
- Moodle core takes care of setting up the connection to the database according to values specified in the main config.php file.
- The $DB global object is an instance of the `moodle_database` class. It is instantiated automatically during the bootstrap setup, i.e. as a part of including the main config.php file.
- The DB object is available in the global scope right after including the config.php file:

example.php

```
<?php
require(__DIR__.'/config.php');

// You can access the database via the $DB method calls here.
```

- To make the DB object available in your local scope, such as within a function:

example.php

```
<?php

functionmy_function_making_use_of_database(){
global$DB;

// You can access the database via the $DB method calls here.
}
```

### Table prefix[​](#table-prefix "Direct link to Table prefix")

- Most Moodle installations use a prefix for all the database tables, such as `mdl_`. This prefix is NOT to be used in the code itself.
- All the `$table` parameters in the functions are meant to be the table name without prefixes:

```
$user=$DB->get_record('user',['id'=>'1']);
```

- In custom SQL queries, table names must be enclosed between curly braces. They will be then automatically converted to the real prefixed table name. There is no need to access `$CFG->prefix`

```
$user=$DB->get_record_sql('SELECT COUNT(*) FROM {user} WHERE deleted = 1 OR suspended = 1;');
```

### Conditions[​](#conditions "Direct link to Conditions")

- All the `$conditions` parameters in the functions are arrays of `fieldname => fieldvalue` elements.
- They all must be fulfilled - that is the logical `AND` is used to populate the actual `WHERE` statement

```
$user=$DB->get_record('user',['firstname'=>'Martin','lastname'=>'Dougiamas']);
```

### Placeholders[​](#placeholders "Direct link to Placeholders")

- All the `$params` parameters in the functions are arrays of values used to fill placeholders in SQL statements.
- Placeholders help to avoid problems with SQL-injection and/or invalid quotes in SQL queries. They facilitate secure and cross-db compatible code.
- Two types of placeholders are supported - question marks (`SQL_PARAMS_QM`) and named placeholders (`SQL_PARAMS_NAMED`).
- Named params **must be unique** even if the value passed is the same. If you need to pass the same value multiple times, you need to have multiple distinct named parameters.

Example of using question-mark placeholders

```
$DB->get_record_sql(
'SELECT * FROM {user} WHERE firstname = ? AND lastname = ?',
[
'Martin',
'Dougiamas',
]
);
```

Example of using named placeholders

```
$DB->get_record_sql(
'SELECT * FROM {user} WHERE firstname = :firstname AND lastname = :lastname',
[
'firstname'=>'Martin',
'lastname'=>'Dougiamas',
]
);
```

### Strictness[​](#strictness "Direct link to Strictness")

Some methods accept the `$strictness` parameter affecting the method behaviour. Supported modes are specified using the constants:

- `MUST_EXIST` - In this mode, the requested record must exist and must be unique. An exception `dml_missing_record_exception` will be thrown if no record is found or `dml_multiple_records_exception` if multiple matching records are found.
- `IGNORE_MISSING` - In this mode, a missing record is not an error. False boolean is returned if the requested record is not found. If more records are found, a debugging message is displayed.
- `IGNORE_MULTIPLE` - This is not a recommended mode. The function will silently ignore multiple records found and will return just the first one of them.

## Getting a single record[​](#getting-a-single-record "Direct link to Getting a single record")

### get\_record[​](#get_record "Direct link to get_record")

Return a single database record as an object where all the given conditions are met.

```
publicfunctionget_record(
$table,
array$conditions,
$fields='*',
$strictness=IGNORE_MISSING
);
```

### get\_record\_select[​](#get_record_select "Direct link to get_record_select")

Return a single database record as an object where the given conditions are used in the WHERE clause.

```
publicfunctionget_record_select(
$table,
$select,
array$params=null,
$fields='*',
$strictness=IGNORE_MISSING
);
```

### get\_record\_sql[​](#get_record_sql "Direct link to get_record_sql")

Return a single database record as an object using a custom SELECT query.

```
publicfunctionget_record_sql(
$sql,
array$params=null,
$strictness=IGNORE_MISSING
);
```

## Getting a hashed array of records[​](#getting-a-hashed-array-of-records "Direct link to Getting a hashed array of records")

Each of the following methods return an array of objects. The array is indexed by the first column of the fields returned by the query. To assure consistency, it is a good practice to ensure that your query include an "id column" as the first field. When designing custom tables, make `id` their first column and primary key.

### get\_records[​](#get_records "Direct link to get_records")

Return a list of records as an array of objects where all the given conditions are met.

```
publicfunctionget_records(
$table,
array$conditions=null,
$sort='',
$fields='*',
$limitfrom=0,
$limitnum=0
);
```

### get\_records\_select[​](#get_records_select "Direct link to get_records_select")

Return a list of records as an array of objects where the given conditions are used in the WHERE clause.

```
publicfunctionget_records_select(
$table,
$select,
array$params=null,
$sort='',
$fields='*',
$limitfrom=0,
$limitnum=0
);
```

The `$fields` parameter is a comma separated list of fields to return (optional, by default all fields are returned).

### get\_records\_sql[​](#get_records_sql "Direct link to get_records_sql")

Return a list of records as an array of objects using a custom SELECT query.

```
publicfunctionget_records_sql(
$sql,
array$params=null,
$limitfrom=0,
$limitnum=0
);
```

### get\_records\_list[​](#get_records_list "Direct link to get_records_list")

Return a list of records as an array of objects where the given field matches one of the possible values.

```
publicfunctionget_records_list(
$table,
$field,
array$values,
$sort=*,
$fields='*',
$limitfrom=*,
$limitnum=''
)
```

## Getting data as key/value pairs in an associative array[​](#getting-data-as-keyvalue-pairs-in-an-associative-array "Direct link to Getting data as key/value pairs in an associative array")

Return the first two columns from a list of records as an associative array where all the given conditions are met.

```
publicfunctionget_records_menu(
$table,
array$conditions=null,
$sort='',
$fields='*',
$limitfrom=0,
$limitnum=0
);
```

Return the first two columns from a list of records as an associative array where the given conditions are used in the WHERE clause.

```
publicfunctionget_records_select_menu(
$table,
$select,
array$params=null,
$sort='',
$fields='*',
$limitfrom=0,
$limitnum=0
);
```

Return the first two columns from a number of records as an associative array using a custom SELECT query.

```
publicfunctionget_records_sql_menu(
$sql,
array$params=null,
$limitfrom=0,
$limitnum=0
);
```

## Counting records that match the given criteria[​](#counting-records-that-match-the-given-criteria "Direct link to Counting records that match the given criteria")

### count\_records[​](#count_records "Direct link to count_records")

Count the records in a table where all the given conditions are met.

```
publicfunctioncount_records(
$table,
array$conditions=null
);
```

### count\_records\_select[​](#count_records_select "Direct link to count_records_select")

Count the records in a table where the given conditions are used in the WHERE clause.

```
publicfunctioncount_records_select(
$table,
$select,
array$params=null,
$countitem="COUNT('x')"
);
```

### count\_records\_sql[​](#count_records_sql "Direct link to count_records_sql")

Counting the records using a custom SELECT COUNT(...) query.

```
publicfunctioncount_records_sql(
$sql,
array$params=null
);
```

## Checking if a given record exists[​](#checking-if-a-given-record-exists "Direct link to Checking if a given record exists")

### record\_exists[​](#record_exists "Direct link to record_exists")

Test whether a record exists in a table where all the given conditions are met.

```
publicfunctionrecord_exists(
$table,
array$conditions=null
);
```

### record\_exists\_select[​](#record_exists_select "Direct link to record_exists_select")

Test whether any records exists in a table where the given conditions are used in the WHERE clause.

```
publicfunctionrecord_exists_select(
$table,
$select,
array$params=null
);
```

### record\_exists\_sql[​](#record_exists_sql "Direct link to record_exists_sql")

Test whether the given SELECT query would return any record.

```
publicfunctionrecord_exists_sql(
$sql,
array$params=null
);
```

## Getting a particular field value from one record[​](#getting-a-particular-field-value-from-one-record "Direct link to Getting a particular field value from one record")

### get\_field[​](#get_field "Direct link to get_field")

Get a single field value from a table record where all the given conditions are met.

```
publicfunctionget_field(
$table,
$return,
array$conditions,
$strictness=IGNORE_MISSING
);
```

### get\_field\_select[​](#get_field_select "Direct link to get_field_select")

Get a single field value from a table record where the given conditions are used in the WHERE clause.

```
publicfunctionget_field_select(
$table,
$return,
$select,
array$params=null,
$strictness=IGNORE_MISSING
);
```

### get\_field\_sql[​](#get_field_sql "Direct link to get_field_sql")

Get a single field value (first field) using a custom SELECT query.

```
publicfunctionget_field_sql(
$sql,
array$params=null,
$strictness=IGNORE_MISSING
);
```

## Getting field values from multiple records[​](#getting-field-values-from-multiple-records "Direct link to Getting field values from multiple records")

### get\_fieldset[​](#get_fieldset "Direct link to get_fieldset")

Return values of the given field from a table record as an array where all the given conditions are met.

```
publicfunctionget_fieldset(
string$table,
string$return,
?array$conditions=null
);
```

### get\_fieldset\_select[​](#get_fieldset_select "Direct link to get_fieldset_select")

Return values of the given field as an array where the given conditions are used in the WHERE clause.

```
publicfunctionget_fieldset_select(
$table,
$return,
$select,
array$params=null
);
```

### get\_fieldset\_sql[​](#get_fieldset_sql "Direct link to get_fieldset_sql")

Return values of the first column as an array using a custom SELECT field FROM ... query.

```
publicfunctionget_fieldset_sql(
$sql,
array$params=null
);
```

## Setting a field value[​](#setting-a-field-value "Direct link to Setting a field value")

### set\_field[​](#set_field "Direct link to set_field")

Set a single field in every record where all the given conditions are met.

```
publicfunctionset_field(
$table,
$newfield,
$newvalue,
array$conditions=null
);
```

### set\_field\_select[​](#set_field_select "Direct link to set_field_select")

Set a single field in every table record where the given conditions are used in the WHERE clause.

```
publicfunctionset_field_select(
$table,
$newfield,
$newvalue,
$select,
array$params=null
);
```

## Deleting records[​](#deleting-records "Direct link to Deleting records")

### delete\_records[​](#delete_records "Direct link to delete_records")

Delete records from the table where all the given conditions are met.

```
publicfunctiondelete_records(
$table,
array$conditions=null
);
```

### delete\_records\_select[​](#delete_records_select "Direct link to delete_records_select")

Delete records from the table where the given conditions are used in the WHERE clause.

```
publicfunctiondelete_records_select(
$table,
$select,
array$params=null
);
```

## Inserting records[​](#inserting-records "Direct link to Inserting records")

### insert\_record[​](#insert_record "Direct link to insert_record")

Insert the given data object into the table and return the "id" of the newly created record.

```
publicfunctioninsert_record(
$table,
$dataobject,
$returnid=true,
$bulk=false
);
```

### insert\_records[​](#insert_records "Direct link to insert_records")

Insert multiple records into the table as fast as possible. Records are inserted in the given order, but the operation is not atomic. Use transactions if necessary.

```
publicfunctioninsert_records(
$table,
$dataobjects
);
```

### insert\_record\_raw[​](#insert_record_raw "Direct link to insert_record_raw")

For rare cases when you also need to specify the ID of the record to be inserted.

## Updating records[​](#updating-records "Direct link to Updating records")

### update\_record[​](#update_record "Direct link to update_record")

Update a record in the table. The data object must have the property "id" set.

```
publicfunctionupdate_record(
$table,
$dataobject,
$bulk=false
);
```

## Executing a custom query[​](#executing-a-custom-query "Direct link to Executing a custom query")

### execute[​](#execute "Direct link to execute")

- If you need to perform a complex update using arbitrary SQL, you can use the low level "execute" method. Only use this when no specialised method exists.

```
publicfunctionexecute(
$sql,
array$params=null
);
```

danger

Do NOT use this to make changes in database structure, use the `database_manager` methods instead.

## Using recordsets[​](#using-recordsets "Direct link to Using recordsets")

If the number of records to be retrieved from DB is high, the 'get\_records\_xxx() functions above are far from optimal, because they load all the records into the memory via the returned array. Under those circumstances, it is highly recommended to use these `get_recordset_xxx()` functions instead. They return an iterator to iterate over all the found records and save a lot of memory.

It is **absolutely important** to not forget to close the returned recordset iterator after using it. This is to free up a lot of resources in the RDBMS.

A general way to iterate over records using the `get_recordset_xxx()` functions:

```
$rs=$DB->get_recordset(....);
foreach($rsas$record){
// Do whatever you want with this record
}
$rs->close();
```

Unlike get\_record functions, you cannot check if `$rs = = true` or `!empty($rs)` to determine if any records were found. Instead, if you need to, you can use:

```
if($rs->valid()){
// The recordset contains some records.
}
```

### get\_recordset[​](#get_recordset "Direct link to get_recordset")

Return a list of records as a moodle\_recordset where all the given conditions are met.

```
publicfunctionget_recordset(
$table,
array$conditions=null,
$sort='',
$fields='*',
$limitfrom=0,
$limitnum=0
);
```

### get\_recordset\_select[​](#get_recordset_select "Direct link to get_recordset_select")

Return a list of records as a moodle\_recordset where the given conditions are used in the WHERE clause.

```
publicfunctionget_recordset_select(
$table,
$select,
array$params=null,
$sort='',
$fields='*',
$limitfrom=0,
$limitnum=0
);
```

### get\_recordset\_sql[​](#get_recordset_sql "Direct link to get_recordset_sql")

Return a list of records as a moodle\_recordset using a custom SELECT query.

```
publicfunctionget_recordset_sql(
$sql,
array$params=null,
$limitfrom=0,
$limitnum=0
);
```

### get\_recordset\_list[​](#get_recordset_list "Direct link to get_recordset_list")

Return a list of records as a moodle\_recordset where the given field matches one of the possible values.

```
publicfunctionget_recordset_list(
$table,
$field,
array$values,
$sort=*,
$fields='*',
$limitfrom=*,
$limitnum=''
);
```

## Delegated transactions[​](#delegated-transactions "Direct link to Delegated transactions")

- Please note some databases do not support transactions (such as the MyISAM MySQL database engine), however all server administrators are strongly encouraged to migrate to databases that support transactions (such as the InnoDB MySQL database engine).
- Previous versions supported only one level of transaction. Since Moodle 2.0, the DML layer emulates delegated transactions that allow nesting of transactions.
- Some subsystems (such as messaging) do not support transactions because it is not possible to rollback in external systems. A transaction is started by:

```
$transaction=$DB->start_delegated_transaction();
```

and finished by:

```
$transaction->allow_commit();
```

Usually a transaction is rolled back when an exception is thrown:

```
$transaction->rollback($ex);
```

which must be used very carefully because it might break compatibility with databases that do not support transactions. Transactions cannot be used as part of expected code flow; they can be used only as an emergency protection of data consistency.

::: More information

For more information see [DB layer 2.0 delegated transactions](https://docs.moodle.org/dev/DB_layer_2.0_delegated_transactions) or [MDL-20625](https://moodle.atlassian.net/browse/MDL-20625).

:::

### Example[​](#example "Direct link to Example")

```
global$DB;
try{
$transaction=$DB->start_delegated_transaction();
$DB->insert_record('foo',$object);
$DB->insert_record('bar',$otherobject);

// Assuming the both inserts work, we get to the following line.
$transaction->allow_commit();

}catch(Exception$e){
$transaction->rollback($e);
}
```

## Cross-DB compatibility[​](#cross-db-compatibility "Direct link to Cross-DB compatibility")

Moodle supports several SQL servers, including MySQL, MariaDB, PostgreSQL, MS-SQL and Oracle. These may have specific syntax in certain cases. In order to achieve cross-db compatibility of the code, the following functions must be used to generate the fragments of the query valid for the actual SQL server.

### sql\_bitand[​](#sql_bitand "Direct link to sql_bitand")

Return the SQL text to be used in order to perform a bitwise AND operation between 2 integers.

```
publicfunctionsql_bitand(
$int1,
$int2
);
```

### sql\_bitnot[​](#sql_bitnot "Direct link to sql_bitnot")

Return the SQL text to be used in order to perform a bitwise NOT operation on the given integer.

```
publicfunctionsql_bitnot(
$int1
);
```

### sql\_bitor[​](#sql_bitor "Direct link to sql_bitor")

Return the SQL text to be used in order to perform a bitwise OR operation between 2 integers.

```
publicfunctionsql_bitor(
$int1,
$int2
);
```

### sql\_bitxor[​](#sql_bitxor "Direct link to sql_bitxor")

Return the SQL text to be used in order to perform a bitwise XOR operation between 2 integers.

```
publicfunctionsql_bitxor(
$int1,
$int2
);
```

### sql\_null\_from\_clause[​](#sql_null_from_clause "Direct link to sql_null_from_clause")

Return an empty FROM clause required by some DBs in all SELECT statements.

```
publicfunctionsql_null_from_clause()
```

### sql\_ceil[​](#sql_ceil "Direct link to sql_ceil")

Return the correct CEIL expression applied to the given fieldname.

```
publicfunctionsql_ceil(
$fieldname
);
```

### sql\_equal[​](#sql_equal "Direct link to sql_equal")

Return the query fragment to perform cross-db varchar comparisons when case-sensitiveness is important.

```
publicfunctionsql_equal(
$fieldname,
$param,
$casesensitive=true,
$accentsensitive=true,
$notequal=false
);
```

### sql\_like[​](#sql_like "Direct link to sql_like")

Return the query fragment to perform the LIKE comparison.

```
$DB->sql_like(
$fieldname,
$param,
$casesensitive=true,
$accentsensitive=true,
$notlike=false,
$escapechar=' \\ '
);
```

Example: Searching for records partially matching the given hard-coded literal

```
$likeidnumber=$DB->sql_like('idnumber',':idnum');
$DB->get_records_sql(
"SELECT id, fullname FROM {course} WHERE {$likeidnumber}",
[
'idnum'=>'DEMO-%',
]
);
```

See below if you need to compare with a value submitted by the user.

### sql\_like\_escape[​](#sql_like_escape "Direct link to sql_like_escape")

Escape the value submitted by the user so that it can be used for partial comparison and the special characters like '\_' or '%' behave as literal characters, not wildcards.

```
$DB->sql_like_escape(
$text,
$escapechar='\\'
);
```

Example: If you need to perform a partial comparison with a value that has been submitted by the user

```
$search=required_param('search',PARAM_RAW);

$likefullname=$DB->sql_like('fullname',':fullname');
$DB->get_records_sql(
"SELECT id, fullname FROM {course} WHERE {$likefullname}",
[
'fullname'=>'%'.$DB->sql_like_escape($search).'%',
]
);
```

### sql\_length[​](#sql_length "Direct link to sql_length")

Return the query fragment to be used to calculate the length of the expression in characters.

```
publicfunctionsql_length(
$fieldname
);
```

### sql\_modulo[​](#sql_modulo "Direct link to sql_modulo")

Return the query fragment to be used to calculate the remainder after division.

```
publicfunctionsql_modulo(
$int1,
$int2
);
```

### sql\_position[​](#sql_position "Direct link to sql_position")

Return the query fragment for searching a string for the location of a substring. If both needle and haystack use placeholders, you must use named placeholders.

```
publicfunctionsql_position(
$needle,
$haystack
);
```

### sql\_substr[​](#sql_substr "Direct link to sql_substr")

Return the query fragment for extracting a substring from the given expression.

```
publicfunctionsql_substr(
$expr,
$start,
$length=false
);
```

### sql\_cast\_char2int[​](#sql_cast_char2int "Direct link to sql_cast_char2int")

Return the query fragment to cast a CHAR column to INTEGER

```
publicfunctionsql_cast_char2int(
$fieldname,
$text=false
);
```

### sql\_cast\_char2real[​](#sql_cast_char2real "Direct link to sql_cast_char2real")

Return the query fragment to cast a CHAR column to REAL (float) number

```
publicfunctionsql_cast_char2real(
$fieldname,
$text=false
);
```

### sql\_cast\_to\_char[​](#sql_cast_to_char "Direct link to sql_cast_to_char")

Return SQL for casting to char of given field/expression.

```
publicfunctionsql_cast_to_char(string$field);
```

### sql\_compare\_text[​](#sql_compare_text "Direct link to sql_compare_text")

Return the query fragment to be used when comparing a TEXT (clob) column with a given string or a VARCHAR field (some RDBMs do not allow for direct comparison).

```
publicfunctionsql_compare_text(
$fieldname,
$numchars=32
);
```

Example

```
$comparedescription=$DB->sql_compare_text('description');
$comparedescriptionplaceholder=$DB->sql_compare_text(':description');
$todogroups=$DB->get_records_sql(
"SELECT id FROM {group} WHERE {$comparedescription} = {$comparedescriptionplaceholder}",
[
'description'=>'TODO',
]
);
```

### sql\_order\_by\_text[​](#sql_order_by_text "Direct link to sql_order_by_text")

Return the query fragment to be used to get records ordered by a TEXT (clob) column. Note this affects the performance badly and should be avoided if possible.

```
publicfunctionsql_order_by_text(
$fieldname,
$numchars=32
);
```

### sql\_order\_by\_null[​](#sql_order_by_null "Direct link to sql_order_by_null")

Return the query fragment to be used to get records with a standardised return pattern of null values across database types to sort nulls first when ascending and last when descending.

```
publicfunctionsql_order_by_null(
string$fieldname,
int$sort=SORT_ASC
);
```

### sql\_concat[​](#sql_concat "Direct link to sql_concat")

Return the query fragment to concatenate all given parameters into one string.

```
publicfunctionsql_concat(...)
```

There is a gotcha if you are trying to concat fields which may be null which result in the entire result being null:

An example of incorrect behaviour

```
publicfunctionsql_concat('requiredfield','optionalfield');
```

You must cast or coalesce every nullable argument, for example:

An example of correct behaviour

```
publicfunctionsql_concat('requiredfield',"COALESCE(optionalfield, '')");
```

### sql\_group\_concat[​](#sql_group_concat "Direct link to sql_group_concat")

Return SQL for performing group concatenation on given field/expression.

```
publicfunctionsql_group_concat(string$field,string$separator=', ',string$sort='')
```

### sql\_concat\_join[​](#sql_concat_join "Direct link to sql_concat_join")

Return the query fragment to concatenate all given elements into one string using the given separator.

```
publicfunctionsql_concat_join(
$separator="' '",
$elements=[]]
);
```

### sql\_fullname[​](#sql_fullname "Direct link to sql_fullname")

Return the query fragment to concatenate the given $firstname and $lastname

```
publicfunctionsql_fullname(
$first='firstname',
$last='lastname'
);
```

### sql\_isempty[​](#sql_isempty "Direct link to sql_isempty")

Return the query fragment to check if the field is empty

```
publicfunctionsql_isempty(
$tablename,
$fieldname,
$nullablefield,
$textfield
);
```

### sql\_isnotempty[​](#sql_isnotempty "Direct link to sql_isnotempty")

Return the query fragment to check if the field is not empty

```
publicfunctionsql_isnotempty(
$tablename,
$fieldname,
$nullablefield,
$textfield
);
```

### get\_in\_or\_equal[​](#get_in_or_equal "Direct link to get_in_or_equal")

Return the query fragment to check if a value is IN the given list of items (with a fallback to plain equal comparison if there is just one item)

```
publicfunctionget_in_or_equal(
$items,
$type=SQL_PARAMS_QM,
$prefix='param',
$equal=true,
$onemptyitems=false
);
```

Example:

```
$statuses=['todo','open','inprogress','intesting'];
[$insql,$inparams]=$DB->get_in_or_equal($statuses);
$sql="SELECT * FROM {bugtracker_issues} WHERE status $insql";
$bugs=$DB->get_records_sql($sql,$inparams);
```

An example using named params:

```
[$insql,$params]=$DB->get_in_or_equal($contexts,SQL_PARAMS_NAMED,'ctx');
$contextsql="AND rc.contextid {$insql}";
```

### sql\_regex\_supported[​](#sql_regex_supported "Direct link to sql_regex_supported")

Does the current database driver support regex syntax when searching?

```
publicfunctionsql_regex_supported()
```

### sql\_regex[​](#sql_regex "Direct link to sql_regex")

Return the query fragment to perform a regex search.

```
publicfunctionsql_regex(
$positivematch=true,
$casesensitive=false
);
```

Example: Searching for Page module instances containing links.

Example: Searching for Page module instances containing links.

```
if($DB->sql_regex_supported()){
$select='content '.$DB->sql_regex().' :pattern';
$params=['pattern'=>"(src|data)\ * = \ *[\\\"\']https?://"]
}else{
$select=$DB->sql_like('content',':pattern',false);
$params=['pattern'=>'% = %http%://%'];
}

$pages=$DB->get_records_select('page',$select,$params,'course','id, course, name');
```

### sql\_regex\_get\_word\_beginning\_boundary\_marker[​](#sql_regex_get_word_beginning_boundary_marker "Direct link to sql_regex_get_word_beginning_boundary_marker")

Return the word-beginning boundary marker if the current database driver supports regex syntax when searching.

Defaults to `[[:<:]]`. On MySQL `v8.0.4+`, it returns `\\b`.

```
publicfunctionsql_regex_get_word_beginning_boundary_marker()
```

### sql\_regex\_get\_word\_end\_boundary\_marker[​](#sql_regex_get_word_end_boundary_marker "Direct link to sql_regex_get_word_end_boundary_marker")

Return the word-end boundary marker if the current database driver supports regex syntax when searching.

Defaults to `[[:>:]]`. On MySQL `v8.0.4+`, it returns `\\b`.

```
publicfunctionsql_regex_get_word_end_boundary_marker()
```

### sql\_intersect[​](#sql_intersect "Direct link to sql_intersect")

Return the query fragment that allows to find intersection of two or more queries

```
publicfunctionsql_intersect(
$selects,
$fields
);
```

## Debugging[​](#debugging "Direct link to Debugging")

### set\_debug[​](#set_debug "Direct link to set_debug")

You can enable a debugging mode to make $DB output the SQL of every executed query, along with some timing information. This can be useful when debugging your code. Obviously, all such calls should be removed before code is submitted for integration.

```
publicfunctionset_debug(bool$state)
```

## Special cases[​](#special-cases "Direct link to Special cases")

### get\_course[​](#get_course "Direct link to get_course")

From Moodle 2.5.1 onwards, you should use the `get_course` function instead of using `get_record('course', ...)` if you want to get a course record based on its ID, especially if there is a significant possibility that the course being retrieved is either the current course for the page, or the site course. Those two course records have probably already been loaded, and using this function will save a database query.

Additionally, the code is shorter and easier to read.

### get\_courses[​](#get_courses "Direct link to get_courses")

If you want to get all the current courses in your Moodle, use get\_courses() without parameter:

```
$courses=get_courses();
```

## See also[​](#see-also "Direct link to See also")

- [SQL coding style](https://moodledev.io/general/development/policies/codingstyle/sql)
- [Core APIs](https://moodledev.io/docs/4.5/apis/core)
- [DML exceptions](https://moodledev.io/docs/4.5/apis/core/dml/exceptions): New DML code is throwing exceptions instead of returning false if anything goes wrong
- [DML drivers](https://moodledev.io/docs/4.5/apis/core/dml/drivers): Database drivers for new DML layer
- [DDL functions](https://moodledev.io/docs/4.5/apis/core/dml/ddl): Where all the functions used to handle DB objects ([DDL](https://en.wikipedia.org/wiki/Data_Definition_Language)) are defined.