vendedores_dic = {'Maria': 1200, 'José': 300, 'Antônio': 800, 'João': 1500, 'Francisco': 1900, 'Ana': 2750, 'Luiz': 400, 'Paulo': 20, 'Carlos': 23, 'Manoel': 70, 'Pedro': 90, 'Francisca': 80, 'Marcos': 1100, 'Raimundo': 999, 'Sebastião': 900, 'Antônia': 880, 'Marcelo': 870, 'Jorge': 50, 'Márcia': 1111, 'Geraldo': 120, 'Adriana': 300, 'Sandra': 450, 'Luis': 800}
meta = 1000

bonus = []

# for:
for valor in vendedores_dic:
    if vendedores_dic[valor] > meta:
        bonus.append(vendedores_dic[valor] * 0.1)
    else:
        bonus.append(0)
print(bonus)

# lc:
lista = [vendedores_dic[valor] * 0.1 if vendedores_dic[valor] > meta else 0  for valor in vendedores_dic]

print(lista)