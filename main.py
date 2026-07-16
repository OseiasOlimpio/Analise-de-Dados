#"Exercicio proposto: destacar produtos mais vendidos, meses que o faturamento cai, resumo geral"

import numpy as np
import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt


# passo 1 - carregar dados 

df = pd.read_csv("data/superstore.csv", encoding="latin1")

# Explorando os dados
print("Formato base (linha e colunas): ", df.shape)
print("\n primeiras 5 linas:")
print(df.head())

print("\n Nome das Colunas:")
print(df.columns.tolist())

print("\n Tipos de Dados: ")
print(df.dtypes)

print("\nValores nulos por colunas: ")
print(df.isnull().sum())

#converter Order Date de texto para data 
df['Order Date'] = pd.to_datetime(df['Order Date'])

# =======Métricas========
faturamento_total = df['Sales'].sum()
ticket_medio = df['Sales'].mean()
qtd_pedidos = df['Order ID'].nunique()

print('-----------RESUMO GERAL-------------')
print(f"Faturamento total: ${faturamento_total:,.2f}")
print(f"Ticket Medio: ${ticket_medio:,.2f}")
print(f"Quantidade de pedidos unicos: {qtd_pedidos}")

#Produto mais vendido
produto_mais_vendido = df.groupby("Product Name")['Quantity'].sum().sort_values(ascending=False).head(1)
print("Produto mais vendido (em unidade): ")
print(produto_mais_vendido)


#Top 5 produtos mais vendidos
top5_produtos_receita = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(5)
print(f"\nTop 5 produtos por receita:")
print(top5_produtos_receita)


# =====Vendas por mês=====
df['AnoMes'] = df['Order Date'].dt.to_period('M')
vendas_mensais = df.groupby('AnoMes')['Sales'].sum()

print("\n====VENDAS POR MÊS====")
print(vendas_mensais)

#Vendas por mês
plt.figure(figsize=(12, 5))
vendas_mensais.plot(kind='line', marker='o')
plt.title("Faturamento por Mês")
plt.xlabel('Mês')
plt.ylabel("Vendas ($)")
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico de vendas mensais.png")
plt.show()

#Top 5 produtos por receita(gráfico de barras)
plt.figure(figsize=(10,5))
top5_produtos_receita.plot(kind='barh')
plt.title('Top 5 Produtos por Receita')
plt.xlabel('Vendas ($)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('grafico top 5 produtos.png')
plt.show()


#top categorias por receita
top_categorias = df.groupby("Category")['Sales'].sum().sort_values(ascending=False)
print(top_categorias)

#Sub-categorias
top_subcategorias = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(5)
print("\n==== TOP 5 SUB-CATEGORIAS =====")
print(top_subcategorias)