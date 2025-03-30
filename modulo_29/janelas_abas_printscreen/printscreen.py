from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from PIL import Image
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

caminho = r"C:\Users\322070\OneDrive - OPEN LABS S.A\Área de Trabalho\python_impressionador\modulo_29\janelas_abas_printscreen\Pagina Hashtag.html"
navegador.get(caminho)

# Dá pra tirar com o pyautogui, mas com ele o computador fica travado, e com o Selenium podemos ter autonomia e mesmo assim ele consegue fazer os prints

# Tirar print de tela inteira: o print será salvo na pasta do código, mas podemos passar o caminho também, caso desejarmos que seja salvo em outra pasta. Pode ser salvo em qualquer extensão de imagem
navegador.save_screenshot("print.png")

# Tirar print de partes específicas da tela: a imagem de tela inteira será cortada com uma ferramenta de edição de imagem: opencv ou PIL.
imagem = Image.open("print.png")

# Vamos supor que queremos tirar print da barra de navegação. Para isso, iremos selecionar esse elemento e pegar sua posição e tamanho
elemento = navegador.find_element(By.ID, "header")
posicao = elemento.location
tamanho = elemento.size

x_inicial = posicao["x"]
y_inicial = posicao["y"]
x_final = x_inicial + tamanho["width"]
y_final = y_inicial + tamanho["height"]

# Em uma tupla, iremos passar os cantos da diagonal em que a imagem será cortada (x_inicial, y_inicial e x_final e y_inicial)
imagem = imagem.crop((x_inicial, y_inicial, x_final, y_final))
imagem.save("print_cortado.png")

time.sleep(10000)