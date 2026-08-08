"""
============================================================
                PYTHON INPUT & OUTPUT
============================================================

Input  -> Getting data from the user
Output -> Displaying data to the user

Main tools:
    input()
    print()

Important:
    input() ALWAYS returns a string.
============================================================
"""


# ============================================================
# 1. BASIC OUTPUT
# ============================================================

print("Hello, Python!")
print("Welcome to Python Lab.")

# print() displays information on the screen.


# ============================================================
# 2. PRINTING VARIABLES
# ============================================================

name = "Piyush"
age = 20

print(name)
print(age)

print("Name:", name)
print("Age:", age)


# ============================================================
# 3. PRINTING MULTIPLE VALUES
# ============================================================

first_name = "Piyush"
last_name = "Kr"

print(first_name, last_name)

# print() automatically puts a space between multiple values.


# ============================================================
# 4. sep PARAMETER ⭐
# ============================================================

print("2026", "08", "08", sep="-")

print("Python", "Java", "C++", sep=" | ")

# sep controls what is placed between multiple values.

# Default:
# sep = " "


# ============================================================
# 5. end PARAMETER ⭐
# ============================================================

print("Hello", end=" ")
print("World")

# Normally print() moves to a new line.
#
# end controls what is printed at the end.

print("Python", end=" -> ")
print("Programming")


# ============================================================
# 6. ESCAPE CHARACTERS
# ============================================================

print("Hello\nWorld")

# \n = new line

print("Python\tProgramming")

# \t = tab

print("He said \"Hello\"")

# \" = double quote inside a string

print('It\'s Python')

# \' = single quote inside a string


# ============================================================
# 7. RAW STRINGS
# ============================================================

path = r"C:\Users\Piyush\Python"

print(path)

# r before a string makes it a raw string.
#
# Useful when working with Windows paths and backslashes.


# ============================================================
# 8. BASIC USER INPUT
# ============================================================

name = input("Enter your name: ")

print("Hello", name)


# ============================================================
# 9. input() ALWAYS RETURNS A STRING ⭐
# ============================================================

age = input("Enter your age: ")

print(age)
print(type(age))

# Even if the user enters:
#
# 20
#
# input() returns:
#
# "20"
#
# which is a string.


# ============================================================
# 10. CONVERTING USER INPUT
# ============================================================

age = int(input("Enter your age: "))

print(age)
print(type(age))


# Float input:

height = float(input("Enter your height: "))

print(height)
print(type(height))


# ============================================================
# 11. TAKING MULTIPLE INPUTS
# ============================================================

first_name, last_name = input(
    "Enter your first and last name: "
).split()

print(first_name)
print(last_name)

# split() breaks the input into separate strings.


# ============================================================
# 12. MULTIPLE NUMBERS FROM INPUT
# ============================================================

a, b = input("Enter two numbers: ").split()

a = int(a)
b = int(b)

print("Sum:", a + b)


# ⭐ Cleaner approach:

a, b = map(int, input("Enter two numbers: ").split())

print("Sum:", a + b)

# map() will be studied more deeply later.
# For now, remember that it can apply int() to each input.


# ============================================================
# 13. f-STRINGS ⭐
# ============================================================

name = "Piyush"
age = 20

print(f"My name is {name} and I am {age} years old.")

# f-strings are one of the most useful ways
# to format strings in Python.


# ============================================================
# 14. EXPRESSIONS INSIDE f-STRINGS
# ============================================================

price = 100
quantity = 3

print(f"Total: {price * quantity}")


# You can also call methods:

name = "piyush"

print(f"Name: {name.upper()}")


# ============================================================
# 15. NUMBER FORMATTING
# ============================================================

price = 1234.56789

print(f"Price: {price:.2f}")

# .2f means:
# display the number with 2 decimal places.


# Thousands separator:

population = 1000000

print(f"Population: {population:,}")

# Output:
# Population: 1,000,000


# ============================================================
# 16. PRINTING WITHOUT A NEW LINE
# ============================================================

print("Loading", end="")
print("...")

print("1", end=" ")
print("2", end=" ")
print("3", end=" ")
print("4", end=" ")
print("5")


# ============================================================
# 17. PRINTING A SIMPLE TABLE
# ============================================================

name = "Piyush"
age = 20
score = 95

print("Name :", name)
print("Age  :", age)
print("Score:", score)


# ============================================================
# 18. MULTI-LINE STRINGS
# ============================================================

message = """
Welcome to Python Lab!

We are learning:
- Variables
- Data Types
- Input
- Output
"""

print(message)


# ============================================================
# 19. USER INPUT + CALCULATION
# ============================================================

price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"Total amount: ₹{total:.2f}")


# ============================================================
# 20. USER INPUT + BOOLEAN
# ============================================================

age = int(input("Enter your age: "))

is_adult = age >= 18

print(f"Adult: {is_adult}")


# ============================================================
# 21. COMMON MISTAKE ⚠️
# ============================================================

# ❌ This causes a TypeError:

# age = input("Enter age: ")
# print(age + 5)

# Why?
#
# age is a string.
# 5 is an integer.
#
# Convert it first:

age = int(input("Enter age: "))

print(age + 5)


# ============================================================
# 22. ANOTHER COMMON MISTAKE ⚠️
# ============================================================

# ❌ Forgetting that split() returns strings:

a, b = input("Enter two numbers: ").split()

# print(a + b)
#
# If the user enters:
# 10 20
#
# output would be:
# 1020
#
# because they are strings.

# Correct:

a = int(a)
b = int(b)

print(a + b)


# ============================================================
# 23. PRACTICAL EXAMPLE 🧪
# ============================================================

"""
Create a small user profile program.
"""

name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")

print("\n--- Profile ---")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"City : {city}")


# ============================================================
# 24. MINI PRACTICE 🧠
# ============================================================

"""
Try these yourself:

1. Ask the user for their name and print a greeting.

2. Ask for two numbers and print:
    sum
    difference
    product
    division

3. Ask for:
    name
    age
    city

Then display them as a formatted profile.

4. Ask for the price and quantity of a product
and calculate the total.

5. Ask for a temperature in Celsius and convert it
    to Fahrenheit.

6. Take three numbers in a single input line.

7. Print three words separated by " - ".

8. Print a sentence without moving to a new line.

9. Create a simple bill using f-strings.

10. Experiment with:
    sep
    end
    \n
    \t
    f-strings
"""


# ============================================================
#                     KEY TAKEAWAYS
# ============================================================

"""
Remember:

1. print() is used for output.

2. input() is used for user input.

3. input() ALWAYS returns a string.

4. Convert input when necessary:
    int()
    float()

5. split() separates a string into multiple parts.

6. map() can apply a conversion to multiple values.

7. f-strings are the preferred way to format
dynamic text in modern Python.

8. sep controls the separator between print values.

9. end controls what print() adds at the end.

10. \n creates a new line.

11. \t creates a tab.

12. Raw strings are useful for paths:
    r"C:\Users\Piyush"

13. Formatting makes output easier to read.
"""