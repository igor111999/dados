#!/usr/bin/env python
# coding: utf-8

# In[4]:


from imap_tools import MailBox, AND
#from senha_email import minha_senha

usuario = "igoropeixinho@gmail.com"
senha = '88392513@Gh'

meu_email = MailBox("imap.gmail.com").login(usuario, senha)


# In[10]:


# pegar email que foram enviados por um remetente específico

lista_emails = meu_email.fetch(AND(from_="pythonimpressionador@gmail.com", to="pythonimpressionador+diretoria@gmail.com"))
for email in lista_emails:
    print(email.subject)
    print(email.text)


# In[1]:


# pegar anexo de um email
lista_emails = meu_email.fetch(AND(from_="pythonimpressionador@gmail.com"))
for email in lista_emails:
    if len(email.attachments) > 0:
        for anexo in email.attachments:
            if "RelatorioExcel" in anexo.filename:
                informacoes_anexo = anexo.payload
                with open("RelatorioExcel.xlsx", "wb") as arquivo_excel:
                    arquivo_excel.write(informacoes_anexo)


# In[ ]:




