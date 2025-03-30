import matplotlib.pyplot as plt

vendas_meses = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 2362, 2100, 2762]
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

#plotar o gráfico da forma mais simples

# eixo X, eixo Y
plt.plot(meses, vendas_meses)
# Botar a legenda de Vendas no eixo Y
plt.ylabel("Vendas")
# Botar a legenda de Vendas no eixo X
plt.xlabel("Meses")
# O axis define o mínimo e o máximo de cada eixo [(xmin, xmax, ymin, ymax)]. Para pegar o máximo das vendas, caso fosse uma lista muito grande, seria só aplicar o max(lista). Podemos adicionar ao máximo também, apenas somando
plt.axis([0, 12, 0, max(vendas_meses) + 500])
# Mostra o gráfico
plt.show()