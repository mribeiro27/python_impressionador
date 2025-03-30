from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# Importando o Action Chains
from selenium.webdriver import ActionChains
import time
import os

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

caminho = os.getcwd()
arquivo = caminho + r"\Pagina Hashtag.html"

navegador.get(arquivo)

# É melhor fazer desta forma, dado que o site pode mudar e essa ação do Action Chains deve ser atualizada
## Opção sem o Action Chains - e sem as infos, dado que não está sendo possível acessar o site informado
# Quando há um menu que parece ser dropdown, mas que quando clicamos nos redireciona para outro link, podemos conseguir extrair o link da página desejada (a qual aparece no menu dropdown)
link = navegador.find_element(By.XPATH, '').get_attribute('href')
print(link)

## Action Chains: simula a ação do mouse, mas sem usar esse
# Conseguir colocar o mouse em cima do botão que vira menu dropdown e aí sim clicar na opção desejada (Curso de SQL)

# XPATH do menu dropdown
menu = navegador.find_element(By.XPATH, '')
# XPATH da opção desejada
curso_sql = navegador.find_element(By.XPATH, '')

# Colocar o mouse em cima do menu dropdown
ActionChains(navegador).move_to_element(menu)

# Clicar na opção "Curso de SQL"
ActionChains(navegador).click(curso_sql)

time.sleep(10000)