# Unpacking: é a maneira mais útil de acessar os valores de uma tupla. Ao invés de pegar os valores pelo índice, iremos desmembrar a tupla em várias variáveis

vendas = ('Lira', '25/08/2020', '15/02/1994', 2000, 'Estagiário')

'''nome = vendas[0]
data_contratacao = vendas[1]
data_nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]'''

# Atribuindo os valores da tupla à novas variáveis. O importante é saber o número de itens da tupla, para que criemos o número correto de variáveis e não cair em erro

nome, data_contratacao, data_nascimento, salario, cargo = vendas
print(salario)

# Enumerate e tuplas

vendas = [1000, 2000, 300, 300, 150]
funcionarios = ['João', 'Lira', 'Ana', 'Maria', 'Paula']

'''for i, venda in enumerate(vendas):
    print('{} vendeu {} unidades'.format(funcionarios[i], venda))'''

# o enumerate faz unpacking: pega os valores e os transforma em tuplas
for item in enumerate(vendas):
    i, venda = item
    print(i)
    print(item)