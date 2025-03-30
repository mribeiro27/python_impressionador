import webbrowser

# Podemos abrir várias páginas ao mesmo tempo, como a home da Hashtag e o blog
# O módulo webbrowser não é muito bom para integarir com a páginas abertas, sendo bom apenas para exibição

# Se possível, irá tentar abrir o site em uma nova janela
webbrowser.open_new('https://hashtagtreinamentos.com')
#webbrowser.open('https://www.hashtagtreinamentos.com/blog/')

# Os módulos do Selenium são muito bons para interações com sites, como clicar em botões, preencher forms