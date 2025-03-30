# Pega pegar o top 3 produtos de um dicionário, usaremos o módulo collections.Counter

from collections import Counter

vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

# Iremos usar uma variável auxiliar, passar o counter e o dicionário
aux = Counter(vendas_tecnologia)

# O método .most_common faz com que seja impressa uma lista de tuplas em ordem decrescente
print(aux.most_common(3))
