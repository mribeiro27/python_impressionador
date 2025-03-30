# Importar a biblioteca win32, que nos permite acessar programas da Microsoft
import win32com.client as win32

# Criar uma instância do outlook que nos permite criar e-mails e enviar
outlook = win32.Dispatch('outlook.application')

# Criando o e-mail
mail = outlook.CreateItem(0)

# Destinatário
mail.To = 'mariana-r-gomes@openlabs.com.br'

# Botar em cópia
mail.CC = 'juliana-a-cardoso@openlabs.com.br'

# Botar em cópia oculta
mail.BCC = 'email@gmail.com'

# Assunto
mail.Subject = 'Teste'

# Corpo do e-mail: uma dica é usar o /m para pular linhas
# mail.Body = 'Teste'

# Podemos criar uma variável com o texto do e-mail, onde podemos manipulá-lo melhor
corpo_email = 'Teste'
mail.Body = corpo_email

# Anexos (quantos necessários)
# Se estivessemos usando o pathlib, para simplificar, o caminho teria que ser com barra, e não contrabarra
# attatchment = r'C:\Users\322070\OneDrive - OPEN LABS S.A\Área de Trabalho\python_impressionador\modulo_27\Integrando Python com Outlook\Financeiro.xslx'
# mail.Attatchments.Add(attatchment)

# Enviar
mail.Send()