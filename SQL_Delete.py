#!/usr/bin/env python
# coding: utf-8

# # Desafio Python e SQL
# 
# ### Delete

# In[1]:


import pyodbc

dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=chinook.db")

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()


# In[2]:


cursor.execute('''
DELETE FROM albums WHERE AlbumId=2
''')

cursor.commit()

cursor.close()
conexao.close()


# In[ ]:




