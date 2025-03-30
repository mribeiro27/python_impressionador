import requests
import pprint
import pandas as pd
from IPython.display import display

# Esse endpoint do BC permite que a gente faça requisições de qualquer tamanho, mas há muitas APIs que só permitem até um limite. Um parâmetro "offset" permite que nossas requisições não tenham limites. O "skip" é um contador que permite começar a contagem de qualquer número: se quisermos começar do 10000, o skip terá valor de 9999
link =requests.get('https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10&$orderby=Data%20desc&$format=json')
link_dic = link.json()

# pprint.pprint(link_dic)

tabela = pd.DataFrame(link_dic['value'])
# display(tabela)

# Formatando as unidades dos valores, $, etc, com o "map"
tabela["Quantidade"] = tabela["Quantidade"].map("{:,}".format)
tabela["Valor"] = tabela["Valor"].map("R${:,.2f}".format)

display(tabela)

# Criando tabela para abrigar todos os valores somados
tabela_final = pd.DataFrame()

# A variável foi criada aqui, para que conforme as requisições sejam feitas, o "skip" aumenta 10 mil
pular_indice = 0

# Tornando o "skip" dinâmico: vamos pegar o link, fazer a requisição, transformar o resultado em tabela (de 10000) linhas. Só que não queremos só com 10 mil linhas, e sim que outras 10 mil sejam adicionadas
while True:
    link = requests.get('https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$skip=10000&$orderby=Data%20desc&$format=json')
    link_dic = link.json()
    tabela = pd.DataFrame(link_dic['value'])
    if len(link_dic['value']) < 1:
        break
    # Depois que todos os valores encontrados pela API forem adicionados na tabela e 'value' for menor que 1, iremos adicionar os valores da tabela na tabela_final que criamos anteriormente (como são listas, devemos adicionar os colchetes)
    tabela_final = pd.concat([tabela_final, tabela])
    pular_indice += 10000
display(tabela_final)