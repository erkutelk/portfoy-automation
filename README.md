# Automation Tests Portfoy
**This document is in English. For the Turkish version, please click [README_TR.md](README_tr.md).**

This project contains web automation tests implemented using **Python** and the **pytest** framework. The tests cover functional testing for income, expense, invoices, and customer pages.



## Requirements

* Python 3.10+
* Selenium
* Pytest
* WebDriver (ChromeDriver or preferred browser)
* Logging module



## Test Structure

The project is organized by modules, each with its own test classes and functions:

### 1. Income Tests

**File:** `tests/test_income.py`

* `test_fill_income_form`: Validates input fields when adding income.
* `test_update_income`: Updates an existing income entry.
* `test_badge_check`: Verifies total income/expense values and table data.
* `test_added_income_appears_in_list`: Checks that newly added income appears correctly in the list.

**Parametrized Test Example:**

```python
@pytest.mark.parametrize(
    'income_amount,description,dropdown,error_message', [
        ('','baaa','1','Please enter income amount'),
        ('aaa','','1','Please enter description'),
        (' ',' ','1','Please enter a value'),
        ('1500','Test income','1',''),
        ('','',0,'Please enter valid values')
    ]
)
```

---

### 2. Expense Tests

**File:** `tests/test_expenses.py`

* `test_add_expense`: Validates the expense addition form.
* `test_update_expense`: Updates existing expense entries.
* `test_badge_check_operations`: Checks total expense and pending expense values on the page.

---

### 3. Invoice Tests

**File:** `tests/test_invoices.py`

* `test_fill_invoice_form`: Tests adding invoices with different inputs.
* `test_update_invoice`: Verifies that added invoices are updated correctly.
* `test_upcoming_payments`: Ensures invoices with 3 days remaining are listed correctly.
* `test_amount_accuracy`: Checks that the total payable matches the table value.

---

### 4. Customer Tests

**File:** `tests/test_customers.py`

* `test_create_customer`: Adds new customers and validates input.
* `test_added_customer_appears_in_list`: Ensures the newly added customer is visible in the list.
* `test_customer_counts_are_correct`: Verifies active and inactive customer counts.
* `test_delete_customer`: Checks that deleted customers are removed correctly.
* `test_update_customer`: Updates customer information.

---

### 5. Reports Tests

**File:** `tests/test_reports.py`

* `test_income_expense_reports_match`: Compares income and expense data with monthly report page values.

---



1. Run all tests:

```bash
pytest -v --html=report.html
```

2. Run tests with specific markers:

```bash
pytest -m update
pytest -m name
pytest -m delete
```

---

## Logging

During tests, all successful and failed actions are logged. Example:

```
🟩 Submitted data: dict_items([('Income Amount', '1500'), ('Description', 'Test income'), ('Dropdown', '1')])
🟩 Expense addition test passed
```

---

## Notes

* Each test can run independently. The local server URL is `http://127.0.0.1:8000`.
* Test data is provided via the **parametrize** decorator, allowing easy testing of multiple scenarios.

---
