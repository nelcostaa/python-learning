rios_e_cidades = {
    "danubio": "europa",
    "reno": "Estrasburgo",
    "Tamisa": "Londres",
}

for rio, cidade in rios_e_cidades.items():
    print(f"O rio {rio} passa pela {cidade}")

for rio in sorted(rios_e_cidades.keys()):
    print(rio.title())

for cidade in rios_e_cidades.values():
    print(cidade)
