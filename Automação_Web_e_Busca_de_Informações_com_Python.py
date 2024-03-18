#!/usr/bin/env python
# coding: utf-8

# # Automação Web e Busca de Informações com Python
# 
# #### Desafio: 
# 
# Trabalhamos em uma importadora e o preço dos nossos produtos é vinculado a cotação de:
# - Dólar
# - Euro
# - Ouro
# 
# Precisamos pegar na internet, de forma automática, a cotação desses 3 itens e saber quanto devemos cobrar pelos nossos produtos, considerando uma margem de contribuição que temos na nossa base de dados.
# 
# Base de Dados: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=sharing
# 
# Para isso, vamos criar uma automação web:
# 
# - Usaremos o selenium
# - Importante: baixar o webdriver

# In[69]:


get_ipython().system(' Pip install Selenium')


# In[70]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#padrão uso do selenium


# Passo a passo
# 3.1 Pegar a cotação do Dollar

#entrar no navegador
navegador = webdriver.Chrome()

#entrar nos site desejado
navegador.get("https://www.google.com/")

#digitar no campo de busca
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotacao dolar')


navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')


print(cotacao_dolar)

navegador.quit()



# 3.2 Pegar a cotação do Euro

navegador = webdriver.Chrome()

#entrar nos site desejado
navegador.get("https://www.google.com/")

#digitar no campo de busca
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotacao euro')


navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')


print(cotacao_euro)

navegador.quit()

 
# 3.3 Pegar a cotação do Ouro
#cotação ouro nao esta no mesmo lugar dos outros

navegador = webdriver.Chrome()
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",",".")
print(cotacao_ouro)
navegador.quit()


# ### Agora vamos atualiza a nossa base de preços com as novas cotações

# - Importando a base de dados

# In[71]:


import pandas as pd 

tabela = pd.read_excel('Produtos.xlsx')
display(tabela)


# - Atualizando os preços e o cálculo do Preço Final

# In[72]:


#3.5 recalcular os preços
# atualizar as colunas de cotações
tabela.loc[tabela['Moeda']== 'Dólar','Cotação'] = float(cotacao_dolar)
tabela.loc[tabela['Moeda']== 'Euro','Cotação'] = float(cotacao_euro)
tabela.loc[tabela['Moeda']== 'Ouro','Cotação'] = float(cotacao_ouro)


#preço de compra= preço original * cotação
tabela['Preço de Compra']= tabela['Preço Original'] * tabela['Cotação']

#preço de venda= preço de compra * Margens
tabela['Preço de Venda']= tabela['Preço de Compra'] * tabela['Margem']

display(tabela)


# ### Agora vamos exportar a nova base de preços atualizada

# In[73]:


tabela.to_excel('produto novoss.xlsx', index=False)


# In[ ]:




