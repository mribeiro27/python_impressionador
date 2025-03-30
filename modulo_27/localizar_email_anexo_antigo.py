# O imap_tools é uma forma de protocolo que os e-mails utilizam
# A integração é útil, pois é possível identificar e-mails e anexos automaticamente, sendo possível até mesmo extrair e baixar anexos
# O MailBox entra no nosso e-mail, logo, precisa de login e senha, e o acesso deve ser permitido (Gerenciar sua conta Google -> Segurança -> Ativar o "Acesso a app menos seguro")
from imap_tools import MailBox, AND, OR, NOT

usuario = 'marinoremini@gmail.com'
senha = '123'

# No método MailBox, iremos botar o servidor iMAP do e-mail, que pode ser achado em systoolsgroup.com/imap/
# O exemplo é no gmail, então será usado o IMAP deste
# A variável meu_email irá funcionar como a caixa de entrada
meu_email = MailBox('imap.gmail.com').login(usuario, senha)

# Filtrar e-mails que foram enviados por e para mim, através do método fetch()
# O operador AND irá ser responsável por selecionar os e-mails enviados pelo remetente escolhido
lista_emails_meus = meu_email.fetch(AND(from_='marinoremini@gmail.com'))

# Filtar os e-mails que eu mandei para uma pessoa
lista_emails_enviados_allan = meu_email.fetch(AND(from_='marinoremini@gmail.com', to='allanfmachado@gmail.com'))

# Com o for, é possível printar os assuntos e corpos de texto enviados
for email in lista_emails_enviados_allan:
    print(email.subject)
    print(email.text)

# O print retorna um objeto, logo, iremos transformar o resultado em uma lista e verificar a quantidade
print(len(list(lista_emails_meus)))
print(len(list(lista_emails_enviados_allan)))

# Como pegar anexo de e-mails
lista_emails_anexo = meu_email.fetch(AND(from_='allanfmachado@gmail.com'))

for email in lista_emails_anexo:
    # Verificar se há anexo
    if len(email.attachments) > 0:
        # Se houver anexo, procurar o nome do anexo, sem extensão, e pegar as informações deste
        for anexo in email.attachments:
            if 'RelatorioExcel' in anexo.filename:
                # .payload transforma o anexo em bytes, e através do payload, o Python consegue armazenar o arquivo inteiro no computador e reescrevê-lo em bytes (wb) - o arquivo volta ao normal
                informacoes_anexo = anexo.payload
                # Agora, quando formos mencionar o arquivo RelatorioExcel.xlsx, ele será chamado de "arquivo_excel"
                with open('RelatorioExcel.xlsx', 'wb') as arquivo_excel:
                    # Escrever as informações do anexo dentro de "arquivo_excel", que será salvo no Desktop
                    arquivo_excel.write(informacoes_anexo)