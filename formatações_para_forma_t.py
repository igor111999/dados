#!/usr/bin/env python
# coding: utf-8

# # Format - Aula de Consulta
# 
# ### Como usar o format para criar formatações personalizadas em prints e textos.
:<		Alinha o texto à esquerda (se tiver espaço na tela para isso)
:>		Alinha o texto à direita (se tiver espaço na tela para isso)
:^		Alinha o texto ao centro (se tiver espaço na tela para isso)
:+		Coloca o sinal sempre na frente do número (independente se é positivo ou negativo)
:,		Coloca a vírgula como separador de milhar
:_		Coloca o _ como separador de milhar
:e		Formato Científico
:f		Número com quantidade fixa de casas decimais
:x		Formato HEX minúscula (para cores)
:X		Formato HEX maiúscula (para cores)
:%		Formato Percentual
# - Exemplo de Alinhamento

# In[18]:


email = 'lira@gmail.com'
print('Meu e-mail não é {:<30}, show?'.format(email))


# - Exemplo de Edição de Sinal

# In[37]:


custo = 500
faturamento = 270
lucro = faturamento - custo
print('Faturamento foi {:+} e lucro foi {:+}'.format(faturamento, lucro))


# - Exemplo de Separador de Milhar

# In[38]:


custo = 500
faturamento = 270
lucro = faturamento - custo
print('Faturamento foi {:+} e lucro foi {:+}'.format(faturamento, lucro))


# - Formato com casas Decimais fixas

# In[47]:


custo = 500
faturamento = 270
lucro = faturamento - custo
print('Faturamento foi {:.2f} e lucro foi {:2f}'.format(faturamento, lucro))


# - Formato Percentual

# In[53]:


custo = 500
faturamento = 1300
lucro = faturamento - custo
margem = lucro / faturamento
print('Margem de lucro foi de {:.2%}'.format(margem))


# - Formato Moeda -> Combinação de Formatos
# 
# Existem módulos/bibliotecas que vão facilitar isso, caso a gente queira, mas vamos ver como usar módulos mais a frente do curso. Por enquanto, se você precisar, pode fazer substituições em string

# In[72]:


custo = 5000
faturamento = 27000
lucro = faturamento - custo
print('Faturamento foi R${:,.2f} e lucro foi R${:,.2f}'.format(faturamento, lucro))

#transformando no formato brasileiro
lucro_texto = 'R${:_.2f}'.format(lucro)
print(lucro_texto.replace('.', ',').replace('_', '.'))


# - Função round() para arredondar números, caso seja necessário

# In[66]:


imposto = 0.15758
preco = 100
valor_imposto = round(preco * imposto, 1)
print('Imposto sobre o preço é de {}'.format(valor_imposto))

