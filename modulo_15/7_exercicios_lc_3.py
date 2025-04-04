estoque = [('BSA2199',396),('PPF5239',251),('BSA1212',989),('PPF2154',449),('BEB3410',241),('PPF8999',527),('EMB9591',601),('BSA2006',314),('EMB3604',469),('EMB2070',733),('PPF9018',339),('PPF1468',906),('BSA5819',291),('PPF8666',850),('BEB2983',353),('BEB5877',456),('PPF5008',963),('PPF3877',185),('PPF7321',163),('BSA8833',644),('PPF4980',421),('PPF3063',757),('BSA2089',271),('BSA8398',180),('EMB4622',515),('EMB9814',563),('PPF3784',229),('PPF2398',270),('BEB3211',181),('PPF8655',459),('PPF1874',799),('PPF8789',126),('PPF6324',375),('EMB9290',883),('BSA5516',555),('BSA8451',243),('BSA8213',423)]

lista_500 = []
lista_1000 = []

# for:

for produto, qtde_estoque in estoque:
    if qtde_estoque < 200:
        lista_1000.append(produto)
    elif qtde_estoque < 1000:
        lista_500.append(produto)

print(f"Realizar pedido de 500 unidades para os seguintes produtos: {lista_500}")
print(f"Realizar pedido de 1000 unidades para os seguintes produtos: {lista_1000}")

# lc:

lista = [1000 if qtde_estoque < 200 else 500 for produto, qtde_estoque in estoque]
print(lista)