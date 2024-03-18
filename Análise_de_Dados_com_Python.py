#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# In[76]:


#2.1 importar a base de dados

import pandas as pd 

tabela = pd.read_csv('telecom_users.csv')
display(tabela)


# In[77]:


#2.2 visualizar a base de dados 

#excluir as colunas inuteis 
tabela = tabela.drop('Unnamed: 0', axis = 1)
display(tabela)


# In[78]:


#2.3 tratamento de dados(resolver os problemas)
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors = 'coerce')

tabela = tabela.dropna(how='all', axis=1)
tabela = tabela.dropna(how='any', axis=0)
print(tabela.info())


# In[79]:


#2.4 analise inicial de dados
#informações são verdadeiras ou não

print(tabela["Churn"].value_counts(normalize= True))


# In[80]:


get_ipython().system(' pip install plotly')


# In[81]:


import plotly.express as py


# In[83]:


#2.5 descobrir os motivos dos cancelamentos
#criar graficos

for  coluna in tabela.columns:
    grafico = py.histogram(tabela, x=coluna, color= 'Churn', text_auto=True )
    #exibir os graficos 
    grafico.show()


# ### Conclusões e Ações

# Escreva aqui suas conclusões:
