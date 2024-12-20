from pathlib import Path

path = Path("capitulo_10/aprendi_no_python.txt")
conteudo = path.read_text()

for linha in conteudo.splitlines():
    linha = linha.replace("python", "C")
    print(linha)
