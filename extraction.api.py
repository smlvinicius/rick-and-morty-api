import requests
import pandas as pd

#Faz a requisição para a API do Rick and Morty
url = 'https://rickandmortyapi.com/api'
response = requests.get(url)
data = response.json()

# Extrai e imprime os dados dos personagens
characters_url = f"{url}/character"
characters_response = requests.get(characters_url)
characters_data = characters_response.json()

df = pd.DataFrame(characters_data['results'])

# Salva os dados em um arquivo CSV
df.to_csv('rick_and_morty_characters.csv', index=False)
print("Dados dos personagens salvos em 'rick_and_morty_characters.csv'")





