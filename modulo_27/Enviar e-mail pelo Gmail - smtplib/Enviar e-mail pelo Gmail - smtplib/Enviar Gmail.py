#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Olá, <b>empresa!</b></p>
    <p>Segue meu e-mail automático</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "E-mail automático"
    msg['From'] = 'marinoremini@gmail.com'
    msg['To'] = 'marinoremini@gmail.com'
    # Depois da mudança do Google, iremos usar uma senha específica no Python, que será gerada pelo próprio: Gerenciar sua conta Google -> Segurança -> Como fazer login no Google (ter a dupla autenticação ativada) -> Senhas de App -> Fazer login novamente -> Selecionar App (E-mail) -> Dispositivo (dar um nome para dispositivo - geralmente o notebook)
    # Uma senha será gerada e deve ser colada aqui. Ela é de uso único, e pode ser apagada em qualquer momento
    password = 'senha' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# In[ ]:

enviar_email()