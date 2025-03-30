from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

caminho = r"C:\Users\322070\OneDrive - OPEN LABS S.A\Área de Trabalho\python_impressionador\modulo_29\janelas_abas_printscreen\Pagina Hashtag.html"
navegador.get(caminho)

# Clicar no banner do "Power BI Impressionador"
navegador.find_element(By.XPATH, '/html/body/section[2]/div/div[6]/figure/a/img').click()

# Preenchendo o formulário
'''navegador.find_element(By.NAME, 'firstname').send_keys("Mariana")'''
# Se tentarmos preencher o formulário diretamente, não irá dar certo, dado que o link do navegador é o que está setado. Logo, antes de preencher, temos que mudar pra nova aba

### Mudando de aba
# Verificando as abas que estão sendo controladas pelo Selelium. Elas irão aparecer conforme a ordem que foram abertas. O nome vem codificado, então abaixo está a maneira de identificá-las
lista_abas = navegador.window_handles
'''print(lista_abas)'''

# Teremos a aba original, que é a primeira que abre quando rodamos o código e a segunda, que é a do banner que clicamos
aba_original = navegador.window_handles[0]
nova_aba = navegador.window_handles[1]

# Alterando a aba e preenchendo o formulário
navegador.switch_to.window(nova_aba)

navegador.find_element(By.NAME, 'firstname').send_keys("Mariana")
navegador.find_element(By.NAME, 'email').send_keys("mariana@email.com")

# Retornando para a aba original e clicando em outro banner
navegador.switch_to.window(aba_original)
navegador.find_element(By.XPATH, '/html/body/section[2]/div/div[8]/figure/a/img').click()

# Como o nome das abas vem codificado, podemos saber quais são abas, em ordem, através do título das mesmas
for aba in navegador.window_handles:
    navegador.switch_to.window(aba)
    print(navegador.title)

# O nome das abas será printado, e aqui podemos ver que, realmente, são 3 abas abertas
abas = navegador.window_handles
print(len(abas))

### Mudando para outra janela
# Se clicarmos com o botão direito em outro banner, mas para abrir em uma nova janela, esta também estará sob o Selenium, e o número de abas irá aumentar. Ele fez pelo Jupiter, então ele consegue rodar o código novamente e será possível interagir com a página aberta manualmente (Curso SQL)

'''aba_sql = navegador.window_handles[3]
navegador.switch_to.window(aba_sql)

navegador.find_element(By.ID, 'fullname').send_keys("Mari Janela")
navegador.find_element(By.ID, 'email').send_keys("janela@mari.com")'''

# Fecha a última janela/aba aberta
navegador.close()
# Tempo para ver a a janela e todo o navegador fechando
time.sleep(3)
# Fecha todo o navegador
navegador.quit()

time.sleep(10000)