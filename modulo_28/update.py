import pyodbc
import pandas as pd

dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=chinook.db;")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

# Executar os comandos no banco
# Para indicar exatamente onde a atualização deve ser feita, utilizamos o e-mail como parâmetro, dado que só uma pessoa tinha esse e-mail na tabela. Poderia ser também o ID, dado que é algo único
cursor.execute('''
UPDATE customers SET Email="luisinho_camisa10@embraer.com.br" WHERE Email="luisg@embraer.com.br"
''')

# Salva a alteração
cursor.commit()

cursor.close()
conexao.close()