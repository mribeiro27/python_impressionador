# Não estou conseguindo concluir isso no site da Hashtag, mas fiz pelo site da Oi

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# Pegar o caminho de um arquivo na mesma pasta do código
# import os

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Pegar o Current Work Directory e contatenar com o nome do arquivo
# caminho = os.getcwd()
#arquivo = caminho + r"\Pagina Hashtag.html"

site = 'https://www.oi.com.br/'

navegador.get(site)

# lista_elementos = navegador.find_elements(By.TAG_NAME, 'figure')
lista_elementos = navegador.find_elements(By.CLASS_NAME, 'signStreaming__cardContent')

# Através do for, podemos encontrar elementos (que estão em grnade número) que estejam dentro de determinada tag (a)
# Quando não há links associados na tag/classe desejada, iremos fazer um try/except, assim não acusará o erro:
for elemento in lista_elementos:
    try:
        # Também é possível usar o find_elements aqui, que gera uma lista, e usamos o if para não usar o try/except
        lista_links = elemento.find_element(By.TAG_NAME, 'a').get_attribute('href')
        print(lista_links)
    except:
        continue