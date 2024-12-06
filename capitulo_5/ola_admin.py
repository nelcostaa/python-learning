nomes_usuarios = [
    "nelson,",
    "rafa,",
    "andre,",
    "admin",
    "nicholas",
]
if nomes_usuarios:
    for nome in nomes_usuarios:
        if nome == "admin":
            print("Ola admin....")
        else:
            print(f"Ola {nome}, obrigado por fazer login novamente")
else:
    print("sua lista esta vazia!")
