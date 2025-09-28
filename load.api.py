import pandas as pd
import psycopg2

# Lê o CSV transformado
df = pd.read_csv('rick_and_morty_characters_transformed.csv')

# Conexão com o PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Sml@2998"
)
cur = conn.cursor()

# Cria a tabela (se não existir)
cur.execute("""
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY,
    name TEXT,
    status TEXT,
    species TEXT,
    gender TEXT,
    origin_name TEXT,
    location_name TEXT
)
""")

# Insere os dados
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO characters (id, name, status, species, gender, origin_name, location_name)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
    """, tuple(row))

conn.commit()
cur.close()
conn.close()
print("Dados carregados no PostgreSQL!")