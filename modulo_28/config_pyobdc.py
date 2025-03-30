import pyodbc

# Verificar quais drivers temos baixados
'''print(pyodbc.drivers())'''

# Criar e rodar apenas uma vez
# Temos que passar 2 infos na tupla: o driver; servidor (todo banco de dados fica armazenado em algum lugar, seja no próprio computador (localhost), online (driver), entre outros; e o arquivo)
dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=salarios.sqlite;")
# Caso tivesse login e senha, seriam adicionados: ;UID=Login;PWD=Senha;")

# Com os dados passados, a conexão será feita com o banco de dados (através do pyodbc) e será armazenada nesta variável 
conexao = pyodbc.connect(dados_conexao)
# O cursor é a ferramenta usada para executar os comandos SQL
cursor = conexao.cursor()

# Agora já podemos executar nossos comandos SQL. Há 2 opções:
## Apenas Executar comandos SQL que vão acontecer no banco  
## Executar o comando SQL e armazenar a consulta em uma variável no Python, como um dataframe do pandas

'''dataframe = pd.read_sql('COMANDO_SQL', conexao) -> vai executar o comando SQL, gerando uma consulta e retornando a resposta dessa consulta para o dataframe

Para pegar uma tabela inteira do nosso banco de dados, usaremos o comando SQL Select *:
"SELECT * FROM BaseDeDados.Tabela"'''

# Tudo fica armazenado em cursor
cursor.execute("SELECT * FROM Salaries")
# Para ver as informações armazenadas, faremos
valores = cursor.fetchall()

# Não podemos simplesmente printar a tabela, pois tem 148 mil linhas. Podemos pedir que sejam printados alguns, que serão apresentados em uma lista de tuplas
print(valores[:10])

# Sempre temos que fechar a conexão entre aulas, pois o banco pode intepretar como se o código estivesse sendo editado por várias fontes e dar lock (impedir edições)
cursor.close()
conexao.close()