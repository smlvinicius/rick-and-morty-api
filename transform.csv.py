import pandas as pd
import ast

# Lê o CSV extraído
df = pd.read_csv('rick_and_morty_characters.csv')

# Extrai o nome do origin e location
df['origin_name'] = df['origin'].apply(lambda x: ast.literal_eval(x)['name'] if pd.notnull(x) else '')
df['location_name'] = df['location'].apply(lambda x: ast.literal_eval(x)['name'] if pd.notnull(x) else '')

# Seleciona apenas algumas colunas para o novo DataFrame
df_transformed = df[['id', 'name', 'status', 'species', 'gender', 'origin_name', 'location_name']]

# Salva o resultado transformado
df_transformed.to_csv('rick_and_morty_characters_transformed.csv', index=False)
print("Transformação concluída e salva em 'rick_and_morty_characters_transformed.csv'")