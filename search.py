from API import searchAnimesByName, saveData, fetchData
from display import displaySearchData, displayIdData
import requests

def searchByName(searchTerm, filename='data.json'):
    """
    Busca animes pelo nome e salva os dados em um arquivo JSON.

    :param searchTerm: Nome do anime para buscar.
    :param filename: Nome do arquivo onde os dados serão salvos.
    """
    try:
        # Obtém os dados da busca por nome
        data = searchAnimesByName(searchTerm)
        return data
        
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return{}

def searchById(id, filename='data.json'):
    """
    Busca um anime pelo ID e salva os dados em um arquivo JSON.

    :param id: ID do anime para buscar.
    :param filename: Nome do arquivo onde os dados serão salvos.
    """
    try:
        # Obtém os dados da busca por ID
        data = fetchData(id)
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return {}
