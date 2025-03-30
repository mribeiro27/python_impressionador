vendas = ('Lira', '25/08/2020', '15/02/1994', 2000, 'Estagiário')

# Irá ser printado entre parêntesis
print(vendas)

# Para acessarmos os valores da tupla, através dos índices, iremos usar os colchetes (assim como em listas)

# Se tentarmos modificar o valor de um item da tupla, ou mesmo fazer um append, irá retornar um erro
# vendas[3] = 3000

nome = vendas[0]
data_contratacao = vendas[1]
data_nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]

print(cargo)