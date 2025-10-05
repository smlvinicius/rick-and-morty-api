import requests
import pandas as pd

# Faz a requisição para todas as páginas da API do Rick and Morty
url = 'https://rickandmortyapi.com/api/character'

response = requests.get(url)
data = response.json()

#Inicializa uma lista para armazenar todos os personagens
all_characters = []

# Loop for para percorrer todas as páginas
for page in range(1,data['info']['pages']+1):
    response = requests.get(f'{url}?page={page}')
    data = response.json()
    all_characters.extend(data['results'])  # Adiciona os personagens da página atual à lista
    print(f'Página {page} processada.')

# Converte a lista de personagens em um DataFrame do pandas
df = pd.DataFrame(all_characters)
print(df.head())

# Conta o número total de personagens extraídos
df_count = len(df)
print(f'Total de personagens extraídos: {df_count}')

# Salva o DataFrame em um arquivo CSV
df.to_csv('rick_and_morty_characters.csv', index=False)
print("Extração concluída e salva em 'rick_and_morty_characters.csv'")





