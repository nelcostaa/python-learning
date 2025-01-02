from pathlib import Path
import json


def recieve_number():
    number = input("Type a random number: ")
    return number


def write_content(path):
    """Escreve o conteudo de numeros dados pelo usr"""
    number = recieve_number()
    contents = json.dumps(number)
    path.write_text(contents)


path = Path("capitulo_10/fav_number.txt")
write_content(path)
