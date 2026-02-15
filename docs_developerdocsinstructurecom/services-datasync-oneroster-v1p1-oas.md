---
title: OneRoster API | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/datasync/oneroster-v1p1-oas
source: sitemap
fetched_at: 2026-02-15T09:15:19.677219-03:00
rendered_js: false
word_count: 602
summary: This document outlines API endpoints for retrieving educational records such as schools, courses, academic sessions, and user enrollments from a student information system.
tags:
    - api-endpoints
    - sis-integration
    - oauth2
    - student-information-system
    - lti-jwt
    - education-technology
category: api
---

### Return collection of categories for the given class.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstringRequired

sourcedId of the class to get categories of

/sis/classes/{id}/categories

### Return collection of orgs.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstringRequired

sourcedId of the org to get

### Return collection of Schools. A School is an instance of an Org.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

### Return specific School. A School is an instance of an Org.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstringRequired

sourcedId of the School to get

### Return collection of enrollments.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

### Return specific enrollment.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstringRequired

sourcedId of the enrollment to get

### Return collection of terms. A Term is an instance of an AcademicSession.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

### Return specific term. A Term is an instance of an AcademicSession.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstringRequired

sourcedId of the term to get

### Return collection of all academic sessions.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

200

Academic session response

200

Academic session response

### Return specific academic session.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstringRequired

sourcedId of the academic session to get

200

Academic session response

200

Academic session response

### Return collection of grading periods. A grading period is an instance of an AcademicSession.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

### Return specific grading period. A grading period is an instance of an academic session.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstringRequired

sourcedId of the grading period to get

### Return collection of courses.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstringRequired

sourcedId of the course to get

### Return collection of classes.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstringRequired

sourcedId of the class to get

### Return collection of users.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstringRequired

sourcedId of the user to get

### Return collection of teachers. A teacher is an instance of a user.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

### Return specific teacher. A teacher is an instance of a user.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstringRequired

sourcedId of the teacher to get

### Return the collection of teachers teaching at this school.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

schoolIdstringRequired

sourcedId of the school to get teachers

/schools/{schoolId}/teachers

### Return collection of students. A student is an instance of a user.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

### Return specific student. A student is an instance of a user.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstringRequired

sourcedId of the student to get

### Return the collection of students attending this school.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

schoolIdstringRequired

sourcedId of the school to get students

/schools/{schoolId}/students

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).