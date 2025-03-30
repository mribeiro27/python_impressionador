meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
#seu código aqui

# vendedores_acima_meta = [] -> primeira forma
# vendedores_acima_meta = 0 -> segunda forma

'''for venda in vendas:
    if venda[1] >= meta:
        # Adiciona o nome do vendedor à lista de vendedores acima da meta
        vendedores_acima_meta.append(venda)
print(vendedores_acima_meta)
# Dividir o tamanho da lista de vendedores que bateram a meta pela lista de vendas nos dá a porcentagem de vendedores que bateram a meta
print("{:.1%} dos vendedores bateram a meta!".format(len(vendedores_acima_meta) / len(vendas)))'''

# Cálculo diretamente na lista

'''for venda in vendas:
    if venda[1] >= meta:
        vendedores_acima_meta += 1
print("{:.1%} dos vendedores bateram a meta!".format(vendedores_acima_meta / len(vendas)))'''

# Vendedor que mais vendeu

melhor_vendedor = ''
maior_venda = 0

for venda in vendas:
    if venda[1] > maior_venda:
        maior_venda = venda[1]
        melhor_vendedor = venda[0]
print(f"O melhor vendedor foi {melhor_vendedor}, com {maior_venda} vendas!")