vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]

# Farturamento de iPhone no dia 20/08/2020:

# Para realizarmos o cálculo, devemos botar o valor da variável para que esta não tenha os valores substituídos, e sim adicionados À ela
faturamento = 0

for item in vendas:
# Forma que também dá pra fazer, ao invés de atribuir as variáveis à item
# for data, produto, cor, capacidade, unidades, valor_unitario in vendas
    # Ver as tuplas da lista
    # print(item)
    # Agora, para ficar fácil fazer os cálculos, iremos fazer o unpacking da tuplas. Botar igual ao item, e não vendas
    data, produto, cor, capacidade, unidades, valor_unitario = item
    if produto == "iphone x" and data == "20/08/2020":
        # Conforme o loop roda, valores serão adicionados na variável
        faturamento += unidades * valor_unitario
print(f"O faturamento de iPhone no dia 20/08/2020 foi de: {faturamento} reais")

# Produto mais vendido no dia 21/08/2020

# Variáveis auxiliares
qtde_produto_mais_vendido = 0
produto_mais_vendido = ""

for item in vendas:
    data, produto, cor, capacidade, unidades, valor_unitario = item
    if data == "21/08/2021":
        if unidades > qtde_produto_mais_vendido:
            # Se as unidades do produto que está sendo analisado for maior que a do anterior, o valor será atribuido à variável de produto e quantidade deste (variáveis auxiliares)
            produto_mais_vendido = produto
            qtde_produto_mais_vendido = unidades
            # Se quiséssemos adicionar mais atributos, como a cor e capacidade do produto, seria só fazer como acima
print("O produto mais vendido no dia 21/08/2020 foi {}, com {} unidades vendidas.".format(produto_mais_vendido, qtde_produto_mais_vendido))