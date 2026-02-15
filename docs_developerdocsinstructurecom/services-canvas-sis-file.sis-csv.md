---
title: SIS CSV Format | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/sis/file.sis_csv
source: sitemap
fetched_at: 2026-02-15T09:11:17.410507-03:00
rendered_js: false
word_count: 4257
summary: This document provides technical specifications and procedures for importing data from Student Information Services (SIS) into Canvas via CSV files. It details formatting rules, batch update modes, and diffing strategies to maintain data integrity between systems.
tags:
    - sis-import
    - canvas-lms
    - csv-formatting
    - data-integration
    - batch-processing
    - diffing-mode
category: reference
---

## SIS Import Format Documentation

Instructure Canvas can integrate with an institution's Student Information Services (SIS) in several ways. The simplest way involves providing Canvas with several CSV files describing users, courses, and enrollments. These files can be zipped together and uploaded to the Account admin area.

Standard CSV rules apply:

- The first row will be interpreted as a header defining the ordering of your columns. This header row is mandatory.
- Fields that contain a comma must be surrounded by double-quotes.
- Fields that contain double-quotes must also be surrounded by double-quotes, with the internal double-quotes doubled. Example: Chevy "The Man" Chase would be included in the CSV as "Chevy ""The Man"" Chase".

All text should be UTF-8 encoded.

All timestamps are sent and returned in ISO 8601 format. All timestamps default to UTC time zone unless specified.

If the option to do a "full batch update" is selected in the UI, then this SIS upload is considered to be the new canonical set of data, and data from previous SIS imports that isn't present in this import will be deleted. This can be useful if the source SIS software doesn't have a way to send delete records as part of the import. This deletion is scoped to a single term, which must be specified when uploading the SIS import. Use this option with caution, as it can delete large data sets without any prompting on the individual records. Currently, this affects courses, sections and enrollments.

This option will only affect data that has been involved in a previous SIS job -- either created by a previous import, or referenced by a SIS job after a SIS ID was manually added. Manually created courses with no SIS ID, for example, won't be deleted even if they don't appear in the new SIS import.

During a term batch mode may be used often and if a partial file is sent, many objects can become deleted. Using `change_threshold=5` will only delete objects if the number of objects to delete is less than 5% of the objects for the term. For example: If change\_threshold set to 5 and the term has 100 courses, and batch\_mode would delete more than 5 of the courses the batch will abort before the courses are deleted. The change\_threshold can be set to any integer between 1 and 100.

change\_threshold also impacts diffing mode.

Multi term batch mode is just like batch mode except against multiple terms. Multi term batch mode is run against all terms included in the same import for the batch. To use multi term batch mode you must also set a change\_threshold. If you intend to remove all items with multi term batch mode, you can set the change\_threshold to 100.

If your account has a SIS integration that is sending its entire data set on each import, rather than just sending what has changed, you can speed up the import process by enabling diffing mode. In diffing mode, a preprocessing step in Canvas will compare the current SIS import against the last successful SIS import with the same *data set identifier*, and only apply the difference between the two imports.

For instance, If user A is created by import 1, and then the name is changed for user A on import 2, Canvas will apply the new information for user A.

If user B is created by import 1, and then user B is omitted from import 2, Canvas will mark the user as deleted.

If user C is created by import 1, and the exact same information is specified for user C in import 2, Canvas will mark that nothing has changed for that CSV row and skip looking up user C entirely. This can greatly speed up SIS imports with thousands of rows that change rarely.

It is important to note that if any SIS data was changed outside of that previous CSV import, the changes will not be noticed by the diffing code. For example:

1. Import 1 sets user A state to "active".
2. An admin sets user A state to "deleted" either through the Canvas UI, or a non-diff SIS import.
3. Import 2 sets user A state to "active" again, and is configured to diff against Import 1.
4. Because only the difference between Import 1 and Import 2 is applied, and the user's state is "active" in both CSVs, the user remains deleted.

