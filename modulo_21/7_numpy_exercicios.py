import numpy as np

salarios = np.array([3000, 2500, 3500, 4000, 2000, 4500, 3000, 3800, 4800])

media = np.mean(salarios)
print(media)

acima_media = np.where(salarios > media)
print(salarios[acima_media])

# O count_nonzero() conta os índices que são verdadeiros, de acordo com a comparção
qtde_funcionarios = np.count_nonzero(salarios > media)
print(f"{qtde_funcionarios} funcionários ganham acima da média.")

# Para conseguir pegar o número de posições que compreendem o where, devemos fazer a comparação, pois aqui voltarão os valores true e false:

#funcionarios = (salarios > media)
# print(funcionarios)

# qtde_funcionarios = np.sum(salarios > media)
# print(qtde_funcionarios)