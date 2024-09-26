import sqlite3

# Carregamento: salvar os dados transformados no SQLite
def load(df, db_name='dados_transformados.db', table_name='dados'):
    # Conectar ao banco de dados SQLite (ou criar um novo)
    conn = sqlite3.connect(db_name)
    
    # Carregar o DataFrame para o banco de dados (substituir a tabela se ela já existir)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    # Fechar a conexão
    conn.close()

# Exemplo de uso
load(df_transformed)
print("Dados carregados com sucesso no banco de dados SQLite.")
