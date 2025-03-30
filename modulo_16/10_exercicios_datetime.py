'''- `year`: ano (por exemplo, 2023)
- `month`: mês (1-12)
- `day`: dia (1-31)
- `hour`: hora (0-23)
- `minute`: minuto (0-59)
- `second`: segundo (0-59)
- `microsecond`: microssegundo (0-999999)
- `tzinfo`: fuso horário'''

'''from datetime import datetime

ultima_compra = datetime(2024, 3, 10)
data_atual = datetime.now()

diferenca = data_atual - ultima_compra

# O tipo da variável "diferença" é timedelta, logo, conseguimos pegar apenas a quantidade de dias desde a última compra, através do "diferenca.days"
# print(type(diferenca))

if diferenca.days > 30:
    print("Faz mais de 30 dias desde sua última compra, logo, você é elegível para descontos!")
else:
    print("Não faz 30 dias desde sua última compra, logo, você não é elegível para descontos.")'''

from datetime import datetime, timezone, timedelta

data_hora_atual = datetime.now()

fuso_horario_sao_paulo = timezone(timedelta(hours=-3))
data_hora_sao_paulo = data_hora_atual.astimezone(fuso_horario_sao_paulo)
print(f"Data/hora atual em São Paulo: {data_hora_sao_paulo}")

data_hora_atual = datetime.now()

fuso_horario_new_york = timezone(timedelta(hours=-4))
data_hora_new_york = data_hora_atual.astimezone(fuso_horario_new_york)
print(f"Data/hora atual em Nova Iorque: {data_hora_new_york}")  

data_hora_atual = datetime.now()

fuso_horario_tokyo = timezone(timedelta(hours=+9))
data_hora_tokyo = data_hora_atual.astimezone(fuso_horario_tokyo)
print(f"Data/hora atual em Tóquio: {data_hora_tokyo}")

# Uma função é a melhor forma de verificar, pois é só passarmos a variável da hora da cidade que a função irá fazer a condição de acordo com a hora, somente
def verifica_horario(data_hora):
    if 9 <= data_hora.hour < 17:
        return "Aberto"
    else:
        return "Fechado"

print(f"Escritório de São Paulo está: {verifica_horario(data_hora_sao_paulo)}")
print(f"Escritório de Nova Iorque está: {verifica_horario(data_hora_new_york)}")
print(f"Escritório de Tóquio está: {verifica_horario(data_hora_tokyo)}")