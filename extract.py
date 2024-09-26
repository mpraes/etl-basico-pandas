import pandas as pd

# Extração: leitura de dados de um arquivo CSV
def extract(file_path):
    df = pd.read_csv(file_path)
    return df
