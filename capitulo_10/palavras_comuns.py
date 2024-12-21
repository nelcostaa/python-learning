from pathlib import Path

path = Path("capitulo_10/a_cidade_do_vicio.txt")
contents = path.read_text().rstrip()
print(contents)

contagem = contents.lower().count("hoje")
print(contagem)
