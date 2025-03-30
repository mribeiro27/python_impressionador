# API ViaCep: informamos o CEP e ele nos dá as informações acerca deste; se botarmos o endereço, o CEP será retornado

import requests
import pandas as pd
from IPython.display import display

## Busca de CEP 

'''cep = "26.600-000"

# Transforma o CEP com os traços e pontos em um número corrido
cep = cep.replace("-", "").replace(".", "").replace(" ", "")

link_cep = f'https://viacep.com.br/ws/{cep}/json/'
requisicao = requests.get(link_cep)

# Código HTTP retornado
# print(requisicao)

# Como a resposta é um dicionário, podemos imprimir as informações da forma que for desejada

if len(cep) == 8:
    dic_requisicao= requisicao.json()

    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    bairro = dic_requisicao['bairro']
    rua = dic_requisicao['logradouro']

    print(f'Estado: {uf}\nCidade: {cidade}\nBairro: {bairro}\nRua: {rua}')
else:
    print("CEP inválido.")'''

## Busca de endereços: voltarão as informações referentes ao lado par e ímpar da rua

uf = 'RJ'
cidade = 'Rio de Janeiro'
rua = 'Senador Vergueiro' 

link_endereco = f'https://viacep.com.br/ws/{uf}/{cidade}/{rua}/json/'
requisicao_endereco = requests.get(link_endereco)
dic_requisicao_endereco = requisicao_endereco.json()

print(dic_requisicao_endereco)

# Tabela com os CEPs da rua
tabela = pd.DataFrame(dic_requisicao_endereco)
display(tabela)