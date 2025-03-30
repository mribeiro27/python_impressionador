# Na tabela ASCII, as letras maiúsculas vêm antes das letras minúsculas, então não é verdadeiramente uma ordem alfabética

produtos = ['apple tv', 'mac', 'IPhone x', 'IPhone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
# produtos.sort()
# print(produtos)

# Para fazer com que a regra seja correta, iremos usar uma key, que será aplicada antes mesmo do sort e corrige o problema. Para isso, iremos botar todas as letras em minúsculo:

produtos.sort(key=str.casefold)
print(produtos)

# Não dá pra ordenar dicionário, então para isso, iremos transformá-lo em uma lista de tuplas, com o list e .items:

vendas_produtos = {'vinho': 100, 'cafeiteira': 150, 'microondas': 300, 'iphone': 5500}

'''lista_vendas = list(vendas_produtos.items())
print(lista_vendas)'''

# Agora que podemos ordenar, temos um outro problema: o primeiro item está como o produto, então não será possível deixar na ordem numérica crescente. Para isso, iremos usar uma função que ordena pelo segundo item:

def segundo_item(tupla):
    return tupla[1]

lista_vendas = list(vendas_produtos.items())
lista_vendas.sort(key=segundo_item)
# print(dict(lista_vendas))
print(lista_vendas)