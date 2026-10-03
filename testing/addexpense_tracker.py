from expenseTracker import ExpenseTracker
from expense import Expense


tracker = ExpenseTracker()


# ============================================================
# VALID ADD
# ============================================================

response = tracker.add_expense(
    1,
    250.50,
    " Food ",
    "UPI",
    " Dinner "
)

assert response.data is not None
assert isinstance(response.data, Expense)

assert response.data.expense_id == 1
assert response.data.amount == 250.50
assert response.data.category == "Food"
assert response.data.payment_method == "upi"
assert response.data.description == "Dinner"

assert 1 in tracker.expenses

print("TEST 1 PASSED - Valid expense added")


# ============================================================
# SECOND VALID EXPENSE
# ============================================================

response = tracker.add_expense(
    2,
    100,
    "Travel",
    "cash",
    "Bus ticket"
)

assert isinstance(response.data, Expense)
assert response.data.expense_id == 2
assert 2 in tracker.expenses

print("TEST 2 PASSED - Second expense added")


# ============================================================
# DUPLICATE ID
# ============================================================

response = tracker.add_expense(
    1,
    500,
    "Food",
    "upi"
)

assert response.data is None
assert "already exists" in response.message.lower()

# Original expense must remain unchanged
assert tracker.expenses[1].amount == 250.50
assert tracker.expenses[1].category == "Food"

print("TEST 3 PASSED - Duplicate ID rejected")


# ============================================================
# INVALID EXPENSE ID
# ============================================================

response = tracker.add_expense(
    "3",
    100,
    "Food",
    "upi"
)

assert response.data is None
assert "3" not in tracker.expenses

print("TEST 4 PASSED - String ID rejected")


# ============================================================
# BOOLEAN EXPENSE ID
# ============================================================

before_count = len(tracker.expenses)

response = tracker.add_expense(
    True,
    100,
    "Food",
    "upi"
)

after_count = len(tracker.expenses)

assert response.data is None
assert before_count == after_count

print("TEST 5 PASSED - Boolean ID rejected")


# ============================================================
# ZERO ID
# ============================================================

response = tracker.add_expense(
    0,
    100,
    "Food",
    "upi"
)

assert response.data is None
assert 0 not in tracker.expenses

print("TEST 6 PASSED - Zero ID rejected")


# ============================================================
# NEGATIVE ID
# ============================================================

response = tracker.add_expense(
    -5,
    100,
    "Food",
    "upi"
)

assert response.data is None
assert -5 not in tracker.expenses

print("TEST 7 PASSED - Negative ID rejected")


# ============================================================
# INVALID AMOUNT TYPE
# ============================================================

response = tracker.add_expense(
    3,
    "500",
    "Food",
    "upi"
)

assert response.data is None
assert 3 not in tracker.expenses

print("TEST 8 PASSED - String amount rejected")


# ============================================================
# ZERO AMOUNT
# ============================================================

response = tracker.add_expense(
    3,
    0,
    "Food",
    "upi"
)

assert response.data is None
assert 3 not in tracker.expenses

print("TEST 9 PASSED - Zero amount rejected")


# ============================================================
# NEGATIVE AMOUNT
# ============================================================

response = tracker.add_expense(
    3,
    -100,
    "Food",
    "upi"
)

assert response.data is None
assert 3 not in tracker.expenses

print("TEST 10 PASSED - Negative amount rejected")


# ============================================================
# INVALID CATEGORY
# ============================================================

response = tracker.add_expense(
    3,
    100,
    "",
    "upi"
)

assert response.data is None
assert 3 not in tracker.expenses

print("TEST 11 PASSED - Empty category rejected")


# ============================================================
# WHITESPACE-ONLY CATEGORY
# ============================================================

response = tracker.add_expense(
    3,
    100,
    "     ",
    "upi"
)

assert response.data is None
assert 3 not in tracker.expenses

print("TEST 12 PASSED - Whitespace category rejected")


# ============================================================
# INVALID DESCRIPTION
# ============================================================

response = tracker.add_expense(
    3,
    100,
    "Food",
    "upi",
    123
)

assert response.data is None
assert 3 not in tracker.expenses

print("TEST 13 PASSED - Invalid description rejected")


# ============================================================
# INVALID PAYMENT METHOD
# ============================================================

response = tracker.add_expense(
    3,
    100,
    "Food",
    "bitcoin"
)

assert response.data is None
assert 3 not in tracker.expenses

print("TEST 14 PASSED - Invalid payment method rejected")


# ============================================================
# PAYMENT METHOD NORMALIZATION
# ============================================================

response = tracker.add_expense(
    3,
    100,
    "Food",
    "   UPI   "
)

assert isinstance(response.data, Expense)
assert response.data.payment_method == "upi"
assert 3 in tracker.expenses

print("TEST 15 PASSED - Payment method normalized")


# ============================================================
# CATEGORY NORMALIZATION
# ============================================================

response = tracker.add_expense(
    4,
    100,
    "   Groceries   ",
    "cash"
)

assert isinstance(response.data, Expense)
assert response.data.category == "Groceries"
assert 4 in tracker.expenses

print("TEST 16 PASSED - Category normalized")


# ============================================================
# DESCRIPTION NORMALIZATION
# ============================================================

response = tracker.add_expense(
    5,
    100,
    "Food",
    "upi",
    "   Dinner   "
)

assert isinstance(response.data, Expense)
assert response.data.description == "Dinner"
assert 5 in tracker.expenses

print("TEST 17 PASSED - Description normalized")


# ============================================================
# INVALID EXPENSE MUST NOT ENTER TRACKER
# ============================================================

before_count = len(tracker.expenses)

response = tracker.add_expense(
    6,
    -500,
    "Food",
    "upi"
)

after_count = len(tracker.expenses)

assert response.data is None
assert before_count == after_count
assert 6 not in tracker.expenses

print("TEST 18 PASSED - Invalid expense not stored")


# ============================================================
# FINAL STATE
# ============================================================

print("\n" + "=" * 70)
print("FINAL TRACKER STATE")
print("=" * 70)

for expense_id, expense in tracker.expenses.items():
    print(f"ID: {expense_id}")
    print(expense)


print("=" * 70)
print("ALL ADD EXPENSE INTEGRATION TESTS PASSED")
print("=" * 70)