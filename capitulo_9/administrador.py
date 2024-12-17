"""Classes usadas para representar a criacao de um administrador"""

from usuario import Usuario


class Privilegios:
    """Define os privilegios que um usuario tem"""

    def __init__(self, privilegios=[]) -> None:
        """Inicializa os privilegios"""
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        """Mostra os privilegios"""
        if self.privilegios:
            print("\nOs privilegios sao:")
            for privilegio in self.privilegios:
                print(f"\t-{privilegio}")


class Administrador(Usuario):
    """Representa um tipo de Usuario administrador"""

    def __init__(self, nome, sobrenome, idade, cidade) -> None:
        """Inicializa um administrador"""
        super().__init__(nome, sobrenome, idade, cidade)
        self.privilegios = Privilegios()
