Automation Assignment - Playwright (Python)

This project contains automation scripts for UI and API testing based on Page Object Model (POM) using Playwright with Python and Pytest.

Tech Stack:
| Category             | Tool                    |
| -------------------- | ----------------------- |
| Programming Language | Python                  |
| Automation Tool      | Playwright              |
| Test Runner          | Pytest                  |
| Design Pattern       | Page Object Model (POM) |
| API Testing          | Requests Library        |

Test Coverage:
| Use Case                     | Type | Status      |
| ---------------------------- | ---- | ----------- |
| Message Box Task Creation    | UI   | ✔ Completed |
| Form With Text & File Upload | UI   | ✔ Completed |
| Learning Instance Creation   | API  | ✔ Completed |

Use Case 1: Message Box Task (UI Automation)

Automates:

Login

Navigate to Automation → Create Task Bot

Add Message Box Action

Validate UI elements & save

Assertions:

Visibility checks

Functional flow validation

Test File:
tests/test_messagebox_task.py


Use Case 2: Form Upload Flow (UI Automation)

Automates:

Login

Create Form

Drag Textbox & File Upload component

Enter text & upload file

Save and validate upload success

Assertions:

UI element visibility

File upload validation

Functional correctness

Test File:
tests/test_form_upload.py

Use Case 3: Learning Instance API (API Automation)

Validates API:

Login and token authentication

Create Learning Instance

Response status, schema & correctness

Assertions:

HTTP codes (200/201)

Response Body Validation (id, name, status)

Test File:
api/test_learning_instance_api.py


Project Structure:
├── pages
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── taskbot_page.py
│   ├── message_box_page.py
│   ├── form_page.py
│
├── tests
│   ├── test_messagebox_task.py
│   ├── test_form_upload.py
│
├── api
│   ├── test_learning_instance_api.py
│
├── utils
│   ├── config.py
│
├── conftest.py
├── requirements.txt
└── README.md

Setup & Installation
1️ Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

2️ Install Dependencies
pip install -r requirements.txt
playwright install


Test Execution Commands
 Run all tests
pytest -q

 UI tests only
pytest -m ui -q

 API tests only
pytest -m api -q

Playwright Options

To run without opening browser:

pytest -q --headed


To run with UI:

pytest -q --headed
