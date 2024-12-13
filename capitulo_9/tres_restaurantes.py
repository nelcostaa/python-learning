class Restaurante:
    """uma classe que representa um restaurente"""

    def __init__(self, nome_restaurante, tipo_cozinha) -> None:
        """Inicializa os atributos nome e tipo"""
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha

    def descrever_restaurante(self):
        """Mostra um resumo do que o restaurante e"""
        print(f"\nO {self.nome_restaurante} tem a cozinha do tipo {self.tipo_cozinha}")

    def abrir_restaurante(self):
        """Mostra uma mensagem para abrir o restaurante"""
        print(f"\nO {self.nome_restaurante.title()} esta aberto!")


restaurante_1 = Restaurante("McDonalds", "fastfood")
restaurante_2 = Restaurante("BurgerKing", "fastfood")
restaurante_3 = Restaurante("Coco Bambu", "Tropical")

restaurante_1.descrever_restaurante()
restaurante_2.descrever_restaurante()
restaurante_3.descrever_restaurante()
