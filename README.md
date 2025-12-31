# QA API Testing Project 🧪

## 📌 Overview
This repository demonstrates a **professional QA approach** to testing REST APIs using **manual testing documentation** and **automated API tests** built with Python.

The project focuses on:
- Test design thinking
- API validation
- Error handling
- Stable and maintainable test automation

It is designed to reflect **real-world QA engineering practices**, not just tool usage.

---

## 🎯 Scope of Testing
The following areas are covered:

- Authentication API testing
- Positive and negative test scenarios
- Status code validation
- Response body validation
- Error handling behavior
- Test stability (mocked API behavior)

---

## 🧰 Tools & Technologies
- **Python**
- **Pytest**
- **Requests**
- **Markdown** (manual QA documentation)
- **Git / GitHub**

---

## 📂 Project Structure
```
qa-api-testing-project/
│
├── manual_testing/
│ ├── test_scenarios.md # High-level test scenarios
│ ├── test_cases.md # Detailed test cases
│ └── bug_reports.md # Sample bug reports
│
├── api_tests/
│ ├── test_auth_api.py # Automated API tests
│
├── utils/
│ └── api_client.py # API client / mocked responses
│
├── requirements.txt
└── README.md
```


---

## 🧪 Manual Testing
Manual testing artifacts include:
- Well-defined **test scenarios**
- Step-by-step **test cases**
- Sample **bug reports** with severity & priority

These documents demonstrate:
- Requirement understanding
- Risk-based thinking
- Clear QA communication

---

## 🤖 Automated API Testing
Automated tests validate:
- Successful authentication
- Failure cases (missing or invalid data)
- Response structure and status codes

### Why Mocking?
Public APIs may block automated requests (e.g. returning `403 Forbidden`).
To ensure **stable, repeatable, and CI-friendly tests**, API behavior is mocked.

This reflects **industry best practices** in QA automation.

---

## ▶️ How to Run Tests

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
2️⃣ Run tests
```bash

pytest
```
✅ Key QA Skills Demonstrated
Test design techniques

API testing fundamentals

Automation best practices

Separation of test logic and test data

QA documentation standards

Git-based workflow

🚀 Future Improvements
API schema validation

HTML test reports

Performance testing (Locust)

CI integration (GitHub Actions)