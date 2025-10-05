import pandas as pd
import psycopg2

# Lê o CSV transformado
df = pd.read_csv('rick_and_morty_characters_transformed.csv')

# Conexão com o PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="seu_banco",
    user="seu_usuario",
    password="sua_senha"
)
cursor = conn.cursor()

cursor = conn.cursor()

# Cria a tabela no banco de dados com as colunas necessárias
cursor.execute("""
CREATE TABLE IF NOT EXISTS rick_and_morty_characters (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    status VARCHAR(50),
    species VARCHAR(50),
    gender VARCHAR(50),
    origin_name VARCHAR(100),
    location_name VARCHAR(100)
);
""")

conn.commit()
print("Tabela criada com sucesso.")

# Insere os dados do DataFrame na tabela do banco de dados
for index, row in df.iterrows(): # Percorre cada linha do DataFrame
    cursor.execute(
        """
        INSERT INTO rick_and_morty_characters 
        (id, name, status, species, gender, origin_name, location_name)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
        """,
        (
            row['id'], 
            row['species'],
            row['gender'],
            row['origin_name'],
            row['location_name']
        )
    )

conn.commit()
print("Dados inseridos com sucesso.")
