import pandas as pd

#às vezes precisaremos mudar o encoding. Possiveis valores para testar:
#encoding='latin1', encoding='ISO-8859-1', encoding='utf-8' ou então encoding='cp1252'
vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';')

# Queremos apenas 2 colunas em cada tabela, logo, escolheremos exibir apenas essas, dado que são poucas
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

#juntando os dataframes
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')

#exibindo o dataframe final
print(vendas_df)

# 1 - Qual cliente comprou mais vezes? Uma forma de saber isso é pela contagem de vezes que o e-mail de determinado cliente aparece na tabela. Depois, deve-se fazer um gráfico:

frequencia_clientes = vendas_df["E-mail do Cliente"].value_counts()
print(frequencia_clientes)

# Assim, o gráfico vai ficar com muita info, dado que são muitos clientes, Para vermos os dados dos primeiros 5 clientes mais frequentes, devemos fazer da seguinte forma. O figsize faz com que regulemos o tamanho do gráfico, e o yticks fazem com que consigamos mudar o range das informação, com min, max e pulo

frequencia_clientes[:5].plot(figsize = (15, 5), yticks = range(0, 100, 5))

# 2 - Qual loja vendeu mais? O nome das lojas aparece por venda, então iremos agrupá-las e somar as quantidades de venda de cada uma

# Dessa forma, Nome da Loja vira como se fosse um índice ou chave de um dicionário
vendas_lojas = vendas_df.groupby("Nome da Loja").sum()

# Apenas a coluna de Quantidade de Vendas irá aparecer. Entre apenas 1 par de colchetes, fica como se fosse uma lista, sem formatação. Com 2, fica formatado
vendas_lojas = vendas_df[["Quantidade de Vendas"]]

# Para botar em ordem, ou seja, iniciar a tabela com maior número de vendas, iremos usar o .sort_values(), e indicar qual a coluna que deve ser somada. Como será ordenado de forma descrescente, botar o parâmetro ascending como falso
vendas_lojas = vendas_lojas.sort_values("Quantidade de Vendas", ascending = False)

vendas_lojas[:5].plot(figsize = (15, 5), kind = "bar")

# Pegar o maior valor e seu índice
maior_valor = vendas_df["Quantidade de Vendas"].max()
melhor_loja = vendas_df["Quantidade de Vendas"].idxmax()

print(f"A melhor loja é {melhor_loja}, com {maior_valor} vendas realizadas.")

# Qual o produto que menos vendeu?

# Ascending verdadeiro
'''vendas_lojas_2 = vendas_lojas.sort_values("Quantidade de Vendas", ascending = True)
pior_valor = vendas_df["Quantidade de Vendas"].max()
pior_loja = vendas_df["Quantidade de Vendas"].idxmax()

print(f"A pior loja é {melhor_loja}, com {maior_valor} vendas realizadas.")'''

# min() e idmin()
'''pior_valor = vendas_df["Quantidade de Vendas"].min()
pior_loja = vendas_df["Quantidade de Vendas"].idxmin()

print(f"A melhor loja é {melhor_loja}, com {maior_valor} vendas realizadas.")'''

# Pegar a loja com menor número de vendas
print(f"A loja que menos vendeu foi{vendas_lojas[-1:]}.")