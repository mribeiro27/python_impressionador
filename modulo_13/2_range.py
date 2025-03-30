#uso mais comum no for:
produtos = ['arroz', 'feijao', 'macarrao', 'atum', 'azeite']
estoque = [50, 100, 20, 5, 80]

# Números de 0 a 4 serão impressos de cada vez
'''for i in range(5):
    print(i)'''

# Na lista acima temos 5 itens, então podemos fazer da mesma forma
'''for i in range(5):
    print("Há {} unidades do produto {} em estoque.".format(estoque[i], produtos[i]))'''

#range com inicio e fim

# Quando rodamos o código abaixo, é impresso somente (range 1, 10). Para imprimir os números, como o range é um iterable, é necessário usar o for
'''print(range(1, 10))'''

#vamos olhar no for para entender

# Ele printa o primeiro número, mas exclui o último, imprimindo até o números antes deste
'''for i in range(1, 10):
    print(i)'''

# Funcionários classe B: devemos pegar o meio, pois 10% são os melhores e os outros 10% são os piores, restando 80%

funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo']
vendas = [2750, 1900, 1500, 1200, 1111, 1100, 999, 900, 880, 870, 800, 800, 450, 400, 300, 300, 120, 90, 80, 70]

# print(len(funcionarios))
# Temos 20 funcionários, e 80% desses são 16. Ou seja, os 10% melhores são os 2 primeiros, e os 10% piores, os 2 últimos

# Como um título, vamos botar aqui, para que não repita toda hora:
'''print("Funcionários Classe B:")
for i in range(2, 18):
    print("{}: fez {} vendas".format(funcionarios[i], vendas[i]))'''

#range com passo
# print(range(0, 1000, 10))

for i in range(0, 1000, 10):
    print(i)