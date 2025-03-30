venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia: ')
vendas = []
#crie aqui o programa

# Também poderia ser: while venda !=0:
while venda:
    vendas.append(venda)
    # Temos que copiar o input dentro do while, se não apenas um produto irá ser cadastrado e não conseguiríamos botar uma opção como vazio, a não ser a primeira
    venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia: ')

print('Registro Finalizado. As vendas cadastradas foram: {}'.format(vendas))