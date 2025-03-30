#texto para upper
cod_produto = 'beb12304'
print(cod_produto.upper())

# lista para sort e extend. 

# A função .sort() só tem parâmetro de palavra-chave
vendas_ano = [100, 200, 50, 90, 240, 300, 55, 10, 789, 60]
vendas_novdez = [500, 1555]

vendas_ano.sort()
print(vendas_ano)

vendas_ano.sort(reverse=True)
print(vendas_ano)

# A função .extend() recebe um iterable (lista, set, tupla, etc): no caso do exemplo, recebe um parâmetro (lista) que é adicionada à outra lista
vendas_ano.extend(vendas_novdez)
print(vendas_ano)
