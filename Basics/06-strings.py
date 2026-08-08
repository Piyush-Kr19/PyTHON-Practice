"""
============================================================
                PYTHON STRING BASICS
============================================================

Strings are a sequence of characters.

In Python:
    - Strings are sequences of Unicode characters.
    - Strings are ordered.
    - Strings are indexed.
    - Strings are iterable.
    - Strings are immutable.

Topics covered:
    1. Creating Strings
    2. Accessing Characters
    3. String Slicing
    4. Editing & Deleting Strings
    5. String Operations
    6. Looping Through Strings
    7. Membership Operations
    8. Common String Functions
    9. Case Conversion
    10. Searching
    11. String Checking
    12. Split & Join
    13. Replace & Strip
    14. String Formatting
    15. String Practice Problems

============================================================
"""


# ============================================================
# 1. CREATING STRINGS
# ============================================================

s1 = 'hello'
s2 = "hello"

print(s1)
print(s2)


# Multiline strings:

s3 = '''Hello
Python
World'''

s4 = """Hello
Python
World"""

print(s3)
print(s4)


# Using str():

s5 = str("hello")

print(s5)


# ⭐ Teacher Tip:
# Strings can use single quotes or double quotes.
# Use whichever makes the code easier to read.


# Example:

message = "It's raining outside"

print(message)


# ============================================================
# 2. ACCESSING CHARACTERS
# ============================================================

s = "hello world"

print(s[0])
print(s[1])
print(s[2])
print(s[4])


"""
Positive Indexing:

    h   e   l   l   o       w   o   r   l   d
    0   1   2   3   4   5   6   7   8   9   10
"""


# ⭐ Remember:
# Python indexing starts from 0.


# ============================================================
# 3. NEGATIVE INDEXING
# ============================================================

s = "hello world"

print(s[-1])
print(s[-2])
print(s[-3])


"""
Negative Indexing:

    h    e    l    l    o       w    o    r    l    d
  -11  -10   -9   -8   -7  -6  -5   -4   -3   -2   -1
"""


# ⭐ Useful trick:
# s[-1] gives the LAST character.


# ============================================================
# 4. INDEX ERROR
# ============================================================

s = "hello"

# print(s[10])

# ❌ IndexError
#
# The requested index does not exist.


# ============================================================
# 5. STRING SLICING
# ============================================================

s = "hello world"

print(s[0:5])
print(s[6:11])


"""
General syntax:

    string[start:stop:step]

Important:
    stop index is NOT included.
"""


# Examples:

print(s[:5])       # hello
print(s[6:])       # world
print(s[:])        # complete string


# ============================================================
# 6. SLICING WITH STEP
# ============================================================

s = "hello world"

print(s[::2])

# Takes every second character.


# ============================================================
# 7. REVERSE A STRING ⭐
# ============================================================

s = "hello world"

print(s[::-1])

# Output:
# dlrow olleh


# ⭐ Remember:
#
# [::-1]
#
# is one of the most useful Python string tricks.


# ============================================================
# 8. NEGATIVE SLICING
# ============================================================

s = "hello world"

print(s[-1:-6:-1])

# Output:
# dlrow


# Another example:

print(s[6:0:-2])


# ============================================================
# 9. STRINGS ARE IMMUTABLE ⭐
# ============================================================

s = "hello world"

# ❌ Not allowed:

# s[0] = "H"

# TypeError:
# 'str' object does not support item assignment


# Strings cannot be changed character-by-character.


# ============================================================
# 10. HOW TO "EDIT" A STRING
# ============================================================

s = "hello world"

# Create a NEW string:

s = "H" + s[1:]

print(s)

# Output:
# Hello world


# ⭐ Important:
# Strings are immutable.
# Operations create new strings.


# ============================================================
# 11. DELETING A STRING
# ============================================================

s = "hello world"

del s

# print(s)

# ❌ NameError
#
# The variable no longer exists.


# Individual characters cannot be deleted:

s = "hello world"

# del s[0]

# ❌ TypeError


# ============================================================
# 12. STRING CONCATENATION
# ============================================================

first = "Hello"
second = "World"

result = first + " " + second

print(result)


# ============================================================
# 13. STRING REPETITION
# ============================================================

print("Python " * 3)

print("*" * 50)


# Useful for separators:

print("=" * 40)


# ============================================================
# 14. RELATIONAL OPERATIONS
# ============================================================

print("delhi" == "delhi")
print("delhi" != "mumbai")

print("mumbai" > "pune")


# Strings are compared lexicographically.


# ============================================================
# 15. STRING COMPARISON IS CASE-SENSITIVE
# ============================================================

print("Pune" == "pune")

# False


# "P" and "p" are different characters.


# ============================================================
# 16. LOGICAL OPERATIONS
# ============================================================

print("hello" and "world")

print("hello" or "world")

print("" and "world")

print("" or "world")

print(not "hello")


# ⭐ Important:
#
# and / or can return one of the operands,
# not necessarily True or False.


# ============================================================
# 17. LOOPING THROUGH A STRING
# ============================================================

