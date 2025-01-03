class Funcionario:
    """Classe para representar um funcionario"""

    def __init__(self, nome, sobrenome, salario_anual) -> None:
        """Inicializa os dados de um funcionario"""
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario_anual = salario_anual

    def dar_aumento(self, aumento=5000):
        """Aumenta o salario do funcionario"""
        self.salario_anual += aumento
