#!/usr/bin/env python
# coding: utf-8

# # Desafio Python e SQL
# 
# ### Create

# In[1]:


import pyodbc as pyo


# In[3]:


dados_conexao = ('Driver={SQLite3 ODBC Driver};'
                 'Sever=localhost;'
                 'Database=chinook.db')

#conectando ao banco de dados

conexao =  pyo.connect(dados_conexao)
print('conexão bem sucedida')


# In[7]:


cursor = conexao.cursor()
cursor.execute('''
INSERT INTO albums(Title; ArtistID)
VALUES 
(IGOROCK; 4)
''')

cursor.commit()




cursor.close()


# In[ ]:




