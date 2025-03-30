# Para o código ficar rodando um código 24h por dia, temos que fazer o deploy do nosso código. As opções de fazer isso são: realmente deixar o computador rodando o código (configurando o Python para rodar em um determinado tempo) e agendador de tarefas. Uma outra opção é deixar em um computador que nunca desliga, ou seja, um servidor (Google (Google Cloud) Amazon (AWS), Microsoft (Azure), Heroku (planos gratuitos e fácil configuração, plugins))

import requests
from datetime import datetime

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_dic = requisicao.json()
cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
cotacao_euro = requisicao_dic["EURBRL"]["bid"]
cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

print(f"Cotação Atualizada. {datetime.now()}\nDólar: R${cotacao_dolar}\nEuro: R${cotacao_euro}\nBTC: R${cotacao_btc}")