Diffing mode is enabled by passing the `diffing_data_set_identifier` option in the "Import SIS Data" API call. This is a unique, non-changing string identifier for the series of SIS imports that will be diffed against one another. The string can contain any valid UTF-8, and be up to 128 bytes in length. If an account has multiple SIS integrations that want to take advantage of diffing, each integration can select a unique data set identifier to avoid interfering with each other.

When choosing a data set identifier, it's important to include any relevant details to differentiate this data set from other import data sets that may come concurrently or later. This might include things such as source system, data type, and term id. Some examples of good identifiers:

- source-system-1:all-data:spring-2016

Diffing mode by default marks objects as "deleted" when they are not included for an import, but enrollments can be marked as 'completed' or 'inactive' if the `diffing_drop_status` is passed. Likewise users removed between diffed batches can be marked as 'suspended' if the `diffing_user_remove_status` is set to `suspended`. If you prefer to leave removed objects alone in diffed imports, pass `skip_deletes=true` instead of either of these (this will apply to all object types, not just users and enrollments).

If changes are made to SIS-managed objects outside of the normal import process, as in the example given above, it may be necessary to process a SIS import with the same data set identifier, but apply the entire import rather than applying just the diff. To enable this mode, set the `diffing_remaster_data_set=true` option when creating the import, and it will be applied without diffing. The next import for the same data set will still diff against that import.

If using automated systems and diffing and there is an issue where the system sends a partial or an empty file, diffing would see that all users not included should be removed. Using `change_threshold=10` will then not perform diffing if the files being compared are greater than 10% different. The threshold can be set to help prevent removing objects unintentionally. When set and the file is over 10% different, the entire import file will be applied instead of diffing against a previous batch and this batch will not be used for diffing any future batches. The change\_threshold can be set to any integer between 1 and 100.

If five consecutive SIS batches with the same diffing data set identifier exceed the change threshold, future imports will fail. You will be required to perform a remaster using the `diffing_remaster_data_set=true` option to resume imports with that data set identifier.

change\_threshold also impacts batch mode.

When a user makes a change to imported data in Canvas (e.g., changes a name), this change is "sticky" and is set as the new default. By default, these "sticky" changes are not overwritten on the next SIS import. This can be overridden by selecting the Override UI option, which allows Canvas to overwrite any "sticky" data updated in the Canvas UI. Otherwise, changes from an import with conflicting data would be disregarded and the existing user data would not be changed. See below for an indication of which fields have this "sticky" property

A unique identifier used to reference users in the enrollments table. This identifier must not change for the user, and must be globally unique. In the user interface, this is called the SIS ID.

A secondary unique identifier useful for more complex SIS integrations. This identifier must not change for the user, and must be globally unique.

The name that a user will use to login to Instructure. If you have an authentication service configured (like LDAP), this will be their username from the remote system.

If the account is configured to use LDAP or an SSO protocol then this should not be set. Otherwise this is the password that will be used to login to Canvas along with the 'login\_id' above.

Setting the password will in most cases log the user out of Canvas. The password can only be set one time. If the password has been set by the user or a previous sis import, it will not be changed.

Instead of a plain-text password, you can pass a pre-hashed password using the SSHA password generation scheme in this field. While better than passing a plain text password, you should still encourage users to change their password after logging in for the first time.

authentication\_provider\_id

The authentication provider this login is associated with. Logins associated with a specific provider can only be used with that provider. Legacy providers (LDAP, CAS, SAML) will search for logins associated with them, or unassociated logins. New providers will only search for logins explicitly associated with them. This can be the integer ID of the provider, or the type of the provider (in which case, it will find the first matching provider).

Given name of the user. If present, used to construct full\_name and/or sortable\_name.

Last name of the user. If present, used to construct full\_name and/or sortable\_name.

Full name of the user. Omit first\_name and last\_name if this is provided.

Sortable name of the user. This is normally inferred from the user's name, but you can customize it here.

Display name of the user. This is normally inferred from the user's name, but you can customize it here.

