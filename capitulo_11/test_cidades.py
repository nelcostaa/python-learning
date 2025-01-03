from cidade_funcoes import criar_cidade_pais


def test_cidade_pais():
    """A formatacao "cidade, pais" funciona?"""
    cidade_pais = criar_cidade_pais("boa vista", "brasil")
    assert cidade_pais == "Boa Vista, Brasil"


def test_cidade_pais_populacao():
    """A formatacao com o arguemnto opcional "populacao" funcionara?"""
    formato_completo = criar_cidade_pais("Boa Vista", "Brasil", populacao=300_000)
    assert formato_completo == "Boa Vista, Brasil - populacao 300000"
