# Importando o pandas para conseguir ler o arquivo excel
import pandas as pd
import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
df_gerentes_area = pd.read_excel('Enviar E-mails.xlsx')
# print(df_gerentes_area)

# Como a leitura dos nomes dos gerentes e da área do relatório será feita pelas linhas, que funcionarão como índices: usar o enumerate
# Como é a coluna 'E-mail' que será manipulada, ela ficará dentro de colchetes
# Logo, para cada e-mail,o que está dentro do for será feito
for i, email in enumerate(df_gerentes_area['E-mail']):
    # O loc funciona da seguinte forma: dataframe.loc[linha(i), coluna]
    gerente = df_gerentes_area.loc[i, 'Gerente']
    area = df_gerentes_area.loc[i, 'Relatório']

    mail = outlook.CreateItem(0)
    mail.To = 'email'
    mail.Subject = 'Relatório de {}'.format(area)
    # Com 3 aspas simples podemos escrever textos pulando linha
    corpo_email = '''
    Prezado {},
    Segue anexo o relatório de {}, conforme solicitação.
    Atenciosamente,
    Funcionário
    '''.format(gerente, area)
    mail.Body = corpo_email

    # Como o nome dos arquivos condizem com os da área, podemos usar o format
    attatchment = r'C:\Users\322070\OneDrive - OPEN LABS S.A\Área de Trabalho\python_impressionador\modulo_27\Integrando Python com Outlook\{}.xslx'.format(area)
    mail.Attatchments.Add(attatchment)

    mail.Send()