#1

'''import numpy as np

dados = [127, 90, 201, 150, 210, 220, 115]

dados_np = np.array(dados)

media_np = np.mean(dados_np)

print(media_np)'''

#2

'''import numpy as np

precos = np.array([31.40, 31.25, 30.95, 31.20, 31.60, 31.50])

max = np.max(precos)
print(max)
min = np.min(precos)
print(min)
variacao = max - min
print(variacao)'''

#3

import numpy as np

quantidades = np.array([5, 3, 2])
precos = np.array([100, 200, 50])

vendas = [quantidades * precos]

total_vendas = np.sum(vendas)
print(total_vendas)