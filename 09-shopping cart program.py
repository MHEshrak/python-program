# Shopping cart exercise

# foods = []
# prices = []
# total = 0

# while True:
# food = input("Enter a food to buy (q to quit): ")
# if food.lower() == "q":
# break
# else:
# price = float(input(f"Enter the price of a {food}: $"))
# foods.append(food)
# prices.append(price)

# print("----- YOUR CART -----")

# for food in foods:
# print(food, end=" ")

# for price in prices:
# total += price

# print()
# print(f"Your total is: ${total}")

foods = []
prices = []
total_prices = 0

while True:
    food = input("Enter a food you like to buy ( q for quit ): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter the price of {food} : $"))
        foods.append(food)
        prices.append(price)

print("-----Your Cart-----")

for food in foods:
    print(food, end=" ")
print()
for price in prices:
    print(price, end=" ")
print()
for price in prices:
    total_prices = total_prices + price
print()
print(f"Your total is ${total_prices}")