The email address of the user. This might be the same as login\_id but would be used to set email for user and will tie the email to the login. It is recommended to omit this field over using fake email addresses for testing.

User's preferred pronouns. Can pass "&lt;delete&gt;" to remove the pronoun from the user. This column will be ignored unless the "Enable Personal Pronouns" account setting is enabled.

User's declared user type. Can be either administrative, observer, staff, student, student\_other, or teacher. Can pass "&lt;delete&gt;" to remove the declared user type from the user.

canvas\_password\_notification

Defaults to false. When true, user is notified for password setup if the authentication\_provider\_id is "canvas"

Setting this to true will create a new user in the target account for the SIS import and merge in another existing user from another account within the consortium with a matching integration\_id. Will be ignored unless the target account is associated with an auto-merge consortium.

active, suspended, deleted

At least one form of name should be supplied. If a user is being created and no name is given, the login\_id will be used as the name.

When a user is 'deleted' it will delete the login tied to the sis\_id. If the login is the last one, all of the users enrollments will also be deleted and they won't be able to log in to the school's account. If you still want the student to be able to log in but just not participate, leave the student 'active' but set the enrollments to 'completed'. If you want to leave a student's enrollments intact, but not allow them to login, use the 'suspended' status.

Sample:

```
user_id,login_id,authentication_provider_id,password,first_name,last_name,short_name,email,status
01103,bsmith01,,,Bob,Smith,Bobby Smith,bob.smith@myschool.edu,active
13834,jdoe03,google,,John,Doe,,john.doe@myschool.edu,active
13aa3,psue01,7,,Peggy,Sue,,peggy.sue@myschool.edu,active
```

A unique identifier used to reference accounts in the enrollments data. This identifier must not change for the account, and must be globally unique. In the user interface, this is called the SIS ID.

The account identifier of the parent account. If this is blank the parent account will be the root account. Note that even if all values are blank, the column must be included to differentiate the file from a group import.

Sets the integration\_id of the account

Any account that will have child accounts must be listed in the csv before any child account references it.

Sample:

```
account_id,parent_account_id,name,status
A001,,Humanities,active
A002,A001,English,active
A003,A001,Spanish,active
```

A unique identifier used to reference terms in the enrollments data. This identifier must not change for the account, and must be globally unique. In the user interface, this is called the SIS ID.

Sets the integration\_id of the term

date\_override\_enrollment\_type

When set, all columns except term\_id, status, start\_date, and end\_date will be ignored for this row. Can only be used for an existing term. If status is active, the term dates will be set to apply only to enrollments of the given type. If status is deleted, the currently set dates for the given enrollment type will be removed. Must be one of StudentEnrollment, TeacherEnrollment, TaEnrollment, or DesignerEnrollment.

The date the term starts. The format should be in ISO 8601: YYYY-MM-DDTHH:MM:SSZ. Will be cleared if empty.

The date the term ends. The format should be in ISO 8601: YYYY-MM-DDTHH:MM:SSZ. Will be cleared if empty.

Sample:

```
term_id,name,status,start_date,end_date
T001,Winter2011,active,,
T002,Spring2011,active,2013-1-03 00:00:00,2013-05-03 00:00:00-06:00
T003,Fall2011,active,,
```

A unique identifier used to reference courses in the enrollments data. This identifier must not change for the account, and must be globally unique. In the user interface, this is called the SIS ID.

A short name for the course

A long name for the course. (This can be the same as the short name, but if both are available, it will provide a better user experience to provide both.)

The account identifier from accounts.csv. New courses will be attached to the root account if not specified here

The term identifier from terms.csv, if no term\_id is specified the default term for the account will be used

The status of the course, also known as the workflow\_state. Allowed values are active, deleted, completed, or published.

Sets the integration\_id of the course

The course start date. The format should be in ISO 8601: YYYY-MM-DDTHH:MM:SSZ. To remove the start date pass "&lt;delete&gt;". Will keep any existing value if empty.

