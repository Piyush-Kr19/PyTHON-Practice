# 🐍 Challenge #3 — Shopping Cart

# 🎯 Objective: Variables aur arithmetic operators ko combine karna.

print("----Shopping Cart----")

burger_price = 50
pizza_price = 100

print("Burger:",burger_price)
print("Pizza:",pizza_price)

choice = input("What do you want? Burger/Pizza: ")
if choice == "Burger":
    quantity = int(input("Quantity: "))
    total = quantity * burger_price
    print("Total Bill:",total)
elif choice == "Pizza":
    quantity = int(input("Quantity: "))
    total = quantity * pizza_price
    print("Total Bill:",total)
else:
    print("Item not avaliabe")


