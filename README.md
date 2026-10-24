# Two Python Full Stack Mini Projects

This folder contains two mini projects in one Django site so both can be demonstrated from one server.

## Technologies
- Python: backend language
- Django: models, forms, views, URLs and database operations
- HTML: page structure
- CSS: custom styling
- Bootstrap 5: responsive layout
- SQLite: database (works without installing MySQL)
- VS Code and Git/GitHub: development tools

## Project 1 — Personal Expense Tracker (SpendWise)
Features: add/edit/delete income and expense entries, categories, search, total income, total expenses and balance calculation.
URL: `http://127.0.0.1:8000/`

## Project 2 — Library Management System (BookNest)
Features: add/edit/delete books, search catalogue, issue books to students, track available copies and due dates, mark returned.
URL: `http://127.0.0.1:8000/library/`

## Folder structure
```text
python_fullstack_mini_projects/
├── manage.py
├── requirements.txt
├── config/                 # Django settings and main URLs
├── expenses/               # Project 1 app: models, forms, views, URLs
├── library/                # Project 2 app: books, loans, forms, views, URLs
├── templates/
│   ├── base.html
│   ├── expenses/dashboard.html
│   ├── library/list.html
│   └── shared/             # reusable form and delete templates
└── static/style.css
```

## Windows PowerShell setup
Extract the ZIP. Open VS Code on this folder, then Terminal > New Terminal and run each command:

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py manage.py makemigrations expenses library
py manage.py migrate
py manage.py runserver
```
Open `http://127.0.0.1:8000/` for Expense Tracker and `http://127.0.0.1:8000/library/` for Library Management.

If PowerShell blocks activation, open Command Prompt and run:
` .\.venv\Scripts\activate.bat `

Optional admin: `py manage.py createsuperuser`, then visit `http://127.0.0.1:8000/admin/`.

## Example test data
Expense Tracker:
- Title: Monthly stipend
- Type: Income
- Category: Salary
- Amount: 5000
- Date: choose today's date

Then add an expense:
- Title: Bus travel
- Type: Expense
- Category: Travel
- Amount: 250
- Date: choose today's date

Expected balance from those two entries: ₹4750.

Library:
- Title: Python Basics
- Author: A. Kumar
- ISBN: PY-1001
- Category: Programming
- Total copies: 3
- Available copies: 3

Then click Issue and fill a student name, roll number and due date. The available count decreases by one. Click Mark returned to increase it again.

## Notes
These are educational portfolio projects, not production-ready systems. They do not currently require user login. Before using real data or deploying, add authentication/permissions, configure production secrets and DEBUG settings, and test all workflows. SQLite is used by default; MySQL can be configured later.
