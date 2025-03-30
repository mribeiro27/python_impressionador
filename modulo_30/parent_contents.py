from bs4 import BeautifulSoup
import re

with open("Pagina Hashtag.html", "r", encoding="utf-8") as arquivo:
    # O html.parser faz o parse do HTML para o BS4
    site = BeautifulSoup(arquivo, "html.parser")

'''textos = site.find_all(string=re.compile("alunos"))
print(textos)'''

## Parent: pega a tag presente e as anteriores ao elemento
# Para ver os elementos (tags) que contêm os textos acima, podemos usar o Parent. Quantos mais ".parent"usamos, mais veremos as tags pai do elemento selecionado. No caso abaixo, o elemento que contém o primeiro texto é um mark, e mark é contido em h2
'''parent_primeiro_texto = textos[0].parent.parent
print(parent_primeiro_texto)'''

## Contents: pega as tags posteriores ao elemento
# É retornada uma lista de tags que vêm após a tag nav
nav = site.find("nav")
# Como vemos aqui, o botão é o segundo elemento, o primeiro é uma string vazia
print(nav.contents)

'''for elemento in nav.contents:
    # Aparecerao 2 elementos: um botão e uma div bem grande
    print(elemento)
    print()'''

botao = nav.contents[1]
# Uma lista de conteúdos será impressa, e a próxima tag, que é o span, aparecerá
print(botao.contents)

titulo = site.find(id="mais-de-50-000-de-alunos-formados-por-todos-os-cursos-da-hashtag")
# Mostra a tag seguinte da qual está inserida o id informado 
print(titulo.contents)
# Agora, para pegar o conteúdo dessa tag seguinte, faremos: .contents[0] -> selecionar a primeira tag retornada; .contents -> pegar o conteúdo dessa tag
print(titulo.contents[0].contents)