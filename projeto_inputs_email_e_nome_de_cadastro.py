#!/usr/bin/env python
# coding: utf-8

# # Exercícios
# 
# ## 1. Cadastro de CPF
# 
# Crie um programa para cadastro de CPF de clientes que recebe o CPF em um input box apenas com números.
# 
# Ex: 'Insira seu CPF (digite apenas números)'
# 
# Caso o usuário digite algo diferente de números ou digite menos de 11 caracteres (tamanho do CPF brasileiro), o programa deve exibir uma mensagem de "Digite seu CPF corretamente e digite apenas números"

# In[22]:


cpf = input('insira seu cpf')


if len(cpf) == 11 and cpf.isnumeric() == True:
    print(cpf)
    
else :
    print('Digite seu CPF corretamente e digite apenas números')


# In[20]:





# ## 2. Melhorando nosso Cadastro de CPF
# 
# Agora, além das validações anteriores, vamos criar um input que permita que o usuário insira pontos, traços e inclusive espaços vazios.
# 
# Nosso programa deve "tratar" o que o usuário inserir para padronizar o CPF dele em apenas números.
# 
# A verificação de tamanho do CPF com 11 caracteres continua válida, mas ela só deve ser feita depois de retirar todos os pontos, traços e espaços do CPF que o cliente inserir e, uma vez retirados pontos, traços e espaços, devem sobrar apenas números no CPF. Qualquer outro caractere deve ser considerado inválido.
# 
# No final, nosso programa deve exibir uma mensagem para o usuário, caso ele tenha inserido o CPF inválido ou então apenas deve printar o CPF correto já só com número.

# In[ ]:


pf = input('insira seu cpf')



if len(cpf) == 11 and cpf.isnumeric() == True:
    print(cpf)
    
else :
    print('Digite seu CPF corretamente e digite apenas números')


# ## 3. Cadastro de e-mails
# 
# - A Hashtag sempre se comunica com seus clientes por e-mail. Para isso, a gente tem em cada página um cadastro de nome e e-mail. Nesse cadastro, nosso sistema verifica se o e-mail que a pessoa inseriu é um e-mail válido, verificando se ele tem '@' e se depois do '@' tem algum ponto, afinal:
# 
# - liragmail.com NÃO é um e-mail válido
# - lira@gmail NÃO é um e-mail válido
# - lira@gmail.com é um e-mail válido
# 
# Crie um programa que permita o cadastro de nome e e-mail de uma pessoa (por meio de inputs) e que verifique:
# 1. Se nome e e-mail foram preenchidos, caso contrário ele deve avisar para preencher todos os dados corretamente
# 2. Se o e-mail contém '@' e se depois do '@' existe algum '.', caso contrário ele deve exibir uma mensagem de e-mail inválido
# 
# Obs: Pode te ajudar lembrar do método .find da aula de Métodos de String. Você pode testar o que ele dá como resposta caso ele não encontre um item dentro da string

# In[66]:


nome = input('insira o nome para cadastro ')
email = input('insira o email para cadastro ')

if  nome.isalpha() and '@' in email:
    print(nome, email)
    
elif '' :
    print('preencha todos os dados corretamente')
    
else:
     print('preencha todos os dados corretamente')
    
    


# In[39]:


print(email.find('@'))


# In[ ]:




