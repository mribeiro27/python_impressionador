import time

'''tempo_atual_segundos = time.time()
# Em nanossegundos
tempo_atual_segundos = time.time_ns()

print(f"Tempo atual: {tempo_atual_segundos} segundos desde a Epoch")'''

# --------------------------------------------------------

'''print("Iniciando a pausa")
time.sleep(5)  # Pausa o programa por 5 segundos
print("Pausa terminada")'''

#---------------------------------------------------------

# Converte o tempo expresso em segundos. desde a EPOC, em uma str represetnando o tempo local
# O formato da data se torta mais legível. Naturalmente, ele vem em inglês, mas é possível transformar em português

'''tempo_em_segundos = time.time()
tempo_local = time.ctime(tempo_em_segundos)
print(f"Tempo local: {tempo_local}")'''

#---------------------------------------------------------

tempo_em_segundos = time.time()
tempo_local = time.localtime(tempo_em_segundos)

# Todas as informações na tupla
print(f"Tempo local: {tempo_local}")
# Como nos exemplos abaixo, podemos selecionar as informações que queremos pegar, e elas não serão inseridas em tupla, e sim impressas indivisualmente
print(f"Tempo local: {tempo_local.tm_year}")

# Retorna um objeto struct_time, que é uma tupla com posições de significado

#---------------------------------------------------------

# Função time: pega a quantidade de segundos que se passaram desde a epoc time
print(time.time())
# Se passar esse tempo em segundos e passar para a ctime(), vamos ter uma string dizendo as informações
print(time.ctime(time.time()))
# O objeto struct_time se comporta como uma tupla dá todas as informações, e temos mais poder sobre elas
print(time.localtime())