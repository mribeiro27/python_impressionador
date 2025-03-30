# Primeira forma de resolver a raspagem de dados
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
    '''# Linhas serão impressas com todos os conteúdos das tags trs
    print(linha.prettify())
    # Dar espaço entre as tags
    print()'''
    # Para pegar os nomes das moedas, iremos pegar uma classe que se repita para todas
    try:
        print(linha.find(class_= "ehyBa-d").text)
        print(linha.find(class_="dzgUIj").text)
    # Caso não tivesse encontrado pela classe, poderíamos encontrar o preço pelo "/$": em Regex, precisamos botarcom a barra na frente para indicar que apenas o texto seja impresso
    # print(linha.find(string=re.compile("/$")))
    # Com o find_all(), serão retornados todos os valores com $, e assim poderíamos escolher qual o montante desejado
    # print(linha.find_all(string=re.compile("/$"))[2])
    except AttributeError:
        break

# Tratando os erros retornados acima: algumas tags tr têm muitas informações - as 10 primeiras - e as outras, não, pois as outras moedas são carregadas conforme o usuário scrolla pelo site. Como o BS4 não performa em páginas dinâmicas, essas informações não carregam, pois não há um navegador como no Selenium. Iremos tratar os erros com um try/except