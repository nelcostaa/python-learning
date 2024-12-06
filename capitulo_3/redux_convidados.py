convidados = ["fafael", "andre", "nicholas"]
print(
    f"{convidados[0].title()}, {convidados[1].title()} e {convidados[2].title()} encontrei uma mesa maior"
)
convidados.insert(0, "noslen")
convidados.insert(2, "edu")
convidados.append("jones")

print("poderei convidar so 2 pessoas para jantar")

convidado_removido = convidados.pop()
print(f"Lamento {convidado_removido} mas nao poderei chama-lo")
convidado_removido = convidados.pop()
print(f"Lamento {convidado_removido} mas nao poderei chama-lo")
convidado_removido = convidados.pop()
print(f"Lamento {convidado_removido} mas nao poderei chama-lo")
convidado_removido = convidados.pop()
print(f"Lamento {convidado_removido} mas nao poderei chama-lo")

print(f"ei {convidados[0]} voce esta convidados para minha festa")
print(f"ei {convidados[1]} voce esta convidados para minha festa")

del convidados[0]
del convidados[0]

print(convidados)
