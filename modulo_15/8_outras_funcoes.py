produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte', 'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
top5 = ['agua', 'brahma', 'skol', 'coca', 'leite de castanha']

total_vendas = sum(vendas)
print(total_vendas)

'''total_top5 = 0

# for:
# Usar para iterar 2 listas do mesmo índice
for i, produto in enumerate(produtos):
    if produto in top5:
    # Popula a lista e vai adicionando conforme a condição 
        total_top5 += vendas[i]
        
print(total_top5)

total = (total_top5 / total_vendas)
print("O total de vendas dos TOP 5 produtos representa {:0.1%} das vendas totais.".format(total))'''

# lc: como estamos fazendo uma única ação em um iterable, podemos usar o list comprehension

# Somar o vendas[i] apenas do top 5
total_top5 = sum(vendas[i] for i, produto in enumerate(produtos) if produto in top5)
print(total_top5)
print('TOP 5 representou {:0.1%} das vendas'.format(total_top5/sum(vendas)))