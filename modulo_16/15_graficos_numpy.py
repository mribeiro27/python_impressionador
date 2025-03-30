#importando o matplotlib
import matplotlib.pyplot as plt

#importando o módulo numpy. Ele gera um range com muitos números, então o gráfico fica com muitas curvas
import numpy as np

# randint() gera um range de inteiros com mínimo, máximo e a quantidade dos números. Será entre 1000 e 2999, excluindo o 3000
# o random faz parte do np
vendas = np.random.randint(1000, 3000, 50)

# Gera um range de números do primeiro, excluindo o último
meses = np.arange(1, 51)

# plt.plot = gera um gráfico de linha

#editando o tamanho e a cor da linha - quais parâmetros posso editar?

# x, y
# O "ro" torna o gráfico em um de bolinhas vermelhas; o "r--" o deixa tracejado; o "bs" deixa quadrados azuis; "g^" deixa com triângulos verdes
plt.plot(meses, vendas, color = "red")
# Botar em escala, indo de 0 a 50 no eixo x, e no y, de ao maior valor de vendas, somado 200
plt.axis([0, 50, 0, max(vendas) + 200])
plt.xlabel("Meses")
plt.ylabel("Vendas")
plt.show()

# Gráfico de dispersão
plt.scatter(meses, vendas)
plt.show()

# Gráfico de barras
plt.bar(meses, vendas)
plt.show()

# Mostrar os gráficos acima juntos
# figure(): o espaço funciona como uma única figura, então iremos fazer um subplot, que pede a quantidade de linhas (1), quantas colunas (vamos botar 3, logo, 3), e o último como posição (1). Podemos escrever os números sem vírgula também, como 131. Agora, é necessário somente plotar os gráficos após os subplots

plt.figure(1, figsize=(15, 3))
plt.subplot(1, 3, 1)
plt.plot(meses, vendas, color = "red")
plt.subplot(1, 3, 2)
plt.scatter(meses, vendas)
plt.subplot(1, 3, 3)
plt.bar(meses, vendas)
plt.show()