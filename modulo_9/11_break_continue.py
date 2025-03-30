vendas = [100, 150, 1500, 2000, 120]
meta = 110

# Se todas as vendas forem maiores que a meta, a loja ganha bônus:

'''for venda in vendas:
    if venda < meta:
        # O código irá percorrer todas as vendas da lista, e se tiver algum menor, a loja não irá ganhar bônus
        print("A loja não ganha bônus.")
        # Mas nesse caso, com o break, se algum valor já for menor que 110 (que no caso é o primeiro), irá parar ali, sem percorrer elas outras vendas da lista
        break
print(venda)'''

# Exiba quem bateu a meta:

vendedores = ["João", "Julia", "Ana", "José", "Maria"]
meta = 130

for venda in vendas:
    if venda < meta:
        # Se a venda for menor que a meta, iremos printar apenas as vendas maiores que 130. Se não for maior, o continue faz com que todo o código antes dele entre em loop novamente e não printa a venda
        continue
    print(venda)