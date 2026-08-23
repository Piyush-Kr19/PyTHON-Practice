# 🐍 Challenge #4 — Smart Checkout

# 🎯 Objective :input() + if/elif/else + arithmetic operators ko ek saath use karna.

print("----Shopping Cart----")

burger_price = 50
pizza_price = 100

print("Burger:",burger_price)
print("Pizza:",pizza_price)


choice = input("What do you want? Burger/Pizza: ")
if choice == "Burger":
    
    quantity = int(input("Quantity: "))
    if quantity >= 5:
        discount = 10
    else:
        discount = 0
    total = quantity * burger_price
    discount_amount = total * (discount / 100) 
    print("Total Bill:",total - discount_amount)
    
elif choice == "Pizza":
    quantity = int(input("Quantity: "))
    if quantity >= 3:
        discount = 15
    else:
        discount = 0
    total = quantity * pizza_price
    discount_amount = total * (discount / 100) 
    print("Total Bill:",total - discount_amount)
else:
    print("Item not avaliabe")