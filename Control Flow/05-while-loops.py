"""
============================================================
                    WHILE LOOPS
============================================================

A while loop repeatedly executes a block of code as long
as a given condition remains True.

Syntax:

    while condition:
        # code to execute

The condition is checked before every iteration.

⭐ Make sure the condition eventually becomes False,
otherwise the loop can run forever.
============================================================
"""

i = 1
while i <= 5:
    print(i)
    i += 1


# ============================================================
# 🧠 WHILE LOOP CHALLENGES
# ============================================================

"""
Challenge 1 — Countdown
-----------------------
Take a number from the user and print a countdown
until 0.

"""

num = int(input("Enter a number: "))

while num >= 0:
    print(num)
    num -= 1

"""
Challenge 2 — Sum Until Zero
----------------------------
Keep taking numbers from the user.

Stop when the user enters 0.

Print the total of all numbers entered.
"""

total = 0
num = int(input("Enter a number:"))

while num != 0:
    total += num
    num = int(input("Enter a number:"))
    
print("Total:",total)

"""
Challenge 3 — Password Attempts
-------------------------------
Ask the user for a password.

Give them 3 attempts.

"""
password = "Bingo"
attempts = 0

while attempts < 3:
    password = input("Enter the password:")
    
    if password == "Bingo":
        print("Login Successful!")
        break
    
    attempts += 1
    if attempts == 3:
        print("Account Locked")
        
        
# ============================================================
#                  WHILE LOOP CHALLENGES
# ============================================================

# CHALLENGE 4 — NUMBER GUESSING
# -----------------------------
# Secret number = 42

# Keep asking the user to guess.

# If guess > secret number:
#     print "Too high"

# If guess < secret number:
#     print "Too low"

# If guess == secret number:
#     print "Correct!" and stop.


# ------------------------------------------------------------

# CHALLENGE 5 — COUNT DIGITS
# ---------------------------
# Take an integer from the user and count how many digits
# it contains.

# Example:
#     Input: 58392
#     Output: 5

# Hint:
#     Think about repeatedly dividing the number by 10.


# ------------------------------------------------------------

# CHALLENGE 6 — REVERSE A NUMBER
# -------------------------------
# Take a number and reverse it using a while loop.

# Example:
#     Input: 12345
#     Output: 54321

# Hint:
#     Think about how to extract the last digit.


# ------------------------------------------------------------

# CHALLENGE 7 — SUM OF DIGITS
# ----------------------------
# Take a number and calculate the sum of its digits.

# Example:
#     Input: 1234
#     Output: 10

# Because:
#     1 + 2 + 3 + 4 = 10


# ------------------------------------------------------------

# CHALLENGE 8 — MULTIPLICATION TABLE
# -----------------------------------
# Ask the user for a number and print its multiplication
# table from 1 to 10.

# Example:
#     Enter number: 7

#     7 x 1 = 7
#     7 x 2 = 14
#     ...
#     7 x 10 = 70


# ------------------------------------------------------------

# CHALLENGE 9 — VOWEL COUNTER
# ----------------------------
# Take a string from the user and count how many vowels
# it contains.

# Example:
#     Input: Python Programming
#     Output: 4

# Vowels:
#     a, e, i, o, u


# ------------------------------------------------------------

# CHALLENGE 10 — MENU PROGRAM
# ----------------------------
# Create a program that repeatedly shows:

#     1. Say Hello
#     2. Show Number
#     3. Exit

# The program should continue until the user chooses 3.

# Example:

#     Enter choice: 1
#     Hello!

#     Enter choice: 2
#     Current number: 10

#     Enter choice: 3
#     Goodbye!


# ============================================================
#                     BONUS CHALLENGES
# ============================================================

# CHALLENGE 11 — PRIME NUMBER
# ----------------------------
# Take a number and determine whether it is prime.

# Example:
#     17 → Prime
#     12 → Not Prime


# ------------------------------------------------------------

# CHALLENGE 12 — PALINDROME NUMBER
# ---------------------------------
# Check whether a number reads the same forwards and
# backwards.

# Example:
#     121 → Palindrome
#     123 → Not Palindrome


# ------------------------------------------------------------

# CHALLENGE 13 — ATM SIMULATION 🚀
# --------------------------------
# Start with:

#     balance = 5000

# Show a menu repeatedly:

#     1. Check Balance
#     2. Deposit
#     3. Withdraw
#     4. Exit

# Handle:

#     - Invalid choices
#     - Deposits
#     - Withdrawals
#     - Insufficient balance
#     - Exit


# ============================================================
# RULE
# ============================================================

# Solve the challenges yourself first.

# If stuck:
#     → Ask for a hint

# Don't immediately look at the solution.

# ============================================================