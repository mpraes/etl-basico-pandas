from extract import extract
from transform import transform
from load import load

file_path = 'source_data/dados.csv' 

def etl_process(file_path):
    # ETL completo
    df = extract(file_path)
    df_transformed = transform(df)
    load(df_transformed)
    print("Processo ETL completo!")

# Executar o processo ETL
etl_process(file_path)
