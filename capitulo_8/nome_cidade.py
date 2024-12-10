def cidade_pais(n_cidade, pais_cidade) -> str:
    """retorna uma string formatada com o nome da cidade e seu pais"""
    nome_formatado = n_cidade.title() + ", " + pais_cidade.title()
    return nome_formatado


cidade = cidade_pais("orlando", "estados unidos")
print(cidade)

cidade = cidade_pais("curitiba", "brasil")
print(cidade)

cidade = cidade_pais("vancouver", "canada")
print(cidade)
