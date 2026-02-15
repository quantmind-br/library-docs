---
title: canvas types | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas/dataset-canvas-types
source: sitemap
fetched_at: 2026-02-15T09:12:08.236249-03:00
rendered_js: false
word_count: 4080
summary: This document provides a technical reference for database column types, enumerations, and object properties within a data schema, specifically focusing on workflow states and metadata fields.
tags:
    - database-schema
    - data-dictionary
    - field-definitions
    - workflow-states
    - backend-reference
    - metadata
category: reference
---

## access\_tokens\_\_workflow\_state

Type for column `access_tokens.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## account\_users\_\_workflow\_state

Type for column `account_users.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `accounts.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **active** = `'active'` - The only state an end customer will ever see.
- **suspended** = `'suspended'` - A state only site admins can see.

## assessment\_question\_banks\_\_context\_type

Discriminator for column `assessment_question_banks.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## assessment\_question\_banks\_\_workflow\_state

Type for column `assessment_question_banks.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## assessment\_questions\_\_workflow\_state

Type for column `assessment_questions.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **independently\_edited** = `'independently_edited'`

## asset\_user\_accesses\_\_action\_level

Type for column `asset_user_accesses.action_level`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **participate** = `'participate'`

## asset\_user\_accesses\_\_asset\_category

Type for column `asset_user_accesses.asset_category`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **announcements** = `'announcements'`
- **assignments** = `'assignments'`
- **calendar\_feed** = `'calendar_feed'`
- **collaborations** = `'collaborations'`
- **conferences** = `'conferences'`
- **speed\_grader** = `'speed_grader'`
- **external\_tools** = `'external_tools'`
- **external\_urls** = `'external_urls'`

## asset\_user\_accesses\_\_context\_type

Discriminator for column `asset_user_accesses.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **assessment\_question** = `'AssessmentQuestion'`

## asset\_user\_accesses\_\_membership\_type

Type for column `asset_user_accesses.membership_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **TeacherEnrollment** = `'TeacherEnrollment'`
- **AccountUser** = `'AccountUser'`
- **TaEnrollment** = `'TaEnrollment'`
- **DesignerEnrollment** = `'DesignerEnrollment'`
- **ObserverEnrollment** = `'ObserverEnrollment'`
- **GroupMembership** = `'GroupMembership'`
- **StudentEnrollment** = `'StudentEnrollment'`
- **StudentViewEnrollment** = `'StudentViewEnrollment'`

## assignment\_groups\_\_context\_type

Discriminator for column `assignment_groups.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type extracted from column `assignment_groups.rules`.

**Properties:**

- **drop\_highest** (int32 | None) - Number of highest scores to be dropped for each user.
- **drop\_lowest** (int32 | None) - Number of lowest scores to be dropped for each user.
- **never\_drop** (List\[int32]) - Assignment IDs that should never be dropped. E.g.: \[33, 17, 24].

## assignment\_groups\_\_workflow\_state

Type for column `assignment_groups.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **available** = `'available'` - Equivalent to `active` state in other tables.

## assignment\_override\_students\_\_workflow\_state

Type for column `assignment_override_students.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## assignment\_overrides\_\_set\_type

Discriminator for column `assignment_overrides.set_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **CourseSection** = `'CourseSection'`

## assignment\_overrides\_\_workflow\_state

Type for column `assignment_overrides.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## assignments\_\_context\_type

Type for column `assignments.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## assignments\_\_grading\_type

Type for column `assignments.grading_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **letter\_grade** = `'letter_grade'`
- **not\_graded** = `'not_graded'`

## assignments\_\_submission\_types

Type for column `assignments.submission_types`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **discussion\_topic** = `'discussion_topic'`
- **online\_quiz** = `'online_quiz'`
- **external\_tool** = `'external_tool'`
- **online\_text\_entry** = `'online_text_entry'`
- **online\_url** = `'online_url'`
- **online\_upload** = `'online_upload'`
- **media\_recording** = `'media_recording'`
- **not\_graded** = `'not_graded'`
- **student\_annotation** = `'student_annotation'`
- **default\_external\_tool** = `'default_external_tool'`

## assignments\_\_turnitin\_settings

Type extracted from column `assignments.turnitin_settings`.

**Properties:**

- **exclude\_small\_matches\_value** (int32 | None) - If exclude\_small\_matches\_type is set to percent or number then the value will be will be a number (of words or a percent).
- **s\_paper\_check** (bool | None) - If set to TRUE, will allow to compare submission against other students' papers.
- **s\_view\_report** (bool | None) - If set to TRUE students will be able to access their originality report.
- **internet\_check** (bool | None) - Select the content you'd like to compare papers against: current and archived website content.
- **journal\_check** (bool | None) - Select the content you'd like to compare papers against: periodicals, journals and publications.
- **exclude\_biblio** (bool | None) - Selecting this option will exclude text appearing in the bibliography, works cited, or references sections of student papers from being checked for matches when generating Similarity Reports.
- **exclude\_quoted** (bool | None) - Selecting this option will exclude text in student papers that is enclosed in quotation marks or is part of a block quotation (an indented block of text) from being checked for matches when generating Similarity Reports.
- **submit\_papers\_to** (bool | None) - If set to FALSE, a similarity report will still be generated for paper submissions but students' papers will not be stored in the Turnitin standard paper repository or the institution's paper repository for future comparison.

## assignments\_\_turnitin\_settings\_\_exclude\_small\_matches\_type

Type for column `assignments__turnitin_settings.exclude_small_matches_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## assignments\_\_turnitin\_settings\_\_originality\_report\_visibility

