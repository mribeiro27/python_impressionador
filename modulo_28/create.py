import pyodbc

dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=chinook.db;")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

# 3 aspas duplas permite que quebremos o texto
# Em parêntesis está a ordem dos valores que serao adicionados
# "Rock do Ronald McDonald" está entre aspas porque tem espaços
cursor.execute("""
INSERT INTO albums (Title, ArtistId)
VALUES ('Rock do Ronald McDonald', 4)
""")

# Commit da inserção
cursor.commit()

cursor.close()
conexao.close()