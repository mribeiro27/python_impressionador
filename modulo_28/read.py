import pyodbc
import pandas as pd

dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=chinook.db;")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

# 3 aspas duplas permite que quebremos o texto
cursor.execute("""
SELECT * FROM customers
""")

# Para ver as informações armazenadas no cursor, faremos
valores = cursor.fetchall()
# Gera uma tupla de tuplas, com os nomes das colunas e outras informações
descricao = cursor.description
# Para pegarmos os nomes das colunas, que são os primeiros itens das tuplas, faremos: salvar, em um variável, o primeiro item de cada tupla da variável "descricao" - para cada tupla na tupla, pegaremos o primeiro item
colunas = [tupla[0] for tupla in descricao]

# Como a tabela é pequena, podemos printar normalmente. Se fosse grande, poderíamos visualizar a tabela de pouco em pouco, por exemplo: print(valores[:10])
# As informações são printadas como uma lista de tuplas. Se quiséssemos ver os dados do primeiro cliente, faríamos: print(valores[:10])
print(valores)

tabela_clientes = pd.DataFrame.from_records(valores)

# Como as colunas vêm enumeradas, podemos nomeá-las de acordo com a tabela. Essa forma abaixo é a manual
# tabela_clientes = pd.DataFrame.from_records(valores, columns='ID, Nome, Sobrenome, Empresa, Endereço...')

# Mas também tem uma forma de fazer pegando diretamente da tabela, através da variável "descricao" e "colunas"
tabela_clientes = pd.DataFrame.from_records(valores, columns=colunas)
# Era pra ser "display", mas não funcionou
print(tabela_clientes)

cursor.close()
conexao.close()