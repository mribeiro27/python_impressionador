vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

# Como fazer com que as listas dos produtos mais vendidos para os menos vendidos sejam relacionadas, mostrando corretamente os valores e preços correspondentes:

# Para conectar as listas, iremos criar uma var auxiliar, que será uma tupla - ela, com o list, será uma lista. Devemos botar os números primeiro, pois o sort irá verificar as maiores vendas, como queremos, e não a letra:

lista_auxiliar = list(zip(vendas_produtos, produtos))
lista_auxiliar.sort(reverse=True)
print(lista_auxiliar)

# Agora iremos fazer o unpacking, unzipar, para assim conseguirmos separar os produtos e preços, os ordenando de forma decrescente:

# Para cada vendas e produto na lista auxiliar, imprima as produtos
produtos = [produto for vendas, produto in lista_auxiliar]
print(produtos)