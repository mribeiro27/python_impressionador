cpf_clientes = ['762.196.080-97', '263.027.380-67', '827.363.930-40', '925.413.640-91', '870.565.160-33', '892.080.930-50', '462.126.030-81', '393.462.330-10', '393.462.330-10', '393.462.330-10', '988.305.810-11', '596.125.830-05', '596.125.830-05', '990.236.770-48']

# Normalmente, para saber um tamanho de uma lista (quantidade de clientes), usaríamos o len desta forma
print(len(cpf_clientes))

# Só que, em uma lista, os valores podem se repetir. Para verificarmos se há repetições, iremos transformar a lista em um set
set_cpf_clientes = set(cpf_clientes)
print(len(set_cpf_clientes))

# Há 11 clientes na loja. Podemos transformar esse set, com os valores aparecendo apenas uma vez, em uma lista:
lista_cpf_clientes = list(set_cpf_clientes)
print("Há {} clientes na loja.".format(len(lista_cpf_clientes)))