def fazer_album(n_artista, titulo_album, num_musicas=None):
    """Constroi um dicionario contendo informacoes sobre um album"""
    album_dict = {
        "nome": n_artista.title(),
        "titulo": titulo_album.title(),
    }

    if num_musicas:
        album_dict["musicas"] = num_musicas
    return album_dict


nome_prompt = "Qual o nome do artista? "
album_prompt = "Qual o nome do album? "
musicas_prompt = "Qual numero de musicas? (Aperte ENTER para pular)"

print("Digite 'q' ao qualquer momento para sair!")

while True:
    n_artista = input(nome_prompt)
    if n_artista == "q":
        break

    nome_album = input(album_prompt)
    if nome_album == "q":
        break

    num_musicas = input(musicas_prompt)
    if num_musicas == "q":
        break
    elif num_musicas:
        album = fazer_album(n_artista, nome_album, num_musicas)
    else:
        album = fazer_album(n_artista, nome_album)

    print(album)
