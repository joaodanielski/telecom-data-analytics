import pandas as pd
import sqlite3

print("Iniciando o processo de ETL...")

df = pd.read_csv('acessos_provedor.csv')

conn = sqlite3.connect('provedor_telecom.db')


dim_tempo = df[['ano', 'mes']].drop_duplicates().reset_index(drop=True)
dim_tempo['id_tempo'] = dim_tempo.index + 1
dim_tempo.to_sql('dim_tempo', conn, if_exists='replace', index=False)

dim_geografia = df[['estado', 'cidade', 'zona']].drop_duplicates().reset_index(drop=True)
dim_geografia['id_geografia'] = dim_geografia.index + 1
dim_geografia.to_sql('dim_geografia', conn, if_exists='replace', index=False)

dim_cliente = df[['tipo_cliente']].drop_duplicates().reset_index(drop=True)
dim_cliente['id_cliente'] = dim_cliente.index + 1
dim_cliente.to_sql('dim_cliente', conn, if_exists='replace', index=False)

dim_produto = df[['tecnologia', 'velocidade']].drop_duplicates().reset_index(drop=True)
dim_produto['id_produto'] = dim_produto.index + 1
dim_produto.to_sql('dim_produto', conn, if_exists='replace', index=False)

fato = df.merge(dim_tempo, on=['ano', 'mes'])
fato = fato.merge(dim_geografia, on=['estado', 'cidade', 'zona'])
fato = fato.merge(dim_cliente, on=['tipo_cliente'])
fato = fato.merge(dim_produto, on=['tecnologia', 'velocidade'])

fato_acessos = fato[['id_tempo', 'id_geografia', 'id_cliente', 'id_produto', 'qtd_acessos']]

fato_acessos.to_sql('fato_acessos', conn, if_exists='replace', index=False)

conn.close()

print("ETL concluido com sucesso!")
print("O banco de dados 'provedor_telecom.db' foi gerado e esta modelado em Star Schema.")