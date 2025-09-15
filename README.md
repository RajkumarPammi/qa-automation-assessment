# QA-automation-assessment #

# 📌 Objective

Automate the following user flows on Magento Test Website:

Sign Up – Create a new account.

Login – Login with the same account.

Sign Out – Logout successfully.

Change Password – Verified via Forgot Password (since Magento does not show a direct Change Password on login).


# 📂 Repository Structure

```bash
qa-automation-assessment/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── change_password_page.py
│   ├── dashboard_page.py
│   ├── login_page.py
│   └── signup_page.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_user_flow.py
├── reports/
│   └── report.html
├── screenshots/
│   ├── step1.png
│   └── step2.png
├── .gitignore
├── README.md
└── requirements.txt

# ⚙️ Setup Instructions

1️⃣ Clone Repository
git clone https://github.com/RajkumarPammi/qa-automation-assessment.git
cd qa-automation-assessment

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Tests
pytest -v tests/test_user_flow.py --html=report.html --self-contained-html

# ✅ Deliverables

Test Cases – Documented in Excel (test_cases.xlsx or similar).

Automation Code – Selenium + Pytest framework.

Design Pattern – Page Object Model (POM).

Reports – Generated using pytest-html.

Proof of Execution – Screenshots in /screenshots/ and report.html.

# 🛠️ Tools & Stack

Language: Python 3.11

Framework: Selenium + Pytest

Design Pattern: Page Object Model (POM)

Reports: pytest-html

Version Control: Git + GitHub





