from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# Permite apertar uma tecla do teclado em um campo específico
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

caminho = os.getcwd()
arquivo = caminho + r"\formulario.html"

navegador.get(arquivo)

'''# Clicar no botão
clicar = navegador.find_element(By.XPATH, '/html/body/form/input[1]').click()
# Dar OK no pop-up: para isso, temos que apontar onde queremos ter a ação
pop_up = navegador.switch_to.alert
# Aceitar o pop-up
time.sleep(3)
pop_up.accept()'''

# Para extrair informações de botões, usamos os argumentos .text (não muito usado, pois o get_attribute('value') pode extrair textos), .get_attribute, is_selected (verificar se está selecionado)

# Marcar a checkbox
check1 = navegador.find_element(By.XPATH, '/html/body/form/input[2]').click()
check2 = navegador.find_element(By.XPATH, '/html/body/form/input[3]').click()

'''# Verificar se o botão está selecionado
is_checked1 = navegador.find_element(By.XPATH, '/html/body/form/input[2]').is_selected()
is_checked2 = navegador.find_element(By.XPATH, '/html/body/form/input[3]').is_selected()
print(is_checked1, is_checked2)'''

# Verficar qual a cor atual. Isso é importante para todos os campos a seguir, pois temos que verificar como está salvo no site. Assim conseguimos preencher corretamente e alçancar o resultado
'''cor = navegador.find_element(By.XPATH, '/html/body/form/input[4]').get_attribute('value')
print(cor)'''

# Mudar para a cor vermelha RGB 232 33 33 (só aceitar HEX)
cor_rgb = navegador.find_element(By.XPATH, '/html/body/form/input[4]').send_keys('#e60f10')

# Cor hexadecimal que está na página: #2143E8
cor_hex = navegador.find_element(By.XPATH, '/html/body/form/input[5]').send_keys('#2143E8')

# Datas
aniversario_cidade = navegador.find_element(By.XPATH, '/html/body/form/input[6]').send_keys('08/08/1960')

# Pegar o valor e verificar como o valor é armazenado. É armazenado como AAAA/MM/DD, mas no site deve ser preenchido como o formato de data brasileiro
aniversario_cidade_valor = navegador.find_element(By.XPATH, '/html/body/form/input[6]').get_attribute('value')
print(aniversario_cidade_valor)

# Data e hora de nascimento: são duas informações que devem ser passadas, e para preencher a segunda sem erro, um macete é dar tab entre as infos - o TAB que é possível com a biblioteca Keys
data_hora_nasc = navegador.find_element(By.XPATH, '/html/body/form/input[7]').send_keys('05/05/1997', Keys.TAB, '10:37')

# Verificar como os valores dos dados acima são apresentados: 1997-05-05T10:37
'''data_hora_nasc_tipo = navegador.find_element(By.XPATH, '/html/body/form/input[7]').get_attribute('value')
print(data_hora_nasc_tipo)'''

# Anexar um arquivo
anexo = navegador.find_element(By.XPATH, '/html/body/form/input[8]').send_keys(f'{arquivo}')

# Selecionar um mês e um ano
mes_ano = navegador.find_element(By.XPATH, '/html/body/form/input[9]').send_keys('agosto', Keys.TAB, '2024')

# Campo numérico

## Limpando o campo para evitar que o número indicado fique diferente do que o indicado no código
mes_ano = navegador.find_element(By.XPATH, '/html/body/form/input[10]').clear()
mes_ano = navegador.find_element(By.XPATH, '/html/body/form/input[10]').send_keys('123456789')

# Senha
senha = navegador.find_element(By.XPATH, '/html/body/form/input[11]').send_keys('senha123')

# Radio Buttons
radio_button = navegador.find_element(By.XPATH, '/html/body/form/input[13]').click()
'''is_radio_button_selected = navegador.find_element(By.XPATH, '/html/body/form/input[13]').is_selected()
print(is_radio_button_selected)'''

# Campo Time
time_futebol = navegador.find_element(By.XPATH, '/html/body/form/input[16]').send_keys('Flamengo')

# Horário
horario = navegador.find_element(By.XPATH, '/html/body/form/input[17]').send_keys('16:50')

# Semana: não foi necesssário dar tab entre as semanas e ano
semana = navegador.find_element(By.XPATH, '/html/body/form/input[18]').send_keys('34', '2024')

# Bloco de texto
bloco_texto = navegador.find_element(By.XPATH, '//*[@id="story"]').send_keys('Olá!', Keys.ENTER, 'Tudo bem?', Keys.ENTER, 'Meu nome é Mariana.', Keys.ENTER, 'Estou aprendendo Python e Selenium!', Keys.ENTER, 'Até mais!')

# Range (Slider)

## Pegar o valor, para que seja possível identificarmos a maneira de selecionar o número 70. Aqui dá 47
'''range = navegador.find_element(By.XPATH, '/html/body/form/input[15]').get_attribute('value')
print(range)'''

slider = navegador.find_element(By.XPATH, '/html/body/form/input[15]')
# Ao "limpar", se percebe que o padrão do range é 50. Para chegar até o 70, precisamos andar 20x
slider.clear()

for i in range(70 - 50):
    # Ao chegar no range, a tecla irá para a direita 20x, para chegar até o 70
    slider.send_keys(Keys.ARROW_RIGHT)

# Botões Dropdown: clicar na lista e selecionar a opção 

## Preencher o valor
'''dropdown = navegador.find_element(By.XPATH, '/html/body/form/select[1]').send_keys('A')'''

## Clicar na lista, esperar a lista abrir e clicar na opção 'A'
dropdown = navegador.find_element(By.XPATH, '/html/body/form/select[1]').click()
time.sleep(0.5)
opcao_a = navegador.find_element(By.XPATH, '/html/body/form/select[1]/option[1]').click()

# Selecionar a opção 'B' com from selenium.webdriver.support.ui import Select
opcao_b_select = navegador.find_element(By.TAG_NAME, 'select')
dropdown_select = Select(opcao_b_select)
# Como a letra B é o segundo elemento, é o índice 1
# Se fosse pelo value, teria que ver no código, pois o value no código pode não ser o que está na lista. É como o exemplo do site, dado que a letra no código estava minúscula, e no texto, maiúscula
'''opcao_b_select.select_by_index(1)
opcao_b_select.select_by_value('b')'''
dropdown_select.select_by_visible_text('B')

# Também há como deselecionar, com o método 'deselect_by'. nessa lista suspensa não é possível, pois ela sempre terá um  valor selecionado

# Verificar se um elemento é múltiplo
print(dropdown_select.is_multiple)

# Maneiras de ler o valor selecionado. Essa variável 'item' é o mesmo que "opcao_a = navegador.find_element(By.XPATH, '/html/body/form/select[1]/option[1]')""
'''item = dropdown_select.first_selected_option
print(item.get_attribute("value"))
'''

# Se fosse uma lista com várias opções para selecionar, para ler as opções, podemos declarar como:
'''lista_itens = dropdown_select.all_selected_options'''
# Para ler o texto, deve-se indicar o índice do item na lista
'''print(lista_itens[0].text)'''

time.sleep(10000)