for character in "hello":
    print(character)


# Output:
#
# h
# e
# l
# l
# o


# Another example:

for character in "delhi":
    print("pune")


# The loop runs once for every character.


# ============================================================
# 18. MEMBERSHIP OPERATORS
# ============================================================

s = "hello world"

print("hello" in s)

print("java" in s)

print("java" not in s)


# ⭐ Useful for checking whether something exists.


# ============================================================
# 19. CASE-SENSITIVE MEMBERSHIP
# ============================================================

print("D" in "delhi")

# False

# "D" != "d"


# ============================================================
# 20. COMMON STRING FUNCTIONS
# ============================================================

s = "hello world"

print(len(s))

print(max(s))

print(min(s))

print(sorted(s))


"""
Common functions:

    len()       -> length
    max()       -> maximum character
    min()       -> minimum character
    sorted()    -> sorted list of characters
"""


# ============================================================
# 21. sorted()
# ============================================================

s = "hello world"

print(sorted(s))

print(sorted(s, reverse=True))


# ⭐ Important:
#
# sorted() returns a LIST.
#
# It does not return a string.


# ============================================================
# 22. capitalize()
# ============================================================

s = "hello world"

print(s.capitalize())

print(s)


# Output:
#
# Hello world
# hello world


# The original string is unchanged.


# ============================================================
# 23. title()
# ============================================================

s = "hello world"

print(s.title())

# Output:
# Hello World


# ============================================================
# 24. upper()
# ============================================================

s = "hello world"

print(s.upper())


# ============================================================
# 25. lower()
# ============================================================

s = "HELLO WORLD"

print(s.lower())


# ============================================================
# 26. swapcase()
# ============================================================

s = "HeLlO WorLD"

print(s.swapcase())

# Output:
# hElLo wORld


# ============================================================
# ⭐ IMPORTANT — STRING METHODS DON'T MODIFY ORIGINAL
# ============================================================

s = "hello"

s.upper()

print(s)

# Still:
# hello


# Correct:

s = s.upper()

print(s)

# HELLO


# ============================================================
# 27. count()
# ============================================================

s = "my name is nitish"

print(s.count("i"))

print("banana".count("na"))


# count() returns the number of occurrences.


# ============================================================
# 28. find()
# ============================================================

s = "my name is nitish"

print(s.find("i"))

print(s.find("x"))


# If not found:
#
# find() returns -1.


# ============================================================
# 29. index()
# ============================================================

s = "my name is nitish"

print(s.index("i"))


# If the value is not found:

# print(s.index("x"))

# ❌ ValueError


# ============================================================
# ⭐ find() vs index()
# ============================================================

"""
find():

    found       -> position
    not found   -> -1


index():

    found       -> position
    not found   -> ValueError
"""


# ============================================================
# 30. startswith()
# ============================================================

s = "my name is nitish"

print(s.startswith("my"))

print(s.startswith("hello"))


# ============================================================
# 31. endswith()
# ============================================================

s = "my name is nitish"

print(s.endswith("nitish"))

print(s.endswith("hello"))


# Practical example:

filename = "program.py"

if filename.endswith(".py"):
    print("Python file")


# ============================================================
# 32. format()
# ============================================================

name = "Piyush"
gender = "male"

message = "Hi my name is {1} and I am a {0}".format(
    gender,
    name
)

print(message)


# ⭐ Note:
# The numbers inside {} refer to the arguments.


# ============================================================
# 33. isalnum()
# ============================================================

print("nitish123".isalnum())

print("nitish1234%".isalnum())

# True
# False


# isalnum() means:
#
# Alphabet + Numbers


# ============================================================
# 34. isalpha()
# ============================================================

print("nitish".isalpha())

print("nitish123".isalpha())


# isalpha() -> only alphabetic characters.


# ============================================================
# 35. isdigit()
# ============================================================

print("123".isdigit())

print("123abc".isdigit())


# isdigit() -> only digits.


# ============================================================
# 36. isidentifier()
# ============================================================

print("first_name".isidentifier())

print("first-name".isidentifier())


# A valid Python identifier cannot contain '-'


# ============================================================
# 37. split()
# ============================================================

s = "hi my name is nitish"

words = s.split()

print(words)


# Output:
#
# ['hi', 'my', 'name', 'is', 'nitish']


# ⭐ split() converts:
#
# String -> List


# ============================================================
# 38. split() WITH SEPARATOR
# ============================================================

data = "apple,banana,mango"

fruits = data.split(",")

print(fruits)


# ============================================================
# 39. join()
# ============================================================

words = ["hi", "my", "name", "is", "nitish"]

sentence = " ".join(words)

print(sentence)


# Output:
#
# hi my name is nitish


# ⭐ join() converts:
#
# List of strings -> String


# ============================================================
# 40. split() vs join()
# ============================================================

"""
split():

    "hello world"
          ↓
    ["hello", "world"]


join():

    ["hello", "world"]
          ↓
    "hello world"
"""


# ============================================================
# 41. replace()
# ============================================================

s = "hi my name is nitish"

result = s.replace("nitish", "Piyush")

