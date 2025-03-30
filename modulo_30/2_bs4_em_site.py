# Segunda forma de resolver a raspagem de dados. Essa forma também caiu no mesmo erro. A anterior é mais fácil de tratá-los
from bs4 import BeautifulSoup
import requests

link = 'https://coinmarketcap.com/'

requisicao = requests.get(link)

# O código do site é salvo na variável requisição, por isso utilizamos o BS4 apenas em sites estáveis
# print(requisicao.text)

site = BeautifulSoup(requisicao.text, "html.parser")
# print(site.prettify())

# Normalmente, uma tabela dentro de um site fica dentro de uma tag chamanda tbody
tbody = site.find("tbody")
# Para pegarmos as linhas da tabela, pegaremos as tags tr
linhas = tbody.find_all("tr")

for linha in linhas:
    # Todas as informações da linha são impressas juntas, e para separar, iremos usar ;
    texto_linha = linha.get_text(separator=';')
    # Agora, a partir do ponto-vírgula, as palavras e números serão separados
    texto_linha_separado = texto_linha.split(";")
    # print(texto_linha_separado)
    nome = texto_linha_separado[1]
    preco = texto_linha_separado[3]
    print(nome, preco)
