from cmd import PROMPT
from pathlib import Path
import json


def get_stored_user_infos(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_infos = json.loads(contents)
        return user_infos
    else:
        return None


def get_new_user_infos(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    age = input("Whats your age? ")
    age = int(age)
    user_city = input("Which city you're born? ")

    user_infos = {
        "username": username,
        "age": age,
        "city_of_birth": user_city,
    }

    contents = json.dumps(user_infos)
    path.write_text(contents)
    return user_infos


def mostrar_infos_usuario(user_infos):
    """Mostra as informacoes de um usuario no terminal"""

    print(f"The user {user_infos['username'].title()} has this infos: ")
    print(f"\t- {user_infos['age']}")
    print(f"\t- {user_infos['city_of_birth'].title()}")


def verify_user(user_infos):
    """Verifica se o usuario que esta executando esta correto"""
    prompt = f"Are you {user_infos['username']}? (Y|N)"
    asnwer = input(prompt)

    if asnwer.lower() == "y":
        return True

    return False


def greet_user():
    """Greet the user by name."""
    path = Path("user_infos.json")
    user_infos = get_stored_user_infos(path)

    if user_infos:
        if verify_user(user_infos):
            mostrar_infos_usuario(user_infos)
            return

    user_infos = get_new_user_infos(path)
    mostrar_infos_usuario(user_infos)


greet_user()
