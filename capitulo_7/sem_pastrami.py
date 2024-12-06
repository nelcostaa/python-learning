pedidos_sanduiche = [
    "atum",
    "pastrami",
    "carne",
    "pastrami",
    "frango",
    "pastrami",
]

pedidos_concluidos = []

print("Os sanduiche de pastrami acabaram!\n")
while "pastrami" in pedidos_sanduiche:
    pedidos_sanduiche.remove("pastrami")

while pedidos_sanduiche:
    pedido_atual = pedidos_sanduiche.pop()
    print(f"Seu sanduiche de {pedido_atual} esta pronto!")
    pedidos_concluidos.append(pedido_atual)


print("\nOs seguintes sanduiches foram feitos:")
for pedido in pedidos_concluidos:
    print(f"\t-{pedido}")
