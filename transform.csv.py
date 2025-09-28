import pandas as pd
import ast

# Lê o CSV extraído
df = pd.read_csv('rick_and_morty_characters.csv')

# Transforma os dados extraídos
def extract_name(field, default=''):
    if isinstance(field, dict) and 'name' in field:
        return field['name']
    return default

# Usa o DataFrame já carregado do CSV
df['origin_name'] = df['origin'].apply(lambda x: extract_name(x))
df['location_name'] = df['location'].apply(lambda x: extract_name(x))

# Seleciona apenas as colunas desejadas
df_transformed = df[['id', 'name', 'status', 'species', 'gender', 'origin_name', 'location_name']]

# Salva o resultado transformado
df_transformed.to_csv('rick_and_morty_characters_transformed.csv', index=False)
print("Extração e transformação concluídas em 'rick_and_morty_characters_transformed.csv'")