from API import searchAnimesByName, fetchData
import requests

def searchByName(searchTerm):
    try:
        # Obtém os dados da busca por nome
        data = searchAnimesByName(searchTerm)
        return data
        
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return{}

def searchById(id):
    try:
        # Obtém os dados da busca por ID
        data = fetchData(id)
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return {}
