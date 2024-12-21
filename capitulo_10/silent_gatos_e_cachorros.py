from pathlib import Path


def mostrar_linhas_arquivo(conteudo):
    """Mostra linha por linha o conteudo de um arquivo"""
    linhas = conteudo.splitlines()

    print("\nConteudo do arquivo lido:")
    for linha in linhas:
        print(linha)


def ler_arquivo(file_path):
    """Le um arquivo e mostra no terminal linha por linha"""
    try:
        conteudo = file_path.read_text()
    except FileNotFoundError:
        pass
    else:
        mostrar_linhas_arquivo(conteudo)


path = Path("capitulo_10/cats.txt")
ler_arquivo(path)

path = Path("dogs.txt")
ler_arquivo(path)
