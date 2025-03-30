import numpy as np

vendas = np.array([[50, 60, 70, 65, 80],
                   [85, 90, 78, 92, 88],
                   [72, 75, 68, 77, 76]])

vendas_dia = vendas.sum(axis=0)
print(f"Número de produtos vendidos no dia 1: {vendas_dia[0]}")
print(f"Número de produtos vendidos no dia 2: {vendas_dia[1]}")
print(f"Número de produtos vendidos no dia 3: {vendas_dia[2]}")
print(f"Número de produtos vendidos no dia 4: {vendas_dia[3]}")
print(f"Número de produtos vendidos no dia 5: {vendas_dia[4]}")

vendas_produto = vendas.sum(axis=1)
print(f"O número de produtos A vendidos por dia é de: {vendas_produto[0]}")
print(f"O número de produtos B vendidos por dia é de: {vendas_produto[1]}")
print(f"O número de produtos C vendidos por dia é de: {vendas_produto[2]}")