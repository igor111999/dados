#!/usr/bin/env python
# coding: utf-8

# # Como descobrir o índice de um item de uma lista?
# 
# i = lista.index('item')

# Exemplo:
# 
# Digamos que você puxou do Banco de Dados da sua empresa uma lista com todos os produtos que a empresa vende e a quantidade em estoque de todos eles.

# In[30]:


produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque = [100, 150, 100, 120, 70, 180, 80]


# Nesse caso a lista é "pequena" para fins didáticos, mas essa lista poderia ter dezenas de milhares de produtos diferentes.
# 
# E agora, como eu faço para descobrir a quantidade em estoque do produto geladeira?

# In[32]:


k = produtos.index('tablet')
l = estoque[i]

print(e)


# Crie um programa para fazer uma consulta de estoque. O usuário do programa deve inserir o nome do produto e, caso ele não exista na lista, ele deve ser avisado. Caso exista, o programa deve dizer a quantidade de unidades em estoque do produto

# In[40]:


produto = input('Qual produto voce deseja: ')

i = produtos.index(produtos)
e = estoque[i]


if produto in produtos :
    print(f'Temos o produto desejado,{produto} , temos {e} unidades em estoque')
    
else:
    print('infelizmente não temos o produto desejado, informe novamente o seu desejo')


# In[ ]:




