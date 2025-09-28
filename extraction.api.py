import requests
import pandas as pd

# Faz a requisição para todas as páginas da API do Rick and Morty
url = 'https://rickandmortyapi.com/api/character'
all_characters = []

while url:
    response = requests.get(url)
    data = response.json()
    all_characters.extend(data['results'])
    url = data['info']['next']  # Próxima página ou None

df = pd.DataFrame(all_characters)

# Salva os dados em um arquivo CSV
df.to_csv('rick_and_morty_characters.csv', index=False)
print("Dados dos personagens salvos em 'rick_and_morty_characters.csv'")





