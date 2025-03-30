preco = 1500
custo = 400
lucro = 800

def carga_tributaria(preco, custo, lucro):
    imposto = preco - custo - lucro
    carga = imposto / preco
    return carga

print("A carga tributária foi de: {:.1%}".format(carga_tributaria(1500, 400, 800)))

    