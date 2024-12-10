def fazer_album(n_artista, titulo_album, num_musicas=None):
    """Constroi um dicionario contendo informacoes sobre um album"""
    album_dict = {
        "nome": n_artista.title(),
        "titulo": titulo_album.title(),
    }

    if num_musicas:
        album_dict["musicas"] = num_musicas
    return album_dict


album = fazer_album("Projeto Sola", "Reforma")
print(album)

album = fazer_album("Purples", "Igreja", 5)
print(album)
