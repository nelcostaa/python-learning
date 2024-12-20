from pathlib import Path

path = Path("capitulo_10/lista_convidados.txt")

prompt_convidado = "Digite o nome do pessoa que voce deseja convidar"
prompt_convidado += "\n(digite 'quit' para parar) "

convidados = ""
while True:
    convidado = input(prompt_convidado)
    if convidado == "quit":
        break

    convidados += f"{convidado.title()}\n"

path.write_text(convidados)
