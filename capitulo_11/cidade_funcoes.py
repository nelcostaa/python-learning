"""Modulo com funcoes para criacao de uma cidade e o pais onde esta"""


def criar_cidade_pais(nome_cidade, nome_pais, populacao=None):
    if populacao:
        cidade_pais = f"{nome_cidade.title()}, {nome_pais.title()}"
        cidade_pais += f" - populacao {populacao}"
    else:
        cidade_pais = f"{nome_cidade.title()}, {nome_pais.title()}"
    return cidade_pais
