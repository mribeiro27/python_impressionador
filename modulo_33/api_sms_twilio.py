# A Twilio é uma plataforma que faz o envio de SMS
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACc1b70ef4ce0c6b3938c5d4e490e9b721"
auth_token  = "7e188b9563213b330aa4ec2d5854fd83"

client = Client(account_sid, auth_token)

remetente = "+16195866719"
destinatario = "+5521999314832"

message = client.messages.create(
    to=destinatario,
    from_=remetente,
    body="Essa mensagem foi enviada porque tô estudando Pythinho :D")

print(message.sid)