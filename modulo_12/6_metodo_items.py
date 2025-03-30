vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

# Transforma o dicionário em uma lista de tuplas
itens_dicionario = vendas_tecnologia.items()
print(itens_dicionario)

# São impresssas diversas tuplas, uma com cada item
for item in vendas_tecnologia.items():
    print(item)

# Unpacking de tuplas:
for produto, qtde in vendas_tecnologia.items():
    print("{}: {} unidades".format(produto, qtde))

# Verificar quais produtos venderam mais de 5000 unidades

#forma 1 -> usando apenas o dicionario e as chaves

for chave in vendas_tecnologia:
    if vendas_tecnologia[chave] > 5000:
        print("Foram vendidas mais de 5000 unidades do produto {}: {}".format(chave, vendas_tecnologia[chave]))

#forma 2 -> usando o dicionario.items()

# Como foi feito o unpacking da tupla, os valores se tornam individuais, então podemos chamar os valores pelos nomes dados no for
for produto, qtde in vendas_tecnologia.items():
    if qtde > 5000:
        print("Foram vendidas mais de 5000 unidades do produto {}: {}".format(produto, qtde))