# ExpenseTracker

A Python library for managing personal expenses with validation and CRUD operations.

## Project Structure

```
ExpenseTracker/
├── expense.py          # Expense model with validation
├── expenseTracker.py   # CRUD operations
├── response.py         # Response wrapper
├── main.py             # Entry point
└── testing/            # Test scripts
```

## Classes

### `Expense`
Represents a single expense record.

**Constructor:** `Expense(expense_id, amount, category, payment_method, description="")`

| Field | Type | Rules |
|---|---|---|
| `expense_id` | `int` | Required, positive, non-boolean |
| `amount` | `int` or `float` | Required, positive |
| `category` | `str` | Required, non-empty, stripped |
| `payment_method` | `str` | Required — `upi`, `netbanking`, or `cash` (case-insensitive) |
| `description` | `str` | Optional, stripped |
| `date_paid` | `str` | Auto-set to current timestamp (`YYYY-MM-DDTHH:MM:SS`) |

### `ExpenseTracker`
Manages a collection of expenses.

| Method | Description |
|---|---|
| `add_expense(expense_id, amount, category, payment_method, description="")` | Add a new expense |
| `get_expense(expense_id)` | Retrieve an expense by ID |
| `get_all_expenses()` | Retrieve all expenses |
| `update_expense(**kwargs)` | Update fields of an existing expense (requires `expense_id`) |
| `delete_expense(expense_id)` | Delete an expense by ID |

All methods return a `Response(message, data)` object.

## Usage

```python
from expenseTracker import ExpenseTracker

tracker = ExpenseTracker()

# Add
tracker.add_expense(1, 250.50, "Food", "upi", "Dinner")

# Get
tracker.get_expense(1)

# Update
tracker.update_expense(expense_id=1, amount=300.00, description="Lunch")

# Delete
tracker.delete_expense(1)

# Get all
tracker.get_all_expenses()
```

## Requirements

- Python >= 3.12

## Setup

```bash
# Using uv
uv sync
```
