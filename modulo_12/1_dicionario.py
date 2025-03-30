mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

# Exemplo: queremos saber o número de vendas de iPhone. Para isso, criaremos uma variável e atribuir a ela o valor da chave 'iphone', no dicionário vendas_tecnologia, que é 15000

qtde_iphone = vendas_tecnologia['iphone']
print(qtde_iphone)

# Livro e Lazer mais vendidos

livro = mais_vendidos['livros']
lazer = mais_vendidos['lazer']

print(f"O livro mais vendido foi {livro}, e o artigo de lazer, {lazer}.")

# Quanto foi vendido de notebook Asus e iPad

notebook_asus = vendas_tecnologia['notebook asus']
ipad = vendas_tecnologia['ipad']

print(f"Foram vendidos {notebook_asus} notebooks Asus e {ipad} iPads.")