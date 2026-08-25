# 🐍 Level 5 — ATM Simulator 💳

# 🏆 Challenge Name: Mini ATM

# 🎯 Objective
# Conditional statements ko real-world situation mein use karna.

balance = int(input("Enter the balance: "))

print(f"Balance: ${balance}")

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
choice = int(input("Choose an option: "))

if choice == 1:
    print(f"Balance: ${balance}")
    
elif choice == 2:
    depoist = int(input("Enter the amount to be depoisted: "))
    balance += depoist
    print(f"Balance: ${balance}")
    
elif choice == 3:
    withdraw = int(input("Enter the amount to withdraw: "))
    if withdraw > balance:
            print("Insufficient Balance")
    else:
        balance -= withdraw
        print(f"Balance: ${balance}")
else:
    print("Invalid option")