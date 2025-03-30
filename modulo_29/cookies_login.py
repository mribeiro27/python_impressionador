from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

servico = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# Argumento para direcionar o perfil que inicializará com o navegador - na barra do navegador, botar "chrome://version/", e lá terá "Caminho de perfil". Ao invés de "Default", iremos criar "Profile Selenium" ao rodar o código
# É bom já criar um perfil para o Selenium, pois o uso do "user-data-dir" pode não ser compatível com o Default ou outro perfis já criados
options.add_argument(r'user-data-dir=C:\Users\322070\AppData\Local\Google\Chrome\User Data\Profile Selenium')
navegador = webdriver.Chrome(service=servico, options=options)

# Aproveitar logins já feitos: vamos criar perfis no Chrome, através do código, e quando logarmos nesses perfis, tudo ficará salvo nesse
# No exemplo, o login do Whatsapp ficará savlo no perfil do Selenium, dado que a liberação do QR Code foi feita durante a automação
navegador.get("https://web.whatsapp.com")

time.sleep(10000)