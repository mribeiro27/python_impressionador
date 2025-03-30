from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os

# Fazer com que a pop-up sobre a segurança do arquivo não apareça - forma antiga, hoje em dia é direto no navegador
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"c:\Users\322070\Downloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

caminho = os.getcwd()
arquivo = caminho + r"\login.html"

navegador.get(arquivo)

# Login 
login = navegador.find_element(By.XPATH, '/html/body/div/form/input[1]').send_keys('Mariana')
senha = navegador.find_element(By.XPATH, '/html/body/div/form/input[2]').send_keys('123456')
botao_login = navegador.find_element(By.XPATH, '/html/body/div/form/button').click()

# Importar a base de clientes
tabela = pd.read_excel('NotasEmitir.xlsx')
print(tabela)

# Formulário
## O formulário deve ser preenchido automaticamente para todas as pessoas da planilha, dependendo da quantidade de clientes nesta
### O tabela.index permite que as linhas sejam percorridas, e não as colunas, para que todas as linhas sejam números e reconhecidos como os clientes

for linha in tabela.index:
  # Todas as informações das linhas devem ser passadas individualmente, de acordo com cada cliente. Para isso, vamos percorrer todas as linhas: tabela.index_loc(linha, coluna)
  ## Todos os campos que forem numéricos, teremos que transformar em string
  nome = navegador.find_element(By.NAME, 'nome').send_keys(tabela.loc[linha, 'Cliente'])
  endereco = navegador.find_element(By.NAME, 'endereco').send_keys(tabela.loc[linha, 'Endereço'])
  bairro = navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[3]').send_keys(tabela.loc[linha, 'Bairro'])
  cidade = navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[4]').send_keys(tabela.loc[linha, 'Municipio'])
  cep = navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[5]').send_keys(str(tabela.loc[linha, 'CEP']))
  uf = navegador.find_element(By.NAME, 'uf').send_keys(tabela.loc[linha, 'UF'])
  cpf = navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[6]').send_keys(str(tabela.loc[linha, 'CPF/CNPJ']))
  inscricao_estadual = navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[7]').send_keys(str(tabela.loc[linha, 'Inscricao Estadual']))
  descricao = navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[8]').send_keys(tabela.loc[linha, 'Descrição'])
  qtde = navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[9]').send_keys(str(tabela.loc[linha, 'Quantidade']))
  valor_unitario = navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[10]').send_keys(str(tabela.loc[linha, 'Valor Unitario']))
  valor_total = navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[11]').send_keys(str(tabela.loc[linha, 'Valor Total']))
  botao_emitir_nota = navegador.find_element(By.CLASS_NAME, 'registerbtn').click()
  
  # Recarregar a página para limpar o formulário para a criação de nota fiscal dos outros clientes
  navegador.refresh()

# Fechar o navegador depois de baixar todas as notas fiscais
navegador.quit()

time.sleep(10000)