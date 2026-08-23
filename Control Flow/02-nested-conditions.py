"""
============================================================
                 NESTED CONDITIONS
============================================================

A nested condition is an if statement inside another
if/elif/else block.

Use nesting when the second decision depends on
the first decision.
============================================================
"""


# ============================================================
# 1. BASIC NESTED IF
# ============================================================

age = 20
has_id = True

if age >= 18:

    if has_id:
        print("Entry allowed")
    else:
        print("ID required")

else:
    print("Underage")


# ============================================================
# 2. NESTED IF WITH MULTIPLE CONDITIONS
# ============================================================

username = "admin"
password = "python123"

if username == "admin":

    if password == "python123":
        print("Login successful")
    else:
        print("Wrong password")

else:
    print("Unknown user")


# ============================================================
# 3. NESTED IF + ELIF
# ============================================================

marks = 85

if marks >= 0:

    if marks >= 90:
        print("A+")

    elif marks >= 80:
        print("A")

    elif marks >= 70:
        print("B")

    else:
        print("C")

else:
    print("Invalid marks")


# ============================================================
# 4. WHEN TO AVOID NESTING ⭐
# ============================================================

age = 25
has_license = True

# Instead of:

if age >= 18:
    if has_license:
        print("Can drive")


# You can often simplify it:

if age >= 18 and has_license:
    print("Can drive")


# ⭐ Teacher Tip:
# If two conditions are independent and both must be True,
# combining them with "and" is often cleaner.


# ============================================================
# 5. EARLY DECISION PATTERN
# ============================================================

age = 15

if age < 18:
    print("Not eligible")
else:
    print("Eligible")


# Keep the main path simple instead of creating
# unnecessary levels of nesting.


# ============================================================
# 6. PRACTICAL EXAMPLE — ATM
# ============================================================

balance = 5000
withdraw = 3000

if withdraw > 0:

    if withdraw <= balance:
        balance -= withdraw
        print("Withdrawal successful")
        print("Remaining:", balance)

    else:
        print("Insufficient balance")

else:
    print("Invalid amount")


# ============================================================
# 7. PRACTICAL EXAMPLE — DISCOUNT
# ============================================================

amount = 2500
is_member = True

if amount >= 1000:

    if is_member:
        discount = 20
    else:
        discount = 10

else:
    discount = 0

print(f"Discount: {discount}%")


# ============================================================
# 8. COMMON MISTAKE ⚠️
# ============================================================

# ❌ Too much nesting:

# if condition1:
#     if condition2:
#         if condition3:
#             if condition4:
#                 print("Something")


# ⭐ If your code keeps going deeper,
# stop and ask whether the logic can be simplified.


# ============================================================
# 9. QUICK PRACTICE 🧠
# ============================================================

"""
Try these:

1. Create a program that checks:
    age >= 18
    has ID
    and decides whether someone can enter.

2. Create a login system with:
    username
    password
    account status

3. Create an ATM withdrawal program.

4. Create a marks program that first checks whether
    the marks are valid, then assigns a grade.

5. Rewrite one nested condition using "and" or "or"
    if possible.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
1. Nested conditions are if statements inside other
    conditions.

2. Use nesting when one decision depends on another.

3. Don't nest unnecessarily.

4. "and" can often replace simple nested if statements.

5. Keep indentation clean and consistent.

6. If nesting becomes too deep, rethink the logic.
"""