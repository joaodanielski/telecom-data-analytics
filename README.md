# Projeto de BI - Provedor de Telecomunicações (ISP)

## Contexto do Negócio

Este projeto simula o ambiente de dados de um provedor de internet regional. O objetivo principal foi estruturar uma base de dados analítica e desenvolver um dashboard executivo para monitorar a base de assinantes, identificar gargalos tecnológicos (dependência de internet via rádio) e mapear oportunidades de _upsell_ no segmento B2B (Pessoas Jurídicas).

## Arquitetura e Tecnologias

O projeto foi construído de ponta a ponta (Full Stack Data), passando por engenharia, análise e visualização de dados:

- **Gerador de Dados:** Python (Mock de 5.000 registros com regras de negócio aplicadas).
- **ETL & Data Warehouse:** Python (Pandas) para transformação e **SQLite** para armazenamento local.
- **Modelagem Dimensional:** Star Schema (Tabela Fato de acessos e Dimensões de Tempo, Geografia, Cliente e Produto).
- **Data Viz (Dashboard):** Python utilizando **Streamlit** e **Plotly** para construção da aplicação web analítica.

## Principais Insights de Negócio

Ao analisar o dashboard gerado, destacam-se as seguintes conclusões estratégicas:

1. **Oportunidade de Migração (Churn Reduction):**
   Notou-se uma alta concentração de clientes na zona rural utilizando tecnologia via Rádio. Essa tecnologia possui alto custo de manutenção e sofre com instabilidades climáticas. Há uma clara oportunidade de projeto para expansão de cabeamento de Fibra (FTTH) nessas regiões para fidelizar essa base.

2. **Foco no Segmento B2B (PJ):**
   O gráfico de perfil de clientes indica um volume considerável de clientes PJ. Cruzando com as métricas de velocidade no banco de dados, nota-se que campanhas de _upsell_ (venda de planos superiores, como 1 Gbps) direcionadas exclusivamente a esses clientes podem elevar o Ticket Médio (ARPU) da empresa sem necessidade de expansão de infraestrutura física.

3. **Concentração de Receita:**
   O Top 5 Cidades demonstra onde o provedor tem maior penetração. Esses dados são fundamentais para a equipe de Marketing direcionar suas campanhas de tráfego pago geolocalizado, otimizando o Custo de Aquisição de Clientes (CAC).

## Como executar este projeto

1. Clone o repositório.
2. Instale as dependências: `pip install pandas sqlite3 streamlit plotly`
3. (Opcional) Gere uma nova base de dados rodando: `python gerador_dados.py`
4. Crie o Data Warehouse rodando: `python etl_sqlite.py`
5. Inicie o Dashboard: `python -m streamlit run dashboard.py`