Type for column `assignments__turnitin_settings.originality_report_visibility`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **after\_grading** = `'after_grading'`
- **after\_due\_date** = `'after_due_date'`

Type for column `assignments.type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **assignment** = `'Assignment'`
- **subassignment** = `'SubAssignment'`

## assignments\_\_workflow\_state

Type for column `assignments.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **unpublished** = `'unpublished'`
- **duplicating** = `'duplicating'`
- **fail\_to\_import** = `'fail_to_import'`
- **failed\_to\_duplicate** = `'failed_to_duplicate'`
- **failed\_to\_import** = `'failed_to_import'`
- **failed\_to\_migrate** = `'failed_to_migrate'`
- **outcome\_alignment\_cloning** = `'outcome_alignment_cloning'`
- **failed\_to\_clone\_outcome\_alignment** = `'failed_to_clone_outcome_alignment'`

## attachment\_associations\_\_context\_type

Discriminator for column `attachment_associations.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **ConversationMessage** = `'ConversationMessage'`
- **Submission** = `'Submission'`

## attachments\_\_context\_type

Type for column `attachments.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **AssessmentQuestion** = `'AssessmentQuestion'`
- **Assignment** = `'Assignment'`
- **Attachment** = `'Attachment'`
- **ContentExport** = `'ContentExport'`
- **ContentMigration** = `'ContentMigration'`
- **Eportfolio** = `'Eportfolio'`
- **EpubExport** = `'EpubExport'`
- **GradebookUpload** = `'GradebookUpload'`
- **GroupAndMembershipImporter** = `'GroupAndMembershipImporter'`
- **OutcomeImport** = `'OutcomeImport'`
- **Quizzes\_\_Quiz** = `'Quizzes::Quiz'`
- **Quizzes\_\_QuizStatistics** = `'Quizzes::QuizStatistics'`
- **Quizzes\_\_QuizSubmission** = `'Quizzes::QuizSubmission'`
- **Submission** = `'Submission'`

Type for column `attachments.file_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **unpublished** = `'unpublished'`

## attachments\_\_workflow\_state

Type for column `attachments.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **pending\_upload** = `'pending_upload'`
- **processing** = `'processing'`
- **to\_be\_zipped** = `'to_be_zipped'`
- **unattached** = `'unattached'`
- **unattached\_temporary** = `'unattached_temporary'`

## calendar\_events\_\_context\_type

Discriminator for column `calendar_events.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **AppointmentGroup** = `'AppointmentGroup'`
- **CourseSection** = `'CourseSection'`

## calendar\_events\_\_workflow\_state

Type for column `calendar_events.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **locked** = `'locked'` - Indicates that `start_at`/`end_at` cannot be changed (though the event could be deleted). Normally only reservations or time slots with reservations are locked (see the Appointment Groups API).

## collaboration\_\_context\_type

Type for column `collaboration_comments.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `comment_bank_items.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **active** = `'active'` - Default value.

## communication\_channels\_\_path\_type

Type for column `communication_channels.path_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## communication\_channels\_\_workflow\_state

Type for column `communication_channels.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **unconfirmed** = `'unconfirmed'`

## content\_migrations\_\_context\_type

Discriminator for column `content_migrations.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## content\_migrations\_\_workflow\_state

Type for column `content_migrations.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **pre\_process\_error** = `'pre_process_error'`
- **pre\_processed** = `'pre_processed'`
- **pre\_processing** = `'pre_processing'`

## content\_participation\_counts\_\_content\_type

Discriminator for column `content_participation_counts.content_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **Submission** = `'Submission'`

## content\_participation\_counts\_\_context\_type

Discriminator for column `content_participation_counts.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## content\_participations\_\_content\_type

Discriminator for column `content_participations.content_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **Submission** = `'Submission'`

## content\_participations\_\_workflow\_state

Type for column `content_participations.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## content\_shares\_\_read\_state

Type for column `content_shares.read_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `content_shares.type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **SentContentShare** = `'SentContentShare'`
- **ReceivedContentShare** = `'ReceivedContentShare'`

