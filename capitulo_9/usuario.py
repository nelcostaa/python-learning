"""Classe que pode ser usada para representar um usuario"""


class Usuario:
    """Representa a criacao de um usuario"""

    def __init__(self, nome, sobrenome, idade, cidade) -> None:
        """Inializa o usuario"""
        self.nome = nome.title()
        self.sobrenome = sobrenome.title()
        self.idade = idade
        self.cidade = cidade.title()
        self.tentativas_login = 0

    def descrever_usuario(self):
        """Mostra um descricao das informacoes do usuario"""
        msg = f"O {self.nome} {self.sobrenome} tem {self.idade} anos"
        msg += f" e mora em {self.cidade}"
        print(f"\n{msg}")

    def cumprimentar_usuario(self):
        """Mostra uma mensagem de boas vindas ao usuario"""
        msg = f"Bem vindo ao nosso site {self.nome} {self.sobrenome}!"
        print(f"\n{msg}")

    def mostrar_qntd_tentativas(self):
        """Mostra a quantidade de tentativas de login realizada"""
        print(f"{self.nome} voce ja realizou {self.tentativas_login} tentativas")

    def incrementar_tentativas_login(self):
        """Aumenta em 1 a quantidade de logins efetuada pelo user"""
        self.tentativas_login += 1

    def resetar_qntd_logins(self):
        """Muda a quantidade de logins feitas para zero"""
        self.tentativas_login = 0
