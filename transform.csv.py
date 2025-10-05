import pandas as pd
import ast

# Lê o CSV extraído
df = pd.read_csv('rick_and_morty_characters.csv')

# Transforma as colunas 'origin' e 'location' de strings para dicionários
df['origin'] = df['origin'].apply(ast.literal_eval)  # Converte string para dicionário
df['location'] = df['location'].apply(ast.literal_eval)  # Converte string para dicionário

# Extrai apenas o nome do local de origem e localização atual
df['origin_name'] = df['origin'].apply(lambda x: x['name']) # Extrai o nome do local de origem
df['location_name'] = df['location'].apply(lambda x: x['name']) # Extrai o nome do local de localização atual

# Seleciona as colunas relevantes para o carregamento no banco de dados
df_transformed = df[['id', 'name', 'status', 'species', 'gender', 'origin_name', 'location_name']]

# Salva o Dataframe transformado em um novo arquivo CSV
df_transformed.to_csv('rick_and_morty_characters_transformed.csv', index=False)
print("Transformação concluída e salva em 'rick_and_morty_characters_transformed.csv'")
