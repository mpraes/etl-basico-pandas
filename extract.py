import pandas as pd

# Extração: leitura de dados de um arquivo CSV
def extract(file_path):
    df = pd.read_csv(file_path)
    return df

# Exemplo de uso
file_path = 'dados.csv'  # Substitua pelo caminho do seu arquivo CSV
df = extract(file_path)
print(df.head())  # Visualizar os primeiros registros
