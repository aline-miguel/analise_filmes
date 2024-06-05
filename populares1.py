import requests
import pandas as pd

API_KEY = ''
BASE_URL = 'https://api.themoviedb.org/3'

def filmes_populares(api_key, page=1):
    url = f"{BASE_URL}/movie/popular"
    parametros = {
        'api_key': api_key,
        'page': page
    }
    resposta = requests.get(url, params=parametros)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        resposta.raise_for_status()

def coletar_filmes(api_key, num_pages=10):
    todos_filmes = []
    for page in range(1, num_pages + 1):
        data = filmes_populares(api_key, page)
        todos_filmes.extend(data['results'])
    return todos_filmes

def normalize_filmes(filmes_data):
    filmes_df = pd.json_normalize(filmes_data)
    
    # Desmembrar os gêneros (genres)
    lista_generos = []
    for filmes in filmes_data:
        for genero in filmes['genre_ids']:
            lista_generos.append({'movies_id': filmes['id'], 'genre_id': genero})
    
    generos_df = pd.DataFrame(lista_generos)
    
    return filmes_df, generos_df

def save_data_to_csv(df, file_name):
    df.to_csv(file_name, index=False)

if __name__ == "__main__":
    num_pages = 10
    filme_data = coletar_filmes(API_KEY, num_pages)
    filmes_df, generos_df = normalize_filmes(filme_data)
    
    save_data_to_csv(filmes_df, 'tmdb_filmes.csv')
    save_data_to_csv(generos_df, 'tmdb_generos_filmes.csv')
    
    print("Dados salvos em tmdb_filmes.csv e tmdb_generos_filmes.csv")
