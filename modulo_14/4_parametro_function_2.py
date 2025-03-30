
produtos = ['beb46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

# Começar pela lógica
# Primeiro, queremos percorrer toda a lista de produto
# Verificar se o produto é uma bebida alcóolica
# Se for uma bebida alcóolica, exibir a mensagem

# Na função, botamos uma váriavel para podermos definir a ação da função
def alcoolico(bebida):
    bebida = bebida.upper()
    if "BEB" in bebida:
        return True
    else:
        return False
    
for produto in produtos:
    # Quando chamamos ela, podemos dar outro valor, como visto anteriormente, e esse valor pode ser uma variável
    if alcoolico(produto):
        print(f"Enviar o {produto} para o setor de bebidas alcóolicas.")
        # Quando printamos, o primeiro item, que começa com 'beb', continua minúsculo, mesmo tendo transformado para letras maiúsculas. Entretando, transformamos em letra maiúscula somente dentro da função, logo, fora da função, ela permanece minúscula
