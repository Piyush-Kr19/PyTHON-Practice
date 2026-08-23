"""
============================================================
                    MATCH - CASE
============================================================

match-case is Python's pattern matching syntax.

It is useful when one value needs to be compared
against several possible patterns.

Available in Python 3.10+
============================================================
"""


# ============================================================
# 1. BASIC MATCH-CASE
# ============================================================

day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Other day")


# ⭐ "_" is the default/wildcard case.
# Similar to "else" in an if-elif-else chain.


# ============================================================
# 2. MATCHING STRINGS
# ============================================================

command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "restart":
        print("Restarting...")
    case _:
        print("Unknown command")


# ============================================================
# 3. MULTIPLE VALUES IN ONE CASE
# ============================================================

day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")


# ⭐ "|" means OR in a pattern.


# ============================================================
# 4. MATCH-CASE WITH USER INPUT
# ============================================================

choice = input("Enter 1, 2 or 3: ")

match choice:
    case "1":
        print("You selected Add")
    case "2":
        print("You selected Delete")
    case "3":
        print("You selected Exit")
    case _:
        print("Invalid choice")


# ============================================================
# 5. MATCHING WITH CONDITIONS (GUARDS)
# ============================================================

age = 20

match age:
    case n if n < 18:
        print("Minor")
    case n if n >= 18:
        print("Adult")


# The "if" after the pattern is called a guard.


# ============================================================
# 6. WHEN TO USE MATCH vs IF
# ============================================================

"""
Use match-case when:

    One value
        ↓
    many possible patterns

Example:
    menu choices
    commands
    status values
    days/months

Use if-elif when:

    Conditions involve ranges,
    calculations, or complex logic.
"""


# Example: if is usually clearer here:

marks = 85

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
else:
    print("B")


# ============================================================
# 7. COMMON MISTAKES ⚠️
# ============================================================

# ❌ Forgetting the wildcard/default case:

# match choice:
#     case "1":
#         print("One")

# It's often useful to include:

# case _:
#     print("Invalid choice")


# ❌ Remember:
#
# match is available from Python 3.10 onward.


# ============================================================
# 8. MINI PRACTICE 🧠
# ============================================================

"""
Try these:

1. Create a calculator using:
    +
    -
    *
    /

2. Create a menu:
    1 -> Start
    2 -> Settings
    3 -> Exit

3. Match the days of the week and print whether
    they are weekdays or weekends.

4. Create a simple traffic-light program:
    red
    yellow
    green
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
match value:
    case pattern:
        code

    case _:
        default code

Remember:

    _           -> wildcard/default
    |           -> OR pattern
    if          -> guard condition

Use match-case for clear value/pattern matching.
Use if-elif for more general conditions.
"""