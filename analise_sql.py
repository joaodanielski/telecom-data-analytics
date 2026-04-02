import sqlite3
import pandas as pd

conn = sqlite3.connect('provedor_telecom.db')

print("\n" + "="*50)
print(" KPI 1: Distribuicao da Base por Tecnologia")
print(" Contexto: Qual a nossa dependencia atual da tecnologia via radio?")
print("="*50)
query_tec = """
SELECT 
    p.tecnologia,
    SUM(f.qtd_acessos) AS total_acessos,
    ROUND((SUM(f.qtd_acessos) * 100.0) / (SELECT SUM(qtd_acessos) FROM fato_acessos), 2) AS percentual_base
FROM fato_acessos f
JOIN dim_produto p ON f.id_produto = p.id_produto
GROUP BY p.tecnologia;
"""
df_tec = pd.read_sql_query(query_tec, conn)
print(df_tec)


print("\n" + "="*50)
print(" KPI 2: Perfil do Cliente B2B (PJ) na Fibra")
print(" Contexto: Quais velocidades nossos clientes corporativos mais consomem?")
print("="*50)
query_pj = """
SELECT 
    p.velocidade,
    SUM(f.qtd_acessos) AS total_acessos_pj
FROM fato_acessos f
JOIN dim_cliente c ON f.id_cliente = c.id_cliente
JOIN dim_produto p ON f.id_produto = p.id_produto
WHERE c.tipo_cliente = 'PJ' AND p.tecnologia = 'Fibra'
GROUP BY p.velocidade
ORDER BY total_acessos_pj DESC;
"""
df_pj = pd.read_sql_query(query_pj, conn)
print(df_pj)


print("\n" + "="*50)
print(" KPI 3: Top 3 Cidades com Maior Volume de Acessos")
print(" Contexto: Onde esta concentrada nossa receita principal?")
print("="*50)
query_cidades = """
SELECT 
    g.cidade,
    SUM(f.qtd_acessos) AS volume_acessos
FROM fato_acessos f
JOIN dim_geografia g ON f.id_geografia = g.id_geografia
GROUP BY g.cidade
ORDER BY volume_acessos DESC
LIMIT 3;
"""
df_cidades = pd.read_sql_query(query_cidades, conn)
print(df_cidades)

conn.close()