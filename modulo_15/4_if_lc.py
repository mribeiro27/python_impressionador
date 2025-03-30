meta = 1000
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

# for:
# i é o índice, que permite que usemos os índices das 2 listas, para fazer comparações entre si:
produtos_acima_meta = []

for i, produto in enumerate(produtos):
    if vendas_produtos[i] > meta:
        produtos_acima_meta.append(produto)
        
print(produtos_acima_meta)

#lc

produtos_meta = [produto for i, produto in enumerate(produtos) if vendas_produtos[i] > meta]
print(produtos_meta)