print(result)


# If the target doesn't exist,
# the original string remains unchanged.


# ============================================================
# 42. strip()
# ============================================================

s = "nitish                 "

print(s.strip())


# Removes whitespace from:
# beginning and end.


# Practical example:

name = input("Enter your name: ").strip()

print(name)


# ⭐ Very useful when cleaning user input.


# ============================================================
# 43. STRING PRACTICE
# ============================================================


# ------------------------------------------------------------
# Problem 1:
# Find length without using len()
# ------------------------------------------------------------

s = input("Enter a string: ")

counter = 0

for character in s:
    counter += 1

print("Length:", counter)


# ------------------------------------------------------------
# Problem 2:
# Extract username from email
# ------------------------------------------------------------

"""
Example:

Input:
    nitish24singh@gmail.com

Output:
    nitish24singh
"""

email = input("Enter email: ")

position = email.index("@")

username = email[0:position]

print(username)


# ------------------------------------------------------------
# Problem 3:
# Count frequency of a character
# ------------------------------------------------------------

s = input("Enter the string: ")

target = input("What would you like to search for? ")

counter = 0

for character in s:

    if character == target:
        counter += 1

print("Frequency:", counter)


# ------------------------------------------------------------
# Problem 4:
# Remove a particular character
# ------------------------------------------------------------

s = input("Enter the string: ")

target = input("What would you like to remove? ")

result = ""

for character in s:

    if character != target:
        result = result + character

print(result)


# ------------------------------------------------------------
# Problem 5:
# Check whether a string is palindrome
# ------------------------------------------------------------

"""
Examples:

    abba
    malayalam
    madam

are palindromes.
"""

s = input("Enter the string: ")

flag = True

for i in range(0, len(s) // 2):

    if s[i] != s[len(s) - i - 1]:

        flag = False
        break


if flag:
    print("Palindrome")
else:
    print("Not a Palindrome")


# ------------------------------------------------------------
# Problem 6:
# Count words without using split()
# ------------------------------------------------------------

s = input("Enter the string: ")

words = []

temp = ""

for character in s:

    if character != " ":

        temp = temp + character

    else:

        words.append(temp)
        temp = ""


words.append(temp)

print(words)


# ------------------------------------------------------------
# Problem 7:
# Convert string to title case without title()
# ------------------------------------------------------------

s = input("Enter the string: ")

words = []

for word in s.split():

    words.append(
        word[0].upper() + word[1:].lower()
    )


print(" ".join(words))


# ============================================================
# 44. STRING PROBLEM-SOLVING PATTERNS ⭐
# ============================================================

"""
When solving string problems, remember these patterns.
"""


# Pattern 1:
# Traverse every character

for character in s:
    pass


# Pattern 2:
# Count something

counter = 0

for character in s:

    if character == "x":
        counter += 1


# Pattern 3:
# Build a new string

result = ""

for character in s:

    if character != "x":
        result += character


# Pattern 4:
# Compare characters from both sides

for i in range(len(s) // 2):

    if s[i] != s[len(s) - i - 1]:
        pass


# Pattern 5:
# Find a position and slice

position = s.index("@")

result = s[:position]


# ============================================================
# 45. QUICK REVISION
# ============================================================

"""
STRING CREATION
---------------

'hello'
"hello"
'''hello'''
\"\"\"hello\"\"\"


INDEXING
--------

s[0]
s[-1]


SLICING
-------

s[start:stop:step]

s[:]
s[:5]
s[5:]
s[::-1]


OPERATIONS
----------

s1 + s2
s * 3

"hello" in s
"hello" not in s


COMMON FUNCTIONS
----------------

len(s)
max(s)
min(s)
sorted(s)


CASE
----

s.capitalize()
s.title()
s.upper()
s.lower()
s.swapcase()


SEARCH
------

s.count()
s.find()
s.index()


CHECK
-----

s.startswith()
s.endswith()

s.isalnum()
s.isalpha()
s.isdigit()
s.isidentifier()


TRANSFORMATION
--------------

s.split()
" ".join(...)
s.replace()
s.strip()


FORMATTING
----------

"Hello {}".format(name)


IMPORTANT
---------

Strings are immutable.

You cannot do:

    s[0] = "H"

Instead, create a new string.
"""


# ============================================================
# 46. ⭐ MOST IMPORTANT THINGS TO REMEMBER
# ============================================================

"""
1. String indexing starts from 0.

2. Negative indexing starts from -1.

3. Slicing follows:
       [start:stop:step]

4. The stop index is excluded.

5. [::-1] reverses a string.

6. Strings are immutable.

7. String methods return new strings.

8. find() returns -1 when not found.

9. index() raises ValueError when not found.

10. split() converts a string into a list.

11. join() combines strings.

12. Strings can be iterated using a for loop.

13. 'x' in string checks membership.

14. String comparison is case-sensitive.

15. strip() is useful for cleaning user input.

16. String problems often use:
        loops
        indexing
        slicing
        counters
        conditions
        result strings
"""


# ============================================================
#                    END OF STRING NOTES
# ============================================================