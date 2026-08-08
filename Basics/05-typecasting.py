"""
============================================================
                    PYTHON TYPE CASTING
============================================================

Type casting means converting a value from one data type
to another.

Common conversion functions:

    int()
    float()
    str()
    bool()
    list()
    tuple()
    set()

Important:
    Not every value can be converted successfully.
============================================================
"""


# ============================================================
# 1. INTEGER CONVERSION — int()
# ============================================================

number = "100"

print(number)
print(type(number))

number = int(number)

print(number)
print(type(number))


# Float -> int

price = 99.99

price_as_int = int(price)

print(price_as_int)

# ⚠️ int() does NOT round the number.
#
# 99.99 -> 99
#
# It removes the decimal portion.


# Boolean -> int

print(int(True))    # 1
print(int(False))   # 0


# ============================================================
# 2. FLOAT CONVERSION — float()
# ============================================================

number = "10.5"

number = float(number)

print(number)
print(type(number))


# int -> float

age = 20

age = float(age)

print(age)
print(type(age))


# Boolean -> float

print(float(True))     # 1.0
print(float(False))    # 0.0


# ============================================================
# 3. STRING CONVERSION — str()
# ============================================================

age = 20

age_text = str(age)

print(age_text)
print(type(age_text))


# Useful when combining numbers with strings:

age = 20

print("I am " + str(age) + " years old.")


# ⭐ Usually, f-strings are cleaner:

print(f"I am {age} years old.")


# ============================================================
# 4. BOOLEAN CONVERSION — bool() ⭐
# ============================================================

print(bool(1))
print(bool(0))

print(bool("Python"))
print(bool(""))

print(bool([1, 2, 3]))
print(bool([]))


"""
Common falsy values:

    False
    None
    0
    0.0
    ""
    []
    ()
    {}
    set()

Most other values are truthy.
"""


# ============================================================
# 5. TYPE CASTING USER INPUT ⭐
# ============================================================

age = input("Enter your age: ")

print(age)
print(type(age))


# Convert the input:

age = int(input("Enter your age: "))

print(age)
print(type(age))


# Float input:

height = float(input("Enter your height: "))

print(height)
print(type(height))


# ⭐ Teacher Tip:
# input() always gives a string.
#
# If you need a number, convert it.


# ============================================================
# 6. MULTIPLE INPUT + TYPE CASTING
# ============================================================

a, b = input("Enter two numbers: ").split()

a = int(a)
b = int(b)

print(a + b)


# Cleaner version:

a, b = map(int, input("Enter two numbers: ").split())

print(a + b)

# map() will be covered in more detail later.


# ============================================================
# 7. STRING -> LIST
# ============================================================

text = "Python"

letters = list(text)

print(letters)
print(type(letters))


# Output:
# ['P', 'y', 't', 'h', 'o', 'n']


# ============================================================
# 8. LIST -> TUPLE
# ============================================================

numbers = [1, 2, 3, 4]

numbers_tuple = tuple(numbers)

print(numbers_tuple)
print(type(numbers_tuple))


# ============================================================
# 9. LIST -> SET
# ============================================================

numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)

print(unique_numbers)
print(type(unique_numbers))

# ⭐ Teacher Tip:
# Converting a list to a set is a simple way to
# remove duplicate values.
#
# Remember:
# A set does not preserve duplicates.


# ============================================================
# 10. TUPLE -> LIST
# ============================================================

coordinates = (10, 20, 30)

coordinates = list(coordinates)

print(coordinates)
print(type(coordinates))


# ============================================================
# 11. SET -> LIST
# ============================================================

numbers = {1, 2, 3, 4}

numbers = list(numbers)

print(numbers)
print(type(numbers))

# ⚠️ Don't depend on a set's order.


# ============================================================
# 12. STRING -> INTEGER
# ============================================================

number = "500"

number = int(number)

print(number + 100)


# ============================================================
# 13. STRING -> FLOAT
# ============================================================

price = "99.99"

price = float(price)

print(price + 10)


# ============================================================
# 14. INVALID CONVERSION ⚠️
# ============================================================

# This will cause a ValueError:

# number = int("Python")

# Python cannot interpret "Python" as an integer.


# Another example:

# number = int("10.5")

# This also fails because "10.5" is not
# a valid integer representation.

# Correct:

number = int(float("10.5"))

print(number)


# ============================================================
# 15. FLOAT -> INT DOES NOT ROUND
# ============================================================

print(int(9.99))
print(int(9.01))
print(int(-9.99))

# ⭐ Important:
#
# int() truncates toward zero.
#
# It does NOT perform normal mathematical rounding.


# ============================================================
# 16. ROUNDING IS DIFFERENT
# ============================================================

number = 9.99

print(int(number))
print(round(number))

# int()  -> 9
# round() -> 10


# ============================================================
# 17. BOOL CONVERSION — IMPORTANT EXPERIMENT 🧪
# ============================================================

values = [
    0,
    1,
    -1,
    "",
    "0",
    "False",
    [],
    [0],
    None
]

for value in values:
    print(repr(value), "->", bool(value))


# ⭐ Notice:
#
# bool("0") is True
# bool("False") is True
#
# because both are NON-EMPTY STRINGS.


# ============================================================
# 18. repr() vs str() — SMALL BONUS
# ============================================================

text = "Hello\nWorld"

print(str(text))
print(repr(text))

# repr() shows a representation useful for
# understanding/debugging the value.


# ============================================================
# 19. TYPE CASTING VS TYPE CHECKING
# ============================================================

value = "100"

print(type(value))

value = int(value)

print(type(value))

# type() tells you what the type is.
#
# int(), float(), str(), etc. can create a value
# of another type.


# ============================================================
# 20. isinstance() ⭐
# ============================================================

value = 100

print(isinstance(value, int))
print(isinstance(value, str))
print(isinstance(value, (int, float)))

# isinstance() checks whether an object is an
# instance of a particular type.


# ============================================================
# 21. PRACTICAL EXAMPLE — BILL
# ============================================================

price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"Total: ₹{total:.2f}")


# ============================================================
# 22. PRACTICAL EXAMPLE — TEMPERATURE
# ============================================================

celsius = float(input("Temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C = {fahrenheit:.2f}°F")


# ============================================================
# 23. PRACTICAL EXAMPLE — USER DATA
# ============================================================

name = input("Name: ")
age = int(input("Age: "))
height = float(input("Height: "))

print("\n--- User Information ---")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"Height : {height}")


# ============================================================
# 24. COMMON MISTAKES ⚠️
# ============================================================

# ❌ Adding string and integer:

# age = "20"
# print(age + 5)

# TypeError


# ✅ Convert first:

age = "20"

print(int(age) + 5)


# ------------------------------------------------------------

# ❌ Assuming int() rounds:

number = 7.9

print(int(number))     # 7
print(round(number))   # 8


# ------------------------------------------------------------

# ❌ Assuming "0" is False:

print(bool("0"))

# True!

# Why?
# Because "0" is a non-empty string.


# ============================================================
# 25. IMPORTANT CONVERSION TABLE
# ============================================================

"""
    int("10")       -> 10
    int(10.9)       -> 10
    int(True)       -> 1
    int(False)      -> 0

    float("10.5")   -> 10.5
    float(10)       -> 10.0
    float(True)     -> 1.0

    str(100)        -> "100"
    str(True)       -> "True"

    bool(0)         -> False
    bool(1)         -> True
    bool("")        -> False
    bool("hello")   -> True
    bool([])        -> False
    bool([1])       -> True
"""


# ============================================================
# 26. MINI PRACTICE 🧠
# ============================================================

"""
Try these yourself:

1. Convert "250" into an integer.

2. Convert "25.75" into a float.

3. Convert 100 into a string.

4. Convert True and False into integers.

5. Find the boolean value of:
       0
       1
       ""
       "hello"
       []
       [1]

6. Take two numbers from the user in one line
   and calculate their product.

7. Take a price as input and calculate 18% GST.

8. Convert a list into a tuple.

9. Convert a list containing duplicates into a set.

10. Try:
        int("hello")
    and understand the error.

11. Find the difference between:
        int(9.99)
        round(9.99)

12. Explain why:
        bool("False")
    returns True.
"""


# ============================================================
#                     KEY TAKEAWAYS
# ============================================================

"""
Remember:

1. Type casting means converting values between types.

2. Common functions:
       int()
       float()
       str()
       bool()
       list()
       tuple()
       set()

3. input() returns a string.

4. int(9.9) does NOT round to 10.
   It becomes 9.

5. Use round() when you actually want rounding.

6. Non-empty strings are truthy:
       bool("False") -> True

7. Empty collections are generally falsy.

8. Invalid conversions can raise ValueError.

9. type() checks the type.

10. isinstance() checks whether an object belongs
    to a particular type.

11. map() is useful when converting multiple inputs.

12. Converting between collection types can change
    important properties such as ordering and duplicates.
"""