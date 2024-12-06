cidades = {
    "curitiba": {
        "country": "brasil",
        "population": "1_500_000",
        "fact": "cidade fria",
    },
    "orlando": {
        "country": "estados unidos",
        "population": "320_000",
        "fact": "la tem a disney",
    },
    "uberlandia": {
        "country": "brasil",
        "population": "800_000",
        "fact": "la tem queijo bom",
    },
}

for cidade, infos in cidades.items():
    print(f"\nAlgumas informacoes sobre {cidade}:")
    for info in infos.values():
        print(f"\t- {info}")
