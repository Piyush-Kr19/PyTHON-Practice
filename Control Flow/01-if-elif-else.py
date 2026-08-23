"""
============================================================
                    IF / ELIF / ELSE
============================================================

Used to make decisions in a Python program.

    if      -> first condition
    elif    -> another condition
    else    -> runs when no condition is True
============================================================
"""


# ============================================================
# 1. BASIC IF
# ============================================================

age = 20

if age >= 18:
    print("Adult")


# ============================================================
# 2. IF / ELSE
# ============================================================

age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")


# ============================================================
# 3. IF / ELIF / ELSE
# ============================================================

marks = 82

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
else:
    grade = "C"

print(grade)


# ⭐ Python checks conditions from TOP to BOTTOM.
# Once a condition is True, the remaining elif/else blocks
# are skipped.


# ============================================================
# 4. COMBINING CONDITIONS
# ============================================================

age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")
else:
    print("Cannot drive")


# ============================================================
# 5. CHAINED COMPARISON ⭐
# ============================================================

age = 25

if 18 <= age <= 60:
    print("Valid age")


# Instead of:
#
# if age >= 18 and age <= 60:


# ============================================================
# 6. MEMBERSHIP IN CONDITIONS
# ============================================================

day = "Saturday"

if day in ("Saturday", "Sunday"):
    print("Weekend")
else:
    print("Weekday")


# ============================================================
# 7. TRUTHY / FALSY VALUES
# ============================================================

username = ""

if username:
    print("Username entered")
else:
    print("Username is empty")


# Common falsy values:
#
# False
# None
# 0
# ""
# []
# {}
# set()


# ============================================================
# 8. NESTED IF
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


# ⭐ Tip:
# Avoid deeply nested if statements when a simpler
# condition can do the same job.


# ============================================================
# 9. TERNARY / CONDITIONAL EXPRESSION ⭐
# ============================================================

age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)


# Use this for simple conditions.
# Don't use it when the logic becomes difficult to read.


# ============================================================
# 10. PRACTICAL EXAMPLE — LOGIN
# ============================================================

username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Login successful")
else:
    print("Invalid credentials")


# ============================================================
# 11. PRACTICAL EXAMPLE — EVEN / ODD
# ============================================================

number = 17

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# ============================================================
# 12. COMMON MISTAKES ⚠️
# ============================================================

# ❌ Missing colon:

# if age >= 18
#     print("Adult")


# ❌ Using = instead of ==:

# if age = 18:
#     print("Adult")

# =  -> assignment
# == -> comparison


# ❌ Incorrect indentation:

# if age >= 18:
# print("Adult")

# Python uses indentation to define the block.


# ============================================================
# 13. QUICK PRACTICE 🧠
# ============================================================

"""
Try these:

1. Check whether a number is positive, negative, or zero.

2. Check whether a person is eligible to vote.

3. Find the largest of two numbers.

4. Create a simple grade calculator.

5. Check whether a year is a leap year.

6. Ask for a username and password and create
   a basic login check.

7. Check whether a number is divisible by both
   3 and 5.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
if       -> checks a condition
elif     -> checks another condition
else     -> fallback

and      -> all conditions must be True
or       -> at least one must be True
not      -> reverses a condition

in       -> membership check

Remember:
    =   assignment
    ==  comparison

Python uses indentation to define code blocks.
"""