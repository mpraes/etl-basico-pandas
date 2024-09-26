def transform(df):
    # Transformação: Exemplo de transformação simples (remover linhas com valores nulos e converter colunas)
    df = df.dropna()  # Remove linhas com valores nulos
    df['valor'] = df['valor'].astype(float)  # Converte a coluna 'valor' para tipo float
    df['data'] = pd.to_datetime(df['data'])  # Converte a coluna 'data' para datetime
    return df

# Exemplo de uso
df_transformed = transform(df)
print(df_transformed.head())  # Visualizar os dados transformados
