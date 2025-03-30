# Função para verificar se o produto é da categoria bebida, e se for, se há álcool ou não

def eh_da_categoria(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else:
        return False
    

produtos = ['CAR46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

for produto in produtos:
    # Irá analisar cada produto, e se eles começarem com "BEB", a linha será impressa
    # Quando definimos uma variável na função, ele vira uma palavra chave, então podemos fazer isso
    # if eh_da_categoria(cod_categoria = "BEB", bebida = produto):
    if eh_da_categoria(produto, "BEB"):
        print('Enviar {} para setor de bebidas alcóolicas.'.format(produto))
        # O mesmo da anterior, mas se a bebida começar com "BSA"
    # elif eh_da_categoria(cod_categoria = "BSA", bebida = produto)
    elif eh_da_categoria(produto, "BSA"):
        print('Enviar {} para setor de bebidas não alcóolicas.'.format(produto))

# É possível usar o print dessa forma, passando argumentos

# Reparar que, mesmo não dando espaço depois dos dois pontos, o print dá um espaço entre as informações automaticamente
print("Meus produtos são:", produtos)

qtde_produtos = len(produtos)
print("Quantidade de produtos na lista:", qtde_produtos)

# Para mudar o separador do print, de espaço para pular uma linha, fazer o seguinte - sempre com o sep no final:
print("Meus produtos são:", produtos, "Há", qtde_produtos, "produtos nesta lista", sep = "\n")