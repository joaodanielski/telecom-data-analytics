import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(page_title="Dashboard ISP Telecom", layout="wide")
st.title("Dashboard de Análise de Acessos")

@st.cache_data 
def carregar_dados():
    conn = sqlite3.connect('provedor_telecom.db')
    query = """
    SELECT 
        t.ano, t.mes, 
        g.estado, g.cidade, g.zona, 
        c.tipo_cliente, 
        p.tecnologia, p.velocidade, 
        f.qtd_acessos
    FROM fato_acessos f
    JOIN dim_tempo t ON f.id_tempo = t.id_tempo
    JOIN dim_geografia g ON f.id_geografia = g.id_geografia
    JOIN dim_cliente c ON f.id_cliente = c.id_cliente
    JOIN dim_produto p ON f.id_produto = p.id_produto
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

df = carregar_dados()

st.sidebar.header("Filtros Estratégicos")
ano_selecionado = st.sidebar.selectbox("Selecione o Ano", df['ano'].unique())

df_filtrado = df[df['ano'] == ano_selecionado]

total_acessos = df_filtrado['qtd_acessos'].sum()
acessos_fibra = df_filtrado[df_filtrado['tecnologia'] == 'Fibra']['qtd_acessos'].sum()
pct_fibra = (acessos_fibra / total_acessos) * 100 if total_acessos > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total de Acessos Ativos", f"{total_acessos:,}")
col2.metric("Acessos em Fibra (FTTH)", f"{acessos_fibra:,}")
col3.metric("Penetração de Fibra", f"{pct_fibra:.1f}%")

st.markdown("---")

colA, colB = st.columns(2)

with colA:
    st.subheader("Top Cidades por Volume de Acessos")
    df_cidades = df_filtrado.groupby('cidade')['qtd_acessos'].sum().reset_index()
    df_cidades = df_cidades.sort_values('qtd_acessos', ascending=False).head(5)
    
    fig_cidades = px.bar(df_cidades, x='qtd_acessos', y='cidade', orientation='h', text_auto=True, color_discrete_sequence=['#1f77b4'])
    fig_cidades.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_cidades, use_container_width=True)

with colB:
    st.subheader("Distribuição do Perfil de Cliente (PF vs PJ)")
    df_cliente = df_filtrado.groupby('tipo_cliente')['qtd_acessos'].sum().reset_index()
    
    fig_cliente = px.pie(df_cliente, values='qtd_acessos', names='tipo_cliente', hole=0.4, color_discrete_sequence=['#ff7f0e', '#2ca02c'])
    st.plotly_chart(fig_cliente, use_container_width=True)