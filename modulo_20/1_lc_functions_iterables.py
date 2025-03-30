def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace("  ", " ")
    texto = texto.strip()
    return texto

produtos = [' ABC12 ', 'abc34', 'AbC37', 'beb12', ' BSA151', 'BEB23']

# Para que possamos alterar um item de uma lista, iremos nos guiar pelo índice e usar o enumerate, pois seria:
# produtos[i] = novo valor

'''for i, produto in enumerate(produtos):
    produtos[i] = padronizar_texto(produto)
print(produtos)'''

# map: botar a função e a lista que será iterada, aplicando essa função ao percorrer a lista
# Temos que botar list, pois o map retorna um objeto, assim como o zip

produtos = list(map(padronizar_texto, produtos))
print(produtos)