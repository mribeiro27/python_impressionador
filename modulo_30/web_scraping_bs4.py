# O Beautiful Soup 4 é uma ferramenta de web scraping, então conseguimos percorrer páginas HTML para extrair e modificar informações
## Vantagem: mais fácil de configurar e mais rápido que o Selenium
## Desvantagens: só consegue funcionar em páginas estáticas, pois ele carrega as informações de um site e as armazena em uma variável. Ele não consegue ler sites dinâmicos, que têm informações carregadas conforme scrollamos ou ficamos no site
### Não é possível fazer o scraping de dados de alguns sites, e nem realizar múltiplas requisições de uma vez - são feitas através da biblioteca "requests"

from bs4 import BeautifulSoup
# Regex (re): códigos que epresentam um padrão de texto - exemplo: primeiro caracter deve ser um número; letra, etc 
import re

# Como iremos fazer apenas leitura da página, passar o parâmetro "r". A página tem muitos caracteres do idioma português, então temos que passar o encoding
with open("Pagina Hashtag.html", "r", encoding="utf-8") as arquivo:
    # O html.parser faz o parse do HTML para o BS4
    site = BeautifulSoup(arquivo, "html.parser")

# A var "site" é o HTML da página, então é retornado o código do site no terminal. Para o HTML ser mais legível, usaremos o .prettify()
# print(site.prettify())

# Pegar informações do site
## Sem o "".text", a tag <title> também é impressa
'''titulo = site.find("title")
print(titulo.text)

# Aparece o conteúdo e tags que estão presentes dentro do h1. Se botarmos ".text", também irá aparecer só o conteúdo da tag
h1 = site.find("h1")
print(h1.text)

# Dentro do nav, que é a barra de navegação, encontramos muitas tags
nav = site.find("nav")
print(nav.prettify())

# Para pegar os links presentes na barra de navegação, iremos fazer o seguinte. Uma lista de links será impressa
# Se tivéssemos botado apenas ".find("a")", iria pegar apenas o primeiro link

#links = nav.find("a")
# É possível também pegar os links pelo índice
#print(links[1])

links = nav.find_all("a")
print(links)
print(len(links))

# É possível pegar os atributos de um link, que irão ser impressos num dicionário
print(links[0].attrs)

# Extraindo URLs
url_link = links[0]["href"]
print(url_link)

# Extraindo todos os links da nav
for link in links:
    print(link["href"])

## Encontrando elementos com várias regras

# Irá pegar todos os botões e links presentes na nav, respectivamente
elementos_nav = nav.find_all("button", "a")'''

## Outras regras de .find(): classe, id, atributos, texto, pedaços de texto

# Class: como "class" é uma palavra reservada no Python, é a única que tera um underline depois
'''subtitulo = site.find(class_="tit")
print(subtitulo)

# Id: traz tudo o que está dentro da tag header
header = site.find(id="header")
print(header)

# Role
header_2 = site.find(role="banner")
print(header_2)

# É possível encontrar elementos através de 2 filtros
header_3 = site.find(id="header", role="banner")
print(header_3)'''

# Não é possível passar parâmetros com hífens, apenas dentro de um dicionário. Se passarmos mais parâmetros, já que temos um dicionário, os outros devem estar inseridos neste - o "class" não precisa ser passado com um underline no final
'''logo = site.find("img", {"data-ll-status":"loaded", "class":"custom-logo"})
print(logo)'''

# Texto
## É igual
foco_mercado = site.find(string="Foco no Mercado")
print(foco_mercado)

## Contém texto: iremos usar a biblioteca de Regular Expressions (Regex)
### Achando textos que possuem a palavra "alunos", com o "re.compile=("string")"
textos = site.find_all(string=re.compile("alunos"))
print(textos)