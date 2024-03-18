#!/usr/bin/env python
# coding: utf-8

# # Exercícios
# 
# ### Antes de irmos para o desafio que apresentamos na última aula (que é bem mais complexo do que um exemplo simples) vamos resolver um exercício um pouco mais simples para treinar
# 
# ## 1. Cálculo do Percentual e da Lista de Vendedores
# 
# - Queremos criar uma function que consiga identificar os vendedores que bateram uma meta, mas além disso, consigo já me dar como resposta o cálculo do % da lista de vendedores que bateu a meta (para eu não precisar calcular manualmente depois)
# - Essa function deve receber 2 informações como parâmetro: a meta e um dicionário com os vendedores e suas vendas. E me dar 2 respostas: uma lista com o nome dos vendedores que bateram a meta e o % de vendedores que bateu a meta.

# In[2]:


meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}


# In[46]:


#1 com print
#crie sua function aqui
def vendendores_meta(valor_M, d_vendas):
    valor_M = 10000
    lista_m = []
    for venda in d_vendas:
        valor = d_vendas[venda]
        if valor > valor_M:
            lista_m.append(valor)
        percentual = len(lista_m) / len(d_vendas)
    return (valor_M, lista_m, percentual)       
    
    


# In[ ]:


#2 sem o print
def vendendores_meta(valor_M, d_vendas):
    valor_M = 10000
    lista_m = []
    for venda in d_vendas:
        valor = d_vendas[venda]
        if valor > valor_M:
            lista_m.append(valor)
        percentual = len(lista_m) / len(d_vendas)
    print('os valores que utrapassaram a meta fora {} e o percentual que bateram a meta foi de {:.1%}'.format(lista_m, percentual))
    return (valor_M, lista_m, percentual)       
    
    


# In[50]:


def calculo_meta(meta, vendas):
    bateram_meta = []
    for vendedor in vendas:
        if vendas[vendedor] >= meta:
            bateram_meta.append(vendedor)
    perc_baterammeta = len(bateram_meta) / len(vendas)
    return perc_baterammeta, bateram_meta


# In[51]:


#aplique sua function nas informações para ver se está funcionando
print(calculo_meta(meta, vendas))


# In[ ]:




