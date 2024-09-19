def displaySearchData(data):
    """
    Exibe as informações dos animes a partir dos dados fornecidos.

    :param data: Dados JSON contendo as informações dos animes.
    """
    animes = data.get('data', {}).get('Page', {}).get('media', [])
    if not animes:
        print("Nenhum anime encontrado.")
    for anime in animes:
        print("ID:", anime.get('id'))
        print("Titulo (Romaji):", anime.get('title', {}).get('romaji'))
        print("Titulo (Inglês):", anime.get('title', {}).get('english'))
        print("Titulo (Nativo):", anime.get('title', {}).get('native'))
        print("Data de lançamento:", anime.get('startDate', {}).get('year'), '\n')
        
def displayIdData(data):
    """
    Exibe as informações de um único anime a partir dos dados fornecidos.

    :param data: Dados JSON contendo as informações do anime.
    """
    anime = data.get('data', {}).get('Media', {})
    if not anime:
        print("Nenhum anime encontrado.")
    else:
        print("ID:", anime.get('id'))
        print("Titulo (Romaji):", anime.get('title', {}).get('romaji'))
        print("Titulo (Inglês):", anime.get('title', {}).get('english'))
        print("Titulo (Nativo):", anime.get('title', {}).get('native'))
        print("Data de lançamento:", anime.get('startDate', {}).get('year'), '\n')
        print("descrição (Inglês):", anime.get('description'), '\n')


