# Rapid API: é um hub de APIs de diversas áreas criadas por diversos desenvolvedores
# É necessário criar uma conta no site, para uma key seja criada e também se inscrever na API desejada
# Abaixo, temos a API Forecast para consultar as informações do tempo em Berlim

import requests
import http.client

conn = http.client.HTTPSConnection("forecast9.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "Sign Up for Key",
    'x-rapidapi-host': "forecast9.p.rapidapi.com"
}

conn.request("GET", "/rapidapi/forecast/Berlin/summary/", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))