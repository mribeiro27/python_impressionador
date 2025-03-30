# No caso do exemplo, o "m" minúsculo indica que o padrão será minúsculo
# Como a padronização seja na função, temos que fazer um for para percorrer toda a lista

def padronizar_codigos(lista_codigos, padrao='m'):
    #seu código aqui
    for i, item in enumerate(lista_codigos):
        item = item.replace("  ", " ")
        item = item.strip()
        # Tem que ser if-elif, pois só tem a opção de ser a letra "m" maiúscula ou minúscula
        if padrao == "m":
            item = item.casefold()
        elif padrao == "M":
            item = item.upper()
        # Se deixarmos até o código acima, vai imprimir como a lista foi introduzida. Com a linha abaixo, aí sim cada item dela sorfrerá as alterações. Botar o enumerate no for, para que possamos incluir a variável "i"
        lista_codigos[i] = item
    # Dará, como resposta, a lista toda padronizar com letra maiúscula ou minúscula
    return lista_codigos


cod_produtos = [' ABC12 ', 'abc34', 'AbC37']
print(padronizar_codigos(cod_produtos, padrao = 'm'))