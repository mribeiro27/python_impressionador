vendas = [941, 852, 783, 714, 697, 686, 685, 670, 631, 453, 386, 371, 294, 269, 259, 218, 208, 163, 125, 102, 87, 47, 7]
vendedores = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']
meta = 50

# Printar todos os funcionários que bateram a meta:

# O índice deverá começar como 0
i = 0

while vendas[i] > meta:
    # PROBLEMA: Diferente do for, o índice não mudará. Se deixarmos apenas com essa linha de código no while, o nome e as vendas de Maria irão ser repetidos infinitamente 
    print("{} bateu a meta. Números de vendas: {}".format(vendedores[i], vendas[i]))
    # SOLUÇÃO: somar o valor da variável i com 1, de forma a percorrer todas as listas
    i += 1
