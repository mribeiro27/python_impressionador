import pyodbc

dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=chinook.db;")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute("""
DELETE FROM albums WHERE Title="Rock do Ronald McDonald"
""")

# Commit da inserção
cursor.commit()

cursor.close()
conexao.close()