def minha_soma(*numeros, num1):
    soma = 0
    for numero in numeros:
        soma += numero
    soma += num1
    return soma


print(minha_soma(2, 5, 1, num1 = 5))