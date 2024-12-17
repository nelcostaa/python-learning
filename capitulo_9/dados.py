from random import randint


class Dado:
    """Uma classe simples que representa um dado de jogos"""

    def __init__(self, lados) -> None:
        """Inicializa a criacao do dado"""
        self.lados = lados

    def rolar_dado(self):
        """Modela a jogada do dado conforme qntd de lados"""
        lado = randint(1, self.lados)
        return lado


d6 = Dado(6)

resultados = []
for roll_num in range(10):
    resultado = d6.rolar_dado()
    resultados.append(resultado)
print("\nO resultado do dado de 6 lados rodado 10 vezes foi:")
print(resultados)
