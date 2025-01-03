from funcionario import Funcionario
import pytest


@pytest.fixture
def funcionario():
    """Um funcionario que estara disponivel para todas as funcs de teste"""
    funcionario = Funcionario("Nelson", "Costa", 700)
    return funcionario


def test_dar_aumento_padrao(funcionario):
    """Teste se o aumento de salario padrao esta correto"""
    funcionario.dar_aumento()
    assert funcionario.salario_anual == 5700


def test_dar_aumento_customizado(funcionario):
    """Testa se o aumento de salario com um valor opcional esta correto"""
    funcionario.dar_aumento(1000)
    assert funcionario.salario_anual == 1700
