preco_produtos = [100, 150, 300, 5500]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

#digamos que o imposto sobre os produtos é de 30%, ou seja, 0.3. Como eu faria para criar uma lista com os 
#valores de imposto de cada produto?

# for em várias linhas 

'''impostos = []

for item in preco_produtos:
    impostos.append(item * 0.3)
print(impostos)'''

# list comprehension

imposto = [preco * 0.3 for preco in preco_produtos]
print(imposto)

# list comprehension com função

def calcular_imposto(preco, imposto):
    return preco * imposto

impostos = [calcular_imposto(preco, 0.3) for preco in preco_produtos]

print(impostos)