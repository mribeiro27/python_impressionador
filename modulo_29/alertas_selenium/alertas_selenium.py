from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# Importando a biblioteca "Alert"
from selenium.webdriver.common.alert import Alert
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

caminho = r"C:\Users\322070\OneDrive - OPEN LABS S.A\Área de Trabalho\python_impressionador\modulo_29\alertas_selenium\alertas.html"
navegador.get(caminho)

## O alerta é proveniente do navegador, diferente do pop-up, que é um algo que podemos interagir

### Alerta Básico: clicando no botão para aparecer o alerta
'''alerta_basico = navegador.find_element(By.XPATH, '/html/body/div[1]/input').click()

## Formas de selecionar o alerta para interação
# Forma simples
# alerta = navegador.switch_to.alert
# Forma completa (importação da biblioteca "Alert")
alerta = Alert(navegador)

## Interagindo com o alerta
# Dando OK para fechar, mas com um sleep(), para dar tempo de vermos o conteúdo do alerta
time.sleep(2)
alerta.accept()'''

### Alerta de Confirmação
'''alerta_confirmacao = navegador.find_element(By.XPATH, '/html/body/div[2]/input').click()

# Selecionando o alerta para interação
alerta = Alert(navegador)

# Dando OK
time.sleep(2)
alerta.accept()

# Cancelando
time.sleep(2)
alerta.dismiss()'''

### IMPORTANTE: podemos extrair o texto do alerta da seguinte maneira
'''alerta = Alert(navegador)
texto = alerta.text
print(texto)'''

### Alerta com Input
alerta_input = navegador.find_element(By.XPATH, '/html/body/div[3]/button').click()

# Selecionando o alerta para interação
alerta = Alert(navegador)

## Preenchendo o input
# Há um bug entre o Selenium e o Google Chrome, porque quando preenchemos o campo através do Selenium, o campo parece que não foi preenchido, mas quando damos o accept pelo código, aparece exatamente o número/texto que preenchemos na caixa via código. Quando o accept é manual, não aparecerá o que foi preenchido no texto abaixo.
time.sleep(2)
alerta.send_keys("12345678901")

time.sleep(2)
alerta.accept()

time.sleep(10000)