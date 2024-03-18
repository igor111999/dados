#!/usr/bin/env python
# coding: utf-8

# # Desafio: 
# 
# Você trabalha em uma grande empresa de Cartão de Crédito e o diretor da empresa percebeu que o número de clientes que cancelam seus cartões tem aumentado significativamente, causando prejuízos enormes para a empresa
# 
# O que fazer para evitar isso? Como saber as pessoas que têm maior tendência a cancelar o cartão?
# 
# # O que temos:
# 
# Temos 1 base de dados com informações dos clientes, tanto clientes atuais quanto clientes que cancelaram o cartão
# 
# Download da Base de Dados: Botão na página
# 
# Referência: https://www.kaggle.com/sakshigoyal7/credit-card-customers

# - Passo 1: Importar a base de dados
# - Passo 2: Visualizar e tratar essa base de dados
# - Passo 3: "Dar uma olhada" na sua base de dados
# - Passo 4: Construir uma análise para identificar o motivo de cancelamento
#   - Identificar qual o motivo ou os principais motivos dos clientes estarem cancelando o cartão de crédito

# In[4]:


import pandas as pd

tabela = pd.read_csv("/content/drive/MyDrive/Minicurso Analise de Dados/ClientesBanco.csv", encoding="latin1")
tabela = tabela.drop("CLIENTNUM", axis=1)
display(tabela)


# # Agora vamos tratar valores vazios e exibir um resumo das colunas da base de dados

# In[8]:


tabela = tabela.dropna()
display(tabela.info())

display(tabela.describe().round(1))


# # Vamos avaliar como está a divisão entre Clientes x Cancelados

# In[10]:


qtde_categoria = tabela["Categoria"].value_counts()
display(qtde_categoria)

qtde_categoria_perc = tabela["Categoria"].value_counts(normalize=True)
display(qtde_categoria_perc)


# # Temos vários formas de descobrir o motivo de cancelamento
#   - Podemos olhar a comparação entre Clientes e Cancelados em cada uma das colunas da nossa base de dados, para ver se essa informação traz algum insight novo para a gente

# In[13]:


import plotly.express as px

for coluna in tabela:
  grafico = px.histogram(tabela, x=coluna, color="Categoria")
  grafico.show()


# # Informações retiradas da análise
# 
# - Me parece que quanto mais produtos contratados um cliente tem, menor a chance dele cancelar
# - E quanto mais transações e quanto maior o valor de transação, menor a chance dele cancelar
# - Quanto maior a quantidade de contatos que a pessoa teve que fazer, maior a chance dela cancelar
