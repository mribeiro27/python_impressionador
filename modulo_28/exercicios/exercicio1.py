# Uma tabela é uma lista de tuplas. Cada linha é uma tupla
import pyodbc
import pandas as pd

dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=salarios.sqlite;")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute("""
SELECT * FROM Salaries
""")

valores = cursor.fetchall()
descricao = cursor.description
colunas = [tupla[0] for tupla in descricao]

tabela_salarios = pd.DataFrame.from_records(valores, columns=colunas)

print(tabela_salarios)

cursor.close()
conexao.close()

## Análise de dados, filtrando apenas a unidade de São Francisco

# Se a tabela fosse maior, com milhões de linhas, as vezes é melhor filtrar a base de dados direto, assim não trava o computador
# Uma boa prática é fazer uma cópia da tabela (criar uma variável com a tabela como valor), para fazer as alterações sem medo de fazer umaalteração de alto risco na original

# O .loc faz um filtro pelas linhas e colunas. ":" faz com que todas as colunas sejam selecionadas. As linhas da coluna Agency devem conter "San Francisco", é uma condição que deve ser verdadeira para ser filtrada
tabela_salarios_sf = tabela_salarios.loc[tabela_salarios["Agency"]=="San Francisco", :]
print(tabela_salarios_sf)

## Média do salário pelos anos: devemos agrupar os anos para fazer a soma. A coluna de ID também será afetada na média, por ter um Dtype numérico

tabela_salarios_medios = tabela_salarios.groupby("Year").mean()

# Selecionar apenas as colunas desejadas, em forma de lista de colunas. O primeiro colchete é para dizer que estamos selecionando uma coluna, e o segundo, é para passarmos uma lista de colunas
print(tabela_salarios_medios[["TotalPay", "TotalPayBenefits"]])

## Quantidade de funcionários ao longo dos anos

tabela_qtde_func = tabela_salarios.groupby("Year").count()

# Quando passamos apenas uma tabela, não se torna um dateframe direto, apenas uma série de informações. Para que se torne um df, devemos passar a coluna entre dois colchetes
tabela_qtde_func = tabela_qtde_func[["Id"]]

# Renomear a "tabela" Id para "Qtde Funcionarios"
tabela_qtde_func = tabela_qtde_func.rename(columns={"Id": "Qtde Funcinarios"})

## Evolução dos salários ao longo dos anos

# Função que recebe o valor e o formata
def formatar(valor):
    return "R${:,2f}".format(valor)

tabela_salarios_somados = tabela_salarios.groupby("Year").sum()
# print(tabela_salarios_somados[["TotalPay", "TotalPayBenefits"]])

# Como o número é muito grande, e não aparece completo na tabela, iremos aplicar a função para tratar a soma nas tabelas
tabela_salarios_somados["TotalPay"] = tabela_salarios_somados["TotalPay"].apply(formatar)
tabela_salarios_somados["TotalPayBenefits"] = tabela_salarios_somados["TotalPayBenefits"].apply(formatar)

print(tabela_salarios_somados)