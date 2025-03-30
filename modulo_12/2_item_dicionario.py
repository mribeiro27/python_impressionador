mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

# Livro mais vendido

print("O livro mais vendido foi: {}.".format(mais_vendidos["livros"]))

# Vendas do notebook Asus

print("Vendemos {} notebook Asus.".format(vendas_tecnologia.get("notebook asus")))

# Procurando uma chave que não está na lista com o método .get(): é retornado "None"

print(vendas_tecnologia.get("ipads"))

# Procurando uma chave que não está na lista com a chave direto: é retornado um erro
# Para não ocorrer erros durante o desenvolvimento, a dica é fazer um if, para verificar se o item copo está dentro de alguma chave

# print(mais_vendidos["ipads"])

if "copo" in vendas_tecnologia:
    print(vendas_tecnologia["copo"])
else:
    print("Copo não está dentro da lista de produtos de tecnologia.")

if vendas_tecnologia.get("copo") == "None":
    print("Copo não está dentro da lista de produtos de tecnologia.")
else:
    print(vendas_tecnologia.get("copo"))
