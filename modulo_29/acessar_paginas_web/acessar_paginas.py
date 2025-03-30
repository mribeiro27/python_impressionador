from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# Pegar o caminho de um arquivo na mesma pasta do código
import os

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Pegar o Current Work Directory e contatenar com o nome do arquivo
caminho = os.getcwd()
arquivo = caminho + r"\Pagina Hashtag.html"

navegador.get(arquivo)

# Formas de selecionar um elemento na web através do Selenium: id (melhor, pois cada item tem um id, que geralmente não é substituído - nem todo item tem um id), XPath, nome da classe, nome, texto, tipo de informação, tag
# É melhor começar com a seguinte ordem - do que menos tem chances de ser alterado para o que mais tem chances: ID (se tiver) > Classe (se for única) > XPath (é o caminho do elemento, mas este também pode ser mudado de lugar)

# Dá um item como resposta: navegador.find_element

# ID: Selecionar e preencher o campo de nome da Newsletter
campo_nome = navegador.find_element(By.ID, "fullname").send_keys("Mariana")

# ID: Selecionar e preencher o campo do e-mail da Newsletter, pelo ID
campo_email = navegador.find_element(By.ID, "email").send_keys("mariana@email.com") 

# ID: Clicar no botão de enviar
campo_botao_enviar = navegador.find_element(By.ID, "_form_176_submit").click()

# CLASS_NAME: Clicar na imagem para ir para a home - no caso do exemplohá 2 classes, mas podemos usar apenas uma, que não repita
campo_img_home = navegador.find_element(By.CLASS_NAME, "custom_logo").click()

# XPATH: Clicar na imagem para ir para a home. É recomendado usar com aspas simples
# Não consegui pegar o XPath, pois o HTML não aparece, apenas o CSS
campo_img_home = navegador.find_element(By.XPATH, '').click()

# TAG: Para pegar textos de elementos, uma forma mais tranquila de encontrá-los é pelas tags
titulo = navegador.find_element(By.TAG_NAME, "h2").text
print(titulo)

# PARTIAL_LINK_TEXT: No caso do exemplo, para conseguir o número de Whatsapp, iremos pegar um pedaço do texto de um link. O selenium vai verificar todos os links da página, e se um link tiver "Whatsapp", ele irá printar
numero_whatsapp = navegador.find_element(By.PARTIAL_LINK_TEXT, "WhatsApp").text
print(numero_whatsapp)

# LINK: Pegamos o link através do atributo "href". O atributo também pode ser uma classe, por exemplo
link_wpp = navegador.find_element(By.XPATH, '').get_attribute('href')
print(link_wpp)

# NAME: Selecionar e preencher o campo de e-mail da Newsletter
nome = navegador.find_element(By.NAME, 'email').send_keys("pythonimpressionador@gmail.com")

# IMAGEM: Pegar o XPath referente à imagem desejada. Geralmente, mesmo no inspecionar, o link da imagem não é necessariamente correspondente À imagem - ver se a imagem aparece nas tags acima
link_img = navegador.find_element(By.XPATH, '').get_attribute("pythonimpressionador@gmail.com")

# Dá uma lista python como resposta: navegador.find_elements

# Como há vários elementos com a classe "nav-link"
lista_elementos = navegador.find_elements(By.CLASS_NAME, 'nav-link')
for elemento in lista_elementos:
    if "blog" in elemento.text.lower():
        elemento.click()
        break