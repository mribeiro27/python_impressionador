meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]

# Identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam

for item in vendas:
    nome, venda = item
    if venda > meta:
        print(f"O vendedor {nome} bateu a meta ao realizar {venda}")

# Identificar quais produtos tiveram maior venda em 2020 do que em 2019

# Criar uma variável auxiliar, dado que os valores das vendas vao ser substituídos
crescimento = 0

vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]

for produto, vendas_2019, vendas_2020 in vendas_produtos:
    if vendas_2020 > vendas_2019:
        crescimento = (vendas_2020/vendas_2019 - 1)
        print("O produto {} vendeu {} unidades em 2020, um crescimento de {:.1%} , comparado às vendas de 2019, que foram de {} unidades".format(produto, vendas_2020, crescimento, vendas_2019))