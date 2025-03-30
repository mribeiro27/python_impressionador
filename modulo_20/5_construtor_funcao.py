# Impostos:
#produto 0.1
#serviço 0.15
#royalties 0.25

'''def calcular_preco_produto(preco):
    return preco * 0.1

def calcular_preco_servico(preco):
    return preco * 0.15

def calcular_preco_royalties(preco):
    return preco * 0.25'''

def calcular_imposto(imposto):
    # Queremos que o imposto seja aplicado na função que recebe o preço como parâmetro
    return lambda preco: preco * imposto

# Estes são construtores de função
calcular_preco_produto = calcular_imposto(0.1)
calcular_preco_servico = calcular_imposto(0.15)
calcular_preco_royalties = calcular_imposto(0.25)

print(calcular_preco_produto(100))
print(calcular_preco_servico(100))
print(calcular_preco_royalties(100))