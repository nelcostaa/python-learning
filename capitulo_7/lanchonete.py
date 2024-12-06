pedidos_sanduiche = [
    "atum",
    "carne",
    "frango",
]

pedidos_concluidos = []

while pedidos_sanduiche:
    pedido_atual = pedidos_sanduiche.pop()
    print(f"Seu sanduiche de {pedido_atual} esta pronto!")
    pedidos_concluidos.append(pedido_atual)


print("\nOs seguintes sanduiches foram feitos:")
for pedido in pedidos_concluidos:
    print(f"\t-{pedido}")
