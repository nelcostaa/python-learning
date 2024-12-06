linguagens_favoritas = {
    "rafael": "rust",
    "eduardo": "solidity",
    "kleber": "python",
    "urian": "java",
}

should_particiate = ["nath", "ricardo", "rafael"]

for pessoa in should_particiate:
    if pessoa in linguagens_favoritas.keys():
        print(f"Obrigado por responder {pessoa}")
    else:
        print(f"Porfavor {pessoa} responda a pesquisa!")
