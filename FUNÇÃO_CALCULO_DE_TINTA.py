#!/usr/bin/env python
# coding: utf-8

# ### Forma de pensar

# In[ ]:


# coisas simples: atravessar a rua (mostrar os diferentes níveis de abstração que dá para fazer)


# tomar café da manhã (mostrar os diferentes níveis de abstração que dá para fazer)


# Shampoo (pegar um shampoo aqui de casa e ler)


# ### Exemplo de Exercício do Curso

# #### 23. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R\\$ 80,00 ou em galões de 3,6 litros, que custam R\\$ 25,00.

# In[57]:



def valor_pintura(tamanho):
    tamanho = float(input('qual a area a ser pintada'))
    L = float(6)
    litros_g = tamanho / L
    lata = 18.0
    galão = 3.6
    qtdeL = litros_g / lata
    qtdeG = litros_g / galão
    prL = 80.0
    prG = 25.0
    rsL = prL * qtdeL
    rsG = prG * qtdeG
    print(f' a quantidade de litros gasta sera de {litros_g}, com a 1 opção gastara {qtdeL} latas, e a segunda gastara {qtdeG}')
    print('o valor gasto pela lata de tinta seria {}, ja pelo galão seria de {}'.format(rsL,rsG))
    return (litros_g, qtdeL, qtdeG)


# In[ ]:


print(valor_pintura(tamanho))


# In[8]:


def valor_pintur(tamanho):
    tamanho = float(input('qual a area a ser pintada'))
    L = float(6)
    litros_g = tamanho / L
    lata = 18.0
    galão = 3.6
    qtdeL = litros_g / lata
    qtdeG = litros_g / galão
    prL = 80.0
    prG = 25.0
    rsL = prL * qtdeL
    rsG = prG * qtdeG
    return print(f' A quantidade de litros gasta sera de {litros_g}, com a 1 opção gastara {qtdeL} latas, e a segunda gastara {qtdeG}. O valor gasto pela lata de tinta seria {rsL}, ja pelo galão seria de {rsG}')


# valor_pintura(tamanho)

# In[ ]:


valor_pintur(tamanho)


# ##### Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações.
# 
# Dica: lembre dos operadores // e % mostrados em exercícios anteriores<br>
# Dica1: numero // 10 vai te dar como resposta a parte inteira da divisão do número por 10.<br>
# Dica2: numero % 10 vai te dar o resto da divisão do número por 10.
# 
# ##### 1. Comprar apenas latas de 18 litros: (apenas latas inteiras)

# In[22]:


def valor_pintur(tamanho):
    tamanho = float(input('qual a area a ser pintada'))
    L = float(6)
    litros_g = tamanho / L
    lata = 18.0
    qtdeL = litros_g / lata
    prL = 80.0
    rsL = prL * qtdeL
    return print(f' A quantidade de litros gasta sera de {litros_g}, com a 1 opção gastara {qtdeL} latas, O valor gasto pela lata de tinta seria {rsL}')


# In[23]:


valor_pintur(tamanho)


# ##### 2. Comprar apenas galões de 3,6 litros: (apenas galoes inteiros)

# In[24]:


def valor_pintu(tamanho):
    tamanho = float(input('qual a area a ser pintada'))
    L = float(6)
    litros_g = tamanho / L
    galão = 3.6
    qtdeG = litros_g / galão
    prG = 25.0
    rsG = prG * qtdeG
    return print(' A quantidade de litros gasta sera de {:.0f}, gastara {:.0f} de galão, . O valor gasto pelo galão seria de {:.0f}'.format(litros_g, qtdeG, rsG))


# In[25]:


valor_pintu(tamanho)


# ##### 3. Misturar latas e galões, de forma que o desperdício de tinta seja menor. Sempre arredonde os valores para cima, isto é, considere latas cheias.

# O custo da lata é 80/18 = 4,44 R\\$/L
# 
# O custo do galão é 25/3,6 = 6,94 R\\$/L
# 
# A lata é mais econômica, então todas as latas inteiras que pudermos usar devemos comprar em latas. Se ficar faltando alguma coisa para completar devemos avaliar se é melhor comprar latas ou galões. Exemplo:
# 
# Se queremos comprar 90 litros. 5 latas dão exatamente 90 litros. Então devemos comprar tudo em latas.
# 
# Se queremos comprar 95 litros. 5 latas dão exatamente 90 litros. Então devemos comprar pelo menos 5 latas e avaliar o que falta, se estes últimos 5 litros valem mais apenas em latas ou galões.
# 
# Para os 5 litros faltantes precisamos de 2 galões que custam 50 reais no total. Ou de uma lata que custa 80 reais no total. Portanto, neste caso vale mais a pena usar 2 galões.
# 
# Se queremos comprar 107 litros. 5 latas dão exatamente 90 litros. Então devemos comprar pelo menos 5 latas e avaliar o que falta, se estes últimos 5 litros valem mais apenas em latas ou galões.
# 
# Para os 17 litros faltantes precisamos de 5 galões que custam 125 reais no total. Ou de uma lata que custa 80 reais no total. Portanto, neste caso vale mais a pena usar uma lata.
# 
# 3 galões custam 75 reais, 4 galões custam 100 reais. Então, se for possível completar com até 3 galões escolhe-se galões. Qualquer quantidade maior que 3 galões, usa-se latas.
# 
# Podemos ir ao exercício:

# In[54]:


#objetivo: tinta com emnor preço e desperdicio possivel
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.¶

def pintura(tamanho):
#pegar area a ser pintada    
    tamanho = float(input('qual a area a ser pintada '))
#preço do litro em cada situação
    custoLilat = 4.44 
    custoligal = 6.94 
    rlata = 80.0
    rgalão = 25.0
#rendimento da tinta em metros    
    L = float(6)
    litros_g = tamanho / L
#qtde de litros em cada item    
    lata = 18.0
    galão = 3.6
#preço a ser gasto de litro de tinta
#galão
    litros_resto = litros_g % 3.6 
    qtdeG = litros_g / galão
    preçoG = qtdeG * rgalão
#lata
    latas_resto = litros_g % 18.0 
    qtdeL = litros_g / lata
    preçoL = qtdeL * rlata
        
    
    if litros_g <= (3 * galão) : 
        if litros_resto > 0:
            qtdeGG = int(qtdeG) + 1
            prg = qtdeGG * rgalão
            print('A quantidade Galões nescessaria é de {:.0f}, o preço a ser pago devera ser {}'.format(qtdeGG, prg))
        else:
            qtdeG = litros_g / galão
            prg2 = qtdeG * rgalão
            print('A quantidade de Galões nescessaria é de {:.0f}, o preço a pagar devera ser {}'.format(qtdeG, prg2))
        
    elif litros_g > (3 * galão):
        if latas_resto > 50:
            if latas_resto < 76:
                preço_restos = 3 * rgalão
                qtdeL = int(qtdeL)
                latapr = (qtdeL * rlata)+ preço_restos
                print('O preço a ser pago deve ser {:.0f}'.format(latapr))
         25 < latas_resto <= 50 :
            preço_restos = 2 * rgalão 
            qtdeL = int(qtdeL)
            latapr = (qtdeL * rlata)+ preço_restos
            print('O preço a pagar devera ser {:.0f}'.format(latapr))
        else:
            preço_restos = 1 * rgalão
            qtdeL = int(qtdeL)
            latapr = (qtdeL * rlata) + preço_restos
            print('O preço a ser pago devera ser {:.0f}'.format(latapr))
                
    else:
        prl = qtdeL * rlata
        print('A quantidade de latas nescessaria é de {:.0f}, o preço a pagar devera ser {}'.format(qtdeL, prl))
    return tamanho


# -

# In[55]:


tamanho = float(input('qual a area a ser pintada '))
pintura(tamanho)


# In[ ]:





# In[ ]:




