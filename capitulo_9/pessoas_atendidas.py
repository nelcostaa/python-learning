class Restaurante:
    """uma classe que representa um restaurente"""

    def __init__(self, nome_restaurante, tipo_cozinha) -> None:
        """Inicializa os atributos nome e tipo"""
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha
        self.qntd_servidas = 0

    def descrever_restaurante(self):
        """Mostra um resumo do que o restaurante e"""
        print(f"\nO {self.nome_restaurante} tem a cozinha do tipo {self.tipo_cozinha}")

    def abrir_restaurante(self):
        """Mostra uma mensagem para abrir o restaurante"""
        print(f"\nO {self.nome_restaurante.title()} esta aberto!")

    def mostrar_qntd_servidas(self):
        """Mostra quantas pessoas ja foram servidas no restaurante"""
        print(f"\n{self.qntd_servidas} ja foram servidas!")

    def definir_qntd_servidas(self, qntd_servidas):
        """Muda a quantidade de pessoas servidas no restaurante"""
        self.qntd_servidas = qntd_servidas

    def incrementar_qntd_servidas(self, servidos):
        self.qntd_servidas += servidos


meu_restaurante = Restaurante("Outback", "Americana")

meu_restaurante.mostrar_qntd_servidas()

meu_restaurante.qntd_servidas = 12
meu_restaurante.mostrar_qntd_servidas()

meu_restaurante.definir_qntd_servidas(24)
meu_restaurante.mostrar_qntd_servidas()

meu_restaurante.incrementar_qntd_servidas(150)
meu_restaurante.mostrar_qntd_servidas()
