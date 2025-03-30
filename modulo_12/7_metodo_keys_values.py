vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

# Pegar apenas as chaves
chaves = vendas_tecnologia.keys()

# Pegar apenas os valores
valores = vendas_tecnologia.values()

# O dict_values e dict_keys aparece por essas listas ainda esterem vinculadas ao dicionário. No caso abaixo, iremos adicionar uma chave e um valor à lista de vendas_tecnologia
vendas_tecnologia['liraphone'] = 10

# As mudanças aparecerão quando printamos:
print(chaves)
print(valores)

# Um lado negativo dessas listas vinculadas a um dicionário é o fato de não conseguirmos usar métodos nessa lista. Para isso, iremos desvinculá-los: 
print(list(chaves))
print(list(valores))

# Oeganizar os produtos em ordem alfabética e combiná-los com a quantidade de veda destes

for chave in vendas_tecnologia:
     print('{}: {} unidades'.format(chave, vendas_tecnologia[chave]))
print('-' * 40)

#agora se quisermos organizar isso, fazemos:

lista_chaves = list(chaves)
# O método .sort() ordena as palavras
lista_chaves.sort()

# Para combiná-los com as vendas, iremos fazer um for. Esse for irá verificar as palavras da lista_chaves com as da lista vendas_tecnologia, e atribuir os valores às palavras iguais
for chave in lista_chaves:
   print('{}: {} unidades'.format(chave, vendas_tecnologia[chave]))