## content\_tags\_\_associated\_asset\_type

Type for column `content_tags.associated_asset_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **LearningOutcomeGroup** = `'LearningOutcomeGroup'`
- **Lti\_\_ResourceLink** = `'Lti::ResourceLink'`

## content\_tags\_\_content\_type

Type for column `content_tags.content_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **Announcement** = `'Announcement'`
- **AssessmentQuestionBank** = `'AssessmentQuestionBank'`
- **Assignment** = `'Assignment'`
- **Attachment** = `'Attachment'`
- **ContextExternalTool** = `'ContextExternalTool'`
- **ContextModuleSubHeader** = `'ContextModuleSubHeader'`
- **DiscussionTopic** = `'DiscussionTopic'`
- **ExternalUrl** = `'ExternalUrl'`
- **LearningOutcome** = `'LearningOutcome'`
- **LearningOutcomeGroup** = `'LearningOutcomeGroup'`
- **LiveAssessments\_\_Assessment** = `'LiveAssessments::Assessment'`
- **Lti\_\_MessageHandler** = `'Lti::MessageHandler'`
- **Quizzes\_\_Quiz** = `'Quizzes::Quiz'`

## content\_tags\_\_context\_type

Type for column `content_tags.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **Assignment** = `'Assignment'`
- **LearningOutcomeGroup** = `'LearningOutcomeGroup'`
- **Quizzes\_\_Quiz** = `'Quizzes::Quiz'`

Type for column `content_tags.tag_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **context\_module** = `'context_module'` - indicates that the content object is a module item in a course (`context_type` will have a value of `Course`); the `id` value in the `content_tags` table may also be referred to as `item_id`; there will be a value in the `context_module_id` which indicates which module this content object appears under
- **learning\_outcome** = `'learning_outcome'` - indicates that the content object is aligned with a learning outcome (there will be a value in the `learning_outcome_id` field)
- **learning\_outcome\_association** = `'learning_outcome_association'` - with this value, the record will also have a value in the `associated_asset_id` and `associated_asset_type` fields; means that the content object is under a learning outcome folder (i.e. *Learning Outcome Group*)

## content\_tags\_\_workflow\_state

Type for column `content_tags.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **unpublished** = `'unpublished'`

## context\_external\_tools\_\_context\_type

Type for column `context_external_tools.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## context\_external\_tools\_\_settings

Type extracted from column `context_external_tools.settings`.

**Properties:**

- **course\_home\_sub\_navigation** (str | None) - Course home sub navigation placement type.
- **course\_settings\_sub\_navigation** (str | None) - Course settings sub navigation placement type.
- **custom\_fields** (str | None) - Custom parameters provider request to share on every single LTI launch, each placement column might have its own set of custom\_fields.
- **discussion\_menu** (str | None) - Discussion menu placement type.
- **discussion\_topic\_index\_menu** (str | None) - Discussion topic index menu placement type.
- **discussion\_topic\_menu** (str | None) - Discussion topic menu placement type.
- **editor\_button** (str | None) - RCE placement type.
- **enabled** (str | None) - Controls if the tool is disabled for user to click on, typically tool gets removed altogether but sometimes provider uses this setting to just disable it in the UI.
- **file\_index\_menu** (str | None) - File index menu placement type.
- **file\_menu** (str | None) - File menu placement type.
- **global\_navigation** (str | None) - Global navigation placement type.
- **grade\_passback** (str | None) - Grade pass-back placement type.
- **homework\_selection** (str | None) - Homework selection placement type.
- **homework\_submission** (str | None) - Homework submission placement type.
- **launch\_presentation\_document\_target** (str | None) - Tells us if it should be opened in another window.
- **link\_selection** (str | None) - Link selection placement type.
- **migration\_selection** (str | None) - Migration selection placement type.
- **module\_group\_menu** (str | None) - Module group menu placement type.
- **module\_index\_menu** (str | None) - Module index menu placement type.
- **account\_navigation** (str | None) - account navigation placement type.
- **assignment\_group\_menu** (str | None) - Assignment group menu placement type.
- **assignment\_index\_menu** (str | None) - Assignment index menu placement type.
- **assignment\_menu** (str | None) - Assignment menu placement type.
- **assignment\_selection** (str | None) - Assignment selection placement type.
- **canvas\_caliper\_url** (str | None) - URL to caliper endpoint if supported by the tool.
- **collaboration** (str | None) - Collaboration placement type.
- **content\_migration** (str | None) - Content migration placement type.
- **course\_assignments\_menu** (str | None) - Course assignments menu placement type.
- **course\_navigation** (str | None) - Course navigation placement type.
- **module\_menu** (str | None) - Module menu placement type.
- **post\_grades** (str | None) - Post grades placement type.
- **quiz\_index\_menu** (str | None) - Quiz index menu placement type.
- **quiz\_menu** (str | None) - Quiz menu placement type.
- **similarity\_detection** (str | None) - Plagiarism platform placement.
- **student\_context\_card** (str | None) - Student context card placement type.
- **text** (str | None) - Identifies the name of the tool, default what the user can see if no label is set.
- **tool\_configuration** (str | None) - Identifies the LTI tool configuration dataset.
- **use\_1\_3** (str | None) - LTI 1.3 compliant tool.
- **user\_navigation** (str | None) - User navigation placement type.
- **visibility** (str | None) - Controls if it is an admin only tool, takes values of `admin` and `members`.
- **wiki\_index\_menu** (str | None) - Wiki index menu placement type.
- **wiki\_page\_menu** (str | None) - Wiki page menu placement type.

## context\_external\_tools\_\_workflow\_state

Type for column `context_external_tools.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **anonymous** = `'anonymous'` - no identifying information about the user will be sent to the vendor
- **email\_only** = `'email_only'` - the user's email is the only identifying information sent to the vendor
- **name\_only** = `'name_only'` - the user's name is the only identifying information sent to the vendor
- **public** = `'public'` - various identifying information (name, email, Canvas ID, SIS ID of the course, SIS ID of the user, etc.) is sent to the vendor

## context\_module\_progressions\_\_workflow\_state

Type for column `context_module_progressions.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## context\_modules\_\_context\_type

Type for column `context_modules.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## context\_modules\_\_workflow\_state

Type for column `context_modules.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **unpublished** = `'unpublished'`

## conversation\_message\_participants\_\_workflow\_state

Type for column `conversation_message_participants.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## conversation\_messages\_\_asset\_type

Type for column `conversation_messages.asset_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **Submission** = `'Submission'`

## conversation\_messages\_\_context\_type

Type for column `conversation_messages.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `conversation_messages.media_comment_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **audio\_flac** = `'audio/flac'`
- **audio\_mpeg** = `'audio/mpeg'`
- **audio\_vnd\_dlna\_adts** = `'audio/vnd.dlna.adts'`
- **audio\_webm** = `'audio/webm'`
- **audio\_xm4a** = `'audio/x-m4a'`
- **audio\_xmswma** = `'audio/x-ms-wma'`
- **audio\_xwav** = `'audio/x-wav'`
- **video\_3gpp** = `'video/3gpp'`
- **video\_mpeg** = `'video/mpeg'`
- **video\_quicktime** = `'video/quicktime'`
- **video\_webm** = `'video/webm'`
- **video\_xm4v** = `'video/x-m4v'`
- **video\_xmatroska** = `'video/x-matroska'`
- **video\_xmsasf** = `'video/x-ms-asf'`
- **video\_xmswmv** = `'video/x-ms-wmv'`
- **video\_xmsvideo** = `'video/x-msvideo'`

## conversation\_participants\_\_workflow\_state

Type for column `conversation_participants.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## conversations\_\_context\_type

Type for column `conversations.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **Course** = `'Course'` - the sender selected a course when composing the message
- **Group** = `'Group'` - the sender selected a group when composing the message
- **Account** = `'Account'` - the sender did not select a course or group when composing the message

## course\_sections\_\_workflow\_state

Type for column `course_sections.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type extracted from column `courses.settings`.

**Properties:**

- **allow\_student\_discussion\_editing** (str | None) - Let students edit or delete their own discussion posts.
- **allow\_student\_discussion\_topics** (str | None) - Let students create discussion topics.
- **course\_format** (str | None) - Format of a course, values include `blended`, `on_campus`, `online`.
- **filter\_speed\_grader\_by\_student\_group** (str | None) - Filter SpeedGrader by student group.
- **hide\_distribution\_graphs** (str | None) - Hide grade distribution graphs from students.
- **hide\_final\_grade** (str | None) - Hide totals in student grades summary.
- **is\_public\_to\_auth\_users** (str | None) - Set to true if course is public only to authenticated users.
- **lock\_all\_announcements** (str | None) - Disable comments on announcements.
- **public\_syllabus** (str | None) - Set to true to make the course syllabus public. Values include true, false.
- **public\_syllabus\_to\_auth** (str | None) - Set to true to make the course syllabus public for authenticated users.
- **restrict\_student\_future\_view** (str | None) - Restrict students from viewing courses before start date.
- **restrict\_student\_past\_view** (str | None) - Restrict students from viewing courses after end date.
- **syllabus\_updated\_at** (str | None) - Timestamp when syllabus was updated in a course.
- **usage\_rights\_required** (str | None) - Copyright and license information must be provided for files before they are published.
- **allow\_student\_forum\_attachments** (str | None) - Whether students can attach files to discussions.

Type for column `courses.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **created** = `'created'` - course created by admin, no teacher assigned yet
- **claimed** = `'claimed'` - teacher has been assigned to course or course created by teacher (not published)
- **available** = `'available'` - published
- **completed** = `'completed'` - course manually marked as completed
- **deleted** = `'deleted'` - course manually deleted (possibly created in error; sometimes admin and instructors delete courses to clear from their list); note: if a course is deleted it won't necessarily delete the wiki pages, but does cascade to enrollments

## custom\_gradebook\_columns\_\_workflow\_state

Type for column `custom_gradebook_columns.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## developer\_key\_account\_bindings\_\_workflow\_state

Type for column `developer_key_account_bindings.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## developer\_keys\_\_workflow\_state

Type for column `developer_keys.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## discussion\_entries\_\_workflow\_state

Type for column `discussion_entries.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## discussion\_entry\_participants\_\_workflow\_state

Type for column `discussion_entry_participants.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## discussion\_topic\_participants\_\_workflow\_state

Type for column `discussion_topic_participants.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## discussion\_topics\_\_context\_type

Type for column `discussion_topics.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **Course** = `'Course'` - entire class can participate
- **Group** = `'Group'` - only people in the group can participate

## discussion\_topics\_\_discussion\_type

Type for column `discussion_topics.discussion_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **side\_comment** = `'side_comment'` - The same as not\_threaded. This value is obsolete.
- **threaded** = `'threaded'` - Allows replies within replies. Maximum depth of replies is 3.
- **not\_threaded** = `'not_threaded'` - Prevent users from replying to replies, only to the original topic.

Type for column `discussion_topics.type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **Announcement** = `'Announcement'`

## discussion\_topics\_\_workflow\_state

Type for column `discussion_topics.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **active** = `'active'` - displayed to any user in the course
- **post\_delayed** = `'post_delayed'` - discussion created, but set to go live at a certain date
- **unpublished** = `'unpublished'` - created but not yet published (draft state)

## enrollment\_dates\_overrides\_\_context\_type

Discriminator for column `enrollment_dates_overrides.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## enrollment\_dates\_overrides\_\_enrollment\_type

Type for column `enrollment_dates_overrides.enrollment_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **DesignerEnrollment** = `'DesignerEnrollment'`
- **StudentEnrollment** = `'StudentEnrollment'`
- **TaEnrollment** = `'TaEnrollment'`
- **TeacherEnrollment** = `'TeacherEnrollment'`

Type for column `enrollment_states.state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **creation\_pending** = `'creation_pending'`
- **current\_and\_invited** = `'current_and_invited'`
- **current\_and\_future** = `'current_and_future'`
- **current\_and\_concluded** = `'current_and_concluded'`
- **pending\_active** = `'pending_active'`
- **pending\_invited** = `'pending_invited'`

## enrollment\_terms\_\_workflow\_state

Type for column `enrollment_terms.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `enrollments.type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **StudentEnrollment** = `'StudentEnrollment'`
- **TeacherEnrollment** = `'TeacherEnrollment'`
- **TaEnrollment** = `'TaEnrollment'`
- **DesignerEnrollment** = `'DesignerEnrollment'`
- **ObserverEnrollment** = `'ObserverEnrollment'`
- **StudentViewEnrollment** = `'StudentViewEnrollment'` - this role is typically used by course designers or instructors to view the course as a student would see it

## enrollments\_\_workflow\_state

Type for column `enrollments.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **creation\_pending** = `'creation_pending'` - created but user hasn't logged in yet
- **invited** = `'invited'` - admin added student through sis
- **rejected** = `'rejected'` - student rejected invite
- **active** = `'active'` - user can fully participate in course
- **inactive** = `'inactive'` - hard state (i.e., tuition not paid or user drops course); user can no longer access course content
- **completed** = `'completed'` - manually marked as completed (*conclude this enrollment* button); user can only view course in read-only format
- **deleted** = `'deleted'` - enrollment removed from course (soft-deleted, so users with admin permissions can include in reports)

Discriminator for column `favorites.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Discriminator for column `folders.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `folders.unique_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **sadocs** = `'student annotation documents'`
- **imicons** = `'icon maker icons'`
- **baicons** = `'buttons and icons'`

Type for column `folders.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## grading\_period\_groups\_\_workflow\_state

Type for column `grading_period_groups.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## grading\_periods\_\_workflow\_state

Type for column `grading_periods.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## grading\_standards\_\_context\_type

Discriminator for column `grading_standards.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## grading\_standards\_\_workflow\_state

Type for column `grading_standards.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## group\_categories\_\_context\_type

Discriminator for column `group_categories.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `group_categories.role`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **communities** = `'communities'`
- **student\_organized** = `'student_organized'`

## group\_memberships\_\_workflow\_state

Type for column `group_memberships.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `groups.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `groups.default_view`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `groups.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## learning\_outcome\_groups\_\_context\_type

