meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}

def calculo_meta(meta, vendas):
    # A lista auxiliar deve ficar fora do for, mas dentro da function
    bateram_a_meta = []
    for vendedor in vendas:
        if vendas[vendedor] > meta:
            bateram_a_meta.append(vendedor)
    porcentagem_bateram_meta = len(bateram_a_meta) / len(vendas)
    return bateram_a_meta, porcentagem_bateram_meta

# Para as informações saírem sepaadas, devemos fazer o unpacking destas
funcionarios_bateram_meta, porcentagem_atingimento_meta = calculo_meta(meta, vendas)

print("A porcentagem de funcionários a bater a meta foi de {:.1%}".format(porcentagem_atingimento_meta))
print(f"Lista de funcionários que bateram a meta: {funcionarios_bateram_meta}")
