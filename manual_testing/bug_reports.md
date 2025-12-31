### Bug ID: API-001
Title: Login API returns 200 with empty password
Severity: High
Priority: High
Steps:
1. Send POST request with empty password
Expected:
400 error
Actual:
200 OK