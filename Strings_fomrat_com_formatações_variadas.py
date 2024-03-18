#!/usr/bin/env python
# coding: utf-8

# # Strings
# 
# <span style="color: red;"><b>Todos os exercícios são feitos partindo-se do pressuposto de que todas as entradas são dadas de forma correta. Casos limite não mencionados no enunciado não são abordados porque não fazem parte do exercício.</b></span>

# #### 1. Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
# <pre>
# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.
# </pre>

# In[57]:


string1 = 'Brasil Hexa 2006'
string2 = 'Brasil! Hexa 2006!'

string3 = string1.replace(' ' , 'z')
string4 = string2.replace(' ' , 'z')

s1 = len(string1)
s2 = len(string2)
s3 = string2[-1]


print(string3.isalnum())
print(string4.isalnum())

print('string1: ', string1 , 'string2: ', string2)


print(f'As duas strings não possuem o mesmo tamanho, a  String1 tem {s1}  caracteres e a string2 tem {s2} caracteres, e elas possuem caracteres diferentes, a string1 é compostas apenas por palavras e numeros e a string2 tem a presença de duas +  {s3}  ') 


# In[58]:


print('Compara duas strings')

s1 = input('String 1: ')
s2 = input('String 2: ')
print(f'Tamanho de "{s1}": {len(s1)} caracteres')
print(f'Tamanho de "{s2}": {len(s2)} caracteres')

if len(s1) == len(s2):
    print('As strings são de tamanhos iguais.')
else:
    print('As duas strings são de tamanhos diferentes.')
    
if s1 == s2:
    print('As strings possuem conteúdos iguais.')
else:
    print('As duas strings possuem conteúdo diferente.')


# #### 2. Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.
# <pre>
# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133
# </pre>

# In[ ]:




telefone = input('qual o seu telefone')
telefone = telefone.replace(' ' , '3')

if len(telefone) == 8 :
    print('seu numero foi validado, segue o numero informado {}'.format(telefone))
    print(f'seu numero foi validado, segue o numero informado {telefone[:4]}-{telefone[4:]}.')
     
    
else :
    print('corrija o numero inserido ')


# In[ ]:




