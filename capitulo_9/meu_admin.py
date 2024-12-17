from administrador import Administrador

ceo = Administrador("John", "Calvin", 500, "Inglaterra")
ceo.descrever_usuario()

ceo.privilegios.privilegios = [
    "pode banir usuarios",
    "pode adicionar post",
    "pode deletar post",
]
ceo.privilegios.mostrar_privilegios()
