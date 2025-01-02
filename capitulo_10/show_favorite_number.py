from pathlib import Path
import json

path = Path("capitulo_10/fav_number.txt")


def show_content(path):
    contents = path.read_text()
    numbers = json.loads(contents)
    print(numbers)


show_content(path)
