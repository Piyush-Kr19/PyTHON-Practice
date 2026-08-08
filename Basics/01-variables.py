"""
============================================================
                    PYTHON VARIABLES
============================================================

A variable is a name used to refer to a value/object.

Python does NOT require you to declare the type of a variable.

Example:
    name = "Piyush"
    age = 20

Python automatically determines the type.
============================================================
"""


# ============================================================
# 1. CREATING VARIABLES
# ============================================================

name = "Piyush"
age = 20
height = 5.9
is_student = True

print(name)
print(age)
print(height)
print(is_student)


# ============================================================
# 2. CHECKING THE TYPE
# ============================================================

print(type(name))        # str
print(type(age))         # int
print(type(height))      # float
print(type(is_student))  # bool


# ============================================================
# 3. PYTHON IS DYNAMICALLY TYPED
# ============================================================

# A variable can refer to different types of objects
# during the execution of a program.

value = 100
print(value)
print(type(value))

value = "Python"
print(value)
print(type(value))

# ⭐ Teacher Tip:
# The variable itself doesn't have a fixed type.
# The object/value that it refers to has a type.


# ============================================================
# 4. MULTIPLE VARIABLES
# ============================================================

x = 10
y = 20
z = 30

print(x, y, z)


# ============================================================
# 5. MULTIPLE ASSIGNMENT
# ============================================================

a, b, c = 10, 20, 30

print(a)
print(b)
print(c)


# ============================================================
# 6. ASSIGNING THE SAME VALUE
# ============================================================

x = y = z = 100

print(x)
print(y)
print(z)


# ============================================================
# 7. SWAPPING VARIABLES ⭐
# ============================================================

a = 10
b = 20

print("Before:", a, b)

a, b = b, a

print("After:", a, b)

# ⭐ Python allows swapping without a temporary variable.
# This is a very common and useful Python feature.


# ============================================================
# 8. VARIABLE NAMING RULES
# ============================================================

# Valid:

user_name = "Piyush"
age2 = 20
_private_value = 100
student1 = "Alex"

# Invalid:

# 2age = 20          # ❌ Cannot start with a number
# user-name = "A"    # ❌ Hyphen is not allowed
# class = "Python"   # ❌ 'class' is a Python keyword
# user name = "A"    # ❌ Spaces are not allowed


# ============================================================
# 9. NAMING CONVENTION
# ============================================================

# Python normally uses snake_case for variable names.

first_name = "Piyush"
last_name = "Krishna"
total_marks = 95

# ❌ Avoid unclear names:

x = 95
a = "Piyush"

# ✅ Prefer meaningful names:

marks = 95
student_name = "Piyush"

# ⭐ Teacher Tip:
# Good variable names make your code easier to understand.


# ============================================================
# 10. CASE SENSITIVITY
# ============================================================

name = "Piyush"
Name = "Alex"

print(name)
print(Name)

# These are two different variables in Python.


# ============================================================
# 11. REASSIGNING A VARIABLE
# ============================================================

score = 50
print(score)

score = 75
print(score)

score = 100
print(score)

# A variable can be reassigned to another value.


# ============================================================
# 12. VARIABLES CAN REFER TO DIFFERENT TYPES
# ============================================================

data = 10
print(data)

data = 10.5
print(data)

data = "Python"
print(data)

data = True
print(data)

# This is another example of Python's dynamic typing.


# ============================================================
# 13. VARIABLES AND EXPRESSIONS
# ============================================================

price = 100
quantity = 3

total = price * quantity

print("Total:", total)


# ⭐ Teacher Tip:
# Store meaningful intermediate results in variables.
# It makes calculations easier to understand and modify.


# ============================================================
# 14. CONSTANTS — PYTHON CONVENTION
# ============================================================

PI = 3.14159
MAX_USERS = 100
APP_NAME = "Python Lab"

# Python does not strictly enforce constants.
# Uppercase names are a convention that means:
# "This value is intended to remain unchanged."


# ============================================================
# 15. DELETE A VARIABLE
# ============================================================

temporary_value = 500

print(temporary_value)

del temporary_value

# After del, the variable no longer exists.

# print(temporary_value)  # ❌ NameError


# ============================================================
# 16. QUICK EXPERIMENT 🧪
# ============================================================

thing = 42

print("Value:", thing)
print("Type:", type(thing))
print("ID:", id(thing))

thing = "Python"

print("Value:", thing)
print("Type:", type(thing))
print("ID:", id(thing))

# id() gives the identity of the object during its lifetime.
# Don't confuse object identity with the variable name itself.


# ============================================================
# 17. COMMON MISTAKES ⚠️
# ============================================================

# ❌ Using a variable before creating it:

# print(username)

# This causes:
# NameError: name 'username' is not defined


# ❌ Accidentally overwriting a variable:

count = 10
count = "ten"

# This is valid Python, but may cause problems
# if you expected count to remain a number.


# ============================================================
# 18. MINI PRACTICE 🧠
# ============================================================

# Try these yourself:

# 1. Create variables for:
#    - your name
#    - your age
#    - your height
#    - whether you are a student
#
# 2. Print their values and types.
#
# 3. Create two numbers and swap them.
#
# 4. Create price and quantity variables
#    and calculate the total.
#
# 5. Create three variables in one line.
#
# 6. Create one variable and assign different
#    types of values to it.


# ============================================================
#                        KEY TAKEAWAYS
# ============================================================

"""
Remember:

1. Variables are names referring to objects/values.
2. Python is dynamically typed.
3. Use snake_case for normal variable names.
4. Variable names are case-sensitive.
5. Multiple assignment is possible:
       a, b = 10, 20

6. Swapping is easy:
       a, b = b, a

7. Use meaningful variable names.
8. Constants are conventionally written in UPPER_CASE.
9. type() tells you the type of an object.
10. id() gives an object's identity.
"""