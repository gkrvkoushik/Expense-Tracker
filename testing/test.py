from expense import Expense


def test(title, func):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

    try:
        result = func()

        if isinstance(result, Expense):
            print("PASS")
            print(result)
        else:
            print("PASS")
            print(result)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


# ============================================================
# VALID EXPENSE
# ============================================================

test(
    "TEST 1 - Valid expense",
    lambda: Expense(
        1,
        250.50,
        " Food ",
        "UPI",
        " Dinner "
    )
)


# ============================================================
# EXPENSE ID
# ============================================================

test(
    "TEST 2 - Missing expense ID",
    lambda: Expense(
        None,
        100,
        "Food",
        "upi"
    )
)

test(
    "TEST 3 - String expense ID",
    lambda: Expense(
        "1",
        100,
        "Food",
        "upi"
    )
)

test(
    "TEST 4 - Zero expense ID",
    lambda: Expense(
        0,
        100,
        "Food",
        "upi"
    )
)

test(
    "TEST 5 - Negative expense ID",
    lambda: Expense(
        -1,
        100,
        "Food",
        "upi"
    )
)

test(
    "TEST 6 - Boolean expense ID",
    lambda: Expense(
        True,
        100,
        "Food",
        "upi"
    )
)


# ============================================================
# AMOUNT
# ============================================================

test(
    "TEST 7 - Missing amount",
    lambda: Expense(
        1,
        None,
        "Food",
        "upi"
    )
)

test(
    "TEST 8 - String amount",
    lambda: Expense(
        1,
        "100",
        "Food",
        "upi"
    )
)

test(
    "TEST 9 - Zero amount",
    lambda: Expense(
        1,
        0,
        "Food",
        "upi"
    )
)

test(
    "TEST 10 - Negative amount",
    lambda: Expense(
        1,
        -100,
        "Food",
        "upi"
    )
)

test(
    "TEST 11 - Integer amount",
    lambda: Expense(
        1,
        100,
        "Food",
        "upi"
    )
)

test(
    "TEST 12 - Float amount",
    lambda: Expense(
        1,
        100.50,
        "Food",
        "upi"
    )
)


# ============================================================
# CATEGORY
# ============================================================

test(
    "TEST 13 - Valid category with whitespace",
    lambda: Expense(
        1,
        100,
        "   Food   ",
        "upi"
    )
)

test(
    "TEST 14 - Empty category",
    lambda: Expense(
        1,
        100,
        "",
        "upi"
    )
)

test(
    "TEST 15 - Whitespace-only category",
    lambda: Expense(
        1,
        100,
        "     ",
        "upi"
    )
)

test(
    "TEST 16 - Non-string category",
    lambda: Expense(
        1,
        100,
        123,
        "upi"
    )
)


# ============================================================
# DESCRIPTION
# ============================================================

test(
    "TEST 17 - Description omitted",
    lambda: Expense(
        1,
        100,
        "Food",
        "upi"
    )
)

test(
    "TEST 18 - Description whitespace stripping",
    lambda: Expense(
        1,
        100,
        "Food",
        "upi",
        "   Dinner   "
    )
)

test(
    "TEST 19 - Empty description",
    lambda: Expense(
        1,
        100,
        "Food",
        "upi",
        ""
    )
)

test(
    "TEST 20 - None description",
    lambda: Expense(
        1,
        100,
        "Food",
        "upi",
        None
    )
)

test(
    "TEST 21 - Invalid description type",
    lambda: Expense(
        1,
        100,
        "Food",
        "upi",
        123
    )
)


# ============================================================
# PAYMENT METHOD
# ============================================================

test(
    "TEST 22 - UPI uppercase",
    lambda: Expense(
        1,
        100,
        "Food",
        "UPI"
    )
)

test(
    "TEST 23 - Payment method whitespace",
    lambda: Expense(
        1,
        100,
        "Food",
        "   upi   "
    )
)

test(
    "TEST 24 - Netbanking",
    lambda: Expense(
        1,
        100,
        "Food",
        "netbanking"
    )
)

test(
    "TEST 25 - Cash",
    lambda: Expense(
        1,
        100,
        "Food",
        "cash"
    )
)

test(
    "TEST 26 - Invalid payment method",
    lambda: Expense(
        1,
        100,
        "Food",
        "bitcoin"
    )
)

test(
    "TEST 27 - Empty payment method",
    lambda: Expense(
        1,
        100,
        "Food",
        ""
    )
)

test(
    "TEST 28 - Non-string payment method",
    lambda: Expense(
        1,
        100,
        "Food",
        123
    )
)


# ============================================================
# DATE
# ============================================================

test(
    "TEST 29 - Automatic date generation",
    lambda: Expense(
        1,
        100,
        "Food",
        "upi"
    )
)