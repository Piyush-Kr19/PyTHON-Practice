"""
============================================================
                    PYTHON DATA TYPES
============================================================

A data type tells Python what kind of value an object holds.

Python has several built-in data types.

Main built-in types:

    Numeric:
        int
        float
        complex

    Boolean:
        bool

    Text:
        str

    Collections:
        list
        tuple
        set
        dict

    Special:
        NoneType

Python is dynamically typed, so you don't need to
declare the type of a variable explicitly.
============================================================
"""


# ============================================================
# 1. INTEGER (int)
# ============================================================

age = 20
score = -10
large_number = 1_000_000

print(age)
print(type(age))

# ⭐ Teacher Tip:
# Underscores can be used to make large numbers easier to read.
#
# 1_000_000 is exactly the same as 1000000.


# ============================================================
# 2. FLOAT (float)
# ============================================================

price = 99.99
temperature = -2.5
pi = 3.14159

print(price)
print(type(price))


# ============================================================
# 3. COMPLEX NUMBERS (complex)
# ============================================================

number = 3 + 4j

print(number)
print(type(number))

print(number.real)
print(number.imag)

# ⭐ Teacher Tip:
# Python uses 'j' for the imaginary part of a complex number.


# ============================================================
# 4. BOOLEAN (bool)
# ============================================================

is_logged_in = True
is_admin = False

print(is_logged_in)
print(type(is_logged_in))


# Boolean values are commonly produced by comparisons:

age = 20

print(age >= 18)
print(age < 18)

# Output:
# True
# False


# ============================================================
# 5. STRING (str)
# ============================================================

name = "Piyush"
message = 'Hello Python'

print(name)
print(type(name))

# Strings can contain numbers, but they are still strings:

number = "100"

print(number)
print(type(number))


# ============================================================
# 6. LIST
# ============================================================

fruits = ["apple", "banana", "mango"]

print(fruits)
print(type(fruits))

# Lists are ordered and mutable.

fruits.append("orange")

print(fruits)

# ⭐ Teacher Tip:
# Mutable means the object can be changed after creation.


# ============================================================
# 7. TUPLE
# ============================================================

coordinates = (10, 20)

print(coordinates)
print(type(coordinates))

# Tuples are ordered but immutable.

# coordinates[0] = 50  # ❌ TypeError

# ⭐ Teacher Tip:
# Lists and tuples look similar, but their mutability is different.


# ============================================================
# 8. SET
# ============================================================

numbers = {1, 2, 3, 4, 4, 4}

print(numbers)
print(type(numbers))

# Duplicate values are automatically removed.

# Sets are useful when you need unique values.


# ============================================================
# 9. DICTIONARY
# ============================================================

student = {
    "name": "Piyush",
    "age": 20,
    "course": "Python"
}

print(student)
print(type(student))

print(student["name"])

# Dictionaries store data as key-value pairs.


# ============================================================
# 10. NONE / NoneType
# ============================================================

result = None

print(result)
print(type(result))

# None represents the absence of a value.

# ⭐ Teacher Tip:
# None is NOT the same as:
#
# 0
# ""
# False
#
# It means "no value" / "nothing assigned."


# ============================================================
# 11. CHECKING DATA TYPES
# ============================================================

x = 100

print(type(x))

name = "Python"

print(type(name))

items = [1, 2, 3]

print(type(items))


# ============================================================
# 12. isinstance() ⭐
# ============================================================

age = 20

print(isinstance(age, int))
print(isinstance(age, str))

# isinstance() checks whether an object belongs to
# a particular type.

# This is often more useful than type() when
# checking types in real programs.


# ============================================================
# 13. TYPE CONVERSION
# ============================================================

number = "100"

number = int(number)

print(number)
print(type(number))


price = "99.99"

price = float(price)

print(price)
print(type(price))


age = 20

age_text = str(age)

print(age_text)
print(type(age_text))


# ============================================================
# 14. BOOLEAN CONVERSION ⭐
# ============================================================

print(bool(0))
print(bool(1))

print(bool(""))
print(bool("Python"))

print(bool([]))
print(bool([1, 2, 3]))

# Generally:
#
# 0, "", [], {}, set(), None
# are considered Falsy.
#
# Most other values are Truthy.


# ============================================================
# 15. TRUTHY AND FALSY VALUES
# ============================================================

username = ""

if username:
    print("Username exists")
else:
    print("Username is empty")

# ⭐ Teacher Tip:
# Python allows objects to be used directly in conditions.
#
# You don't always need:
#
# if username != "":
#
# You can simply use:
#
# if username:


# ============================================================
# 16. MUTABLE VS IMMUTABLE
# ============================================================

"""
Immutable objects:
    int
    float
    complex
    bool
    str
    tuple

Mutable objects:
    list
    dict
    set

You will study this more deeply in Data Structures.
"""


# Example of mutable data:

numbers = [1, 2, 3]

numbers.append(4)

print(numbers)


# Example of immutable data:

text = "Python"

text.upper()

print(text)

# text.upper() does NOT modify the original string.
#
# You need to assign the result:

text = text.upper()

print(text)


# ============================================================
# 17. SEQUENCE VS COLLECTION
# ============================================================

"""
Some useful categories to remember:

Sequence:
    str
    list
    tuple

Set:
    set

Mapping:
    dict

Numeric:
    int
    float
    complex
"""

# You don't need to memorize every category right now.
# You'll understand them better as you learn Data Structures.


# ============================================================
# 18. TYPE OF AN EXPRESSION
# ============================================================

print(type(10 + 5))
print(type(10 / 2))
print(type(10 > 5))
print(type("Hello" + " World"))

# ⭐ Teacher Tip:
# The result of an operation also has a data type.


# ============================================================
# 19. IMPORTANT TYPE BEHAVIOR 🧠
# ============================================================

print(10 + 5)        # int
print(10 + 5.5)      # float

# Python may automatically promote an integer
# to a float when performing certain operations.


# ============================================================
# 20. SAME VALUE, DIFFERENT TYPE
# ============================================================

number_1 = 100
number_2 = "100"

print(number_1)
print(number_2)

print(type(number_1))
print(type(number_2))

print(number_1 == number_2)

# False!
#
# 100 (int) and "100" (str) are different objects/types.


# ============================================================
# 21. COMMON MISTAKES ⚠️
# ============================================================

# ❌ Treating a string number as an actual number:

number = "10"

# print(number + 5)
# TypeError

# Convert it first:

number = int(number)

print(number + 5)


# ❌ Confusing None with False:

value = None

print(value is None)
print(value == False)

# ⭐ For checking None, prefer:
#
# value is None
#
# rather than:
#
# value == None


# ============================================================
# 22. QUICK EXPERIMENT 🧪
# ============================================================

values = [
    10,
    10.5,
    3 + 4j,
    True,
    "Python",
    [1, 2, 3],
    (1, 2, 3),
    {1, 2, 3},
    {"name": "Piyush"},
    None
]

for value in values:
    print(value, "→", type(value))


# ============================================================
# 23. MINI PRACTICE 🧠
# ============================================================

"""
Try these yourself:

1. Create one example of every main built-in type.

2. Check the type of each value using type().

3. Use isinstance() to check whether a variable
   is an int, str, or list.

4. Find which values are truthy and falsy:

       0
       1
       ""
       "Python"
       []
       [1]
       None

5. Create a list and modify it.

6. Create a tuple and try to modify it.
   Observe the error.

7. Create a dictionary containing:
       name
       age
       city

8. Store "500" in a variable and convert it to int.

9. Explain the difference between:
       100
       "100"

10. Explain the difference between:
       None
       False
       0
"""


# ============================================================
#                     KEY TAKEAWAYS
# ============================================================

"""
Remember:

1. Python has many built-in data types.

2. Common types:
       int
       float
       complex
       bool
       str
       list
       tuple
       set
       dict
       NoneType

3. type() tells you the type of an object.

4. isinstance() checks whether an object is an instance
   of a particular type.

5. Lists, dictionaries, and sets are mutable.

6. Strings, numbers, booleans, and tuples are immutable.

7. None means absence of a value.

8. Python has Truthy and Falsy values.

9. input() gives you a string, even when the user enters
   a number.

10. Different data types behave differently.

11. Understanding types is essential before moving into
    functions, data structures, and OOP.
"""