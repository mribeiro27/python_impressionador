'''lista = [150, 10, 30, 2000, 90]

lista.sort()
print(lista)'''

# Como a função faz uma ação, botar o nome dela com verbos no infinitivo
def cadastrar_produto():
    produto = input("Digite o nome do produto a ser cadastrado: ")
    produto_minusculo = produto.casefold()

    print(f"Produto '{produto_minusculo}' cadastrado com sucesso.")

for i in range(3):
    cadastrar_produto()
