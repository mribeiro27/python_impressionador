# A função abaixo faz: exibe uma caixa para cadastrar o produto e trata a info para ser cadastrado de forma correta

def cadastrar_produto():
    produto = input('Digite o nome do produto que deseja cadastrar: ')
    produto = produto.casefold()
    # Remove espaços no início ou final de uma string
    produto = produto.strip()
    # No código anterior, printamos a frase com o nome do produto imputado. Só que isso não é por si só o cadatro do produto, só foi para mostrar que, de fato, isso foi cadastrado. Logo, isso não deveria estar dentro da nossa função. 
    # O return executa o código e dá como resposta a variável produto. O return define a variável retornada
    # Uma var, quando usada dentro de uma function, ela só existe dentro dela, exemplo abaixo
    return produto
    # Nada mais é executado depois do return

# Uma var, quando usada dentro de uma function, ela só existe dentro dela, exemplo abaixo
# cadastrar_produto()
# A variável produto não está deifinida, é retornado um erro
# print(produto)

# Como a variável produto não existe fora de função, podemos usá-la
produto = cadastrar_produto()
# O valor da variável produto, recebido na função, é impresso aqui
print(produto)

