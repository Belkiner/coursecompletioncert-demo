# Suggested Course Criteria

Use these if the current CourseCompletionCert UI supports them.

1. API functionality — 40%
   - GET /health returns HTTP 200 and JSON status.
   - GET /tasks returns the task list.
   - POST /tasks creates a task and returns HTTP 201.

2. Validation and error handling — 30%
   - title is required and cannot be blank.
   - Non-JSON or malformed payloads are rejected.
   - Errors use predictable JSON fields.

3. Documentation and tests — 30%
   - README includes setup, run, and request examples.
   - Automated tests cover success and invalid-input cases.
   - A reviewer can reproduce the result locally.

Total: 100%.
