from chave_api import chave_api
from IPython.display import display
# Imprime as informações em JSON indentadas
import pprint
import pandas as pd
# Transforma um texto em arquivo
from io import StringIO
import requests

# Substituir o "demo" pela chave API que foi gerada em https://www.alphavantage.co/support/#api-key
# o "?" inicia os parâmetros, que são dividos pelo "&"
# JSON: url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=ITUB3.SAO&apikey={chave_api}'

## Criação de tabela de cotações de 3 ações diferentes: Itaú, AMBEV, Banco do Brasil

# Lista de ações
'''acoes = ['ITUB4', 'ABEV3', 'BBAS3']

# Criação de tabela compilada, vazia, para popular com os valores das ações acima
compilada = pd.DataFrame() 

for acao in acoes:
    # Global Quote, usado pra saber o preço e volume
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={acao}.SAO&apikey={chave_api}&datatype=csv'
    r = requests.get(url)

    ## Extraindo as inforamções em JSON
    # data = r.json()

    # Pegando somente as informações da chave Meta Data
    # print(data['Meta Data'])

    ## Extraindo as informações em CSV: ele é impresso como um arquivo, não é um CSV propriamente dito. Para ser um CSV, devemos transformar o texto em arquivo
    data = r.text
    # print(data)

    # Transformando o texto em arquivo e o imprimindo como tabela
    tabela = pd.read_csv(StringIO(data))

    # Criação de uma lista de tabelas para a concatenação
    lista_tabelas = [compilada, tabela]

    # Concatenando as tabelas "compilada" e "tabela"
    compilada = pd.concat(lista_tabelas)

display(compilada)'''

## Encontrando ações de empresas através do nome, pelo parâmetro "keywords"

'''url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=amazon&apikey={chave_api}&datatype=csv'
r = requests.get(url)

tabela = pd.read_csv(StringIO(r.text))
display(tabela)'''

## Informações de resultados financeiros: disponíveis apenas em JSON, e os resultados devem ser apenas de empresas americanas
# Dica para trabalhar com os dicionários: biblioteca "pprint", que imprime as infos em JSON indentadas

url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol=AMZN&apikey={chave_api}'
r = requests.get(url)
data = r.json()
# pprint.pprint(data)

# Imprimindo a lista de dicionários "annualEarnings" em uma tabela Python, ou seja, transformando JSON em uma tabela Python
resultado = pd.DataFrame(data['annualEarnings'])
display(resultado)