#!/usr/bin/env python
# coding: utf-8

# # sort (ou sorted) com function
# 
# ### Descrição:
# 
# Até agora no programa, usamos várias vezes o .sort() para ordenar listas
# 
# Mas o método sort tem um parâmetro que nunca usamos e que agora sabemos usar.

# In[ ]:


produtos = ['apple tv', 'mac', 'IPhone x', 'IPhone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
produtos.sort()
print(produtos)


# - Como faríamos para ordenar corretamente?

# In[ ]:


produtos.sort(key=str.casefold)
print(produtos)


# ### Outro exemplo: como ordenar um dicionário de acordo com o valor

# In[ ]:


vendas_produtos = {'vinho': 100, 'cafeiteira': 150, 'microondas': 300, 'iphone': 5500}


# - Queremos listar da maior quantidade de vendas para a menor, para enviar como report para o diretor, por exemplo

# In[11]:


def segundo_item(tupla):
    return tupla[1]
lista_vendas = list(vendas_produtos.items())
lista_vendas.sort(key=segundo_item, reverse=True)
print(dict(lista_vendas))