Type for column `learning_outcome_groups.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **Department** = `'Department'`

## learning\_outcome\_groups\_\_workflow\_state

Type for column `learning_outcome_groups.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## learning\_outcome\_question\_results\_\_associated\_asset\_type

Discriminator for column `learning_outcome_question_results.associated_asset_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **AssessmentQuestion** = `'AssessmentQuestion'`

## learning\_outcome\_results\_\_artifact\_type

Discriminator for column `learning_outcome_results.artifact_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **LiveAssessments\_\_Submission** = `'LiveAssessments::Submission'`
- **Quizzes\_\_QuizSubmission** = `'Quizzes::QuizSubmission'`
- **RubricAssessment** = `'RubricAssessment'`
- **Submission** = `'Submission'`

## learning\_outcome\_results\_\_associated\_asset\_type

Discriminator for column `learning_outcome_results.associated_asset_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **AssessmentQuestion** = `'AssessmentQuestion'`
- **LiveAssessments\_\_Assessment** = `'LiveAssessments::Assessment'`
- **Assignment** = `'Assignment'`
- **Quizzes\_\_Quiz** = `'Quizzes::Quiz'`

## learning\_outcome\_results\_\_association\_type

Discriminator for column `learning_outcome_results.association_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **Assignment** = `'Assignment'`
- **Quizzes\_\_Quiz** = `'Quizzes::Quiz'`
- **RubricAssociation** = `'RubricAssociation'`

## learning\_outcome\_results\_\_context\_type

Type for column `learning_outcome_results.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## learning\_outcome\_results\_\_workflow\_state

Type for column `learning_outcome_results.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## learning\_outcomes\_\_calculation\_method

Type for column `learning_outcomes.calculation_method`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **decaying\_average** = `'decaying_average'`
- **weighted\_average** = `'weighted_average'`
- **standard\_decaying\_average** = `'standard_decaying_average'`

## learning\_outcomes\_\_context\_type

Type for column `learning_outcomes.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## learning\_outcomes\_\_workflow\_state

Type for column `learning_outcomes.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## lti\_line\_items\_\_workflow\_state

Type for column `lti_line_items.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## lti\_resource\_links\_\_context\_type

Discriminator for column `lti_resource_links.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **Assignment** = `'Assignment'`

## lti\_resource\_links\_\_workflow\_state

Type for column `lti_resource_links.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## lti\_results\_\_workflow\_state

Type for column `lti_results.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## master\_courses\_child\_content\_tags\_\_content\_type

Discriminator for column `master_courses_child_content_tags.content_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **AssessmentQuestionBank** = `'AssessmentQuestionBank'`
- **Assignment** = `'Assignment'`
- **AssignmentGroup** = `'AssignmentGroup'`
- **Attachment** = `'Attachment'`
- **CalendarEvent** = `'CalendarEvent'`
- **ContextExternalTool** = `'ContextExternalTool'`
- **ContextModule** = `'ContextModule'`
- **ContentTag** = `'ContentTag'`
- **CoursePace** = `'CoursePace'`
- **DiscussionTopic** = `'DiscussionTopic'`
- **LearningOutcome** = `'LearningOutcome'`
- **LearningOutcomeGroup** = `'LearningOutcomeGroup'`
- **Quizzes\_\_Quiz** = `'Quizzes::Quiz'`

## master\_courses\_child\_subscriptions\_\_workflow\_state

Type for column `master_courses_child_subscriptions.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## master\_courses\_master\_content\_tags\_\_content\_type

Discriminator for column `master_courses_master_content_tags.content_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **AssessmentQuestionBank** = `'AssessmentQuestionBank'`
- **Assignment** = `'Assignment'`
- **AssignmentGroup** = `'AssignmentGroup'`
- **Attachment** = `'Attachment'`
- **CalendarEvent** = `'CalendarEvent'`
- **ContextExternalTool** = `'ContextExternalTool'`
- **ContextModule** = `'ContextModule'`
- **ContentTag** = `'ContentTag'`
- **CoursePace** = `'CoursePace'`
- **DiscussionTopic** = `'DiscussionTopic'`
- **LearningOutcome** = `'LearningOutcome'`
- **Quizzes\_\_Quiz** = `'Quizzes::Quiz'`
- **MediaTrack** = `'MediaTrack'`

## master\_courses\_master\_migrations\_\_workflow\_state

Type for column `master_courses_master_migrations.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **exports\_failed** = `'exports_failed'`
- **imports\_failed** = `'imports_failed'`
- **imports\_queued** = `'imports_queued'`

## master\_courses\_master\_templates\_\_workflow\_state

Type for column `master_courses_master_templates.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## master\_courses\_migration\_results\_\_import\_type

Type for column `master_courses_migration_results.import_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## master\_courses\_migration\_results\_\_state

