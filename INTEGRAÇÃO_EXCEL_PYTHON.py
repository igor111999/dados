#!/usr/bin/env python
# coding: utf-8

# # Integração Python + Excel
# 
# ### 2 formas:
# 
# 1. Pandas
#     - Mais usada no geral
#     - Trata o Excel como uma base de dados
#     - Faz o que quiser com o arquivo
#     - Pode desfazer a estrutura original do arquivo, caso queira editar
#     
# 2. Openpyxl
#     - Trata o Excel como uma planilha mesmo que pode ter várias coisas
#     - Edita "como se fosse um VBA"
#     - Menos eficiente
#     - Mantém mais a estrutura original do arquivo, mas cuidado porque não necessariamente tudo, então tem que testar

# ### Desafio
# 
# - Temos uma planilha de produtos e serviços. Com o aumento de imposto sobre os serviços, temos que atualizar o preço dos produtos impactados pela mudança.
# 
# Novo Multiplicador Imposto: 1.5

# In[1]:


# pandas
import pandas as pd

tabela = pd.read_excel("Produtos.xlsx")
display(tabela)


# In[3]:


# atualizar o multiplicador
tabela.loc[tabela["Tipo"]=="Serviço", "Multiplicador Imposto"] = 1.5

# fazer a conta do Preço Base Reais
tabela["Preço Base Reais"] = tabela["Multiplicador Imposto"] * tabela["Preço Base Original"]

tabela.to_excel("ProdutosPandas.xlsx", index=False)


# In[5]:


# openpyxl
from openpyxl import Workbook, load_workbook

planilha = load_workbook("Produtos.xlsx")

aba_ativa = planilha.active

for celula in aba_ativa["C"]:
    if celula.value == "Serviço":
        linha = celula.row
        aba_ativa[f"D{linha}"] = 1.5
        
planilha.save("ProdutosOpenPy.xlsx")


# In[ ]:




