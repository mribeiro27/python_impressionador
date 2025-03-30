produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']
vendas = [15000, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450]

# A lista produtos irá virar agora um dicionário, com os itens se transformando em chaves e com o valor padrão de 0
# dicionario = dict.fromkeys("produtos", 0)

# O zip os une e transforma em um objeto, onde conseguimos vê-los como tuplas através do for
'''lista_tuplas = zip(produtos, vendas)
print(lista_tuplas)

for item in lista_tuplas:
    print(item)'''

# Para tranformar as tuplas em um dicionário, usaremos o dict()
lista_tuplas = zip(produtos, vendas)
dicionario_vendas = dict(lista_tuplas)
print(dicionario_vendas)

# Para sabermos, na lista, a quantidade de venda de iPad:

# Descobrir o índice do iPad na lista de produtos
'''i = produtos.index("ipad")
print("A quantidade de iPads vendidos foi de: {} unidades.".format(vendas[i]))'''

# Quantidade de iPads no dicionário:
print("A quantidade de iPads vendidos foi de: {} unidades.".format(dicionario_vendas['ipad']))