Type for column `master_courses_migration_results.state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## originality\_reports\_\_workflow\_state

Type for column `originality_reports.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## outcome\_proficiencies\_\_context\_type

Discriminator for column `outcome_proficiencies.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## outcome\_proficiencies\_\_workflow\_state

Type for column `outcome_proficiencies.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## outcome\_proficiency\_ratings\_\_workflow\_state

Type for column `outcome_proficiency_ratings.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## pseudonyms\_\_workflow\_state

Type for column `pseudonyms.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## quiz\_questions\_\_question\_data

Type extracted from column `quiz_questions.question_data`.

**Properties:**

- **neutral\_comments** (str | None) - Comments to be displayed regardless of how the student answers the question.
- **answers** (str | None) - Collection of possible answers.
- **name** (str | None) - Name of the question.
- **question\_type** (str | None) - Denotes the type of the question.
- **question\_text** (str | None) - Text of the question.
- **regrade\_option** ([quiz\_questions\_\_question\_data\_\_regrade\_option](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas/dataset-canvas-types#dap_schemas.canvas.quiz_questions__question_data__regrade_option) | None) - Denotes if regrading is available for the question. Possible values are `available` and `unavailable` for question types. Defaults to `available` for the allowed question types and NULL for the rest.
- **correct\_comments** (str | None) - Comments to be displayed if the student answers the question correctly.
- **incorrect\_comments** (str | None) - Comments to be displayed if the student answers the question incorrectly.
- **text\_after\_answers** (str | None) - (Used in *short\_answer\_question*, also known as *fill\_in\_the\_blank*. Omitted for other question types.) Text following the missing word.
- **matching\_answer\_incorrect\_matches** (str | None) - (Used in *matching\_question*. Omitted for other question types.) List of distractors (incorrect answers), delimited by new lines, that will be seeded with all the *answer\_match\_right* values.
- **points\_possible** (float64 | None) - Maximum number of points that can be awarded for answering the question correctly.

## quiz\_questions\_\_question\_data\_\_regrade\_option

Type for `regrade_option` extracted from column `quiz_questions.question_data`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **unavailable** = `'unavailable'`
- **multiple\_answers\_question** = `'multiple_answers_question'`
- **multiple\_choice\_question** = `'multiple_choice_question'`
- **true\_false\_question** = `'true_false_question'`
- **current\_and\_previous\_correct** = `'current_and_previous_correct'`
- **no\_regrade** = `'no_regrade'`
- **current\_correct\_only** = `'current_correct_only'`
- **full\_credit** = `'full_credit'`

## quiz\_questions\_\_workflow\_state

Type for column `quiz_questions.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## quiz\_submissions\_\_workflow\_state

Type for column `quiz_submissions.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **pending\_review** = `'pending_review'` - denotes that a manual submission has been made by the student which has not been completely graded yet. This usually happens when one or more questions in the quiz cannot be autograded (e.g. *essay\_question* type questions)
- **preview** = `'preview'` - when a Teacher or Admin previews a quiz (even a partial one)
- **settings\_only** = `'settings_only'` - pertains only to quiz moderation events (stores the settings to create and store moderation events before the student has begun an attempt)
- **untaken** = `'untaken'` - default value; a quiz submission is recorded as soon as a student starts the quiz-taking process (before even answering the first question)

Type for column `quizzes.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `quizzes.quiz_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **assignment** = `'assignment'` - appears as *Graded Quiz* in the UI (a column is created in the grade book for any graded quizzes)
- **practice\_quiz** = `'practice_quiz'` - appears as *Practice Quiz* in the UI (students do not receive a grade for practice quizzes)
- **graded\_survey** = `'graded_survey'` - appears as *Graded Survey* in the UI (allows instructor to give students points for completing the survey, but it does not allow the survey to be graded for right or wrong answers)
- **survey** = `'survey'` - appears as *Ungraded Survey* in the UI (students do not receive a grade for their responses)

Type for column `quizzes.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **created** = `'created'` - quiz created, but no further actions have been taken
- **edited** = `'edited'` - after the teacher makes edits to quiz
- **unpublished** = `'unpublished'` - teacher unpublished a published quiz
- **available** = `'available'` - published and available

## role\_overrides\_\_context\_type

Discriminator for column `role_overrides.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `roles.base_role_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **AccountAdmin** = `'AccountAdmin'`
- **AccountMembership** = `'AccountMembership'`
- **DesignerEnrollment** = `'DesignerEnrollment'`
- **NoPermissions** = `'NoPermissions'`
- **ObserverEnrollment** = `'ObserverEnrollment'`
- **StudentEnrollment** = `'StudentEnrollment'`
- **TaEnrollment** = `'TaEnrollment'`
- **TeacherEnrollment** = `'TeacherEnrollment'`

Type for column `roles.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **built\_in** = `'built_in'` - default roles that are included in each Canvas shard

## rubric\_assessments\_\_artifact\_type

Discriminator for column `rubric_assessments.artifact_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **Submission** = `'Submission'`
- **Assignment** = `'Assignment'`
- **ModeratedGrading\_\_ProvisionalGrade** = `'ModeratedGrading::ProvisionalGrade'`

## rubric\_assessments\_\_assessment\_type

Type for column `rubric_assessments.assessment_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **invited\_assessment** = `'invited_assessment'`
- **peer\_review** = `'peer_review'`

## rubric\_associations\_\_association\_type

Discriminator for column `rubric_associations.association_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **Assignment** = `'Assignment'`

## rubric\_associations\_\_context\_type

Discriminator for column `rubric_associations.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## rubric\_associations\_\_workflow\_state

Type for column `rubric_associations.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Discriminator for column `rubrics.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `rubrics.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `scores.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## submission\_comments\_\_context\_type

Discriminator for column `submission_comments.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `submission_comments.media_comment_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **audio\_flac** = `'audio/flac'`
- **audio\_mpeg** = `'audio/mpeg'`
- **audio\_vnd\_dlna\_adts** = `'audio/vnd.dlna.adts'`
- **audio\_webm** = `'audio/webm'`
- **audio\_xm4a** = `'audio/x-m4a'`
- **audio\_xmswma** = `'audio/x-ms-wma'`
- **audio\_xwav** = `'audio/x-wav'`
- **video\_3gpp** = `'video/3gpp'`
- **video\_mpeg** = `'video/mpeg'`
- **video\_quicktime** = `'video/quicktime'`
- **video\_webm** = `'video/webm'`
- **video\_xm4v** = `'video/x-m4v'`
- **video\_xmatroska** = `'video/x-matroska'`
- **video\_xmsasf** = `'video/x-ms-asf'`
- **video\_xmswmv** = `'video/x-ms-wmv'`
- **video\_xmsvideo** = `'video/x-msvideo'`

## submission\_versions\_\_context\_type

Discriminator for column `submission_versions.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `submissions.media_comment_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **audio\_flac** = `'audio/flac'`
- **audio\_mpeg** = `'audio/mpeg'`
- **audio\_vnd\_dlna\_adts** = `'audio/vnd.dlna.adts'`
- **audio\_webm** = `'audio/webm'`
- **audio\_xm4a** = `'audio/x-m4a'`
- **audio\_xmswma** = `'audio/x-ms-wma'`
- **audio\_xwav** = `'audio/x-wav'`
- **video\_3gpp** = `'video/3gpp'`
- **video\_mpeg** = `'video/mpeg'`
- **video\_quicktime** = `'video/quicktime'`
- **video\_webm** = `'video/webm'`
- **video\_xm4v** = `'video/x-m4v'`
- **video\_xmatroska** = `'video/x-matroska'`
- **video\_xmsasf** = `'video/x-ms-asf'`
- **video\_xmswmv** = `'video/x-ms-wmv'`
- **video\_xmsvideo** = `'video/x-msvideo'`

## submissions\_\_submission\_type

Type for column `submissions.submission_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **basic\_lti\_launch** = `'basic_lti_launch'`
- **discussion\_topic** = `'discussion_topic'`
- **external\_tool** = `'external_tool'`
- **media\_recording** = `'media_recording'`
- **online\_file\_upload** = `'online_file_upload'`
- **online\_quiz** = `'online_quiz'`
- **online\_text\_entry** = `'online_text_entry'`
- **online\_upload** = `'online_upload'`
- **online\_url** = `'online_url'`
- **student\_annotation** = `'student_annotation'`

## submissions\_\_workflow\_state

Type for column `submissions.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **pending\_review** = `'pending_review'`
- **unsubmitted** = `'unsubmitted'`

Type for column `users.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **creation\_pending** = `'creation_pending'`
- **pending\_approval** = `'pending_approval'`
- **pre\_registered** = `'pre_registered'`
- **registered** = `'registered'`

## web\_conference\_participants\_\_participation\_type

Type for column `web_conference_participants.participation_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## web\_conferences\_\_conference\_type

Type for column `web_conferences.conference_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **AdobeConnect** = `'AdobeConnect'`
- **BigBlueButton** = `'BigBlueButton'`
- **CiscoWebex** = `'CiscoWebex'`

## web\_conferences\_\_context\_type

Discriminator for column `web_conferences.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Type for column `wiki_pages.context_type`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

## wiki\_pages\_\_workflow\_state

Type for column `wiki_pages.workflow_state`.

**Members:**

- **unspecified** = `'__dap_unspecified__'`
- **post\_delayed** = `'post_delayed'`
- **unpublished** = `'unpublished'`

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).