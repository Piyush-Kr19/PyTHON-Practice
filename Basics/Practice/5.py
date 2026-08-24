#🐍 Challenge #5 — Movie Ticket 🎬

#🏆 Challenge Name: Cinema Ticket Calculator

#🎯 Objective
#input() + if/elif/else + comparison operators + arithmetic ko combine karna.

age = int(input("Enter the age: "))
ticket = int(input("Enter the price of ticket: "))

print(f"Age: {age} years")
print(f"Ticket: ${ticket}")

if age < 5:
    print("\n-----Ticket is FREE-----\n")
    bill = 0
    
elif 5 <= age <= 17:
    print("\n-----50% Discount-----\n")
    discount = 50
    d_price = ticket * (discount / 100)
    bill = ticket - d_price
    
elif 18 <= age <= 59:
    print("\n-----No discount-----\n")
    bill = ticket
    
elif age >= 60:
    print("\n-----30% Discount-----\n")
    discount = 30
    d_price = ticket * (discount / 100)
    bill = ticket - d_price
    
print(f"Total Bill: ${bill}")