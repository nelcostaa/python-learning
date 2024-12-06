pizzas = [
    "calabresa ",
    "quatro-queijos ",
    "bacon",
]

for pizza in pizzas:
    print(f"Gosto de pizza de {pizza}")

print("\nComo eu amo pizza!")

friend_pizzas = pizzas[:]

pizzas.append("frango")
friend_pizzas.append("portuguesa")

print("\nMinhas pizzas favoritas sao:")
for pizza in pizzas:
    print(pizza)

print("\nMinhas pizzas favoritas sao:")
for pizza in friend_pizzas:
    print(pizza)
