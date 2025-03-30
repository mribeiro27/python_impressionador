import keyboard
import time

# O keyboard.press_and_release demora um tempo para acontecer, enquanto o de escrever na barra de Iniciar é muito rápido. Para isso, iremos usar o sleep

# Abre o Iniciar do Windows
keyboard.press_and_release('win')
time.sleep(1)

# Digita isso na barra do Iniciar
keyboard.write('chrome')
time.sleep(1)

# Dá enter para abrir o Chrome
keyboard.press_and_release('enter')
time.sleep(1)

# Escreve o site na barra de navegação
keyboard.write('hashtagtreinamentos.com')

# Dá o enter e entre no site
keyboard.press_and_release('enter')
