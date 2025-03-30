from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

caminho = os.getcwd()
arquivo = caminho + r"\formulario.html"
navegador.get(arquivo)

time.sleep(1000)