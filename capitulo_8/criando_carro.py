def criar_carro(marca, modelo, **kwargs):
    """Cria o modelo de um carro de determinada marca com varias infos"""
    kwargs["marca"] = marca
    kwargs["modelo"] = modelo

    return kwargs
