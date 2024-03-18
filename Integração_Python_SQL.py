#!/usr/bin/env python
# coding: utf-8

# # Integração Python e SQL
# 
# ### Objetivo
# 
# A integração do Python com o SQL permite que execute comandos SQL diretamente pelo Python no seu banco de dados. Isso vai permitir a gente pegar consultas e já importar elas para dentro de uma análise no Python automaticamente.
# 
# ### O que vamos precisar
# 
# - Para aprender, vamos usar o SQLite, o objetivo é simplificar a instalação do SQL para que qualquer um consiga acompanhar.
# - Para isso, vamos precisar apenas de um driver, que vamos instalar aqui: http://www.ch-werner.de/sqliteodbc/
# - Um banco de dados para testar -> disponível para Download
# 
# ### No Python, o que vamos usar
# 
# - Biblioteca pyodbc -> pode ser usada com a mesma estrutura para diversos bancos de dados, como SQL Server, MySQL, Oracle, Access, IBM, etc.
# 
# ### Obs Importante
# 
# - Isso não vai ser um curso completo de SQL, portanto não vamos trabalhar extensivamente todos os comandos SQL, apesar de fazermos todo o CRUD dentro desse módulo.
# 
# ### Quando faz sentido usar Python e SQL? Quando usar só SQL?
# 
# - Criação do Banco de Dados
# - Interagir com um sistema

# In[2]:


import pyodbc as pyo


# In[3]:


print(pyo.drivers())


# In[4]:


import pyodbc as pyo
#criando a conexão , criando para o python o banco de dados
dados_conexao = ('Driver={SQLite3 ODBC Driver};'
                 'Sever=localhost;'
                 'Database=salarios.sqlite')

#conectando ao banco de dados

conexao =  pyodbc.connect(dados_conexao)
print('conexão bem sucedida')


# In[5]:


cursor = conexao.cursor()


# In[6]:


cursor.execute('SELECT * FROM Salaries')


# In[7]:


informações = cursor.fetchall()


# In[21]:


print(informações[:10000])


# In[25]:


print(informações[10000:15000])


# In[1]:


cursor.close()


# In[ ]:




