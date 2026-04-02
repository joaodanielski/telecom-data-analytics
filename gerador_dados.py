import pandas as pd
import random

meses = list(range(1, 13))
anos = [2025, 2026]
cidades = ['São Paulo - SP', 'Campinas - SP', 'Ribeirão Preto - SP', 'Bauru - SP', 'Franca - SP']
zonas = ['Urbana', 'Rural']
tipos_cliente = ['PF', 'PJ']
tecnologias = ['Fibra', 'Rádio']
velocidades_fibra = ['300 Mbps', '500 Mbps', '1 Gbps']
velocidades_radio = ['10 Mbps', '20 Mbps', '50 Mbps']

dados = []

for _ in range(5000):
    ano = random.choice(anos)
    mes = random.choice(meses)
    
    cidade_estado = random.choice(cidades).split(' - ')
    cidade, estado = cidade_estado[0], cidade_estado[1]
    
    zona = random.choices(zonas, weights=[0.8, 0.2])[0] # 80% Urbano
    tipo_cliente = random.choices(tipos_cliente, weights=[0.85, 0.15])[0] # 85% PF
    
    if zona == 'Rural':
        tecnologia = random.choices(tecnologias, weights=[0.3, 0.7])[0] 
    else:
        tecnologia = random.choices(tecnologias, weights=[0.9, 0.1])[0] 
        
    velocidade = random.choice(velocidades_fibra) if tecnologia == 'Fibra' else random.choice(velocidades_radio)
    
    qtd_acessos = random.randint(1, 10) if tipo_cliente == 'PF' else random.randint(5, 50)

    dados.append([ano, mes, estado, cidade, zona, tipo_cliente, tecnologia, velocidade, qtd_acessos])

df = pd.DataFrame(dados, columns=['ano', 'mes', 'estado', 'cidade', 'zona', 'tipo_cliente', 'tecnologia', 'velocidade', 'qtd_acessos'])
df.to_csv('acessos_provedor.csv', index=False)
print("Arquivo acessos_provedor.csv gerado com sucesso!")