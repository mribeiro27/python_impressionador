#retornar um boolean
def bateu_meta(vendas, meta):
    if vendas >= meta:
        return True
    else:
        return False

vendas_jose = 500
meta = 230

if bateu_meta(vendas_jose, meta):
    print("José bateu a meta.")

#retornar uma lista, tupla ou dicionario
def filtrar_lista_texto(lista, pedaco_texto):
    lista_filtrada = []
    for item in lista:
        if pedaco_texto in item:
            lista_filtrada.append(item)
    # O return deve estar sempre fora do for, senão irá pegar apenas o primeiro item, fazer a verificação e o loop irá terminar
    return lista_filtrada


lista_email = ["mari@exemplo.com", "mel@exemplinho.com", "allan@exemplo.com"]

print(filtrar_lista_texto(lista_email, "exemplo"))