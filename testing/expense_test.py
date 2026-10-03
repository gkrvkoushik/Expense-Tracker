from expense import Expense


# ============================================================
# VALID EXPENSE
# ============================================================

expense = Expense(
    1,
    250.50,
    " Food ",
    "UPI",
    " Dinner "
)

assert expense.expense_id == 1
assert expense.amount == 250.50
assert expense.category == "Food"
assert expense.description == "Dinner"
assert expense.payment_method == "upi"
assert expense.date_paid is not None

print("TEST 1 PASSED - Valid expense")


# ============================================================
# EXPENSE ID
# ============================================================

try:
    Expense(None, 100, "Food", "upi")
    assert False
except ValueError:
    pass

print("TEST 2 PASSED - Missing expense ID")


try:
    Expense("1", 100, "Food", "upi")
    assert False
except TypeError:
    pass

print("TEST 3 PASSED - String expense ID")


try:
    Expense(0, 100, "Food", "upi")
    assert False
except ValueError:
    pass

print("TEST 4 PASSED - Zero expense ID")


try:
    Expense(-1, 100, "Food", "upi")
    assert False
except ValueError:
    pass

print("TEST 5 PASSED - Negative expense ID")


try:
    Expense(True, 100, "Food", "upi")
    assert False
except TypeError:
    pass

print("TEST 6 PASSED - Boolean expense ID")


# ============================================================
# AMOUNT
# ============================================================

try:
    Expense(1, None, "Food", "upi")
    assert False
except ValueError:
    pass

print("TEST 7 PASSED - Missing amount")


try:
    Expense(1, "100", "Food", "upi")
    assert False
except TypeError:
    pass

print("TEST 8 PASSED - String amount")


try:
    Expense(1, 0, "Food", "upi")
    assert False
except ValueError:
    pass

print("TEST 9 PASSED - Zero amount")


try:
    Expense(1, -100, "Food", "upi")
    assert False
except ValueError:
    pass

print("TEST 10 PASSED - Negative amount")


expense = Expense(1, 100, "Food", "upi")
assert expense.amount == 100

print("TEST 11 PASSED - Integer amount")


expense = Expense(1, 100.50, "Food", "upi")
assert expense.amount == 100.50

print("TEST 12 PASSED - Float amount")


# ============================================================
# CATEGORY
# ============================================================

expense = Expense(1, 100, "   Food   ", "upi")
assert expense.category == "Food"

print("TEST 13 PASSED - Category whitespace stripping")


try:
    Expense(1, 100, "", "upi")
    assert False
except ValueError:
    pass

print("TEST 14 PASSED - Empty category")


try:
    Expense(1, 100, "     ", "upi")
    assert False
except ValueError:
    pass

print("TEST 15 PASSED - Whitespace-only category")


try:
    Expense(1, 100, 123, "upi")
    assert False
except TypeError:
    pass

print("TEST 16 PASSED - Non-string category")


# ============================================================
# DESCRIPTION
# ============================================================

expense = Expense(1, 100, "Food", "upi")
assert expense.description == ""

print("TEST 17 PASSED - Description omitted")


expense = Expense(
    1,
    100,
    "Food",
    "upi",
    "   Dinner   "
)

assert expense.description == "Dinner"

print("TEST 18 PASSED - Description whitespace stripping")


expense = Expense(
    1,
    100,
    "Food",
    "upi",
    ""
)

assert expense.description == ""

print("TEST 19 PASSED - Empty description")


expense = Expense(
    1,
    100,
    "Food",
    "upi",
    None
)

assert expense.description == ""

print("TEST 20 PASSED - None description")


try:
    Expense(1, 100, "Food", "upi", 123)
    assert False
except TypeError:
    pass

print("TEST 21 PASSED - Invalid description type")


# ============================================================
# PAYMENT METHOD
# ============================================================

expense = Expense(1, 100, "Food", "UPI")
assert expense.payment_method == "upi"

print("TEST 22 PASSED - Uppercase UPI normalization")


expense = Expense(1, 100, "Food", "   upi   ")
assert expense.payment_method == "upi"

print("TEST 23 PASSED - Payment method whitespace stripping")


expense = Expense(1, 100, "Food", "NETBANKING")
assert expense.payment_method == "netbanking"

print("TEST 24 PASSED - Netbanking normalization")


expense = Expense(1, 100, "Food", "cash")
assert expense.payment_method == "cash"

print("TEST 25 PASSED - Cash payment method")


try:
    Expense(1, 100, "Food", "bitcoin")
    assert False
except ValueError:
    pass

print("TEST 26 PASSED - Invalid payment method")


try:
    Expense(1, 100, "Food", "")
    assert False
except ValueError:
    pass

print("TEST 27 PASSED - Empty payment method")


try:
    Expense(1, 100, "Food", 123)
    assert False
except TypeError:
    pass

print("TEST 28 PASSED - Non-string payment method")


# ============================================================
# DATE
# ============================================================

expense = Expense(1, 100, "Food", "upi")

assert expense.date_paid is not None
assert len(expense.date_paid) == 19
assert expense.date_paid[4] == "-"
assert expense.date_paid[7] == "-"
assert expense.date_paid[10] == "T"
assert expense.date_paid[13] == ":"
assert expense.date_paid[16] == ":"

print("TEST 29 PASSED - Automatic timestamp generation")


print("\n" + "=" * 70)
print("ALL EXPENSE TESTS PASSED")
print("=" * 70)