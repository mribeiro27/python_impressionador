import pandas as pd

# O separador está como se fosse o ponto e vírgula, então temos que declarar o parâmetro sep aqui, para que consigamos ver o arquivo normalmente
# Também é possível passar o caminho da pasta, caso o .py não esteja na mesma pasta do .csv, em string. E, antes dessa string, botar r, como no exemplo: r'C:\Users\...\exemplo.csv'

vendas_df = pd.read_csv("Contoso - Cadastro Produtos.csv", sep=";")

# Se escrevessemos somente o nome da variável, no notebook, apareceria a tabela
print(vendas_df)

