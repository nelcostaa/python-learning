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
        """Aumenta a quantidade de pessoas servidas conforme valor
        fornecido"""
        self.qntd_servidas += servidos


class EstandeDeSorvete(Restaurante):
    """Representa um simples estande sorveteria"""

    def __init__(self, nome_restaurante, tipo_cozinha="sorvete") -> None:
        """Inicializa o estande de sorvete"""
        super().__init__(nome_restaurante, tipo_cozinha)
        self.sabores = []

    def mostrar_sabores(self):
        """Mostra os sabores disponiveis no estande de sorveteria"""
        print("\nOs sabores disponiveis no restaurante sao:")
        for sabor in self.sabores:
            print(f"\t-{sabor.title()}")


minha_sorveteria = EstandeDeSorvete("PicNic")
minha_sorveteria.sabores = [
    "chocolate",
    "morango",
    "pistache",
    "napolitano",
    "limao",
]

minha_sorveteria.descrever_restaurante()
minha_sorveteria.mostrar_sabores()