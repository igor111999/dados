#!/usr/bin/env python
# coding: utf-8

# ### Documentação Selenium:
# 
# - https://selenium-python.readthedocs.io/locating-elements.html

# In[35]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)


# In[36]:


import os

caminho = os.getcwd()
arquivo = caminho + r"\formulario.html"
navegador.get(arquivo)


# #### Botão Padrão (clicar em botão)

# In[37]:


navegador.find_element(By.XPATH, '/html/body/form/input[1]').click()
alerta = navegador.switch_to.alert
alerta.accept()


# #### Dica, esteja atento ao atributo "value" dos inputs, ele pode te ajudar
# 
# - .text
# - .get_attribute("value")
# - .is_selected

# #### Botão de Seleção estilo Checkbox (clicar no botão)

# In[38]:


# clicar no botão
navegador.find_element(By.XPATH, '/html/body/form/input[2]').click()


# In[39]:


# verificar o valor do botão
valor = navegador.find_element(By.XPATH, '/html/body/form/input[2]').is_selected()
print(valor)


# #### Botão de Seleção de Cores (enviar valor)

# In[40]:


# preencher a cor
navegador.find_element(By.XPATH, '/html/body/form/input[5]').send_keys('#2143E8')


# In[41]:


# verificar qual a cor foi selecionada
valor = navegador.find_element(By.XPATH, '/html/body/form/input[4]').get_attribute("value")
print(valor)


# #### Botão de Datas (enviar valor)

# In[42]:


# preencher o valor
navegador.find_element(By.XPATH, '/html/body/form/input[6]').send_keys('15/02/1994')


# In[43]:


# pegar o valor
valor = navegador.find_element(By.XPATH, '/html/body/form/input[6]').get_attribute("value")
print(valor)


# #### Botão de Datas com Horas (enviar valor)

# In[44]:


# preenchendo
from selenium.webdriver.common.keys import Keys

navegador.find_element(By.XPATH, '/html/body/form/input[7]').send_keys('15/02/1994', Keys.TAB, '22:00')


# In[45]:


# pegando o valor
valor = navegador.find_element(By.XPATH, '/html/body/form/input[7]').get_attribute("value")
print(valor)


# #### Botão para selecionar o arquivo (enviar valor com caminho completo)

# In[46]:


# preenchendo

caminho = os.getcwd()
arquivo = caminho + r"\formulario.html"

navegador.find_element(By.XPATH, '/html/body/form/input[8]').send_keys(arquivo)


# In[47]:


# pegar o valor
valor = navegador.find_element(By.XPATH, '/html/body/form/input[8]').get_attribute("value")
print(valor)


# #### Botão para selecionar mês e ano (enviar valor)

# In[48]:


# preenche
navegador.find_element(By.XPATH, '/html/body/form/input[9]').send_keys('janeiro', Keys.TAB, '1980')
# pegar o valor
valor = navegador.find_element(By.XPATH, '/html/body/form/input[9]').get_attribute('value')
print(valor)


# #### Campos Numéricos

# In[49]:


navegador.find_element(By.XPATH, '/html/body/form/input[10]').clear()
navegador.find_element(By.XPATH, '/html/body/form/input[10]').send_keys("123456")


# #### Campos de Senha

# In[50]:


# preencher
navegador.find_element(By.XPATH, '/html/body/form/input[11]').send_keys("123456")
# pego o valor
valor = navegador.find_element(By.XPATH, '/html/body/form/input[11]').get_attribute('value')
print(valor)


# #### RadioButtons (botões que só consegue marcar 1)

# In[51]:


navegador.find_element(By.XPATH, '/html/body/form/input[14]').click()


# In[52]:


valor = navegador.find_element(By.XPATH, '/html/body/form/input[14]').is_selected()
print(valor)


# #### Slider (enviar valor)

# In[53]:


# pegar o valor
valor = navegador.find_element(By.XPATH, '/html/body/form/input[15]').get_attribute('value')
print(valor)


# In[54]:


# preencher o valor
elemento = navegador.find_element(By.XPATH, '/html/body/form/input[15]')

elemento.clear()
for i in range(50 - 30):
    elemento.send_keys(Keys.ARROW_LEFT)


# #### Caixa de Texto

# In[55]:


# preencher
navegador.find_element(By.XPATH, '/html/body/form/input[16]').send_keys("Vasco")


# In[56]:


valor = navegador.find_element(By.XPATH, '/html/body/form/input[16]').get_attribute("value")
print(valor)


# #### Caixa de Horas

# In[57]:


navegador.find_element(By.XPATH, '/html/body/form/input[17]').send_keys('15:15')


# #### Caixa de Data Personalizada (Semanal)

# In[58]:


navegador.find_element(By.XPATH, '/html/body/form/input[18]').send_keys('17', '2005')


# #### Blocos de texto (enviar valor)

# In[59]:


navegador.find_element(By.XPATH, '//*[@id="story"]').clear()
navegador.find_element(By.XPATH, '//*[@id="story"]').send_keys("Olá", Keys.ENTER, 'Meu nome é Lira', Keys.ENTER, 'Value, Tmj')


# #### Selecionando itens de uma lista

# In[60]:


# preencher o valor
navegador.find_element(By.XPATH, '/html/body/form/select[1]').send_keys('B')


# In[61]:


# pegando o valor
valor = navegador.find_element(By.XPATH, '/html/body/form/select[1]').get_attribute('value')
print(valor)


# In[62]:


# clicando para selecionar
import time
navegador.find_element(By.XPATH, '/html/body/form/select[1]').click()
time.sleep(0.5)
navegador.find_element(By.XPATH, '/html/body/form/select[1]/option[3]').click()


# In[63]:


# com o select
# próxima aula
# https://www.selenium.dev/pt-br/documentation/webdriver/elements/select_lists/

from selenium.webdriver.support.select import Select

elemento = navegador.find_element(By.TAG_NAME, 'select')
elemento_select = Select(elemento)


# In[64]:


elemento_select.select_by_visible_text('C')


# In[65]:


# ler o item selecionado
lista_itens = elemento_select.all_selected_options
print(lista_itens)
# find_element = elemento
# find_elements = [elemento1, elemento2, elemento3]

print(lista_itens[0].get_attribute("value"))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




