# Às vezes, você vai fazer tudo certo no Selenium e aparentemente não vai funcionar o seu código
# Possivelmente o elemento que você está tentando selecionar está dentro de um iFrame
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

link = "https://pbdatatrader.com.br/jogosdodia"

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Entrar no site
navegador.get(link)
# O Power BI pode demorar a carregar, então é bom dar um sleep()
time.sleep(10)

# Queremos pegar os pontos por jogo mandante da 1ª linha da tabela
# O elemento que queremos está dentro de um iFrame, que está dentro de outro iFrame, por isso não é possível encontrá-lo diretamente
# valor_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[19]/transform/div/div[3]/div/div/visual-modern/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div[5]'

# texto = navegador.find_element(By.XPATH, valor_xpath).text'''

# Procurando os iFrames e verificando quantos existem
# lista_iframes = navegador.find_elements(By.TAG_NAME, 'iframe')
# print(len(lista_iframes))

# Com o switch_to.frame(), iremos mudar, assim como mudamos de janela e aba, para o primeiro iFrame
iframe = navegador.find_element(By.TAG_NAME, 'iframe')
navegador.switch_to.frame(iframe)

# Indo para o segundo iFrame
iframe = navegador.find_element(By.TAG_NAME, 'iframe')
navegador.switch_to.frame(iframe)

# Agora assim podemos encontrar o elemento desejado
valor_xpath = '//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[19]/transform/div/div[3]/div/div/visual-modern/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div[5]'

texto = navegador.find_element(By.XPATH, valor_xpath).text
print(texto)

time.sleep(10000)