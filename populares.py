import requests
import pandas as pd

API_KEY = ''
BASE_URL = 'https://api.themoviedb.org/3'

# Função para obter gêneros de filmes
def get_nome_genero(api_key):
    url = f"{BASE_URL}/genre/movie/list"
    parametros = {
        'api_key': api_key
    }
    resposta = requests.get(url, params=parametros)
    if resposta.status_code == 200:
        return resposta.json()['genres']
    else:
        resposta.raise_for_status()

# Salvar os dados em um arquivo CSV
def save_data_to_csv(data, file_name):
    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)

# Main
if __name__ == "__main__":
    # Obter gêneros de filmes
    genero = get_nome_genero(API_KEY)
    
    # Salvar os gêneros em um arquivo CSV
    save_data_to_csv(genero, 'tmdb_nome_genero.csv')
    
    print("Dados dos gêneros salvos em tmdb_nome_genero.csv")

