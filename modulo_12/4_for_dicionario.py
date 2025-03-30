vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

#demonstrando o for

# Não é bom botar a variável do for como item, pois um item no dicionário é o conjunto chave:valor. É melhor chamar a variável de "chave"

for chave in vendas_tecnologia:
    # Para conseguirmos saber o valor de uma chave, devemos digitar dicionario[chave]
    print("{}: {} unidades".format(chave, vendas_tecnologia[chave]))

# Descobrir o total de notebooks vendidos

# Variável auxiliar, pois as unidades serão somadas com as anteriores
total_notebooks = 0

for chave in vendas_tecnologia:
    if "notebook" in chave:
        # Na variável serão somados o valor da própria variável (que serão os outros valores já somados) com o valor da chave
        # total_notebooks = total_notebooks + vendas_tecnologia[chave]
        total_notebooks += vendas_tecnologia[chave]

print(f"O total de notebooks vendidos foi de {total_notebooks} unidades.")
