import requests
import pprint

# A API de Agregados tem muitas informações.Nela temos o "Query Builder", onde podemos criar URLs através dos tópicos que temos interesse
'''link_ibge = requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/7392/periodos/2014/variaveis/10484?localidades=N1[all]')'''
link_ibge = requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/7392/periodos/2014/variaveis/10484?localidades=N1[all]')
link_ibge_dic = link_ibge.json()

# A variável "link_ibge_dic" é uma lista que tem um único item. Mesmo assim, para pegarmos o único item, temos que informar [0]
'''pprint.pprint(link_ibge_dic[0])'''

# Pegar a variável (Número de espécies da fauna e da flora brasileira avaliadas quanto ao risco de extinção) e série (2014)

# Para selecionar elementos desta lista "link_ibge_dic", temos que ir por partes e sempre mencionar o [0] antes da pesquisa
variavel = link_ibge_dic[0]['variavel']

# Os "series", que são os resultados, estão inseridos no parâmetro "resultados"
series = link_ibge_dic[0]['resultados'][0]['series']

print(variavel)
print(series)