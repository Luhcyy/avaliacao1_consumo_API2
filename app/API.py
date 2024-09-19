import requests

# Consulta GraphQL para buscar por ID
fetch_query = '''
query ($id: Int) {
  Media (id: $id, type: ANIME) { 
    id
    title {
      romaji
      english
      native
    }  
    description 
    startDate {
      year
    }
    episodes
  }
}
'''

# Consulta GraphQL para buscar por nome
search_query = '''
query ($search: String) {
  Page { 
    media (search: $search, type: ANIME) { 
      id
      title {
        romaji
        english
        native
      }
      startDate {
        year
      }   
    }
  }
}
'''

URL = 'https://graphql.anilist.co'


def fetchData(id):
    variables = {'id': id}
    response = requests.post(
        URL, json={'query': fetch_query, 'variables': variables}
    )
    response.raise_for_status()  
    return response.json()
  
    
def searchAnimesByName(searchTerm):
    variables = {'search': searchTerm}
    response = requests.post(
        URL, json={'query': search_query, 'variables': variables}
    )
    
    response.raise_for_status()  
    return response.json()
