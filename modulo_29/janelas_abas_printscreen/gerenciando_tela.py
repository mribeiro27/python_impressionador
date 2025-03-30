from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

servico = Service(ChromeDriverManager().install())
# navegador = webdriver.Chrome(service=servico)

# caminho = r"C:\Users\322070\OneDrive - OPEN LABS S.A\Área de Trabalho\python_impressionador\modulo_29\janelas_abas_printscreen\Pagina Hashtag.html"
# navegador.get(caminho)

## Maximizar
# navegador.maximize_window()

## Minimizar
# navegador.minimize_window()

## Headless: é um argumento que faz com que a automação ocorra de forma oculta, ou seja, o processo acontece normalmente, mas a janela não se abre. Pra isso, iremos criar um novo navegador
# Além do headless, também é possível iniciar a automação com o navegador maximizado: "--start-maximized" e também sem extensões: "--disable-extensions", por exemplo
# Às vezes pode não funcionar no modo headless
options = webdriver.ChromeOptions()
options.add_argument('--headless')
novo_nav = webdriver.Chrome(service=servico, options=options)
novo_nav.get("https://google.com")
print(novo_nav.title)

time.sleep(10000)