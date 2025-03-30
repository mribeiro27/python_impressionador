lucro_1tri = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
lucro_2tri = {'abril': 88000, 'maio': 89000, 'junho': 120000}

#adicionando 1 item

lucro_1tri["abril"] = 880000
print(lucro_1tri)

#adicionando vários itens ou um dicionário a outro

lucro_1tri.update(lucro_2tri)
# lucro_1tri.update({'abril': 88000, 'maio': 89000, 'junho': 120000})
print(lucro_1tri)

#adicionando um item já existente (manualmente ou pelo update)

# Para modificar o valor de uma chave, iremos usar a mesma estrutura de adicionar, mas com a chave existente e seu novo valor. É impossível haver 2 chaves iguais. Se tentarmos botar uma mesma chave, com outro valor, a chave que foi posta por último é a que é printada

lucro_1tri["janeiro"] = 88000

lucro_fev = 85000

lucro_1tri["fevereiro"] = lucro_fev
print(lucro_1tri)

# Remover itens

# Remover o mês de junho com del:
    # Se botássemos como abaixo, o dicionário é deletado
    # del lucro_1tri 
'''del lucro_1tri["junho"]
print(lucro_1tri)'''

#.pop() não só tira um item la lista, mas o armazena num variável, caso queira usá-la depois
lucro_junho = lucro_1tri.pop("junho")

print(lucro_1tri)
# O valor da chave "junho" fica armazenado aqui
print(lucro_junho)

# Se quiséssmos apagar o conteúdo todo o do dicionário, ao invés de del, deve-se usar o .clear()
lucro_1tri.clear()
print(lucro_1tri)

#obs: o del também funciona para listas, caso queira usar -> ao invés de usar a chave, deveremos usar o índice do item que deve ser removido
#del lista[i]

funcionarios = ['João', 'Lira', 'Maria', 'Ana', 'Paula']

del funcionarios[0]
print(funcionarios)