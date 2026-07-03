menu = {
    "pizza": 350,
    "chips": 80,
    "popcorn": 260,
    "fries": 95,
    "samosa": 18,
    "cold-drink": 60,
    "ice-cream": 150,
    "coffee": 50
}

cart = {}
total = 0

print("\n========== WELCOME TO ELITEENCLAVE ==========\n")

print("----------- MENU -----------")
for item, price in menu.items():
    print(f"{item.capitalize():12} : ₹{price}")
print("----------------------------")

while True:
    food = input("\nSelect an item (q to quit): ").lower()

    if food == "q":
        break

    if food in menu:
        try:
            qty = int(input(f"Enter quantity for {food}: "))
            if qty <= 0:
                print("Quantity must be greater than 0.")
                continue

            if food in cart:
                cart[food] += qty
            else:
                cart[food] = qty

            print(f"{food.capitalize()} added to cart.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Item not in menu. Try again.")

print("\n=========== ELITEENCLAVE BILL ===========")

if not cart:
    print("Your cart is empty.")
else:
    print(f"{'Item':12}{'Qty':>5}{'Price':>10}{'Total':>10}")
    print("-" * 40)

    for item, qty in cart.items():
        price = menu[item]
        cgst = total * 0.003
        sgst = total * 0.003
        item_total = price * qty
        total += item_total
        sum_total = total + cgst + sgst
        print(f"{item.capitalize():12}{qty:>5}{price:>10}{item_total:>10}")

    print("-" * 40)
    print(f"{'Grand Total':>30} : ₹{sum_total}")
    print("\nThank you for choosing EliteEnclave.")
    print("Experience quality. Experience class.")
