import sqlite3
import pandas as pd

# Aconexão será criada com o sqlite3, logo, o banco precisa ter uma conexão sqlite3
# Para verificar como seria em outras, basta pesquisar "pd.read_sql", que as documentações aparecerão
conexao = sqlite3.connect("chinook.db")

# tabela_clientes = pd.read_sql.("COMANDO SQL", conexao)
tabela_clientes = pd.read_sql("SELECT * from customers", conexao)

# Era pra ser display, mas não está funcionando
# Agora os títulos das tabelas aparecem automaticamente como o da tabela no SQL
print(tabela_clientes)

conexao.close()