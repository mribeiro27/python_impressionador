# Função normal:

def minha_funcao(num):
    return num * 2
print(minha_funcao(5))

# Lambda Expression:

minha_funcao_le = lambda num: num * 2
print(minha_funcao_le(5))

# Criar uma função que calcula o preço de produtos acrescido de imposto: 

imposto = 0.3

minha_funcao_le2 = lambda preco: preco * (1 + imposto)
print(minha_funcao_le2(300))