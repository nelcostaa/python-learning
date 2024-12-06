convidados = ["fafael", "andre", "nicholas"]
print(
    f"{convidados[0].title()}, {convidados[1].title()} e {convidados[2].title()} encontrei uma mesa maior"
)
convidados.insert(0, "noslen")
convidados.insert(2, "edu")
convidados.append("jones")

print(f"ei {convidados[0]} voce esta convidados para minha festa")
print(f"ei {convidados[1]} voce esta convidados para minha festa")
print(f"ei {convidados[2]} voce esta convidados para minha festa")
print(f"ei {convidados[3]} voce esta convidados para minha festa")
print(f"ei {convidados[4]} voce esta convidados para minha festa")
print(f"ei {convidados[5]} voce esta convidados para minha festa")

print(len(convidados))
