import pandas as pd

vendas_df = pd.read_csv("Contoso - Vendas - 2017.csv", sep=";")

# Pega a coluna
# print(vendas_df["ID Cliente"])

# Pega até a linha de índice 3 do dataframe
# print(vendas_df[:3])

# Cria um dataframe com as colunas citadas
# print(vendas_df[["Numero da Venda", "Data da Venda", "ID Produto"]])

# Pega o item do 1º índice da coluna
# print(vendas_df["ID Produto"][0])

# Resumo de uma tabela, usado em casos de tabelas muito grandes
print(vendas_df.info())

# Criar uma lista de clientes
lista_clientes = vendas_df["ID Cliente"]
print(lista_clientes)

lista_colunas = ["ID Produto", "Quantidade Vendida", "Quantidade Devolvida"]
produto_qtde = vendas_df[lista_colunas]
print(produto_qtde)