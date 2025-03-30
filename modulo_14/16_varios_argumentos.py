# Normalmente, botam *args
def minha_soma(*numeros):
    # Mostra que é uma tupla, faz o processo contrário do unpacking, pois une todos os valores em uma tupla
    print(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

# Permite botar vários argumentos
print(minha_soma(10, 13, 1, 90, 0, 9, 8))

# **kwargs: argumentos de palavras-chave
# Function para calcular o preço final de um produto
# Passarmos um argumento que não existe no código não tem problema, ele será ignorado, como no caso de 'mudanca_cor'

def preco_final(preco, **adicionais):
    # Quando passamos **, podemos ter quantos argumentos quisermos, contanto que passemos uma palavra-chave e seu valor, ou seja, é um dicionário de adicionais. Se adicionamos um desconto, desconto está dentro do dicionário de adicionais
    print(adicionais)
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra'] 
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco

print(preco_final(1000, desconto = 0.1, garantia_extra = 100, imposto = 0.3))
# Se adicionarmos um adicional que não está no código, ele será ignorado. No print acima, dá 1300, e aqui, mesmo adicionando 150, o resultado é o mesmo
# print(preco_final(1000, desconto = 0.1, garantia_extra = 100, imposto = 0.3, mudanca_cor = 150))