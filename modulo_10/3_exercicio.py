vendas = []

# No caso abaixo, apenas uma condição basta, pois se não há produtos, não há quantidades

'''# A melhor forma para rodar o while, com uma comparação embaixo para limitar o loop
while True:
    produto = input("Digite o nome do produto. Se não houver produtos para registrar, aperte ENTER: ")
    if not produto:
        break
    qtde = int(input("Digite a quantidade vendida do produto. Se não houver quantidades para registrar, aperte ENTER: "))
    # Para adicionar uma lista de 2 elementos na lista vendas:
    vendas.append([produto, qtde])

print(vendas)'''

# Como no caso acima, apenas a constatação, no while, de que produtos está preenchido, basta

produto = input("Digite o nome do produto. Se não houver produtos para registrar, aperte ENTER: ")
qtde = int(input("Digite a quantidade vendida do produto. Se não houver quantidades para registrar, digite 0: "))

while produto:
    # Para adicionar uma lista de 2 elementos na lista vendas:
    vendas.append([produto, qtde])
    produto = input("Digite o nome do produto. Se não houver produtos para registrar, aperte ENTER: ")
    # Um problema com essa forma é que é necessário preencher a quantidade, dado que é um int, e o "produto:" vale apenas para strings. Deve-se botar 0
    qtde = int(input("Digite a quantidade vendida do produto. Se não houver quantidades para registrar, digite 0: "))

print(vendas)




