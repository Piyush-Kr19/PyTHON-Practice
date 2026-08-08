"""
============================================================
                    PYTHON OPERATORS
============================================================

Operators are symbols/keywords used to perform operations
on values and variables.

Main categories:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Membership Operators
6. Identity Operators
7. Bitwise Operators

============================================================
"""


# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================

a = 10
b = 3

print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a // b)   # Floor Division
print(a % b)    # Modulus
print(a ** b)   # Exponentiation


# ============================================================
# 2. / vs // ⭐
# ============================================================

print(10 / 3)
print(10 // 3)

# /  -> normal division
# // -> floor division

# ⭐ Teacher Tip:
# / normally produces a float.
#
# // removes the fractional part by flooring the result.


# ============================================================
# 3. MODULUS (%) ⭐
# ============================================================

print(10 % 3)   # 1
print(20 % 5)   # 0

# % gives the remainder.

# Very useful for checking even/odd:

number = 10

print(number % 2 == 0)

# True -> even
# False -> odd


# ============================================================
# 4. EXPONENTIATION (**)
# ============================================================

print(2 ** 3)
print(5 ** 2)

# 2 ** 3 means:
# 2 × 2 × 2 = 8


# ============================================================
# 5. OPERATOR PRECEDENCE ⭐
# ============================================================

result = 10 + 5 * 2

print(result)

# Multiplication happens before addition.

# Use parentheses when you want to make the
# order explicit:

result = (10 + 5) * 2

print(result)

"""
General order to remember:

()
**
* / // %
+ -

Comparison
not
and
or
"""


# ============================================================
# 6. ASSIGNMENT OPERATOR
# ============================================================

x = 10

# = means assignment.
#
# It assigns the value on the right
# to the variable on the left.


# ============================================================
# 7. COMPOUND ASSIGNMENT OPERATORS
# ============================================================

x = 10

x += 5
print(x)

x -= 3
print(x)

x *= 2
print(x)

x /= 4
print(x)

x //= 2
print(x)

x %= 3
print(x)

x **= 2
print(x)


# These are shortcuts.

# x += 5
# means:
# x = x + 5


# ============================================================
# 8. COMPARISON OPERATORS
# ============================================================

a = 10
b = 20

print(a == b)   # Equal
print(a != b)   # Not equal
print(a > b)    # Greater than
print(a < b)    # Less than
print(a >= b)   # Greater than or equal
print(a <= b)   # Less than or equal

# Comparison operators always produce a boolean result:
# True or False


# ============================================================
# 9. = vs == ⚠️
# ============================================================

x = 10       # Assignment
print(x == 10)   # Comparison

# ⭐ Very common beginner mistake:
#
# =  -> assign
# == -> compare


# ============================================================
# 10. CHAINED COMPARISONS ⭐
# ============================================================

age = 25

print(18 <= age <= 60)

# This is equivalent to:

print(age >= 18 and age <= 60)

# Python allows mathematical-style comparisons.


# ============================================================
# 11. LOGICAL OPERATORS
# ============================================================

# and
# or
# not

age = 25
has_license = True

print(age >= 18 and has_license)

print(age < 18 or has_license)

print(not has_license)


# ============================================================
# 12. AND
# ============================================================

# and returns True only when BOTH conditions are True.

print(True and True)
print(True and False)
print(False and True)
print(False and False)


# Example:

age = 20
has_id = True

can_enter = age >= 18 and has_id

print(can_enter)


# ============================================================
# 13. OR
# ============================================================

# or returns True when AT LEAST ONE condition is True.

print(True or True)
print(True or False)
print(False or True)
print(False or False)


# Example:

is_admin = False
is_owner = True

can_edit = is_admin or is_owner

print(can_edit)


# ============================================================
# 14. NOT
# ============================================================

is_logged_in = False

print(not is_logged_in)

# not reverses a boolean result.


# ============================================================
# 15. SHORT-CIRCUITING ⭐
# ============================================================

# Python may stop evaluating a logical expression
# once the result is already known.

# AND:

False and print("This will not run")

# OR:

True or print("This will not run")

# ⭐ This behavior is called short-circuit evaluation.


# ============================================================
# 16. MEMBERSHIP OPERATORS
# ============================================================

# in
# not in

name = "Piyush"

print("P" in name)
print("x" in name)
print("z" not in name)


numbers = [10, 20, 30]

print(20 in numbers)
print(50 not in numbers)


# Very useful with strings, lists, sets, etc.


# ============================================================
# 17. IDENTITY OPERATORS
# ============================================================

# is
# is not

a = None

print(a is None)
print(a is not None)


# ⭐ Important:
#
# == checks whether values are equal.
# is checks whether two references point to the same object.


# For example:

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)   # True
print(x is y)   # False

