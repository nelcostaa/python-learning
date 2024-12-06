lugares_favoritos = {
    "Nelson": ["italia", "eua", "canada"],
    "Rafael": ["praia", "sao jose", "curitiba"],
    "andre": ["trabalho", "casa", "praia"],
}

for pessoa, lugares in lugares_favoritos.items():
    print(f"\nOs lugares favoritos do {pessoa.title()} sao:")
    for lugar in lugares:
        print(f"\t- {lugar.title()}")
