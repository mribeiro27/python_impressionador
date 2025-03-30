# O requests é necessário para usarmos o método GET para pegar a informação
import matplotlib.pyplot as plt
import requests
import json

## Cotação das moedas
cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
# Ao printar a var acima, será impresso: <Response [200]>. Se tranformarmos o dicionário JSON em dicionário import requests
cotacoes_dic = cotacoes.json()
# print(cotacoes_dic)

## Pegar as cotações (preço de compra, que é "bid") do Dólar, Euro e Bitcoin
'''print('Dólar: {}'.format(cotacoes_dic['USD']['bid']))
print('Euro: {}'.format(cotacoes_dic['EUR']['bid']))
print('Bitcoin: {}'.format(cotacoes_dic['BTC']['bid']))'''

## Pegar a cotação do Dólar nos 30 últimos dias
'''cotacoes_dolar30d = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
cotacoes_dolar_dic = cotacoes_dolar30d.json()
# Como são muitos valores, iremos botá-los em uma lista. Como os valores dos itens a serem iterados são do tipo "float" e da cotação, temos que declarar isso antes do loop
lista_cotacoes_dolar = [float(item['bid']) for item in cotacoes_dolar_dic]
print(lista_cotacoes_dolar)'''

## Pegar a cotação do Bitcoin entre Jan/20 e Outubro/20
cotacoes_btc = requests.get('https://economia.awesomeapi.com.br/json/daily/BTC-BRL/200?start_date=20200101&end_date=20201031')
cotacoes_btc_dic = cotacoes_btc.json()
lista_cotacoes_btc = [float(item['bid']) for item in cotacoes_btc_dic]
# Quando pegamos informações de dias, por padrão, os resultados retornados são de 30 dias. No link, antes da interrogação, botamos 200 ocorrências, para que consigamos pegar mais dias
# Vamos ter que fazer um reverse, pois o resultado será impresso com os valores de Outubro primeiro - ou seja, do valor mais atual para o mais antigo. Para o gráfico abaixo isso é muito importante, pois o crescimento do valor da moeda será visível e seguirá as datas corretamente
lista_cotacoes_btc.reverse()
print(len(lista_cotacoes_btc))

## Fazer um gráfico com as infos acima
plt.figure(figsize=(15, 5))
plt.plot(lista_cotacoes_btc)
plt.show()