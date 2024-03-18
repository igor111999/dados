#!/usr/bin/env python
# coding: utf-8

# ### Documentação Selenium:
# 
# - https://selenium-python.readthedocs.io/locating-elements.html

# In[1]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)


# In[4]:


import os

caminho = os.getcwd()
arquivo = caminho + r"\Pagina Hashtag.html"
navegador.get(arquivo)


# #### Botão que abre outra janela

# In[5]:


navegador.find_element(By.XPATH, '/html/body/section[2]/div/div[4]/figure/a/img').click()


# In[6]:


# preenchendo o formulario

navegador.find_element(By.ID, 'fullname').send_keys("LiraLira")


# ### Outra aba

# In[7]:


aba_original = navegador.window_handles[0]
nova_aba = navegador.window_handles[1]
navegador.switch_to.window(nova_aba)
navegador.find_element(By.ID, 'fullname').send_keys("LiraNovaAba")


# In[8]:


navegador.find_element(By.ID, 'email').send_keys("lira@lira.com")


# ### Identificar qual aba é qual item da lista do window_handles

# In[ ]:


# ver os titulos de todas as abas
for aba in navegador.window_handles:
    navegador.switch_to.window(aba)
    print(navegador.title)


# ### Outra janela

# In[10]:


abas = navegador.window_handles
print(len(abas))
nova_janela = navegador.window_handles[2]
navegador.switch_to.window(nova_janela)


# In[11]:


navegador.find_element(By.ID, 'fullname').send_keys("LiraJanela")
navegador.find_element(By.ID, 'email').send_keys("janela@lira.com")


# In[ ]:


# fechar a aba atualmente selecionada
navegador.close()
# fechar todas as abas (navegador inteiro)
navegador.quit()