The course end date. The format should be in ISO 8601: YYYY-MM-DDTHH:MM:SSZ. To remove the end date pass "&lt;delete&gt;" Will keep any existing value if empty.

on\_campus, online, blended

The SIS id of a pre-existing Blueprint course. When provided, the current course will be set up to receive updates from the blueprint course. Requires Blueprint Courses feature. To remove the Blueprint Course link you can pass 'dissociate' in place of the id.

Whether the course is a homeroom course. Requires the courses to be associated with a "Canvas for Elementary"-enabled account.

Friendly name for course, will be shown only for the Elementary account

If the start\_date is set, it will override the term start date. If the end\_date is set, it will override the term end date.

To view the current status of a course that has already been imported into Canvas, please fetch the course data using the [get a single course](https://developerdocs.instructure.com/services/canvas/resources/courses#method.courses.show) API endpoint and refer to the workflow\_state value returned in the [Course](https://developerdocs.instructure.com/services/canvas/resources/courses#Course) object.

Sample:

```
course_id,short_name,long_name,account_id,term_id,status
E411208,ENG115,English 115: Intro to English,A002,,active
R001104,BIO300,"Biology 300: Rocking it, Bio Style",A004,Fall2011,active
A110035,ART105,"Art 105: ""Art as a Medium""",A001,,active
```

A unique identifier used to reference sections in the enrollments data. This identifier must not change for the section, and must be globally unique. In the user interface, this is called the SIS ID.

The course identifier from courses.csv

Sets the integration\_id of the section

The section start date. The format should be in ISO 8601: YYYY-MM-DDTHH:MM:SSZ. Will be cleared if empty.

The section end date The format should be in ISO 8601: YYYY-MM-DDTHH:MM:SSZ. Will be cleared if empty.

If the start\_date is set, it will override the course and term start dates. If the end\_date is set, it will override the course and term end dates.

Sample:

```
section_id,course_id,name,status,start_date,end_date
S001,E411208,Section 1,active,,
S002,E411208,Section 2,active,,
S003,R001104,Section 1,active,,
```

The course identifier from courses.csv

The domain of the account to search for the user.

The enrollment start date. For start\_date to take effect the end\_date also needs to be populated. The format should be in ISO 8601: YYYY-MM-DDTHH:MM:SSZ. Will be cleared if empty.

The enrollment end date. For end\_date to take effect the start\_date also needs to be populated. The format should be in ISO 8601: YYYY-MM-DDTHH:MM:SSZ. Will be cleared if empty.

The User identifier from users.csv, required to identify user. If the user\_integration\_id is present, this field will be ignored.

The integration\_id of the user from users.csv required to identify user if the user\_id is not present.

student, teacher, ta, observer, designer, or a custom role defined by the account. When using a custom role, the name is case sensitive.

Uses a role id, either built-in or defined by the account

The section identifier from sections.csv, if none is specified the default section for the course will be used

active, deleted, completed, inactive, deleted\_last\_completed\**

For observers, the user identifier from users.csv of a student in the same course that this observer should be able to see grades for. Ignored for any role other than observer

Defaults to false. When true, the enrollment will only allow the user to see and interact with users enrolled in the section given by course\_section\_id.

If true, a notification will be sent to the enrolled user. Notifications are not sent by default.

temporary\_enrollment\_source\_user\_id

The User identifier from users.csv of a provider in a temporary enrollment. If included, the created enrollment is a temporary enrollment. *Requires Temporary Enrollments feature option.*

\* course\_id or section\_id is required, role or role\_id is required, and user\_id or user\_integration\_id is required.

\** deleted\_last\_completed is not a state, but it combines the deleted and completed states in a function that will delete an enrollment from a course if there are at least one other active enrollment in the course. If it is the last enrollment in the course it will complete it. This may be useful for when a user moves to a different section of a course in which there are section specific assignments. It offloads the logic required to determine if the enrollment is the users last enrollment in the given course or not.

When an enrollment is in a 'completed' state the student is limited to read-only access to the course.

If in an 'inactive' state, the student will be listed in the course roster for teachers, but will not be able to view or participate in the course until the enrollment is activated.

Sample:

```
course_id,user_id,role,section_id,status
E411208,01103,student,1B,active
E411208,13834,student,2A,active
E411208,13aa3,teacher,2A,active
```

A unique identifier used to reference a group category. This identifier must not change for the group category, and must be globally unique.

The account identifier from accounts.csv, if no account or course is specified the group will be attached to the root account.

The course identifier from courses.csv, if no course or account is specified the group will be attached to the root account.

The name of the group category.

Sample:

```
group_category_id,account_id,course_id,category_name,status
GC08,A001,,First Group Category,active
GC07,,,GC7,active
GC10,,,GC10,deleted
```

A unique identifier used to reference groups in the group\_users data. This identifier must not change for the group, and must be globally unique.

The group category identifier from group\_categories.csv, if none is specified the group will be put in the default group category for the account or course or root\_account if there is no course\_id or account\_id.

The account identifier from accounts.csv, if none is specified the group will be attached to the root account.

The course identifier from courses.csv, if none is specified the group will be attached to the root account.

Sample:

```
group_id,account_id,name,status
G411208,A001,Group1,available
G411208,,Group2,available
G411208,,Group3,deleted
```

The group identifier from groups.csv

The user identifier from users.csv

Sample:

```
group_id,user_id,status
G411208,U001,accepted
G411208,U002,accepted
G411208,U003,deleted
```

### differentiation\_tag\_sets.csv

A unique identifier used to reference a differentiation tag set. This identifier must not change for the tag set, and must be globally unique.

The course identifier from courses.csv the tag set will be attached to.

The name of the differentiation tag set.

Sample:

```
tag_set_id,course_id,set_name,status
TS08,C001,First Tag Set,active
TS07,C001,TS7,active
TS10,C001,TS10,deleted
```

A unique identifier used to reference a differentiation tag. This identifier must not change for the tag, and must be globally unique.

The differentiation tag set identifier from differentiation\_tag\_sets.csv, if none is specified the tag will be created as a single tag.

The course identifier from courses.csv the tag will be created in.

The name of the differentiation tag.

\* tag\_set\_id or course\_id is required for new tags.

Sample:

```
tag_id,tag_set_id,course_id,name,status
T01,TS08,,Tag1,available
T02,,C001,Tag2,available
T03,,C001,Tag3,deleted
```

### differentiation\_tag\_membership.csv

The differentiation tag identifier from differentiation\_tags.csv

The user identifier from users.csv

Sample:

```
tag_id,user_id,status
T01,U001,accepted
T02,U002,accepted
T03,U003,deleted
```

The course identifier from courses.csv

The section identifier from sections.csv

xlists.csv is optional. The goal of xlists.csv is to provide a way to add cross-listing information to an existing course and section hierarchy. Section ids are expected to exist already and already reference other course ids. If a section id is provided in this file, it will be moved from its existing course id to a new course id, such that if that new course is removed or the cross-listing is removed, the section will revert to its previous course id. If xlist\_course\_id does not reference an existing course, it will be created. If you want to provide more information about the cross-listed course, please do so in courses.csv.

While the xlists.csv does not have any sticky fields, the sections.csv does have course\_id as a sticky field. If the section's course\_id is "sticky", the import will not cross list the section to another course unless it is run with the Override UI option on the sis import.

Sample:

```
xlist_course_id,section_id,status
E411208,1B,active
E411208,2A,active
E411208,2A,active
```

The User identifier from users.csv for the observing user.

The User identifier from users.csv for the student user.

user\_observers.csv is optional. The goal of user\_observers.csv is to provide a way to create user\_observers. These observers will automatically be enrolled as an observer for each of the students enrollments. When a user\_observer is deleted the observer enrollments of the student are also deleted.

Sample:

```
observer_id,student_id,status
u411208,u411222,active
u411208,u411295,active
u413405,u411385,deleted
```

The User identifier from users.csv

The account identifier from accounts.csv. Uses the root\_account if left blank. The column is required even when importing for the root\_account and the value is blank.

Uses a role id, either built-in or defined by the account.

AccountAdmin, or a custom role defined by the account. When using a custom role, the name is case sensitive.

The domain of the account to search for the user.

admins.csv is optional. When importing admins that already exist in canvas the admin will become managed by sis. An admin cannot be deleted by running a sis import unless the admin is already managed by sis. Batch mode does not apply to the admins.csv, but diffing mode does apply to the admins.csv. Admins that already exist in the account will receive a notification of the new admin if notification preferences are set to receive this type of notification.

Sample:

```
user_id,account_id,role,status
E411208,01103,AccountAdmin,active
E411208,13834,AccountAdmin,deleted
E411208,13aa3,CustomAdmin,active
```

\* role or role\_id is required.

A unique identifier used to reference users in the enrollments table. This identifier must not change for the user, and must be globally unique. In the user interface, this is called the SIS ID.

A secondary unique identifier useful for more complex SIS integrations. This identifier must not change for the user, and must be globally unique.

The name that a user will use to login to Instructure. If you have an authentication service configured (like LDAP), this will be their username from the remote system.

If the account is configured to use LDAP or an SSO protocol then this should not be set. Otherwise this is the password that will be used to login to Canvas along with the 'login\_id' above.

Setting the password will in most cases log the user out of Canvas. The password can only be set one time. If the password has been set by the user or a previous sis import, it will not be changed.

Instead of a plain-text password, you can pass a pre-hashed password using the SSHA password generation scheme in this field. While better than passing a plain text password, you should still encourage users to change their password after logging in for the first time.

authentication\_provider\_id

The authentication provider this login is associated with. Logins associated with a specific provider can only be used with that provider. Legacy providers (LDAP, CAS, SAML) will search for logins associated with them, or unassociated logins. New providers will only search for logins explicitly associated with them. This can be the integer ID of the provider, or the type of the provider (in which case, it will find the first matching provider).

The User sis id from users.csv, required to identify a user.

The User integration\_id from users.csv, required to identify a user.

The canvas id for a user, required to identify a user.

The domain of the account to search for the user. This field is required when identifying a user in a trusted account.

The email address of the user. This might be the same as login\_id, but should still be provided.

\* One of existing\_user\_id or existing\_integration\_id or existing\_canvas\_user\_id is required.

logins.csv is optional. Logins can only be added to existing users. Logins can be removed using the users.csv.

Sample:

```
user_id,login_id,authentication_provider_id,password,existing_canvas_user_id,email
01103,bsmith01,,,Bob,Smith,Bobby Smith,98,bob.smith@myschool.edu
13834,jdoe03,google,,John,Doe,,92,john.doe@myschool.edu
13aa3,psue01,7,,Peggy,Sue,,93,peggy.sue@myschool.edu
```

The current sis\_id of the object that should be changed.

The desired sis\_id of the object. This id must be currently unique to the object type and the root\_account.

The current integration\_id of the object that should be changed. This column is not supported for group categories.

The desired integration\_id of the object. This id must be currently unique to the object type and the root\_account. This column is not supported for group categories. Can pass "&lt;delete&gt;" to remove the integration\_id from the object.

account, term, course, section, group, group\_category, user

\* old\_id or old\_integration\_id is required, new\_id or new\_integration\_id is required.

change\_sis\_id.csv is optional. The goal of change\_sis\_id.csv is to provide a way to change sis\_ids or integration\_ids of existing objects. If included in a zip file this file will process first. All other files should include the new ids.

Sample:

```
old_id,new_id,old_integration_id,new_integration_id,type
u001,u001a,user
couse1,old_course1,course
term1,fall17,term
u001,,,,user
,,integration01,int01,section
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 6 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).