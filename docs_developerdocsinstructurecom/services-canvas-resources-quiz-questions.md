---
title: Quiz Questions | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/quiz_questions
source: sitemap
fetched_at: 2026-02-15T09:08:58.797008-03:00
rendered_js: false
word_count: 464
summary: This document provides technical specifications for the QuizQuestion and Answer objects, including detailed descriptions of API endpoints for creating, updating, and retrieving quiz questions within a course.
tags:
    - api-reference
    - canvas-lms
    - quiz-management
    - rest-api
    - educational-technology
    - data-schema
category: api
---

**A QuizQuestion object looks like:**

```
{
  // The ID of the quiz question.
"id": 1,
  // The ID of the Quiz the question belongs to.
"quiz_id": 2,
  // The order in which the question will be retrieved and displayed.
"position": 1,
  // The name of the question.
"question_name": "Prime Number Identification",
  // The type of the question.
"question_type": "multiple_choice_question",
  // The text of the question.
"question_text": "Which of the following is NOT a prime number?",
  // The maximum amount of points possible received for getting this question
  // correct.
"points_possible": 5,
  // The comments to display if the student answers the question correctly.
"correct_comments": "That's correct!",
  // The comments to display if the student answers incorrectly.
"incorrect_comments": "Unfortunately, that IS a prime number.",
  // The comments to display regardless of how the student answered.
"neutral_comments": "Goldbach's conjecture proposes that every even integer greater than 2 can be expressed as the sum of two prime numbers.",
  // An array of available answers to display to the student.
"answers": null
}
```

**An Answer object looks like:**

```
{
  // The unique identifier for the answer.  Do not supply if this answer is part
  // of a new question
  "id": 6656,
  // The text of the answer.
  "answer_text": "Constantinople",
  // An integer to determine correctness of the answer. Incorrect answers should
  // be 0, correct answers should be 100.
  "answer_weight": 100,
  // Specific contextual comments for a particular answer.
  "answer_comments": "Remember to check your spelling prior to submitting this answer.",
  // Used in missing word questions.  The text to follow the missing word
  "text_after_answers": " is the capital of Utah.",
  // Used in matching questions.  The static value of the answer that will be
  // displayed on the left for students to match for.
  "answer_match_left": "Salt Lake City",
  // Used in matching questions. The correct match for the value given in
  // answer_match_left.  Will be displayed in a dropdown with the other
  // answer_match_right values..
  "answer_match_right": "Utah",
  // Used in matching questions. A list of distractors, delimited by new lines (
  // ) that will be seeded with all the answer_match_right values.
  "matching_answer_incorrect_matches": "Nevada
  California
  Washington",
  // Used in numerical questions.  Values can be 'exact_answer', 'range_answer',
  // or 'precision_answer'.
  "numerical_answer_type": "exact_answer",
  // Used in numerical questions of type 'exact_answer'.  The value the answer
  // should equal.
  "exact": 42,
  // Used in numerical questions of type 'exact_answer'. The margin of error
  // allowed for the student's answer.
  "margin": 4,
  // Used in numerical questions of type 'precision_answer'.  The value the answer
  // should equal.
  "approximate": 1234600000.0,
  // Used in numerical questions of type 'precision_answer'. The numerical
  // precision that will be used when comparing the student's answer.
  "precision": 4,
  // Used in numerical questions of type 'range_answer'. The start of the allowed
  // range (inclusive).
  "start": 1,
  // Used in numerical questions of type 'range_answer'. The end of the allowed
  // range (inclusive).
  "end": 10,
  // Used in fill in multiple blank and multiple dropdowns questions.
  "blank_id": 1170
}
```

[Quizzes::QuizQuestionsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_questions_controller.rb)

`GET /api/v1/courses/:course_id/quizzes/:quiz_id/questions`

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/questions`

Returns the paginated list of QuizQuestions in this quiz.

**Request Parameters:**

If specified, the endpoint will return the questions that were presented for that submission. This is useful if the quiz has been modified after the submission was created and the latest quiz version’s set of questions does not match the submission’s. NOTE: you must specify quiz\_submission\_attempt as well if you specify this parameter.

The attempt of the submission you want the questions for.

Returns a list of [QuizQuestion](https://developerdocs.instructure.com/services/canvas/resources/quiz_questions#quizquestion) objects.

[Quizzes::QuizQuestionsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_questions_controller.rb)

`GET /api/v1/courses/:course_id/quizzes/:quiz_id/questions/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/questions/:id`

Returns the quiz question with the given id

**Request Parameters:**

The quiz question unique identifier.

Returns a [QuizQuestion](https://developerdocs.instructure.com/services/canvas/resources/quiz_questions#quizquestion) object.

[Quizzes::QuizQuestionsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_questions_controller.rb)

`POST /api/v1/courses/:course_id/quizzes/:quiz_id/questions`

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:quiz_id/questions`

Create a new quiz question for this quiz

**Request Parameters:**

The name of the question.

The text of the question.

The id of the quiz group to assign the question to.

The type of question. Multiple optional fields depend upon the type of question to be used.

Allowed values: `calculated_question`, `essay_question`, `file_upload_question`, `fill_in_multiple_blanks_question`, `matching_question`, `multiple_answers_question`, `multiple_choice_question`, `multiple_dropdowns_question`, `numerical_question`, `short_answer_question`, `text_only_question`, `true_false_question`

The order in which the question will be displayed in the quiz in relation to other questions.

`question[points_possible]`

The maximum amount of points received for answering this question correctly.

`question[correct_comments]`

The comment to display if the student answers the question correctly.

`question[incorrect_comments]`

The comment to display if the student answers incorrectly.

`question[neutral_comments]`

The comment to display regardless of how the student answered.

`question[text_after_answers]`

Returns a [QuizQuestion](https://developerdocs.instructure.com/services/canvas/resources/quiz_questions#quizquestion) object.

[Quizzes::QuizQuestionsController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_questions_controller.rb)

`PUT /api/v1/courses/:course_id/quizzes/:quiz_id/questions/:id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/quizzes/:quiz_id/questions/:id`

Updates an existing quiz question for this quiz

**Request Parameters:**

The associated quiz’s unique identifier.

The quiz question’s unique identifier.

The name of the question.

The text of the question.

The id of the quiz group to assign the question to.

The type of question. Multiple optional fields depend upon the type of question to be used.

Allowed values: `calculated_question`, `essay_question`, `file_upload_question`, `fill_in_multiple_blanks_question`, `matching_question`, `multiple_answers_question`, `multiple_choice_question`, `multiple_dropdowns_question`, `numerical_question`, `short_answer_question`, `text_only_question`, `true_false_question`

The order in which the question will be displayed in the quiz in relation to other questions.

`question[points_possible]`

The maximum amount of points received for answering this question correctly.

`question[correct_comments]`

The comment to display if the student answers the question correctly.

`question[incorrect_comments]`

The comment to display if the student answers incorrectly.

`question[neutral_comments]`

The comment to display regardless of how the student answered.

`question[text_after_answers]`

Returns a [QuizQuestion](https://developerdocs.instructure.com/services/canvas/resources/quiz_questions#quizquestion) object.

[Quizzes::QuizQuestionsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_questions_controller.rb)

`DELETE /api/v1/courses/:course_id/quizzes/:quiz_id/questions/:id`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/quizzes/:quiz_id/questions/:id`

**204 No Content** response code is returned if the deletion was successful.

**Request Parameters:**

The associated quiz’s unique identifier

The quiz question’s unique identifier

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).