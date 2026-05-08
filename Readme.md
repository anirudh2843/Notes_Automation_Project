# Notes App Automation Framework

A Hybrid Enterprise Automation Framework built using Selenium, Pytest, Python, API Testing, Jenkins, Selenium Grid, Agentic Automation, and MCP (AI-Assisted Automation).

---

# Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Requests
- Allure Reports
- Jenkins
- Selenium Grid
- Pytest-xdist
- MCP Layer

---

# 📂 Project Structure

```text
Notes_App_Automation_Framework/
│
├── agentic/
├── api/
├── config/
├── mcp/
├── pages/
├── tests/
├── utils/
├── logs/
├── screenshots/
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

# ✅ Features Implemented

## UI Automation

- Login automation
- Notes CRUD operations
- Negative validations
- Reusable BasePage
- Explicit waits
- Screenshot capture

---

## API Automation

- Login API testing
- Notes API validation
- Response validation
- Response time validation

---

## Hybrid UI + API Testing

- Create note using UI
- Validate using API
- Delete using API
- Verify deletion in UI

---

# Parallel Execution

Implemented using:

pytest -n 2

---

### Supports:

- Faster execution
- Multi-worker execution
- Grid-compatible runs

---

# Selenium Grid Integration

Framework supports:

- Distributed execution
- Remote browser execution
- Parallel browser testing

---

# Jenkins CI/CD

Integrated Jenkins Pipeline with:

- Source checkout
- Dependency installation
- Parallel test execution
- Allure report publishing
- Screenshot & logs archival

---

# Agentic Automation

Implemented modern automation recovery mechanisms.

## Features

- Intelligent Wait System
- Retry Engine
- Self-Healing Locators
- AI Decision-Based Retry Logic

---

# MCP (Model Context Protocol)

Implemented AI-assisted automation enhancements.

## MCP Features

- LLM-powered test data generation
- LLM-assisted failure analysis
- LLM locator improvement suggestions

---

# Reporting

Implemented:

- Allure Reports
- Logs
- Failure screenshots
- Retry logs
- Healing logs

Generate report using:

```bash
allure serve allure-results
```
