# Por meio do Selenium, é possível executar comandos JS no computador
# Isso é essencial para dar scroll na tela, como no caso do Youtube, por exemplo

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get("https://www.youtube.com/results?search_query=python")

# Antes de declarar a lista e o loop, iremos scrollar a tela através do JS
# Fazer 1000 scrolls, 30x - 29, dado que começará no 0
for i in range(30):
    # Se executarmos um scroll de 1000 várias vezes, ele não vai sair do lugar, então temos que multiplicá-lo
    qtde_scroll = i * 2000
    navegador.execute_script(f'window.scroll(0, {qtde_scroll})')
    # Para evitar erros, dado que o site demora um pouco para carregar o scroll, iremos usar um sleep de 2s
    time.sleep(2)

# Abrir o navegador, entrar no Youtube e pegar 50 vídeos que retornam da busca por "python"
# O que é semelhante em todos os vídeos é o ID "thumbnail"
lista_videos = navegador.find_elements(By.ID, "thumbnail")

# Como queremos 50 vídeos, precisamos scrollar para que mais vídeos com links úteis (que não sejam None) vão pra lista de vídeos
for video in lista_videos:
    print(video.get_attribute("href"))

time.sleep(10000)