# Same contents, but different list objects.


# ============================================================
# 18. is vs == ⚠️
# ============================================================

# Use == when comparing values:

age = 20

print(age == 20)


# Use is commonly when checking None:

result = None

if result is None:
    print("No result")


# Avoid using "is" simply because two values look equal.


# ============================================================
# 19. BITWISE OPERATORS
# ============================================================

"""
Bitwise operators work directly with binary bits.

&   AND
|   OR
^   XOR
~   NOT
<<  Left shift
>>  Right shift
"""

a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)


# ============================================================
# 20. BINARY REPRESENTATION
# ============================================================

number = 10

print(bin(number))

# bin() converts an integer to binary representation.

# Example:
#
# 10 -> 1010


# ============================================================
# 21. BITWISE EXAMPLE 🧠
# ============================================================

a = 5       # 0101
b = 3       # 0011

print(a & b)
print(a | b)
print(a ^ b)

"""
  0101
& 0011
------
  0001

Result = 1
"""


# ============================================================
# 22. LEFT SHIFT / RIGHT SHIFT
# ============================================================

number = 5

print(number << 1)
print(number << 2)

print(number >> 1)
print(number >> 2)

# Left shift generally multiplies by powers of 2.
#
# Right shift generally divides by powers of 2
# for positive integers.


# ============================================================
# 23. OPERATOR PRECEDENCE EXAMPLE
# ============================================================

result = 10 + 2 * 3 ** 2

print(result)

# ** happens first
# then *
# then +

# Use parentheses if the expression becomes difficult
# to understand.


# ============================================================
# 24. PRACTICAL EXAMPLE — EVEN / ODD
# ============================================================

number = 17

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# ============================================================
# 25. PRACTICAL EXAMPLE — RANGE CHECK
# ============================================================

age = 25

if 18 <= age <= 60:
    print("Age is within the range")


# ============================================================
# 26. PRACTICAL EXAMPLE — LOGIN CHECK
# ============================================================

username = "admin"
password = "python123"

entered_username = "admin"
entered_password = "python123"

login_successful = (
    entered_username == username
    and entered_password == password
)

print(login_successful)


# ============================================================
# 27. PRACTICAL EXAMPLE — DISCOUNT
# ============================================================

price = 1500
is_member = True

if price >= 1000 and is_member:
    discount = 0.20
else:
    discount = 0.10

final_price = price - (price * discount)

print(f"Final price: ₹{final_price:.2f}")


# ============================================================
# 28. COMMON MISTAKES ⚠️
# ============================================================

# ❌ Confusing = and ==

# if age = 18:
#     print("Adult")


# ❌ Using is instead of ==

# if name is "Piyush":
#     print("Hello")


# ❌ Forgetting operator precedence

result = 10 + 2 * 5

print(result)

# If you intended:
result = (10 + 2) * 5

print(result)


# ❌ Integer division confusion

print(7 / 2)
print(7 // 2)


# ============================================================
# 29. MINI PRACTICE 🧠
# ============================================================

"""
Try these yourself:

1. Take two numbers and perform all arithmetic operations.

2. Check whether a number is even or odd.

3. Check whether a number is divisible by 5.

4. Take age and check whether it is between 18 and 60.

5. Create a login condition using:
    username
    password

6. Check whether a character exists in a string.

7. Compare two lists using == and is.
    Observe the difference.

8. Practice compound assignments.

9. Convert a number to binary using bin().

10. Practice &, |, ^, << and >> using small integers.

11. Predict the output before running:
        10 + 2 * 3
       (10 + 2) * 3
        10 // 3
        10 % 3
        2 ** 4
"""


# ============================================================
#                     KEY TAKEAWAYS
# ============================================================

"""
Remember:

1. Arithmetic:
       +  -  *  /  //  %  **

2. Assignment:
       =  +=  -=  *=  /=  //=  %=  **=

3. Comparison:
    ==  !=  >  <  >=  <=

4. Logical:
    and  or  not

5. Membership:
    in  not in

6. Identity:
    is  is not

7. Bitwise:
    &  |  ^  ~  <<  >>

8. % gives the remainder.

9. // performs floor division.

10. == compares values.

11. is checks object identity.

12. Logical operators use short-circuit evaluation.

13. Operator precedence determines the order
    in which expressions are evaluated.

14. Parentheses make complicated expressions
    easier to understand.
"""