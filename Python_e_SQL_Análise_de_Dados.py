#!/usr/bin/env python
# coding: utf-8

# ## Exercício Desafio
# 
# - Digamos que seu chefe pediu para você um relatório da análise dos salários da unidade de San Francisco da empresa. O objetivo dele é entender:
# 
# 1. Qual foi a evolução do salário médio ao longo dos anos (TotalPay e TotalPayBenefits)
# 2. Quantos funcionários tivemos ao longo dos anos
# 3. Qual foi a evolução do total gasto com salário ao longo dos anos (TotalPayBenefits)
# 
# - Base de Dados a ser usada: salarios.sqlite

# ### Importação da Base de Dados

# In[22]:


import pandas as pd
import sqlite3

conexao = sqlite3.connect('salarios.sqlite')
tabela_salarios = pd.read_sql('SELECT * FROM Salaries', conexao)
conexao.close()

display(tabela_salarios)


# In[26]:


import pyodbc

dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=salarios.sqlite")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute('SELECT * FROM Salaries')
valores = cursor.fetchall()
descricao = cursor.description

# print(valores[:10])
# print(descricao)

cursor.close()
conexao.close()


# In[30]:


colunas = [tupla[0] for tupla in descricao]
tabela_salarios2 = pd.DataFrame.from_records(valores, columns=colunas)
display(tabela_salarios2)


# ### Análise de Dados

# In[34]:


# garantindo que estamos só com San Francisco
tabela_salarios = tabela_salarios.loc[tabela_salarios["Agency"]=="San Francisco", :]
display(tabela_salarios)

print(tabela_salarios.info())


# ##### 1. Qual foi a evolução do salário médio ao longo dos anos

# In[35]:


tabela_sm = tabela_salarios.groupby("Year").mean()
display(tabela_sm[["TotalPay", "TotalPayBenefits"]])


# ##### 2. Quantos funcionários tivemos ao longo dos anos

# In[39]:


tabela_qtde = tabela_salarios.groupby("Year").count()
tabela_qtde = tabela_qtde[["Id"]]
tabela_qtde = tabela_qtde.rename(columns={"Id": "Qtde"})
display(tabela_qtde)


# ##### 3. Qual foi a evolução do total gasto com salário ao longo dos anos

# In[42]:


def formatar(valor):
    return 'R${:,.2f}'.format(valor)

tabela_total = tabela_salarios.groupby("Year").sum()
tabela_total = tabela_total[["TotalPay", "TotalPayBenefits"]]
tabela_total["TotalPay"] = tabela_total["TotalPay"].apply(formatar)
tabela_total["TotalPayBenefits"] = tabela_total["TotalPayBenefits"].apply(formatar)
display(tabela_total)


# In[ ]:




