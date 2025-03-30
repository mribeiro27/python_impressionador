import time
import locale

'''# Range: começa do 10, vai tirando 1 até o 0
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("O evento começou!")'''

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

tempo_em_struct = time.localtime()
tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M:%S", tempo_em_struct)
print(f"Tempo formatado: {tempo_formatado}")