from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# Importando as bibliotecas de Explicit Waits para ser possível fazer o Expect Conditions 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# No site da Hashtag, por exemplo, os elementos carregam. Mas, em alguns segundos, um pop-up irá aparecer. Como precisamos esperar que esse elemento apareça ou carregue, iremos utilizar a biblioteca time, um loop ou o Expected Conditions (próprio do Selenium)

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.hashtagtreinamentos.com/")

## Biblioteca Time
'''time.sleep(15)
navegador.find_element(By.CLASS_NAME, 'eicon-close').click()'''

## Loop
# Procurar uma lista de elementos da classe 'eicon-close'. Enquanto ela for vazia, iremos esperar 1s
'''while len(navegador.find_elements(By.CLASS_NAME, 'eicon-close')) < 1:
    time.sleep(1)
# É bom botar um outro  sleep() aqui, para dar tempo de vermos o pop-up sendo fechado
time.sleep(1)
navegador.find_element(By.CLASS_NAME, 'eicon-close').click()'''

## Expected Conditions
# O Selenium irá verificar, de 500 em 500 milissegundos se aquela condição foi seguida. Iremos esperar o navegador por 20s, até que o elemento esperado seja localizado
elemento = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'eicon-close')))

# sleep() para vermos o pop-up sendo fechado
time.sleep(1)
elemento.click()

time.sleep(10000)