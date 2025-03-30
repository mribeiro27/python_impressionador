import time
import locale

tempo_atual = time.localtime()
# print(tempo_atual)

# Como é um tempo que ainda não aconteceu, não podemos chamar uma função. Nesse caso, podemos fazer uma tupla com as infos
# Para deixar o código usável em qualquer ano, não iremos botar 2025, mas sim seguir pelo ano atual + 1
# Dia 1, mês 1, e 0 para todo o resto
tempo_ano_novo = (tempo_atual.tm_year + 1, 1, 1, 0, 0, 0, 0, 0, 0)

# Para fazermos as diferenças, o tempo deve estar em segundos, epara botar em seg, iremos usar a função mktime()
# print(tempo_ano_novo)

# Nas duas variáveis há uma tupla, logo podemos fazer a operação:
segundos_restantes = int(time.mktime(tempo_ano_novo) - time.mktime(tempo_atual))

# Na conta para transformação, queremos os dados de quociente e resto. Isso é feito através da função "divmod()". Os restos dos dias darão as horas, o resto das horas darão os minutos, assim em diante. Exemplo abaixo:

segundos_por_minuto = 60
segundos_por_hora = 60 * 60
segundos_por_dia = 24 * 60 * 60

'''print(f"Segundos por minuto: {segundos_por_minuto}")
print(f"Segundos por hora: {segundos_por_hora}")
print(f"Segundos por dia: {segundos_por_dia}")'''
      
print(divmod(130, segundos_por_minuto))

# O resultado será (2, 10), quociente e resto, agora iremos fazer um unpacking da tupla. O quociente será 2 e o resto será 10
quociente, resto = divmod(130, segundos_por_minuto)

# Para saber a quantidade de dias, iremos fazer também o unpacking de uma tupla. O restante será a quantidade de horas
dias, resto_segundos = divmod(segundos_restantes, segundos_por_dia)

# Deu 243 dias e 29234 segundos. Com os segundo restantes, descobriremos as horas. Ao invés de ser segundos restantes, será o resto dos segundos da conta dos dias
horas, resto_segundos = divmod(resto_segundos, segundos_por_hora)

# Deu 8h e 190 segundos restantes, que são 3 minutos
minutos, segundos = divmod(resto_segundos, segundos_por_minuto)

print(f"Faltam {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos para o Ano Novo!")

