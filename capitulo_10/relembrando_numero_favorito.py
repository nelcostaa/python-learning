from pathlib import Path
import json


def get_numero_armazenado(path):
    """Retorna o numero armazenado no arquivo"""
    if path.exists():
        conteudo = path.read_text()
        numero = json.loads(conteudo)
        return numero
    else:
        return None


def get_numero_favorito(path):
    """Escreve o conteudo de numeros dados pelo usuario"""
    number = input("Type a random number: ")
    number = int(number)
    contents = json.dumps(number)
    path.write_text(contents)

    return number


def show_content():
    """Mostra o numero favorito do usuario"""
    path = Path("numero_favorito.txt")
    numero = get_numero_armazenado(path)

    if numero:
        print(f"O seu numero favorito e: {numero}")
    else:
        numero = get_numero_favorito(path)
        print(f"O seu numero favorito e: {numero}")
