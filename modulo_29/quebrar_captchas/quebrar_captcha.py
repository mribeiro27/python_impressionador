from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# O tipo de captcha do link é um Recaptcha v2 sem proxy
from anticaptchaofficial.recaptchav2proxyless import *
import time
# Chave da API que eles enviam por e-mail. Para botar esse "from chave", ele criou um arquivo chamado chave.py com a variável "chave_api", que deve ser importada para esse arquivo
from chave import chave_api

link = "https://google.com/recaptcha/api2/demo"

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get(link)

# Formas de quebrar captchas: treinar uma IA, serviços de quebrar captchas. No caso do exemplo, foi usado o AntiCaptcha
chave_captcha = navegador.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey')

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key(chave_captcha)
solver.set_website_url(link)
solver.set_website_key(chave_api)

resposta = solver.solve_and_return_solution()

if resposta != 0:
    print(resposta)
    # Preencher o campo do token do captcha
    # g-recaptcha-response
    navegador.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
    navegador.find_element(By.ID, 'recaptcha-demo-submit').click()
else:
    print(solver.err_string)

time.sleep(10000)