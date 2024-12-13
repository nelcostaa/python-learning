class Usuario:
    """Representa a criacao de um usuario"""

    def __init__(self, nome, sobrenome, idade, cidade) -> None:
        """Inializa o usuario"""
        self.nome = nome.title()
        self.sobrenome = sobrenome.title()
        self.idade = idade
        self.cidade = cidade.title()

    def descrever_usuario(self):
        """Mostra um descricao das informacoes do usuario"""
        msg = f"O {self.nome} {self.sobrenome} tem {self.idade}"
        msg += f" e mora em {self.cidade}"
        print(f"\n{msg}")

    def cumprimentar_usuario(self):
        """Mostra uma mensagem de boas vindas ao usuario"""
        msg = f"Bem vindo ao nosso site {self.nome} {self.sobrenome}!"
        print(f"\n{msg}")


usuario_1 = Usuario("nelson", "costa", 22, "curitiba")
usuario_1.descrever_usuario()
usuario_1.cumprimentar_usuario()

usuario_2 = Usuario("julio", "costa", 42, "joao pessoa")
usuario_2.descrever_usuario()
usuario_2.cumprimentar_usuario()

usuario_3 = Usuario("Jonas", "Rodrigues", 32, "Boganvile")
usuario_3.descrever_usuario()
usuario_3.cumprimentar_usuario()
