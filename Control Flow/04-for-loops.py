"""
============================================================
                    FOR LOOPS
============================================================

A for loop is used to iterate over a sequence/iterable.

Commonly used with:
    strings
    lists
    tuples
    sets
    dictionaries
    range()
============================================================
"""


# ============================================================
# 1. BASIC FOR LOOP
# ============================================================

for i in range(5):
    print(i)

# Output:
# 0 1 2 3 4


# ⭐ range(5) stops BEFORE 5.


# ============================================================
# 2. RANGE(start, stop)
# ============================================================

for i in range(1, 6):
    print(i)

# 1 2 3 4 5


# ============================================================
# 3. RANGE(start, stop, step)
# ============================================================

for i in range(1, 10, 2):
    print(i)

# 1 3 5 7 9


# Reverse:

for i in range(5, 0, -1):
    print(i)


# ============================================================
# 4. LOOP THROUGH A STRING
# ============================================================

name = "Python"

for character in name:
    print(character)


# ============================================================
# 5. LOOP THROUGH A LIST
# ============================================================

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# ⭐ Python's for loop directly gives you each item.
# You don't normally need to manage an index manually.


# ============================================================
# 6. enumerate() ⭐
# ============================================================

fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


# Start indexing from another number:

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


# ============================================================
# 7. LOOP THROUGH A DICTIONARY
# ============================================================

student = {
    "name": "Piyush",
    "age": 20
}

# Keys:

for key in student:
    print(key)


# Values:

for value in student.values():
    print(value)


# Key + value:

for key, value in student.items():
    print(key, value)


# ============================================================
# 8. NESTED FOR LOOP
# ============================================================

for i in range(3):

    for j in range(3):
        print(i, j)


# Useful for grids, patterns and 2D data.


# ============================================================
# 9. for + if
# ============================================================

for number in range(1, 11):

    if number % 2 == 0:
        print(number)


# Prints even numbers from 1 to 10.


# ============================================================
# 10. ELSE WITH FOR ⭐
# ============================================================

for number in range(5):
    print(number)
else:
    print("Loop completed")


# The else runs when the loop finishes normally.


# ============================================================
# 11. break
# ============================================================

for number in range(1, 10):

    if number == 5:
        break

    print(number)


# break immediately stops the loop.


# ============================================================
# 12. continue
# ============================================================

for number in range(1, 6):

    if number == 3:
        continue

    print(number)


# continue skips the current iteration.


# ============================================================
# 13. PRACTICAL EXAMPLE — SUM
# ============================================================

total = 0

for number in range(1, 6):
    total += number

print("Total:", total)


# ============================================================
# 14. PRACTICAL EXAMPLE — FIND A VALUE
# ============================================================

numbers = [10, 20, 30, 40]

target = 30

for number in numbers:

    if number == target:
        print("Found!")
        break


# ============================================================
# 15. COMMON MISTAKES ⚠️
# ============================================================

# range(5) gives:
#
# 0, 1, 2, 3, 4
#
# NOT 1 to 5.


# ❌ Don't modify a collection while directly iterating
# over it unless you understand the consequences.


# ============================================================
# 16. QUICK PRACTICE 🧠
# ============================================================

"""
Try these:

1. Print numbers from 1 to 20.

2. Print all even numbers from 1 to 50.

3. Print numbers from 10 down to 1.

4. Find the sum of numbers from 1 to 100.

5. Count vowels in a string.

6. Find the largest number in a list.

7. Search for a value in a list.

8. Print a multiplication table.

9. Use enumerate() to print:
    1. Apple
    2. Banana
    3. Mango

10. Create a simple nested loop to print a 3x3 grid.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
for        -> iterate over items
range()    -> generate a sequence of numbers
enumerate() -> index + value
break      -> stop the loop
continue   -> skip current iteration

Remember:

range(stop)
range(start, stop)
range(start, stop, step)

The stop value is NOT included.

Python's for loop iterates over objects directly,
which makes it cleaner than traditional C/Java-style
index-based loops in many situations.
"""