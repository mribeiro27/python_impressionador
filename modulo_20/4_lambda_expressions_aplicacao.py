
preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}

#Fazendo por function
# Vamos usar o map para aplicar a função para cada item do dicionário. No dicionário, o item são as duas infos juntas, a chave e o valor. Para pegarmos só o valores, iremos usar o .values()

def calcular_preco(preco):
    return preco * 1.3

# O map está aplicando a função calcular_preco para todos os valores do dicionário. Com o list(), iremos transformar tudo em lista
preco_com_imposto = list(map(calcular_preco, preco_tecnologia.values()))
print(preco_com_imposto)

# Lambda Expression: a LE ficará extamente no lugar que chamamos a função

preco_com_imposto2 = list(map(lambda preco: preco * 1.3 , preco_tecnologia.values()))
print(preco_com_imposto2)

#fazendo por function
# A função recebe a tupla como parâmetro, que será uma tupla de itens de um dicionário, com chave e valor. Logo, não é somente o valor

def acima_2000(item):
    return item[1] > 2000

produtos_acima_2000 = dict(list(filter(acima_2000, preco_tecnologia.items())))
print(produtos_acima_2000)

#fazendo por lambda

produtos_acima_2000_2 = dict(list(filter(lambda item: item[1] > 2000, preco_tecnologia.items())))
print(produtos_acima_2000_2)