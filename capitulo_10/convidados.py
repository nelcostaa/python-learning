from pathlib import Path

convidado = input("Qual o nome do convidado que voce ira chamar? ")

path = Path("capitulo_10/lista_convidados")
path.write_text(convidado)
